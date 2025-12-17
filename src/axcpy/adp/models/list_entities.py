from __future__ import annotations

from pydantic import BaseModel, Field

from typing import Any

from .base import BaseTaskConfig

__all__ = ["ListEntitiesTaskConfig", "ListEntitiesResult"]


class ListEntitiesTaskConfig(BaseTaskConfig):
    """Configuration model for List Entities task."""

    adp_listEntities_file: str = Field(default="output.json")
    adp_listEntities_numberOfEntities: str = Field(default="-1")
    adp_listEntities_axcRequestTimeoutSeconds: int = Field(default=900)
    adp_listEntities_userHasAccess: str = Field(default="")
    adp_listEntities_whiteList: str = Field(default="id,displayName")
    adp_listEntities_relatedEntity: str = Field(default="")
    adp_listEntities_workspace: str = Field(default="")
    adp_listEntities_status: str = Field(default="")
    adp_listEntities_axcServiceCoreAddress: str = Field(default="")
    adp_listEntities_relatedEntityType: str = Field(default="")
    adp_listEntities_type: str = Field(default="")
    adp_listEntities_httpsKeystoreFile: str | None = Field(default=None)
    adp_listEntities_httpsPassword: str = Field(default="")
    adp_listEntities_axcConnectTimeoutSeconds: int = Field(default=300)
    adp_listEntities_axcServicePassword: str = Field(default="")
    adp_listEntities_startingEntity: str = Field(default="1")
    adp_listEntities_outputJson: str = Field(default="adp_entities_json_output")
    adp_listEntities_descriptionSettingFilterValueDateFormat: str = Field(
        default="yyyy-MM-dd"
    )
    adp_listEntities_descriptionFilters: list[str] = Field(default_factory=list)
    adp_listEntities_axcServiceUser: str = Field(default="")
    adp_listEntities_axcFields: str = Field(default="")
    adp_listEntities_httpsTrustCertificate: str = Field(default="")
    adp_listEntities_host: str = Field(default="")
    adp_listEntities_outputFilename: str = Field(
        default="adp_entities_output_file_name"
    )
    adp_listEntities_id: str = Field(default="")
    adp_listEntities_httpsAllowUntrustedHosts: str = Field(default="true")


class ListEntitiesResult(BaseModel):
    """Typed representation of List Entities execution metadata.

    Example shape:
    {
        "adp_entities_output_file_name": "E:/MindServer/Projects/adp.adp/adpRootDir/output.json",
        "adp_entities_json_output": [
            {"id": "singleMindServer.demo01", "displayName": "Demo 01"},
            {"id": "singleMindServer.demo02", "displayName": "Demo 02"}
        ]
    }

    The entity objects may include additional fields beyond `id`; they are
    stored verbatim in the list for downstream consumers.
    """

    adp_entities_output_file_name: str
    adp_entities_json_output: list[dict[str, Any]] = []
