"""
Handler for transforming responses api requests to embrouter.completion requests
"""

from collections.abc import Coroutine, Mapping
from typing import Final

import embrouter
from embrouter.responses.additional_tools import hoist_additional_tools
from embrouter.responses.embrouter_completion_transformation.streaming_iterator import (
    EmbRouterCompletionStreamingIterator,
)
from embrouter.responses.embrouter_completion_transformation.transformation import (
    EmbRouterCompletionResponsesConfig,
)
from embrouter.responses.streaming_iterator import BaseResponsesAPIStreamingIterator
from embrouter.types.llms.openai import (
    ResponseInputParam,
    ResponsesAPIOptionalRequestParams,
    ResponsesAPIResponse,
)
from embrouter.types.utils import ModelResponse


class EmbRouterCompletionTransformationHandler:
    def response_api_handler(
        self,
        model: str,
        input: str | ResponseInputParam,
        responses_api_request: ResponsesAPIOptionalRequestParams,
        custom_llm_provider: str | None = None,
        _is_async: bool = False,
        stream: bool | None = None,
        extra_headers: Mapping[str, object] | None = None,
        **kwargs,
    ) -> (
        ResponsesAPIResponse
        | BaseResponsesAPIStreamingIterator
        | Coroutine[object, object, ResponsesAPIResponse | BaseResponsesAPIStreamingIterator]
    ):
        hoisted: Final = hoist_additional_tools(input, responses_api_request.get("tools"))
        bridged_input: Final = hoisted.input
        bridged_request: Final[ResponsesAPIOptionalRequestParams] = (
            {**responses_api_request, "tools": list(hoisted.tools)} if hoisted.hoisted else responses_api_request
        )
        embrouter_completion_request: Final[dict] = (
            EmbRouterCompletionResponsesConfig.transform_responses_api_request_to_chat_completion_request(
                model=model,
                input=bridged_input,
                responses_api_request=bridged_request,
                custom_llm_provider=custom_llm_provider,
                stream=stream,
                extra_headers=extra_headers,
                **kwargs,
            )
        )

        if _is_async:
            return self.async_response_api_handler(
                embrouter_completion_request=embrouter_completion_request,
                request_input=bridged_input,
                responses_api_request=bridged_request,
                **kwargs,
            )

        completion_args: Final = {}
        completion_args.update(kwargs)
        completion_args.update(embrouter_completion_request)
        completion_args["_skip_responses_api_bridge"] = True

        embrouter_completion_response: Final[ModelResponse | embrouter.CustomStreamWrapper] = embrouter.completion(
            **completion_args,
        )

        if isinstance(embrouter_completion_response, ModelResponse):
            responses_api_response: Final[ResponsesAPIResponse] = (
                EmbRouterCompletionResponsesConfig.transform_chat_completion_response_to_responses_api_response(
                    chat_completion_response=embrouter_completion_response,
                    request_input=bridged_input,
                    responses_api_request=bridged_request,
                )
            )

            return responses_api_response

        elif isinstance(embrouter_completion_response, embrouter.CustomStreamWrapper):
            return EmbRouterCompletionStreamingIterator(
                model=model,
                embrouter_custom_stream_wrapper=embrouter_completion_response,
                request_input=bridged_input,
                responses_api_request=bridged_request,
                custom_llm_provider=custom_llm_provider,
                embrouter_metadata=kwargs.get("embrouter_metadata", {}),
            )
        raise ValueError(f"Unexpected response type: {type(embrouter_completion_response)}")

    async def async_response_api_handler(
        self,
        embrouter_completion_request: dict,
        request_input: str | ResponseInputParam,
        responses_api_request: ResponsesAPIOptionalRequestParams,
        **kwargs,
    ) -> ResponsesAPIResponse | BaseResponsesAPIStreamingIterator:
        previous_response_id: Final[str | None] = responses_api_request.get("previous_response_id")
        if previous_response_id:
            embrouter_completion_request = await EmbRouterCompletionResponsesConfig.async_responses_api_session_handler(
                previous_response_id=previous_response_id,
                embrouter_completion_request=embrouter_completion_request,
            )

        acompletion_args: Final = {}
        acompletion_args.update(kwargs)
        acompletion_args.update(embrouter_completion_request)
        acompletion_args["_skip_responses_api_bridge"] = True

        embrouter_completion_response: Final[ModelResponse | embrouter.CustomStreamWrapper] = await embrouter.acompletion(
            **acompletion_args,
        )

        if isinstance(embrouter_completion_response, ModelResponse):
            responses_api_response: Final[ResponsesAPIResponse] = (
                EmbRouterCompletionResponsesConfig.transform_chat_completion_response_to_responses_api_response(
                    chat_completion_response=embrouter_completion_response,
                    request_input=request_input,
                    responses_api_request=responses_api_request,
                )
            )

            return responses_api_response

        elif isinstance(embrouter_completion_response, embrouter.CustomStreamWrapper):
            return EmbRouterCompletionStreamingIterator(
                model=embrouter_completion_request.get("model") or "",
                embrouter_custom_stream_wrapper=embrouter_completion_response,
                request_input=request_input,
                responses_api_request=responses_api_request,
                custom_llm_provider=embrouter_completion_request.get("custom_llm_provider"),
                embrouter_metadata=kwargs.get("embrouter_metadata", {}),
            )
        raise ValueError(f"Unexpected response type: {type(embrouter_completion_response)}")
