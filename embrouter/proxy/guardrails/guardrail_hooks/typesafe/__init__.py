from __future__ import annotations

from typing import TYPE_CHECKING, Final

from pydantic import BaseModel

from embrouter.types.guardrails import (
    GuardrailEventHooks,
    Mode,
    SupportedGuardrailIntegrations,
)
from embrouter.types.proxy.guardrails.guardrail_hooks.typesafe import (
    TypeSafeGuardrailOptionalParams,
)

from .typesafe import TypeSafeGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def _coerce_event_hook(
    mode: str | list[str] | Mode,
) -> GuardrailEventHooks | list[GuardrailEventHooks] | Mode:
    if isinstance(mode, Mode):
        return mode
    if isinstance(mode, list):
        return [  # mutable-ok: CustomGuardrail event_hook contract wants a list
            GuardrailEventHooks(item) for item in mode
        ]
    return GuardrailEventHooks(mode)


def _optional_params(embrouter_params: EmbrouterParams) -> TypeSafeGuardrailOptionalParams:
    value: Final = embrouter_params.optional_params
    if isinstance(value, TypeSafeGuardrailOptionalParams):
        return value
    if isinstance(value, BaseModel):
        return TypeSafeGuardrailOptionalParams.model_validate(value.model_dump())
    return TypeSafeGuardrailOptionalParams()


def initialize_guardrail(embrouter_params: EmbrouterParams, guardrail: Guardrail) -> TypeSafeGuardrail:
    import embrouter

    optional_params: Final = _optional_params(embrouter_params)

    _callback: Final = TypeSafeGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        model=embrouter_params.model,
        relevance_threshold=optional_params.relevance_threshold,
        min_chars_to_evaluate=optional_params.min_chars_to_evaluate,
        max_result_chars_in_state=optional_params.max_result_chars_in_state,
        guardrail_name=guardrail["guardrail_name"],
        event_hook=_coerce_event_hook(embrouter_params.mode),
        default_on=embrouter_params.default_on or False,
        unreachable_fallback=(
            embrouter_params.unreachable_fallback if "unreachable_fallback" in embrouter_params.model_fields_set else None
        ),
    )
    embrouter.logging_callback_manager.add_embrouter_callback(  # pyright: ignore[reportUnknownMemberType]  # callback manager is untyped
        _callback
    )
    return _callback


guardrail_initializer_registry: Final = {  # mutable-ok: guardrail_registry discovery checks isinstance(registry, dict)
    SupportedGuardrailIntegrations.TYPESAFE.value: initialize_guardrail,
}

guardrail_class_registry: Final = {  # mutable-ok: guardrail_registry discovery checks isinstance(registry, dict)
    SupportedGuardrailIntegrations.TYPESAFE.value: TypeSafeGuardrail,
}
