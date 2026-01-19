from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig

__all__ = [
    "ReadServiceAlertsTaskConfig",
    "ReadServiceAlertsResult",
    "ServiceAlert",
]


class ServiceAlert(BaseModel):
    """Represents a single service alert.

    Maps to the Go ServiceAlert struct.
    """

    model_config = {"populate_by_name": True}

    message: str = Field(default="")
    id: str = Field(default="")
    identification: str = Field(default="")
    alternative_identification: str = Field(default="", alias="alternativeIdentification")
    host_name: str = Field(default="", alias="hostName")
    applications: list[str] = Field(default_factory=list, alias="applications")
    severity: str = Field(default="")
    report_on: datetime | None = Field(default=None, alias="reportOn")


class ReadServiceAlertsTaskConfig(BaseTaskConfig):
    """Configuration model for Read Service Alerts task."""

    adp_readServiceAlerts_blacklist: str = Field(default="")
    adp_readServiceAlerts_date: Any = Field(default=None)
    adp_readServiceAlerts_lastDate: str = Field(default="")
    adp_readServiceAlerts_listOfProperties: str = Field(default="")
    adp_readServiceAlerts_maximum: str = Field(default="")
    adp_readServiceAlerts_outputJson: str = Field(default="adp_readServiceAlerts_json_output")
    adp_abortWfOnFailure: bool = Field(default=True)


class ReadServiceAlertsResult(BaseModel):
    """Typed representation of Read Service Alerts execution metadata.

    Example shape:
    {
        "adp_readServiceAlerts_json_output": [
            {
                "message": "Alert message",
                "id": "alert-001",
                "identification": "identification",
                "alternativeIdentification": "alternative-identification",
                "hostName": "server.example.com",
                "applications": ["app1", "app2"],
                "severity": "high",
                "reportOn": "2026-01-19T10:30:00Z"
            },
            ...
        ]
    }

    The alert objects are stored as a list of ServiceAlert structures.
    """

    adp_readServiceAlerts_json_output: list[ServiceAlert] = Field(default_factory=list)
