from typing import Final

import embrouter
from embrouter.types.guardrails import Guardrail, EmbrouterParams


def initialize_guardrail(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.tool_policy.tool_policy_guardrail import (
        ToolPolicyGuardrail,
    )

    _callback: Final = ToolPolicyGuardrail(
        guardrail_name=guardrail.get("guardrail_name", "tool_policy"),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_callback)
    return _callback
