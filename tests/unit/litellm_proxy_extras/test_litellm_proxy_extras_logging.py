import importlib
import logging
from collections.abc import Iterator

import pytest

import litellm_proxy_extras._logging as extras_logging


@pytest.fixture
def fresh_extras_logger() -> Iterator[logging.Logger]:
    logger = logging.getLogger("litellm_proxy_extras")
    saved_handlers = logger.handlers[:]
    saved_level = logger.level
    logger.handlers[:] = []
    try:
        yield logger
    finally:
        logger.handlers[:] = saved_handlers
        logger.setLevel(saved_level)


def test_litellm_log_error_silences_extras_info_lines(monkeypatch, fresh_extras_logger):
    monkeypatch.setenv("LITELLM_LOG", "ERROR")
    reloaded = importlib.reload(extras_logging).logger
    assert reloaded is fresh_extras_logger
    assert reloaded.isEnabledFor(logging.INFO) is False
    assert reloaded.isEnabledFor(logging.ERROR) is True


def test_unset_litellm_log_hides_extras_info_lines_but_keeps_warnings(monkeypatch, fresh_extras_logger):
    monkeypatch.delenv("LITELLM_LOG", raising=False)
    reloaded = importlib.reload(extras_logging).logger
    assert reloaded.isEnabledFor(logging.INFO) is False
    assert reloaded.isEnabledFor(logging.WARNING) is True


@pytest.mark.parametrize("litellm_log", ["info", "DEBUG"])
def test_verbose_litellm_log_shows_extras_info_lines(monkeypatch, fresh_extras_logger, litellm_log):
    monkeypatch.setenv("LITELLM_LOG", litellm_log)
    assert importlib.reload(extras_logging).logger.isEnabledFor(logging.INFO) is True
