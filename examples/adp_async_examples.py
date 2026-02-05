#!/usr/bin/env python3
"""
Async example demonstrating AsyncSession client sharing with asyncio.

This script shows how to create a shared AsyncADPClient and use it across
multiple AsyncSession instances with different task types using asyncio.

Run with: python adp_async_examples.py
Run with debug: python adp_async_examples.py --debug
"""

import sys
from pathlib import Path
import logging
import asyncio

# Add src to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from axcpy.adp import AsyncADPClient, AsyncSession
from axcpy.adp.models import (
    CreateOcrJobTaskConfig,
    ListEntitiesTaskConfig,
    ManageHostRolesTaskConfig,
    QueryEngineTaskConfig,
    ReadConfigurationTaskConfig,
    TaxonomyStatisticTaskConfig,
)
from axcpy.adp.models.read_configuration import ConfigToReadArg
from axcpy.adp.models.taxonomy_statistic import OutputTaxonomy

ADPUSERNAME = "adpuser"
ADPPASSWORD = "adpus3r"


async def list_entities_example(session: AsyncSession):
    """Example showing List Entities task using session.list_entities() method."""
    print("\n[*] Example 1: List Entities Task (Async)")

    try:
        config = ListEntitiesTaskConfig(
            adp_listEntities_type="singleMindServer",
            # adp_listEntities_whiteList="id",  # ,displayName,hostNane,hostID",
        )
        result = await session.list_entities(config)
        for entity in result.adp_entities_json_output:
            print(
                f"  - ID: {entity.get('id')}, Display Name: {entity.get('displayName')}, Host Name: {entity.get('hostName')}"
            )

    except Exception as e:
        print(f"[X] Error: {e}")


async def manage_host_roles_example(session: AsyncSession):
    """Example showing Manage Host Roles task using session.manage_host_roles() method."""
    print("\n[*] Example 2: Manage Host Roles Task (Async)")

    try:
        config = ManageHostRolesTaskConfig()  # Use defaults
        result = await session.manage_host_roles(config)

        if result.adp_manageHostRoles_json_output:
            for hostname, roles in result.adp_manageHostRoles_json_output.items():
                print(f"  - {hostname}: {(roles)}")
    except Exception as e:
        print(f"[X] Error: {e}")


async def read_configuration_example(session: AsyncSession):
    """Example showing Read Configuration task using session.read_configuration() method."""
    print("\n[*] Example 3: Read Configuration Task (Async)")

    try:
        config = ReadConfigurationTaskConfig(
            adp_readConfiguration_configsToRead=[
                ConfigToReadArg(
                    **{
                        "Configuration ID": "dataSource.file_demo_01",
                        "Field list": "name,value,cells",
                        "Name value list": "crawlLocationClassifierRules,uriPerlPatterns",
                        "Dynamic Component Names": "x",
                    }
                )
            ],
        )
        result = await session.read_configuration(config)

        print(f"Output file: {result.adp_readConfiguration_output_file_name}")
        print("Configuration data:")
        for (
            config_name,
            config_info,
        ) in result.adp_readConfiguration_json_output.items():
            print(f"  - Configuration: {config_name}")
            print(f"    Global Parameters: {len(config_info.Global.Static.Parameters)} items")
            print(f"    Dynamic Components: {len(config_info.DynamicComponents)} items")

            # Show first few parameters if they exist
            if config_info.Global.Static.Parameters:
                print(f"{config_info.Global.Static.Parameters}")

    except Exception as e:
        print(f"[X] Error: {e}")


async def query_engine_example(session: AsyncSession):
    """Example showing Query Engine task using session.query_engine() method."""
    print("\n[*] Example 4: Query Engine Task (Async)")

    try:
        config = QueryEngineTaskConfig(
            adp_queryEngine_engineName="",
            adp_queryEngine_applicationIdentifier="documentHold.demo00001",
        )
        result = await session.query_engine(config)

        print(f"Query Results:")
        print(f"  - Document Count: {result.adp_query_engine_documents_count}")
        print(f"  - Aggregated Value: {result.adp_query_engine_aggregated_value}")

    except Exception as e:
        print(f"[X] Error: {e}")


async def taxonomy_statistics_example(session: AsyncSession):
    """Example showing Taxonomy Statistic task using session.taxonomy_statistic() method."""
    print("\n[*] Example 5: Taxonomy Statistic Task (Async)")

    try:
        # Define output taxonomies with specific configuration
        output_taxonomies = [
            OutputTaxonomy(
                Taxonomy="rm_document_hold",
                Mode="Category counts",
                MaximumNumberOfCategories=100,
            )
        ]

        config = TaxonomyStatisticTaskConfig(
            adp_taxonomyStatistic_engineName="singleMindServer.demo00001",
            adp_taxonomyStatistic_computeCounts="true",
            adp_taxonomyStatistic_outputTaxonomies=output_taxonomies,
            adp_taxonomyStatistic_listCategoryProperties="false",
        )

        result = await session.taxonomy_statistic(config)

        print(f"Taxonomy Statistics:")

        if result.adp_taxonomy_statistics_json_output:
            stats = result.adp_taxonomy_statistics_json_output
            print(f"  - Date: {stats.date}")
            print(f"  - Search Parameters: {len(stats.searchParameter)} items")

            for taxonomy in stats.statistics.taxonomy:
                print(f"\n  [+] Taxonomy: {taxonomy.id}")
                print(f"     Categories: {len(taxonomy.category)} items")

                # Show first few categories
                for i, category in enumerate(taxonomy.category[:3]):
                    print(f"     - {category.id} ({category.displayName})")
                    if category.count is not None:
                        print(f"       Count: {category.count}")

                if len(taxonomy.category) > 3:
                    print(f"     ... and {len(taxonomy.category) - 3} more categories")

    except Exception as e:
        print(f"[X] Error: {e}")


async def concurrent_tasks_example(session: AsyncSession):
    """Example showing concurrent execution of multiple tasks using the same session."""
    print("\n[*] Example 6: Concurrent Tasks Execution (Async)")

    try:
        # Define multiple configurations
        list_entities_config = ListEntitiesTaskConfig(
            adp_listEntities_type="singleMindServer",
        )

        manage_roles_config = ManageHostRolesTaskConfig()

        query_config = QueryEngineTaskConfig(
            adp_queryEngine_engineName="",
            adp_queryEngine_applicationIdentifier="documentHold.demo00001",
        )

        # Execute all tasks concurrently using the session methods
        print("  [*] Launching 3 tasks concurrently...")
        results = await asyncio.gather(
            session.list_entities(list_entities_config),
            session.manage_host_roles(manage_roles_config),
            session.query_engine(query_config),
            return_exceptions=True,
        )

        # Process results
        print("  [+] All tasks completed!")

        # Result 1: List Entities
        if isinstance(results[0], Exception):
            print(f"  [X] List Entities failed: {results[0]}")
        else:
            print(
                f"  [+] List Entities returned {len(results[0].adp_entities_json_output)} entities"
            )

        # Result 2: Manage Host Roles
        if isinstance(results[1], Exception):
            print(f"  [X] Manage Host Roles failed: {results[1]}")
        else:
            print(
                f"  [+] Manage Host Roles returned {len(results[1].adp_manageHostRoles_json_output)} hosts"
            )

        # Result 3: Query Engine
        if isinstance(results[2], Exception):
            print(f"  [X] Query Engine failed: {results[2]}")
        else:
            print(
                f"  [+] Query Engine returned {results[2].adp_query_engine_documents_count} documents"
            )

    except Exception as e:
        print(f"[X] Concurrent execution error: {e}")


async def create_ocr_job_example(session: AsyncSession):
    """Example showing Create OCR Job task (async only)."""
    print("\n[*] Example 7: Create OCR Job Task (Async)")

    try:
        config = CreateOcrJobTaskConfig(
            adp_createOcrJob_engineName="singleMindServer.demo00001",
            adp_createOcrJob_applicationIdentifier="documentHold.demo00001",
            adp_createOcrJob_jobName="OCR Processing Job",
            adp_createOcrJob_jobDescription="Process documents for OCR",
            adp_createOcrJob_query="*",
            adp_createOcrJob_wait="false",  # Async execution
            adp_createOcrJob_jobPriority="10",
            adp_createOcrJob_engineUserName="adpuser",
        )

        execution_id = await session.create_ocr_job(config)

        print("  [+] OCR Job Created Successfully")
        print(f"  - Execution ID: {execution_id}")
        print(f"\n  [i] Monitor job progress with session.statusAndProgress()")

    except Exception as e:
        print(f"  [X] Error: {e}")


async def main():
    """Main async function that creates a shared client and demonstrates its usage."""
    # Check if --debug flag is passed
    debug_mode = "--debug" in sys.argv

    # Basic logging configuration for demo purposes
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    print("[*] Creating shared AsyncADPClient for multiple async examples")
    print("=" * 60)

    # Create a single shared async client that will be used by all examples
    async with AsyncADPClient(
        base_url="https://vm-rhauswirth2.otxlab.net:8443",
        ignore_tls=True,
        timeout=30.0,
        debug=debug_mode,
    ) as shared_client:
        print(f"[+] Created shared async client with ID: {id(shared_client)}")

        # Create a single session object that will be reused for all examples
        session = AsyncSession(
            client=shared_client, auth_username=ADPUSERNAME, auth_password=ADPPASSWORD
        )
        print(f"[+] Created shared session with username: {session.auth_username}")
        print("[*] This same session will be reused for all task examples")

        # Run individual examples - all reusing the same session
        # await list_entities_example(session)
        # await manage_host_roles_example(session)
        # await query_engine_example(session)
        await read_configuration_example(session)
        await taxonomy_statistics_example(session)

        # Demonstrate concurrent execution with the same session
        await concurrent_tasks_example(session)

    print("\n[+] All async examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
