from typing import Final

from fastapi import Request


def get_embrouter_virtual_key(request: Request) -> str:
    """
    Extract and format API key from request headers.
    Prioritizes x-embrouter-api-key over Authorization header.


    Vertex JS SDK uses `Authorization` header, we use `x-embrouter-api-key` to pass embrouter virtual key

    """
    embrouter_api_key: Final = request.headers.get("x-embrouter-api-key")
    if embrouter_api_key:
        return f"Bearer {embrouter_api_key}"
    return request.headers.get("Authorization", "")
