from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .javelin import JavelinGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    if embrouter_params.guard_name is None:
        raise Exception(
            "JavelinGuardrailException - Please pass the Javelin guard name via 'embrouter_params::guard_name'"
        )

    _javelin_callback: Final = JavelinGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        javelin_guard_name=embrouter_params.guard_name,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on or False,
        api_version=embrouter_params.api_version or "v1",
        config=embrouter_params.config,
        metadata=embrouter_params.metadata,
        application=embrouter_params.application,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_javelin_callback)

    return _javelin_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.JAVELIN.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.JAVELIN.value: JavelinGuardrail,
}
