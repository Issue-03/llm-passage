"""
OpenRouter Responses API Configuration.

OpenRouter supports the Responses API at https://openrouter.ai/api/v1/responses
with OpenAI-compatible request/response format, including reasoning with
encrypted_content for multi-turn stateless workflows.

Docs: https://openrouter.ai/docs/api/reference/responses/overview
"""

from typing import Final

import embrouter
from embrouter.llms.openai.responses.transformation import OpenAIResponsesAPIConfig
from embrouter.secret_managers.main import get_secret_str
from embrouter.types.router import GenericEmbRouterParams
from embrouter.types.utils import LlmProviders


class OpenRouterResponsesAPIConfig(OpenAIResponsesAPIConfig):
    """
    Configuration for OpenRouter's Responses API.

    Inherits from OpenAIResponsesAPIConfig since OpenRouter's Responses API
    is compatible with OpenAI's Responses API specification.

    Key difference from direct OpenAI:
    - Uses https://openrouter.ai/api/v1 as the API base
    - Uses OPENROUTER_API_KEY for authentication
    """

    @property
    def custom_llm_provider(self) -> LlmProviders:
        return LlmProviders.OPENROUTER

    def validate_environment(
        self,
        headers: dict,
        model: str,
        embrouter_params: GenericEmbRouterParams | None,
    ) -> dict:
        embrouter_params = embrouter_params or GenericEmbRouterParams()
        api_key: Final = (
            embrouter_params.api_key
            or embrouter.api_key
            or get_secret_str("OPENROUTER_API_KEY")
            or get_secret_str("OR_API_KEY")
        )

        if not api_key:
            raise ValueError(
                "OpenRouter API key is required. Set OPENROUTER_API_KEY environment variable or pass api_key parameter."
            )

        headers.update(
            {
                "Authorization": f"Bearer {api_key}",
            }
        )
        return headers

    def get_complete_url(
        self,
        api_base: str | None,
        embrouter_params: dict,
    ) -> str:
        api_base = (
            api_base or embrouter.api_base or get_secret_str("OPENROUTER_API_BASE") or "https://openrouter.ai/api/v1"
        )

        api_base = api_base.rstrip("/")

        return f"{api_base}/responses"

    def supports_native_websocket(self) -> bool:
        """OpenRouter does not support native WebSocket for Responses API"""
        return False
