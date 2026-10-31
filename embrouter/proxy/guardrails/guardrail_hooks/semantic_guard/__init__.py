"""
Semantic Guard guardrail — embedding-based prompt injection detection.

Uses semantic-router to match user prompts against known attack patterns.
"""

from typing import TYPE_CHECKING, Final, Optional

import embrouter
from embrouter.constants import (
    DEFAULT_SEMANTIC_GUARD_EMBEDDING_MODEL,
    DEFAULT_SEMANTIC_GUARD_SIMILARITY_THRESHOLD,
)
from embrouter.proxy.guardrails.guardrail_hooks.semantic_guard.semantic_guard import (
    SemanticGuardrail,
)
from embrouter.types.guardrails import SupportedGuardrailIntegrations

if TYPE_CHECKING:
    from embrouter import Router
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(
    embrouter_params: "EmbrouterParams",
    guardrail: "Guardrail",
    llm_router: Optional["Router"] = None,
):
    """
    Initialize the Semantic Guard guardrail.

    Args:
        embrouter_params: Guardrail configuration parameters
        guardrail: Guardrail metadata
        llm_router: EmbRouter Router instance (required for embeddings)

    Returns:
        Initialized SemanticGuardrail instance
    """
    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("SemanticGuard: guardrail_name is required")

    if llm_router is None:
        raise ValueError(
            "SemanticGuard requires llm_router for embeddings. Configure a model_list with an embedding model."
        )

    semantic_guardrail: Final = SemanticGuardrail(
        guardrail_name=guardrail_name,
        llm_router=llm_router,
        embedding_model=getattr(embrouter_params, "embedding_model", None) or DEFAULT_SEMANTIC_GUARD_EMBEDDING_MODEL,
        similarity_threshold=getattr(embrouter_params, "similarity_threshold", None)
        or DEFAULT_SEMANTIC_GUARD_SIMILARITY_THRESHOLD,
        route_templates=getattr(embrouter_params, "route_templates", None),
        custom_routes_file=getattr(embrouter_params, "custom_routes_file", None),
        custom_routes=getattr(embrouter_params, "custom_routes", None),
        on_flagged_action=getattr(embrouter_params, "on_flagged_action", "block"),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on or False,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(semantic_guardrail)

    return semantic_guardrail


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.SEMANTIC_GUARD.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.SEMANTIC_GUARD.value: SemanticGuardrail,
}
