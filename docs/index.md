# Axcelerate Python Client Library Documentation

Welcome to the axcpy documentation!

## Overview

axcpy is a Python client library for OpenText Axcelerate eDiscovery service, providing:

- **ADP Client**: REST client for Axcelerate ADP service with 10+ task types
- **SearchWebAPI Client**: OpenAPI-based client for search operations
- **CLI**: Command-line interface for both services
- **Type Safety**: Full type hints and Pydantic models

## Quick Links

- [Getting Started](getting-started.md)
- [API Reference](api-reference/)
- [Examples](examples/)

## Installation

```bash
# Core package (ADP client only)
pip install axcpy

# With SearchWebAPI support
pip install axcpy[searchwebapi]

# For development
pip install axcpy[dev]
```

## Quick Example

```python
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

# Create client and session
client = ADPClient(
    base_url="https://axcelerate.example.com:8443",
    ignore_tls=True
)
session = Session(
    client=client,
    auth_username="your-username",
    auth_password="your-password"
)

# Execute task
config = ListEntitiesTaskConfig(adp_listEntities_type="singleMindServer")
result = session.list_entities(config)
for entity in result.adp_entities_json_output:
    print(f"Entity: {entity['id']}")
```

## Supported ADP Tasks

axcpy supports the following Axcelerate ADP tasks:

1. **List Entities** - List servers, collections, applications, and other entities
2. **Manage Host Roles** - View and manage host role assignments
3. **Read Configuration** - Read configuration settings for data sources and engines
4. **Query Engine** - Execute queries and retrieve document counts
5. **Taxonomy Statistic** - Get statistics and category counts for taxonomies
6. **Create Data Source** - Create new data sources on engines
7. **Export Documents** - Export documents with field mappings
8. **Manage Users and Groups** - Create and manage users, groups, and application roles
9. **Read Service Alerts** - Retrieve system alerts and warnings
10. **Create OCR Job** - Create OCR processing jobs for documents

All tasks support both synchronous and asynchronous execution.

## Next Steps

- Read the [Getting Started Guide](getting-started.md)
- Browse [Example Code](examples/)
- Check the [API Reference](api-reference/)
