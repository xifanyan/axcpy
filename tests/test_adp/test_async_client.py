"""Tests for async ADP client."""

import pytest
from axcpy.adp import AsyncADPClient, AsyncSession
from axcpy.adp.models import ADPTaskRequest, BaseTaskConfig

TEST_BASE_URL = "https://test.axcelerate.example.com"


@pytest.mark.asyncio
async def test_async_adp_client_initialization() -> None:
    """Test async ADP client initialization."""
    client = AsyncADPClient(base_url=TEST_BASE_URL)

    assert client.base_url == TEST_BASE_URL
    assert client.ignore_tls is False
    assert client.debug is False

    await client.close()


@pytest.mark.asyncio
async def test_async_adp_client_with_options() -> None:
    """Test async ADP client initialization with options."""
    client = AsyncADPClient(
        base_url=TEST_BASE_URL,
        ignore_tls=True,
        debug=True,
        timeout=60.0,
        headers={"Custom-Header": "value"},
    )

    assert client.base_url == TEST_BASE_URL
    assert client.ignore_tls is True
    assert client.debug is True

    await client.close()


@pytest.mark.asyncio
async def test_async_adp_client_context_manager() -> None:
    """Test async ADP client as context manager."""
    async with AsyncADPClient(base_url=TEST_BASE_URL) as client:
        assert client is not None
        assert client.base_url == TEST_BASE_URL


@pytest.mark.asyncio
async def test_async_session_initialization() -> None:
    """Test async session initialization."""
    client = AsyncADPClient(base_url=TEST_BASE_URL)

    try:
        session = AsyncSession(
            client=client,
            auth_username="testuser",
            auth_password="testpass",
        )

        assert session.auth_username == "testuser"
        assert session.auth_password == "testpass"
        assert session.client == client

    finally:
        await client.close()


@pytest.mark.asyncio
async def test_async_session_context_manager() -> None:
    """Test async session as context manager."""
    client = AsyncADPClient(base_url=TEST_BASE_URL)

    try:
        async with AsyncSession(client, "user", "pass") as session:
            assert session is not None
            assert session.auth_username == "user"
    finally:
        await client.close()
