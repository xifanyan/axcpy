from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .base import BaseTaskConfig

__all__ = [
    "ReadConfigurationTaskConfig",
    "ReadConfigurationResult",
    "ConfigurationInfo",
    "ParameterInfo",
    "CellInfo",
    "ConfigToReadArg",
]


class ConfigToReadArg(BaseModel):
    """Configuration argument for specifying what configuration to read.

    Maps to the Go ConfigurationArg struct used in ReadConfiguration calls.
    """

    ConfigurationID: str = Field(default="", alias="Configuration ID")
    DynamicComponentNames: str = Field(default="", alias="Dynamic Component Names")
    FieldList: str = Field(default="", alias="Field list")
    NameValueList: str = Field(default="", alias="Name value list")
    ApplicationType: str = Field(default="", alias="Application type")
    EntityType: str = Field(default="", alias="Entity type")


class ReadConfigurationTaskConfig(BaseTaskConfig):
    """Configuration model for Read Configuration task."""

    adp_readConfiguration_outputJson: str = Field(default="adp_entities_json_output")
    adp_readConfiguration_configsToRead: list[ConfigToReadArg] = Field(
        default_factory=list
    )
    adp_readConfiguration_outputFilename: str = Field(
        default="adp_entities_output_file_name"
    )
    adp_readConfiguration_entityIdToRead: str = Field(default="")
    adp_readConfiguration_file: str = Field(default="output.json")
    adp_readConfiguration_fileFormat: str = Field(default="JSON")


class CellInfo(BaseModel):
    """Represents a single cell in a parameter."""

    value: Any = None
    name: str = ""


class ParameterInfo(BaseModel):
    """Represents a parameter with cells, name, and value."""

    cells: list[list[CellInfo]] = Field(default_factory=list)
    name: str = ""
    value: Any = None


class StaticInfo(BaseModel):
    """Represents static configuration information."""

    Parameters: list[ParameterInfo] = Field(default_factory=list)


class GlobalInfo(BaseModel):
    """Represents global configuration information."""

    Static: StaticInfo = Field(default_factory=StaticInfo)


class ConfigurationInfo(BaseModel):
    """Represents configuration information for a single configuration.

    Structure:
    {
        "DynamicComponents": {...},
        "Global": {
            "Static": {
                "Parameters": [
                    {
                        "cells": [[{"value": ..., "name": ...}]],
                        "name": "...",
                        "value": ...
                    }
                ]
            }
        }
    }
    """

    DynamicComponents: dict[str, Any] = Field(default_factory=dict)
    Global: GlobalInfo = Field(default_factory=GlobalInfo)


class ReadConfigurationResult(BaseModel):
    """Typed representation of Read Configuration execution metadata.

    Example shape:
    {
        "adp_readConfiguration_output_file_name": "E:/MindServer/Projects/adp.adp/adpRootDir/output.json",
        "adp_readConfiguration_json_output": {
            "configName1": {
                "DynamicComponents": {...},
                "Global": {
                    "Static": {
                        "Parameters": [...]
                    }
                }
            },
            "configName2": {...}
        }
    }

    The configuration objects are stored as a dictionary mapping configuration
    names to their respective ConfigurationInfo structures.
    """

    adp_readConfiguration_output_file_name: str
    adp_readConfiguration_json_output: dict[str, ConfigurationInfo] = Field(
        default_factory=dict
    )
