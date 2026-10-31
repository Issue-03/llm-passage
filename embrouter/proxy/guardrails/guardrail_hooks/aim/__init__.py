from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .aim import AimGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter
    from embrouter.proxy.guardrails.guardrail_hooks.aim import AimGuardrail

    _aim_callback: Final = AimGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        inspect_embeddings=embrouter_params.inspect_embeddings,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_aim_callback)

    return _aim_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.AIM.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.AIM.value: AimGuardrail,
}
