from __future__ import annotations

import inspect
from typing import get_args

import pytest

from axcpy.adp.models import BaseTaskConfig
from axcpy.adp.models.request import TaskConfigurationType
from axcpy.adp.models.task_spec import TASK_SPECS


def test_all_task_configs_in_union() -> None:
    """Verify that all TaskConfig classes are included in TaskConfigurationType union.

    This test ensures that when a new TaskConfig is added, it must be added to
    the TaskConfigurationType union in request.py. Otherwise, ADPTaskRequest
    will fail validation.
    """
    import axcpy.adp.models as models_module

    # Get all types in the union
    union_types = set(get_args(TaskConfigurationType))

    # Find all TaskConfig classes defined in the models module
    task_config_classes = set()
    for name, obj in inspect.getmembers(models_module, inspect.isclass):
        # Check if it's a TaskConfig (inherits from BaseTaskConfig, but not BaseTaskConfig itself)
        if (
            name.endswith("TaskConfig")
            and name != "BaseTaskConfig"
            and issubclass(obj, BaseTaskConfig)
            and obj is not BaseTaskConfig
        ):
            task_config_classes.add(obj)

    # Find configs that are defined but missing from the union
    missing_from_union = task_config_classes - union_types

    if missing_from_union:
        missing_names = [cls.__name__ for cls in missing_from_union]
        pytest.fail(
            f"The following TaskConfig classes are not included in TaskConfigurationType union:\n"
            f"{', '.join(missing_names)}\n\n"
            f"Please add them to the union in src/axcpy/adp/models/request.py"
        )


def test_all_task_specs_have_matching_config() -> None:
    """Verify that all task specs have their corresponding TaskConfig in the union.

    This ensures that task specs registered in TASK_SPECS can actually be used
    with ADPTaskRequest.

    Note: This test uses fuzzy matching to handle variations in naming conventions
    (e.g., "OCR" vs "Ocr", "and" vs "And").
    """
    union_types = set(get_args(TaskConfigurationType))
    # Create lowercase versions for fuzzy matching
    union_names_lower = {t.__name__.lower(): t.__name__ for t in union_types}

    # Map common patterns to find the TaskConfig name from task key
    missing_specs = []
    for task_key, spec in TASK_SPECS.items():
        # Try to infer the config class name from the task_type
        # Most follow pattern: "Task Type" -> "TaskTypeTaskConfig"
        task_type = spec["task_type"]
        expected_config_lower = (task_type.replace(" ", "") + "TaskConfig").lower()

        # Check if there's a matching config (case-insensitive)
        if expected_config_lower not in union_names_lower:
            missing_specs.append((task_key, task_type, expected_config_lower))

    if missing_specs:
        error_msg = "The following task specs do not have their TaskConfig in the union:\n"
        for key, task_type, expected in missing_specs:
            error_msg += f"  - Task '{key}' (type: {task_type}) expects a config like {expected}\n"
        error_msg += "\nPlease add the missing configs to TaskConfigurationType in request.py"
        pytest.fail(error_msg)


def test_task_config_union_not_empty() -> None:
    """Ensure the TaskConfigurationType union has at least one type."""
    union_types = get_args(TaskConfigurationType)
    assert len(union_types) > 0, "TaskConfigurationType union should not be empty"


def test_all_union_types_are_task_configs() -> None:
    """Verify that all types in the union are actually TaskConfig classes."""
    union_types = get_args(TaskConfigurationType)

    for config_type in union_types:
        assert issubclass(config_type, BaseTaskConfig), (
            f"{config_type.__name__} should inherit from BaseTaskConfig"
        )
        assert config_type.__name__.endswith("TaskConfig"), (
            f"{config_type.__name__} should end with 'TaskConfig'"
        )
