from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .lasso import LassoGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _lasso_callback: Final = LassoGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        user_id=embrouter_params.lasso_user_id,
        conversation_id=embrouter_params.lasso_conversation_id,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_lasso_callback)

    return _lasso_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.LASSO.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.LASSO.value: LassoGuardrail,
}
