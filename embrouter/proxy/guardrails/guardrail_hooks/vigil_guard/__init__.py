from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .vigil_guard import VigilGuardGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _vigil_guard_callback: Final = VigilGuardGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        unreachable_fallback=embrouter_params.unreachable_fallback,
        timeout=embrouter_params.timeout,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_vigil_guard_callback)
    return _vigil_guard_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.VIGIL_GUARD.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.VIGIL_GUARD.value: VigilGuardGuardrail,
}
