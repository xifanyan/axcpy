#!/usr/bin/env python3
"""
Simple example demonstrating Session client sharing.

This script shows how to create a shared ADPClient and use it across
multiple Session instances with different task types.

Run with: python demo.py
"""

import logging
import sys
from pathlib import Path

# Add src to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from axcpy.adp import ADPClient, Session
from axcpy.adp.models import (
    CreateDataSourceTaskConfig,
    ExportDocumentsTaskConfig,
    ListEntitiesTaskConfig,
    ManageHostRolesTaskConfig,
    ManageUsersAndGroupsTaskConfig,
    QueryEngineTaskConfig,
    ReadConfigurationTaskConfig,
    ReadServiceAlertsTaskConfig,
    TaxonomyStatisticTaskConfig,
)
from axcpy.adp.models.manage_users_and_groups import (
    ApplicationRoles,
    GroupDefinition,
    UserDefinition,
    UserToGroup,
)
from axcpy.adp.models.read_configuration import ConfigToReadArg
from axcpy.adp.models.taxonomy_statistic import OutputTaxonomy

ADPUSERNAME = "adpuser"
ADPPASSWORD = "adpus3r"


def list_entities_example(session: Session):
    """Example showing List Entities task using session.list_entities() method."""
    print("\n[*] Example 1: List Entities Task")

    try:
        config = ListEntitiesTaskConfig(
            adp_listEntities_type="singleMindServer",
            # adp_listEntities_whiteList="id",  # ,displayName,hostNane,hostID",
        )
        result = session.list_entities(config)
        for entity in result.adp_entities_json_output:
            print(
                f"  - ID: {entity.get('id')}, Display Name: {entity.get('displayName')}, Host Name: {entity.get('hostName')}"
            )

    except Exception as e:
        print(f"❌ Error: {e}")


def manage_host_roles_example(session: Session):
    """Example showing Manage Host Roles task using session.manage_host_roles() method."""
    print("\n[*] Example 2: Manage Host Roles Task")

    try:
        config = ManageHostRolesTaskConfig()  # Use defaults
        result = session.manage_host_roles(config)

        if result.adp_manageHostRoles_json_output:
            for hostname, roles in result.adp_manageHostRoles_json_output.items():
                print(f"  - {hostname}: {(roles)}")
    except Exception as e:
        print(f"❌ Error: {e}")


def read_configuration_example(session: Session):
    """Example showing Read Configuration task using session.read_configuration() method."""
    print("\n[*] Example 3: Read Configuration Task")

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
        result = session.read_configuration(config)

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
        print(f"❌ Error: {e}")


def export_documents_example(session: Session):
    """Example showing Export Documents task using session.export_documents() method."""
    print("\n[*] Example 6: Export Documents Task")

    fieldMap = '{"rm_numeric_identifier": "Document ID", "rm_title": "Title" }'
    try:
        config = ExportDocumentsTaskConfig(
            adp_exportDocuments_applicationIdentifier="documentHold.demo00001",
            adp_exportDocuments_exportName="demo_export",
            adp_exportDocuments_exportFields=fieldMap,
        )
        result = session.export_documents(config)
        print(result)

    except Exception as e:
        print(f"❌ Error: {e}")


def query_engine_example(session: Session):
    """Example showing Query Engine task using session.query_engine() method."""
    print("\n[*] Example 4: Query Engine Task")

    try:
        config = QueryEngineTaskConfig(
            adp_queryEngine_engineName="",
            adp_queryEngine_applicationIdentifier="documentHold.demo00001",
        )
        result = session.query_engine(config)

        print("Query Results:")
        print(f"  - Document Count: {result.adp_query_engine_documents_count}")
        print(f"  - Aggregated Value: {result.adp_query_engine_aggregated_value}")

    except Exception as e:
        print(f"❌ Error: {e}")


def taxonomy_statistics_example(session: Session):
    """Example showing Taxonomy Statistic task using session.taxonomy_statistic() method."""
    print("\n[*] Example 5: Taxonomy Statistic Task")

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

        result = session.taxonomy_statistic(config)

        print("Taxonomy Statistics:")

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
        print(f"❌ Error: {e}")


def create_data_source_example(session: Session):
    """Example showing Create Data Source task using session.create_data_source() method."""
    print("\n[*] Example 6: Create Data Source Task")

    try:
        config = CreateDataSourceTaskConfig(
            adp_createDataSource_dataSourceName="pyds",
            adp_createDataSource_engineIdentifier="singleMindServer.demo00001",
        )

        result = session.create_data_source(config)

        print("✅ Data Source Created Successfully")
        print(f"  - Data Source Name: {result.adp_created_data_source_name}")
        print(f"  - Data Source Display Name: {result.adp_created_data_source_displayname}")
        print(f"  - Host Name: {result.adp_hostname}")
        print(f"  - Engine: {result.adp_chosen_engine}")
        print(f"  - Template Used: {result.adp_used_data_source_template}")
        print(f"  - Host CPU Load: {result.adp_chosen_host_cpu_load}")
        print(f"  - Host Memory: {result.adp_chosen_host_memory}")
        print(f"  - Host Memory Ratio: {result.adp_chosen_host_memory_ratio}")

    except Exception as e:
        print(f"❌ Error: {e}")


def manage_users_and_groups_example(session: Session) -> None:
    """Example showing Manage Users and Groups task."""
    print("\n[*] Example 7: Manage Users and Groups Task")

    try:
        # Define users to create or modify
        users_to_manage = [
            UserDefinition(
                Enabled=True,
                ExternalUser=False,
                Password="SecurePassword123!",
                Remove=False,
                UserName="new.user@example.com",
            ),
            UserDefinition(
                Enabled=True,
                ExternalUser=True,
                Password="",
                Remove=False,
                UserName="external.user@company.com",
            ),
        ]

        # Define groups to create or modify
        groups_to_manage = [
            GroupDefinition(
                Enabled=True,
                GroupName="ReviewTeam",
                Remove=False,
            ),
            GroupDefinition(
                Enabled=True,
                GroupName="AdminTeam",
                Remove=False,
            ),
        ]

        # Assign users to groups
        user_group_assignments = [
            UserToGroup(
                Enabled=True,
                GroupName="ReviewTeam",
                Remove=False,
                UserName="new.user@example.com",
            ),
            UserToGroup(
                Enabled=True,
                GroupName="AdminTeam",
                Remove=False,
                UserName="new.user@example.com",
            ),
        ]

        # Define application roles for users/groups
        app_roles = [
            ApplicationRoles(
                GroupOrUserName="new.user@example.com",
                Enabled=True,
                ApplicationIdentifier="documentHold",
                Roles="reviewer,editor",
            ),
            ApplicationRoles(
                GroupOrUserName="AdminTeam",
                Enabled=True,
                ApplicationIdentifier="documentHold",
                Roles="admin",
            ),
        ]

        # Create configuration
        config = ManageUsersAndGroupsTaskConfig(
            adp_manageUsersAndGroups_userDefinition=[
                user.model_dump(by_alias=True) for user in users_to_manage
            ],
            adp_manageUsersAndGroups_groupDefinition=[
                group.model_dump(by_alias=True) for group in groups_to_manage
            ],
            # adp_manageUsersAndGroups_assignmentUserToGroup=[
            #    assignment.model_dump(by_alias=True) for assignment in user_group_assignments
            # ],
            # adp_manageUsersAndGroups_addApplicationRoles=[
            #    role.model_dump(by_alias=True) for role in app_roles
            # ],
            # Optionally filter by application or group
            # adp_manageUsersAndGroups_AppIdsToFilterFor="documentHold",
            # adp_manageUsersAndGroups_GroupUserIdsToFilterFor="ReviewTeam",
        )

        # Execute the task
        result = session.manage_users_and_groups(config)

        # Display results
        print("✅ Users and Groups Management Completed")
        print(f"  - Output file: {result.adp_manageUsersAndGroups_output_file_name}")

        # Display groups
        if result.adp_manageUsersAndGroups_json_output.Groups:
            print(
                f"\n  [+] Groups found: {len(result.adp_manageUsersAndGroups_json_output.Groups)}"
            )
            for (
                group_id,
                group_data,
            ) in result.adp_manageUsersAndGroups_json_output.Groups.items():
                print(f"     - Group: {group_data.Name}")
                print(f"       Display Name: {group_data.DisplayName}")
                if group_data.Users:
                    print(f"       Users ({len(group_data.Users)}): {', '.join(group_data.Users)}")
                if group_data.Description:
                    print(f"       Description: {group_data.Description}")

        # Display users
        if result.adp_manageUsersAndGroups_json_output.Users:
            print(f"\n  [+] Users found: {len(result.adp_manageUsersAndGroups_json_output.Users)}")
            for (
                user_id,
                user_data,
            ) in result.adp_manageUsersAndGroups_json_output.Users.items():
                print(f"     - User: {user_data.Name}")
                print(f"       Display Name: {user_data.DisplayName}")
                print(f"       External: {user_data.External}")
                if user_data.EmailAddress:
                    print(f"       Email: {user_data.EmailAddress}")

        # Filter example - Show only users in specific application
        if result.adp_manageUsersAndGroups_json_output.Groups:
            print("\n  [*] Filtering Results Example:")
            # Users in ReviewTeam group
            review_team_groups = [
                (k, v)
                for k, v in result.adp_manageUsersAndGroups_json_output.Groups.items()
                if "Review" in v.Name
            ]
            if review_team_groups:
                for group_id, group_data in review_team_groups:
                    print("     - Review Team Users:")
                    for username in group_data.Users:
                        user_data = result.adp_manageUsersAndGroups_json_output.Users.get(username)
                        if user_data:
                            print(f"       - {user_data.DisplayName} ({username})")

    except Exception as e:
        print(f"❌ Error: {e}")


def read_service_alerts_example(session: Session):
    """Example showing Read Service Alerts task using session.read_service_alerts() method."""
    print("\n[*] Example 8: Read Service Alerts Task")

    try:
        config = ReadServiceAlertsTaskConfig(
            adp_readServiceAlerts_maximum="10",
        )
        result = session.read_service_alerts(config)

        print(f"Found {len(result.adp_readServiceAlerts_json_output)} alerts")

        for alert in result.adp_readServiceAlerts_json_output:
            print(
                f"  - ID: {alert.id}, Severity: {alert.severity}, Message: {alert.message[:50]}..."
            )
            if alert.host_name:
                print(f"    Host: {alert.host_name}")
            if alert.report_on:
                print(f"    Reported: {alert.report_on}")

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Main function that creates a shared client and demonstrates its usage."""
    import sys

    # Check if --debug flag is passed
    debug_mode = "--debug" in sys.argv

    # Basic logging configuration for demo purposes (library itself does not configure handlers)
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    print("[*] Creating shared ADPClient for multiple examples")
    print("=" * 60)

    # Create a single shared client that will be used by both examples
    shared_client = ADPClient(
        base_url="https://vm-rhauswirth2.otxlab.net:8443",
        ignore_tls=True,
        timeout=30.0,
        debug=debug_mode,
    )

    print(f"[+] Created shared client with ID: {id(shared_client)}")

    # Create a single session object that will be reused for all examples
    session = Session(client=shared_client, auth_username=ADPUSERNAME, auth_password=ADPPASSWORD)
    print(f"[+] Created shared session with username: {session.auth_username}")
    print("[*] This same session will be reused for all task examples")

    # Pass the session to all example functions
    list_entities_example(session)
    manage_host_roles_example(session)
    read_configuration_example(session)
    query_engine_example(session)
    taxonomy_statistics_example(session)
    # export_documents_example(session)
    # create_data_source_example(session)
    manage_users_and_groups_example(session)
    read_service_alerts_example(session)


if __name__ == "__main__":
    main()
