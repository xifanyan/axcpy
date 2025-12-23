# Axcelerate Python Client Library - Design Document

## Project Overview

**axcpy** is a Python client library and toolset for interacting with OpenText Axcelerate, an eDiscovery service platform. The project provides programmatic access to Axcelerate's ADP (Axcelerate Data Platform) REST API and SearchWebAPI through well-structured client libraries, a command-line interface, and potential web service integration.

The library emphasizes type safety, modern Python practices, and developer experience through comprehensive tooling and documentation.

## Current Status (December 2025)

**✅ Production Ready:**
- **ADP Client**: Fully implemented with sync/async support, 5+ task types, comprehensive models
- **SearchWebAPI Client**: Generated with Kiota, tested and working with session management
- **Package Structure**: Unified package with optional dependencies for flexibility

**🚧 In Progress:**
- CLI interface (basic structure in place, commands in development)
- Documentation (DESIGN doc complete, API reference and tutorials planned)

**📋 Planned:**
- FastAPI web service wrapper
- Additional CLI commands
- Enhanced testing coverage

**Installation:**
```bash
# Core (ADP only)
pip install axcpy

# With SearchWebAPI support
pip install axcpy[searchwebapi]

# From local build
pip install dist/axcpy-0.1.0-py3-none-any.whl[searchwebapi]
```

**Quick Start:**
```python
# ADP Client
from axcpy.adp import ADPClient, Session
client = ADPClient(base_url="https://server.com")
session = Session(client, "user", "pass")

# SearchWebAPI Client
from axcpy.searchwebapi import SearchWebApiClient
# See examples/searchWebApi_examples.py for full usage
```

## Goals and Objectives

- **Primary**: Provide robust Python client libraries for Axcelerate's REST services (ADP and SearchWebAPI)
- **Automation**: Enable automation of eDiscovery workflows and batch operations
- **Accessibility**: Offer both programmatic API and CLI access to Axcelerate services
- **Type Safety**: Maintain comprehensive type hints and Pydantic models for validation
- **Developer Experience**: Use modern tooling (uv, httpx, typer) for optimal development workflow
- **Extensibility**: Support future extension with FastAPI web service and additional features
- **Documentation**: Comprehensive API documentation and practical examples

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
- **Python**: 3.12+ (primary target, 3.9+ supported)
- **Package Manager**: `uv` (fast Python package and environment manager)
- **HTTP Client**: `httpx` (async support, HTTP/2, connection pooling)
- **CLI Framework**: `typer` (modern, type-based CLI)
- **Code Generation**: Microsoft Kiota (for SearchWebAPI OpenAPI client generation)
- **Serialization**: `pydantic` v2 (data validation and settings management)

### Future Technologies
- **Web Framework**: FastAPI (REST API service)
- **API Documentation**: Swagger/OpenAPI
- **Testing**: pytest, pytest-asyncio

## Project Structure

```
axcpy/
├── README.md                      # Project overview and quick start
├── DESIGN.md                      # This document (architecture and design)
├── LICENSE                        # License information
├── pyproject.toml                 # Project configuration and dependencies
├── main.py                        # Development entry point
│
├── src/
│   └── axcpy/
│       ├── __init__.py           # Package initialization with subpackage exports
│       ├── __version__.py        # Version information
│       │
│       ├── adp/                  # ADP Client Library
│       │   ├── __init__.py       # Exports ADPClient, AsyncADPClient, Session
│       │   ├── api_spec.md       # Complete ADP API specification
│       │   │
│       │   ├── models/           # Pydantic models
│       │   │   ├── __init__.py   # Model exports
│       │   │   ├── base.py       # BaseTaskConfig (shared fields)
│       │   │   ├── request.py    # ADPTaskRequest wrapper
│       │   │   ├── response.py   # Response base classes
│       │   │   ├── task_spec.py  # Task specifications registry
│       │   │   ├── list_entities.py        # List entities config/result
│       │   │   ├── manage_host_roles.py    # Host roles config/result
│       │   │   ├── query_engine.py         # Query engine config/result
│       │   │   ├── read_configuration.py   # Read config config/result
│       │   │   └── taxonomy_statistic.py   # Taxonomy stats config/result
│       │   │
│       │   └── services/         # Client implementations
│       │       ├── __init__.py
│       │       ├── client.py           # ADPClient (sync)
│       │       ├── async_client.py     # AsyncADPClient (async)
│       │       ├── session.py          # Session (sync wrapper)
│       │       └── async_session.py    # AsyncSession (async wrapper)
│       │
│       ├── searchwebapi/         # SearchWebAPI Client (Kiota-generated)
│       │   ├── __init__.py       # Exports SearchWebApiClient
│       │   ├── api_spec.json     # OpenAPI specification
│       │   └── generated/        # Kiota-generated code
│       │       ├── search_web_api_client.py  # Main client class
│       │       ├── login/        # Login endpoint handlers
│       │       ├── logout/       # Logout endpoint handlers
│       │       ├── projects/     # Projects endpoint handlers
│       │       └── models/       # Request/response models
│       │
│       ├── common/               # Shared utilities
│       │   ├── __init__.py
│       │   ├── auth.py           # AuthHandler protocol, APIKeyAuth, OAuth2Auth
│       │   ├── config.py         # AxcelerateConfig (Pydantic settings)
│       │   ├── http.py           # HTTP utilities and helpers
│       │   └── exceptions.py     # Exception hierarchy
│       │
│       ├── cli/                  # Command-line interface
│       │   ├── __init__.py
│       │   ├── main.py           # CLI entry point (Typer app)
│       │   ├── adp_commands.py   # ADP CLI commands (in development)
│       │   └── search_commands.py # SearchWebAPI CLI commands (planned)
│       │
│       └── api/                  # FastAPI service (Future)
│           ├── __init__.py
│           ├── main.py           # FastAPI app
│           ├── routes/           # API routes
│           │   └── ...
│           └── middleware/       # Custom middleware
│               └── ...
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration and fixtures
│   ├── test_adp/                # ADP client tests
│   │   ├── __init__.py
│   │   ├── test_client.py       # ADPClient tests
│   │   └── test_async_client.py # AsyncADPClient tests
│   ├── test_searchwebapi/       # SearchWebAPI tests
│   │   └── __init__.py
│   └── test_cli/                # CLI tests
│       ├── __init__.py
│       └── test_main.py         # CLI command tests
│
├── docs/                         # Documentation
│   ├── index.md
│   ├── getting-started.md
│   ├── api-reference/
│   │   └── ...
│   └── examples/
│       └── ...
│
├── examples/                     # Usage examples
│   ├── adp_examples.py          # ADP client examples
│   ├── adp_async_examples.py    # Async ADP client examples
│   └── searchWebApi_examples.py # SearchWebAPI client examples
│
└── scripts/                      # Build and utility scripts
    ├── generate_searchwebapi.sh  # Kiota generation script (Bash)
    ├── generate_searchwebapi.ps1 # Kiota generation script (PowerShell)
    └── setup_dev.sh              # Development environment setup
```

**Key Directories**:

- **`src/axcpy/adp/models/`**: All Pydantic models for ADP tasks, organized by task type
- **`src/axcpy/adp/services/`**: HTTP client and session implementations (sync and async)
- **`src/axcpy/common/`**: Reusable utilities shared across all modules
- **`tests/`**: Comprehensive test suite with pytest
- **`examples/`**: Practical usage examples for developers
- **`docs/`**: User and API documentation

## Component Design

### 1. ADP Client Library

**Purpose**: Manually crafted REST client for ADP service using PUT-only semantics

The ADP service uses a unique task-based API where all operations are submitted via PUT requests to specific endpoints. Each task has a type and configuration, sent as JSON payloads.

#### Architecture Layers

**1.1 HTTP Client Layer** (`ADPClient` and `AsyncADPClient`)
- Low-level HTTP client built on `httpx`
- Handles PUT requests to ADP endpoints
- Manages TLS verification, timeouts, and headers
- Provides debug logging capabilities
- Implements context manager protocol for resource cleanup

**Key Features**:
- Synchronous and async variants for flexibility
- Built-in request/response logging when debug mode enabled
- Configurable timeouts and headers per request
- Connection pooling via httpx client
- Support for self-signed certificates (testing)

**Example**:
```python
from axcpy.adp import ADPClient, AsyncADPClient

# Synchronous client
client = ADPClient(
    base_url="https://axcelerate.example.com",
    ignore_tls=False,
    timeout=30.0,
    debug=True
)

# Async client
async_client = AsyncADPClient(
    base_url="https://axcelerate.example.com",
    timeout=60.0
)

# Context manager support
with ADPClient(base_url=url) as client:
    response = client.run(task)
```

**1.2 Session Layer** (`Session` and `AsyncSession`)
- High-level abstraction over ADPClient
- Manages authentication headers (Auth-Username, Auth-Password)
- Provides type-safe methods for each task type
- Automatically constructs ADPTaskRequest objects
- Parses responses into strongly-typed result models

**Key Features**:
- Header-based authentication management
- Type-safe task execution methods
- Automatic response parsing to Pydantic models
- Shared client instance across sessions (efficient resource usage)
- Task-specific convenience methods (e.g., `list_entities()`, `query_engine()`)

**Example**:
```python
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

# Create shared client
client = ADPClient(base_url="https://axcelerate.example.com/adp")

# Create session with authentication
session = Session(
    client=client,
    auth_username="adpuser",
    auth_password="password"
)

# Use type-safe task methods
config = ListEntitiesTaskConfig(adp_listEntities_type="singleMindServer")
result = session.list_entities(config)  # Returns ListEntitiesResult

# Access typed results
for entity in result.adp_entities_json_output:
    print(f"ID: {entity.get('id')}, Name: {entity.get('displayName')}")
```

**1.3 Model Layer** (Pydantic Models)
- **Base Models**: `BaseTaskConfig` - shared configuration fields across all tasks
- **Task Configs**: Type-safe configuration for each ADP task type
  - `ListEntitiesTaskConfig`
  - `ManageHostRolesTaskConfig`
  - `QueryEngineTaskConfig`
  - `ReadConfigurationTaskConfig`
  - `TaxonomyStatisticTaskConfig`
- **Request Models**: `ADPTaskRequest` - wraps task type and configuration
- **Response Models**: Strongly-typed result objects for each task type
  - `ListEntitiesResult`
  - `ManageHostRolesResult`
  - `QueryEngineResult`
  - etc.

**Model Structure**:
```python
# Base configuration (shared fields)
class BaseTaskConfig(BaseModel):
    adp_loggingEnabled: bool = True
    adp_executionPersistent: bool = True
    adp_progressTaskTimeout: int = 0
    adp_taskActive: bool = True
    adp_taskTimeout: int = 0
    adp_cleanUpHistory: bool = False

# Task-specific configuration
class ListEntitiesTaskConfig(BaseTaskConfig):
    adp_listEntities_type: str
    adp_listEntities_whiteList: str = ""
    # ... other fields

# Request wrapper
class ADPTaskRequest(BaseModel):
    taskType: str
    taskConfiguration: TaskConfigurationType
    taskDescription: str = ""
    taskDisplayName: str = ""
    
    def as_payload(self) -> dict[str, object]:
        # Serializes to wire format
```

#### API Endpoints

The ADP service exposes two main endpoints:
- `/adp/rest/api/task/executeAdpTask` - Synchronous task execution
- `/adp/rest/api/task/executeAdpTaskAsync` - Asynchronous task execution (returns task ID for polling)

#### Task Types

Currently implemented task types:
1. **List Entities**: Query SingleMind servers and other entity types
2. **Manage Host Roles**: Get host role configurations
3. **Query Engine**: Execute search queries against data engines
4. **Read Configuration**: Retrieve configuration data
5. **Taxonomy Statistic**: Get taxonomy statistics and metadata

See [api_spec.md](src/axcpy/adp/api_spec.md) for comprehensive task type documentation.

### 2. SearchWebAPI Client Library

**Purpose**: OpenAPI 3.x based client generated with Microsoft Kiota

The SearchWebAPI client provides access to Axcelerate's search capabilities through a fully-typed, auto-generated Python client.

**Current Status**: ✅ Implemented and tested

**Key Features**:
- Auto-generated from OpenAPI specification using Microsoft Kiota
- Strongly-typed request/response models
- Built-in serialization/deserialization (JSON and Text)
- Fluent API design with method chaining
- Session-based authentication support
- Support for multiple authentication methods

**Architecture**:
```
SearchWebApiClient (generated/search_web_api_client.py)
├── login/          # Login endpoints
├── logout/         # Logout endpoints
├── projects/       # Project management
│   ├── collections/    # Collection operations
│   │   ├── fields/     # Field definitions
│   │   └── search/     # Search operations
│   └── ...
└── models/         # Request/response models
```

**Generation Process**:
```powershell
# Generate client from OpenAPI spec using PowerShell script
.\scripts\generate_searchwebapi.ps1

# Or manually with Kiota CLI
kiota generate `
  --language python `
  --openapi api_spec.json `
  --output src/axcpy/searchwebapi/generated `
  --class-name SearchWebApiClient `
  --namespace-name axcpy.searchwebapi.generated `
  --clear-output
```

**Dependencies** (automatically managed):
- `microsoft-kiota-abstractions` - Core abstractions
- `microsoft-kiota-http` - HTTP transport (httpx-based)
- `microsoft-kiota-serialization-json` - JSON serialization
- `microsoft-kiota-serialization-text` - Text serialization

**Usage Example**:
```python
import asyncio
import httpx
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from axcpy.searchwebapi import SearchWebApiClient

class BasicAuthProvider:
    """Basic authentication with session management"""
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session_id = None
    
    async def authenticate_request(self, request, additional_authentication_context=None):
        import base64
        if hasattr(request, "headers"):
            if self.session_id:
                # Use session if available
                request.headers.try_add("SWA-SESSION", self.session_id)
            else:
                # Send Basic Auth credentials
                credentials = f"{self.username}:{self.password}"
                encoded = base64.b64encode(credentials.encode()).decode()
                request.headers.try_add("Authorization", f"Basic {encoded}")
        return request

async def main():
    # Setup authentication
    auth_provider = BasicAuthProvider("admin", "password")
    
    # Create HTTP client and request adapter
    http_client = httpx.AsyncClient(verify=False, timeout=30.0)
    request_adapter = HttpxRequestAdapter(auth_provider, http_client=http_client)
    request_adapter.base_url = "https://server:8443/searchWebApi"
    
    # Create SearchWebAPI client
    client = SearchWebApiClient(request_adapter)
    
    # Login and capture session
    await client.login.post()
    
    # Get projects (using session)
    projects = await client.projects.get()
    print(f"Found {len(projects)} projects")
    
    # Get fields for a specific collection
    fields = await (client.projects
        .by_project_id("singleMindServer.demo00001")
        .collections.by_collection_id("default")
        .fields.get())
    
    # Logout
    await client.logout.delete()
    await http_client.aclose()

asyncio.run(main())
```

**Session Management**:
The SearchWebAPI uses session-based authentication:
1. Initial request sends Basic Auth credentials
2. Server returns `SWA-SESSION` header
3. Subsequent requests use session header (no credentials)
4. Logout clears the session

See [searchWebApi_examples.py](../examples/searchWebApi_examples.py) for complete working example.

### 3. Common Utilities

#### 3.1 Authentication (`common/auth.py`)

The authentication module provides a protocol-based design supporting multiple auth methods:

**Authentication Protocol**:
```python
class AuthHandler(Protocol):
    """Protocol for authentication handlers"""
    def get_headers(self) -> dict[str, str]: ...
```

**Implementations**:
- `APIKeyAuth`: Bearer token authentication
- `OAuth2Auth`: OAuth 2.0 token-based authentication

**Usage**:
```python
from axcpy.common.auth import APIKeyAuth, OAuth2Auth

# API Key auth
auth = APIKeyAuth(api_key="your-api-key")
headers = auth.get_headers()  # {"Authorization": "Bearer your-api-key"}

# OAuth2 auth
oauth = OAuth2Auth(token="oauth-token")
headers = oauth.get_headers()  # {"Authorization": "Bearer oauth-token"}
```

**Note**: The ADP service currently uses custom header-based authentication (`Auth-Username`/`Auth-Password`) managed by the Session layer. The common auth module provides extensibility for other services like SearchWebAPI.

#### 3.2 Configuration Management (`common/config.py`)

Configuration uses Pydantic Settings for environment variable and .env file support:

```python
class AxcelerateConfig(BaseSettings):
    """Application configuration using Pydantic settings"""
    model_config = SettingsConfigDict(
        env_prefix="AXCELERATE_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    
    adp_base_url: Optional[str] = None
    search_base_url: Optional[str] = None
    api_key: Optional[str] = None
    timeout: int = 30
    max_retries: int = 3
    verify_ssl: bool = True
```

**Configuration Sources** (priority order):
1. Direct programmatic configuration via `configure()`
2. Environment variables with `AXCELERATE_` prefix
3. `.env` file in working directory
4. Default values

**Usage**:
```python
from axcpy.common.config import get_config, configure

# Get global config (auto-loads from env)
config = get_config()
print(config.adp_base_url)

# Programmatic configuration
configure(
    adp_base_url="https://axcelerate.example.com/adp",
    api_key="your-key",
    timeout=60
)
```

#### 3.3 HTTP Utilities (`common/http.py`)

Common HTTP utilities, middleware, and helpers:
- Custom exception handling
- Request/response interceptors
- Retry logic with exponential backoff
- Rate limiting utilities
- Response parsing helpers

#### 3.4 Exception Hierarchy (`common/exceptions.py`)

Structured exception hierarchy for clear error handling:

```python
AxcelerateException
├── ADPException
│   ├── ADPAuthenticationError
│   ├── ADPNotFoundError
│   ├── ADPValidationError
│   └── ADPTimeoutError
├── SearchWebAPIException
│   ├── SearchAuthenticationError
│   └── SearchQueryError
└── ConfigurationError
    ├── MissingConfigurationError
    └── InvalidConfigurationError
```

### 4. CLI Interface

**Purpose**: Command-line interface for interacting with Axcelerate services

**Framework**: Typer (modern, type-based CLI framework) + Rich (terminal formatting)

**Current Implementation Status**:
- ✅ CLI framework structure (`cli/main.py`)
- ✅ Version command
- 🚧 Configuration management (placeholder)
- 🚧 ADP commands (`cli/adp_commands.py`) - in development
- 🚧 SearchWebAPI commands (`cli/search_commands.py`) - planned

**CLI Structure**:
```python
# Main app entry point
app = typer.Typer(
    name="axcpy",
    help="Axcelerate Python Client - CLI for OpenText Axcelerate eDiscovery service",
    no_args_is_help=True,
)

@app.command()
def version() -> None:
    """Show version information."""
    
@app.command()
def config() -> None:
    """Manage configuration."""
    
# Subcommands (to be added)
# app.add_typer(adp_app, name="adp")
# app.add_typer(search_app, name="search")
```

**Planned Command Structure**:
```
axcpy [OPTIONS] COMMAND [ARGS]

Commands:
  version              Show version information
  config               Manage configuration (set/get/list)
  adp                  ADP service commands
  search               SearchWebAPI commands

axcpy config [COMMAND]
  set [KEY] [VALUE]    Set configuration value
  get [KEY]            Get configuration value
  list                 List all configuration
  init                 Initialize configuration interactively

axcpy adp [COMMAND]
  list-entities        List entities (SingleMind servers, etc.)
  query-engine         Execute query engine search
  read-config          Read configuration data
  manage-roles         Manage host roles
  taxonomy-stats       Get taxonomy statistics
  
axcpy search [COMMAND]
  query [QUERY]        Execute search query
  export [OPTIONS]     Export search results
```

**Example Usage** (planned):
```bash
# Show version
axcpy version

# Configure credentials
axcpy config set adp_base_url https://axcelerate.example.com/adp
axcpy config set auth_username adpuser
axcpy config set auth_password password

# List SingleMind servers
axcpy adp list-entities --type singleMindServer

# Query engine
axcpy adp query-engine --engine myengine --query "document search"

# Read configuration
axcpy adp read-config --config-id "dataSource.file_demo_01"
```

**Rich Console Integration**:
Uses Rich library for:
- Colored output and syntax highlighting
- Progress bars for long operations
- Formatted tables for results
- Error messages with context

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

## Implementation Patterns and Principles

### Design Patterns

**1. Builder Pattern** (Task Configuration)
- Pydantic models act as builders for task configurations
- Fluent API through model instantiation with named parameters
- Validation happens at construction time

**2. Strategy Pattern** (Authentication)
- `AuthHandler` protocol defines authentication interface
- Multiple implementations (`APIKeyAuth`, `OAuth2Auth`)
- Easily extensible for new auth methods

**3. Adapter Pattern** (Client/Session Layers)
- `Session` adapts low-level `ADPClient` to high-level task API
- Converts between generic HTTP responses and typed models
- Shields users from HTTP details

**4. Factory Pattern** (Task Creation)
- Task specifications registry (`TASK_SPECS`) maps task types to configs
- Enables dynamic task creation and validation

**5. Context Manager Pattern**
- Both sync and async clients implement context managers
- Ensures proper resource cleanup (connection closing)
- Pythonic resource management

### Code Quality Principles

**Type Safety**:
- Comprehensive type hints throughout codebase
- `mypy` strict mode compliance
- Pydantic models for runtime validation

**Separation of Concerns**:
- Clear layering: HTTP client → Session → User code
- Models separated from business logic
- Configuration isolated in common module

**DRY (Don't Repeat Yourself)**:
- `BaseTaskConfig` eliminates field duplication
- Shared utilities in common module
- Reusable patterns in sync/async variants

**Explicit is Better Than Implicit**:
- Field names match wire format exactly (e.g., `adp_listEntities_type`)
- No magic string conversions or hidden transformations
- Debug logging shows actual payloads

**Fail Fast**:
- Pydantic validation at construction
- HTTP errors raised immediately
- Type checking catches errors early

### Testing Strategy

**Unit Tests**:
- Test individual components in isolation
- Mock HTTP responses with `pytest-httpx`
- Validate model serialization/deserialization

**Integration Tests**:
- Test client libraries against mock/test servers
- Verify request/response flow
- Test error handling paths

**CLI Tests**:
- Use Typer's testing utilities
- Test command parsing and execution
- Validate output formatting

**Example Test Structure**:
```python
# tests/test_adp/test_client.py
def test_adp_client_run(httpx_mock):
    """Test synchronous task execution"""
    httpx_mock.add_response(
        method="PUT",
        url="http://example.com/adp/rest/api/task/executeAdpTask",
        json={"status": "success"}
    )
    
    client = ADPClient(base_url="http://example.com")
    task = ADPTaskRequest(
        taskType="List Entities",
        taskConfiguration=ListEntitiesTaskConfig(
            adp_listEntities_type="singleMindServer"
        )
    )
    
    response = client.run(task)
    assert response.status_code == 200
```

## Development Phases and Status

### ✅ Phase 1: Foundation (Complete)
- [x] Project structure setup
- [x] pyproject.toml configuration with uv
- [x] Common utilities (auth, config, HTTP)
- [x] Exception hierarchy
- [x] Development environment setup

### ✅ Phase 2: ADP Client Library Core (Complete)
- [x] Core ADPClient implementation (sync)
- [x] AsyncADPClient implementation
- [x] Pydantic models for ADP tasks
- [x] BaseTaskConfig for shared fields
- [x] ADPTaskRequest wrapper
- [x] Session and AsyncSession wrappers
- [x] Type-safe task methods

### ✅ Phase 3: ADP Models and Task Types (Complete)
- [x] List Entities task (config + result)
- [x] Manage Host Roles task
- [x] Query Engine task
- [x] Read Configuration task
- [x] Taxonomy Statistic task
- [x] Task specifications registry
- [x] Response parsing

### 🚧 Phase 4: CLI Interface (In Progress)
- [x] Typer CLI framework setup
- [x] Version command
- [ ] Configuration management commands
- [ ] ADP task commands
- [ ] Output formatting with Rich
- [ ] CLI testing

### ✅ Phase 5: SearchWebAPI Client (Complete)
- [x] Obtain OpenAPI specification (api_spec.json)
- [x] Generate client with Kiota (SearchWebApiClient)
- [x] Generated client structure (login, logout, projects, collections, fields)
- [x] Authentication providers (Basic Auth with session management)
- [x] Working examples (searchWebApi_examples.py - fully tested)
- [x] PowerShell generation script (generate_searchwebapi.ps1)
- [x] Bash generation script (generate_searchwebapi.sh)
- [x] Package exports via __init__.py
- [x] Kiota dependencies installed and configured
- [x] Session capture and reuse implementation
- [ ] Wrapper/adapter layer (optional - direct usage is clean)
- [ ] Unit tests for SearchWebAPI
- [ ] CLI commands for SearchWebAPI

### 📋 Phase 6: Documentation & Examples (In Progress)
- [x] Basic examples (adp_examples.py, adp_async_examples.py, searchWebApi_examples.py)
- [x] Comprehensive DESIGN.md documentation
- [x] Package building and distribution guide
- [x] Installation strategies documentation
- [x] Multi-client usage examples
- [ ] API reference documentation (auto-generated)
- [ ] User guide and tutorials
- [ ] Enhanced README with quick start
- [ ] Contribution guidelines

### 🔮 Phase 7: FastAPI Service (Future)
- [ ] FastAPI application setup
- [ ] REST endpoints wrapping client libraries
- [ ] Authentication/authorization
- [ ] OpenAPI documentation
- [ ] Rate limiting
- [ ] Deployment configuration

## Dependencies

### Core Dependencies

Current dependencies as defined in `pyproject.toml`:

```toml
[project]
name = "axcpy"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "httpx>=0.26.0",              # Modern async HTTP client with HTTP/2 support
    "pydantic>=2.5.0",            # Data validation and settings management
    "pydantic-settings>=2.0.0",   # Settings management with env support
    "typer>=0.9.0",               # CLI framework with type hints
    "rich>=13.7.0",               # Terminal formatting and styling
    "python-dotenv>=1.0.0",       # .env file support
]
```

**Rationale for Core Dependencies**:
- **httpx**: Superior to requests - async support, HTTP/2, modern API, connection pooling
- **pydantic v2**: Runtime validation, serialization, settings management with excellent performance
- **typer**: Type-based CLI framework with great developer experience
- **rich**: Beautiful terminal output with progress bars, tables, syntax highlighting
- **python-dotenv**: Simple .env file support for local development

**Rationale for SearchWebAPI Dependencies**:
- **microsoft-kiota-abstractions**: Core abstractions for Kiota-generated clients (request adapters, authentication, serialization)
- **microsoft-kiota-http**: HTTP transport implementation using httpx for async support
- **microsoft-kiota-serialization-json**: JSON content type support for API requests/responses
- **microsoft-kiota-serialization-text**: Plain text content type support
- These are optional dependencies - only install if using SearchWebAPI client

### Development Dependencies

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",              # Testing framework
    "pytest-asyncio>=0.21.0",     # Async test support
    "pytest-httpx>=0.30.0",       # httpx mocking
    "ruff>=0.1.0",                # Fast linting and formatting
    "mypy>=1.7.0",                # Static type checking
    "types-requests",             # Type stubs
]
```

### Optional Feature Dependencies

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-httpx>=0.30.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
    "types-requests",
]
api = [
    "fastapi>=0.108.0",           # Web framework (future)
    "uvicorn>=0.25.0",            # ASGI server (future)
]
searchwebapi = [
    "microsoft-kiota-abstractions>=1.3.0",      # Kiota core abstractions
    "microsoft-kiota-http>=1.3.0",              # HTTP transport for Kiota
    "microsoft-kiota-serialization-json>=1.0.0", # JSON serialization
    "microsoft-kiota-serialization-text>=1.0.0", # Text serialization
]
```

### Tool Dependencies

External tools not managed by pip:
- **Microsoft Kiota**: OpenAPI client generation (npm/dotnet tool)
  ```bash
  # Install via npm
  npm install -g @microsoft/kiota
  
  # Or via .NET tool
  dotnet tool install -g Microsoft.OpenApi.Kiota
  ```
- **uv**: Package and environment manager (installed separately)
  ```bash
  # Install on Windows (PowerShell)
  irm https://astral.sh/uv/install.ps1 | iex
  ```

### Dependency Philosophy

**Minimal Core**: Keep core dependencies minimal and well-maintained
**Optional Features**: Use optional dependency groups for non-essential features
**Version Pinning**: Use lower bounds (`>=`) for flexibility, rely on lockfile for reproducibility
**Quality over Quantity**: Prefer well-maintained, popular libraries with good documentation

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

### Configuration Sources

The library uses a layered configuration approach with Pydantic Settings:

1. **Environment Variables** (highest priority)
2. **.env File** (local development)
3. **Programmatic Configuration** (code-based)
4. **Default Values** (lowest priority)

### Environment Variables

All configuration can be set via environment variables with `AXCELERATE_` prefix:

```bash
# .env file or system environment
AXCELERATE_ADP_BASE_URL=https://axcelerate.example.com/adp
AXCELERATE_SEARCH_BASE_URL=https://axcelerate.example.com/search
AXCELERATE_API_KEY=your-api-key-here
AXCELERATE_TIMEOUT=30
AXCELERATE_MAX_RETRIES=3
AXCELERATE_VERIFY_SSL=true
```

### Programmatic Configuration

```python
from axcpy.common.config import configure, get_config

# Set configuration programmatically
configure(
    adp_base_url="https://axcelerate.example.com/adp",
    search_base_url="https://axcelerate.example.com/search",
    api_key="your-api-key",
    timeout=60,
    verify_ssl=True
)

# Access configuration
config = get_config()
print(config.adp_base_url)
print(config.timeout)
```

### Configuration in Application Code

Configuration is typically used at client initialization:

```python
from axcpy.common.config import get_config
from axcpy.adp import ADPClient, Session

# Load config from environment
config = get_config()

# Use config values
client = ADPClient(
    base_url=config.adp_base_url,
    timeout=config.timeout,
    ignore_tls=not config.verify_ssl
)

session = Session(
    client=client,
    auth_username="user",
    auth_password="pass"
)
```

### Best Practices

1. **Development**: Use `.env` file (not committed to git)
2. **Production**: Use environment variables or secrets management
3. **Testing**: Use programmatic configuration with test values
4. **CI/CD**: Use environment variables in pipelines

## Detailed API Usage Examples

### Synchronous Client Usage

```python
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import (
    ListEntitiesTaskConfig,
    QueryEngineTaskConfig,
    ReadConfigurationTaskConfig
)

# Create shared client
client = ADPClient(
    base_url="https://axcelerate.example.com",
    timeout=30.0,
    debug=True  # Enable request/response logging
)

# Create authenticated session
session = Session(
    client=client,
    auth_username="adpuser",
    auth_password="password"
)

# List SingleMind servers
config = ListEntitiesTaskConfig(
    adp_listEntities_type="singleMindServer"
)
result = session.list_entities(config)

for entity in result.adp_entities_json_output:
    print(f"Server: {entity.get('displayName')} (ID: {entity.get('id')})")

# Execute query engine search
query_config = QueryEngineTaskConfig(
    adp_queryEngine_identifier="my_engine",
    adp_queryEngine_query="document AND type:email",
    adp_queryEngine_maxHits=100
)
query_result = session.query_engine(query_config)
print(f"Found {query_result.hit_count} documents")

# Clean up
client.close()
```

### Asynchronous Client Usage

```python
import asyncio
from axcpy.adp import AsyncADPClient, AsyncSession
from axcpy.adp.models import ListEntitiesTaskConfig, ManageHostRolesTaskConfig

async def main():
    # Create async client
    async with AsyncADPClient(
        base_url="https://axcelerate.example.com",
        timeout=60.0
    ) as client:
        # Create async session
        session = AsyncSession(
            client=client,
            auth_username="adpuser",
            auth_password="password"
        )
        
        # Execute multiple tasks concurrently
        entities_config = ListEntitiesTaskConfig(
            adp_listEntities_type="singleMindServer"
        )
        roles_config = ManageHostRolesTaskConfig()
        
        # Run tasks in parallel
        entities_result, roles_result = await asyncio.gather(
            session.list_entities(entities_config),
            session.manage_host_roles(roles_config)
        )
        
        print(f"Found {len(entities_result.adp_entities_json_output)} entities")
        print(f"Host roles: {roles_result.adp_manageHostRoles_json_output}")

asyncio.run(main())
```

### Context Manager Usage

```python
# Automatic resource cleanup with context managers
with ADPClient(base_url=url) as client:
    session = Session(client, username, password)
    result = session.list_entities(config)
    # Client automatically closed when exiting context

# Async context manager
async with AsyncADPClient(base_url=url) as client:
    session = AsyncSession(client, username, password)
    result = await session.list_entities(config)
    # Client automatically closed when exiting context
```

### Error Handling

```python
from axcpy.adp import ADPClient, Session
from axcpy.common.exceptions import ADPException, ADPAuthenticationError
import httpx

client = ADPClient(base_url="https://axcelerate.example.com")
session = Session(client, "user", "pass")

try:
    result = session.list_entities(config)
except httpx.HTTPStatusError as e:
    print(f"HTTP error: {e.response.status_code} - {e.response.text}")
except httpx.TimeoutException:
    print("Request timed out")
except ADPAuthenticationError:
    print("Authentication failed")
except ADPException as e:
    print(f"ADP error: {e}")
finally:
    client.close()
```

## Testing Strategy

**Testing Framework**: pytest + pytest-asyncio + pytest-httpx

**Test Categories**:

1. **Unit Tests**: Test individual components in isolation
   - Model validation and serialization
   - Configuration management
   - Authentication handlers
   - Utility functions

2. **Integration Tests**: Test client libraries against mocked servers
   - HTTP request/response flow
   - Task execution (sync and async)
   - Error handling paths
   - Authentication integration

3. **CLI Tests**: Test CLI commands with Typer test client
   - Command parsing and validation
   - Output formatting
   - Configuration management
   - Error messages

4. **End-to-End Tests**: Test complete workflows (optional)
   - Multi-step task sequences
   - Real API interactions (with test environment)

**Mock Strategy**:
- Use `pytest-httpx` for mocking HTTP requests
- Create fixtures for common test data
- Separate fixtures for successful and error responses

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

## Technical Deep Dive

### ADP API Protocol

The Axcelerate ADP service uses a unique PUT-only REST API design:

**Endpoints**:
- `PUT /adp/rest/api/task/executeAdpTask` - Synchronous execution
- `PUT /adp/rest/api/task/executeAdpTaskAsync` - Asynchronous execution (returns task ID)

**Request Format**:
```json
{
  "taskType": "List Entities",
  "taskConfiguration": {
    "adp_loggingEnabled": true,
    "adp_executionPersistent": true,
    "adp_progressTaskTimeout": 0,
    "adp_taskActive": true,
    "adp_taskTimeout": 0,
    "adp_cleanUpHistory": false,
    "adp_listEntities_type": "singleMindServer",
    "adp_listEntities_whiteList": ""
  },
  "taskDescription": "Optional description",
  "taskDisplayName": "Optional display name"
}
```

**Response Format**:
```json
{
  "status": "success",
  "adp_entities_json_output": [
    {
      "id": "server1",
      "displayName": "Server 1",
      "hostName": "server1.example.com"
    }
  ]
}
```

**Authentication**:
- Custom header-based: `Auth-Username` and `Auth-Password`
- Headers passed with every request
- No session management or tokens

### Type System Architecture

**Pydantic Model Hierarchy**:

```
BaseModel (Pydantic)
├── BaseTaskConfig
│   ├── ListEntitiesTaskConfig
│   ├── ManageHostRolesTaskConfig
│   ├── QueryEngineTaskConfig
│   ├── ReadConfigurationTaskConfig
│   └── TaxonomyStatisticTaskConfig
├── ADPTaskRequest
└── Result Models
    ├── ListEntitiesResult
    ├── ManageHostRolesResult
    ├── QueryEngineResult
    ├── ReadConfigurationResult
    └── TaxonomyStatisticResult
```

**Type Safety Benefits**:
- Compile-time type checking with mypy
- Runtime validation with Pydantic
- IDE autocomplete and inline documentation
- Self-documenting code
- Reduced bugs from typos or incorrect types

### Async/Sync Duality

The library provides both sync and async variants:

**Synchronous**:
- `ADPClient` - Basic HTTP operations
- `Session` - High-level task API
- Uses `httpx.Client`
- Blocks on I/O

**Asynchronous**:
- `AsyncADPClient` - Async HTTP operations
- `AsyncSession` - Async task API
- Uses `httpx.AsyncClient`
- Non-blocking, enables concurrency

**Code Sharing**:
- Models are shared between sync/async
- Similar API surface for consistency
- Parallel implementation for clarity

**When to Use Each**:
- **Sync**: Scripts, simple automations, interactive use
- **Async**: High-performance applications, concurrent operations, web services

### Performance Considerations

**Connection Pooling**:
- httpx automatically pools connections
- Reuse client instances across requests
- Close clients when done to free resources

**Concurrent Requests**:
```python
# Async allows concurrent execution
async with AsyncADPClient(base_url) as client:
    session = AsyncSession(client, user, pass)
    
    # Run multiple tasks concurrently
    results = await asyncio.gather(
        session.list_entities(config1),
        session.query_engine(config2),
        session.read_configuration(config3)
    )
```

**Memory Management**:
- Streaming responses for large payloads (future)
- Pagination for list operations (future)
- Connection limits to prevent resource exhaustion

**Timeouts**:
- Global default timeout at client level
- Per-request timeout override
- Prevents hung requests

### Security Best Practices

**Credential Management**:
```python
# ❌ BAD - hardcoded credentials
client = ADPClient(base_url="https://example.com")
session = Session(client, "user", "password123")

# ✅ GOOD - environment variables
import os
username = os.environ["ADP_USERNAME"]
password = os.environ["ADP_PASSWORD"]
session = Session(client, username, password)

# ✅ BEST - configuration management
from axcpy.common.config import get_config
config = get_config()
# Credentials from secure environment
```

**TLS/SSL**:
- Always use HTTPS in production
- `ignore_tls=True` only for development/testing
- Verify certificates in production

**Logging**:
- Debug mode logs request/response payloads
- Never log credentials
- Sanitize sensitive data in logs

**Input Validation**:
- Pydantic validates all inputs
- Prevents injection attacks
- Type coercion with validation

### Extensibility Points

**Adding New Task Types**:

1. Create Pydantic models in `adp/models/`:
```python
# my_task.py
from .base import BaseTaskConfig

class MyTaskConfig(BaseTaskConfig):
    adp_myTask_parameter: str
    
class MyTaskResult(BaseModel):
    adp_myTask_output: list[dict]
```

2. Update `TaskConfigurationType` union in `request.py`

3. Add method to `Session`:
```python
def my_task(self, config: MyTaskConfig) -> MyTaskResult:
    task = ADPTaskRequest(
        taskType="My Task",
        taskConfiguration=config
    )
    response_data = self.run(task)
    return MyTaskResult.model_validate(response_data)
```

**Adding Authentication Methods**:

Create new auth handler in `common/auth.py`:
```python
class CustomAuth:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self) -> dict[str, str]:
        return {"X-Custom-Auth": self.token}
```

**Custom HTTP Middleware**:

Extend httpx transport for custom behavior:
```python
import httpx

class LoggingTransport(httpx.HTTPTransport):
    def handle_request(self, request):
        logger.info(f"Request: {request.method} {request.url}")
        return super().handle_request(request)

client = ADPClient(base_url=url)
client._client._transport = LoggingTransport()
```

## Building and Using the Package

### Package Architecture Decision

There are two approaches to packaging:

**Current Approach: Unified Package** (✅ Implemented)
- Single package: `axcpy`
- Contains both `adp` and `searchwebapi` as subpackages
- Install: `pip install axcpy[searchwebapi]`
- Import: `from axcpy.adp import ...` or `from axcpy import adp`

**Alternative: Separate Packages** (Optional, not implemented)
- Multiple packages: `axcpy-adp`, `axcpy-searchwebapi`
- Each installable independently
- Install: `pip install axcpy-adp` or `pip install axcpy-searchwebapi`
- Import: `from adp import ...` or `import adp`

The unified package approach is recommended because:
- ✅ Single installation and versioning
- ✅ Shared dependencies and utilities
- ✅ Easier maintenance
- ✅ Optional dependencies avoid installing unused code
- ✅ Both modules can work together seamlessly

### Building the Package

The axcpy package can be built and distributed for use in external projects:

**Build Process**:
```powershell
# Navigate to project root
cd C:\Users\pyan\github\axcpy

# Build the package (creates wheel and source distribution)
uv build

# Output will be in dist/
# - axcpy-0.1.0-py3-none-any.whl (wheel distribution)
# - axcpy-0.1.0.tar.gz (source distribution)
```

### Installation Strategies

#### Strategy 1: Install from Local Build (Development/Testing)

```powershell
# Install the built wheel directly
pip install dist/axcpy-0.1.0-py3-none-any.whl

# Or install with SearchWebAPI dependencies
pip install "dist/axcpy-0.1.0-py3-none-any.whl[searchwebapi]"

# Or install all optional dependencies
pip install "dist/axcpy-0.1.0-py3-none-any.whl[searchwebapi,api,dev]"
```

#### Strategy 2: Install from Local Directory (Editable Mode)

```powershell
# Install in editable mode (changes reflect immediately)
pip install -e .

# With SearchWebAPI dependencies
pip install -e ".[searchwebapi]"

# With all dependencies
pip install -e ".[searchwebapi,api,dev]"
```

#### Strategy 3: Install from Git Repository

```bash
# Direct from GitHub (main branch)
pip install git+https://github.com/xifanyan/axcpy.git

# From specific branch
pip install git+https://github.com/xifanyan/axcpy.git@feature-branch

# With SearchWebAPI dependencies
pip install "git+https://github.com/xifanyan/axcpy.git#egg=axcpy[searchwebapi]"
```

#### Strategy 4: PyPI Release (Future)

```bash
# Once published to PyPI
pip install axcpy

# With optional dependencies
pip install axcpy[searchwebapi]
```

### Using Both ADP and SearchWebAPI in External Projects

Once installed, you can use both clients in your external Python projects.

#### Import Styles

The package supports multiple import styles for convenience:

```python
# Style 1: Direct subpackage import (explicit)
from axcpy.adp import ADPClient, Session
from axcpy.searchwebapi import SearchWebApiClient

# Style 2: Via parent package (convenient)
import axcpy
client = axcpy.adp.ADPClient(base_url="...")
search_client = axcpy.searchwebapi.SearchWebApiClient(adapter)

# Style 3: Import subpackage as module
from axcpy import adp, searchwebapi
client = adp.ADPClient(base_url="...")
search_client = searchwebapi.SearchWebApiClient(adapter)
```

#### Example 1: Using ADP Client Only

```python
# external_project/my_script.py
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

# No additional dependencies needed (already in core)
client = ADPClient(base_url="https://axcelerate.example.com")
session = Session(client, "username", "password")

config = ListEntitiesTaskConfig(adp_listEntities_type="singleMindServer")
result = session.list_entities(config)
print(f"Found {len(result.adp_entities_json_output)} entities")
```

#### Example 2: Using SearchWebAPI Client Only

```python
# external_project/search_script.py
# Requires: pip install axcpy[searchwebapi]

import asyncio
import httpx
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from axcpy.searchwebapi import SearchWebApiClient

class BasicAuthProvider:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session_id = None
    
    async def authenticate_request(self, request, additional_authentication_context=None):
        import base64
        if hasattr(request, "headers"):
            if self.session_id:
                request.headers.try_add("SWA-SESSION", self.session_id)
            else:
                credentials = f"{self.username}:{self.password}"
                encoded = base64.b64encode(credentials.encode()).decode()
                request.headers.try_add("Authorization", f"Basic {encoded}")
        return request

async def main():
    auth_provider = BasicAuthProvider("admin", "password")
    http_client = httpx.AsyncClient(verify=False, timeout=30.0)
    request_adapter = HttpxRequestAdapter(auth_provider, http_client=http_client)
    request_adapter.base_url = "https://server:8443/searchWebApi"
    
    client = SearchWebApiClient(request_adapter)
    await client.login.post()
    
    projects = await client.projects.get()
    print(f"Found projects: {projects}")
    
    await client.logout.delete()
    await http_client.aclose()

asyncio.run(main())
```

#### Example 3: Using Both ADP and SearchWebAPI

```python
# external_project/combined_workflow.py
# Requires: pip install axcpy[searchwebapi]

import asyncio
import httpx
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import QueryEngineTaskConfig
from axcpy.searchwebapi import SearchWebApiClient
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

# Your authentication providers
class BasicAuthProvider:
    # ... (as shown above)
    pass

async def main():
    # Setup ADP client
    adp_client = ADPClient(base_url="https://axcelerate.example.com")
    adp_session = Session(adp_client, "adpuser", "adppass")
    
    # Setup SearchWebAPI client
    auth = BasicAuthProvider("admin", "admin")
    http_client = httpx.AsyncClient(verify=False)
    adapter = HttpxRequestAdapter(auth, http_client=http_client)
    adapter.base_url = "https://server:8443/searchWebApi"
    search_client = SearchWebApiClient(adapter)
    
    # Use ADP for data management
    query_config = QueryEngineTaskConfig(
        adp_queryEngine_identifier="engine1",
        adp_queryEngine_query="document search"
    )
    adp_result = adp_session.query_engine(query_config)
    print(f"ADP Results: {adp_result.hit_count} hits")
    
    # Use SearchWebAPI for search operations
    await search_client.login.post()
    projects = await search_client.projects.get()
    print(f"SearchWebAPI Projects: {len(projects.results)} projects")
    
    # Cleanup
    await search_client.logout.delete()
    await http_client.aclose()
    adp_client.close()

asyncio.run(main())
```

### Requirements File for External Projects

Create a `requirements.txt` for your external project:

```text
# requirements.txt for project using ADP only
axcpy

# Or for project using both ADP and SearchWebAPI
axcpy[searchwebapi]

# With specific version
axcpy[searchwebapi]==0.1.0

# From local build
./path/to/axcpy/dist/axcpy-0.1.0-py3-none-any.whl[searchwebapi]
```

### Project Setup for External Projects

```powershell
# Create new project
mkdir my_axcelerate_project
cd my_axcelerate_project

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install axcpy from local build
pip install "C:\Users\pyan\github\axcpy\dist\axcpy-0.1.0-py3-none-any.whl[searchwebapi]"

# Or install from source in editable mode
pip install -e "C:\Users\pyan\github\axcpy[searchwebapi]"

# Create your script
New-Item my_script.py

# Run your script
python my_script.py
```

### Dependency Management

The package has smart dependency management:

**Core Dependencies** (always installed):
- httpx, pydantic, typer, rich, python-dotenv

**Optional Dependencies** (install as needed):
- `searchwebapi`: Kiota client dependencies (only if using SearchWebAPI)
- `api`: FastAPI and uvicorn (only if building API service)
- `dev`: Testing and development tools (only for contributors)

**Minimal Installation**:
```bash
# Only ADP client + core deps (~5MB)
pip install axcpy
```

**Full Installation**:
```bash
# Everything including SearchWebAPI (~15MB)
pip install axcpy[searchwebapi]
```

## Deployment Considerations

### Package Distribution

**PyPI Release**:
```bash
# Build package
uv build

# Check package
twine check dist/*

# Upload to PyPI
twine upload dist/*

# Test installation
pip install axcpy
```

**Installation Methods Summary**:
```bash
# From PyPI (when published)
pip install axcpy[searchwebapi]

# From source repository
pip install git+https://github.com/xifanyan/axcpy.git

# From local build
pip install dist/axcpy-0.1.0-py3-none-any.whl[searchwebapi]

# Development installation (editable)
pip install -e .[searchwebapi]
```

### Docker Deployment (Future)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY src/ ./src/

# Install dependencies
RUN uv sync --no-dev

# Set entry point
ENTRYPOINT ["uv", "run", "axcpy"]
```

### CI/CD Integration

**GitHub Actions Example**:
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install uv
        run: pip install uv
      - name: Install dependencies
        run: uv sync --all-extras
      - name: Run tests
        run: uv run pytest
      - name: Type check
        run: uv run mypy src/
      - name: Lint
        run: uv run ruff check src/
```

## Future Enhancements

### Planned Features

1. **Enhanced Error Handling**
   - Retry logic with exponential backoff
   - Circuit breaker pattern for failed services
   - Detailed error context and recovery suggestions

2. **Batch Operations**
   - Submit multiple tasks in one request
   - Bulk data operations
   - Progress tracking for batch jobs

3. **Response Caching**
   - Cache frequently accessed data
   - TTL-based cache invalidation
   - Configurable cache backends

4. **Streaming Support**
   - Stream large responses
   - Chunked file uploads/downloads
   - Real-time progress updates

5. **Advanced CLI Features**
   - Interactive mode with prompts
   - Output to multiple formats (JSON, CSV, Excel)
   - Shell completion
   - Command aliases

6. **Observability**
   - OpenTelemetry integration
   - Structured logging
   - Metrics and monitoring
   - Distributed tracing

7. **Plugin System**
   - Custom task types via plugins
   - Extension hooks
   - Third-party integrations

8. **GraphQL Support** (if Axcelerate adds it)
   - GraphQL client
   - Query builder
   - Schema introspection

### Research Areas

- **Async Task Polling**: Automated polling for async task completion
- **WebSocket Support**: Real-time updates and notifications
- **Rate Limiting**: Client-side rate limiting for API quotas
- **Request Signing**: Cryptographic request signing for enhanced security
- **Multi-tenancy**: Support for multiple Axcelerate instances

## Contributing Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use `ruff` for linting and formatting
- Maximum line length: 100 characters
- Use type hints for all functions
- Write docstrings in Google style

### Development Workflow

```bash
# Setup
git clone https://github.com/xifanyan/axcpy.git
cd axcpy
uv sync --all-extras

# Create feature branch
git checkout -b feature/my-feature

# Make changes
# ...

# Run tests
uv run pytest

# Type check
uv run mypy src/

# Lint and format
uv run ruff check src/
uv run ruff format src/

# Commit
git add .
git commit -m "feat: add my feature"

# Push and create PR
git push origin feature/my-feature
```

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples**:
```
feat(adp): add support for export task
fix(cli): handle missing configuration gracefully
docs(readme): update installation instructions
test(session): add tests for async session
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure all tests pass
5. Update documentation
6. Submit pull request with clear description
7. Address review feedback

### Testing Requirements

- Maintain or improve code coverage
- Add unit tests for new functions
- Add integration tests for new features
- Update existing tests as needed
- All tests must pass before merge

## References

### Official Documentation
- [OpenText Axcelerate](https://www.opentext.com/products/axcelerate)
- [Python httpx](https://www.python-httpx.org/)
- [Pydantic V2](https://docs.pydantic.dev/)
- [Typer](https://typer.tiangolo.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/)
- [uv Package Manager](https://github.com/astral-sh/uv)

### Related Projects
- [httpx](https://github.com/encode/httpx) - HTTP client
- [pydantic](https://github.com/pydantic/pydantic) - Data validation
- [typer](https://github.com/tiangolo/typer) - CLI framework
- [rich](https://github.com/Textualize/rich) - Terminal formatting

### Python Standards
- [PEP 8](https://peps.python.org/pep-0008/) - Style Guide
- [PEP 484](https://peps.python.org/pep-0484/) - Type Hints
- [PEP 517](https://peps.python.org/pep-0517/) - Build System
- [PEP 621](https://peps.python.org/pep-0621/) - Project Metadata

---

## Document Information

**Version**: 2.1  
**Last Updated**: December 19, 2025  
**Authors**: Paul Yan, Development Team  
**Status**: Active Development  
**License**: MIT  

**Change Log**:
- v2.1 (2025-12-19): Updated with SearchWebAPI implementation, Kiota generation, package building strategies
- v2.0 (2025-12-17): Comprehensive update reflecting actual implementation
- v1.0 (Initial): Planning phase document

**Maintainers**: 
- Paul Yan (pyan@opentext.com)

**Review Cycle**: Update design document when:
- Major architectural changes occur
- New components are added
- APIs change significantly
- New development phases begin
