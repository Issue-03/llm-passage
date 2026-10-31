"""
Handler for transforming /chat/completions api requests to embrouter.responses requests
"""

from typing import TYPE_CHECKING, Final

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from embrouter import EmbRouterLoggingObj
    from embrouter.types.llms.openai import HttpxBinaryResponseContent


class SpeechToCompletionBridgeHandlerInputKwargs(TypedDict):
    model: str
    input: str
    voice: str | dict | None
    optional_params: dict
    embrouter_params: dict
    logging_obj: "EmbRouterLoggingObj"
    headers: dict
    custom_llm_provider: str


class SpeechToCompletionBridgeHandler:
    def __init__(self):
        from .transformation import SpeechToCompletionBridgeTransformationHandler

        super().__init__()
        self.transformation_handler = SpeechToCompletionBridgeTransformationHandler()

    def validate_input_kwargs(self, kwargs: dict) -> SpeechToCompletionBridgeHandlerInputKwargs:
        from embrouter import EmbRouterLoggingObj

        model: Final = kwargs.get("model")
        if model is None or not isinstance(model, str):
            raise ValueError("model is required")

        custom_llm_provider: Final = kwargs.get("custom_llm_provider")
        if custom_llm_provider is None or not isinstance(custom_llm_provider, str):
            raise ValueError("custom_llm_provider is required")

        input: Final = kwargs.get("input")
        if input is None or not isinstance(input, str):
            raise ValueError("input is required")

        optional_params: Final = kwargs.get("optional_params")
        if optional_params is None or not isinstance(optional_params, dict):
            raise ValueError("optional_params is required")

        embrouter_params: Final = kwargs.get("embrouter_params")
        if embrouter_params is None or not isinstance(embrouter_params, dict):
            raise ValueError("embrouter_params is required")

        headers = kwargs.get("headers")
        if headers is None or not isinstance(headers, dict):
            raise ValueError("headers is required")

        headers = kwargs.get("headers")
        if headers is None or not isinstance(headers, dict):
            raise ValueError("headers is required")

        logging_obj: Final = kwargs.get("logging_obj")
        if logging_obj is None or not isinstance(logging_obj, EmbRouterLoggingObj):
            raise ValueError("logging_obj is required")

        return SpeechToCompletionBridgeHandlerInputKwargs(
            model=model,
            input=input,
            voice=kwargs.get("voice"),
            optional_params=optional_params,
            embrouter_params=embrouter_params,
            logging_obj=logging_obj,
            custom_llm_provider=custom_llm_provider,
            headers=headers,
        )

    def speech(
        self,
        model: str,
        input: str,
        voice: str | dict | None,
        optional_params: dict,
        embrouter_params: dict,
        headers: dict,
        logging_obj: "EmbRouterLoggingObj",
        custom_llm_provider: str,
    ) -> "HttpxBinaryResponseContent":
        received_args: Final = locals()
        from embrouter import completion
        from embrouter.types.utils import ModelResponse

        validated_kwargs: Final = self.validate_input_kwargs(received_args)
        model = validated_kwargs["model"]
        input = validated_kwargs["input"]
        optional_params = validated_kwargs["optional_params"]
        embrouter_params = validated_kwargs["embrouter_params"]
        headers = validated_kwargs["headers"]
        logging_obj = validated_kwargs["logging_obj"]
        custom_llm_provider = validated_kwargs["custom_llm_provider"]
        voice = validated_kwargs["voice"]

        request_data: Final = self.transformation_handler.transform_request(
            model=model,
            input=input,
            optional_params=optional_params,
            embrouter_params=embrouter_params,
            headers=headers,
            embrouter_logging_obj=logging_obj,
            custom_llm_provider=custom_llm_provider,
            voice=voice,
        )

        result: Final = completion(
            **request_data,
        )

        requested_response_format: Final = optional_params.get("response_format")
        if isinstance(result, ModelResponse):
            return self.transformation_handler.transform_response(
                model_response=result,
                response_format=requested_response_format if isinstance(requested_response_format, str) else None,
            )
        else:
            raise Exception(f"Unmapped response type. Got type: {type(result)}")


speech_to_completion_bridge_handler = SpeechToCompletionBridgeHandler()
