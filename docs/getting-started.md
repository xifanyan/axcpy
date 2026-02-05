# Getting Started with axcpy

## Installation

### Using pip

```bash
# Core package (ADP client only)
pip install axcpy

# With SearchWebAPI support
pip install axcpy[searchwebapi]

# For development
pip install axcpy[dev]
```

### Using uv (Recommended for Development)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repository and setup
git clone https://github.com/xifanyan/axcpy
cd axcpy
uv sync --all-extras
```

## Configuration

### Basic Configuration

The ADP client requires three basic parameters:

- **base_url**: The URL of your Axcelerate ADP service (e.g., `https://axcelerate.example.com:8443`)
- **auth_username**: Your ADP username
- **auth_password**: Your ADP password

### Optional Parameters

- **ignore_tls**: Ignore SSL certificate verification (default: `False`)
- **timeout**: Request timeout in seconds (default: `30.0`)
- **debug**: Enable debug logging (default: `False`)

## Basic Usage

### Synchronous ADP Client

```python
from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

# Initialize client
client = ADPClient(
    base_url="https://axcelerate.example.com:8443",
    ignore_tls=True,
    timeout=30.0
)

# Create session
session = Session(
    client=client,
    auth_username="your-username",
    auth_password="your-password"
)

# Execute task
config = ListEntitiesTaskConfig(adp_listEntities_type="singleMindServer")
result = session.list_entities(config)

for entity in result.adp_entities_json_output:
    print(f"Entity: {entity['id']} - {entity['displayName']}")
```

### Asynchronous ADP Client

```python
import asyncio
from axcpy.adp import AsyncADPClient, AsyncSession
from axcpy.adp.models import QueryEngineTaskConfig

async def main():
    # Initialize async client with context manager
    async with AsyncADPClient(
        base_url="https://axcelerate.example.com:8443",
        ignore_tls=True
    ) as client:
        # Create async session
        session = AsyncSession(
            client=client,
            auth_username="your-username",
            auth_password="your-password"
        )
        
        # Execute task
        config = QueryEngineTaskConfig(
            adp_queryEngine_applicationIdentifier="documentHold.demo00001"
        )
        result = await session.query_engine(config)
        print(f"Document count: {result.adp_query_engine_documents_count}")

asyncio.run(main())
```

## Available ADP Tasks

### 1. List Entities

List servers, collections, applications, and other entities in your Axcelerate environment.

```python
from axcpy.adp.models import ListEntitiesTaskConfig

config = ListEntitiesTaskConfig(
    adp_listEntities_type="singleMindServer",  # Options: singleMindServer, collection, application, etc.
    adp_listEntities_whiteList="id,displayName,hostName"  # Optional: filter fields
)
result = session.list_entities(config)
```

### 2. Manage Host Roles

View and manage host role assignments.

```python
from axcpy.adp.models import ManageHostRolesTaskConfig

config = ManageHostRolesTaskConfig()  # Uses defaults
result = session.manage_host_roles(config)
```

### 3. Read Configuration

Read configuration settings for data sources, engines, and other components.

```python
from axcpy.adp.models import ReadConfigurationTaskConfig
from axcpy.adp.models.read_configuration import ConfigToReadArg

config = ReadConfigurationTaskConfig(
    adp_readConfiguration_configsToRead=[
        ConfigToReadArg(**{
            "Configuration ID": "dataSource.file_demo_01",
            "Field list": "name,value,cells",
            "Name value list": "crawlLocationClassifierRules"
        })
    ]
)
result = session.read_configuration(config)
```

### 4. Query Engine

Execute queries and retrieve document counts.

```python
from axcpy.adp.models import QueryEngineTaskConfig

config = QueryEngineTaskConfig(
    adp_queryEngine_applicationIdentifier="documentHold.demo00001",
    adp_queryEngine_query="*"  # Optional: query string
)
result = session.query_engine(config)
print(f"Documents: {result.adp_query_engine_documents_count}")
```

### 5. Taxonomy Statistic

Get statistics and category counts for taxonomies.

```python
from axcpy.adp.models import TaxonomyStatisticTaskConfig
from axcpy.adp.models.taxonomy_statistic import OutputTaxonomy

config = TaxonomyStatisticTaskConfig(
    adp_taxonomyStatistic_engineName="singleMindServer.demo00001",
    adp_taxonomyStatistic_computeCounts="true",
    adp_taxonomyStatistic_outputTaxonomies=[
        OutputTaxonomy(
            Taxonomy="rm_document_hold",
            Mode="Category counts",
            MaximumNumberOfCategories=100
        )
    ]
)
result = session.taxonomy_statistic(config)
```

### 6. Create Data Source

Create new data sources on engines.

```python
from axcpy.adp.models import CreateDataSourceTaskConfig

config = CreateDataSourceTaskConfig(
    adp_createDataSource_dataSourceName="my_datasource",
    adp_createDataSource_engineIdentifier="singleMindServer.demo00001"
)
result = session.create_data_source(config)
print(f"Created: {result.adp_created_data_source_name}")
```

### 7. Export Documents

Export documents with field mappings.

```python
from axcpy.adp.models import ExportDocumentsTaskConfig

field_map = '{"rm_numeric_identifier": "Document ID", "rm_title": "Title"}'
config = ExportDocumentsTaskConfig(
    adp_exportDocuments_applicationIdentifier="documentHold.demo00001",
    adp_exportDocuments_exportName="my_export",
    adp_exportDocuments_exportFields=field_map
)
result = session.export_documents(config)
```

### 8. Manage Users and Groups

Create and manage users, groups, and application roles.

```python
from axcpy.adp.models import ManageUsersAndGroupsTaskConfig
from axcpy.adp.models.manage_users_and_groups import UserDefinition, GroupDefinition

users = [
    UserDefinition(
        Enabled=True,
        ExternalUser=False,
        Password="SecurePassword123!",
        Remove=False,
        UserName="new.user@example.com"
    )
]

groups = [
    GroupDefinition(
        Enabled=True,
        GroupName="ReviewTeam",
        Remove=False
    )
]

config = ManageUsersAndGroupsTaskConfig(
    adp_manageUsersAndGroups_userDefinition=[u.model_dump(by_alias=True) for u in users],
    adp_manageUsersAndGroups_groupDefinition=[g.model_dump(by_alias=True) for g in groups]
)
result = session.manage_users_and_groups(config)
```

### 9. Read Service Alerts

Retrieve system alerts and warnings.

```python
from axcpy.adp.models import ReadServiceAlertsTaskConfig

config = ReadServiceAlertsTaskConfig(
    adp_readServiceAlerts_maximum="10"  # Max number of alerts to retrieve
)
result = session.read_service_alerts(config)

for alert in result.adp_readServiceAlerts_json_output:
    print(f"{alert.severity}: {alert.message}")
```

### 10. Create OCR Job

Create OCR processing jobs for documents (asynchronous task).

```python
from axcpy.adp.models import CreateOcrJobTaskConfig

config = CreateOcrJobTaskConfig(
    adp_createOcrJob_engineName="singleMindServer.demo00001",
    adp_createOcrJob_jobName="OCR Processing Job",
    adp_createOcrJob_jobDescription="Process documents for OCR",
    adp_createOcrJob_query="*",
    adp_createOcrJob_wait="false"  # Async execution
)
execution_id = session.create_ocr_job(config)
print(f"Job submitted: {execution_id}")
```

## Async Execution and Concurrent Tasks

The async client supports running multiple tasks concurrently:

```python
import asyncio
from axcpy.adp import AsyncADPClient, AsyncSession

async def main():
    async with AsyncADPClient(
        base_url="https://axcelerate.example.com:8443",
        ignore_tls=True
    ) as client:
        session = AsyncSession(
            client=client,
            auth_username="your-username",
            auth_password="your-password"
        )
        
        # Execute multiple tasks concurrently
        results = await asyncio.gather(
            session.list_entities(config1),
            session.query_engine(config2),
            session.taxonomy_statistic(config3)
        )
        
        # Process results
        entities, query_result, taxonomy_stats = results

asyncio.run(main())
```

## Error Handling

All tasks raise exceptions on errors. Use try-except blocks for error handling:

```python
try:
    result = session.list_entities(config)
except Exception as e:
    print(f"Error executing task: {e}")
```

## Next Steps

- Explore the [examples/](../examples/) directory for complete working examples
- Check out [adp_examples.py](../examples/adp_examples.py) for synchronous usage
- Check out [adp_async_examples.py](../examples/adp_async_examples.py) for asynchronous usage
- Read the [DESIGN.md](../DESIGN.md) for architecture details
