from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock, patch

import pytest

import embrouter
from embrouter.images.utils import ImageEditRequestUtils
from embrouter.embrouter_core_utils.embrouter_logging import use_custom_pricing_for_model
from embrouter.llms.base_llm.image_edit.transformation import BaseImageEditConfig
from embrouter.types.images.main import ImageEditOptionalRequestParams


class MockImageEditConfig(BaseImageEditConfig):
    def get_supported_openai_params(self, model: str) -> List[str]:
        return ["size", "quality"]

    def map_openai_params(
        self,
        image_edit_optional_params: ImageEditOptionalRequestParams,
        model: str,
        drop_params: bool,
    ) -> Dict[str, Any]:
        return dict(image_edit_optional_params)

    def get_complete_url(self, model: str, api_base: str, embrouter_params: dict) -> str:
        return "https://example.com/api"

    def validate_environment(
        self,
        headers: dict,
        model: str,
        api_key: Optional[str] = None,
        embrouter_params: Optional[dict] = None,
        api_base: Optional[str] = None,
    ) -> dict:
        return headers

    def transform_image_edit_request(self, *args, **kwargs):
        return {}, []

    def transform_image_edit_response(self, *args, **kwargs):
        return MagicMock()


class TestImageEditRequestUtilsDropParams:
    def setup_method(self):
        self.config = MockImageEditConfig()
        self.model = "test-model"
        self._original_drop_params = getattr(embrouter, "drop_params", None)

    def teardown_method(self):
        if self._original_drop_params is None:
            if hasattr(embrouter, "drop_params"):
                delattr(embrouter, "drop_params")
        else:
            embrouter.drop_params = self._original_drop_params

    def test_unsupported_params_raises_without_drop(self):
        embrouter.drop_params = False
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "unsupported_param": "value",
        }

        with pytest.raises(embrouter.UnsupportedParamsError) as exc_info:
            ImageEditRequestUtils.get_optional_params_image_edit(
                model=self.model,
                image_edit_provider_config=self.config,
                image_edit_optional_params=optional_params,
            )

        assert "unsupported_param" in str(exc_info.value)

    def test_drop_params_global_setting(self):
        embrouter.drop_params = True
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "unsupported_param": "value",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
        )

        assert "size" in result
        assert "unsupported_param" not in result

    def test_drop_params_explicit_parameter(self):
        embrouter.drop_params = False
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "unsupported_param": "value",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
            drop_params=True,
        )

        assert "size" in result
        assert "unsupported_param" not in result

    def test_additional_drop_params(self):
        embrouter.drop_params = False
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "quality": "high",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
            additional_drop_params=["quality"],
        )

        assert "size" in result
        assert "quality" not in result

    def test_drop_params_false_with_global_true(self):
        embrouter.drop_params = True
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "unsupported_param": "value",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
            drop_params=False,
        )

        assert "size" in result
        assert "unsupported_param" not in result

    def test_supported_params_pass_through(self):
        embrouter.drop_params = False
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "quality": "high",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
        )

        assert result["size"] == "1024x1024"
        assert result["quality"] == "high"

    def test_additional_drop_params_with_unsupported_and_drop_true(self):
        embrouter.drop_params = True
        optional_params: ImageEditOptionalRequestParams = {
            "size": "1024x1024",
            "quality": "high",
            "unsupported_param": "value",
        }

        result = ImageEditRequestUtils.get_optional_params_image_edit(
            model=self.model,
            image_edit_provider_config=self.config,
            image_edit_optional_params=optional_params,
            additional_drop_params=["quality"],
        )

        assert "size" in result
        assert "quality" not in result
        assert "unsupported_param" not in result


class TestImageEditCustomPricing:
    """


    image_edit must forward model_info and metadata into embrouter_params
    when calling update_environment_variables, so that custom pricing
    detection works after PR #20679 stripped custom pricing fields from
    the shared backend model key.
    """

    def test_image_edit_passes_model_info_to_logging(self):
        """
        When the router provides model_info with custom pricing fields,
        image_edit should include model_info and metadata in embrouter_params.
        """
        from embrouter.images.main import image_edit

        custom_model_info = {
            "id": "test-deployment-id",
            "input_cost_per_image": 0.00676128,
            "mode": "image_generation",
        }
        custom_metadata = {
            "model_info": custom_model_info,
        }

        captured_embrouter_params = {}

        mock_logging_obj = MagicMock()
        mock_logging_obj.model_call_details = {}

        original_update = mock_logging_obj.update_from_kwargs

        def capturing_update(**update_kwargs):
            captured_embrouter_params.update(update_kwargs.get("embrouter_params", {}))
            inner_kwargs = update_kwargs.get("kwargs", {})
            if "metadata" in inner_kwargs:
                captured_embrouter_params["metadata"] = inner_kwargs["metadata"]
            return original_update(**update_kwargs)

        mock_logging_obj.update_from_kwargs = capturing_update

        with (
            patch(
                "embrouter.images.main.get_llm_provider",
                return_value=("test-model", "openai", None, None),
            ),
            patch(
                "embrouter.images.main.ProviderConfigManager.get_provider_image_edit_config",
                return_value=MagicMock(),
            ),
            patch(
                "embrouter.images.main._get_ImageEditRequestUtils",
                return_value=MagicMock(
                    get_requested_image_edit_optional_param=MagicMock(return_value={}),
                    get_optional_params_image_edit=MagicMock(return_value={}),
                ),
            ),
            patch("embrouter.images.main.base_llm_http_handler") as mock_handler,
        ):
            mock_handler.image_edit_handler.return_value = MagicMock()

            try:
                image_edit(
                    image=b"fake-image-data",
                    prompt="test prompt",
                    model="openai/test-model",
                    embrouter_logging_obj=mock_logging_obj,
                    model_info=custom_model_info,
                    metadata=custom_metadata,
                )
            except Exception:
                pass

        assert "model_info" in captured_embrouter_params
        assert captured_embrouter_params["model_info"] == custom_model_info
        assert "metadata" in captured_embrouter_params
        assert captured_embrouter_params["metadata"] == custom_metadata

    def test_custom_pricing_detected_from_model_info_in_metadata(self):
        embrouter_params = {
            "metadata": {
                "model_info": {
                    "id": "deployment-id",
                    "input_cost_per_image": 0.00676128,
                },
            },
        }
        assert use_custom_pricing_for_model(embrouter_params) is True

    def test_custom_pricing_not_detected_without_model_info(self):
        embrouter_params = {"embrouter_call_id": "test-call-id"}
        assert use_custom_pricing_for_model(embrouter_params) is False


class TestImageEditHandlerCredentialsForwarding:
    """
    Regression tests for Vertex AI image_edit credentials bug.

    image_edit handler must forward embrouter_params to validate_environment,
    so that credentials passed via YAML config (vertex_ai_project,
    vertex_ai_credentials, etc.) reach the auth layer instead of falling
    through to Application Default Credentials.
    """

    def test_vertex_gemini_image_edit_reads_credentials_from_embrouter_params(self):
        """
        VertexAIGeminiImageEditConfig.validate_environment should read
        vertex_ai_project/vertex_ai_credentials from embrouter_params first.
        """
        from embrouter.llms.vertex_ai.image_edit.vertex_gemini_transformation import (
            VertexAIGeminiImageEditConfig,
        )

        config = VertexAIGeminiImageEditConfig()

        embrouter_params = {
            "vertex_ai_project": "test-project-from-params",
            "vertex_ai_credentials": "/path/to/creds.json",
        }

        with patch.object(
            config, "_ensure_access_token", return_value=("token", "project")
        ) as mock_ensure:
            config.validate_environment(
                headers={},
                model="test-model",
                embrouter_params=embrouter_params,
            )

            mock_ensure.assert_called_once()
            call_kwargs = mock_ensure.call_args[1]

            assert call_kwargs["credentials"] == "/path/to/creds.json"
            assert call_kwargs["project_id"] == "test-project-from-params"

    def test_vertex_imagen_image_edit_reads_credentials_from_embrouter_params(self):
        """
        VertexAIImagenImageEditConfig.validate_environment should read
        vertex_ai_project/vertex_ai_credentials from embrouter_params first.
        """
        from embrouter.llms.vertex_ai.image_edit.vertex_imagen_transformation import (
            VertexAIImagenImageEditConfig,
        )

        config = VertexAIImagenImageEditConfig()

        embrouter_params = {
            "vertex_ai_project": "test-project-from-params",
            "vertex_ai_credentials": "/path/to/creds.json",
        }

        with patch.object(
            config, "_ensure_access_token", return_value=("token", "project")
        ) as mock_ensure:
            config.validate_environment(
                headers={},
                model="test-model",
                embrouter_params=embrouter_params,
            )

            mock_ensure.assert_called_once()
            call_kwargs = mock_ensure.call_args[1]

            assert call_kwargs["credentials"] == "/path/to/creds.json"
            assert call_kwargs["project_id"] == "test-project-from-params"

    def test_vertex_imagen_get_complete_url_reads_project_and_location_from_embrouter_params(
        self,
    ):
        """
        VertexAIImagenImageEditConfig.get_complete_url should read
        vertex_ai_project and vertex_ai_location from embrouter_params,
        not only from env vars / global settings.
        """
        from embrouter.llms.vertex_ai.image_edit.vertex_imagen_transformation import (
            VertexAIImagenImageEditConfig,
        )

        config = VertexAIImagenImageEditConfig()

        embrouter_params = {
            "vertex_ai_project": "param-project",
            "vertex_ai_location": "us-east1",
        }

        url = config.get_complete_url(
            model="vertex_ai/imagegeneration@002",
            api_base=None,
            embrouter_params=embrouter_params,
        )

        assert "param-project" in url
        assert "us-east1" in url

    def test_validate_environment_signature_includes_embrouter_params(self):
        """
        All image_edit config validate_environment methods should accept
        embrouter_params to allow credentials to be forwarded from the handler.
        """
        import inspect

        from embrouter.llms.vertex_ai.image_edit.vertex_gemini_transformation import (
            VertexAIGeminiImageEditConfig,
        )
        from embrouter.llms.vertex_ai.image_edit.vertex_imagen_transformation import (
            VertexAIImagenImageEditConfig,
        )
        from embrouter.llms.openai.image_edit.transformation import (
            OpenAIImageEditConfig,
        )

        configs = [
            VertexAIGeminiImageEditConfig(),
            VertexAIImagenImageEditConfig(),
            OpenAIImageEditConfig(),
            MockImageEditConfig(),
        ]

        for config in configs:
            sig = inspect.signature(config.validate_environment)
            params = list(sig.parameters.keys())

            assert "embrouter_params" in params, (
                f"{config.__class__.__name__}.validate_environment "
                "missing embrouter_params parameter"
            )
            assert "api_base" in params, (
                f"{config.__class__.__name__}.validate_environment "
                "missing api_base parameter"
            )
