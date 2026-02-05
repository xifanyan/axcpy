# axcpy - Axcelerate Python Client Library

Python client library and CLI for OpenText Axcelerate eDiscovery service.

## Features

- **ADP Client**: Full-featured REST client for Axcelerate ADP service
  - Sync and async support with `ADPClient` and `AsyncADPClient`
  - Session-based task execution with `Session` and `AsyncSession`
  - 10+ task types: List Entities, Manage Host Roles, Query Engine, Read Configuration, Taxonomy Statistics, Create Data Source, Export Documents, Manage Users and Groups, Read Service Alerts, Create OCR Job
  - Type-safe Pydantic models for request and response validation
- **SearchWebAPI Client**: Auto-generated Kiota client from OpenAPI specification
  - Full CRUD operations for collections, projects, fields, searches, and more
  - Session authentication and transaction management
  - Type-safe models for all API operations
- **CLI Interface**: Command-line tool for both services (in development)
- **Type Safe**: Comprehensive type hints throughout
- **Modern Stack**: Built on httpx, Pydantic v2, and Typer

## Installation

```bash
# Core package (ADP client only)
pip install axcpy

# With SearchWebAPI support
pip install axcpy[searchwebapi]

# With API service (future)
pip install axcpy[api]

# For development
pip install axcpy[dev]
```

## Quick Start

### ADP Client (Sync)

```python
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

# Initialize client
client = ADPClient(
    base_url="https://axcelerate.example.com:8443",
    ignore_tls=True,
    timeout=30.0
)

# Create session and execute task
session = Session(
    client=client,
    auth_username="your-username",
    auth_password="your-password"
)

config = ListEntitiesTaskConfig(adp_listEntities_type="singleMindServer")
result = session.list_entities(config)
for entity in result.adp_entities_json_output:
    print(f"Entity: {entity['id']}")
```

### ADP Client (Async)

```python
import asyncio
from axcpy.adp import AsyncADPClient, AsyncSession
from axcpy.adp.models import QueryEngineTaskConfig

async def main():
    # Initialize async client
    client = AsyncADPClient(
        base_url="https://axcelerate.example.com:8443",
        ignore_tls=True
    )
    
    # Create async session and execute task
    session = AsyncSession(
        client=client,
        auth_username="your-username",
        auth_password="your-password"
    )
    
    config = QueryEngineTaskConfig(
        adp_queryEngine_applicationIdentifier="documentHold.demo00001"
    )
    result = await session.query_engine(config)
    print(f"Document count: {result.adp_query_engine_documents_count}")

asyncio.run(main())
```

### SearchWebAPI Client

```python
from axcpy.searchwebapi import SearchWebApiClient

# Initialize client
client = SearchWebApiClient(
    base_url="https://axcelerate.example.com",
    ignore_tls=True
)

# Login and get session
await client.login.post(username="your-username", password="your-password")

# List collections
collections = await client.collections.get()
print(f"Found {len(collections.collections)} collections")

# Don't forget to logout
await client.logout.post()
```

## Examples

Check out the [examples/](examples/) directory for complete working examples:

- [adp_examples.py](examples/adp_examples.py) - Synchronous ADP client usage
- [adp_async_examples.py](examples/adp_async_examples.py) - Asynchronous ADP client usage
- [searchWebApi_examples.py](examples/searchWebApi_examples.py) - SearchWebAPI client usage

## Development

This project uses [uv](https://github.com/astral-sh/uv) for fast dependency management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup development environment
uv sync --all-extras

# Run tests
uv run pytest

# Run specific test file
uv run pytest tests/test_adp/test_client.py

# Run CLI (in development)
uv run axcpy --help

# Run examples
uv run python examples/adp_examples.py
uv run python examples/adp_async_examples.py
```

## Project Structure

```
axcpy/
├── src/axcpy/
│   ├── adp/              # ADP client library
│   │   ├── models/       # Pydantic models for tasks
│   │   └── services/     # Client and session implementations
│   ├── searchwebapi/     # SearchWebAPI client (Kiota-generated)
│   │   └── generated/    # Auto-generated client code
│   ├── cli/              # Command-line interface (in development)
│   └── api/              # FastAPI service (planned)
├── examples/             # Working examples
├── tests/                # Test suite
└── docs/                 # Documentation
```

## OpenCode Integration

This project includes an OpenCode skill for checking AXcelerate entity status! When using OpenCode in this repository, you can ask natural language questions like:

- "What's the status of demo00001?"
- "Show me all SingleMind servers"
- "Is singleMindServer.demo00001 running?"

OpenCode will automatically use the `axcelerate-status` skill to query your AXcelerate environment.

**Quick setup:**
```bash
# Set your credentials via environment variables
export ADP_USERNAME="your_username"
export ADP_PASSWORD="your_password"
export ADP_BASE_URL="https://your-server:8443"

# Start OpenCode and ask about entity status
opencode
```

See the skill documentation for more details on available commands and usage.

## Documentation

- [Documentation](docs/) - Complete documentation including Getting Started guide
- [DESIGN.md](DESIGN.md) - Comprehensive architecture and design documentation
- [examples/](examples/) - Practical usage examples
- API Reference - Coming soon

## Requirements

- Python 3.12+ (recommended) or 3.9+
- Dependencies: httpx, pydantic, typer, rich
- Optional: Microsoft Kiota dependencies for SearchWebAPI

## License

See [LICENSE](LICENSE) for license information.
