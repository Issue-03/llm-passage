from typing import TYPE_CHECKING, Any, Final

from embrouter.embrouter_core_utils.url_utils import encode_url_path_segment
from embrouter.llms.openai.vector_stores.transformation import OpenAIVectorStoreConfig
from embrouter.secret_managers.main import get_secret_str
from embrouter.types.router import GenericEmbRouterParams
from embrouter.types.vector_stores import VectorStoreSearchOptionalRequestParams

if TYPE_CHECKING:
    from embrouter.embrouter_core_utils.embrouter_logging import Logging as EmbRouterLoggingObj
else:
    EmbRouterLoggingObj = Any


class PGVectorStoreConfig(OpenAIVectorStoreConfig):
    """
    PG Vector Store configuration that inherits from OpenAI since it's OpenAI-compatible.

    EmbRouter Provides an OpenAI Compatible Server to connect to PG Vector.



    You just need to connect embrouter proxy to this deployed server.

    Requires:
    - api_base: The base URL for the PG vector service
    - api_key: API key for authentication with the PG vector service
    """

    def validate_environment(self, headers: dict, embrouter_params: GenericEmbRouterParams | None) -> dict:
        """
        Validate environment and set headers for PG vector service authentication
        """
        embrouter_params = embrouter_params or GenericEmbRouterParams()

        # Get API key from various sources
        api_key: Final = embrouter_params.api_key or get_secret_str("PG_VECTOR_API_KEY")

        if not api_key:
            raise ValueError(
                "PG Vector API key is required. Set PG_VECTOR_API_KEY environment variable or pass api_key in embrouter_params."
            )

        headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )

        return headers

    def get_complete_url(
        self,
        api_base: str | None,
        embrouter_params: dict,
    ) -> str:
        """
        Get the complete URL for PG vector service endpoints
        """
        # Get API base from various sources
        api_base = api_base or get_secret_str("PG_VECTOR_API_BASE")

        if not api_base:
            raise ValueError(
                "PG Vector API base URL is required. Set PG_VECTOR_API_BASE environment variable or pass api_base in embrouter_params."
            )

        # Remove trailing slashes
        api_base = api_base.rstrip("/")

        return f"{api_base}/v1/vector_stores"

    def transform_search_vector_store_request(
        self,
        vector_store_id: str,
        query: str | list[str],
        vector_store_search_optional_params: VectorStoreSearchOptionalRequestParams,
        api_base: str,
        embrouter_logging_obj: EmbRouterLoggingObj,
        embrouter_params: dict,
        extra_body: dict[str, Any] | None = None,
    ) -> tuple[str, dict]:
        encoded_vector_store_id: Final = encode_url_path_segment(vector_store_id, field_name="vector_store_id")
        url: Final = f"{api_base}/{encoded_vector_store_id}/search"
        _, request_body = super().transform_search_vector_store_request(
            vector_store_id=vector_store_id,
            query=query,
            vector_store_search_optional_params=vector_store_search_optional_params,
            api_base=api_base,
            embrouter_logging_obj=embrouter_logging_obj,
            embrouter_params=embrouter_params,
            extra_body=extra_body,
        )
        return url, request_body
