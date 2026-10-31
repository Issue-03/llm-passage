from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .xecguard import XecGuardGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(
    embrouter_params: "EmbrouterParams",
    guardrail: "Guardrail",
):
    import embrouter

    _cb: Final = XecGuardGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        xecguard_model=embrouter_params.xecguard_model,
        policy_names=embrouter_params.policy_names,
        block_on_error=embrouter_params.block_on_error,
        grounding_strictness=embrouter_params.grounding_strictness,
        guardrail_name=guardrail.get(
            "guardrail_name",
            "",
        ),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(
        _cb,
    )

    return _cb


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.XECGUARD.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.XECGUARD.value: XecGuardGuardrail,
}
