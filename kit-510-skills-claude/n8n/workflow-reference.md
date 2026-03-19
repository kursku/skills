# n8n Workflow Reference

## Workflow Design Patterns

### Sequential Processing
Nodes execute one after another. Data flows from trigger → processing → output.

```
Webhook → Set Fields → HTTP Request → Respond to Webhook
```

### Conditional Branching
Use IF or Switch nodes to route data based on conditions.

```json
{
  "name": "IF",
  "type": "n8n-nodes-base.if",
  "parameters": {
    "conditions": {
      "options": { "caseSensitive": true },
      "conditions": [
        {
          "leftValue": "={{ $json.status }}",
          "rightValue": "active",
          "operator": { "type": "string", "operation": "equals" }
        }
      ]
    }
  }
}
```

### Parallel Processing
Use Merge node to combine outputs from parallel branches.

```
Trigger → Branch A → Merge → Output
       ↘ Branch B ↗
```

Merge modes:
- **Append** — combine all items from both inputs
- **Combine** — match items by position or field
- **Choose Branch** — wait for one input, ignore the other
- **Multiplex** — create all possible combinations

### Loop Pattern
Use `SplitInBatches` for processing large datasets in chunks:

```
Trigger → SplitInBatches → Process Batch → [loop back to SplitInBatches]
                         ↘ Done output → Final Step
```

### Sub-Workflow Pattern
Extract reusable logic into separate workflows:

```json
{
  "name": "Execute Workflow",
  "type": "n8n-nodes-base.executeWorkflow",
  "parameters": {
    "source": "database",
    "workflowId": "workflow-id-here",
    "mode": "each"
  }
}
```

## Triggers

### Webhook Trigger
```json
{
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "my-endpoint",
    "httpMethod": "POST",
    "responseMode": "responseNode",
    "options": {
      "rawBody": true
    }
  }
}
```

Webhook options:
- `responseMode`: `"onReceived"` (immediate 200), `"lastNode"` (wait for completion), `"responseNode"` (use Respond to Webhook node)
- `authentication`: `"none"`, `"basicAuth"`, `"headerAuth"`
- `rawBody`: access raw request body
- `binaryPropertyName`: handle file uploads

### Schedule Trigger
```json
{
  "name": "Schedule Trigger",
  "type": "n8n-nodes-base.scheduleTrigger",
  "parameters": {
    "rule": {
      "interval": [
        {
          "field": "cronExpression",
          "expression": "0 9 * * 1-5"
        }
      ]
    }
  }
}
```

Interval options: `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `cronExpression`

### Form Trigger
```json
{
  "name": "Form Trigger",
  "type": "n8n-nodes-base.formTrigger",
  "parameters": {
    "formTitle": "Contact Form",
    "formDescription": "Submit your details",
    "formFields": {
      "values": [
        { "fieldLabel": "Name", "fieldType": "text", "requiredField": true },
        { "fieldLabel": "Email", "fieldType": "email", "requiredField": true },
        { "fieldLabel": "Message", "fieldType": "textarea" }
      ]
    },
    "options": { "respondWithData": true }
  }
}
```

## Flow Control

### IF Node
```json
{
  "type": "n8n-nodes-base.if",
  "parameters": {
    "conditions": {
      "conditions": [
        {
          "leftValue": "={{ $json.amount }}",
          "rightValue": 100,
          "operator": { "type": "number", "operation": "gt" }
        }
      ],
      "combinator": "and"
    }
  }
}
```

Operators by type:
- **string**: equals, notEquals, contains, notContains, startsWith, endsWith, regex, isEmpty, isNotEmpty
- **number**: equals, notEquals, gt, gte, lt, lte
- **boolean**: true, false
- **dateTime**: after, before, equals
- **array**: contains, notContains, lengthEquals, lengthGt, lengthLt, isEmpty, isNotEmpty

### Switch Node
Route to multiple outputs based on rules:
```json
{
  "type": "n8n-nodes-base.switch",
  "parameters": {
    "mode": "rules",
    "rules": {
      "values": [
        {
          "conditions": {
            "conditions": [{ "leftValue": "={{ $json.type }}", "rightValue": "email", "operator": { "type": "string", "operation": "equals" } }]
          },
          "output": 0
        },
        {
          "conditions": {
            "conditions": [{ "leftValue": "={{ $json.type }}", "rightValue": "sms", "operator": { "type": "string", "operation": "equals" } }]
          },
          "output": 1
        }
      ]
    },
    "options": { "fallbackOutput": "extra" }
  }
}
```

### Wait Node
Pause execution for a duration or until a webhook is received:
```json
{
  "type": "n8n-nodes-base.wait",
  "parameters": {
    "resume": "timeInterval",
    "amount": 5,
    "unit": "minutes"
  }
}
```

Resume options: `"timeInterval"`, `"specificTime"`, `"webhook"`

## Error Handling

### Node-Level Retry
```json
{
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 1000
}
```

### Error Output Branch
Set `onError: "continueErrorOutput"` on a node to route errors to a second output:

```
HTTP Request → (success) → Process Result
            ↘ (error)   → Handle Error → Notify Admin
```

### Error Workflow
Configure in workflow settings to catch unhandled execution failures:
```json
{
  "settings": {
    "errorWorkflow": "error-handler-workflow-id"
  }
}
```

The error workflow receives:
```json
{
  "execution": { "id": "...", "url": "...", "retryOf": "...", "error": { "message": "...", "stack": "..." } },
  "workflow": { "id": "...", "name": "..." }
}
```

### Try/Catch Pattern
Wrap risky operations in error branches and use Merge to continue regardless:

```
→ HTTP Request (onError: continueErrorOutput)
    → (success) → Merge → Continue
    → (error)   → Set Default → Merge
```

## Expressions Reference

### Data Access
```
{{ $json }}                              // current item's JSON data
{{ $json.nested.field }}                 // nested field access
{{ $json['field with spaces'] }}         // bracket notation
{{ $binary }}                            // current item's binary data
{{ $input.all() }}                       // all input items
{{ $input.first() }}                     // first input item
{{ $input.last() }}                      // last input item
{{ $input.item }}                        // current item in loop
{{ $('Node Name').all() }}               // all items from a specific node
{{ $('Node Name').first().json.field }}  // specific field from a node
{{ $('Node Name').params.fieldName }}    // node parameter value
```

### Built-in Variables
```
{{ $now }}                     // current DateTime (Luxon)
{{ $today }}                   // today at midnight (Luxon)
{{ $runIndex }}                // current run index (0-based)
{{ $itemIndex }}               // current item index (0-based)
{{ $nodeVersion }}             // version of the current node
{{ $prevNode }}                // previous node info
{{ $execution.id }}            // execution ID
{{ $execution.resumeUrl }}     // URL to resume a waiting execution
{{ $workflow.id }}             // workflow ID
{{ $workflow.name }}           // workflow name
{{ $workflow.active }}         // whether workflow is active
{{ $vars.myVariable }}         // workflow variable
{{ $env.MY_ENV_VAR }}          // environment variable (if allowed)
```

### Data Transformation Functions

**String:**
```
{{ "hello".toUpperCase() }}              // HELLO
{{ "Hello World".toSnakeCase() }}        // hello_world
{{ "hello".replaceAll('l', 'r') }}       // herro
{{ "hello@email.com".isEmail() }}        // true
{{ "not empty".isEmpty() }}              // false
{{ "hello world".extractUrl() }}         // extracts URL if present
{{ "<p>text</p>".stripTags() }}          // text
{{ "hello".hash('sha256') }}             // SHA-256 hash
```

**Number:**
```
{{ (1.5).ceil() }}                       // 2
{{ (1.5).floor() }}                      // 1
{{ (1.567).round(2) }}                   // 1.57
{{ (100).isEven() }}                     // true
{{ (1024).toFixed(2) }}                  // "1024.00"
```

**Array:**
```
{{ [1,2,3].length }}                     // 3
{{ ["a","b"].includes("a") }}            // true
{{ [3,1,2].sort() }}                     // [1,2,3]
{{ [1,2,3].reverse() }}                  // [3,2,1]
{{ [1,[2,3]].flatten() }}                // [1,2,3]
{{ [1,2,2,3].unique() }}                 // [1,2,3]
{{ ["a","b","c"].chunk(2) }}             // [["a","b"],["c"]]
{{ [1,2,3].average() }}                  // 2
{{ [1,2,3].sum() }}                      // 6
{{ [1,2,3].min() }}                      // 1
{{ [1,2,3].max() }}                      // 3
```

**Object:**
```
{{ $json.keys() }}                       // array of keys
{{ $json.values() }}                     // array of values
{{ $json.hasField('name') }}             // true/false
{{ $json.isEmpty() }}                    // true/false
{{ Object.keys($json).length }}          // number of fields
```

**DateTime (Luxon):**
```
{{ $now.toFormat('yyyy-MM-dd HH:mm') }}  // 2024-01-15 09:30
{{ $now.plus({ days: 7 }) }}             // 7 days from now
{{ $now.minus({ hours: 2 }) }}           // 2 hours ago
{{ $now.startOf('month') }}              // first of current month
{{ $now.endOf('month') }}                // last of current month
{{ $now.toISO() }}                       // ISO 8601 string
{{ $now.toMillis() }}                    // Unix timestamp (ms)
{{ $now.weekday }}                       // 1 (Mon) to 7 (Sun)
{{ DateTime.fromISO('2024-01-15') }}     // parse ISO date
{{ DateTime.fromFormat('15/01/2024', 'dd/MM/yyyy') }}  // parse custom format
```

### JMESPath Queries
```
{{ $jmespath($json, "items[*].name") }}              // all item names
{{ $jmespath($json, "items[?price > `100`]") }}      // filter by price
{{ $jmespath($json, "items[0:3]") }}                 // first 3 items
{{ $jmespath($json, "max_by(items, &price)") }}      // item with max price
{{ $jmespath($json, "sort_by(items, &name)") }}      // sort by name
{{ $jmespath($json, "length(items)") }}              // count items
```

### Helper Functions
```
{{ $if(condition, trueValue, falseValue) }}   // ternary
{{ $ifEmpty(value, fallback) }}               // fallback if empty/null
{{ $min(1, 2, 3) }}                           // 1
{{ $max(1, 2, 3) }}                           // 3
{{ $not(true) }}                              // false
```

## HTTP Request Node

### GET with Authentication
```json
{
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "GET",
    "url": "https://api.example.com/data",
    "authentication": "genericCredentialType",
    "genericAuthType": "httpHeaderAuth",
    "sendQuery": true,
    "queryParameters": {
      "parameters": [
        { "name": "page", "value": "={{ $json.page }}" }
      ]
    },
    "options": {
      "response": { "response": { "responseFormat": "json" } },
      "timeout": 10000,
      "batching": { "batch": { "batchSize": 10, "batchInterval": 1000 } }
    }
  }
}
```

### POST with JSON Body
```json
{
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/create",
    "sendBody": true,
    "bodyParameters": {
      "parameters": [
        { "name": "name", "value": "={{ $json.name }}" },
        { "name": "email", "value": "={{ $json.email }}" }
      ]
    },
    "options": {
      "response": { "response": { "responseFormat": "json" } }
    }
  }
}
```

### Pagination
```json
{
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "GET",
    "url": "https://api.example.com/items",
    "options": {
      "pagination": {
        "paginationMode": "off",
        "paginationCompleteWhen": "responseIsEmpty",
        "limitPagesFetched": true,
        "maxRequests": 10
      }
    }
  }
}
```

## Common Workflow Templates

### API Proxy (Webhook → Transform → Respond)
```
Webhook (POST /api/proxy)
  → Set (transform request)
  → HTTP Request (call external API)
  → Set (transform response)
  → Respond to Webhook
```

### Scheduled Data Sync
```
Schedule Trigger (every hour)
  → HTTP Request (fetch from source)
  → SplitInBatches (batch of 50)
  → HTTP Request (upsert to destination)
  → [loop back]
  → Slack (notify completion)
```

### Event-Driven Processing
```
Webhook (receive event)
  → Switch (route by event type)
  → [Branch 1: created] → Process new item → DB Insert
  → [Branch 2: updated] → Process update → DB Update
  → [Branch 3: deleted] → Archive → DB Delete
  → [Fallback] → Log unknown event
```

### AI-Powered Pipeline
```
Form Trigger (user question)
  → AI Agent (process with LLM)
  → Set (format response)
  → Respond to Webhook
```

### Error-Resilient Integration
```
Schedule Trigger
  → HTTP Request (onError: continueErrorOutput)
      → (success) → Process → DB Insert
      → (error)   → Wait (5 min) → HTTP Request (retry)
                          → (success) → Process → DB Insert
                          → (error)   → Slack (alert team)
```
