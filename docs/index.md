# Axcelerate Python Client Library Documentation

Welcome to the axcpy documentation!

## Overview

axcpy is a Python client library for OpenText Axcelerate eDiscovery service, providing:

- **ADP Client**: REST client for Axcelerate ADP service
- **SearchWebAPI Client**: OpenAPI-based client for search operations
- **CLI**: Command-line interface for both services
- **Type Safety**: Full type hints and Pydantic models

## Quick Links

- [Getting Started](getting-started.md)
- [API Reference](api-reference/)
- [Examples](examples/)

## Installation

```bash
pip install axcpy
```

## Quick Example

```python
from axcpy.adp import ADPClient

async with ADPClient(base_url="...", api_key="...") as client:
    cases = await client.cases.list()
    print(cases)
```

## Next Steps

- Read the [Getting Started Guide](getting-started.md)
- Browse [Example Code](examples/)
- Check the [API Reference](api-reference/)
