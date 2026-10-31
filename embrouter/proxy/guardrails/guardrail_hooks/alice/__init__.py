from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .alice import AliceGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _alice_guardrail_callback: Final = AliceGuardrail(
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        unreachable_fallback=getattr(embrouter_params, "unreachable_fallback", "fail_closed"),
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_alice_guardrail_callback)
    return _alice_guardrail_callback


guardrail_initializer_registry: Final = {  # mutable-ok: module-level registry, built once and never mutated
    SupportedGuardrailIntegrations.ALICE.value: initialize_guardrail,
}


guardrail_class_registry: Final = {  # mutable-ok: module-level registry, built once and never mutated
    SupportedGuardrailIntegrations.ALICE.value: AliceGuardrail,
}
