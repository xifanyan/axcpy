"""Tests for ADP client."""

import pytest
from axcpy.adp import ADPClient

TEST_BASE_URL = "https://test.axcelerate.example.com"


def test_adp_client_initialization() -> None:
    """Test ADP client initialization."""
    client = ADPClient(base_url=TEST_BASE_URL)

    assert client.base_url == TEST_BASE_URL
    assert client.ignore_tls is False
    assert client.debug is False

    client.close()


def test_adp_client_with_options() -> None:
    """Test ADP client initialization with options."""
    client = ADPClient(
        base_url=TEST_BASE_URL,
        ignore_tls=True,
        debug=True,
        timeout=60.0,
        headers={"Custom-Header": "value"},
    )

    assert client.base_url == TEST_BASE_URL
    assert client.ignore_tls is True
    assert client.debug is True

    client.close()


def test_adp_client_context_manager() -> None:
    """Test ADP client as context manager."""
    with ADPClient(base_url=TEST_BASE_URL) as client:
        assert client is not None
        assert client.base_url == TEST_BASE_URL
