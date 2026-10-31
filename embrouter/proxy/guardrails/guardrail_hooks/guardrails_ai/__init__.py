from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .guardrails_ai import GuardrailsAI

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    if embrouter_params.guard_name is None:
        raise Exception(
            "GuardrailsAIException - Please pass the Guardrails AI guard name via 'embrouter_params::guard_name'"
        )

    _guardrails_ai_callback: Final = GuardrailsAI(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        guard_name=embrouter_params.guard_name,
        guardrails_ai_api_input_format=getattr(embrouter_params, "guardrails_ai_api_input_format", "llmOutput"),
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_guardrails_ai_callback)

    return _guardrails_ai_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.GUARDRAILS_AI.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.GUARDRAILS_AI.value: GuardrailsAI,
}
