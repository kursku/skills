# Composio SDK Reference

## Python SDK

### Installation
```bash
pip install composio composio-claude-agent-sdk
```

### Initialize Client
```python
from composio import Composio

# Explicit API key
composio = Composio(api_key="your_api_key")

# Or via environment variable COMPOSIO_API_KEY
composio = Composio()
```

### Sessions

Sessions are isolated user contexts that provide access to tools from connected apps.

```python
# Create session with specific toolkits
session = composio.create(
    user_id="user_123",
    toolkits=["github", "gmail", "slack"]
)

# Get native tool definitions (for passing to agent frameworks)
tools = session.tools()

# Get MCP endpoint URL (for MCP-compatible clients)
mcp_url = session.mcp.url
```

### Native Tools with Claude Agent SDK
```python
from composio import Composio
from composio_claude_agent_sdk import get_tools
import anthropic

composio = Composio()
session = composio.create(user_id="user_123", toolkits=["github"])
tools = session.tools()

client = anthropic.Anthropic()
# Pass tools to Claude as tool definitions
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "Create a GitHub issue titled 'Bug fix needed'"}]
)
```

### MCP Integration
```python
session = composio.create(user_id="user_123", toolkits=["github", "slack"])

# The MCP URL can be used with:
# - Claude Desktop (add to claude_desktop_config.json)
# - Cursor
# - Any MCP-compatible client
mcp_url = session.mcp.url

# MCP includes a Tool Router for dynamic tool discovery
# Agent discovers available tools at runtime — no upfront definition needed
```

### Execute a Specific Action
```python
# Execute an action directly (without agent)
result = composio.actions.execute(
    action="GITHUB_CREATE_ISSUE",
    params={
        "owner": "myorg",
        "repo": "myrepo",
        "title": "New issue",
        "body": "Issue description"
    },
    user_id="user_123"
)
```

### List Available Tools
```python
# List all tools in a toolkit
tools = composio.tools.list(toolkit="github")
for tool in tools:
    print(f"{tool.name}: {tool.description}")

# Search for specific tools
tools = composio.tools.search("create issue")
```

### Connected Accounts Management
```python
# List connected accounts for a user
accounts = composio.connected_accounts.list(
    user_ids=["user_123"],
    statuses=["ACTIVE"]
)

# Get a specific connected account
account = composio.connected_accounts.get(connected_account_id="ca_xxx")

# Delete a connected account
composio.connected_accounts.delete(connected_account_id="ca_xxx")
```

---

## TypeScript SDK

### Installation
```bash
npm install composio @composio/claude-agent-sdk
```

### Initialize Client
```typescript
import { Composio } from "composio";

const composio = new Composio({ apiKey: "your_api_key" });
// Or set COMPOSIO_API_KEY env var
const composio = new Composio();
```

### Sessions and Tools
```typescript
// Create session
const session = await composio.create({
  userId: "user_123",
  toolkits: ["github", "gmail", "slack"]
});

// Get native tool definitions
const tools = await session.tools();

// Get MCP URL
const mcpUrl = session.mcp.url;
```

### Execute Actions
```typescript
const result = await composio.actions.execute({
  action: "GITHUB_CREATE_ISSUE",
  params: {
    owner: "myorg",
    repo: "myrepo",
    title: "New issue",
    body: "Description"
  },
  userId: "user_123"
});
```

### With Claude Agent SDK
```typescript
import { Composio } from "composio";
import Anthropic from "@anthropic-ai/sdk";

const composio = new Composio();
const session = await composio.create({
  userId: "user_123",
  toolkits: ["github"]
});
const tools = await session.tools();

const client = new Anthropic();
const response = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 1024,
  tools,
  messages: [{ role: "user", content: "List my GitHub repos" }]
});
```

---

## Common Tool Names by Toolkit

### GitHub
- `GITHUB_CREATE_ISSUE` — Create a new issue
- `GITHUB_GET_ISSUE` — Get issue details
- `GITHUB_CREATE_PULL_REQUEST` — Create a PR
- `GITHUB_MERGE_PULL_REQUEST` — Merge a PR
- `GITHUB_LIST_REPOS` — List repositories
- `GITHUB_STAR_REPO` — Star a repository
- `GITHUB_CREATE_COMMENT` — Comment on issue/PR

### Gmail
- `GMAIL_SEND_EMAIL` — Send an email
- `GMAIL_LIST_EMAILS` — List emails
- `GMAIL_GET_EMAIL` — Read email details
- `GMAIL_CREATE_DRAFT` — Create email draft
- `GMAIL_REPLY_TO_EMAIL` — Reply to an email

### Slack
- `SLACK_POST_MESSAGE` — Post a message to a channel
- `SLACK_LIST_CHANNELS` — List channels
- `SLACK_GET_CHANNEL_HISTORY` — Read channel messages
- `SLACK_SEND_DIRECT_MESSAGE` — Send a DM
- `SLACK_ADD_REACTION` — Add emoji reaction

### Notion
- `NOTION_CREATE_PAGE` — Create a page
- `NOTION_UPDATE_PAGE` — Update a page
- `NOTION_QUERY_DATABASE` — Query a database
- `NOTION_CREATE_DATABASE` — Create a database

### Linear
- `LINEAR_CREATE_ISSUE` — Create an issue
- `LINEAR_UPDATE_ISSUE` — Update an issue
- `LINEAR_LIST_ISSUES` — List issues
- `LINEAR_CREATE_COMMENT` — Comment on issue

### Google Calendar
- `GOOGLE_CALENDAR_CREATE_EVENT` — Create calendar event
- `GOOGLE_CALENDAR_LIST_EVENTS` — List events
- `GOOGLE_CALENDAR_UPDATE_EVENT` — Update event
- `GOOGLE_CALENDAR_DELETE_EVENT` — Delete event

---

## Error Handling

```python
from composio.exceptions import ComposioError

try:
    result = composio.actions.execute(
        action="GITHUB_CREATE_ISSUE",
        params={"owner": "org", "repo": "repo", "title": "Test"},
        user_id="user_123"
    )
except ComposioError as e:
    print(f"Composio error: {e.message}")
    # Common errors:
    # - No active connected account for the toolkit
    # - Invalid action name
    # - Missing required parameters
    # - Rate limiting from the target app
```

## Best Practices

1. **Reuse sessions** — Don't create a new session for every request; reuse within a user's interaction
2. **Prefer MCP mode** — Reduces token usage by not sending all tool schemas upfront
3. **Scope toolkits narrowly** — Only include toolkits the agent actually needs
4. **Handle tool errors gracefully** — Third-party APIs can fail; always check results
5. **Use user_id consistently** — Same user_id across sessions maintains connected account access
