from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .zscaler_ai_guard import ZscalerAIGuard

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _zscaler_ai_guard_callback: Final = ZscalerAIGuard(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        policy_id=embrouter_params.policy_id,
        send_user_api_key_alias=embrouter_params.send_user_api_key_alias,
        send_user_api_key_user_id=embrouter_params.send_user_api_key_user_id,
        send_user_api_key_team_id=embrouter_params.send_user_api_key_team_id,
        timeout=embrouter_params.timeout,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_zscaler_ai_guard_callback)

    return _zscaler_ai_guard_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.ZSCALER_AI_GUARD.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.ZSCALER_AI_GUARD.value: ZscalerAIGuard,
}
