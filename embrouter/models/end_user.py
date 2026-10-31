"""
End-user table model.

Canonical definition for ``embrouter_endusertable``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from typing import Literal

from pydantic import ConfigDict, model_validator

from embrouter.models.budget import EmbRouter_BudgetTable
from embrouter.models.object_permission import EmbRouter_ObjectPermissionTable
from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_EndUserTable(EmbRouterPydanticObjectBase):
    user_id: str
    blocked: bool
    alias: str | None = None
    spend: float = 0.0
    allowed_model_region: Literal["eu", "us"] | None = None
    default_model: str | None = None
    budget_id: str | None = None
    embrouter_budget_table: EmbRouter_BudgetTable | None = None
    object_permission_id: str | None = None
    object_permission: EmbRouter_ObjectPermissionTable | None = None

    @model_validator(mode="before")
    @classmethod
    def set_model_info(cls, values):
        if values.get("spend") is None:
            values.update({"spend": 0.0})
        return values

    model_config = ConfigDict(protected_namespaces=())
