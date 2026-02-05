from __future__ import annotations

from axcpy.adp.models.start_application import (
    StartApplicationResult,
    StartApplicationTaskConfig,
)


def test_start_application_config_defaults() -> None:
    """Test StartApplicationTaskConfig with default values."""
    config = StartApplicationTaskConfig()
    assert config.adp_startApplication_applicationIdentifier == (
        "{adp_create_application_application_identifier}"
    )
    assert config.adp_startApplication_useHttps is False
    assert config.adp_startApplication_applicationUrl == "adp_started_application_url"
    assert config.adp_abortWfOnFailure is True
    assert config.adp_loggingEnabled is True
    assert config.adp_taskActive is True


def test_start_application_config_custom() -> None:
    """Test StartApplicationTaskConfig with custom values."""
    config = StartApplicationTaskConfig(
        adp_startApplication_applicationIdentifier="my-app-id",
        adp_startApplication_useHttps=True,
        adp_startApplication_applicationUrl="custom_url_var",
    )
    assert config.adp_startApplication_applicationIdentifier == "my-app-id"
    assert config.adp_startApplication_useHttps is True
    assert config.adp_startApplication_applicationUrl == "custom_url_var"


def test_start_application_result() -> None:
    """Test StartApplicationResult with URL."""
    result = StartApplicationResult(adp_started_application_url="http://localhost:8080/myapp")
    assert result.adp_started_application_url == "http://localhost:8080/myapp"


def test_start_application_result_none() -> None:
    """Test StartApplicationResult with None URL."""
    result = StartApplicationResult(adp_started_application_url=None)
    assert result.adp_started_application_url is None


def test_start_application_result_default() -> None:
    """Test StartApplicationResult with default values."""
    result = StartApplicationResult()
    assert result.adp_started_application_url is None


def test_start_application_result_from_dict() -> None:
    """Test StartApplicationResult parsing from dict."""
    data = {"adp_started_application_url": "https://example.com/app"}
    result = StartApplicationResult(**data)
    assert result.adp_started_application_url == "https://example.com/app"


def test_start_application_config_json_dump() -> None:
    """Test StartApplicationTaskConfig JSON serialization."""
    config = StartApplicationTaskConfig(
        adp_startApplication_applicationIdentifier="test-app",
        adp_startApplication_useHttps=True,
    )
    json_data = config.model_dump()
    assert json_data["adp_startApplication_applicationIdentifier"] == "test-app"
    assert json_data["adp_startApplication_useHttps"] is True


def test_start_application_request_creation() -> None:
    """Test that ADPTaskRequest can be created with StartApplicationTaskConfig."""
    from axcpy.adp.models.request import ADPTaskRequest

    config = StartApplicationTaskConfig(
        adp_startApplication_applicationIdentifier="test-app-123",
    )

    request = ADPTaskRequest(
        taskType="Start Application",
        taskConfiguration=config,
        taskDisplayName="Start application",
        taskDescription="Starts an application",
    )

    assert request.taskType == "Start Application"
    assert isinstance(request.taskConfiguration, StartApplicationTaskConfig)
    assert request.taskDisplayName == "Start application"

    # Test payload generation
    payload = request.as_payload()
    assert payload["taskType"] == "Start Application"
    assert "taskConfiguration" in payload
    config_dict = payload["taskConfiguration"]
    assert isinstance(config_dict, dict)
    assert config_dict["adp_startApplication_applicationIdentifier"] == "test-app-123"
