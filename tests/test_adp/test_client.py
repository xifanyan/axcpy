"""Tests for ADP client."""

import pytest
from axcpy.adp import ADPClient


def test_adp_client_initialization(mock_base_url: str) -> None:
    """Test ADP client initialization."""
    client = ADPClient(base_url=mock_base_url)

    assert client.base_url == mock_base_url
    assert client.ignore_tls is False
    assert client.debug is False

    client.close()


def test_adp_client_with_options(mock_base_url: str) -> None:
    """Test ADP client initialization with options."""
    client = ADPClient(
        base_url=mock_base_url,
        ignore_tls=True,
        debug=True,
        timeout=60.0,
        headers={"Custom-Header": "value"},
    )

    assert client.base_url == mock_base_url
    assert client.ignore_tls is True
    assert client.debug is True

    client.close()


def test_adp_client_context_manager(mock_base_url: str) -> None:
    """Test ADP client as context manager."""
    with ADPClient(base_url=mock_base_url) as client:
        assert client is not None
        assert client.base_url == mock_base_url
