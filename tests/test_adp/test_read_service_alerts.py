"""Test read_service_alerts models."""

from datetime import datetime

from axcpy.adp.models.read_service_alerts import (
    ReadServiceAlertsResult,
    ReadServiceAlertsTaskConfig,
    ServiceAlert,
)


def test_service_alert() -> None:
    """Test ServiceAlert model."""
    alert = ServiceAlert(
        message="Test alert message",
        id="alert-001",
        identification="test-identification",
        alternative_identification="alt-identification",
        host_name="server.example.com",
        applications=["app1", "app2"],
        severity="high",
        report_on=datetime(2026, 1, 19, 10, 30, 0),
    )
    assert alert.message == "Test alert message"
    assert alert.id == "alert-001"
    assert alert.identification == "test-identification"
    assert alert.alternative_identification == "alt-identification"
    assert alert.host_name == "server.example.com"
    assert len(alert.applications) == 2
    assert alert.applications == ["app1", "app2"]
    assert alert.severity == "high"
    assert alert.report_on == datetime(2026, 1, 19, 10, 30, 0)


def test_service_alert_with_defaults() -> None:
    """Test ServiceAlert model with default values."""
    alert = ServiceAlert(
        id="alert-002",
        message="Another alert",
    )
    assert alert.message == "Another alert"
    assert alert.id == "alert-002"
    assert alert.identification == ""
    assert alert.alternative_identification == ""
    assert alert.host_name == ""
    assert alert.applications == []
    assert alert.severity == ""
    assert alert.report_on is None


def test_service_alert_json_serialization() -> None:
    """Test ServiceAlert JSON serialization with aliases."""
    alert = ServiceAlert(
        message="Test alert",
        id="alert-003",
        host_name="server.test.com",
        applications=["app1"],
        severity="low",
    )
    serialized = alert.model_dump(by_alias=True)
    assert "hostName" in serialized
    assert "alternativeIdentification" in serialized
    assert "reportOn" in serialized
    assert "applications" in serialized
    assert serialized["hostName"] == "server.test.com"
    assert serialized["applications"] == ["app1"]


def test_read_service_alerts_config() -> None:
    """Test ReadServiceAlertsTaskConfig model."""
    config = ReadServiceAlertsTaskConfig(
        adp_readServiceAlerts_blacklist="test1|test2",
        adp_readServiceAlerts_lastDate="2026-01-01",
        adp_readServiceAlerts_listOfProperties="id,severity,message",
        adp_readServiceAlerts_maximum="100",
    )
    assert config.adp_readServiceAlerts_blacklist == "test1|test2"
    assert config.adp_readServiceAlerts_lastDate == "2026-01-01"
    assert config.adp_readServiceAlerts_listOfProperties == "id,severity,message"
    assert config.adp_readServiceAlerts_maximum == "100"
    assert config.adp_abortWfOnFailure is True
    assert config.adp_loggingEnabled is True


def test_read_service_alerts_config_defaults() -> None:
    """Test ReadServiceAlertsTaskConfig model with defaults."""
    config = ReadServiceAlertsTaskConfig()
    assert config.adp_readServiceAlerts_blacklist == ""
    assert config.adp_readServiceAlerts_date is None
    assert config.adp_readServiceAlerts_lastDate == ""
    assert config.adp_readServiceAlerts_listOfProperties == ""
    assert config.adp_readServiceAlerts_maximum == ""
    assert config.adp_readServiceAlerts_outputJson == "adp_readServiceAlerts_json_output"
    assert config.adp_abortWfOnFailure is True
    assert config.adp_loggingEnabled is True
    assert config.adp_executionPersistent is True


def test_read_service_alerts_result() -> None:
    """Test ReadServiceAlertsResult model."""
    alerts = [
        ServiceAlert(
            message="First alert",
            id="alert-1",
            severity="high",
        ),
        ServiceAlert(
            message="Second alert",
            id="alert-2",
            severity="low",
        ),
    ]
    result = ReadServiceAlertsResult(adp_readServiceAlerts_json_output=alerts)
    assert len(result.adp_readServiceAlerts_json_output) == 2
    assert result.adp_readServiceAlerts_json_output[0].id == "alert-1"
    assert result.adp_readServiceAlerts_json_output[1].id == "alert-2"


def test_read_service_alerts_result_empty() -> None:
    """Test ReadServiceAlertsResult model with empty list."""
    result = ReadServiceAlertsResult()
    assert result.adp_readServiceAlerts_json_output == []
    assert len(result.adp_readServiceAlerts_json_output) == 0


def test_read_service_alerts_config_output_json() -> None:
    """Test ReadServiceAlertsTaskConfig with custom outputJson."""
    config = ReadServiceAlertsTaskConfig(
        adp_readServiceAlerts_outputJson="custom_output_key",
    )
    assert config.adp_readServiceAlerts_outputJson == "custom_output_key"


def test_service_alert_with_applications_list() -> None:
    """Test ServiceAlert with applications list."""
    alert = ServiceAlert(
        message="Multi-app alert",
        id="alert-004",
        applications=["app1", "app2", "app3", "app4"],
        host_name="server.example.com",
    )
    assert len(alert.applications) == 4
    assert "app1" in alert.applications
    assert "app4" in alert.applications


def test_service_alert_parsing_from_dict() -> None:
    """Test parsing ServiceAlert from dictionary (simulating API response)."""
    alert_data = {
        "message": "API alert",
        "id": "api-001",
        "identification": "api-id",
        "alternativeIdentification": "alt-api-id",
        "hostName": "api-server.example.com",
        "applications": ["web", "api"],
        "severity": "critical",
        "reportOn": "2026-01-19T12:00:00Z",
    }
    alert = ServiceAlert(**alert_data)
    assert alert.message == "API alert"
    assert alert.id == "api-001"
    assert alert.host_name == "api-server.example.com"
    assert alert.applications == ["web", "api"]
    assert alert.severity == "critical"


def test_read_service_alerts_config_json_dump() -> None:
    """Test ReadServiceAlertsTaskConfig JSON serialization."""
    config = ReadServiceAlertsTaskConfig(
        adp_readServiceAlerts_maximum="50",
        adp_readServiceAlerts_blacklist="ignore",
    )
    dumped = config.model_dump(exclude_unset=True)
    assert "adp_readServiceAlerts_maximum" in dumped
    assert "adp_readServiceAlerts_blacklist" in dumped
    assert dumped["adp_readServiceAlerts_maximum"] == "50"
    assert dumped["adp_readServiceAlerts_blacklist"] == "ignore"


def test_read_service_alerts_result_parsing() -> None:
    """Test parsing ReadServiceAlertsResult from API-like response."""
    response_data = {
        "adp_readServiceAlerts_json_output": [
            {
                "message": "Alert 1",
                "id": "1",
                "severity": "high",
            },
            {
                "message": "Alert 2",
                "id": "2",
                "severity": "low",
            },
        ]
    }
    result = ReadServiceAlertsResult(**response_data)
    assert len(result.adp_readServiceAlerts_json_output) == 2
    assert result.adp_readServiceAlerts_json_output[0].message == "Alert 1"
    assert result.adp_readServiceAlerts_json_output[1].severity == "low"


if __name__ == "__main__":
    test_service_alert()
    print("[+] ServiceAlert test passed")
    test_service_alert_with_defaults()
    print("[+] ServiceAlert with defaults test passed")
    test_service_alert_json_serialization()
    print("[+] ServiceAlert JSON serialization test passed")
    test_read_service_alerts_config()
    print("[+] ReadServiceAlertsTaskConfig test passed")
    test_read_service_alerts_config_defaults()
    print("[+] ReadServiceAlertsTaskConfig defaults test passed")
    test_read_service_alerts_result()
    print("[+] ReadServiceAlertsResult test passed")
    test_read_service_alerts_result_empty()
    print("[+] ReadServiceAlertsResult empty test passed")
    test_read_service_alerts_config_output_json()
    print("[+] ReadServiceAlertsTaskConfig outputJson test passed")
    test_service_alert_with_applications_list()
    print("[+] ServiceAlert applications list test passed")
    test_service_alert_parsing_from_dict()
    print("[+] ServiceAlert parsing from dict test passed")
    test_read_service_alerts_config_json_dump()
    print("[+] ReadServiceAlertsTaskConfig JSON dump test passed")
    test_read_service_alerts_result_parsing()
    print("[+] ReadServiceAlertsResult parsing test passed")
    print("\nAll tests passed!")
