from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .pangea import PangeaHandler

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("Pangea guardrail name is required")

    _pangea_callback: Final = PangeaHandler(
        guardrail_name=guardrail_name,
        pangea_input_recipe=embrouter_params.pangea_input_recipe,
        pangea_output_recipe=embrouter_params.pangea_output_recipe,
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_pangea_callback)

    return _pangea_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.PANGEA.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.PANGEA.value: PangeaHandler,
}
