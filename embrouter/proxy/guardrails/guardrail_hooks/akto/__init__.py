from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .akto import AktoGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    _akto_callback: Final = AktoGuardrail(
        akto_base_url=getattr(embrouter_params, "akto_base_url", None),
        akto_api_key=getattr(embrouter_params, "akto_api_key", None),
        akto_account_id=getattr(embrouter_params, "akto_account_id", None),
        akto_vxlan_id=getattr(embrouter_params, "akto_vxlan_id", None),
        unreachable_fallback=getattr(embrouter_params, "unreachable_fallback", "fail_closed"),
        guardrail_timeout=getattr(embrouter_params, "guardrail_timeout", None),
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(_akto_callback)
    return _akto_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.AKTO.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.AKTO.value: AktoGuardrail,
}
