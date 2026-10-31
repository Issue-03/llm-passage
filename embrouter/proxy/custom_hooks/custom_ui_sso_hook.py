from typing import Final

from fastapi import Request
from fastapi_sso.sso.base import OpenID

from embrouter._logging import verbose_logger
from embrouter.integrations.custom_logger import CustomLogger
from embrouter.proxy.common_utils.http_parsing_utils import _safe_get_request_headers


class CustomSSOLoginHandler(CustomLogger):
    """
    Custom logger for the UI SSO sign in

    Use this to parse the request headers and return a OpenID object

    Useful when you have an OAuth proxy in front of EmbRouter
    and you want to use the headers from the proxy to sign in the user
    """

    async def handle_custom_ui_sso_sign_in(
        self,
        request: Request,
    ) -> OpenID:
        request_headers_dict: Final = _safe_get_request_headers(request)
        verbose_logger.debug("inside custom ui sso sign in hook...")
        return OpenID(
            id=request_headers_dict.get("x-embrouter-user-id") or "123",
            email=request_headers_dict.get("x-embrouter-user-email") or "test@test.com",
            first_name="Test",
            last_name="Test",
            display_name="Test",
            picture="https://test.com/test.png",
            provider="test",
        )


custom_ui_sso_sign_in_handler: Final = CustomSSOLoginHandler()
