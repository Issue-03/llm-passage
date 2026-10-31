"""
EmbRouter Skills Hook - Proxy integration for skills

This module provides the CustomLogger hook for skills processing.
The actual skill logic is in embrouter/llms/embrouter_proxy/skills/.

Usage:
    from embrouter.proxy.hooks.embrouter_skills import SkillsInjectionHook

    # Register hook in proxy
    embrouter.callbacks.append(SkillsInjectionHook())
"""

# Re-export from the SDK location for convenience
from embrouter.llms.embrouter_proxy.skills import (
    EMBROUTER_CODE_EXECUTION_TOOL,
    CodeExecutionHandler,
    EmbRouterInternalTools,
    SkillPromptInjectionHandler,
    SkillsSandboxExecutor,
    code_execution_handler,
    get_embrouter_code_execution_tool,
)
from embrouter.proxy.hooks.embrouter_skills.main import SkillsInjectionHook

__all__ = [
    "EMBROUTER_CODE_EXECUTION_TOOL",
    "CodeExecutionHandler",
    "EmbRouterInternalTools",
    "SkillPromptInjectionHandler",
    "SkillsInjectionHook",
    "SkillsSandboxExecutor",
    "code_execution_handler",
    "get_embrouter_code_execution_tool",
]
