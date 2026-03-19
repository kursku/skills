---
name: composio
description: Build AI agent integrations with Composio (composio.dev). Use when the user wants to connect AI agents to third-party apps (GitHub, Gmail, Slack, Notion, Salesforce, etc.), set up OAuth authentication for tools, create Composio sessions, use Composio tools natively or via MCP, set up event triggers, or build multi-app agent workflows. Triggers on imports from composio or @composio or mentions of composio.
argument-hint: [description of what to build or integrate]
---

# Composio Skill

You are an expert at integrating AI agents with third-party applications using Composio — the developer-first platform that connects agents to 1000+ apps via unified SDKs and MCP.

Read the detailed reference files in `${CLAUDE_SKILL_DIR}` for comprehensive patterns:

- `sdk-reference.md` — Python and TypeScript SDK patterns, sessions, tools, MCP integration, executing actions
- `auth-and-triggers.md` — OAuth/API key authentication flows, connected accounts, triggers, webhooks, polling

## Setup Checklist

### Python
```bash
pip install composio composio-claude-agent-sdk
```

### TypeScript
```bash
npm install composio @composio/claude-agent-sdk
```

### Environment Variables
```bash
COMPOSIO_API_KEY=your_composio_api_key    # from composio.dev dashboard
ANTHROPIC_API_KEY=your_anthropic_api_key  # for Claude integration
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Toolkits** | Bundles of tools by service (github, gmail, slack, notion, etc.) |
| **Tools** | Discrete operations: `GITHUB_CREATE_ISSUE`, `GMAIL_SEND_EMAIL`, `SLACK_POST_MESSAGE` |
| **Auth Configs** | Reusable auth blueprints (OAuth2, API Key, Bearer Token) per toolkit |
| **Connected Accounts** | User-to-toolkit links created after OAuth consent or API key setup |
| **Triggers** | Event listeners: `GITHUB_COMMIT_EVENT`, `SLACK_NEW_MESSAGE`, `GMAIL_NEW_EMAIL` |
| **Sessions** | Isolated user contexts with access to tools (native or MCP) |
| **User ID** | Primary identifier scoping all operations to a specific user |

## Core Patterns

### Initialize Client

**Python:**
```python
from composio import Composio

composio = Composio(api_key="your_api_key")
# Or set COMPOSIO_API_KEY env var and omit api_key
```

**TypeScript:**
```typescript
import { Composio } from "composio";

const composio = new Composio({ apiKey: "your_api_key" });
```

### Create Session and Get Tools (Native)
```python
session = composio.create(user_id="user_123", toolkits=["github", "gmail"])
tools = session.tools()
# Pass tools to your Claude agent
```

### Create Session and Get MCP URL
```python
session = composio.create(user_id="user_123", toolkits=["github", "slack"])
mcp_url = session.mcp.url
# Use mcp_url in MCP-compatible clients (Claude Desktop, Cursor, etc.)
```

### Authenticate a User (OAuth2)
```python
connection_request = composio.connected_accounts.initiate(
    user_id="user_123",
    auth_config_id="your_auth_config_id",
    config={"auth_scheme": "OAUTH2"},
    callback_url="https://yourapp.com/callback"
)
# Redirect user to: connection_request.redirect_url
# After consent, wait for connection:
connected_account = connection_request.wait_for_connection()
```

### Set Up a Trigger
```python
trigger = composio.triggers.create(
    slug="GITHUB_COMMIT_EVENT",
    user_id="user_123",
    trigger_config={"owner": "repo-owner", "repo": "repo-name"},
)
```

## Critical Rules

1. **Always scope operations by user_id** — every session, connected account, and trigger belongs to a user
2. **Only ACTIVE connected accounts can execute tools** — check status before using
3. **Use MCP mode for dynamic tool discovery** — reduces token usage vs passing all tool definitions upfront
4. **Auth configs are reusable** — create one per toolkit per environment, reuse across users
5. **Composio auto-refreshes OAuth tokens** — no manual token refresh needed
6. **Webhook triggers are real-time** — polling triggers check every ~1 minute
7. **Never hardcode API keys** — use environment variables (`COMPOSIO_API_KEY`)
8. **Use type-safe tool names** — e.g., `GITHUB_CREATE_ISSUE` not arbitrary strings
9. **Check connected account status** before executing tools: ACTIVE, INITIATED, EXPIRED, FAILED, INACTIVE
10. **Max toolkits per session vary by plan** — check Composio dashboard for limits

## Common Workflows

### Email Triage Agent
```python
session = composio.create(user_id="user_1", toolkits=["gmail", "slack", "notion"])
tools = session.tools()
# Agent reads Gmail, classifies emails, routes to Slack channels, logs in Notion
```

### GitHub PR Monitor
```python
trigger = composio.triggers.create(
    slug="GITHUB_PULL_REQUEST_EVENT",
    user_id="user_1",
    trigger_config={"owner": "myorg", "repo": "myrepo"},
)
# On PR event -> agent reviews code, posts summary to Slack
```

### Multi-App Workflow
```python
session = composio.create(
    user_id="user_1",
    toolkits=["github", "slack", "linear", "notion"]
)
tools = session.tools()
# Agent receives Slack message -> creates Linear issue -> updates Notion -> confirms in Slack
```

Use `$ARGUMENTS` to understand what the user wants to integrate. Read the reference files for detailed SDK patterns and authentication flows before writing code.
