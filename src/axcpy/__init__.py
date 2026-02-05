"""axcpy - Axcelerate Python Client Library.

Python client library for OpenText Axcelerate eDiscovery service.
"""

# Re-export subpackages for convenience
from axcpy import adp, searchwebapi
from axcpy.__version__ import __version__

__all__ = [
    "__version__",
    "adp",
    "searchwebapi",
]
