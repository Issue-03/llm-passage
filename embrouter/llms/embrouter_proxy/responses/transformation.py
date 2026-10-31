"""
Responses API transformation for EmbRouter Proxy provider.

EmbRouter Proxy supports the OpenAI Responses API natively when the underlying model supports it.
This config enables pass-through behavior to the proxy's /v1/responses endpoint.
"""

from embrouter.llms.openai.responses.transformation import OpenAIResponsesAPIConfig
from embrouter.secret_managers.main import get_secret_str
from embrouter.types.utils import LlmProviders


class EmbRouterProxyResponsesAPIConfig(OpenAIResponsesAPIConfig):
    """
    Configuration for EmbRouter Proxy Responses API support.

    Extends OpenAI's config since the proxy follows OpenAI's API spec,
    but uses EMBROUTER_PROXY_API_BASE for the base URL.
    """

    @property
    def custom_llm_provider(self) -> LlmProviders:
        return LlmProviders.EMBROUTER_PROXY

    def get_complete_url(
        self,
        api_base: str | None,
        embrouter_params: dict,
    ) -> str:
        """
        Get the endpoint for EmbRouter Proxy responses API.

        Uses EMBROUTER_PROXY_API_BASE environment variable if api_base is not provided.
        """
        api_base = api_base or get_secret_str("EMBROUTER_PROXY_API_BASE")

        if api_base is None:
            raise ValueError(
                "api_base not set for EmbRouter Proxy responses API. "
                "Set via api_base parameter or EMBROUTER_PROXY_API_BASE environment variable"
            )

        # Remove trailing slashes
        api_base = api_base.rstrip("/")

        return f"{api_base}/responses"

    def supports_native_websocket(self) -> bool:
        """EmbRouter Proxy does not support native WebSocket for Responses API"""
        return False
