from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .qohash import QostodianNexus

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _instance: Final = QostodianNexus(
        api_base=embrouter_params.api_base,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        additional_provider_specific_params=embrouter_params.additional_provider_specific_params,
        extra_headers=getattr(embrouter_params, "extra_headers", None),
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_instance)

    return _instance


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.QOSTODIAN_NEXUS.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.QOSTODIAN_NEXUS.value: QostodianNexus,
}
