# Default Credentials Added to AXcelerate Status Skill

## Summary

I've successfully added default credentials to the OpenCode `axcelerate-status` skill. The skill will now automatically use these defaults when environment variables are not set.

## Default Credentials

- **Username**: `adpuser`
- **Password**: `adpus3r`
- **Base URL**: `https://vm-rhauswirth2.otxlab.net:8443`

## How It Works

### Priority Order
1. **First**: Check for environment variables (`ADP_USERNAME`, `ADP_PASSWORD`, `ADP_BASE_URL`)
2. **Fallback**: If not set, use the default credentials above

### Command Construction

**When environment variables are NOT set:**
```bash
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  -u adpuser \
  -p adpus3r \
  -b https://vm-rhauswirth2.otxlab.net:8443 \
  --ignore-tls
```

**When environment variables ARE set:**
```bash
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  --ignore-tls
```

## Files Updated

### 1. `.opencode/skills/axcelerate-status/SKILL.md`
- Added default credentials to "Required Authentication" section
- Updated all example commands to show both environment variable and explicit credential usage
- Modified "Important Notes" to explain when to use defaults
- Updated "Response Format" to automatically use defaults instead of asking user
- Changed example interactions to use explicit credentials

### 2. `.opencode/skills/axcelerate-status/QUICKSTART.md`
- Changed "Step 1" from required to optional
- Added note that default credentials are pre-configured
- Added section showing the default credentials
- Updated skill capabilities section to mention automatic fallback

### 3. `.opencode/skills/axcelerate-status/README.md`
- Updated "Prerequisites" section to show defaults first
- Made environment variables optional (for overrides)
- Added information about default environment

### 4. `README.md` (Project root)
- Updated "OpenCode Integration" section
- Added default credentials display
- Made environment variable setup optional
- Reordered quick setup to show defaults first

## Usage Examples

### No Setup Required (Uses Defaults)
```bash
cd /path/to/axcpy
opencode
```

Then ask:
```
What's the status of demo00001?
```

OpenCode will automatically use the default credentials!

### Override with Custom Credentials
```bash
export ADP_USERNAME="myuser"
export ADP_PASSWORD="mypass"
export ADP_BASE_URL="https://my-server:8443"
opencode
```

Then ask the same question - it will use your custom credentials instead.

## Benefits

✅ **Zero Configuration**: Works out of the box with no setup required
✅ **Flexible**: Can still override with environment variables when needed
✅ **Convenient**: Perfect for the development environment
✅ **Smart**: OpenCode automatically detects and uses the right credentials

## Security Notes

⚠️ **Important**: The default credentials are suitable for:
- Development environments
- Testing purposes
- Internal lab environments (vm-rhauswirth2.otxlab.net)

For production environments or sensitive data:
- Always use environment variables
- Use strong, unique passwords
- Consider using a secrets management system
- Don't commit real credentials to git

## Testing

To test the skill with defaults:

1. **Ensure environment variables are NOT set:**
   ```bash
   unset ADP_USERNAME
   unset ADP_PASSWORD
   unset ADP_BASE_URL
   ```

2. **Start OpenCode:**
   ```bash
   cd /path/to/axcpy
   opencode
   ```

3. **Ask about entity status:**
   ```
   Show me all SingleMind servers
   ```

4. **OpenCode will run:**
   ```bash
   uv run axcpy adp list-entities \
     --id "" \
     -u adpuser \
     -p adpus3r \
     -b https://vm-rhauswirth2.otxlab.net:8443 \
     --ignore-tls
   ```

## What OpenCode Sees

When the skill is loaded, OpenCode will understand:
- Default credentials are available
- When environment variables are missing, use defaults
- Always use `--ignore-tls` for vm-rhauswirth2.otxlab.net
- Don't ask the user for credentials - just use the defaults

## Complete Skill Behavior

```
User: "What's the status of demo00001?"

OpenCode (internal):
  1. Load axcelerate-status skill
  2. Check for ADP_USERNAME environment variable
  3. Not found → Use default: adpuser
  4. Check for ADP_PASSWORD environment variable
  5. Not found → Use default: adpus3r
  6. Check for ADP_BASE_URL environment variable
  7. Not found → Use default: https://vm-rhauswirth2.otxlab.net:8443
  8. Construct command with explicit credentials
  9. Run: uv run axcpy adp list-entities --id "singleMindServer.demo00001" 
          -u adpuser -p adpus3r -b https://vm-rhauswirth2.otxlab.net:8443 
          --ignore-tls

OpenCode (to user):
  "I'll check the status of SingleMind server demo00001 for you.
   The server is currently STARTED and running normally."
```

## Next Steps

The skill is now fully configured with default credentials and ready to use! Simply start OpenCode in the axcpy directory and ask about entity status - no setup required!

---

**Created**: January 22, 2026
**Default Server**: vm-rhauswirth2.otxlab.net:8443
**Default User**: adpuser
