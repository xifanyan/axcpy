from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig

__all__ = ["ManageHostRolesTaskConfig", "ManageHostRolesResult"]


class ManageHostRolesTaskConfig(BaseTaskConfig):
    """Configuration model for Manage Host Roles task."""

    adp_manageHostRoles_outputFilename: str = Field(default="adp_manageHostRoles_output_file_name")
    adp_manageHostRoles_hostRoles: list[dict[str, Any]] = Field(default_factory=list)
    adp_manageHostRoles_filterForAutomatedCreation: str = Field(default="false")
    adp_manageHostRoles_extJson: str = Field(default="false")
    adp_manageHostRoles_file: str = Field(default="output.json")
    adp_manageHostRoles_outputJson: str = Field(default="adp_manageHostRoles_json_output")
    adp_manageHostRoles_hostIdsToFilterFor: str = Field(default="")
    adp_manageHostRoles_inputJson: str = Field(default="")


class ManageHostRolesResult(BaseModel):
    """Typed representation of Manage Host Roles execution metadata.

    Example:
    {
        "adp_manageHostRoles_output_file_name": "E:/MindServer/Projects/adp.adp/adpRootDir/output.json",
        "adp_manageHostRoles_json_output": {
            "vm-rhauswirth2.otxlab.net": [
                "applicationServer",
                "crawler",
                "crawlServer",
                "ingestionApplicationServer",
                "ingestionEngineServer",
                "axcelerateApplicationServer",
                "axcelerateEngineServer",
                "engineServer",
                "batchPrintingServer",
                "conversionServer",
                "ocrServer",
                "productionServer",
                "redactionServer"
            ]
        }
    }

    The host roles are mapped by hostname to their respective role lists.
    Each hostname maps to a list of role strings that the host can perform.
    """

    adp_manageHostRoles_output_file_name: str
    adp_manageHostRoles_json_output: dict[str, list[str]] = Field(default_factory=dict)
