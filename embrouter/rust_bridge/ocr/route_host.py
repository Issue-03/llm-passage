from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from pydantic import TypeAdapter

import embrouter
from embrouter.llms.base_llm.ocr.transformation import PROVIDER_NATIVE_RESPONSE_KEY, OCRResponse
from embrouter.rust_bridge import failures
from embrouter.rust_bridge.failures import UpstreamFailure
from embrouter.rust_bridge.ocr.entrypoints import EmbRouterOcrRequest

__all__ = ("UpstreamFailure", "arguments", "map_failure", "response")

_RESPONSE_ADAPTER: Final = TypeAdapter(dict[str, object])


def response(value: Mapping[str, object]) -> OCRResponse:
    provider_native_response: Final = value.get(PROVIDER_NATIVE_RESPONSE_KEY)
    normalized: Final = OCRResponse.model_validate(
        MappingProxyType({key: item for key, item in value.items() if key != PROVIDER_NATIVE_RESPONSE_KEY})
    )
    if isinstance(provider_native_response, Mapping):
        normalized.set_provider_native_response(_RESPONSE_ADAPTER.validate_python(provider_native_response))
    return normalized


def arguments(request: EmbRouterOcrRequest) -> Mapping[str, object]:
    return request.kwargs


def map_failure(error: Exception, request: EmbRouterOcrRequest, request_provider: str) -> Exception:
    if getattr(error, "ocr_request_format_error", False):
        return embrouter.UnsupportedParamsError(
            message=f"Invalid `req_format`: {request.kwargs.get('req_format')!r}. Expected 'native' or 'embrouter'.",
            model=request.model.removeprefix(f"{request_provider}/"),
            llm_provider=request_provider,
        )
    return failures.map_native_failure(error, request.model, request_provider, arguments(request), request.api_base)
