"""
Test that max_budget from environment variable (string) is correctly
converted to float.
GitHub Issue: #23843
"""

import pytest

import embrouter


@pytest.mark.asyncio
async def test_max_budget_string_converted_to_float():
    """
    When max_budget is set via os.environ/MAX_BUDGET, it arrives as a
    string. initialize() should convert it to float so the comparison
    `embrouter.max_budget > 0` doesn't raise TypeError.
    """
    from embrouter.proxy.proxy_server import initialize

    original = embrouter.max_budget
    try:
        await initialize(max_budget="100.5")
        assert isinstance(embrouter.max_budget, float)
        assert embrouter.max_budget == 100.5
    finally:
        embrouter.max_budget = original


@pytest.mark.asyncio
async def test_max_budget_float_stays_float():
    """max_budget as float should still work."""
    from embrouter.proxy.proxy_server import initialize

    original = embrouter.max_budget
    try:
        await initialize(max_budget=200.0)
        assert isinstance(embrouter.max_budget, float)
        assert embrouter.max_budget == 200.0
    finally:
        embrouter.max_budget = original
