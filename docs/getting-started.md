# Getting Started with axcpy

## Installation

### Using pip

```bash
pip install axcpy
```

### Using uv (Recommended for Development)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install axcpy
uv add axcpy
```

## Configuration

### Environment Variables

Create a `.env` file:

```bash
AXCELERATE_ADP_BASE_URL=https://axcelerate.example.com/adp
AXCELERATE_SEARCH_BASE_URL=https://axcelerate.example.com/search
AXCELERATE_API_KEY=your-api-key-here
```

### Programmatic Configuration

```python
from axcpy.common.config import configure

configure(
    adp_base_url="https://axcelerate.example.com/adp",
    api_key="your-api-key"
)
```

## Basic Usage

### ADP Client

```python
import asyncio
from axcpy.adp import ADPClient

async def main():
    async with ADPClient(
        base_url="https://axcelerate.example.com/adp",
        api_key="your-api-key"
    ) as client:
        # List cases
        cases = await client.cases.list()
        
        # Get specific case
        case = await client.cases.get(case_id=123)
        
        # Search documents
        results = await client.search.query("contract")

if __name__ == "__main__":
    asyncio.run(main())
```

### CLI Usage

```bash
# Configure
axcpy config set --adp-url https://axcelerate.example.com/adp
axcpy config set --api-key your-api-key

# Use commands
axcpy adp cases list
axcpy adp search "document query"
```

## Next Steps

- Explore the [API Reference](api-reference/)
- Check out [Examples](examples/)
- Read the [DESIGN.md](../DESIGN.md) for architecture details
