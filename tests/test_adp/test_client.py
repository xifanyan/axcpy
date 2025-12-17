"""Tests for ADP client."""

import pytest
from axcpy.adp import ADPClient


@pytest.mark.asyncio
async def test_adp_client_initialization(mock_base_url: str, mock_api_key: str) -> None:
    """Test ADP client initialization."""
    client = ADPClient(base_url=mock_base_url, api_key=mock_api_key)

    assert client.base_url == mock_base_url
    assert client.api_key == mock_api_key

    await client.close()


@pytest.mark.asyncio
async def test_adp_client_context_manager(
    mock_base_url: str, mock_api_key: str
) -> None:
    """Test ADP client as context manager."""
    async with ADPClient(base_url=mock_base_url, api_key=mock_api_key) as client:
        assert client is not None
