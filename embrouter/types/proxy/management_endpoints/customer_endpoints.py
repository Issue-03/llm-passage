from pydantic import BaseModel, Field

from embrouter.models.budget import EmbRouter_BudgetTableFull
from embrouter.models.end_user import EmbRouter_EndUserTable


class CustomerResponse(EmbRouter_EndUserTable):
    """Customer object returned by the /customer read+write endpoints.

    Nests the full budget response model so server-managed budget fields
    (budget_reset_at, created_at) survive response_model filtering, rather than
    the narrow write-allowlist shape EmbRouter_EndUserTable carries for internal use.
    """

    embrouter_budget_table: EmbRouter_BudgetTableFull | None = None  # pyright: ignore


class BlockUsersResponse(BaseModel):
    blocked_users: list[EmbRouter_EndUserTable]


class UnblockUsersResponse(BaseModel):
    blocked_users: list[str] = Field(description="User IDs that remain blocked after this unblock call")


class DeleteCustomersResponse(BaseModel):
    deleted_customers: int
    message: str
