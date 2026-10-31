"""
Example Custom SSO Handler

Use this if you want to run custom code after embrouter has retrieved information from your IDP (Identity Provider).

Flow:
- User lands on Admin UI
- EmbRouter redirects user to your SSO provider
- Your SSO provider redirects user back to EmbRouter
- EmbRouter has retrieved user information from your IDP
- Your custom SSO handler is called and returns an object of type SSOUserDefinedValues
- User signed in to UI
"""

from typing import Final

from fastapi_sso.sso.base import OpenID

from embrouter.proxy import proxy_server
from embrouter.proxy._types import EmbrouterUserRoles, SSOUserDefinedValues


async def custom_sso_handler(userIDPInfo: OpenID) -> SSOUserDefinedValues:
    try:
        if userIDPInfo.id is None:
            raise ValueError(f"No ID found for user. userIDPInfo.id is None {userIDPInfo}")

        # Access extra fields from the IDP response (requires GENERIC_USER_EXTRA_ATTRIBUTES env var)
        # Example: Set GENERIC_USER_EXTRA_ATTRIBUTES="group,NTID,domain" to capture these fields
        # extra_fields = getattr(userIDPInfo, 'extra_fields', None) or {}
        # user_groups = extra_fields.get("group", [])

        # check if user exists in embrouter proxy DB
        if proxy_server.prisma_client is not None:
            _user_info: Final = await proxy_server.prisma_client.get_data(user_id=userIDPInfo.id)

        return SSOUserDefinedValues(
            models=[],
            user_id=userIDPInfo.id,
            user_email=userIDPInfo.email,
            user_role=EmbrouterUserRoles.INTERNAL_USER.value,
            max_budget=10,
            budget_duration="1d",
        )
    except Exception:
        raise Exception("Failed custom auth")
