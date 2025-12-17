"""ADP-specific exceptions."""

from axcpy.common.exceptions import AxcelerateException


class ADPException(AxcelerateException):
    """Base exception for ADP client errors."""

    pass


class ADPAuthenticationError(ADPException):
    """Authentication failed."""

    pass


class ADPNotFoundError(ADPException):
    """Resource not found."""

    pass


class ADPValidationError(ADPException):
    """Validation error."""

    pass


class ADPRateLimitError(ADPException):
    """Rate limit exceeded."""

    pass
