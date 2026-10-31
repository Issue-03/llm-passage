"""
EmbRouter Interactions API

This module provides SDK methods for Google's Interactions API.

Usage:
    import embrouter

    # Create an interaction with a model
    response = embrouter.interactions.create(
        model="gemini-2.5-flash",
        input="Hello, how are you?"
    )

    # Create an interaction with an agent
    response = embrouter.interactions.create(
        agent="deep-research-pro-preview-12-2025",
        input="Research the current state of cancer research"
    )

    # Async version
    response = await embrouter.interactions.acreate(...)

    # Get an interaction
    response = embrouter.interactions.get(interaction_id="...")

    # Delete an interaction
    result = embrouter.interactions.delete(interaction_id="...")

    # Cancel an interaction
    result = embrouter.interactions.cancel(interaction_id="...")

    # Create a managed agent on the provider side
    result = embrouter.interactions.agents.create(
        name="waverunner",
        custom_llm_provider="gemini",
        api_key="...",
        base_agent="gemini-2.5-flash",
        instructions="You are a helpful assistant.",
    )

Methods:
- create(): Sync create interaction
- acreate(): Async create interaction
- get(): Sync get interaction
- aget(): Async get interaction
- delete(): Sync delete interaction
- adelete(): Async delete interaction
- cancel(): Sync cancel interaction
- acancel(): Async cancel interaction

Sub-modules:
- agents: Provider-side agent creation (embrouter.interactions.agents.create)
"""

from embrouter.interactions import agents
from embrouter.interactions.main import (
    acancel,
    acreate,
    adelete,
    aget,
    cancel,
    create,
    delete,
    get,
)

__all__ = [
    "acancel",
    "acreate",
    "adelete",
    "agents",
    "aget",
    "cancel",
    "create",
    "delete",
    "get",
]
