from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig


class CreateOcrJobTaskConfig(BaseTaskConfig):
    """Configuration for Create OCR Job task.

    Creates an OCR job to process documents in an engine.
    This task should be called asynchronously.
    """

    adp_createOcrJob_engineUserPassword: str = Field(default="")
    adp_createOcrJob_query: str = Field(default="*")
    adp_createOcrJob_listOfJobProperties: str = Field(default="")
    adp_createOcrJob_engineType: str = Field(default="true")
    adp_createOcrJob_AdvancedRestrictions: list[Any] = Field(default_factory=list)
    adp_createOcrJob_globalSearchJson: str = Field(default="")
    adp_createOcrJob_wait: str = Field(default="false")
    adp_createOcrJob_engineName: str | None = Field(default=None)
    adp_createOcrJob_jobDescription: str = Field(default="")
    adp_createOcrJob_applicationIdentifier: str = Field(default="")
    adp_createOcrJob_jobPriority: str = Field(default="10")
    adp_createOcrJob_jobName: str = Field(default="")
    adp_createOcrJob_restrictions: list[Any] = Field(default_factory=list)
    adp_createOcrJob_engineUserName: str | None = Field(default=None)
    adp_createOcrJob_mainQueryType: str | None = Field(default=None)
    adp_createOcrJob_applicationType: str = Field(default="")
    adp_createOcrJob_globalSearchId: str = Field(default="")
    adp_createOcrJob_jsonOutputVariable: str = Field(default="adp_createOcrJob_json_output")


class CreateOcrJobResult(BaseModel):
    """Result from Create OCR Job task.

    This class is deprecated and kept for backward compatibility.
    The create_ocr_job method now returns the execution ID as a string directly.
    """

    pass


__all__ = [
    "CreateOcrJobTaskConfig",
    "CreateOcrJobResult",
]
