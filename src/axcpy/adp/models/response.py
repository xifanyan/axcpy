from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class ADPTaskResponse(BaseModel):
    """Response model for ADP task execution results.

    This model represents the API response returned after executing any ADP task.
    It contains execution metadata, progress information, and task-specific results.

    The model uses camelCase aliases to match the ADP API response format while
    providing Pythonic snake_case attribute names for internal use.

    Attributes:
        execution_id: Unique identifier for this task execution instance.
        task_type: The type of ADP task that was executed (e.g., "list_entities",
            "query_engine", "start_application").
        logging_enabled: Whether logging is enabled for this execution. May be
            bool or string representation from the API.
        execution_root_dir: Root directory path where execution artifacts are stored.
        context_id: Unique identifier for the ADP application context.
        execution_persistent: Whether the execution state persists across sessions.
            May be bool or string representation from the API.
        task_display_name: Human-readable name for the task (optional).
        progress_max: Maximum progress value for tracking task completion (optional).
        execution_status: Current status of the execution (e.g., "SUCCESS", "FAILED",
            "RUNNING"). None if status is not yet available.
        progress_current: Current progress value (optional).
        progress_percentage: Progress as a percentage (0.0-100.0) (optional).
        execution_metadata: Task-specific metadata containing execution results.
            Structure varies by task type. Use task-specific Result models to parse
            this field (see task_spec.py TASK_SPECS for parsers).

    Example:
        >>> response = ADPTaskResponse.model_validate(api_response)
        >>> print(f"Task: {response.task_type}")
        >>> print(f"Status: {response.execution_status}")
        >>> if response.is_success():
        ...     # Parse task-specific metadata
        ...     result = ListEntitiesResult.model_validate(response.execution_metadata)
    """

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
        """Check if the task execution completed successfully.

        Returns:
            True if execution_status is "SUCCESS" (case-insensitive), False otherwise.
            Returns False if execution_status is None.

        Example:
            >>> response = ADPTaskResponse.model_validate(api_response)
            >>> if response.is_success():
            ...     print("Task completed successfully")
            ... else:
            ...     print(f"Task failed or incomplete: {response.execution_status}")
        """
        if self.execution_status is None:
            return False
        return self.execution_status.lower() == "success"
