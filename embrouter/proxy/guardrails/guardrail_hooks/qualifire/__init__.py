from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .qualifire import QualifireGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _qualifire_callback: Final = QualifireGuardrail(
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        evaluation_id=getattr(embrouter_params, "evaluation_id", None),
        prompt_injections=getattr(embrouter_params, "prompt_injections", None),
        hallucinations_check=getattr(embrouter_params, "hallucinations_check", None),
        grounding_check=getattr(embrouter_params, "grounding_check", None),
        pii_check=getattr(embrouter_params, "pii_check", None),
        content_moderation_check=getattr(embrouter_params, "content_moderation_check", None),
        tool_selection_quality_check=getattr(embrouter_params, "tool_selection_quality_check", None),
        assertions=getattr(embrouter_params, "assertions", None),
        on_flagged=getattr(embrouter_params, "on_flagged", "block"),
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_qualifire_callback)

    return _qualifire_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.QUALIFIRE.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.QUALIFIRE.value: QualifireGuardrail,
}
