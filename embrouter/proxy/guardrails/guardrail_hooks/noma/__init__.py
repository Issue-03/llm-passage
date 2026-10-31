from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .noma import NomaGuardrail
from .noma_v2 import NomaV2Guardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    use_v2 = getattr(embrouter_params, "use_v2", False)
    if isinstance(use_v2, str):
        use_v2 = use_v2.lower() == "true"
    if use_v2:
        return initialize_guardrail_v2(embrouter_params=embrouter_params, guardrail=guardrail)

    import embrouter

    _noma_callback: Final = NomaGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        application_id=embrouter_params.application_id,
        monitor_mode=embrouter_params.monitor_mode,
        block_failures=embrouter_params.block_failures,
        anonymize_input=embrouter_params.anonymize_input,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_noma_callback)

    return _noma_callback


def initialize_guardrail_v2(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _noma_v2_callback: Final = NomaV2Guardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        application_id=embrouter_params.application_id,
        gateway_name=embrouter_params.gateway_name,
        monitor_mode=embrouter_params.monitor_mode,
        block_failures=embrouter_params.block_failures,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_noma_v2_callback)

    return _noma_v2_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.NOMA.value: initialize_guardrail,
    SupportedGuardrailIntegrations.NOMA_V2.value: initialize_guardrail_v2,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.NOMA.value: NomaGuardrail,
    SupportedGuardrailIntegrations.NOMA_V2.value: NomaV2Guardrail,
}
