"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def mock_api_key() -> str:
    """Mock API key for testing."""
    return "test-api-key-12345"


@pytest.fixture
def mock_base_url() -> str:
    """Mock base URL for testing."""
    return "https://test.axcelerate.example.com"
