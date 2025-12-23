"""axcpy - Axcelerate Python Client Library.

Python client library for OpenText Axcelerate eDiscovery service.
"""

from axcpy.__version__ import __version__

# Re-export subpackages for convenience
from axcpy import adp
from axcpy import searchwebapi

__all__ = [
    "__version__",
    "adp",
    "searchwebapi",
]
