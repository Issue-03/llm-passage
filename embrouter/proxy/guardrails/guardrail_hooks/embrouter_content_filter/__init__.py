from typing import TYPE_CHECKING, Final, Optional

import embrouter
from embrouter.proxy.guardrails.guardrail_hooks.embrouter_content_filter.content_filter import (
    ContentFilterGuardrail,
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
    Initialize the Content Filter Guardrail.

    Args:
        embrouter_params: Guardrail configuration parameters
        guardrail: Guardrail metadata

    Returns:
        Initialized ContentFilterGuardrail instance
    """
    guardrail_name: Final = guardrail.get("guardrail_name")

    if not guardrail_name:
        raise ValueError("Content Filter: guardrail_name is required")

    content_filter_guardrail: Final = ContentFilterGuardrail(
        guardrail_name=guardrail_name,
        guardrail_id=guardrail.get("guardrail_id"),
        policy_template=guardrail.get("policy_template"),
        patterns=embrouter_params.patterns,
        blocked_words=embrouter_params.blocked_words,
        blocked_words_file=embrouter_params.blocked_words_file,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on or False,
        categories=getattr(embrouter_params, "categories", None),
        severity_threshold=getattr(embrouter_params, "severity_threshold", "medium"),
        llm_router=llm_router,
        image_model=getattr(embrouter_params, "image_model", None),
        competitor_intent_config=getattr(embrouter_params, "competitor_intent_config", None),
        end_session_after_n_fails=getattr(embrouter_params, "end_session_after_n_fails", None),
        on_violation=getattr(embrouter_params, "on_violation", None),
        realtime_violation_message=getattr(embrouter_params, "realtime_violation_message", None),
    )

    embrouter.logging_callback_manager.add_embrouter_callback(content_filter_guardrail)

    return content_filter_guardrail


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.EMBROUTER_CONTENT_FILTER.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.EMBROUTER_CONTENT_FILTER.value: ContentFilterGuardrail,
}
