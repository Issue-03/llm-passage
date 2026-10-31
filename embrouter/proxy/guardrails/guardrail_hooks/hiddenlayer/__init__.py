from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .hiddenlayer import HiddenlayerGuardrail, HiddenlayerGuardrailV2

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    api_id: Final = embrouter_params.api_id if hasattr(embrouter_params, "api_id") else None
    auth_url: Final = embrouter_params.auth_url if hasattr(embrouter_params, "auth_url") else None
    version: Final[int | None] = embrouter_params.version if hasattr(embrouter_params, "version") else None

    _hiddenlayer_callback: HiddenlayerGuardrail | HiddenlayerGuardrailV2
    if not version or version < 2:
        _hiddenlayer_callback = HiddenlayerGuardrail(
            api_base=embrouter_params.api_base,
            api_id=api_id,
            api_key=embrouter_params.api_key,
            auth_url=auth_url,
            guardrail_name=guardrail.get("guardrail_name", ""),
            event_hook=embrouter_params.mode,
            default_on=embrouter_params.default_on,
        )
    else:
        _hiddenlayer_callback = HiddenlayerGuardrailV2(
            api_base=embrouter_params.api_base,
            api_id=api_id,
            api_key=embrouter_params.api_key,
            auth_url=auth_url,
            guardrail_name=guardrail.get("guardrail_name", ""),
            event_hook=embrouter_params.mode,
            default_on=embrouter_params.default_on,
        )

    embrouter.logging_callback_manager.add_embrouter_callback(_hiddenlayer_callback)
    return _hiddenlayer_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.HIDDENLAYER.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.HIDDENLAYER.value: HiddenlayerGuardrail,
}
