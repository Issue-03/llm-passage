"""
SSO (Single Sign-On) related modules for EmbRouter Proxy.

This package contains custom SSO implementations and utilities.
"""

from embrouter.proxy.management_endpoints.sso.custom_microsoft_sso import (
    CustomMicrosoftSSO,
)

__all__ = ["CustomMicrosoftSSO"]
