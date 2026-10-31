"""Cohere Rerank handler for Unified Guardrails."""

from typing import Final

from embrouter.llms.cohere.rerank.guardrail_translation.handler import CohereRerankHandler
from embrouter.types.utils import CallTypes

guardrail_translation_mappings: Final = {
    CallTypes.rerank: CohereRerankHandler,
    CallTypes.arerank: CohereRerankHandler,
}

__all__ = ["CohereRerankHandler", "guardrail_translation_mappings"]
