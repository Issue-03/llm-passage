from __future__ import annotations

from collections.abc import Mapping
from typing import Final

import embrouter
from embrouter import get_llm_provider
from embrouter.rust_bridge import failures
from embrouter.rust_bridge.public_call import inference_decline_reason
from embrouter.rust_bridge.responses.entrypoints import EmbRouterResponsesRequest
from embrouter.types.llms.openai import ResponsesAPIOptionalRequestParams, ResponsesAPIResponse

PARAMETERS: Final = tuple(ResponsesAPIOptionalRequestParams.__annotations__)


def connection_defaults(_provider: str) -> tuple[str | None, str | None]:
    return embrouter.api_key or embrouter.openai_key, embrouter.api_base


def response(value: Mapping[str, object]) -> ResponsesAPIResponse:
    return ResponsesAPIResponse.model_validate(value)


def arguments(request: EmbRouterResponsesRequest) -> Mapping[str, object]:
    return request.kwargs


def map_failure(error: Exception, request: EmbRouterResponsesRequest) -> Exception:
    provider: Final = request.custom_llm_provider or "openai"
    return failures.map_native_failure(error, request.model, provider, arguments(request), request.api_base)


def decline_reason(request: EmbRouterResponsesRequest) -> str | None:
    if request.custom_llm_provider is None and "/" not in request.model:
        try:
            _, provider, _, _ = get_llm_provider(model=request.model)
        except embrouter.exceptions.BadRequestError:
            return "native Responses could not resolve the provider"
        if provider != "openai":
            return "native HTTP responses provider"
    return inference_decline_reason(PARAMETERS, {**request.parameters, **request.kwargs})
