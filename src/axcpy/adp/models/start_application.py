from __future__ import annotations

from pydantic import BaseModel, Field

from .base import BaseTaskConfig

# ruff: noqa: N815 - Field names must match API specification

__all__ = ["StartApplicationTaskConfig", "StartApplicationResult"]


class StartApplicationTaskConfig(BaseTaskConfig):
    """Configuration model for Start Application task."""

    adp_startApplication_applicationIdentifier: str = Field(
        default="{adp_create_application_application_identifier}"
    )
    adp_startApplication_useHttps: bool = Field(default=False)
    adp_startApplication_applicationUrl: str = Field(default="adp_started_application_url")
    adp_abortWfOnFailure: bool = Field(default=True)


class StartApplicationResult(BaseModel):
    """Typed representation of Start Application execution metadata.

    Example shape:
    {
        "adp_started_application_url": "http://hostname:port/project"
    }

    The application URL can be used to access the started application.
    """

    adp_started_application_url: str | None = None
