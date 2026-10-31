import re
from datetime import datetime
from typing import TYPE_CHECKING, Any, Final

import httpx

import embrouter
from embrouter._logging import verbose_proxy_logger
from embrouter.embrouter_core_utils.embrouter_logging import Logging as EmbRouterLoggingObj
from embrouter.llms.gemini.videos.transformation import GeminiVideoConfig
from embrouter.llms.vertex_ai.gemini.vertex_and_google_ai_studio_gemini import (
    ModelResponseIterator as GeminiModelResponseIterator,
)
from embrouter.proxy._types import PassThroughEndpointLoggingTypedDict
from embrouter.proxy.pass_through_endpoints.llm_provider_handlers.vertex_passthrough_logging_handler import (
    VertexPassthroughLoggingHandler,
)
from embrouter.types.utils import (
    ModelResponse,
    TextCompletionResponse,
)

if TYPE_CHECKING:
    from embrouter.types.passthrough_endpoints.pass_through_endpoints import EndpointType

    from ..success_handler import PassThroughEndpointLogging
else:
    PassThroughEndpointLogging = Any
    EndpointType = Any


class GeminiPassthroughLoggingHandler:
    @staticmethod
    def gemini_passthrough_handler(
        httpx_response: httpx.Response,
        response_body: dict,
        logging_obj: EmbRouterLoggingObj,
        url_route: str,
        result: str,
        start_time: datetime,
        end_time: datetime,
        cache_hit: bool,
        request_body: dict,
        **kwargs,
    ) -> PassThroughEndpointLoggingTypedDict:
        if VertexPassthroughLoggingHandler.is_interactions_route(url_route):
            return VertexPassthroughLoggingHandler.interactions_passthrough_handler(
                httpx_response=httpx_response,
                request_body=request_body,
                logging_obj=logging_obj,
                kwargs=kwargs,
                start_time=start_time,
                end_time=end_time,
                custom_llm_provider="gemini",
                vertex_location=None,
            )
        if "predictLongRunning" in url_route:
            model = GeminiPassthroughLoggingHandler.extract_model_from_url(url_route)

            gemini_video_config: Final = GeminiVideoConfig()
            embrouter_video_response: Final = gemini_video_config.transform_video_create_response(
                model=model,
                raw_response=httpx_response,
                logging_obj=logging_obj,
                custom_llm_provider="gemini",
                request_data=request_body,
            )
            logging_obj.model = model
            logging_obj.model_call_details["model"] = model
            logging_obj.model_call_details["custom_llm_provider"] = "gemini"
            logging_obj.custom_llm_provider = "gemini"

            response_cost: Final = embrouter.completion_cost(
                completion_response=embrouter_video_response,
                model=model,
                custom_llm_provider="gemini",
                call_type="create_video",
            )

            # Set response_cost in _hidden_params to prevent recalculation
            if not hasattr(embrouter_video_response, "_hidden_params"):
                embrouter_video_response._hidden_params = {}
            embrouter_video_response._hidden_params["response_cost"] = response_cost

            kwargs["response_cost"] = response_cost
            kwargs["model"] = model
            kwargs["custom_llm_provider"] = "gemini"
            logging_obj.model_call_details["response_cost"] = response_cost
            return {
                "result": embrouter_video_response,
                "kwargs": kwargs,
            }

        if "generateContent" in url_route:
            model = GeminiPassthroughLoggingHandler.extract_model_from_url(url_route)

            # Use Gemini config for transformation
            instance_of_gemini_llm: Final = embrouter.GoogleAIStudioGeminiConfig()
            embrouter_model_response: Final[ModelResponse] = instance_of_gemini_llm.transform_response(
                model=model,
                messages=[{"role": "user", "content": "no-message-pass-through-endpoint"}],
                raw_response=httpx_response,
                model_response=embrouter.ModelResponse(),
                logging_obj=logging_obj,
                optional_params={},
                embrouter_params={},
                api_key="",
                request_data={},
                encoding=getattr(embrouter, "encoding", None),
            )
            kwargs = GeminiPassthroughLoggingHandler._create_gemini_response_logging_payload_for_generate_content(
                embrouter_model_response=embrouter_model_response,
                model=model,
                kwargs=kwargs,
                start_time=start_time,
                end_time=end_time,
                logging_obj=logging_obj,
                custom_llm_provider="gemini",
            )

            return {
                "result": embrouter_model_response,
                "kwargs": kwargs,
            }
        else:
            return {
                "result": None,
                "kwargs": kwargs,
            }

    @staticmethod
    def _handle_logging_gemini_collected_chunks(
        embrouter_logging_obj: EmbRouterLoggingObj,
        passthrough_success_handler_obj: PassThroughEndpointLogging,
        url_route: str,
        request_body: dict,
        endpoint_type: EndpointType,
        start_time: datetime,
        all_chunks: list[str],
        model: str | None,
        end_time: datetime,
    ) -> PassThroughEndpointLoggingTypedDict:
        """
        Takes raw chunks from Gemini passthrough endpoint and logs them in embrouter callbacks

        - Builds complete response from chunks
        - Creates standard logging object
        - Logs in embrouter callbacks
        """
        kwargs: dict[str, object] = {}
        model = model or GeminiPassthroughLoggingHandler.extract_model_from_url(url_route)
        complete_streaming_response: Final = GeminiPassthroughLoggingHandler._build_complete_streaming_response(
            all_chunks=all_chunks,
            embrouter_logging_obj=embrouter_logging_obj,
            model=model,
            url_route=url_route,
        )

        if complete_streaming_response is None:
            verbose_proxy_logger.error(
                "Unable to build complete streaming response for Gemini passthrough endpoint, not logging..."
            )
            return {
                "result": None,
                "kwargs": kwargs,
            }

        kwargs = GeminiPassthroughLoggingHandler._create_gemini_response_logging_payload_for_generate_content(
            embrouter_model_response=complete_streaming_response,
            model=model,
            kwargs=kwargs,
            start_time=start_time,
            end_time=end_time,
            logging_obj=embrouter_logging_obj,
            custom_llm_provider="gemini",
        )

        return {
            "result": complete_streaming_response,
            "kwargs": kwargs,
        }

    @staticmethod
    def _build_complete_streaming_response(
        all_chunks: list[str],
        embrouter_logging_obj: EmbRouterLoggingObj,
        model: str,
        url_route: str,
    ) -> ModelResponse | TextCompletionResponse | None:
        parsed_chunks = []
        if "generateContent" in url_route or "streamGenerateContent" in url_route:
            gemini_iterator: Final[Any] = GeminiModelResponseIterator(
                streaming_response=None,
                sync_stream=False,
                logging_obj=embrouter_logging_obj,
            )
            chunk_parsing_logic: Final[Any] = gemini_iterator._common_chunk_parsing_logic
            parsed_chunks = [chunk_parsing_logic(chunk) for chunk in all_chunks]
        else:
            return None

        if len(parsed_chunks) == 0:
            return None

        all_openai_chunks: Final = []
        for parsed_chunk in parsed_chunks:
            if parsed_chunk is None:
                continue
            all_openai_chunks.append(parsed_chunk)

        complete_streaming_response: Final = embrouter.stream_chunk_builder(chunks=all_openai_chunks)

        return complete_streaming_response

    @staticmethod
    def extract_model_from_url(url: str) -> str:
        pattern: Final = r"/models/([^:]+)"
        match: Final = re.search(pattern, url)
        if match:
            return match.group(1)
        return "unknown"

    @staticmethod
    def _create_gemini_response_logging_payload_for_generate_content(
        embrouter_model_response: ModelResponse | TextCompletionResponse,
        model: str,
        kwargs: dict,
        start_time: datetime,
        end_time: datetime,
        logging_obj: EmbRouterLoggingObj,
        custom_llm_provider: str,
    ):
        """
        Create the standard logging object for Gemini passthrough generateContent (streaming and non-streaming)
        """

        response_cost: Final = embrouter.completion_cost(
            completion_response=embrouter_model_response,
            model=model,
            custom_llm_provider="gemini",
        )

        kwargs["response_cost"] = response_cost
        kwargs["model"] = model
        kwargs["custom_llm_provider"] = custom_llm_provider

        # pretty print standard logging object
        verbose_proxy_logger.debug("kwargs= %s", kwargs)

        # set embrouter_call_id to logging response object
        embrouter_model_response.id = logging_obj.embrouter_call_id
        logging_obj.model = embrouter_model_response.model or model
        logging_obj.model_call_details["model"] = logging_obj.model
        logging_obj.model_call_details["custom_llm_provider"] = custom_llm_provider
        logging_obj.model_call_details["response_cost"] = response_cost
        return kwargs
