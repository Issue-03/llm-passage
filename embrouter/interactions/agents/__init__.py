"""
embrouter.interactions.agents

Full CRUD SDK for provider-side managed agents (e.g. Gemini v1beta/agents).

    embrouter.interactions.agents.create(name=..., ...)
    embrouter.interactions.agents.list(api_key=...)
    embrouter.interactions.agents.get(name=..., ...)
    embrouter.interactions.agents.delete(name=..., ...)
    embrouter.interactions.agents.list_versions(name=..., ...)

Async counterparts: acreate, alist, aget, adelete, alist_versions
"""

from embrouter.interactions.agents.main import (
    acreate,
    adelete,
    aget,
    alist,
    alist_versions,
    create,
    delete,
    get,
    list,
    list_versions,
)

__all__ = [
    "acreate",
    "adelete",
    "aget",
    "alist",
    "alist_versions",
    "create",
    "delete",
    "get",
    "list",
    "list_versions",
]
