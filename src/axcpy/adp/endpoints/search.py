"""Search endpoint implementation."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from axcpy.adp.client import ADPClient


class SearchEndpoint:
    """Handle search operations."""

    def __init__(self, client: "ADPClient") -> None:
        self.client = client

    async def query(self, query: str, case_id: int | None = None) -> dict:
        """Execute a search query.

        Args:
            query: Search query string
            case_id: Optional case ID to limit search

        Returns:
            Search results
        """
        # TODO: Implement
        return {}
