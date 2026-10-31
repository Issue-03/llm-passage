from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .prompt_security import PromptSecurityGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter
    from embrouter.proxy.guardrails.guardrail_hooks.prompt_security import (
        PromptSecurityGuardrail,
    )

    _prompt_security_callback: Final = PromptSecurityGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        streaming_transform_mode=getattr(embrouter_params, "streaming_transform_mode", None),
        file_sanitization_fail_open=getattr(embrouter_params, "file_sanitization_fail_open", None),
        block_on_file_modify=getattr(embrouter_params, "block_on_file_modify", None),
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_prompt_security_callback)

    return _prompt_security_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.PROMPT_SECURITY.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.PROMPT_SECURITY.value: PromptSecurityGuardrail,
}
