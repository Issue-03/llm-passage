from typing import TYPE_CHECKING, Any, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .generic_guardrail_api import GenericGuardrailAPI

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def _get_config_value(embrouter_params: "EmbrouterParams", optional_params: object, attribute_name: str) -> Any | None:
    if optional_params is not None:
        value: Final = (
            optional_params.get(attribute_name)
            if isinstance(optional_params, dict)
            else getattr(optional_params, attribute_name, None)
        )
        if value is not None:
            return value
    return getattr(embrouter_params, attribute_name, None)


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    optional_params: Final = getattr(embrouter_params, "optional_params", None)

    _generic_guardrail_api_callback: Final = GenericGuardrailAPI(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        headers=getattr(embrouter_params, "headers", None),
        additional_provider_specific_params=getattr(embrouter_params, "additional_provider_specific_params", {}),
        unreachable_fallback=getattr(embrouter_params, "unreachable_fallback", "fail_closed"),
        fail_on_error=getattr(embrouter_params, "fail_on_error", True),
        extra_headers=getattr(embrouter_params, "extra_headers", None),
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        streaming_end_of_stream_only=_get_config_value(embrouter_params, optional_params, "streaming_end_of_stream_only"),
        streaming_sampling_rate=_get_config_value(embrouter_params, optional_params, "streaming_sampling_rate"),
        streaming_transform_mode=_get_config_value(embrouter_params, optional_params, "streaming_transform_mode"),
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_generic_guardrail_api_callback)
    return _generic_guardrail_api_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.GENERIC_GUARDRAIL_API.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.GENERIC_GUARDRAIL_API.value: GenericGuardrailAPI,
}
