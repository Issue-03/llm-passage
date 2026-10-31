"""
EmbRouter Proxy Skills - Database-backed skills storage and execution

This module provides:
- Database-backed skills storage (alternative to Anthropic's cloud-based skills API)
- Skill content extraction and prompt injection
- Sandboxed code execution for skills
- Automatic code execution handler

Main components:
- handler.py: EmbRouterSkillsHandler - database CRUD operations
- transformation.py: EmbRouterSkillsTransformationHandler - SDK transformation layer
- prompt_injection.py: SkillPromptInjectionHandler - SKILL.md extraction and injection
- sandbox_executor.py: SkillsSandboxExecutor - Docker sandbox execution
- code_execution.py: CodeExecutionHandler - automatic agentic loop
"""

from embrouter.llms.embrouter_proxy.skills.code_execution import (
    EMBROUTER_CODE_EXECUTION_TOOL,
    CodeExecutionHandler,
    EmbRouterInternalTools,
    add_code_execution_tool,
    code_execution_handler,
    get_embrouter_code_execution_tool,
    has_code_execution_tool,
)
from embrouter.llms.embrouter_proxy.skills.constants import (
    DEFAULT_MAX_ITERATIONS,
    DEFAULT_SANDBOX_TIMEOUT,
)
from embrouter.llms.embrouter_proxy.skills.handler import EmbRouterSkillsHandler
from embrouter.llms.embrouter_proxy.skills.prompt_injection import (
    SkillPromptInjectionHandler,
)
from embrouter.llms.embrouter_proxy.skills.sandbox_executor import SkillsSandboxExecutor
from embrouter.llms.embrouter_proxy.skills.transformation import (
    EmbRouterSkillsTransformationHandler,
)

__all__ = [
    "DEFAULT_MAX_ITERATIONS",
    "DEFAULT_SANDBOX_TIMEOUT",
    "EMBROUTER_CODE_EXECUTION_TOOL",
    "CodeExecutionHandler",
    "EmbRouterInternalTools",
    "EmbRouterSkillsHandler",
    "EmbRouterSkillsTransformationHandler",
    "SkillPromptInjectionHandler",
    "SkillsSandboxExecutor",
    "add_code_execution_tool",
    "code_execution_handler",
    "get_embrouter_code_execution_tool",
    "has_code_execution_tool",
]
