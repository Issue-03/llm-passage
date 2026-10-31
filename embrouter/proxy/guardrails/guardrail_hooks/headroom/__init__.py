from __future__ import annotations

from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import (
    GuardrailEventHooks,
    Mode,
    SupportedGuardrailIntegrations,
)

from .headroom import HeadroomGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def _coerce_event_hook(
    mode: str | list[str] | Mode,
) -> GuardrailEventHooks | list[GuardrailEventHooks] | Mode:
    if isinstance(mode, Mode):
        return mode
    if isinstance(mode, list):
        return [GuardrailEventHooks(item) for item in mode]
    return GuardrailEventHooks(mode)


def initialize_guardrail(embrouter_params: EmbrouterParams, guardrail: Guardrail) -> HeadroomGuardrail:
    import embrouter

    _callback: Final = HeadroomGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        model=embrouter_params.model,
        guardrail_name=guardrail["guardrail_name"],
        event_hook=_coerce_event_hook(embrouter_params.mode),
        default_on=embrouter_params.default_on or False,
        unreachable_fallback=embrouter_params.unreachable_fallback,
        timeout=embrouter_params.timeout,
        ccr_retrieval=embrouter_params.ccr_retrieval,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(  # pyright: ignore[reportUnknownMemberType]
        _callback
    )
    return _callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.HEADROOM.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.HEADROOM.value: HeadroomGuardrail,
}
