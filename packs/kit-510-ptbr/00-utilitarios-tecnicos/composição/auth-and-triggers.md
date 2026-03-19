# Composio Authentication & Triggers Reference

## Authentication

Composio supports multiple auth methods per toolkit. Auth configs define how authentication works; connected accounts are the result of a user completing auth.

### Auth Methods

| Method | Description | Example Apps |
|--------|-------------|-------------|
| **OAuth2** | Full OAuth consent flow with redirect | GitHub, Gmail, Slack, Notion, Google Calendar |
| **API Key** | User provides an API key | OpenAI, Anthropic, Sendgrid |
| **Bearer Token** | User provides a bearer token | Various REST APIs |
| **Basic Auth** | Username + password | Legacy systems |

### Creating an Auth Config

Auth configs are reusable blueprints — create one per toolkit per environment.

**Via Dashboard:**
1. Go to composio.dev dashboard
2. Navigate to Auth Configs
3. Select toolkit (e.g., GitHub)
4. Enter OAuth client ID, client secret, scopes
5. Save — get an `auth_config_id`

**Via SDK:**
```python
auth_config = composio.auth_configs.create(
    toolkit="github",
    auth_scheme="OAUTH2",
    config={
        "client_id": "your_oauth_client_id",
        "client_secret": "your_oauth_client_secret",
        "scopes": ["repo", "user", "read:org"]
    }
)
# auth_config.id — use this when initiating connections
```

### Initiating User Authentication (OAuth2)

```python
# Start OAuth flow for a user
connection_request = composio.connected_accounts.initiate(
    user_id="user_123",
    auth_config_id="ac_xxx",  # from auth config creation
    config={"auth_scheme": "OAUTH2"},
    callback_url="https://yourapp.com/auth/callback"
)

# Redirect user to the OAuth consent page
print(connection_request.redirect_url)  # Send user here

# Wait for the user to complete OAuth (blocking)
connected_account = connection_request.wait_for_connection()
# connected_account.id, connected_account.status
```

### Initiating User Authentication (API Key)

```python
connection_request = composio.connected_accounts.initiate(
    user_id="user_123",
    auth_config_id="ac_xxx",
    config={
        "auth_scheme": "API_KEY",
        "api_key": "user_provided_api_key"
    }
)
# No redirect needed — connection is immediately active
```

### Connected Account Statuses

| Status | Meaning |
|--------|---------|
| `ACTIVE` | Ready to use, tokens valid |
| `INITIATED` | OAuth flow started, user hasn't completed consent |
| `EXPIRED` | Token expired (Composio auto-refreshes, so this is rare) |
| `FAILED` | Authentication failed |
| `INACTIVE` | Manually deactivated |

### Managing Connected Accounts

```python
# List all active accounts for a user
accounts = composio.connected_accounts.list(
    user_ids=["user_123"],
    statuses=["ACTIVE"]
)

# Check if a user has an active connection for a toolkit
github_accounts = [a for a in accounts if a.toolkit == "github"]
has_github = len(github_accounts) > 0

# Get specific account
account = composio.connected_accounts.get(connected_account_id="ca_xxx")

# Delete (disconnect)
composio.connected_accounts.delete(connected_account_id="ca_xxx")
```

### Token Auto-Refresh

Composio automatically refreshes OAuth tokens before they expire. You never need to manually refresh tokens. If a token refresh fails, the connected account status changes to `EXPIRED`.

---

## Triggers

Triggers are event listeners that push data to your application when something happens in a connected app.

### Trigger Types

| Type | Delivery | Latency | Apps |
|------|----------|---------|------|
| **Webhook** | Real-time push | Instant | GitHub, Slack, Linear |
| **Polling** | Composio checks periodically | ~1 minute | Gmail, Google Calendar |

### Common Trigger Slugs

**GitHub:**
- `GITHUB_COMMIT_EVENT` — New commit pushed
- `GITHUB_PULL_REQUEST_EVENT` — PR opened/closed/merged
- `GITHUB_ISSUE_EVENT` — Issue created/updated
- `GITHUB_PUSH_EVENT` — Code pushed to branch
- `GITHUB_STAR_EVENT` — Repository starred

**Slack:**
- `SLACK_NEW_MESSAGE` — New message in channel
- `SLACK_REACTION_ADDED` — Reaction added to message
- `SLACK_CHANNEL_CREATED` — New channel created

**Gmail:**
- `GMAIL_NEW_EMAIL` — New email received (polling)
- `GMAIL_NEW_LABEL` — Email labeled

**Linear:**
- `LINEAR_ISSUE_CREATED` — New issue
- `LINEAR_ISSUE_UPDATED` — Issue updated
- `LINEAR_COMMENT_CREATED` — New comment

### Creating Triggers

```python
# Webhook trigger (GitHub)
trigger = composio.triggers.create(
    slug="GITHUB_PULL_REQUEST_EVENT",
    user_id="user_123",
    trigger_config={
        "owner": "myorg",
        "repo": "myrepo"
    }
)
# trigger.id — trigger identifier
# trigger.webhook_url — URL that receives events (for webhook triggers)

# Polling trigger (Gmail)
trigger = composio.triggers.create(
    slug="GMAIL_NEW_EMAIL",
    user_id="user_123",
    trigger_config={
        "label": "INBOX",
        "interval": 60  # check every 60 seconds
    }
)
```

### Listening for Trigger Events

```python
# Subscribe to trigger events
listener = composio.triggers.subscribe(
    trigger_ids=["trigger_xxx"]
)

# Process events
for event in listener:
    print(f"Event: {event.trigger_slug}")
    print(f"Data: {event.data}")
    # Route to appropriate handler
```

### Managing Triggers

```python
# List triggers for a user
triggers = composio.triggers.list(user_id="user_123")

# Get trigger details
trigger = composio.triggers.get(trigger_id="trigger_xxx")

# Delete a trigger
composio.triggers.delete(trigger_id="trigger_xxx")

# Pause/resume
composio.triggers.pause(trigger_id="trigger_xxx")
composio.triggers.resume(trigger_id="trigger_xxx")
```

---

## Complete Auth + Trigger Flow Example

A full example: authenticate GitHub, set up a PR trigger, and handle events.

```python
from composio import Composio

composio = Composio()

# 1. Initiate GitHub OAuth for user
connection = composio.connected_accounts.initiate(
    user_id="user_123",
    auth_config_id="ac_github_xxx",
    config={"auth_scheme": "OAUTH2"},
    callback_url="https://myapp.com/callback"
)
print(f"Auth URL: {connection.redirect_url}")

# 2. Wait for user to complete OAuth
account = connection.wait_for_connection()
assert account.status == "ACTIVE"

# 3. Set up PR event trigger
trigger = composio.triggers.create(
    slug="GITHUB_PULL_REQUEST_EVENT",
    user_id="user_123",
    trigger_config={"owner": "myorg", "repo": "myrepo"}
)

# 4. Create session with GitHub tools
session = composio.create(user_id="user_123", toolkits=["github", "slack"])
tools = session.tools()

# 5. Listen for events and process with agent
listener = composio.triggers.subscribe(trigger_ids=[trigger.id])
for event in listener:
    # Pass event data + tools to your Claude agent for processing
    # Agent can use GitHub tools to review PR, Slack tools to notify team
    pass
```

## Security Best Practices

1. **Never log or expose OAuth tokens** — Composio manages tokens internally
2. **Use callback URLs with HTTPS** — Never use HTTP for OAuth callbacks
3. **Validate trigger event signatures** — Verify webhook payloads are from Composio
4. **Scope OAuth permissions narrowly** — Only request the scopes your agent needs
5. **Rotate API keys periodically** — Refresh your `COMPOSIO_API_KEY` on a schedule
6. **Use separate auth configs per environment** — Don't share between dev/staging/prod
