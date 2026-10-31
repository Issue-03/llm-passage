"""
Budget repository for database operations on EmbRouter_BudgetTable.
"""

from collections.abc import Mapping
from typing import TYPE_CHECKING, Final, Protocol

from embrouter.models.budget import EmbRouter_BudgetTable
from embrouter.repositories.base_repository import BaseRepository
from embrouter.repositories.prisma_protocols import TableActions

if TYPE_CHECKING:
    from prisma import models as prisma_models


class _BudgetDb(Protocol):
    """The single Prisma table this repository reaches for on ``prisma_client.db``."""

    @property
    def embrouter_budgettable(self) -> TableActions["prisma_models.EmbRouter_BudgetTable"]: ...


class _PrismaClientView(Protocol):
    """The one attribute this repository reads off the untyped Prisma client wrapper."""

    @property
    def db(self) -> _BudgetDb: ...


class BudgetRepository(BaseRepository[EmbRouter_BudgetTable]):
    """Repository for budget database operations."""

    @property
    def table(self) -> TableActions["prisma_models.EmbRouter_BudgetTable"]:
        client: Final[_PrismaClientView] = self.prisma_client
        return client.db.embrouter_budgettable

    @property
    def model_class(self) -> type[EmbRouter_BudgetTable]:
        return EmbRouter_BudgetTable

    async def find_by_id(self, budget_id: str, id_field: str = "budget_id") -> EmbRouter_BudgetTable | None:
        return await super().find_by_id(budget_id, id_field)

    async def create_budget(
        self,
        created_by: str,
        max_budget: float | None = None,
        soft_budget: float | None = None,
        max_parallel_requests: int | None = None,
        tpm_limit: int | None = None,
        rpm_limit: int | None = None,
        model_max_budget: Mapping[str, object] | None = None,
        budget_duration: str | None = None,
        allowed_models: list[str] | None = None,
    ) -> EmbRouter_BudgetTable:
        """Create a new budget record."""
        data: Final[dict[str, object]] = {
            "created_by": created_by,
            "updated_by": created_by,
        }
        if max_budget is not None:
            data["max_budget"] = max_budget
        if soft_budget is not None:
            data["soft_budget"] = soft_budget
        if max_parallel_requests is not None:
            data["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not None:
            data["tpm_limit"] = tpm_limit
        if rpm_limit is not None:
            data["rpm_limit"] = rpm_limit
        if model_max_budget is not None:
            data["model_max_budget"] = model_max_budget
        if budget_duration is not None:
            data["budget_duration"] = budget_duration
        if allowed_models is not None:
            data["allowed_models"] = allowed_models

        return await self.create(data)

    async def update_budget(
        self,
        budget_id: str,
        updated_by: str,
        max_budget: float | None = None,
        soft_budget: float | None = None,
        max_parallel_requests: int | None = None,
        tpm_limit: int | None = None,
        rpm_limit: int | None = None,
        model_max_budget: Mapping[str, object] | None = None,
        budget_duration: str | None = None,
        allowed_models: list[str] | None = None,
    ) -> EmbRouter_BudgetTable | None:
        """Update an existing budget record."""
        data: Final[dict[str, object]] = {"updated_by": updated_by}
        if max_budget is not None:
            data["max_budget"] = max_budget
        if soft_budget is not None:
            data["soft_budget"] = soft_budget
        if max_parallel_requests is not None:
            data["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not None:
            data["tpm_limit"] = tpm_limit
        if rpm_limit is not None:
            data["rpm_limit"] = rpm_limit
        if model_max_budget is not None:
            data["model_max_budget"] = model_max_budget
        if budget_duration is not None:
            data["budget_duration"] = budget_duration
        if allowed_models is not None:
            data["allowed_models"] = allowed_models

        return await self.update(budget_id, data, id_field="budget_id")

    async def delete_budget(self, budget_id: str) -> EmbRouter_BudgetTable | None:
        """Delete a budget record."""
        return await self.delete(budget_id, id_field="budget_id")
