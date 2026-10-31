import pytest

import embrouter


@pytest.fixture(autouse=True)
def local_model_cost_map(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("EMBROUTER_LOCAL_MODEL_COST_MAP", "True")
    monkeypatch.setattr(embrouter, "model_cost", embrouter.get_model_cost_map(url=""))


def test_typesafe_models_share_pricing_and_provider_metadata():
    entries = [embrouter.model_cost[f"typesafe/{model}"] for model in ("jev-1.13.0", "jev-latest", "jev-preview")]

    assert {entry["input_cost_per_token"] for entry in entries} == {entries[0]["input_cost_per_token"]}
    assert {entry["output_cost_per_token"] for entry in entries} == {entries[0]["output_cost_per_token"]}
    assert {entry["embrouter_provider"] for entry in entries} == {"typesafe"}
