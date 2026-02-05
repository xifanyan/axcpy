from __future__ import annotations

from pydantic import BaseModel, Field

from .base import BaseTaskConfig


class CreateDataSourceTaskConfig(BaseTaskConfig):
    """Configuration for Create Data Source task.

    Creates a new data source in an ADP application.
    """

    adp_createDataSource_abortOnExistingDataSource: bool = Field(default=False)
    adp_createDataSource_applicationIdentifier: str | None = Field(default=None)
    adp_createDataSource_choosenHostNameParameter: str = Field(default="adp_hostname")
    adp_createDataSource_choosenHostMemoryRatio: str = Field(
        default="adp_chosen_host_memory_ratio"
    )
    adp_createDataSource_chosenHostCpuLoad: str = Field(
        default="adp_chosen_host_cpu_load"
    )
    adp_createDataSource_dataSourceSystemTemplateDisplayName: str = Field(
        default="Server - file share"
    )
    adp_createDataSource_usedTemplate: str = Field(
        default="adp_used_data_source_template"
    )
    adp_createDataSource_hostCpuLoadThreshold: str = Field(default="50")
    adp_createDataSource_createdDataSourceNameParameter: str = Field(
        default="adp_created_data_source_name"
    )
    adp_createDataSource_retryMaxNumberRunningCrawlers: str = Field(default="30")
    adp_createDataSource_choosenHostMemory: str = Field(
        default="adp_chosen_host_memory"
    )
    adp_createDataSource_workspaceIdentifier: str | None = Field(default=None)
    adp_createDataSource_hostIdentifier: str | None = Field(default=None)
    adp_createDataSource_hostMemoryLimit: str = Field(default="0")
    adp_createDataSource_maxNumberRunningCrawlers: str = Field(default="0")
    adp_createDataSource_engineIdentifier: str | None = Field(default=None)
    adp_createDataSource_engineBoxDocThreshold: str = Field(default="1000000")
    adp_createDataSource_hostMemoryLimitRatio: str = Field(default="0")
    adp_createDataSource_choosenEngineNameParameter: str = Field(
        default="adp_chosen_engine"
    )
    adp_createDataSource_hostRolesBlackList: str | None = Field(default=None)
    adp_createDataSource_dataSourceIdentifier: str = Field(default="{datasource_id}")
    adp_createDataSource_createdDataSourceDisplaynameParameter: str = Field(
        default="adp_created_data_source_displayname"
    )
    adp_createDataSource_dataSourceTemplate: str = Field(default="")
    adp_createDataSource_dataSourceName: str = Field(default="{datasource_name}")


class CreateDataSourceResult(BaseModel):
    """Result from Create Data Source task.

    Contains output metadata keys populated by the task execution.

    Example:
    {
        "adp_hostname": "host-crawler-01",
        "adp_chosen_host_cpu_load": "25.5",
        "adp_chosen_host_memory_ratio": "0.45",
        "adp_chosen_host_memory": "16384",
        "adp_used_data_source_template": "Server - file share",
        "adp_created_data_source_name": "DS_FileShare_001",
        "adp_created_data_source_displayname": "File Share Data Source 001",
        "adp_chosen_engine": "engine-01"
    }
    """

    adp_hostname: str | None = None
    adp_chosen_host_cpu_load: str | None = None
    adp_chosen_host_memory_ratio: str | None = None
    adp_chosen_host_memory: str | None = None
    adp_used_data_source_template: str | None = None
    adp_created_data_source_name: str | None = None
    adp_created_data_source_displayname: str | None = None
    adp_chosen_engine: str | None = None


__all__ = [
    "CreateDataSourceTaskConfig",
    "CreateDataSourceResult",
]
