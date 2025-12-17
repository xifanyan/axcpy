"""HTTP utilities and middleware."""

import httpx
from typing import Any


async def make_request(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    **kwargs: Any,
) -> httpx.Response:
    """Make an HTTP request with error handling.

    Args:
        client: HTTP client
        method: HTTP method
        url: Request URL
        **kwargs: Additional request parameters

    Returns:
        Response object

    Raises:
        httpx.HTTPError: On HTTP errors
    """
    response = await client.request(method, url, **kwargs)
    response.raise_for_status()
    return response
