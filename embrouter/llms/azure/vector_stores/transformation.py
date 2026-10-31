from embrouter.llms.azure.common_utils import BaseAzureLLM
from embrouter.llms.openai.vector_stores.transformation import OpenAIVectorStoreConfig
from embrouter.types.router import GenericEmbRouterParams


class AzureOpenAIVectorStoreConfig(OpenAIVectorStoreConfig):
    def get_complete_url(
        self,
        api_base: str | None,
        embrouter_params: dict,
    ) -> str:
        return BaseAzureLLM._get_base_azure_url(
            api_base=api_base,
            embrouter_params=embrouter_params,
            route="/openai/vector_stores",
        )

    def validate_environment(self, headers: dict, embrouter_params: GenericEmbRouterParams | None) -> dict:
        return BaseAzureLLM._base_validate_azure_environment(headers=headers, embrouter_params=embrouter_params)
