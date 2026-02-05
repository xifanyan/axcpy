---
name: axcelerate-status
description: Check the status of AXcelerate entities (SingleMind servers, collections, etc.)
license: MIT
compatibility: opencode
metadata:
  category: axcelerate
  workflow: operations
---

## What I do

I check the operational status of AXcelerate entities using the axcpy CLI tool. I can:
- Query the status of SingleMind servers
- List all entities of a specific type
- Show detailed entity information including ID, display name, and process status
- Provide operational insights about the AXcelerate infrastructure

## When to use me

Use this skill when the user asks about:
- "What is the status of [entity]?"
- "Check if [server/entity] is running"
- "Show me all [entities]"
- "Is [entity] online/offline/working?"
- Any question about the operational state of AXcelerate components

## How I work

I run the `axcpy adp list-entities` command with appropriate parameters. The command requires:

### Required Authentication
- ADP username (from `ADP_USERNAME` env var, defaults to: `adpuser`)
- ADP password (from `ADP_PASSWORD` env var, defaults to: `adpus3r`)  
- Base URL (from `ADP_BASE_URL` env var, defaults to: `https://vm-rhauswirth2.otxlab.net:8443`)
- Usually requires `--ignore-tls` flag for development environments

**Default Credentials:**
If environment variables are not set, use these defaults:
- Username: `adpuser`
- Password: `adpus3r`
- Base URL: `https://vm-rhauswirth2.otxlab.net:8443`

### Query Parameters
- `--id`: Entity ID to query (e.g., "singleMindServer.demo00001")
  - Use empty string `""` to list all entities of a type
- `--type`: Entity type (default: "singleMindServer")
- `--white-list`: Fields to return (default: "id,displayName,processStatus")

## Example Usage

### Check a specific server
```bash
# Using environment variables
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  --ignore-tls

# Using explicit credentials (defaults)
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  -u adpuser \
  -p adpus3r \
  -b https://vm-rhauswirth2.otxlab.net:8443 \
  --ignore-tls
```

### List all servers
```bash
# Using environment variables
uv run axcpy adp list-entities \
  --id "" \
  --ignore-tls

# Using explicit credentials (defaults)
uv run axcpy adp list-entities \
  --id "" \
  -u adpuser \
  -p adpus3r \
  -b https://vm-rhauswirth2.otxlab.net:8443 \
  --ignore-tls
```

### Get detailed information
```bash
uv run axcpy adp list-entities \
  --id "" \
  --white-list "id,displayName,processStatus,hostName" \
  --debug \
  --ignore-tls
```

## Process Status Values

Common `processStatus` values you might see:
- `STARTED`: Entity is running normally
- `STOPPED`: Entity is stopped
- `STARTING`: Entity is in the process of starting
- `STOPPING`: Entity is in the process of stopping
- `ERROR`: Entity encountered an error

## Important Notes

1. **Environment Variables**: Check if `ADP_USERNAME`, `ADP_PASSWORD`, and `ADP_BASE_URL` are set. If not set, use these defaults:
   - Username: `adpuser`
   - Password: `adpus3r`
   - Base URL: `https://vm-rhauswirth2.otxlab.net:8443`

2. **Command Construction**: When environment variables are NOT set, explicitly pass credentials:
   ```bash
   uv run axcpy adp list-entities \
     --id "..." \
     -u adpuser \
     -p adpus3r \
     -b https://vm-rhauswirth2.otxlab.net:8443 \
     --ignore-tls
   ```
   When environment variables ARE set, omit the credential flags:
   ```bash
   uv run axcpy adp list-entities \
     --id "..." \
     --ignore-tls
   ```

2. **TLS Certificate**: Always use `--ignore-tls` flag for the development environment at vm-rhauswirth2.otxlab.net.

3. **Field Availability**: The `processStatus` field may not be returned when querying by specific entity ID. For full status information, query with an empty ID to list all entities.

4. **Entity Types**: Besides "singleMindServer", other entity types might include collections, connectors, etc. Ask the user if they need a different entity type.

5. **Output Format**: The command outputs a formatted table by default. Use `--debug` for JSON output and detailed field information.

## Response Format

When reporting status to the user:
1. Show the entity ID and display name
2. Report the process status clearly (e.g., "STARTED", "STOPPED")
3. Include any additional relevant fields like hostname
4. If there are issues, suggest troubleshooting steps
5. If credentials are missing from environment variables, automatically use the default credentials (don't ask the user)

## Error Handling

Common errors and solutions:
- **Authentication failure**: Verify credentials and base URL
- **Connection timeout**: Check network connectivity and base URL
- **TLS errors**: Add `--ignore-tls` flag for dev environments
- **Entity not found**: Verify entity ID format (e.g., "singleMindServer.xxxxx")
- **No processStatus returned**: Query with empty ID to list all entities

## Example Interaction

**User**: "What's the status of demo00001?"

**Assistant**: "I'll check the status of the SingleMind server demo00001 for you."

*Runs*: `uv run axcpy adp list-entities --id "singleMindServer.demo00001" -u adpuser -p adpus3r -b https://vm-rhauswirth2.otxlab.net:8443 --ignore-tls`

**Assistant**: "The server demo00001 (Display Name: Demo Server) is currently **STARTED** and running normally."

---

**User**: "Show me all servers"

**Assistant**: "I'll list all SingleMind servers for you."

*Runs*: `uv run axcpy adp list-entities --id "" -u adpuser -p adpus3r -b https://vm-rhauswirth2.otxlab.net:8443 --ignore-tls`

**Assistant**: "Here are all the servers:
- demo00001: STARTED
- demo00002: STOPPED
- demo00003: STARTED"
