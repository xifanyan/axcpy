from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig


class QueryEngineTaskConfig(BaseTaskConfig):
    """Configuration for Query Engine task.

    Queries an engine with various search parameters and restrictions.
    """

    adp_queryEngine_fieldName: str = Field(default="virtual_filesize")
    adp_queryEngine_enableSiblingExpansion: str = Field(default="false")
    adp_queryEngine_engineName: str | None = Field(default=None)
    adp_queryEngine_engineUserPassword: str = Field(default="")
    adp_queryEngine_engineTaxonomies: list[Any] = Field(default_factory=list)
    adp_queryEngine_engineUserName: str | None = Field(default=None)
    adp_queryEngine_engineType: str = Field(default="true")
    adp_queryEngine_saveVariable: str | None = Field(default=None)
    adp_queryEngine_categoryToDelete: str = Field(default="")
    adp_queryEngine_activateCategoryDeletion: bool = Field(default=False)
    adp_queryEngine_applicationIdentifier: str = Field(default="")
    adp_queryEngine_taxonomyToDelete: str = Field(default="")
    adp_queryEngine_successIfCountIs: str | None = Field(default=None)
    adp_queryEngine_category: str = Field(default="")
    adp_queryEngine_activateTagging: bool = Field(default=False)
    adp_queryEngine_globalSearchId: str = Field(default="")
    adp_queryEngine_aggregatedValue: str = Field(
        default="adp_query_engine_aggregated_value"
    )
    adp_queryEngine_AdvancedRestrictions: list[Any] = Field(default_factory=list)
    adp_queryEngine_taxonomy: str = Field(default="")
    adp_queryEngine_globalSearchJson: str = Field(default="")
    adp_queryEngine_saveCompareString: str = Field(default="true")
    adp_queryEngine_numberOfDocuments: str = Field(
        default="adp_query_engine_documents_count"
    )
    adp_queryEngine_siblingFields: str = Field(default="rm_attachmentroot")
    adp_queryEngine_engineQuery: str = Field(default="*")
    adp_queryEngine_mainQueryType: str | None = Field(default=None)
    adp_queryEngine_waitForResult: bool = Field(default=False)
    adp_queryEngine_categoryDisplayName: str = Field(default="")
    adp_queryEngine_waitWhileCountIs: str | None = Field(default=None)
    adp_queryEngine_applicationType: str = Field(default="")
    adp_queryEngine_exitOnValueChanged: bool = Field(default=True)


class QueryEngineResult(BaseModel):
    """Result from Query Engine task.

    Contains output metadata keys populated by the task execution.

    Example:
    {
        "adp_query_engine_aggregated_value": "524983291",
        "adp_query_engine_documents_count": "14322"
    }
    """

    adp_query_engine_aggregated_value: str | int | float | None = None
    adp_query_engine_documents_count: int | None = None


__all__ = [
    "QueryEngineTaskConfig",
    "QueryEngineResult",
]
