"""Gray Swan Cygnal guardrail integration for EmbRouter."""

from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .grayswan import (
    GraySwanGuardrail,
    GraySwanGuardrailAPIError,
    GraySwanGuardrailMissingSecrets,
)

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail") -> GraySwanGuardrail:
    import embrouter

    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("Gray Swan guardrail requires a guardrail_name")

    optional_params: Final = getattr(embrouter_params, "optional_params", None)

    grayswan_guardrail: Final = GraySwanGuardrail(
        guardrail_name=guardrail_name,
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        on_flagged_action=_get_config_value(embrouter_params, optional_params, "on_flagged_action"),
        violation_threshold=_get_config_value(embrouter_params, optional_params, "violation_threshold"),
        reasoning_mode=_get_config_value(embrouter_params, optional_params, "reasoning_mode"),
        categories=_get_config_value(embrouter_params, optional_params, "categories"),
        policy_id=_get_config_value(embrouter_params, optional_params, "policy_id"),
        streaming_end_of_stream_only=_get_config_value(embrouter_params, optional_params, "streaming_end_of_stream_only")
        or False,
        streaming_sampling_rate=_get_config_value(embrouter_params, optional_params, "streaming_sampling_rate") or 5,
        fail_open=_get_config_value(embrouter_params, optional_params, "fail_open"),
        guardrail_timeout=_get_config_value(embrouter_params, optional_params, "guardrail_timeout"),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(grayswan_guardrail)
    return grayswan_guardrail


def _get_config_value(embrouter_params, optional_params, attribute_name):
    if optional_params is not None:
        value: Final = getattr(optional_params, attribute_name, None)
        if value is not None:
            return value
    return getattr(embrouter_params, attribute_name, None)


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.GRAYSWAN.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.GRAYSWAN.value: GraySwanGuardrail,
}


__all__ = [
    "GraySwanGuardrail",
    "GraySwanGuardrailAPIError",
    "GraySwanGuardrailMissingSecrets",
    "initialize_guardrail",
]
