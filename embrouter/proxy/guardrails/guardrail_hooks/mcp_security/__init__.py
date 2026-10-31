from typing import TYPE_CHECKING, Final, Literal, Optional

import embrouter
from embrouter.proxy.guardrails.guardrail_hooks.mcp_security.mcp_security_guardrail import (
    MCPSecurityGuardrail,
)
from embrouter.types.guardrails import SupportedGuardrailIntegrations

if TYPE_CHECKING:
    from embrouter import Router
    from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(
    embrouter_params: "EmbrouterParams",
    guardrail: "Guardrail",
    llm_router: Optional["Router"] = None,
):
    guardrail_name: Final = guardrail.get("guardrail_name")
    if not guardrail_name:
        raise ValueError("MCP Security: guardrail_name is required")

    on_violation: Final[Literal["block", "alert"]] = "block" if embrouter_params.on_violation == "block" else "alert"

    mcp_security_guardrail: Final = MCPSecurityGuardrail(
        guardrail_name=guardrail_name,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on or False,
        on_violation=on_violation,
    )

    embrouter.logging_callback_manager.add_embrouter_callback(mcp_security_guardrail)
    return mcp_security_guardrail


guardrail_initializer_registry: Final = {
    SupportedGuardrailIntegrations.MCP_SECURITY.value: initialize_guardrail,
}

guardrail_class_registry: Final = {
    SupportedGuardrailIntegrations.MCP_SECURITY.value: MCPSecurityGuardrail,
}
