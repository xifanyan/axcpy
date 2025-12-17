# axcpy - Axcelerate Python Client Library

Python client library and CLI for OpenText Axcelerate eDiscovery service.

## Features

- **ADP Client**: Full-featured REST client for Axcelerate ADP service
- **SearchWebAPI Client**: Auto-generated client from OpenAPI specification
- **CLI Interface**: Command-line tool for both services
- **Type Safe**: Full type hints and Pydantic models
- **Async Support**: Built on httpx for async operations

## Installation

```bash
pip install axcpy
```

## Quick Start

### Python API

```python
from axcpy.adp import ADPClient

# Initialize client
client = ADPClient(
    base_url="https://axcelerate.example.com/adp",
    api_key="your-api-key"
)

# Get case information
case = await client.cases.get(case_id=123)
```

### CLI

```bash
# Configure
axcpy config set --adp-url https://axcelerate.example.com/adp
axcpy config set --api-key your-api-key

# List cases
axcpy adp cases list

# Search documents
axcpy adp docs search "contract AND parties:acme"
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) for fast dependency management.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup development environment
uv sync --all-extras

# Run tests
uv run pytest

# Run CLI
uv run axcpy --help
```

## Documentation

See [DESIGN.md](DESIGN.md) for architecture and design details.

## License

See [LICENSE](LICENSE) for license information.
