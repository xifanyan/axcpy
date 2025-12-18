from enum import Enum

class JobStatus(str, Enum):
    RUNNING = "RUNNING",
    STOPPED = "STOPPED",
    STOPPING = "STOPPING",
    PAUSED = "PAUSED",
    PAUSING = "PAUSING",
    FATAL = "FATAL",
    FINISHING = "FINISHING",
    FINISHED = "FINISHED",
    SCHEDULED = "SCHEDULED",
    WAITING = "WAITING",
    CREATED = "CREATED",

