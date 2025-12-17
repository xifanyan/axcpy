from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class ADPTaskResponse(BaseModel):
    execution_id: UUID = Field(alias="ExecutionID")
    task_type: str = Field(alias="TaskType")
    logging_enabled: bool = Field(alias="LoggingEnabled")
    progress_max: int = Field(alias="ProgressMax")
    execution_status: str = Field(alias="ExecutionStatus")
    execution_root_dir: str = Field(alias="ExecutionRootDir")
    context_id: UUID = Field(alias="ContextID")
    execution_persistent: bool = Field(alias="ExecutionPersistent")
    progress_current: int = Field(alias="ProgressCurrent")
    progress_percentage: float = Field(alias="ProgressPercentage")
    task_display_name: str | None = Field(alias="TaskDisplayName", default=None)
    execution_metadata: dict[str, Any] = Field(alias="ExecutionMetaData")

    def is_success(self) -> bool:
        return self.execution_status.lower() == "success"
