"""Regression guard for the enterprise hook registration / import cycle.

Python 3.13 is stricter about partially-initialized modules and surfaces
cycles that Python 3.12 silently tolerated. The previous bug:

  embrouter.proxy.hooks.__init__
    -> enterprise.enterprise_hooks
    -> embrouter_enterprise.proxy.hooks.managed_files
    -> embrouter.llms.base_llm.managed_resources.isolation
    -> embrouter.proxy.management_endpoints.common_utils
    -> embrouter.proxy.utils  (re-enters embrouter.proxy.hooks mid-init)

silently swallowed the ImportError in `hooks/__init__.py`, leaving
``managed_files`` unregistered and the /files endpoint returning 500.
"""

import pytest

from embrouter.proxy.hooks import PROXY_HOOKS, get_proxy_hook


def test_managed_files_hook_registered():
    pytest.importorskip("embrouter_enterprise")
    assert "managed_files" in PROXY_HOOKS
    hook_cls = get_proxy_hook("managed_files")
    assert hook_cls.__name__ == "_PROXY_EmbRouterManagedFiles"


def test_managed_vector_stores_hook_registered():
    pytest.importorskip("embrouter_enterprise")
    assert "managed_vector_stores" in PROXY_HOOKS
    hook_cls = get_proxy_hook("managed_vector_stores")
    assert hook_cls.__name__ == "_PROXY_EmbRouterManagedVectorStores"


def test_isolation_module_does_not_pull_in_proxy_utils():
    """Layering guard: embrouter.llms.* must not transitively import
    embrouter.proxy.utils, which would reintroduce the import cycle."""
    import importlib
    import sys

    for mod in [
        "embrouter.proxy.utils",
        "embrouter.proxy.management_endpoints.common_utils",
        "embrouter.llms.base_llm.managed_resources.isolation",
    ]:
        sys.modules.pop(mod, None)

    importlib.import_module("embrouter.llms.base_llm.managed_resources.isolation")
    assert "embrouter.proxy.utils" not in sys.modules
    assert "embrouter.proxy.management_endpoints.common_utils" not in sys.modules
