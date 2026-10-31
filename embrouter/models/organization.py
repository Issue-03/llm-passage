"""
Organization table model.

Canonical definition for ``embrouter_organizationtable``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from embrouter.models.budget import EmbRouter_BudgetTable
from embrouter.models.object_permission import EmbRouter_ObjectPermissionTable
from embrouter.models.user import EmbRouter_UserTable
from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_OrganizationTable(EmbRouterPydanticObjectBase):
    """Represents user-controllable params for a EmbRouter_OrganizationTable record"""

    organization_id: str | None = None
    organization_alias: str | None = None
    budget_id: str
    spend: float = 0.0
    metadata: dict | None = None
    models: list[str] = []
    model_spend: dict | None = {}
    created_by: str
    updated_by: str
    users: list[EmbRouter_UserTable] | None = None
    embrouter_budget_table: EmbRouter_BudgetTable | None = None
    object_permission: EmbRouter_ObjectPermissionTable | None = None
    object_permission_id: str | None = None
