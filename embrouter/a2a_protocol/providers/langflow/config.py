from collections.abc import AsyncIterator
from typing import Any

from embrouter.a2a_protocol.embrouter_completion_bridge.handler import (
    A2A_USER_API_KEY_HASH_PARAM,
    A2ACompletionBridgeHandler,
)
from embrouter.a2a_protocol.providers.base import BaseA2AProviderConfig
from embrouter.llms.langflow.a2a import merge_a2a_session_into_embrouter_params


class LangFlowA2AConfig(BaseA2AProviderConfig):
    """A2A bridge for LangFlow: scopes contextId to the authenticated key as the
    LangFlow session_id, then uses completion."""

    async def handle_non_streaming(
        self,
        request_id: str,
        params: dict[str, Any],
        api_base: str | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        embrouter_params = kwargs.get("embrouter_params")
        if not embrouter_params:
            raise ValueError(
                "embrouter_params is required for LangFlowA2AConfig (must contain custom_llm_provider and model)"
            )
        embrouter_params = merge_a2a_session_into_embrouter_params(
            embrouter_params, params, embrouter_params.get(A2A_USER_API_KEY_HASH_PARAM)
        )
        return await A2ACompletionBridgeHandler.handle_non_streaming(
            request_id=request_id,
            params=params,
            embrouter_params=embrouter_params,
            api_base=api_base,
            _skip_a2a_provider_routing=True,
        )

    async def handle_streaming(
        self,
        request_id: str,
        params: dict[str, Any],
        api_base: str | None = None,
        **kwargs,
    ) -> AsyncIterator[dict[str, Any]]:
        embrouter_params = kwargs.get("embrouter_params")
        if not embrouter_params:
            raise ValueError(
                "embrouter_params is required for LangFlowA2AConfig (must contain custom_llm_provider and model)"
            )
        embrouter_params = merge_a2a_session_into_embrouter_params(
            embrouter_params, params, embrouter_params.get(A2A_USER_API_KEY_HASH_PARAM)
        )
        async for chunk in A2ACompletionBridgeHandler.handle_streaming(
            request_id=request_id,
            params=params,
            embrouter_params=embrouter_params,
            api_base=api_base,
            _skip_a2a_provider_routing=True,
        ):
            yield chunk
