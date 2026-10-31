"""
Test filter_out_embrouter_params helper function.
"""

from typing import Final


import embrouter
from embrouter.utils import filter_out_embrouter_params


def test_filter_out_embrouter_params():
    """
    Test that filter_out_embrouter_params removes EmbRouter internal parameters
    while keeping provider-specific parameters.
    """
    kwargs = {
        "query": "test query",
        "max_results": 10,
        "shared_session": "mock_session_object",
        "metadata": {"key": "value"},
        "embrouter_trace_id": "trace-123",
        "proxy_server_request": {"url": "http://example.com"},
        "secret_fields": {"api_key": "secret"},
        "custom_param": "should_be_kept",
    }

    filtered = filter_out_embrouter_params(kwargs=kwargs)

    # Provider-specific params are kept
    assert filtered["query"] == "test query"
    assert filtered["max_results"] == 10
    assert filtered["custom_param"] == "should_be_kept"

    # EmbRouter internal params are removed
    assert "shared_session" not in filtered
    assert "metadata" not in filtered
    assert "embrouter_trace_id" not in filtered
    assert "proxy_server_request" not in filtered
    assert "secret_fields" not in filtered


def test_filter_out_embrouter_params_also_drops_the_excluded_names():
    kwargs = {"temperature": 0.2, "top_k": 5, "embrouter_trace_id": "trace-1", "_embrouter_control": object()}

    assert filter_out_embrouter_params(kwargs, excluding=("temperature",)) == {"top_k": 5}


def test_filter_out_embrouter_params_sees_a_name_appended_to_the_public_list_after_import():
    embrouter.all_embrouter_params.append("registered_later")
    try:
        filtered: Final = filter_out_embrouter_params({"registered_later": 1, "top_k": 2})
    finally:
        embrouter.all_embrouter_params.remove("registered_later")

    assert filtered == {"top_k": 2}
