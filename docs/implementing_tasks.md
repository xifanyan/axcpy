# Implementing New ADP Tasks

This guide explains how to implement a new ADP task in the axcpy library.

## Overview

When implementing a new ADP task, you need to create several interconnected pieces:
1. Task configuration and result models
2. Task specification for the registry
3. Session methods (sync and async)
4. Tests
5. **CRITICAL**: Add the config to the `TaskConfigurationType` union

## Step-by-Step Guide

### 1. Create Task Models

Create a new file in `src/axcpy/adp/models/` named after your task (e.g., `start_application.py`):

```python
from __future__ import annotations

from pydantic import BaseModel, Field

from .base import BaseTaskConfig

# ruff: noqa: N815 - Field names must match API specification

__all__ = ["YourTaskConfig", "YourTaskResult"]


class YourTaskConfig(BaseTaskConfig):
    """Configuration model for Your Task."""

    adp_yourTask_parameter1: str = Field(default="default_value")
    adp_yourTask_parameter2: bool = Field(default=False)
    # Add other fields from api_spec.json


class YourTaskResult(BaseModel):
    """Typed representation of Your Task execution metadata.

    Example shape:
    {
        "adp_yourTask_output": "result_value"
    }
    """

    adp_yourTask_output: str | None = None
```

### 2. Update `__init__.py`

Add exports in `src/axcpy/adp/models/__init__.py`:

```python
from axcpy.adp.models.your_task import (
    YourTaskResult,
    YourTaskConfig,
)

__all__ = [
    # ... existing exports ...
    "YourTaskResult",
    "YourTaskConfig",
]
```

### 3. **CRITICAL: Add to TaskConfigurationType Union**

**This is the most commonly forgotten step!**

Edit `src/axcpy/adp/models/request.py`:

```python
# Add import
from .your_task import YourTaskConfig

# Add to union
TaskConfigurationType = (
    ListEntitiesTaskConfig
    | ManageHostRolesTaskConfig
    # ... other configs ...
    | YourTaskConfig  # ← ADD THIS LINE
)
```

**If you forget this step**, you'll get Pydantic validation errors like:
```
ValidationError: Input should be a valid dictionary or instance of YourTaskConfig
```

### 4. Add Task Specification

Edit `src/axcpy/adp/models/task_spec.py`:

```python
# Add import
from .your_task import YourTaskResult

# Add to TASK_SPECS dictionary
TASK_SPECS: dict[str, _TaskSpec] = {
    # ... existing specs ...
    "your_task": {
        "task_type": "Your Task",  # Must match api_spec.json
        "display_name": "Your task",
        "description": "Description of your task",
        "parser": lambda md: YourTaskResult(
            adp_yourTask_output=md.get("adp_yourTask_output"),
        ),
    },
}
```

### 5. Add Session Methods

#### Sync Session (`src/axcpy/adp/services/session.py`)

```python
# Add import at top
from axcpy.adp.models.your_task import (
    YourTaskResult,
    YourTaskConfig,
)

# Add method in Session class
def your_task(
    self,
    config: YourTaskConfig,
    *,
    timeout: float | None = None,
) -> YourTaskResult:
    """Execute your task.

    Parameters
    ----------
    config : YourTaskConfig
        Configuration for the task.
    timeout : float | None
        Optional timeout in seconds.

    Returns
    -------
    YourTaskResult
        Result containing task output.
    """
    return self.run_task(
        "your_task",
        config=config,
        timeout=timeout,
    )
```

#### Async Session (`src/axcpy/adp/services/async_session.py`)

Same as above but with `async` keyword:

```python
async def your_task(
    self,
    config: YourTaskConfig,
    *,
    timeout: float | None = None,
) -> YourTaskResult:
    """Execute your task (async)."""
    return await self.run_task(
        "your_task",
        config=config,
        timeout=timeout,
    )
```

### 6. Create Tests

Create `tests/test_adp/test_your_task.py`:

```python
from __future__ import annotations

from axcpy.adp.models.your_task import YourTaskConfig, YourTaskResult


def test_your_task_config_defaults() -> None:
    """Test YourTaskConfig with default values."""
    config = YourTaskConfig()
    assert config.adp_yourTask_parameter1 == "default_value"
    assert config.adp_yourTask_parameter2 is False


def test_your_task_result() -> None:
    """Test YourTaskResult."""
    result = YourTaskResult(adp_yourTask_output="test")
    assert result.adp_yourTask_output == "test"


def test_your_task_request_creation() -> None:
    """Test that ADPTaskRequest can be created with YourTaskConfig."""
    from axcpy.adp.models.request import ADPTaskRequest

    config = YourTaskConfig()
    request = ADPTaskRequest(
        taskType="Your Task",
        taskConfiguration=config,
        taskDisplayName="Your task",
    )
    
    assert request.taskType == "Your Task"
    assert isinstance(request.taskConfiguration, YourTaskConfig)
```

### 7. Run Tests

```bash
# Run your specific tests
uv run pytest tests/test_adp/test_your_task.py -v

# Run all ADP tests
uv run pytest tests/test_adp/ -v

# The union enforcement test will catch if you forgot step 3
uv run pytest tests/test_adp/test_task_config_union.py -v
```

## Enforcement Mechanisms

### Automated Test

The file `tests/test_adp/test_task_config_union.py` contains tests that will **automatically fail** if:

1. **A TaskConfig class exists but is not in the union** - This catches when you forget step 3
2. **A task spec is registered but its config is missing** - This catches inconsistencies

These tests run as part of the normal test suite and will catch the most common mistake.

### Example Failure

If you forget to add your config to the union, the test will fail with:

```
FAILED tests/test_adp/test_task_config_union.py::test_all_task_configs_in_union
Failed: The following TaskConfig classes are not included in TaskConfigurationType union:
YourTaskConfig

Please add them to the union in src/axcpy/adp/models/request.py
```

## Checklist

Use this checklist when implementing a new task:

- [ ] Create models file (`your_task.py`)
- [ ] Add exports to `models/__init__.py`
- [ ] **Add config to `TaskConfigurationType` union in `request.py`** ⚠️
- [ ] Add task spec to `task_spec.py`
- [ ] Add sync method to `session.py`
- [ ] Add async method to `async_session.py`
- [ ] Create comprehensive tests
- [ ] Run all tests including `test_task_config_union.py`
- [ ] Add usage example to `examples/adp_examples.py` (optional)

## Common Mistakes

### 1. Forgetting the Union (MOST COMMON)
**Problem**: Config not added to `TaskConfigurationType`
**Symptom**: Pydantic validation errors when creating `ADPTaskRequest`
**Solution**: Add your config to the union in `request.py`

### 2. Mismatched Task Type
**Problem**: `task_type` in spec doesn't match `api_spec.json`
**Symptom**: Task fails on server or returns wrong results
**Solution**: Use exact string from `api_spec.json`

### 3. Missing Fields
**Problem**: Not all fields from `api_spec.json` are in config
**Symptom**: Task fails or uses wrong defaults
**Solution**: Review `api_spec.json` carefully

### 4. Wrong Field Defaults
**Problem**: Default values don't match `api_spec.json`
**Symptom**: Unexpected task behavior
**Solution**: Copy exact defaults from `api_spec.json`

## References

- API Specification: `src/axcpy/adp/api_spec.json`
- Task Types List: `adp_tasks_description.md`
- Code Style: `AGENTS.md`
- Existing Examples: Look at `start_application.py`, `list_entities.py`, etc.
