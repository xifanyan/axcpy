from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig


class ExportDocumentsTaskConfig(BaseTaskConfig):
    """Configuration for Export Documents task.

    Export documents from an engine in CSV format.
    """

    adp_exportDocuments_field_separator: str = Field(default=";")
    adp_exportDocuments_waitForExport: bool = Field(default=False)
    adp_exportDocuments_image_field: str | None = Field(default=None)
    adp_exportDocuments_searchResultSize: str = Field(
        default="adp_exportDocuments_searchResultSize"
    )
    adp_exportDocuments_File_Ending: str = Field(default="csv")
    adp_exportDocuments_applicationType: str = Field(default="")
    adp_exportDocuments_query: str = Field(default="*")
    adp_exportDocuments_exportName: str | None = Field(default=None)
    adp_exportDocuments_text_indicator: str = Field(default='"')
    adp_exportDocuments_natives_field: str | None = Field(default=None)
    adp_exportDocuments_multivalue_separator: str = Field(default="|")
    adp_exportDocuments_line_break: str = Field(default="")
    adp_exportDocuments_applicationIdentifier: str = Field(default="")
    adp_exportDocuments_engineIdentifier: str | None = Field(default=None)
    adp_exportDocuments_exportFileName: str = Field(
        default="adp_exportDocuments_exportFileName"
    )
    adp_exportDocuments_engineUser: str | None = Field(default=None)
    adp_exportDocuments_image_volume: str = Field(default="Volume")
    adp_exportDocuments_exportFields: str | None = Field(default=None)
    adp_exportDocuments_fullExportPath: str = Field(
        default="adp_exportDocuments_exportPath"
    )
    adp_exportDocuments_text_field: str | None = Field(default=None)
    adp_exportDocuments_exportDirectory: str | None = Field(default=None)
    adp_exportDocuments_enginePassword: str | None = Field(default=None)
    adp_exportDocuments_adp_exportDocuments_mainQueryType: str | None = Field(
        default=None
    )


class ExportDocumentsResult(BaseModel):
    """Result from Export Documents task.

    Contains output metadata keys populated by the task execution.
    """

    adp_exportDocuments_searchResultSize: int | None = None
    adp_exportDocuments_exportFileName: str | None = None
    adp_exportDocuments_exportPath: str | None = None


__all__ = [
    "ExportDocumentsTaskConfig",
    "ExportDocumentsResult",
]
