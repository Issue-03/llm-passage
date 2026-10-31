from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import TYPE_CHECKING, Final

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .conduct import ConductGuardrail

if TYPE_CHECKING:
    from embrouter.integrations.custom_guardrail import CustomGuardrail
    from embrouter.types.guardrails import Guardrail, EmbrouterParams

DEFAULT_TIMEOUT_SECONDS: Final = 8.0
_NO_EXTRAS: Final[Mapping[str, object]] = MappingProxyType({})


def initialize_guardrail(
    embrouter_params: EmbrouterParams,
    guardrail: Guardrail,
    guardrail_cls: type[CustomGuardrail] = ConductGuardrail,
) -> CustomGuardrail:
    import embrouter

    extras: Final = embrouter_params.model_extra or _NO_EXTRAS
    _callback: Final = guardrail_cls(
        api_url=embrouter_params.api_base,
        agent_token=embrouter_params.api_key,
        workspace_id=extras.get("workspace_id"),
        tool_name=extras.get("tool_name", "llm_call"),
        unreachable_fallback=embrouter_params.unreachable_fallback,
        timeout=DEFAULT_TIMEOUT_SECONDS if embrouter_params.timeout is None else embrouter_params.timeout,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        supported_event_hooks=guardrail_cls.get_supported_event_hooks(),
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_callback)
    return _callback


guardrail_initializer_registry: Final = {  # mutable-ok: module-level registry, built once and never mutated
    SupportedGuardrailIntegrations.CONDUCT.value: initialize_guardrail,
}

guardrail_class_registry: Final = {  # mutable-ok: module-level registry, built once and never mutated
    SupportedGuardrailIntegrations.CONDUCT.value: ConductGuardrail,
}
