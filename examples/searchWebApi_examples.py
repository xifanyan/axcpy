"""
SearchWebAPI Examples - Demonstrates usage of the generated SearchWebAPI client
Edit the configuration section below with your credentials
"""

import sys
from pathlib import Path

# Add src to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import asyncio
import httpx
from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.serialization import ParseNodeFactoryRegistry
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

# Import the generated SearchWebAPI client
from axcpy.searchwebapi import SearchWebApiClient


# ==================== CONFIGURATION ====================
# Edit these values for your environment

# API Configuration
API_BASE_URL = "https://vm-rhauswirth2.otxlab.net:8443/searchWebApi"

# Authentication Method - choose one:
AUTH_METHOD = "basic"  # Options: "basic", "bearer", "apikey", "none"

# Basic Auth Credentials (used if AUTH_METHOD = "basic")
USERNAME = "admin"
PASSWORD = "adm1n"

# Bearer Token (used if AUTH_METHOD = "bearer")
BEARER_TOKEN = "your_bearer_token"

# API Key (used if AUTH_METHOD = "apikey")
API_KEY = "your_api_key"
API_KEY_HEADER = "X-API-Key"

# SSL Configuration
VERIFY_SSL = False  # Set to True if you have valid SSL certificates

# HTTP Version
USE_HTTP2 = False  # Set to True to use HTTP/2 instead of HTTP/1.1

# ==================== END CONFIGURATION ====================


class BasicAuthProvider:
    """Basic Authentication Provider with Session Management"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session_id = None  # Store the SWA-SESSION

    def set_session(self, session_id: str):
        """Store the session ID for reuse"""
        self.session_id = session_id
        print(f"  Session stored: {session_id[:50]}...")

    async def authenticate_request(
        self, request, additional_authentication_context: dict = None
    ):
        import base64

        if hasattr(request, "headers"):
            # Add session header if we have one
            if self.session_id:
                request.headers.try_add("SWA-SESSION", self.session_id)
            else:
                # No session yet, send Basic Auth credentials
                credentials = f"{self.username}:{self.password}"
                encoded = base64.b64encode(credentials.encode()).decode()
                request.headers.try_add("Authorization", f"Basic {encoded}")

        return request


class BearerTokenProvider:
    """Bearer Token Authentication Provider"""

    def __init__(self, token: str):
        self.token = token

    async def authenticate_request(
        self, request, additional_authentication_context: dict = None
    ):
        if hasattr(request, "headers"):
            request.headers.try_add("Authorization", f"Bearer {self.token}")
        return request


class ApiKeyProvider:
    """API Key Authentication Provider"""

    def __init__(self, api_key: str, header_name: str = "X-API-Key"):
        self.api_key = api_key
        self.header_name = header_name

    async def authenticate_request(
        self, request, additional_authentication_context: dict = None
    ):
        if hasattr(request, "headers"):
            request.headers.try_add(self.header_name, self.api_key)
        return request


class SessionCapturingHttpClient(httpx.AsyncClient):
    """HTTP client that captures SWA-SESSION from responses"""

    def __init__(self, auth_provider=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth_provider = auth_provider

    async def send(self, request, **kwargs):
        response = await super().send(request, **kwargs)

        # Capture SWA-SESSION from response headers
        if self.auth_provider and "swa-session" in response.headers:
            session_id = response.headers["swa-session"]
            if hasattr(self.auth_provider, "set_session"):
                self.auth_provider.set_session(session_id)

        return response


async def test_api():
    """Test the API connection with configured settings"""

    print("=" * 60)
    print("SearchWebAPI Client Test")
    print("=" * 60)
    print(f"API URL: {API_BASE_URL}")
    print(f"Auth Method: {AUTH_METHOD}")
    print(f"SSL Verification: {VERIFY_SSL}")
    print(f"HTTP/2: {USE_HTTP2}")
    print("=" * 60)
    print()

    try:
        # Register serialization factories
        registry = ParseNodeFactoryRegistry()
        registry.CONTENT_TYPE_ASSOCIATED_FACTORIES["application/json"] = (
            JsonParseNodeFactory()
        )
        registry.CONTENT_TYPE_ASSOCIATED_FACTORIES["text/plain"] = (
            TextParseNodeFactory()
        )

        # Setup authentication based on method
        if AUTH_METHOD == "basic":
            print(f"Using Basic Auth with username: {USERNAME}")
            auth_provider = BasicAuthProvider(USERNAME, PASSWORD)
        elif AUTH_METHOD == "bearer":
            print("Using Bearer Token authentication")
            auth_provider = BearerTokenProvider(BEARER_TOKEN)
        elif AUTH_METHOD == "apikey":
            print(f"Using API Key in header: {API_KEY_HEADER}")
            auth_provider = ApiKeyProvider(API_KEY, API_KEY_HEADER)
        else:
            print("Using no authentication (anonymous)")
            auth_provider = AnonymousAuthenticationProvider()

        # Create HTTP client with session capture
        http_client = SessionCapturingHttpClient(
            auth_provider=auth_provider,
            verify=VERIFY_SSL,
            http2=USE_HTTP2,
            timeout=30.0,
            follow_redirects=True,
        )

        # Create request adapter and client
        request_adapter = HttpxRequestAdapter(auth_provider, http_client=http_client)
        request_adapter.base_url = API_BASE_URL
        client = SearchWebApiClient(request_adapter)

        # Test 1: Login
        print("\n[TEST 1] Testing login endpoint...")
        print("  → Sending Basic Auth credentials...")
        try:
            login_response = await client.login.post()
            print("✅ Login successful!")
            print(f"   Response: {login_response[:100]}...")
            if hasattr(auth_provider, "session_id") and auth_provider.session_id:
                print(f"   ✓ Session captured and stored")
        except Exception as e:
            print(f"❌ Login failed: {type(e).__name__}")
            print(f"   Details: {e}")
            return

        # Test 2: Get Projects (should use session)
        print("\n[TEST 2] Testing projects endpoint...")
        print("  → Using stored session (no auth credentials sent)...")
        try:
            projects = await client.projects.get()
            print("✅ Retrieved projects using session!")
            print(f"   Response: {projects}")
        except Exception as e:
            print(f"❌ Failed to get projects: {type(e).__name__}")
            print(f"   Details: {e}")

        # Test 3: Get Projects again (verify session reuse)
        print("\n[TEST 3] Testing projects endpoint again...")
        print("  → Reusing same session...")
        try:
            projects = await client.projects.get()
            print("✅ Retrieved projects again with same session!")
            print(f"   Response: {projects[:100]}...")
        except Exception as e:
            print(f"❌ Failed to get projects: {type(e).__name__}")
            print(f"   Details: {e}")

        # Test 3.5: Get field information for a specific collection
        print("\n[TEST 4] Testing fields endpoint...")
        print("  → Getting fields for singleMindServer.demo00001/default...")
        try:
            fields = (
                await client.projects.by_project_id("singleMindServer.demo00001")
                .collections.by_collection_id("default")
                .fields.get()
            )
            print("✅ Retrieved fields!")
            print(f"   Response: {fields}...")
        except Exception as e:
            print(f"❌ Failed to get fields: {type(e).__name__}")
            print(f"   Details: {e}")

        # Test 5: Search for documents with specific fields
        print("\n[TEST 5] Testing search endpoint with field retrieval...")
        print("  → Searching for documents in singleMindServer.demo00001/default...")
        try:
            import json
            from axcpy.searchwebapi.generated.projects.item.collections.item.records.records_request_builder import (
                RecordsRequestBuilder,
            )

            # Request specific fields to be returned with the search results
            fields_to_retrieve = [
                "rm_numeric_identifier",  # Document ID
                "rm_subject",  # Subject
                "meta_title",  # Title
                "rm_filename",  # File Name
                "rm_source",  # Data Source
                "rm_custodian",  # Custodian
                "rm_fileextension",  # File Extension
                "rm_filesize",  # File Size
                "rm_creationdate",  # Creation Date
                "rm_sentdate",  # Sent Date
                "meta_from",  # Sender
                "meta_to",  # Recipients
            ]

            search_results = (
                await client.projects.by_project_id("singleMindServer.demo00001")
                .collections.by_collection_id("default")
                .records.get(
                    RequestConfiguration(
                        query_parameters=RecordsRequestBuilder.RecordsRequestBuilderGetQueryParameters(
                            query="*",
                            limit=3,
                            page=1,
                            fields=",".join(
                                fields_to_retrieve
                            ),  # Specify fields to retrieve
                        )
                    )
                )
            )
            print("✅ Search successful!")

            # Parse and display the results
            if isinstance(search_results, bytes):
                results_json = json.loads(search_results.decode("utf-8"))
                print(f"   Total results: {results_json.get('numberResults', 'N/A')}")

                if "results" in results_json:
                    for idx, record in enumerate(results_json["results"], 1):
                        print(f"\n   Document {idx}:")
                        print(f"      Record ID: {record.get('id', 'N/A')}")
                        print(f"      Unique Field: {record.get('uniqueField', 'N/A')}")

                        # The 'fields' array contains the requested field values
                        if "fields" in record and record["fields"]:
                            print(
                                f"      Fields retrieved: {len(record['fields'])} fields"
                            )
                            for field in record["fields"]:
                                field_id = field.get("id", "unknown")
                                field_value = field.get("value", "")
                                # Truncate long values for display
                                display_value = (
                                    str(field_value)[:100] + "..."
                                    if len(str(field_value)) > 100
                                    else field_value
                                )
                                print(f"         {field_id}: {display_value}")
                        else:
                            print(f"      No fields returned")
                            print(f"      Available keys: {list(record.keys())}")
                else:
                    print(
                        f"   No 'results' key found. Available keys: {results_json.keys()}"
                    )
                    print(
                        f"   Full response: {json.dumps(results_json, indent=3)[:1000]}..."
                    )
        except Exception as e:
            print(f"❌ Search failed: {type(e).__name__}")
            print(f"   Details: {e}")
            import traceback

            traceback.print_exc()

        # Test 99: Logout
        print("\n[TEST 99] Testing logout endpoint...")
        try:
            logout_response = (
                await client.logout.delete()
            )  # Use DELETE method, not POST
            print("✅ Logout successful!")
            print(f"   Response: {logout_response[:100]}...")
            # Clear the session after logout
            if hasattr(auth_provider, "session_id"):
                auth_provider.session_id = None
                print("   ✓ Session cleared")
        except Exception as e:
            print(f"❌ Logout failed: {type(e).__name__}")
            print(f"   Details: {e}")

        print("\n" + "=" * 60)
        print("Tests completed!")
        print("=" * 60)

    except httpx.ConnectError as e:
        print(f"\n❌ Connection Error: Cannot connect to {API_BASE_URL}")
        print(f"   Make sure the server is running and the URL is correct.")
        print(f"   Details: {e}")
    except httpx.TimeoutException as e:
        print(f"\n❌ Timeout Error: Request took too long")
        print(f"   Details: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {type(e).__name__}")
        print(f"   Details: {e}")
        import traceback

        traceback.print_exc()
    finally:
        if "http_client" in locals():
            await http_client.aclose()


if __name__ == "__main__":
    print("\n⚠️  Remember to edit the configuration section at the top of this file!")
    print("Press Enter to continue or Ctrl+C to cancel...")
    input()

    asyncio.run(test_api())
