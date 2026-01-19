# Agent Guidelines for axcpy

## Development Commands

### Environment Setup
```bash
# Setup development environment with all extras
uv sync --all-extras
```

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_adp/test_client.py

# Run specific test function
uv run pytest tests/test_adp/test_client.py::test_adp_client_initialization

# Run tests with coverage
uv run pytest --cov=src/axcpy

# Run tests in verbose mode
uv run pytest -v
```

### Code Quality
```bash
# Lint with ruff
uv run ruff check src/ tests/

# Format with ruff
uv run ruff format src/ tests/

# Type check with mypy
uv run mypy src/

# Run all quality checks (lint + typecheck)
uv run ruff check src/ tests/ && uv run mypy src/
```

## Code Style Guidelines

### Imports
- Always start with `from __future__ import annotations`
- Standard library → third-party → local imports (separated by blank lines)
- Use absolute imports for internal modules: `from axcpy.adp import ADPClient`
- Group related imports together

### Formatting
- Line length: 100 characters (configured in ruff)
- Use ruff for both linting and formatting
- ruff selects: E, F, I, N, W, UP

### Type Hints
- Type hints required on all functions and methods
- Use modern union syntax: `str | None` (not `Optional[str]`)
- Use generic type syntax: `list[str]`, `dict[str, str]`
- Explicit `None` return type: `def method(self) -> None:`
- Pydantic models use `Field()` for default values

### Naming Conventions
- Classes: `PascalCase` (ADPClient, Session)
- Functions/methods: `snake_case` (list_entities, run_task)
- Variables/attributes: `snake_case` (base_url, auth_username)
- Constants: `UPPER_SNAKE_CASE` (AUTH_USERNAME_HEADER)
- Private members: `_prefix` (_client, _default_headers)

### Pydantic Models
- Inherit from `BaseModel` or `BaseTaskConfig`
- Use `Field()` for all default values and descriptions
- Field names in snake_case (Python) but may map to camelCase (API)
- Use `default_factory=list` for mutable collections
- Separate Config and Result models for task operations
- Define `__all__` list for explicit exports

### Error Handling
- Use `response.raise_for_status()` for HTTP errors
- Raise descriptive exceptions: `RuntimeError`, `ValueError`
- Validate response status before processing (e.g., `if status != "success"`)
- Try/except around JSON parsing with fallback handling
- Include context in error messages (task type, status, etc.)

### Logging
- Get logger by module name: `logger = logging.getLogger(__name__)`
- Check log level before expensive operations: `if logger.isEnabledFor(logging.DEBUG)`
- Log request/response payloads in debug mode only
- Don't configure logging handlers in library code

### Async/Sync Patterns
- Mirror sync API with async equivalents (AsyncADPClient, AsyncSession)
- Use `httpx.AsyncClient` for async operations
- Implement `__aenter__`/`__aexit__` for async context managers
- Use `await` for all async client calls
- Keep sync and async implementations identical where possible

### Documentation
- Google-style docstrings with Parameters and Returns sections
- Brief one-line summary followed by detailed description
- Include example shapes in Result model docstrings
- Mark untestable code with `# pragma: no cover`

### Testing
- Use pytest with pytest-asyncio and pytest-httpx
- Test files mirror source structure in `tests/`
- Descriptive test names: `test_adp_client_initialization`
- Use fixtures for common data (defined in `tests/conftest.py`)
- Type hints on test functions: `def test_something() -> None:`

### Resource Management
- Implement context managers for clients (`__enter__`/`__exit__`)
- Implement async context managers for async clients (`__aenter__`/`__aexit__`)
- Provide explicit `close()` methods
- Sessions share client instances (don't close client on session close)
- Always use `with` statements or explicit cleanup in tests

### Project Structure
- Organize by feature: `src/axcpy/{adp,searchwebapi,cli}/`
- Separate `models/` and `services/` subdirectories
- Use `__init__.py` with `__all__` for clean public API
- Auto-generated code (Kiota) goes in `generated/` subdirectory
- Keep external API surface minimal and explicit

### Configuration Management
- Use pydantic-settings for CLI/config if needed
- Keep configuration in Pydantic models with Field() defaults
- Support optional features via extras (dev, api, searchwebapi)
- API specs in `.json` files for code generation reference
