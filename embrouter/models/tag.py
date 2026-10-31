"""
Tag table model.

Canonical definition for ``embrouter_tagtable``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from datetime import datetime

from pydantic import model_validator

from embrouter.models.budget import EmbRouter_BudgetTable
from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_TagTable(EmbRouterPydanticObjectBase):
    tag_name: str
    description: str | None = None
    models: list[str] = []
    model_info: dict | None = None
    spend: float = 0.0
    budget_id: str | None = None
    embrouter_budget_table: EmbRouter_BudgetTable | None = None
    created_at: datetime | None = None
    created_by: str | None = None
    updated_at: datetime | None = None

    @model_validator(mode="before")
    @classmethod
    def set_model_info(cls, values):
        if values.get("spend") is None:
            values.update({"spend": 0.0})
        if values.get("models") is None:
            values.update({"models": []})
        return values
