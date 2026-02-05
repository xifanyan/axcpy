from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class ADPTaskResponse(BaseModel):
    model_config = {"populate_by_name": True}

    execution_id: UUID = Field(alias="executionId")
    task_type: str = Field(alias="taskType")
    logging_enabled: bool | str = Field(alias="loggingEnabled")
    execution_root_dir: str = Field(alias="executionRootDir")
    context_id: UUID = Field(alias="contextId")
    execution_persistent: bool | str = Field(alias="executionPersistent")
    task_display_name: str | None = Field(alias="taskDisplayName", default=None)
    progress_max: int | None = Field(alias="progressMax", default=None)
    execution_status: str | None = Field(alias="executionStatus", default=None)
    progress_current: int | None = Field(alias="progressCurrent", default=None)
    progress_percentage: float | None = Field(alias="progressPercentage", default=None)
    execution_metadata: dict[str, Any] | None = Field(alias="executionMetaData", default=None)

    def is_success(self) -> bool:
        if self.execution_status is None:
            return False
        return self.execution_status.lower() == "success"
