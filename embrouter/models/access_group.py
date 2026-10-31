"""
Access group table model.

Canonical definition for ``embrouter_accessgrouptable``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from datetime import datetime

from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_AccessGroupTable(EmbRouterPydanticObjectBase):
    access_group_id: str
    access_group_name: str
    description: str | None = None
    access_model_names: list[str] = []
    access_mcp_server_ids: list[str] = []
    access_agent_ids: list[str] = []
    assigned_team_ids: list[str] = []
    assigned_key_ids: list[str] = []
    created_at: datetime | None = None
    created_by: str | None = None
    updated_at: datetime | None = None
    updated_by: str | None = None
