from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .model_armor import ModelArmorGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter
    from embrouter.proxy.guardrails.guardrail_hooks.model_armor import (
        ModelArmorGuardrail,
    )

    _model_armor_callback: Final = ModelArmorGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        template_id=embrouter_params.template_id,
        project_id=embrouter_params.project_id,
        location=embrouter_params.location,
        credentials=embrouter_params.credentials,
        api_endpoint=embrouter_params.api_endpoint,
        default_on=embrouter_params.default_on,
        mask_request_content=embrouter_params.mask_request_content,
        mask_response_content=embrouter_params.mask_response_content,
        fail_on_error=embrouter_params.fail_on_error,
        skip_unscannable_attachments=embrouter_params.skip_unscannable_attachments,
        sanitize_error_detail=embrouter_params.sanitize_error_detail,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_model_armor_callback)

    return _model_armor_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.MODEL_ARMOR.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.MODEL_ARMOR.value: ModelArmorGuardrail,
}
