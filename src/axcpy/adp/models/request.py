from __future__ import annotations

from pydantic import BaseModel, Field

from .create_data_source import CreateDataSourceTaskConfig
from .export_documents import ExportDocumentsTaskConfig
from .list_entities import ListEntitiesTaskConfig
from .manage_host_roles import ManageHostRolesTaskConfig
from .manage_users_and_groups import ManageUsersAndGroupsTaskConfig
from .query_engine import QueryEngineTaskConfig
from .read_configuration import ReadConfigurationTaskConfig
from .taxonomy_statistic import TaxonomyStatisticTaskConfig

# ruff: noqa: N815 - Field names must match API specification

TaskConfigurationType = (
    ListEntitiesTaskConfig
    | ManageHostRolesTaskConfig
    | ManageUsersAndGroupsTaskConfig
    | QueryEngineTaskConfig
    | ReadConfigurationTaskConfig
    | TaxonomyStatisticTaskConfig
    | ExportDocumentsTaskConfig
    | CreateDataSourceTaskConfig
)


class ADPTaskRequest(BaseModel):
    """Generic ADP task request model.

    Provides a payload that can be sent via PUT to the ADP service.
    Field names intentionally mirror expected wire format (taskType, taskConfiguration, etc.).
    """

    taskType: str
    taskConfiguration: TaskConfigurationType
    taskDescription: str = Field(default="")
    taskDisplayName: str = Field(default="")

    def as_payload(self) -> dict[str, object]:
        """Generate the payload for the ADP service."""

        return {
            "taskType": self.taskType,
            "taskConfiguration": self.taskConfiguration.model_dump(
                exclude_defaults=True, by_alias=True
            ),
            "taskDescription": self.taskDescription,
            "taskDisplayName": self.taskDisplayName,
        }


__all__ = ["ADPTaskRequest", "TaskConfigurationType"]
