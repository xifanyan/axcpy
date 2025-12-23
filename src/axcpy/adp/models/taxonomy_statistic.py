from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, model_validator

from .base import BaseTaskConfig


class SearchParameter(BaseModel):
    """Search parameter used in taxonomy statistics."""

    key: str
    value: str


class OutputTaxonomy(BaseModel):
    """Output taxonomy configuration argument."""

    Taxonomy: str
    Mode: str = Field(default="Category counts")
    MaximumNumberOfCategories: int = Field(default=100)


class CategoryProperties(BaseModel):
    """Properties of a category."""

    model_config = {"extra": "allow"}


class Category(BaseModel):
    """Category information in a taxonomy."""

    id: str
    displayName: str
    properties: dict[str, list[str]] = Field(default_factory=dict)
    count: int | None = None


class Taxonomy(BaseModel):
    """Taxonomy information."""

    id: str
    category: list[Category] = Field(default_factory=list)


class TaxonomyStatistics(BaseModel):
    """Statistics container for taxonomies."""

    taxonomy: list[Taxonomy] = Field(default_factory=list)


class TaxonomyStatisticsOutput(BaseModel):
    """Complete taxonomy statistics output structure."""

    date: str
    searchParameter: list[SearchParameter] = Field(default_factory=list)
    statistics: TaxonomyStatistics


class TaxonomyStatisticTaskConfig(BaseTaskConfig):
    """Configuration for Taxonomy Statistic task.

    Retrieves category counts for a taxonomy with various search parameters.
    """

    adp_taxonomyStatistic_outputJsonAbsFilePath: str = Field(
        default="adp_taxonomy_statistics_json_file_path"
    )
    adp_taxonomyStatistic_applicationIdentifier: str | None = Field(default=None)
    adp_taxonomyStatistic_mainQueryType: str | None = Field(default=None)
    adp_taxonomyStatistic_engineUserName: str = Field(default="{adp_user}")
    adp_taxonomyStatistic_applicationType: str = Field(default="")
    adp_taxonomyStatistic_computeCounts: str = Field(default="true")
    adp_taxonomyStatistic_outputJsonFilePath: str | None = Field(default=None)
    adp_taxonomyStatistic_engineTaxonomies: list[Any] = Field(default_factory=list)
    adp_taxonomyStatistic_engineUserPassword: str = Field(default="")
    adp_taxonomyStatistic_outputXmlAbsFilePath: str = Field(
        default="adp_taxonomy_statistics_xml_file_path"
    )
    adp_taxonomyStatistic_engineQuery: str = Field(default="*")
    adp_taxonomyStatistic_listCategoryProperties: str = Field(default="false")
    adp_taxonomyStatistic_outputTaxonomies: list[OutputTaxonomy] = Field(
        default_factory=list
    )
    adp_taxonomyStatistic_outputJson: str = Field(
        default="adp_taxonomy_statistics_json_output"
    )
    adp_taxonomyStatistic_engineType: str = Field(default="true")
    adp_taxonomyStatistic_outputXmlFilePath: str | None = Field(default=None)
    adp_taxonomyStatistic_outputFields: list[Any] = Field(default_factory=list)
    adp_taxonomyStatistic_engineGlobalSearch: str = Field(default="")
    adp_taxonomyStatistic_listDocuments: str = Field(default="false")
    adp_taxonomyStatistic_engineName: str | None = Field(default=None)

    @model_validator(mode="after")
    def validate_identifier_exclusivity(self):
        """Ensure applicationIdentifier and engineName are not both set."""
        app_id = self.adp_taxonomyStatistic_applicationIdentifier
        engine_name = self.adp_taxonomyStatistic_engineName

        # Check if both are provided (not None and not empty string)
        if app_id and engine_name:
            raise ValueError(
                "Cannot specify both adp_taxonomyStatistic_applicationIdentifier "
                "and adp_taxonomyStatistic_engineName at the same time. "
                "Please provide only one."
            )

        # Ensure at least one is provided
        if not app_id and not engine_name:
            raise ValueError(
                "Must specify either adp_taxonomyStatistic_applicationIdentifier "
                "or adp_taxonomyStatistic_engineName."
            )

        return self


class TaxonomyStatisticResult(BaseModel):
    """Result from Taxonomy Statistic task.

    Contains output metadata keys populated by the task execution.

    Example:
    {
        "adp_taxonomy_statistics_json_output": {
            "date": "Tue Dec 23 16:22:41 EST 2025",
            "searchParameter": [
                {"key": "rm_main", "value": "[*]"},
                {"key": "rm_pagesize", "value": "[-1]"}
            ],
            "statistics": {
                "taxonomy": [
                    {
                        "id": "rm_document_hold",
                        "category": [
                            {
                                "id": "Demo_Review",
                                "displayName": "Demo_Review",
                                "count": 14322
                            },
                            ...
                        ]
                    }
                ]
            }
        }
    }
    """

    adp_taxonomy_statistics_json_output: TaxonomyStatisticsOutput | None = None


__all__ = [
    "TaxonomyStatisticTaskConfig",
    "TaxonomyStatisticResult",
    "TaxonomyStatisticsOutput",
    "TaxonomyStatistics",
    "Taxonomy",
    "Category",
    "SearchParameter",
    "OutputTaxonomy",
]
