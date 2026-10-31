from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .crowdstrike_aidr import CrowdStrikeAIDRHandler, streaming_params_from_embrouter_params

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("CrowdStrike AIDR guardrail name is required")

    streaming_params: Final = streaming_params_from_embrouter_params(embrouter_params)
    _crowdstrike_aidr_callback: Final = CrowdStrikeAIDRHandler(
        guardrail_name=guardrail_name,
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        fail_on_error=embrouter_params.fail_on_error,
        streaming_buffer_until_moderated=streaming_params.streaming_buffer_until_moderated,
        streaming_buffer_release_on_scan=streaming_params.streaming_buffer_release_on_scan,
        streaming_end_of_stream_only=streaming_params.streaming_end_of_stream_only,
        streaming_sampling_rate=streaming_params.streaming_sampling_rate,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_crowdstrike_aidr_callback)

    return _crowdstrike_aidr_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.CROWDSTRIKE_AIDR.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.CROWDSTRIKE_AIDR.value: CrowdStrikeAIDRHandler,
}
