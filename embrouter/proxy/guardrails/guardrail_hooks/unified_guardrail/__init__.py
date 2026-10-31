from typing import Final

from embrouter.llms.openai.chat.guardrail_translation.handler import (
    OpenAIChatCompletionsHandler,
)
from embrouter.types.utils import CallTypes

endpoint_translation_mappings: Final = {
    CallTypes.completion: OpenAIChatCompletionsHandler,
    CallTypes.acompletion: OpenAIChatCompletionsHandler,
}

__all__ = ["endpoint_translation_mappings"]
