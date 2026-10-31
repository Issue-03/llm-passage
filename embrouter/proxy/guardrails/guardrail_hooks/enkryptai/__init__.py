from .enkryptai import EnkryptAIGuardrails

__all__ = ["EnkryptAIGuardrails"]


from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _enkryptai_callback: Final = EnkryptAIGuardrails(
        guardrail_name=guardrail.get("guardrail_name", ""),
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        policy_name=embrouter_params.policy_name,
        deployment_name=embrouter_params.deployment_name,
        detectors=embrouter_params.detectors,
        block_on_violation=embrouter_params.block_on_violation,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_enkryptai_callback)

    return _enkryptai_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.ENKRYPTAI.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.ENKRYPTAI.value: EnkryptAIGuardrails,
}
