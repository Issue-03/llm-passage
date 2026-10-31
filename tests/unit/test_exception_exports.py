"""
Test that all standard HTTP error exceptions are exported from embrouter.__init__.
"""

import embrouter


def test_permission_denied_error_is_exported():
    """PermissionDeniedError (403) should be accessible as embrouter.PermissionDeniedError."""
    assert hasattr(embrouter, "PermissionDeniedError")
    assert embrouter.PermissionDeniedError is not None


def test_all_http_error_exceptions_exported():
    """All standard HTTP error exceptions should be accessible at module level."""
    expected_exceptions = [
        "BadRequestError",  # 400
        "AuthenticationError",  # 401
        "PermissionDeniedError",  # 403
        "NotFoundError",  # 404
        "Timeout",  # 408
        "UnprocessableEntityError",  # 422
        "RateLimitError",  # 429
        "InternalServerError",  # 500
        "BadGatewayError",  # 502
        "ServiceUnavailableError",  # 503
    ]
    for exc_name in expected_exceptions:
        assert hasattr(
            embrouter, exc_name
        ), f"embrouter.{exc_name} is not exported from embrouter.__init__"
