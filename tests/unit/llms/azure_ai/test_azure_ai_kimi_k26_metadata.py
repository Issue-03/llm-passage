"""
Test Azure AI Kimi K2.6 model metadata.
"""

import json
from importlib.resources import files

import pytest


@pytest.fixture(scope="module")
def use_local_model_cost_map():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setenv("EMBROUTER_LOCAL_MODEL_COST_MAP", "True")

    import embrouter
    from embrouter.utils import _invalidate_model_cost_lowercase_map

    original_model_cost = embrouter.model_cost
    embrouter.model_cost = json.loads(
        files("embrouter")
        .joinpath("model_prices_and_context_window_backup.json")
        .read_text(encoding="utf-8")
    )
    embrouter.get_model_info.cache_clear()
    _invalidate_model_cost_lowercase_map()
    try:
        yield embrouter
    finally:
        embrouter.model_cost = original_model_cost
        embrouter.get_model_info.cache_clear()
        _invalidate_model_cost_lowercase_map()
        monkeypatch.undo()


