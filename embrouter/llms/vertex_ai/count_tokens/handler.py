from typing import Any, Final

from embrouter.llms.gemini.count_tokens.handler import GoogleAIStudioTokenCounter
from embrouter.llms.vertex_ai.vertex_llm_base import VertexBase


class VertexAITokenCounter(GoogleAIStudioTokenCounter, VertexBase):
    async def validate_environment(
        self,
        api_base: str | None = None,
        api_key: str | None = None,
        headers: dict[str, Any] | None = None,
        model: str = "",
        embrouter_params: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], str]:
        """
        Returns a Tuple of headers and url for the Vertex AI countTokens endpoint.
        """
        embrouter_params = embrouter_params or {}
        vertex_credentials: Final = self.get_vertex_ai_credentials(embrouter_params=embrouter_params)
        vertex_project = self.get_vertex_ai_project(embrouter_params=embrouter_params)
        vertex_location: Final = self.get_vertex_ai_location(embrouter_params=embrouter_params)
        _auth_header, vertex_project = await self._ensure_access_token_async(
            credentials=vertex_credentials,
            project_id=vertex_project,
            custom_llm_provider="vertex_ai",
        )

        auth_header, api_base = self._get_token_and_url(
            model=model,
            gemini_api_key=None,
            auth_header=_auth_header,
            vertex_project=vertex_project,
            vertex_location=vertex_location,
            vertex_credentials=vertex_credentials,
            stream=False,
            custom_llm_provider="vertex_ai",
            api_base=None,
            mode="count_tokens",
        )
        headers = {
            "Authorization": f"Bearer {auth_header}",
        }
        return headers, api_base
