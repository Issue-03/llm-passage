"""
Team membership table model.

Canonical definition for ``embrouter_teammembership``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from embrouter.models.budget import EmbRouter_BudgetTable, EmbRouter_BudgetTableFull
from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_TeamMembership(EmbRouterPydanticObjectBase):
    user_id: str
    team_id: str
    budget_id: str | None = None
    spend: float | None = 0.0
    total_spend: float | None = 0.0
    embrouter_budget_table: EmbRouter_BudgetTableFull | EmbRouter_BudgetTable | None = None

    def safe_get_team_member_rpm_limit(self) -> int | None:
        if self.embrouter_budget_table is not None:
            return self.embrouter_budget_table.rpm_limit
        return None

    def safe_get_team_member_tpm_limit(self) -> int | None:
        if self.embrouter_budget_table is not None:
            return self.embrouter_budget_table.tpm_limit
        return None
