# AXcelerate Status Skill - Quick Start Guide

## ✅ Installation Complete!

Your OpenCode skill for checking AXcelerate entity status has been successfully installed at:
```
.opencode/skills/axcelerate-status/SKILL.md
```

## 🚀 Quick Start

### Step 1: Set Up Authentication (Optional)

The skill comes with default credentials pre-configured:
- **Username**: `adpuser`
- **Password**: `adpus3r`
- **Base URL**: `https://vm-rhauswirth2.otxlab.net:8443`

If you want to use different credentials, set these environment variables:

```bash
export ADP_USERNAME="your_adp_username"
export ADP_PASSWORD="your_adp_password"
export ADP_BASE_URL="https://your-adp-server:8443"
```

**Note**: If environment variables are not set, the skill will automatically use the default credentials above.

### Step 2: Start OpenCode

Navigate to this project directory and start OpenCode:

```bash
cd /path/to/axcpy
opencode
```

### Step 3: Ask About Entity Status

OpenCode will automatically use the skill when you ask questions like:

#### Example 1: Check a specific server
```
You: What's the status of demo00001?
```

OpenCode will:
1. Recognize this as an entity status query
2. Load the `axcelerate-status` skill
3. Run: `uv run axcpy adp list-entities --id "singleMindServer.demo00001" --ignore-tls`
4. Parse the results and present them clearly

#### Example 2: List all servers
```
You: Show me all SingleMind servers
```

OpenCode will list all available servers with their statuses.

#### Example 3: Check if a server is running
```
You: Is singleMindServer.demo00001 running?
```

OpenCode will check the status and tell you if it's STARTED, STOPPED, etc.

## 🎯 What the Skill Does

When you ask about AXcelerate entity status, the skill will:

✅ **Automatically authenticate** using environment variables OR default credentials
✅ **Run the appropriate axcpy command** with the right parameters
✅ **Parse and format the results** in a user-friendly way
✅ **Explain the status** (STARTED, STOPPED, ERROR, etc.)
✅ **Provide troubleshooting tips** if there are issues

**Default Credentials**: If no environment variables are set, the skill uses:
- Username: `adpuser`
- Password: `adpus3r`
- Server: `https://vm-rhauswirth2.otxlab.net:8443`

## 📋 Common Questions You Can Ask

- "What's the status of [entity-id]?"
- "Check if demo00001 is running"
- "Show me all servers"
- "List all SingleMind servers with their status"
- "Is singleMindServer.demo00001 online?"
- "Get detailed information about demo00001"
- "What servers are currently stopped?"

## 🔍 How It Works Behind the Scenes

1. **Discovery**: OpenCode automatically discovers the skill from `.opencode/skills/axcelerate-status/`
2. **Trigger**: When you ask about entity status, OpenCode recognizes it matches the skill description
3. **Loading**: OpenCode loads the full skill instructions from `SKILL.md`
4. **Execution**: OpenCode follows the skill's instructions to run the appropriate `axcpy` command
5. **Response**: OpenCode presents the results in a clear, conversational format

## 🛠️ Testing the Skill

### Test 1: Verify the skill is loaded
In OpenCode, ask:
```
What skills do you have available?
```

You should see `axcelerate-status` listed.

### Test 2: Check credentials
In OpenCode, ask:
```
Are my ADP credentials set up?
```

The skill will check for the required environment variables.

### Test 3: Run a status check
In OpenCode, ask:
```
What's the status of demo00001?
```

(Replace `demo00001` with an actual entity ID from your environment)

## 📖 Skill Capabilities

The `axcelerate-status` skill knows how to:

| Capability | Example Command |
|------------|----------------|
| Check specific entity | `--id "singleMindServer.demo00001"` |
| List all entities | `--id ""` |
| Query different types | `--type "collection"` |
| Get specific fields | `--white-list "id,displayName,hostName"` |
| Debug mode | `--debug` |
| Handle TLS issues | `--ignore-tls` |

## 🔐 Security Notes

- Credentials are read from environment variables (not stored in the skill)
- The skill uses your existing `axcpy` CLI tool (no separate authentication)
- All commands run locally on your machine
- No data is sent to external services (except your ADP server)

## 🎨 Customization

To customize the skill behavior, edit:
```
.opencode/skills/axcelerate-status/SKILL.md
```

You can modify:
- Default parameters (entity types, whitelists)
- Response format preferences
- Error handling behavior
- Example interactions

## 📚 Additional Resources

- **OpenCode Skills Documentation**: https://opencode.ai/docs/skills
- **axcpy CLI Documentation**: See `README.md` in this repo
- **ADP API Reference**: See `docs/` directory

## 🆘 Troubleshooting

### Skill not recognized
- Make sure you're in the axcpy project directory
- Restart OpenCode to reload skills
- Check that `SKILL.md` is in the correct location

### Authentication errors
- Verify environment variables: `echo $ADP_USERNAME`
- Check base URL format: `https://hostname:port`
- Try adding `--ignore-tls` for development environments

### Command not found
- Ensure axcpy is installed: `uv run axcpy --help`
- Check that you're in the project directory
- Run `uv sync --all-extras` to install dependencies

## 🎉 Success!

You're all set! Start OpenCode and try asking about your AXcelerate entities. The skill will handle everything automatically.

**Example conversation to get started:**

```
You: Show me all SingleMind servers

OpenCode: I'll list all SingleMind servers for you using the axcelerate-status skill.
          [Executes command...]
          
          Here are all the servers:
          
          ID                          Display Name      Status
          ─────────────────────────── ───────────────── ────────
          singleMindServer.demo00001  Demo Server 1     STARTED
          singleMindServer.demo00002  Demo Server 2     STOPPED
          singleMindServer.demo00003  Demo Server 3     STARTED
```

Happy coding! 🚀
