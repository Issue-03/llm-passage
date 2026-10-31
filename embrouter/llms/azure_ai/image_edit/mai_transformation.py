from typing import TYPE_CHECKING, Any, Final

import httpx
from httpx._types import RequestFiles

from embrouter.llms.azure_ai.common_utils import (
    AzureFoundryModelInfo,
    get_azure_ai_auth_headers,
)
from embrouter.llms.azure_ai.image_generation.mai_transformation import (
    AzureFoundryMAIImageGenerationConfig,
)
from embrouter.llms.openai.common_utils import OpenAIError
from embrouter.llms.openai.image_edit.transformation import OpenAIImageEditConfig
from embrouter.secret_managers.main import get_secret_str
from embrouter.types.llms.openai import FileTypes
from embrouter.types.router import GenericEmbRouterParams
from embrouter.types.utils import ImageResponse
from embrouter.utils import convert_to_model_response_object

if TYPE_CHECKING:
    from embrouter.embrouter_core_utils.logging import Logging as EmbRouterLoggingObj


class AzureFoundryMAIImageEditConfig(OpenAIImageEditConfig):
    """Azure AI Foundry MAI image editing (e.g. MAI-Image-2.5)."""

    def get_supported_openai_params(self, model: str) -> list:
        return ["prompt", "image", "model", "n"]

    def validate_environment(
        self,
        headers: dict,
        model: str,
        api_key: str | None = None,
        embrouter_params: dict | None = None,
        api_base: str | None = None,
    ) -> dict:
        headers.update(
            get_azure_ai_auth_headers(
                api_key=AzureFoundryModelInfo.get_api_key(api_key),
                embrouter_params=embrouter_params,
                api_key_header="api-key",
            )
        )
        return headers

    def get_complete_url(
        self,
        model: str,
        api_base: str | None,
        embrouter_params: dict,
    ) -> str:
        api_base = AzureFoundryModelInfo.get_api_base(api_base)

        if api_base is None:
            raise ValueError(
                "Azure AI API base is required. Set AZURE_AI_API_BASE environment variable or pass api_base parameter."
            )

        api_version: Final = embrouter_params.get("api_version") or get_secret_str("AZURE_AI_API_VERSION") or "preview"

        return AzureFoundryMAIImageGenerationConfig.get_mai_image_edit_url(
            api_base=api_base,
            api_version=api_version,
        )

    def transform_image_edit_request(
        self,
        model: str,
        prompt: str | None,
        image: FileTypes | None,
        image_edit_optional_request_params: dict,
        embrouter_params: GenericEmbRouterParams,
        headers: dict,
    ) -> tuple[dict, RequestFiles]:
        request_params: Final = {
            "model": model,
            **image_edit_optional_request_params,
        }
        if prompt is not None:
            request_params["prompt"] = prompt

        data_without_files = {key: value for key, value in request_params.items() if key not in ["image", "mask"]}
        files_list: Final[list[tuple[str, Any]]] = []

        if image is not None:
            image_list: Final = [image] if not isinstance(image, list) else image
            for _image in image_list:
                if _image is not None:
                    self._add_image_to_files(
                        files_list=files_list,
                        image=_image,
                        field_name="image",
                    )
                    break

        return data_without_files, files_list

    def transform_image_edit_response(
        self,
        model: str,
        raw_response: httpx.Response,
        logging_obj: "EmbRouterLoggingObj",
    ) -> ImageResponse:
        try:
            response: Final = raw_response.json()
        except Exception:
            raise OpenAIError(message=raw_response.text, status_code=raw_response.status_code)

        if "usage" in response:
            response["usage"] = AzureFoundryMAIImageGenerationConfig.normalize_mai_image_usage(response.get("usage"))

        logging_obj.post_call(
            input="",
            api_key="",
            additional_args={"complete_input_dict": {}},
            original_response=response,
        )

        return convert_to_model_response_object(
            response_object=response,
            model_response_object=ImageResponse(),
            response_type="image_generation",
        )
