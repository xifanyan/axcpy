"""Common exceptions for axcpy."""


class AxcelerateException(Exception):
    """Base exception for all axcpy errors."""

    pass


class ConfigurationError(AxcelerateException):
    """Configuration error."""

    pass


class AuthenticationError(AxcelerateException):
    """Authentication failed."""

    pass


class APIError(AxcelerateException):
    """API request failed."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
