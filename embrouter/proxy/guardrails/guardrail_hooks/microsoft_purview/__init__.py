from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .purview_dlp import MicrosoftPurviewDLPGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    tenant_id: Final = getattr(embrouter_params, "tenant_id", None)
    client_id: Final = getattr(embrouter_params, "client_id", None)

    # client_secret can be passed via the standard api_key field or as
    # a dedicated client_secret parameter.
    client_secret: Final = embrouter_params.api_key or getattr(embrouter_params, "client_secret", None)

    if not tenant_id:
        raise ValueError("Microsoft Purview: tenant_id is required")
    if not client_id:
        raise ValueError("Microsoft Purview: client_id is required")
    if not client_secret:
        raise ValueError("Microsoft Purview: client_secret (or api_key) is required")

    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("Microsoft Purview: guardrail_name is required")

    purview_guardrail: Final = MicrosoftPurviewDLPGuardrail(
        guardrail_name=guardrail_name,
        tenant_id=str(tenant_id),
        client_id=str(client_id),
        client_secret=str(client_secret),
        purview_app_name=str(getattr(embrouter_params, "purview_app_name", None) or "EmbRouter"),
        user_id_field=str(getattr(embrouter_params, "user_id_field", None) or "user_id"),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(purview_guardrail)
    return purview_guardrail


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.MICROSOFT_PURVIEW.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.MICROSOFT_PURVIEW.value: MicrosoftPurviewDLPGuardrail,
}
