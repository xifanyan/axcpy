"""Cases endpoint implementation."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from axcpy.adp.client import ADPClient


class CasesEndpoint:
    """Handle case-related operations."""

    def __init__(self, client: "ADPClient") -> None:
        self.client = client

    async def list(self) -> list[dict]:
        """List all cases.

        Returns:
            List of cases
        """
        # TODO: Implement
        return []

    async def get(self, case_id: int) -> dict:
        """Get a specific case.

        Args:
            case_id: Case ID

        Returns:
            Case details
        """
        # TODO: Implement
        return {}
