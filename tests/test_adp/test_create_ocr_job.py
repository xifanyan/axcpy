"""Tests for Create OCR Job task."""

from __future__ import annotations

from axcpy.adp.models.create_ocr_job import (
    CreateOcrJobResult,
    CreateOcrJobTaskConfig,
)


def test_create_ocr_job_config_defaults() -> None:
    """Test Create OCR Job config default values."""
    config = CreateOcrJobTaskConfig()

    assert config.adp_createOcrJob_query == "*"
    assert config.adp_createOcrJob_wait == "false"
    assert config.adp_createOcrJob_jobPriority == "10"
    assert config.adp_createOcrJob_engineName is None
    assert config.adp_createOcrJob_AdvancedRestrictions == []
    assert config.adp_createOcrJob_restrictions == []
    assert config.adp_createOcrJob_engineUserPassword == ""
    assert config.adp_createOcrJob_engineType == "true"
    assert config.adp_createOcrJob_applicationType == ""


def test_create_ocr_job_config_custom() -> None:
    """Test Create OCR Job config with custom values."""
    config = CreateOcrJobTaskConfig(
        adp_createOcrJob_engineName="test_engine",
        adp_createOcrJob_applicationIdentifier="app.test001",
        adp_createOcrJob_jobName="Test OCR Job",
        adp_createOcrJob_query="field:value",
        adp_createOcrJob_jobPriority="5",
        adp_createOcrJob_engineUserName="testuser",
        adp_createOcrJob_jobDescription="Test description",
    )

    assert config.adp_createOcrJob_engineName == "test_engine"
    assert config.adp_createOcrJob_applicationIdentifier == "app.test001"
    assert config.adp_createOcrJob_jobName == "Test OCR Job"
    assert config.adp_createOcrJob_query == "field:value"
    assert config.adp_createOcrJob_jobPriority == "5"
    assert config.adp_createOcrJob_engineUserName == "testuser"
    assert config.adp_createOcrJob_jobDescription == "Test description"


def test_create_ocr_job_config_restrictions() -> None:
    """Test Create OCR Job config with restrictions."""
    restrictions = [{"field": "status", "value": "active"}]
    advanced = [{"type": "advanced", "condition": "true"}]

    config = CreateOcrJobTaskConfig(
        adp_createOcrJob_restrictions=restrictions,
        adp_createOcrJob_AdvancedRestrictions=advanced,
    )

    assert config.adp_createOcrJob_restrictions == restrictions
    assert config.adp_createOcrJob_AdvancedRestrictions == advanced


def test_create_ocr_job_result() -> None:
    """Test Create OCR Job result model (deprecated)."""
    result = CreateOcrJobResult()

    # CreateOcrJobResult is now an empty placeholder class
    assert isinstance(result, CreateOcrJobResult)


def test_create_ocr_job_result_none() -> None:
    """Test Create OCR Job result instantiation (deprecated)."""
    result = CreateOcrJobResult()

    assert isinstance(result, CreateOcrJobResult)


def test_create_ocr_job_result_from_dict() -> None:
    """Test Create OCR Job result from dictionary (deprecated)."""
    # Extra fields are ignored by Pydantic
    data = {"executionID": "67890"}
    result = CreateOcrJobResult(**data)

    assert isinstance(result, CreateOcrJobResult)
