from __future__ import annotations

import json
from typing import Any, Callable, TypedDict, NotRequired

from .list_entities import ListEntitiesResult
from .manage_host_roles import ManageHostRolesResult
from .query_engine import QueryEngineResult
from .read_configuration import ConfigurationInfo, ReadConfigurationResult
from .taxonomy_statistic import TaxonomyStatisticResult, TaxonomyStatisticsOutput
from .export_documents import ExportDocumentsResult


class _TaskSpec(TypedDict):
    """Specification for a task type supported by `Session.run_task`.

    Keys
    ----
    task_type: str
        Wire value placed in the ADP task request ("taskType").
    display_name: str
        Human readable display name used in the payload.
    description: str
        Longer description placed in the request.
    parser: Callable[[dict], Any]
        Function that converts executionMetaData (dict) into a typed Result model.
    defaults: dict[str, Any] (optional)
        Configuration attribute overrides applied to the TaskConfig instance *before* request
        construction. These always overwrite user-provided values.
    """

    task_type: str
    display_name: str
    description: str
    parser: Callable[[dict], Any]
    defaults: NotRequired[dict[str, Any]]


TASK_SPECS: dict[str, _TaskSpec] = {
    "list_entities": {
        "task_type": "List Entities",
        "display_name": "List Entities",
        "description": "List entities from ADP service",
        "defaults": {
            "adp_listEntities_whiteList": "id,displayName,hostName",
        },
        "parser": lambda md: ListEntitiesResult(
            adp_entities_output_file_name=md.get("adp_entities_output_file_name", ""),
            adp_entities_json_output=(
                json.loads(md.get("adp_entities_json_output", "[]"))
                if isinstance(md.get("adp_entities_json_output"), str)
                else md.get("adp_entities_json_output", [])
            ),
        ),
    },
    "manage_host_roles": {
        "task_type": "Manage Host Roles",
        "display_name": "Manage Host Roles",
        "description": "Manage roles for hosts",
        "parser": lambda md: ManageHostRolesResult(
            adp_manageHostRoles_output_file_name=md.get(
                "adp_manageHostRoles_output_file_name", ""
            ),
            adp_manageHostRoles_json_output=(
                json.loads(md.get("adp_manageHostRoles_json_output", "{}"))
                if isinstance(md.get("adp_manageHostRoles_json_output"), str)
                else md.get("adp_manageHostRoles_json_output", {})
            ),
        ),
    },
    "read_configuration": {
        "task_type": "Read Configuration",
        "display_name": "Read Configuration",
        "description": "A Task to read configurations into JSON or XML.",
        "defaults": {
            # default value for those 2 output fields probably got copied from another task; adjust to match task name
            "adp_readConfiguration_outputJson": "adp_readConfiguration_json_output",
            "adp_readConfiguration_outputFilename": "adp_readConfiguration_output_file_name",
        },
        "parser": lambda md: ReadConfigurationResult(
            adp_readConfiguration_output_file_name=md.get(
                "adp_readConfiguration_output_file_name", ""
            ),
            adp_readConfiguration_json_output={
                name: ConfigurationInfo(**cfg)
                for name, cfg in (
                    (
                        json.loads(md.get("adp_readConfiguration_json_output", "{}"))
                        if isinstance(md.get("adp_readConfiguration_json_output"), str)
                        else md.get("adp_readConfiguration_json_output", {})
                    ).items()
                )
            },
        ),
    },
    "query_engine": {
        "task_type": "Query Engine",
        "display_name": "Query engine",
        "description": "Queries an engine",
        "parser": lambda md: QueryEngineResult(
            adp_query_engine_aggregated_value=md.get(
                "adp_query_engine_aggregated_value"
            ),
            adp_query_engine_documents_count=(
                int(md.get("adp_query_engine_documents_count", 0))
                if md.get("adp_query_engine_documents_count") is not None
                else None
            ),
        ),
    },
    "taxonomy_statistic": {
        "task_type": "Taxonomy Statistic",
        "display_name": "Taxonomy statistic",
        "description": "Retrieves category counts for a taxonomy",
        "defaults": {
            "adp_taxonomyStatistic_outputJson": "adp_taxonomy_statistics_json_output",
        },
        "parser": lambda md: TaxonomyStatisticResult(
            adp_taxonomy_statistics_json_output=(
                TaxonomyStatisticsOutput(
                    **json.loads(md.get("adp_taxonomy_statistics_json_output"))
                )
                if md.get("adp_taxonomy_statistics_json_output")
                and isinstance(md.get("adp_taxonomy_statistics_json_output"), str)
                else (
                    TaxonomyStatisticsOutput(
                        **md.get("adp_taxonomy_statistics_json_output")
                    )
                    if md.get("adp_taxonomy_statistics_json_output")
                    and isinstance(md.get("adp_taxonomy_statistics_json_output"), dict)
                    else None
                )
            ),
        ),
    },
    "export_documents": {
        "task_type": "Export Documents",
        "display_name": "Export documents task",
        "description": "Export documents in CSV format.",
        "parser": lambda md: ExportDocumentsResult(
            adp_exportDocuments_searchResultSize=(
                int(md.get("adp_exportDocuments_searchResultSize", 0))
                if md.get("adp_exportDocuments_searchResultSize") is not None
                else None
            ),
            adp_exportDocuments_exportFileName=md.get(
                "adp_exportDocuments_exportFileName"
            ),
            adp_exportDocuments_exportPath=md.get("adp_exportDocuments_exportPath"),
        ),
    },
}

__all__ = ["_TaskSpec", "TASK_SPECS"]
