# AXcelerate Status Skill - Quick Reference

## Default Credentials (Pre-configured)

```
Username: adpuser
Password: adpus3r
Base URL: https://vm-rhauswirth2.otxlab.net:8443
```

## Quick Start (Zero Setup!)

```bash
cd /path/to/axcpy
opencode
```

Ask: `"What's the status of demo00001?"`

That's it! No configuration needed.

## Override Defaults (Optional)

```bash
export ADP_USERNAME="custom_user"
export ADP_PASSWORD="custom_pass"
export ADP_BASE_URL="https://custom-server:8443"
```

## Example Questions

| Ask This | OpenCode Does This |
|----------|-------------------|
| "What's the status of demo00001?" | Checks specific server status |
| "Show me all SingleMind servers" | Lists all servers with status |
| "Is demo00001 running?" | Reports if server is STARTED/STOPPED |
| "Get detailed info for all servers" | Shows ID, name, status, hostname |
| "What servers are stopped?" | Filters and shows stopped servers |

## Status Values

- `STARTED` - Running normally ✅
- `STOPPED` - Not running 🛑
- `STARTING` - Starting up ⏳
- `STOPPING` - Shutting down ⏳
- `ERROR` - Has errors ❌

## Files

```
.opencode/skills/axcelerate-status/
├── SKILL.md                    # Main skill definition (OpenCode reads this)
├── README.md                   # Full documentation
├── QUICKSTART.md              # Getting started guide
├── DEFAULT_CREDENTIALS.md     # Credential configuration details
└── QUICK_REFERENCE.md         # This file
```

## Commands OpenCode Runs

**With defaults:**
```bash
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  -u adpuser \
  -p adpus3r \
  -b https://vm-rhauswirth2.otxlab.net:8443 \
  --ignore-tls
```

**With environment variables:**
```bash
uv run axcpy adp list-entities \
  --id "singleMindServer.demo00001" \
  --ignore-tls
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not found | Restart OpenCode in axcpy directory |
| Connection timeout | Check network/VPN to vm-rhauswirth2.otxlab.net |
| Authentication failed | Verify credentials are correct |
| TLS errors | Skill automatically uses `--ignore-tls` |
| Command not found | Run `uv sync --all-extras` |

## Pro Tips

💡 **No setup required** - Defaults are pre-configured for the lab environment

💡 **Smart fallback** - Uses env vars if set, otherwise uses defaults

💡 **Always current** - OpenCode loads the latest SKILL.md each time

💡 **Natural language** - Ask questions naturally, OpenCode understands

💡 **Debug mode** - Say "with debug info" to see detailed output

## More Info

- **Full docs**: [README.md](README.md)
- **Setup guide**: [QUICKSTART.md](QUICKSTART.md)
- **Credential details**: [DEFAULT_CREDENTIALS.md](DEFAULT_CREDENTIALS.md)
- **OpenCode skills**: https://opencode.ai/docs/skills

---
**Last Updated**: January 22, 2026
