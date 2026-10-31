"""Single source of truth for whether ``embrouter.request_timeout`` was configured.

``embrouter.request_timeout`` always holds a value (the package default,
:data:`~embrouter.constants.DEFAULT_REQUEST_TIMEOUT_SECONDS`), so a bare read can't
tell "user asked for this" from "nobody set it". This resolver answers that:

* ``request_timeout_explicitly_set`` is the authoritative signal, set when the
  value comes from the ``REQUEST_TIMEOUT`` env var or ``embrouter_settings``.
* A runtime value that differs from the package default (e.g. ``embrouter.request_timeout
  = 300`` in SDK code) is also treated as explicit, for backwards compatibility.
"""

from __future__ import annotations

from typing import Final

from embrouter.constants import DEFAULT_REQUEST_TIMEOUT_SECONDS


def get_configured_request_timeout() -> float | None:
    """Return the explicitly-configured ``embrouter.request_timeout``, else ``None``."""
    import embrouter

    timeout: Final = float(embrouter.request_timeout)
    if embrouter.request_timeout_explicitly_set:
        return timeout
    if timeout != float(DEFAULT_REQUEST_TIMEOUT_SECONDS):
        return timeout
    return None
