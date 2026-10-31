from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .singulr import SingulrGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(
    embrouter_params: "EmbrouterParams",
    guardrail: "Guardrail",
):
    import embrouter

    _cb: Final = SingulrGuardrail(
        singulr_api_base=getattr(embrouter_params, "singulr_api_base", None) or embrouter_params.api_base,
        singulr_api_key=getattr(embrouter_params, "singulr_api_key", None) or embrouter_params.api_key,
        singulr_application_id=getattr(embrouter_params, "singulr_application_id", None),
        singulr_guardrail_id=getattr(embrouter_params, "singulr_guardrail_id", None),
        block_on_error=getattr(embrouter_params, "block_on_error", None),
        timeout=embrouter_params.timeout,
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
    SupportedGuardrailIntegrations.SINGULR.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.SINGULR.value: SingulrGuardrail,
}
