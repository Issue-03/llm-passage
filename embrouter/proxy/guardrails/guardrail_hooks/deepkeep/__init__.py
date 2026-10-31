from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .deepkeep import DeepKeepGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _deepkeep_guardrail_callback: Final = DeepKeepGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        firewall_id=getattr(embrouter_params, "deepkeep_firewall_id", None),
        unreachable_fallback=getattr(embrouter_params, "unreachable_fallback", "fail_closed"),
        extra_headers=getattr(embrouter_params, "extra_headers", None),
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_deepkeep_guardrail_callback)
    return _deepkeep_guardrail_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.DEEPKEEP.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.DEEPKEEP.value: DeepKeepGuardrail,
}
