"""Authentication handlers for Axcelerate services."""

from typing import Protocol


class AuthHandler(Protocol):
    """Protocol for authentication handlers."""

    def get_headers(self) -> dict[str, str]:
        """Get authentication headers.

        Returns:
            Dictionary of headers
        """
        ...


class APIKeyAuth:
    """API Key authentication handler."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_headers(self) -> dict[str, str]:
        """Get headers with API key."""
        return {"Authorization": f"Bearer {self.api_key}"}


class OAuth2Auth:
    """OAuth 2.0 authentication handler."""

    def __init__(self, token: str) -> None:
        self.token = token

    def get_headers(self) -> dict[str, str]:
        """Get headers with OAuth token."""
        return {"Authorization": f"Bearer {self.token}"}
