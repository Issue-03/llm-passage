import pytest

import embrouter
from embrouter.interactions.utils import get_provider_interactions_api_config
from embrouter.llms.gemini.interactions.transformation import (
    GoogleAIStudioInteractionsConfig,
)
from embrouter.llms.vertex_ai.interactions.transformation import (
    VertexAIInteractionsConfig,
)
from embrouter.types.llms.vertex_ai import VERTEX_CREDENTIALS_TYPES
from embrouter.types.router import GenericEmbRouterParams
from embrouter.types.utils import LlmProviders

GLOBAL_BASE = "https://aiplatform.googleapis.com/v1beta1/projects/test-proj/locations/global/interactions"


class MinterRecorder:
    def __init__(self, resolved_project: str = "creds-proj") -> None:
        self.calls: list[tuple[VERTEX_CREDENTIALS_TYPES | None, str | None]] = []
        self.resolved_project = resolved_project

    def __call__(
        self,
        credentials: VERTEX_CREDENTIALS_TYPES | None,
        project_id: str | None,
    ) -> tuple[str, str]:
        self.calls.append((credentials, project_id))
        return "test-token", project_id or self.resolved_project


@pytest.fixture
def minter():
    return MinterRecorder()


@pytest.fixture
def config(minter):
    return VertexAIInteractionsConfig(mint_access_token=minter)


@pytest.fixture
def embrouter_params():
    return GenericEmbRouterParams(vertex_project="test-proj", vertex_credentials="creds.json")


class TestRegistration:
    def test_vertex_ai_returns_vertex_config(self):
        assert isinstance(get_provider_interactions_api_config("vertex_ai"), VertexAIInteractionsConfig)

    def test_vertex_ai_beta_returns_vertex_config(self):
        assert isinstance(get_provider_interactions_api_config("vertex_ai_beta"), VertexAIInteractionsConfig)

    def test_gemini_still_returns_google_ai_studio_config(self):
        gemini_config = get_provider_interactions_api_config("gemini")
        assert isinstance(gemini_config, GoogleAIStudioInteractionsConfig)
        assert not isinstance(gemini_config, VertexAIInteractionsConfig)

    def test_lazy_import_resolves(self):
        assert embrouter.VertexAIInteractionsConfig is VertexAIInteractionsConfig

    def test_custom_llm_provider_is_vertex_ai(self, config):
        assert config.custom_llm_provider == LlmProviders.VERTEX_AI


class TestValidateEnvironment:
    def test_sets_bearer_auth_without_gemini_headers(self, config, minter, embrouter_params):
        headers = config.validate_environment(
            headers={},
            model="gemini-omni-flash-preview",
            embrouter_params=embrouter_params,
        )

        assert headers["Authorization"] == "Bearer test-token"
        assert headers["Content-Type"] == "application/json"
        assert "x-goog-api-key" not in headers
        assert "Api-Revision" not in headers
        assert minter.calls == [("creds.json", "test-proj")]

    def test_caller_authorization_wins(self, config, embrouter_params):
        headers = config.validate_environment(
            headers={"Authorization": "Bearer caller-token"},
            model="gemini-omni-flash-preview",
            embrouter_params=embrouter_params,
        )

        assert headers["Authorization"] == "Bearer caller-token"


class TestGetCompleteUrl:
    def test_defaults_to_global_v1beta1(self, config, embrouter_params):
        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params=dict(embrouter_params),
        )

        assert url == GLOBAL_BASE

    def test_stream_appends_alt_sse(self, config, embrouter_params):
        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params=dict(embrouter_params),
            stream=True,
        )

        assert url == f"{GLOBAL_BASE}?alt=sse"

    def test_multi_region_location_uses_rep_host(self, config):
        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params={"vertex_project": "test-proj", "vertex_location": "us"},
        )

        assert url == "https://aiplatform.us.rep.googleapis.com/v1beta1/projects/test-proj/locations/us/interactions"

    def test_regional_location_uses_regional_host(self, config):
        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params={"vertex_project": "test-proj", "vertex_location": "us-central1"},
        )

        assert url == (
            "https://us-central1-aiplatform.googleapis.com"
            "/v1beta1/projects/test-proj/locations/us-central1/interactions"
        )

    def test_location_env_fallback_is_ignored(self, config, monkeypatch):
        monkeypatch.setenv("VERTEXAI_LOCATION", "us-east5")

        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params={"vertex_project": "test-proj"},
        )

        assert url == GLOBAL_BASE

    def test_api_base_override(self, config, embrouter_params):
        url = config.get_complete_url(
            api_base="https://proxy.example.test",
            model="gemini-omni-flash-preview",
            embrouter_params=dict(embrouter_params),
        )

        assert url == "https://proxy.example.test/v1beta1/projects/test-proj/locations/global/interactions"

    def test_project_resolved_from_credentials_when_not_passed(self, config, monkeypatch):
        monkeypatch.delenv("VERTEXAI_PROJECT", raising=False)
        monkeypatch.setattr(embrouter, "vertex_project", None)

        url = config.get_complete_url(
            api_base=None,
            model="gemini-omni-flash-preview",
            embrouter_params={"vertex_credentials": "creds.json"},
        )

        assert url == "https://aiplatform.googleapis.com/v1beta1/projects/creds-proj/locations/global/interactions"

    def test_invalid_location_rejected(self, config):
        with pytest.raises(ValueError, match="Invalid vertex_location"):
            config.get_complete_url(
                api_base=None,
                model="gemini-omni-flash-preview",
                embrouter_params={"vertex_project": "test-proj", "vertex_location": "evil.com#"},
            )

    def test_missing_project_rejected(self, monkeypatch):
        monkeypatch.delenv("VERTEXAI_PROJECT", raising=False)
        monkeypatch.setattr(embrouter, "vertex_project", None)

        def unresolved_minter(
            credentials: VERTEX_CREDENTIALS_TYPES | None,
            project_id: str | None,
        ) -> tuple[str, str]:
            return "test-token", ""

        with pytest.raises(ValueError, match="Vertex AI project is required"):
            VertexAIInteractionsConfig(mint_access_token=unresolved_minter).get_complete_url(
                api_base=None,
                model="gemini-omni-flash-preview",
                embrouter_params={},
            )


class TestInteractionByIdRequests:
    def test_get_url(self, config, embrouter_params):
        url, request_body = config.transform_get_interaction_request(
            interaction_id="abc123",
            api_base="",
            embrouter_params=embrouter_params,
            headers={},
        )

        assert url == f"{GLOBAL_BASE}/abc123"
        assert request_body == {}

    def test_get_url_encodes_interaction_id(self, config, embrouter_params):
        url, _ = config.transform_get_interaction_request(
            interaction_id="id/with space",
            api_base="",
            embrouter_params=embrouter_params,
            headers={},
        )

        assert url == f"{GLOBAL_BASE}/id%2Fwith%20space"

    def test_delete_url(self, config, embrouter_params):
        url, request_body = config.transform_delete_interaction_request(
            interaction_id="abc123",
            api_base="",
            embrouter_params=embrouter_params,
            headers={},
        )

        assert url == f"{GLOBAL_BASE}/abc123"
        assert request_body == {}

    def test_cancel_url(self, config, embrouter_params):
        url, request_body = config.transform_cancel_interaction_request(
            interaction_id="abc123",
            api_base="",
            embrouter_params=embrouter_params,
            headers={},
        )

        assert url == f"{GLOBAL_BASE}/abc123:cancel"
        assert request_body == {}
