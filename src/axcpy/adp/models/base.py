from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ["BaseTaskConfig"]


class BaseTaskConfig(BaseModel):
    """Shared ADP task configuration fields.

    These fields appear across multiple task configuration payloads and were
    previously duplicated in `ListEntitiesTaskConfig`. Centralizing them here
    reduces repetition and eases future extension.
    """

    adp_loggingEnabled: bool = Field(default=True)
    adp_executionPersistent: bool = Field(default=True)
    adp_progressTaskTimeout: int = Field(default=0)
    adp_taskActive: bool = Field(default=True)
    adp_taskTimeout: int = Field(default=0)
    adp_cleanUpHistory: bool = Field(default=False)
