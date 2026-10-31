from typing import TYPE_CHECKING, Any, Final, cast

from embrouter.types.guardrails import SupportedGuardrailIntegrations

from .mcp_end_user_permission import MCPEndUserPermissionGuardrail

if TYPE_CHECKING:
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: "EmbrouterParams", guardrail: "Guardrail"):
    import embrouter

    # Default to always-on. Only disable if the user explicitly sets default_on: false.
    # We check the raw guardrail dict because EmbrouterParams normalizes None → False,
    # making it impossible to distinguish "not set" from "explicitly false" via embrouter_params.
    _raw_default_on: Final = cast(dict[str, Any], guardrail).get("embrouter_params", {}).get("default_on")
    _default_on: Final = _raw_default_on is not False

    _callback: Final = MCPEndUserPermissionGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=_default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_callback)
    return _callback


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.MCP_END_USER_PERMISSION.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.MCP_END_USER_PERMISSION.value: MCPEndUserPermissionGuardrail,
}
