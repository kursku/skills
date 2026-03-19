# n8n REST API Reference

## Authentication

All API requests require an API key passed as a header:

```
X-N8N-API-KEY: your-api-key
```

Generate API keys in n8n: Settings → API → Create API Key

Base URL: `http://localhost:5678/api/v1` (self-hosted) or your cloud instance URL.

## Workflows

### List Workflows
```bash
GET /api/v1/workflows
# Query params: cursor, limit (max 250), tags, name, active
```

### Get Workflow
```bash
GET /api/v1/workflows/{id}
```

### Create Workflow
```bash
POST /api/v1/workflows
Content-Type: application/json

{
  "name": "My Workflow",
  "nodes": [...],
  "connections": {...},
  "settings": { "executionOrder": "v1" }
}
```

### Update Workflow
```bash
PUT /api/v1/workflows/{id}
Content-Type: application/json

{
  "name": "Updated Workflow",
  "nodes": [...],
  "connections": {...},
  "settings": { "executionOrder": "v1" }
}
```

### Delete Workflow
```bash
DELETE /api/v1/workflows/{id}
```

### Activate/Deactivate Workflow
```bash
PATCH /api/v1/workflows/{id}/activate
PATCH /api/v1/workflows/{id}/deactivate
```

### Transfer Workflow (Enterprise)
```bash
PUT /api/v1/workflows/{id}/transfer
Content-Type: application/json

{ "destinationProjectId": "project-id" }
```

## Executions

### List Executions
```bash
GET /api/v1/executions
# Query params: cursor, limit, status (error|success|waiting), workflowId, includeData
```

### Get Execution
```bash
GET /api/v1/executions/{id}
# Query params: includeData (boolean)
```

### Delete Execution
```bash
DELETE /api/v1/executions/{id}
```

## Credentials

### List Credentials
```bash
GET /api/v1/credentials
# Query params: cursor, limit
```

### Create Credential
```bash
POST /api/v1/credentials
Content-Type: application/json

{
  "name": "My API Key",
  "type": "httpHeaderAuth",
  "data": {
    "name": "Authorization",
    "value": "Bearer sk-..."
  }
}
```

### Delete Credential
```bash
DELETE /api/v1/credentials/{id}
```

## Tags

### List Tags
```bash
GET /api/v1/tags
# Query params: cursor, limit
```

### Create Tag
```bash
POST /api/v1/tags
Content-Type: application/json

{ "name": "production" }
```

### Update Tag
```bash
PATCH /api/v1/tags/{id}
Content-Type: application/json

{ "name": "staging" }
```

### Delete Tag
```bash
DELETE /api/v1/tags/{id}
```

## Users (Admin)

### List Users
```bash
GET /api/v1/users
# Query params: cursor, limit, includeRole
```

### Get User
```bash
GET /api/v1/users/{id}
```

## Variables

### List Variables
```bash
GET /api/v1/variables
# Query params: cursor, limit
```

### Create Variable
```bash
POST /api/v1/variables
Content-Type: application/json

{ "key": "API_BASE_URL", "value": "https://api.example.com" }
```

### Update Variable
```bash
PUT /api/v1/variables/{id}
Content-Type: application/json

{ "key": "API_BASE_URL", "value": "https://api-v2.example.com" }
```

### Delete Variable
```bash
DELETE /api/v1/variables/{id}
```

## Source Control (Enterprise)

### Pull from Remote
```bash
POST /api/v1/source-control/pull
Content-Type: application/json

{ "force": false }
```

### Push to Remote
```bash
POST /api/v1/source-control/push
Content-Type: application/json

{ "commitMessage": "Update workflows", "force": false }
```

## Audit Logs (Enterprise)

### List Audit Events
```bash
GET /api/v1/audit
# Query params: cursor, limit
```

## Webhook URLs

When a workflow has a Webhook trigger, n8n exposes:
- **Production**: `{baseUrl}/webhook/{path}` (when workflow is active)
- **Test**: `{baseUrl}/webhook-test/{path}` (during manual testing)

## Programmatic Workflow Management

### JavaScript/TypeScript Client Example
```typescript
class N8nClient {
  constructor(
    private baseUrl: string,
    private apiKey: string,
  ) {}

  private async request(method: string, path: string, body?: unknown) {
    const response = await fetch(`${this.baseUrl}/api/v1${path}`, {
      method,
      headers: {
        'X-N8N-API-KEY': this.apiKey,
        'Content-Type': 'application/json',
      },
      body: body ? JSON.stringify(body) : undefined,
    });

    if (!response.ok) {
      throw new Error(`n8n API error: ${response.status} ${await response.text()}`);
    }

    return response.json();
  }

  // Workflows
  async listWorkflows(params?: { active?: boolean; tags?: string }) {
    const query = new URLSearchParams(params as Record<string, string>).toString();
    return this.request('GET', `/workflows${query ? `?${query}` : ''}`);
  }

  async getWorkflow(id: string) {
    return this.request('GET', `/workflows/${id}`);
  }

  async createWorkflow(workflow: { name: string; nodes: unknown[]; connections: unknown }) {
    return this.request('POST', '/workflows', workflow);
  }

  async updateWorkflow(id: string, workflow: unknown) {
    return this.request('PUT', `/workflows/${id}`, workflow);
  }

  async activateWorkflow(id: string) {
    return this.request('PATCH', `/workflows/${id}/activate`);
  }

  async deactivateWorkflow(id: string) {
    return this.request('PATCH', `/workflows/${id}/deactivate`);
  }

  async deleteWorkflow(id: string) {
    return this.request('DELETE', `/workflows/${id}`);
  }

  // Executions
  async listExecutions(params?: { workflowId?: string; status?: string; limit?: number }) {
    const query = new URLSearchParams(params as Record<string, string>).toString();
    return this.request('GET', `/executions${query ? `?${query}` : ''}`);
  }

  async getExecution(id: string, includeData = true) {
    return this.request('GET', `/executions/${id}?includeData=${includeData}`);
  }

  // Credentials
  async createCredential(credential: { name: string; type: string; data: unknown }) {
    return this.request('POST', '/credentials', credential);
  }

  // Variables
  async setVariable(key: string, value: string) {
    return this.request('POST', '/variables', { key, value });
  }
}

// Usage
const n8n = new N8nClient('http://localhost:5678', 'your-api-key');
const workflows = await n8n.listWorkflows();
```

## Rate Limits & Best Practices

1. **No official rate limits** on self-hosted — but be reasonable with API calls
2. **Cloud instances** may have rate limits — check your plan
3. **Use pagination** — always paginate list endpoints for large datasets
4. **Include `executionOrder: "v1"`** in workflow settings for predictable behavior
5. **Test webhooks** with the test URL before activating workflows
6. **Use tags** to organize workflows (production, staging, team-specific)
7. **Back up workflows** — export via API before major changes
8. **Use variables** for environment-specific configuration instead of hardcoding
