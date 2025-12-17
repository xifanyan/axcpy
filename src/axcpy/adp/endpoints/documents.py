"""Documents endpoint implementation."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from axcpy.adp.client import ADPClient


class DocumentsEndpoint:
    """Handle document-related operations."""

    def __init__(self, client: "ADPClient") -> None:
        self.client = client

    async def get(self, document_id: str) -> dict:
        """Get a specific document.

        Args:
            document_id: Document ID

        Returns:
            Document details
        """
        # TODO: Implement
        return {}

    async def list(self, case_id: int) -> list[dict]:
        """List documents in a case.

        Args:
            case_id: Case ID

        Returns:
            List of documents
        """
        # TODO: Implement
        return []
