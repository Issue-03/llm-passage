import os
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from embrouter.integrations.custom_prompt_management import CustomPromptManagement
    from embrouter.types.prompts.init_prompts import PromptEmbRouterParams, PromptSpec

from embrouter.types.prompts.init_prompts import SupportedPromptIntegrations

from .arize_phoenix_prompt_manager import ArizePhoenixPromptManager

# Global instances
global_arize_config: Final[dict | None] = None


def prompt_initializer(embrouter_params: "PromptEmbRouterParams", prompt_spec: "PromptSpec") -> "CustomPromptManagement":
    """
    Initialize a prompt from Arize Phoenix.
    """
    api_key: Final = getattr(embrouter_params, "api_key", None) or os.environ.get("PHOENIX_API_KEY")
    api_base: Final = getattr(embrouter_params, "api_base", None)
    prompt_id: Final = getattr(embrouter_params, "prompt_id", None)

    if not api_key or not api_base:
        raise ValueError("api_key and api_base are required for Arize Phoenix prompt integration")

    try:
        arize_prompt_manager: Final = ArizePhoenixPromptManager(
            **{
                "api_key": api_key,
                "api_base": api_base,
                "prompt_id": prompt_id,
                **embrouter_params.model_dump(exclude={"api_key", "api_base", "prompt_id"}),
            },
        )

        return arize_prompt_manager
    except Exception as e:
        raise e


prompt_initializer_registry: Final = {
    SupportedPromptIntegrations.ARIZE_PHOENIX.value: prompt_initializer,
}
