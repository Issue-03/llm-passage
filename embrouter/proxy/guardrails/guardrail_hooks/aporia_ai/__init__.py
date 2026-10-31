from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .aporia_ai import AporiaGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _aporia_callback: Final = AporiaGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_aporia_callback)

    return _aporia_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.APORIA.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.APORIA.value: AporiaGuardrail,
}
