from dataclasses import fields
from datetime import datetime, timezone
from typing import Any, Dict, List, Mapping, Tuple

import pytest

from embrouter.repositories.unit_of_work import (
    LinkedSpendResetWrites,
    budget_cascade_unit_of_work,
    spend_reset_unit_of_work,
)


class FakeBatchTable:
    def __init__(self, table_name: str, calls: List[Tuple[str, Dict[str, Any], Dict[str, Any]]]):
        self._table_name = table_name
        self._calls = calls

    def update(self, where: Mapping[str, object], data: Mapping[str, object]) -> None:
        self._calls.append((self._table_name, dict(where), dict(data)))

    def update_many(self, where: Mapping[str, object], data: Mapping[str, object]) -> None:
        self._calls.append((f"{self._table_name}.update_many", dict(where), dict(data)))


class FakeBatch:
    def __init__(self):
        self.calls: List[Tuple[str, Dict[str, Any], Dict[str, Any]]] = []
        self.commit_count = 0
        self.embrouter_verificationtoken = FakeBatchTable("embrouter_verificationtoken", self.calls)
        self.embrouter_usertable = FakeBatchTable("embrouter_usertable", self.calls)
        self.embrouter_teamtable = FakeBatchTable("embrouter_teamtable", self.calls)
        self.embrouter_budgettable = FakeBatchTable("embrouter_budgettable", self.calls)
        self.embrouter_teammembership = FakeBatchTable("embrouter_teammembership", self.calls)
        self.embrouter_organizationtable = FakeBatchTable("embrouter_organizationtable", self.calls)
        self.embrouter_tagtable = FakeBatchTable("embrouter_tagtable", self.calls)
        self.embrouter_modelaccessgroupbudgettable = FakeBatchTable("embrouter_modelaccessgroupbudgettable", self.calls)
        self.embrouter_projecttable = FakeBatchTable("embrouter_projecttable", self.calls)
        self.embrouter_endusertable = FakeBatchTable("embrouter_endusertable", self.calls)

    async def commit(self) -> None:
        self.commit_count += 1


async def test_updates_across_tables_share_one_batch_and_commit_once():
    batch = FakeBatch()
    reset_at = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)

    async with spend_reset_unit_of_work(lambda: batch) as uow:
        uow.keys.queue_spend_reset(token="tok-1", budget_reset_at=reset_at, spend_decrement=1.5)
        uow.users.queue_spend_reset(user_id="user-1", budget_reset_at=reset_at, spend_decrement=2.5)
        uow.teams.queue_spend_reset(team_id="team-1", budget_reset_at=None, spend_decrement=0.0)
        assert batch.commit_count == 0

    assert batch.commit_count == 1
    assert batch.calls == [
        ("embrouter_verificationtoken", {"token": "tok-1"}, {"spend": {"decrement": 1.5}, "budget_reset_at": reset_at}),
        ("embrouter_usertable", {"user_id": "user-1"}, {"spend": {"decrement": 2.5}, "budget_reset_at": reset_at}),
        ("embrouter_teamtable", {"team_id": "team-1"}, {"spend": {"decrement": 0.0}, "budget_reset_at": None}),
    ]


async def test_raising_inside_block_skips_commit():
    batch = FakeBatch()

    async def _blow_up_mid_transaction():
        async with spend_reset_unit_of_work(lambda: batch) as uow:
            uow.keys.queue_spend_reset(token="tok-1", budget_reset_at=None, spend_decrement=0.0)
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        await _blow_up_mid_transaction()

    assert batch.commit_count == 0


async def test_empty_block_still_commits_the_batch():
    batch = FakeBatch()

    async with spend_reset_unit_of_work(lambda: batch):
        pass

    assert batch.commit_count == 1
    assert batch.calls == []


async def test_budget_cascade_dependents_and_window_advance_share_one_batch():
    batch = FakeBatch()
    reset_at = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)
    linked = {"budget_id": {"in": ["budget-1"]}}

    async with budget_cascade_unit_of_work(lambda: batch) as uow:
        uow.team_memberships.queue_spend_zero(where=linked)
        uow.keys.queue_spend_zero(where=linked)
        uow.organizations.queue_spend_zero(where=linked)
        uow.tags.queue_spend_zero(where=linked)
        uow.model_access_groups.queue_spend_zero(where=linked)
        uow.projects.queue_spend_zero(where=linked)
        uow.endusers.queue_spend_zero(where={"user_id": {"in": ["enduser-1"]}})
        uow.budgets.queue_window_advance(budget_id="budget-1", budget_reset_at=reset_at)
        assert batch.commit_count == 0

    assert batch.commit_count == 1
    assert batch.calls == [
        ("embrouter_teammembership.update_many", linked, {"spend": 0}),
        ("embrouter_verificationtoken.update_many", linked, {"spend": 0}),
        ("embrouter_organizationtable.update_many", linked, {"spend": 0}),
        ("embrouter_tagtable.update_many", linked, {"spend": 0}),
        ("embrouter_modelaccessgroupbudgettable.update_many", linked, {"spend": 0}),
        ("embrouter_projecttable.update_many", linked, {"spend": 0}),
        ("embrouter_endusertable.update_many", {"user_id": {"in": ["enduser-1"]}}, {"spend": 0}),
        ("embrouter_budgettable.update_many", {"budget_id": "budget-1"}, {"budget_reset_at": reset_at}),
    ]


async def test_budget_window_advance_tolerates_a_tier_deleted_mid_chunk():
    """A tier deleted between the read and the commit must not abort the batch:
    ``update`` raises P2025 on a missing row and takes every other write in the
    chunk down with it, while ``update_many`` just matches nothing."""
    batch = FakeBatch()

    async with budget_cascade_unit_of_work(lambda: batch) as uow:
        uow.budgets.queue_window_advance(budget_id="budget-1", budget_reset_at=datetime.now(timezone.utc))

    assert [call[0] for call in batch.calls] == ["embrouter_budgettable.update_many"]


async def test_every_cascade_dependent_writes_to_its_own_table_on_the_one_batch():
    """Walks the dataclass instead of naming tables, so a dependent added to
    BudgetCascadeUnitOfWork later cannot go uncovered.

    The named test above only proves the tables it lists, and an unbound
    dependent surfaces as an AttributeError from whichever tests happen to
    open a cascade. This pins the real contract: every field writes, each to a
    distinct table, all on the same batch.
    """
    reset_at = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)
    batches: List[FakeBatch] = []

    def _new_batch() -> FakeBatch:
        # Fresh per call like db.batch_(), unlike the `lambda: batch` above: a
        # second transaction would otherwise alias onto the first and hide.
        batches.append(FakeBatch())
        return batches[-1]

    async with budget_cascade_unit_of_work(_new_batch) as uow:
        writes = [getattr(uow, field.name) for field in fields(uow)]
        for write in writes:
            if isinstance(write, LinkedSpendResetWrites):
                write.queue_spend_zero(where={"budget_id": "budget-1"})
            else:
                write.queue_window_advance(budget_id="budget-1", budget_reset_at=reset_at)

    assert len(batches) == 1, "the cascade must open exactly one transaction"
    batch = batches[0]
    assert len(batch.calls) == len(writes), "a dependent bound to a batch of its own would not land here"
    assert len({call[0] for call in batch.calls}) == len(writes), "two dependents share one table"
    assert batch.commit_count == 1


async def test_budget_cascade_raising_inside_block_skips_commit():
    """A failure part-way through must leave budget_reset_at where it was, so
    the tier is still due on the next tick."""
    batch = FakeBatch()

    async def _blow_up_mid_transaction():
        async with budget_cascade_unit_of_work(lambda: batch) as uow:
            uow.team_memberships.queue_spend_zero(where={"budget_id": {"in": ["budget-1"]}})
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        await _blow_up_mid_transaction()

    assert batch.commit_count == 0
