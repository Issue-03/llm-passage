from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .panw_prisma_airs import PanwPrismaAirsHandler

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    guardrail_name: Final = guardrail.get("guardrail_name")

    # Note: api_key and profile_name can be None - handler will use env vars or API key's linked profile
    if not guardrail_name:
        raise ValueError("PANW Prisma AIRS: guardrail_name is required")

    _panw_callback: Final = PanwPrismaAirsHandler(
        **{
            **embrouter_params.model_dump(exclude_unset=True),
            "guardrail_name": guardrail_name,
            "event_hook": embrouter_params.mode,
            "default_on": embrouter_params.default_on or False,
        }
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_panw_callback)

    return _panw_callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.PANW_PRISMA_AIRS.value: initialize_guardrail,
}


guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.PANW_PRISMA_AIRS.value: PanwPrismaAirsHandler,
}
