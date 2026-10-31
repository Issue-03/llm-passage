"""Force ``embrouter.model_cost`` to load from the PR-local JSON for these tests.

By default ``embrouter.model_cost`` is fetched from the main branch on GitHub,
which lags behind PR-branch flag additions. This fixture loads the local
file so per-model flag tests pass in CI as well as locally.

"""

import pytest

import embrouter
from embrouter.embrouter_core_utils.get_model_cost_map import get_model_cost_map


@pytest.fixture(autouse=True)
def _use_pr_local_model_cost_map(monkeypatch):
    monkeypatch.setenv("EMBROUTER_LOCAL_MODEL_COST_MAP", "True")
    monkeypatch.setattr(
        embrouter,
        "model_cost",
        get_model_cost_map(url=embrouter.model_cost_map_url),
    )
    yield
