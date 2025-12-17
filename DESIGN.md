# Axcelerate Python Client Library - Design Document

## Project Overview

**axcpy** is a Python client library and toolset for interacting with OpenText Axcelerate, an eDiscovery service platform. The project provides programmatic access to Axcelerate's REST APIs through well-structured client libraries, a command-line interface, and potential web service integration.

## Goals and Objectives

- Provide robust Python client libraries for Axcelerate's REST services
- Enable automation of eDiscovery workflows
- Offer both programmatic and CLI access to Axcelerate services
- Maintain type safety and comprehensive documentation
- Support future extension with FastAPI web service

## System Architecture

```
┌──────────────────────────────────────────────────────┐
│                     axcpy Project                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ┌────────────────┐           ┌──────────────────┐   │
│  │   CLI Layer    │           │  FastAPI Service │   │
│  │   (Typer)      │           │    (Future)      │   │
│  └────────┬───────┘           └────────┬─────────┘   │
│           │                            │             │
│           └─────────┬──────────────────┘             │
│                     │                                │
│  ┌──────────────────▼───────────────────────┐        │
│  │         Client Libraries Layer           │        │
│  ├──────────────────────────────────────────┤        │
│  │  ┌─────────────┐    ┌────────────────┐   │        │
│  │  │ ADP Client  │    │ SearchWebAPI   │   │        │
│  │  │  (Manual)   │    │ Client (Kiota) │   │        │
│  │  └──────┬──────┘    └──────┬─────────┘   │        │
│  └─────────┼──────────────────┼─────────────┘        │
│            │                  │                      │
└────────────┼──────────────────┼──────────────────────┘
             │                  │
             ▼                  ▼
    ┌─────────────────┐  ┌─────────────────┐
    │   ADP REST API  │  │ SearchWebAPI    │
    │   (Axcelerate)  │  │ (OpenAPI 3.x)   │
    └─────────────────┘  └─────────────────┘
```

## Technology Stack

### Core Technologies
- **Python**: 3.9+ (for modern type hints and features)
- **Package Manager**: `uv` (fast Python package and environment manager)
- **HTTP Client**: `httpx` (async support for future scalability)
- **CLI Framework**: `typer` (modern, type-based CLI)
- **Code Generation**: Microsoft Kiota (for SearchWebAPI OpenAPI client)
- **Serialization**: `pydantic` (data validation and settings management)

### Future Technologies
- **Web Framework**: FastAPI (REST API service)
- **API Documentation**: Swagger/OpenAPI
- **Testing**: pytest, pytest-asyncio

## Project Structure

```
axcpy/
├── README.md                    # Project overview and quick start
├── DESIGN.md                    # This document
├── LICENSE                      # License information
├── pyproject.toml              # Project configuration and dependencies
├── uv.lock                     # uv lockfile for reproducible builds
├── .python-version             # Python version specification for uv
├── .gitignore                  # Git ignore rules
│
├── src/
│   └── axcpy/
│       ├── __init__.py         # Package initialization
│       ├── __version__.py      # Version information
│       │
│       ├── adp/                # ADP Client Library
│       │   ├── __init__.py
│       │   ├── client.py       # Main ADP client class
│       │   ├── models.py       # Pydantic models for ADP
│       │   ├── exceptions.py   # ADP-specific exceptions
│       │   └── endpoints/      # Organized endpoint methods
│       │       ├── __init__.py
│       │       ├── cases.py
│       │       ├── documents.py
│       │       └── search.py
│       │
│       ├── searchwebapi/       # SearchWebAPI Client (Kiota-generated)
│       │   ├── __init__.py
│       │   ├── client.py       # Wrapper/adapter for generated client
│       │   └── generated/      # Kiota-generated code
│       │       └── ...         # Auto-generated files
│       │
│       ├── common/             # Shared utilities
│       │   ├── __init__.py
│       │   ├── auth.py         # Authentication handlers
│       │   ├── config.py       # Configuration management
│       │   ├── http.py         # HTTP utilities and middleware
│       │   └── exceptions.py   # Common exceptions
│       │
│       ├── cli/                # Command-line interface
│       │   ├── __init__.py
│       │   ├── main.py         # CLI entry point
│       │   ├── adp_commands.py # ADP CLI commands
│       │   └── search_commands.py # SearchWebAPI CLI commands
│       │
│       └── api/                # FastAPI service (Future)
│           ├── __init__.py
│           ├── main.py         # FastAPI app
│           ├── routes/
│           └── middleware/
│
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── conftest.py            # Pytest configuration
│   ├── test_adp/              # ADP client tests
│   ├── test_searchwebapi/     # SearchWebAPI tests
│   └── test_cli/              # CLI tests
│
├── docs/                       # Documentation
│   ├── index.md
│   ├── getting-started.md
│   ├── api-reference/
│   └── examples/
│
├── examples/                   # Usage examples
│   ├── adp_examples.py
│   ├── search_examples.py
│   └── combined_workflow.py
│
└── scripts/                    # Build and utility scripts
    ├── generate_searchwebapi.sh  # Kiota generation script
    └── setup_dev.sh              # Development setup (using uv)
```

## Component Design

### 1. ADP Client Library

**Purpose**: Manually crafted REST client for ADP service

**Key Features**:
- Type-safe request/response models using Pydantic
- Organized endpoint modules (cases, documents, search)
- Comprehensive error handling
- Authentication management
- Retry logic and rate limiting

**Example API**:
```python
from axcpy.adp import ADPClient

client = ADPClient(
    base_url="https://axcelerate.example.com/adp",
    api_key="your-api-key"
)

# Get case information
case = await client.cases.get(case_id=123)

# Search documents
results = await client.search.query(
    case_id=123,
    query="contract AND date:[2020 TO 2023]"
)
```

### 2. SearchWebAPI Client Library

**Purpose**: OpenAPI 3.x based client generated with Microsoft Kiota

**Key Features**:
- Auto-generated from OpenAPI specification
- Strongly-typed request/response models
- Built-in serialization/deserialization
- Wrapper layer for convenience methods

**Generation Process**:
```bash
# Generate client from OpenAPI spec
kiota generate \
  --language python \
  --openapi openapi.yaml \
  --output src/axcpy/searchwebapi/generated \
  --class-name SearchWebAPIClient \
  --namespace-name axcpy.searchwebapi.generated
```

**Example API**:
```python
from axcpy.searchwebapi import SearchWebAPIClient

client = SearchWebAPIClient(
    base_url="https://axcelerate.example.com/search",
    credentials=credentials
)

# Execute search
search_results = await client.search.execute(
    query_params={"q": "document search"}
)
```

### 3. Common Utilities

**Authentication Handler**:
```python
class AuthHandler:
    """Handles various authentication methods"""
    - API Key authentication
    - OAuth 2.0 flow
    - Token refresh
    - Credential storage
```

**Configuration Management**:
```python
class AxcelerateConfig(BaseSettings):
    """Application configuration using Pydantic settings"""
    adp_base_url: str
    search_base_url: str
    api_key: Optional[str]
    timeout: int = 30
    max_retries: int = 3
```

### 4. CLI Interface

**Purpose**: Command-line interface for both libraries

**Framework**: Typer (modern, type-based CLI framework)

**Structure**:
```
axcpy [OPTIONS] COMMAND [ARGS]

Commands:
  adp      ADP service commands
  search   SearchWebAPI commands
  config   Configuration management

axcpy adp [COMMAND]
  cases list          List cases
  cases get [ID]      Get case details
  docs search [QUERY] Search documents

axcpy search [COMMAND]
  query [QUERY]       Execute search query
  export [OPTIONS]    Export search results
```

**Example Usage**:
```bash
# Configure credentials
axcpy config set --adp-url https://axcelerate.example.com/adp
axcpy config set --api-key your-api-key

# List cases
axcpy adp cases list

# Search documents
axcpy adp docs search "contract AND parties:acme"

# Execute SearchWebAPI query
axcpy search query --query "litigation hold" --format json
```

### 5. FastAPI Service (Future)

**Purpose**: REST API wrapper for internal/external consumption

**Key Features**:
- RESTful endpoints wrapping both client libraries
- Authentication and authorization
- Request validation
- Rate limiting
- API documentation (Swagger UI)

**Example Endpoints**:
```
GET  /api/v1/adp/cases
POST /api/v1/adp/search
GET  /api/v1/search/query
POST /api/v1/workflow/execute
```

## Authentication Strategy

### Supported Methods

1. **API Key Authentication**
   - Simple key-based auth
   - Passed in headers or query params

2. **OAuth 2.0** (if required)
   - Authorization code flow
   - Client credentials flow
   - Token refresh handling

3. **Configuration Sources**
   - Environment variables
   - Configuration files (.env, config.yaml)
   - CLI parameters
   - Programmatic configuration

## Error Handling

### Exception Hierarchy
```python
AxcelerateException
├── ADPException
│   ├── ADPAuthenticationError
│   ├── ADPNotFoundError
│   └── ADPValidationError
├── SearchWebAPIException
│   ├── SearchAuthenticationError
│   └── SearchQueryError
└── ConfigurationError
```

## Development Phases

### Phase 1: Foundation (Weeks 1-2)
- [ ] Project structure setup
- [ ] pyproject.toml configuration with uv
- [ ] Initialize uv environment and lockfile
- [ ] Common utilities (auth, config, HTTP)
- [ ] Basic exception handling
- [ ] Development environment setup with uv

### Phase 2: ADP Client Library (Weeks 3-4)
- [ ] Core ADP client implementation
- [ ] Pydantic models for ADP entities
- [ ] Endpoint modules (cases, documents, search)
- [ ] Authentication integration
- [ ] Unit tests for ADP client

### Phase 3: SearchWebAPI Client (Weeks 5-6)
- [ ] Obtain OpenAPI specification
- [ ] Generate client with Kiota
- [ ] Create wrapper/adapter layer
- [ ] Integration with common auth
- [ ] Unit tests for SearchWebAPI

### Phase 4: CLI Interface (Weeks 7-8)
- [ ] Typer CLI framework setup
- [ ] ADP commands implementation
- [ ] SearchWebAPI commands implementation
- [ ] Configuration commands
- [ ] CLI testing and documentation

### Phase 5: Documentation & Examples (Week 9)
- [ ] API reference documentation
- [ ] User guide and tutorials
- [ ] Code examples
- [ ] README and getting started guide

### Phase 6: FastAPI Service (Future)
- [ ] FastAPI application setup
- [ ] Endpoint implementation
- [ ] Authentication/authorization
- [ ] API documentation
- [ ] Deployment configuration

## Dependencies

### Core Dependencies
```toml
[project]
name = "axcpy"
requires-python = ">=3.9"
dependencies = [
    "httpx>=0.26.0",           # Async HTTP client
    "pydantic>=2.5.0",         # Data validation
    "typer>=0.9.0",            # CLI framework
    "rich>=13.7.0",            # CLI formatting
    "python-dotenv>=1.0.0",    # Environment management
]
```

### Development Dependencies
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-httpx>=0.30.0",
    "ruff>=0.1.0",             # Linting and formatting
    "mypy>=1.7.0",             # Type checking
]
```

### Code Generation
```toml
[tool.uv]
dev-dependencies = [
    "kiota>=1.0.0",            # OpenAPI client generator
]
```

### Future Dependencies
```toml
# To be added to [project.dependencies] when needed
fastapi = ">=0.108.0"        # Web framework
uvicorn = ">=0.25.0"         # ASGI server
```

## Environment Management with uv

### Why uv?

[uv](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver, written in Rust. Benefits include:
- **Speed**: 10-100x faster than pip
- **Reliability**: Comprehensive dependency resolution
- **Simplicity**: Single tool for environment and package management
- **Compatibility**: Drop-in replacement for pip and pip-tools
- **Lockfile**: Automatic generation of lockfiles for reproducibility

### Initial Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create new project with uv
cd axcpy
uv init

# Set Python version
echo "3.12" > .python-version

# Install dependencies
uv sync
```

### Development Workflow

```bash
# Add a new dependency
uv add httpx pydantic typer

# Add a development dependency
uv add --dev pytest ruff mypy

# Install all dependencies (including dev)
uv sync --all-extras

# Run commands in the virtual environment
uv run python -m axcpy.cli
uv run pytest

# Update dependencies
uv lock --upgrade

# Activate virtual environment (optional)
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### Building and Publishing

```bash
# Build the package
uv build

# Publish to PyPI
uv publish
```

### Project Configuration (pyproject.toml)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "axcpy"
version = "0.1.0"
description = "Python client library for OpenText Axcelerate eDiscovery service"
readme = "README.md"
requires-python = ">=3.9"
authors = [
    { name = "Your Name", email = "your.email@example.com" },
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

[project.scripts]
axcpy = "axcpy.cli.main:app"

[tool.uv]
package = true

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.mypy]
python_version = "3.9"
strict = true
```

## Configuration Management

### Configuration File (.env)
```bash
AXCELERATE_ADP_BASE_URL=https://axcelerate.example.com/adp
AXCELERATE_SEARCH_BASE_URL=https://axcelerate.example.com/search
AXCELERATE_API_KEY=your-api-key-here
AXCELERATE_TIMEOUT=30
AXCELERATE_MAX_RETRIES=3
```

### Programmatic Configuration
```python
from axcpy import configure

configure(
    adp_url="https://axcelerate.example.com/adp",
    search_url="https://axcelerate.example.com/search",
    api_key="your-api-key"
)
```

## Testing Strategy

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test client libraries against mock/test servers
3. **CLI Tests**: Test CLI commands with various inputs
4. **End-to-End Tests**: Test complete workflows
5. **Mock Services**: Use `httpx-mock` or `responses` for HTTP mocking

## Documentation Strategy

1. **README.md**: Quick start and overview
2. **API Reference**: Auto-generated from docstrings
3. **User Guide**: Comprehensive usage documentation
4. **Examples**: Practical usage examples
5. **CHANGELOG.md**: Version history and changes

## Security Considerations

1. **Credential Management**: Never hardcode credentials
2. **HTTPS Only**: Enforce secure connections
3. **Input Validation**: Validate all inputs with Pydantic
4. **Rate Limiting**: Implement client-side rate limiting
5. **Logging**: Sanitize sensitive data in logs

## Performance Considerations

1. **Async Support**: Use `httpx` for async HTTP requests
2. **Connection Pooling**: Reuse HTTP connections
3. **Caching**: Implement response caching where appropriate
4. **Pagination**: Handle large result sets efficiently
5. **Retry Logic**: Exponential backoff for failed requests

## Deployment & Distribution

### Package Distribution
- Publish to PyPI as `axcpy`
- Support installation via `pip install axcpy`
- Provide wheel and source distributions

### CLI Distribution
```bash
pip install axcpy
axcpy --version
```

### Docker Support (Future)
```dockerfile
FROM python:3.11-slim
RUN pip install axcpy
ENTRYPOINT ["axcpy"]
```

## Future Enhancements

1. **Async/Await Support**: Full async implementation
2. **Batch Operations**: Bulk API operations
3. **WebSocket Support**: Real-time updates
4. **GraphQL Support**: If Axcelerate adds GraphQL
5. **Plugin System**: Extensibility for custom integrations
6. **GUI Interface**: Optional desktop/web interface
7. **Monitoring**: Telemetry and observability

## Contributing Guidelines

1. Follow PEP 8 style guidelines
2. Add type hints to all functions
3. Write docstrings in Google style
4. Include unit tests for new features
5. Update documentation for API changes
6. Use conventional commits for commit messages

## References

- [OpenText Axcelerate Documentation](https://www.opentext.com/products/axcelerate)
- [Microsoft Kiota Documentation](https://learn.microsoft.com/en-us/openapi/kiota/)
- [Typer Documentation](https://typer.tiangolo.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Version**: 1.0  
**Last Updated**: December 17, 2025  
**Author**: Development Team  
**Status**: Planning Phase
