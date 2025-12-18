from enum import Enum

class DeletionMode(str, Enum):
    Delete = "delete",
    Softdelete = "softdelete",

