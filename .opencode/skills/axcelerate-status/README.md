# AXcelerate Status Skill for OpenCode

This OpenCode skill enables you to check the operational status of AXcelerate entities (SingleMind servers, collections, etc.) directly from your conversations with OpenCode.

## Installation

The skill is already installed in this project at `.opencode/skills/axcelerate-status/SKILL.md`.

OpenCode will automatically discover and load this skill when you start a session in this repository.

## Prerequisites

The skill comes with default credentials pre-configured for the development environment:
- **Username**: `adpuser`
- **Password**: `adpus3r`
- **Base URL**: `https://vm-rhauswirth2.otxlab.net:8443`

If you want to use different credentials, set these environment variables to override the defaults:

```bash
export ADP_USERNAME="your_adp_username"
export ADP_PASSWORD="your_adp_password"
export ADP_BASE_URL="https://your-adp-server:8443"
```

You can also add these to your shell profile (`.bashrc`, `.zshrc`, etc.) to make them persistent.

## How to Use

Once the skill is loaded, OpenCode will automatically recognize when you ask about AXcelerate entity status and use this skill to help you.

### Example Queries

**Check a specific server:**
```
What's the status of demo00001?
```

**List all servers:**
```
Show me all SingleMind servers
```

**Check if a server is running:**
```
Is singleMindServer.demo00001 running?
```

**Get detailed information:**
```
Get detailed status for all servers including hostname
```

### What OpenCode Will Do

When you ask about entity status, OpenCode will:

1. **Load the skill** (automatically when needed)
2. **Check for credentials** (environment variables or ask you)
3. **Run the appropriate command** using the `axcpy` CLI
4. **Parse the results** and present them in a user-friendly format
5. **Provide insights** about the operational state

### Example Interaction

```
You: What's the status of demo00001?

OpenCode: I'll check the status of the SingleMind server demo00001 for you.
          [Runs: uv run axcpy adp list-entities --id "singleMindServer.demo00001" --ignore-tls]
          
          The server demo00001 (Display Name: Demo Server) is currently STARTED 
          and running normally.
```

## Skill Capabilities

The skill can:
- ✅ Query status of specific entities by ID
- ✅ List all entities of a type
- ✅ Show process status (STARTED, STOPPED, ERROR, etc.)
- ✅ Display entity details (ID, display name, hostname)
- ✅ Handle authentication automatically
- ✅ Provide error troubleshooting guidance

## Process Status Values

The skill understands these common status values:
- `STARTED`: Entity is running normally
- `STOPPED`: Entity is stopped
- `STARTING`: Entity is in the process of starting
- `STOPPING`: Entity is in the process of stopping
- `ERROR`: Entity encountered an error

## Advanced Usage

### Query Different Entity Types

```
Check the status of collection entities
```

### Get Debug Information

```
Show me detailed debug information for all servers
```

### Custom Field Selection

```
List all servers with ID, displayName, hostName, and processStatus
```

## Troubleshooting

If the skill doesn't work as expected:

1. **Verify environment variables are set:**
   ```bash
   echo $ADP_USERNAME
   echo $ADP_PASSWORD
   echo $ADP_BASE_URL
   ```

2. **Check that axcpy is installed:**
   ```bash
   uv run axcpy --help
   ```

3. **Test the command directly:**
   ```bash
   uv run axcpy adp list-entities --id "" --ignore-tls
   ```

4. **Check OpenCode skill loading:**
   In OpenCode, OpenCode should automatically see the skill. You can verify by asking:
   ```
   What skills do you have available?
   ```

## Customization

You can customize the skill by editing `.opencode/skills/axcelerate-status/SKILL.md`:

- Change default entity types
- Add more example queries
- Adjust output formats
- Add custom error handling logic

## Permissions

By default, this skill has no special permissions configured. To control access:

### Allow the skill globally (in `opencode.json`):
```json
{
  "permission": {
    "skill": {
      "axcelerate-status": "allow"
    }
  }
}
```

### Require user confirmation before use:
```json
{
  "permission": {
    "skill": {
      "axcelerate-status": "ask"
    }
  }
}
```

### Disable the skill:
```json
{
  "permission": {
    "skill": {
      "axcelerate-status": "deny"
    }
  }
}
```

## Integration with Other Tools

This skill works seamlessly with:
- The `axcpy` CLI tool (which it uses internally)
- Your existing ADP authentication setup
- OpenCode's command execution capabilities
- OpenCode's natural language understanding

## Contributing

To improve this skill:

1. Edit `.opencode/skills/axcelerate-status/SKILL.md`
2. Test your changes by asking OpenCode relevant questions
3. Share improvements with your team

## License

MIT License - Same as the axcpy project

## Support

For issues or questions:
- Check the main axcpy documentation
- Review OpenCode skill documentation: https://opencode.ai/docs/skills
- Ask OpenCode directly: "How does the axcelerate-status skill work?"
