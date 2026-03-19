# n8n Custom Nodes Reference

## Overview

Custom nodes extend n8n with new integrations. Two approaches:
- **Declarative** — for simple HTTP-based APIs (no code logic)
- **Programmatic** — for complex logic, non-HTTP protocols, or custom processing

## Project Setup

### Scaffold a New Node Package
```bash
npx n8n-node-dev new
# or clone the starter:
git clone https://github.com/n8n-io/n8n-nodes-starter.git
cd n8n-nodes-starter
npm install
```

### Directory Structure
```
n8n-nodes-<name>/
├── package.json
├── tsconfig.json
├── nodes/
│   └── MyNode/
│       ├── MyNode.node.ts          # Node implementation
│       ├── MyNode.node.json        # Codex metadata
│       └── mynode.svg              # Node icon
├── credentials/
│   └── MyApi.credentials.ts        # Credential definition
└── dist/                           # Compiled output
```

### package.json Requirements
```json
{
  "name": "n8n-nodes-myservice",
  "version": "1.0.0",
  "n8n": {
    "n8nNodesApiVersion": 1,
    "nodes": ["dist/nodes/MyNode/MyNode.node.js"],
    "credentials": ["dist/credentials/MyApi.credentials.js"]
  },
  "files": ["dist"],
  "scripts": {
    "build": "tsc && gulp build:icons",
    "dev": "tsc --watch",
    "lint": "tslint -p tsconfig.json -c tslint.json",
    "lintfix": "tslint --fix -p tsconfig.json -c tslint.json"
  },
  "devDependencies": {
    "n8n-workflow": "latest",
    "typescript": "~5.x"
  }
}
```

## Programmatic Node

### Basic Structure
```typescript
import {
  IExecuteFunctions,
  INodeExecutionData,
  INodeType,
  INodeTypeDescription,
  NodeConnectionType,
} from 'n8n-workflow';

export class MyNode implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'My Node',
    name: 'myNode',
    icon: 'file:mynode.svg',
    group: ['transform'],
    version: 1,
    subtitle: '={{$parameter["operation"]}}',
    description: 'Description of what this node does',
    defaults: { name: 'My Node' },
    inputs: [NodeConnectionType.Main],
    outputs: [NodeConnectionType.Main],
    credentials: [
      {
        name: 'myApi',
        required: true,
      },
    ],
    properties: [
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        noDataExpression: true,
        options: [
          { name: 'Create', value: 'create', description: 'Create a record' },
          { name: 'Get', value: 'get', description: 'Get a record' },
          { name: 'Get Many', value: 'getMany', description: 'Get many records' },
          { name: 'Update', value: 'update', description: 'Update a record' },
          { name: 'Delete', value: 'delete', description: 'Delete a record' },
        ],
        default: 'create',
      },
      {
        displayName: 'Name',
        name: 'name',
        type: 'string',
        default: '',
        required: true,
        displayOptions: {
          show: { operation: ['create', 'update'] },
        },
        description: 'The name of the record',
      },
      {
        displayName: 'ID',
        name: 'id',
        type: 'string',
        default: '',
        required: true,
        displayOptions: {
          show: { operation: ['get', 'update', 'delete'] },
        },
      },
      {
        displayName: 'Additional Fields',
        name: 'additionalFields',
        type: 'collection',
        placeholder: 'Add Field',
        default: {},
        displayOptions: {
          show: { operation: ['create', 'update'] },
        },
        options: [
          { displayName: 'Description', name: 'description', type: 'string', default: '' },
          { displayName: 'Tags', name: 'tags', type: 'string', default: '' },
        ],
      },
      {
        displayName: 'Limit',
        name: 'limit',
        type: 'number',
        default: 50,
        typeOptions: { minValue: 1, maxValue: 100 },
        displayOptions: {
          show: { operation: ['getMany'] },
        },
      },
    ],
  };

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    const items = this.getInputData();
    const returnData: INodeExecutionData[] = [];
    const operation = this.getNodeParameter('operation', 0) as string;
    const credentials = await this.getCredentials('myApi');

    for (let i = 0; i < items.length; i++) {
      try {
        if (operation === 'create') {
          const name = this.getNodeParameter('name', i) as string;
          const additionalFields = this.getNodeParameter('additionalFields', i) as Record<string, unknown>;

          const body: Record<string, unknown> = { name, ...additionalFields };

          const response = await this.helpers.httpRequestWithAuthentication.call(
            this,
            'myApi',
            {
              method: 'POST',
              url: `${credentials.baseUrl}/api/records`,
              body,
              json: true,
            },
          );

          returnData.push({ json: response });
        } else if (operation === 'get') {
          const id = this.getNodeParameter('id', i) as string;

          const response = await this.helpers.httpRequestWithAuthentication.call(
            this,
            'myApi',
            {
              method: 'GET',
              url: `${credentials.baseUrl}/api/records/${id}`,
              json: true,
            },
          );

          returnData.push({ json: response });
        } else if (operation === 'getMany') {
          const limit = this.getNodeParameter('limit', i) as number;

          const response = await this.helpers.httpRequestWithAuthentication.call(
            this,
            'myApi',
            {
              method: 'GET',
              url: `${credentials.baseUrl}/api/records`,
              qs: { limit },
              json: true,
            },
          );

          const records = Array.isArray(response) ? response : response.data || [];
          for (const record of records) {
            returnData.push({ json: record });
          }
        } else if (operation === 'update') {
          const id = this.getNodeParameter('id', i) as string;
          const name = this.getNodeParameter('name', i) as string;
          const additionalFields = this.getNodeParameter('additionalFields', i) as Record<string, unknown>;

          const body: Record<string, unknown> = { name, ...additionalFields };

          const response = await this.helpers.httpRequestWithAuthentication.call(
            this,
            'myApi',
            {
              method: 'PUT',
              url: `${credentials.baseUrl}/api/records/${id}`,
              body,
              json: true,
            },
          );

          returnData.push({ json: response });
        } else if (operation === 'delete') {
          const id = this.getNodeParameter('id', i) as string;

          await this.helpers.httpRequestWithAuthentication.call(
            this,
            'myApi',
            {
              method: 'DELETE',
              url: `${credentials.baseUrl}/api/records/${id}`,
              json: true,
            },
          );

          returnData.push({ json: { success: true, id } });
        }
      } catch (error) {
        if (this.continueOnFail()) {
          returnData.push({ json: { error: (error as Error).message }, pairedItem: { item: i } });
          continue;
        }
        throw error;
      }
    }

    return [returnData];
  }
}
```

## Declarative Node (HTTP-Based)

For simple REST APIs, use the declarative style — no `execute()` method needed:

```typescript
import { INodeType, INodeTypeDescription, NodeConnectionType } from 'n8n-workflow';

export class MyApiNode implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'My API',
    name: 'myApi',
    icon: 'file:myapi.svg',
    group: ['transform'],
    version: 1,
    subtitle: '={{$parameter["operation"]}}',
    description: 'Interact with My API',
    defaults: { name: 'My API' },
    inputs: [NodeConnectionType.Main],
    outputs: [NodeConnectionType.Main],
    credentials: [{ name: 'myApi', required: true }],
    requestDefaults: {
      baseURL: '={{ $credentials.baseUrl }}',
      headers: { Accept: 'application/json' },
    },
    properties: [
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        noDataExpression: true,
        options: [
          {
            name: 'Get User',
            value: 'getUser',
            action: 'Get a user',
            routing: {
              request: {
                method: 'GET',
                url: '=/api/users/{{ $parameter.userId }}',
              },
            },
          },
          {
            name: 'Create User',
            value: 'createUser',
            action: 'Create a user',
            routing: {
              request: {
                method: 'POST',
                url: '/api/users',
              },
              send: {
                type: 'body',
                properties: {
                  name: '={{ $parameter.name }}',
                  email: '={{ $parameter.email }}',
                },
              },
            },
          },
        ],
        default: 'getUser',
      },
      {
        displayName: 'User ID',
        name: 'userId',
        type: 'string',
        default: '',
        required: true,
        displayOptions: { show: { operation: ['getUser'] } },
      },
      {
        displayName: 'Name',
        name: 'name',
        type: 'string',
        default: '',
        required: true,
        displayOptions: { show: { operation: ['createUser'] } },
      },
      {
        displayName: 'Email',
        name: 'email',
        type: 'string',
        default: '',
        required: true,
        displayOptions: { show: { operation: ['createUser'] } },
      },
    ],
  };
}
```

## Credential Definition

```typescript
import {
  IAuthenticateGeneric,
  ICredentialTestRequest,
  ICredentialType,
  INodeProperties,
} from 'n8n-workflow';

export class MyApi implements ICredentialType {
  name = 'myApi';
  displayName = 'My API';
  documentationUrl = 'https://docs.example.com/api';

  properties: INodeProperties[] = [
    {
      displayName: 'Base URL',
      name: 'baseUrl',
      type: 'string',
      default: 'https://api.example.com',
      required: true,
    },
    {
      displayName: 'API Key',
      name: 'apiKey',
      type: 'string',
      typeOptions: { password: true },
      default: '',
      required: true,
    },
  ];

  authenticate: IAuthenticateGeneric = {
    type: 'generic',
    properties: {
      headers: {
        Authorization: '=Bearer {{ $credentials.apiKey }}',
      },
    },
  };

  test: ICredentialTestRequest = {
    request: {
      baseURL: '={{ $credentials.baseUrl }}',
      url: '/api/me',
    },
  };
}
```

## Property Types Reference

| Type | Description | TypeOptions |
|------|-------------|-------------|
| `string` | Text input | `password`, `rows` (textarea) |
| `number` | Numeric input | `minValue`, `maxValue`, `numberStepSize` |
| `boolean` | Toggle | — |
| `options` | Dropdown | Use `options` array |
| `multiOptions` | Multi-select | Use `options` array |
| `collection` | Group of optional fields | Use `options` array |
| `fixedCollection` | Group of required fields | Use `values` array |
| `color` | Color picker | — |
| `dateTime` | Date/time picker | — |
| `json` | JSON editor | — |
| `resourceLocator` | Resource picker with search | `modes` |

## Display Options

Control when properties are shown:
```typescript
{
  displayOptions: {
    show: {
      operation: ['create', 'update'],     // show when operation is create OR update
      resource: ['user'],                   // AND resource is user
    },
    hide: {
      operation: ['delete'],               // hide when operation is delete
    },
  },
}
```

## Trigger Node

```typescript
import {
  ITriggerFunctions,
  INodeType,
  INodeTypeDescription,
  ITriggerResponse,
  NodeConnectionType,
} from 'n8n-workflow';

export class MyTrigger implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'My Trigger',
    name: 'myTrigger',
    icon: 'file:mytrigger.svg',
    group: ['trigger'],
    version: 1,
    description: 'Triggers on events from My Service',
    defaults: { name: 'My Trigger' },
    inputs: [],
    outputs: [NodeConnectionType.Main],
    credentials: [{ name: 'myApi', required: true }],
    polling: true,                          // for polling triggers
    properties: [
      {
        displayName: 'Event',
        name: 'event',
        type: 'options',
        options: [
          { name: 'Record Created', value: 'created' },
          { name: 'Record Updated', value: 'updated' },
        ],
        default: 'created',
      },
    ],
  };

  async poll(this: ITriggerFunctions): Promise<ITriggerResponse | null> {
    const credentials = await this.getCredentials('myApi');
    const event = this.getNodeParameter('event') as string;
    const webhookData = this.getWorkflowStaticData('node');
    const lastTimestamp = webhookData.lastTimestamp as string || new Date(0).toISOString();

    const response = await this.helpers.httpRequestWithAuthentication.call(
      this,
      'myApi',
      {
        method: 'GET',
        url: `${credentials.baseUrl}/api/events`,
        qs: { type: event, since: lastTimestamp },
        json: true,
      },
    );

    const events = Array.isArray(response) ? response : response.data || [];

    if (events.length === 0) return null;

    webhookData.lastTimestamp = events[events.length - 1].timestamp;

    return {
      workflowData: [this.helpers.returnJsonArray(events)],
    };
  }
}
```

## Testing Custom Nodes

### Local Development
```bash
# Build the node
npm run build

# Link to local n8n
cd /path/to/n8n-nodes-myservice
npm link

cd ~/.n8n
npm link n8n-nodes-myservice

# Start n8n
n8n start
```

### Linting
```bash
npx n8n-node-dev lint
```

### Publishing to npm
```bash
npm publish
# Users install via: npm install n8n-nodes-myservice
# Then restart n8n
```

## Best Practices

1. **Always handle `continueOnFail()`** — check in catch blocks
2. **Use `pairedItem`** — track item lineage for debugging
3. **Validate inputs early** — throw `NodeOperationError` for bad input
4. **Use `this.helpers.httpRequestWithAuthentication`** — handles credential injection
5. **Support expressions** — don't set `noDataExpression: true` unless the field is static
6. **Add codex metadata** — create `MyNode.node.json` for searchability
7. **Use `NodeConnectionType`** — import from `n8n-workflow` for type safety
8. **Handle pagination** — for "Get Many" operations, implement cursor/offset pagination
9. **Return proper `INodeExecutionData`** — always wrap in `{ json: {...} }`
10. **Use `additionalFields` collection** — for optional parameters to keep the UI clean
