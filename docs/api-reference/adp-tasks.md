# ADP Tasks API Reference

This document provides detailed information about all available ADP tasks in axcpy.

## Table of Contents

1. [List Entities](#list-entities)
2. [Manage Host Roles](#manage-host-roles)
3. [Read Configuration](#read-configuration)
4. [Query Engine](#query-engine)
5. [Taxonomy Statistic](#taxonomy-statistic)
6. [Create Data Source](#create-data-source)
7. [Export Documents](#export-documents)
8. [Manage Users and Groups](#manage-users-and-groups)
9. [Read Service Alerts](#read-service-alerts)
10. [Create OCR Job](#create-ocr-job)

---

## List Entities

List servers, collections, applications, and other entities in your Axcelerate environment.

### Configuration

**Class:** `ListEntitiesTaskConfig`

**Parameters:**
- `adp_listEntities_type` (str): Type of entity to list
  - Options: `"singleMindServer"`, `"collection"`, `"application"`, `"dataSource"`, etc.
- `adp_listEntities_whiteList` (str, optional): Comma-separated list of fields to include
  - Example: `"id,displayName,hostName"`
- `adp_listEntities_filterForHosts` (str, optional): Filter entities by host

### Result

**Class:** `ListEntitiesResult`

**Fields:**
- `adp_entities_json_output` (list[dict]): List of entities with their properties
- `adp_entities_output_file_name` (str): Output file name

### Example

```python
from axcpy.adp.models import ListEntitiesTaskConfig

config = ListEntitiesTaskConfig(
    adp_listEntities_type="singleMindServer",
    adp_listEntities_whiteList="id,displayName,hostName"
)
result = session.list_entities(config)

for entity in result.adp_entities_json_output:
    print(f"{entity['id']}: {entity['displayName']}")
```

---

## Manage Host Roles

View and manage host role assignments.

### Configuration

**Class:** `ManageHostRolesTaskConfig`

**Parameters:**
- `adp_manageHostRoles_displayFormat` (str): Display format (default: `"json"`)
- `adp_manageHostRoles_json_output_variable` (str): Output variable name

### Result

**Class:** `ManageHostRolesResult`

**Fields:**
- `adp_manageHostRoles_json_output` (dict[str, list[str]]): Mapping of hostnames to role lists
- `adp_manageHostRoles_output_file_name` (str): Output file name

### Example

```python
from axcpy.adp.models import ManageHostRolesTaskConfig

config = ManageHostRolesTaskConfig()
result = session.manage_host_roles(config)

for hostname, roles in result.adp_manageHostRoles_json_output.items():
    print(f"{hostname}: {', '.join(roles)}")
```

---

## Read Configuration

Read configuration settings for data sources, engines, and other components.

### Configuration

**Class:** `ReadConfigurationTaskConfig`

**Parameters:**
- `adp_readConfiguration_configsToRead` (list[ConfigToReadArg]): List of configurations to read

**ConfigToReadArg Fields:**
- `Configuration ID` (str): Configuration identifier (e.g., `"dataSource.file_demo_01"`)
- `Field list` (str): Comma-separated list of fields (e.g., `"name,value,cells"`)
- `Name value list` (str, optional): Specific name-value pairs to retrieve
- `Dynamic Component Names` (str, optional): Dynamic component filter

### Result

**Class:** `ReadConfigurationResult`

**Fields:**
- `adp_readConfiguration_json_output` (dict): Configuration data
- `adp_readConfiguration_output_file_name` (str): Output file name

### Example

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

---

## Query Engine

Execute queries and retrieve document counts and aggregated values.

### Configuration

**Class:** `QueryEngineTaskConfig`

**Parameters:**
- `adp_queryEngine_applicationIdentifier` (str): Application identifier
- `adp_queryEngine_engineName` (str, optional): Engine name
- `adp_queryEngine_query` (str, optional): Query string (default: `"*"`)
- `adp_queryEngine_aggregate` (str, optional): Aggregation field

### Result

**Class:** `QueryEngineResult`

**Fields:**
- `adp_query_engine_documents_count` (int): Number of documents matching query
- `adp_query_engine_aggregated_value` (str | None): Aggregated value if specified

### Example

```python
from axcpy.adp.models import QueryEngineTaskConfig

config = QueryEngineTaskConfig(
    adp_queryEngine_applicationIdentifier="documentHold.demo00001",
    adp_queryEngine_query="*"
)
result = session.query_engine(config)
print(f"Found {result.adp_query_engine_documents_count} documents")
```

---

## Taxonomy Statistic

Get statistics and category counts for taxonomies.

### Configuration

**Class:** `TaxonomyStatisticTaskConfig`

**Parameters:**
- `adp_taxonomyStatistic_engineName` (str): Engine name
- `adp_taxonomyStatistic_computeCounts` (str): Compute counts (`"true"` or `"false"`)
- `adp_taxonomyStatistic_outputTaxonomies` (list[OutputTaxonomy]): Taxonomies to output
- `adp_taxonomyStatistic_listCategoryProperties` (str): List category properties

**OutputTaxonomy Fields:**
- `Taxonomy` (str): Taxonomy identifier
- `Mode` (str): Output mode (e.g., `"Category counts"`)
- `MaximumNumberOfCategories` (int): Maximum categories to return

### Result

**Class:** `TaxonomyStatisticResult`

**Fields:**
- `adp_taxonomy_statistics_json_output` (TaxonomyStatistics): Statistics data
- `adp_taxonomyStatistic_output_file_name` (str): Output file name

### Example

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

---

## Create Data Source

Create new data sources on engines.

### Configuration

**Class:** `CreateDataSourceTaskConfig`

**Parameters:**
- `adp_createDataSource_dataSourceName` (str): Name for the new data source
- `adp_createDataSource_engineIdentifier` (str): Engine identifier
- `adp_createDataSource_dataSourceTemplate` (str, optional): Template to use
- `adp_createDataSource_hostBalancing` (str, optional): Host balancing strategy

### Result

**Class:** `CreateDataSourceResult`

**Fields:**
- `adp_created_data_source_name` (str): Created data source name
- `adp_created_data_source_displayname` (str): Display name
- `adp_hostname` (str): Host name where created
- `adp_chosen_engine` (str): Engine used
- `adp_used_data_source_template` (str): Template used
- `adp_chosen_host_cpu_load` (str): CPU load of chosen host
- `adp_chosen_host_memory` (str): Memory of chosen host
- `adp_chosen_host_memory_ratio` (str): Memory ratio of chosen host

### Example

```python
from axcpy.adp.models import CreateDataSourceTaskConfig

config = CreateDataSourceTaskConfig(
    adp_createDataSource_dataSourceName="my_datasource",
    adp_createDataSource_engineIdentifier="singleMindServer.demo00001"
)
result = session.create_data_source(config)
print(f"Created: {result.adp_created_data_source_name}")
```

---

## Export Documents

Export documents with field mappings.

### Configuration

**Class:** `ExportDocumentsTaskConfig`

**Parameters:**
- `adp_exportDocuments_applicationIdentifier` (str): Application identifier
- `adp_exportDocuments_exportName` (str): Export name
- `adp_exportDocuments_exportFields` (str): JSON string mapping fields
  - Format: `'{"source_field": "Target Field Name"}'`
- `adp_exportDocuments_query` (str, optional): Query to filter documents
- `adp_exportDocuments_exportFormat` (str, optional): Export format

### Result

**Class:** `ExportDocumentsResult`

**Fields:**
- `adp_exportDocuments_export_file_name` (str): Exported file path

### Example

```python
from axcpy.adp.models import ExportDocumentsTaskConfig

field_map = '{"rm_numeric_identifier": "Document ID", "rm_title": "Title"}'
config = ExportDocumentsTaskConfig(
    adp_exportDocuments_applicationIdentifier="documentHold.demo00001",
    adp_exportDocuments_exportName="my_export",
    adp_exportDocuments_exportFields=field_map
)
result = session.export_documents(config)
print(f"Exported to: {result.adp_exportDocuments_export_file_name}")
```

---

## Manage Users and Groups

Create and manage users, groups, and application roles.

### Configuration

**Class:** `ManageUsersAndGroupsTaskConfig`

**Parameters:**
- `adp_manageUsersAndGroups_userDefinition` (list[dict]): User definitions
- `adp_manageUsersAndGroups_groupDefinition` (list[dict]): Group definitions
- `adp_manageUsersAndGroups_assignmentUserToGroup` (list[dict], optional): User-to-group assignments
- `adp_manageUsersAndGroups_addApplicationRoles` (list[dict], optional): Application role assignments

**UserDefinition Fields:**
- `Enabled` (bool): Whether user is enabled
- `ExternalUser` (bool): Whether user is external
- `Password` (str): User password
- `Remove` (bool): Whether to remove user
- `UserName` (str): Username/email

**GroupDefinition Fields:**
- `Enabled` (bool): Whether group is enabled
- `GroupName` (str): Group name
- `Remove` (bool): Whether to remove group

### Result

**Class:** `ManageUsersAndGroupsResult`

**Fields:**
- `adp_manageUsersAndGroups_json_output` (ManageUsersAndGroupsOutput): Users and groups data
- `adp_manageUsersAndGroups_output_file_name` (str): Output file name

### Example

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

---

## Read Service Alerts

Retrieve system alerts and warnings.

### Configuration

**Class:** `ReadServiceAlertsTaskConfig`

**Parameters:**
- `adp_readServiceAlerts_maximum` (str): Maximum number of alerts to retrieve (default: `"20"`)
- `adp_readServiceAlerts_display_format` (str): Display format (default: `"json"`)

### Result

**Class:** `ReadServiceAlertsResult`

**Fields:**
- `adp_readServiceAlerts_json_output` (list[ServiceAlert]): List of alerts
- `adp_readServiceAlerts_output_file_name` (str): Output file name

**ServiceAlert Fields:**
- `id` (str): Alert ID
- `severity` (str): Severity level (e.g., `"Warning"`, `"Error"`)
- `message` (str): Alert message
- `host_name` (str | None): Host name if applicable
- `report_on` (str | None): Timestamp

### Example

```python
from axcpy.adp.models import ReadServiceAlertsTaskConfig

config = ReadServiceAlertsTaskConfig(
    adp_readServiceAlerts_maximum="10"
)
result = session.read_service_alerts(config)

for alert in result.adp_readServiceAlerts_json_output:
    print(f"[{alert.severity}] {alert.message}")
    if alert.host_name:
        print(f"  Host: {alert.host_name}")
```

---

## Create OCR Job

Create OCR processing jobs for documents. This is an asynchronous task that returns immediately with an execution ID.

### Configuration

**Class:** `CreateOcrJobTaskConfig`

**Parameters:**
- `adp_createOcrJob_engineName` (str): Engine name
- `adp_createOcrJob_jobName` (str): Job name
- `adp_createOcrJob_jobDescription` (str, optional): Job description
- `adp_createOcrJob_query` (str): Query to select documents (default: `"*"`)
- `adp_createOcrJob_wait` (str): Wait for completion (`"true"` or `"false"`, default: `"false"`)
- `adp_createOcrJob_jobPriority` (str): Job priority (default: `"10"`)
- `adp_createOcrJob_engineUserName` (str | None): Engine username
- `adp_createOcrJob_engineUserPassword` (str): Engine password
- `adp_createOcrJob_applicationIdentifier` (str, optional): Application identifier

### Result

Returns execution ID as a string.

### Example

```python
from axcpy.adp.models import CreateOcrJobTaskConfig

config = CreateOcrJobTaskConfig(
    adp_createOcrJob_engineName="singleMindServer.demo00001",
    adp_createOcrJob_jobName="OCR Processing Job",
    adp_createOcrJob_jobDescription="Process documents for OCR",
    adp_createOcrJob_query="*",
    adp_createOcrJob_wait="false"
)
execution_id = session.create_ocr_job(config)
print(f"Job submitted: {execution_id}")

# Monitor job status
# status = session.statusAndProgress(execution_id)
```

---

## Common Patterns

### Error Handling

All tasks raise exceptions on errors:

```python
try:
    result = session.list_entities(config)
except Exception as e:
    print(f"Task failed: {e}")
```

### Async Execution

All tasks support async execution:

```python
result = await async_session.list_entities(config)
```

### Concurrent Tasks

Run multiple tasks concurrently with asyncio:

```python
results = await asyncio.gather(
    session.list_entities(config1),
    session.query_engine(config2),
    session.taxonomy_statistic(config3)
)
```

### Debug Mode

Enable debug logging to see request/response details:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

client = ADPClient(
    base_url="...",
    debug=True
)
```
