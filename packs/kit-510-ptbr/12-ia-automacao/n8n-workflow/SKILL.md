---
name: n8n-workflow
description: "N8N Workflow — Skill especializada para n8n workflow"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# N8N Workflow

Esta skill capacita o Claude a projetar, configurar e depurar workflows complexos no n8n, utilizando nós específicos, expressões e manipulação de dados para automações robustas.

---

## Keywords

n8n, workflow automation, nós, expressões, webhook, HTTP request, Function, data transformation, credentials, error handling, cron, queue, sub-workflow, triggers, nodes, flows.

---

## Quick Start

1.  **Instalação e Acesso**: Garanta que o n8n esteja instalado (Docker é recomendado: `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`). Acesse a interface web em `http://localhost:5678`.
2.  **Criação do Primeiro Workflow**: No dashboard, clique em "New Workflow". Arraste um nó `Webhook` para a tela, configure o método POST e salve para obter a URL de teste.
3.  **Adição de Nó de Processamento**: Conecte um nó `Function` ao `Webhook`. Dentro do nó `Function`, insira um código JavaScript simples como `return [{json: {message: 'Webhook recebido com sucesso!', data: $json}}];` para manipular os dados de entrada.
4.  **Teste e Execução**: Envie um POST request para a URL do Webhook (ex: `curl -X POST -H "Content-Type: application/json" -d '{"nome": "Maria", "email": "maria@exemplo.com"}' SEU_WEBHOOK_URL`). Observe os dados fluindo pelos nós no painel de execução do n8n.
5.  **Ativação do Workflow**: Após testar e validar o fluxo, ative o workflow usando o toggle no canto superior direito para que ele comece a processar requisições em produção.

---

## Core Workflows

### Workflow 1: Captura de Leads via Webhook e Envio para Google Sheets e Slack

Este workflow automatiza a captura de leads de um formulário web (via webhook) e os registra em uma planilha Google Sheets, além de enviar uma notificação em tempo real para um canal do Slack.

**Passos Detalhados:**

1.  **Trigger `Webhook`**:
    *   **Configuração**: Arraste um nó `Webhook` para a tela.
    *   **Method**: Selecione `POST`.
    *   **Authentication**: `None` (para formulários simples) ou `Header Auth` se o formulário enviar um token.
    *   **Path**: `lead-form`.
    *   **Teste**: Salve o workflow. A URL de teste será algo como `https://your.n8n.url/webhook-test/lead-form`.
    *   **Exemplo de Payload de Entrada**:
        ```json
        {
          "nome": "João Silva",
          "email": "joao.silva@empresa.com",
          "telefone": "+5511987654321",
          "origem": "Landing Page X"
        }
        ```

2.  **Node `Google Sheets` (Append Row)**:
    *   **Conexão**: Conecte o nó `Google Sheets` ao nó `Webhook`.
    *   **Credentials**: Adicione uma nova credencial `Google Sheets API`. Siga os passos de autenticação OAuth2 (crie um projeto no Google Cloud Console, habilite a Google Sheets API, gere credenciais de cliente OAuth e configure no n8n).
    *   **Operation**: Selecione `Append Row`.
    *   **Spreadsheet ID**: Cole o ID da sua planilha Google Sheets (ex: `1ABCDEFG_HIJKLMNOPQRSTUVWXYZ1234567890`).
    *   **Sheet Name**: `Leads` (certifique-se de que a aba exista).
    *   **Data to Append**: Use expressões para mapear os dados do webhook para as colunas.
        *   `Nome da Coluna 1`: `{{$json.nome}}`
        *   `Nome da Coluna 2`: `{{$json.email}}`
        *   `Nome da Coluna 3`: `{{$json.telefone}}`
        *   `Nome da Coluna 4`: `{{$json.origem}}`
        *   `Data de Registro`: `{{new Date().toISOString()}}`

3.  **Node `Slack` (Send Message)**:
    *   **Conexão**: Conecte o nó `Slack` ao nó `Google Sheets` (ou diretamente ao `Webhook` se a ordem não importar).
    *   **Credentials**: Adicione uma nova credencial `Slack API`. Gere um token de bot no painel de apps do Slack e configure no n8n.
    *   **Channel**: `#leads-novo` (ou o ID do canal).
    *   **Text**: Crie uma mensagem formatada.
        ```
        Novo Lead Capturado! 🚀
        Nome: {{$json.nome}}
        Email: {{$json.email}}
        Telefone: {{$json.telefone}}
        Origem: {{$json.origem}}
        ```

### Workflow 2: Monitoramento de Disponibilidade de Produto e Notificação Telegram

Este workflow verifica a disponibilidade de um produto em um e-commerce a cada hora e envia uma notificação via Telegram se o produto estiver de volta ao estoque.

**Passos Detalhados:**

1.  **Trigger `Cron`**:
    *   **Configuração**: Arraste um nó `Cron` para a tela.
    *   **Mode**: `Every X`.
    *   **Value**: `1`.
    *   **Unit**: `Hours`.
    *   **Start Hour**: `0` (começa à meia-noite).
    *   **End Hour**: `23` (termina às 23h).

2.  **Node `HTTP Request` (GET para API do Produto)**:
    *   **Conexão**: Conecte o nó `HTTP Request` ao nó `Cron`.
    *   **URL**: `https://api.ecommerce.com/products/SKU12345` (substitua pela URL real da API ou página a ser scrapeada).
    *   **Method**: `GET`.
    *   **Send Headers**: `User-Agent: n8n-monitor/1.0` (boa prática).
    *   **Response Format**: `JSON`.
    *   **Exemplo de Resposta (supondo JSON):**
        ```json
        {
          "product_id": "SKU12345",
          "name": "Smartphone XYZ",
          "price": 999.99,
          "availability": "out_of_stock",
          "last_updated": "2023-10-26T10:00:00Z"
        }
        ```

3.  **Node `Function` (Lógica de Verificação)**:
    *   **Conexão**: Conecte o nó `Function` ao nó `HTTP Request`.
    *   **Código JavaScript**:
        ```javascript
        const previousAvailability = this.getWorkflowStaticData('productAvailability') || 'unknown';
        const currentAvailability = items[0].json.availability;
        const productName = items[0].json.name;

        if (currentAvailability === 'in_stock' && previousAvailability !== 'in_stock') {
          this.setWorkflowStaticData('productAvailability', 'in_stock');
          return [{ json: { message: `${productName} está AGORA em estoque!`, status: 'in_stock' } }];
        } else if (currentAvailability === 'out_of_stock' && previousAvailability !== 'out_of_stock') {
          this.setWorkflowStaticData('productAvailability', 'out_of_stock');
          // Opcional: notificar quando esgotar
          // return [{ json: { message: `${productName} esgotou.`, status: 'out_of_stock' } }];
        } else {
          // Não houve mudança de estado relevante para notificação
          return []; // Retorna vazio para não prosseguir no workflow
        }
        ```
    *   **Explicação**: Este nó usa `workflowStaticData` para persistir o estado de disponibilidade entre execuções. Ele só passa o item adiante se houver uma mudança de "fora de estoque" para "em estoque".

4.  **Node `Telegram` (Send Message)**:
    *   **Conexão**: Conecte o nó `Telegram` ao nó `Function`.
    *   **Credentials**: Adicione uma nova credencial `Telegram API`. Crie um bot via BotFather, obtenha o token e o chat ID do usuário/grupo.
    *   **Chat ID**: `YOUR_CHAT_ID` (ex: `-1001234567890` para grupo, ou ID do seu usuário).
    *   **Text**: `{{$json.message}}` (utiliza a mensagem gerada pelo nó Function).

---

## Templates

### Template: Webhook para Envio de Mensagem Discord

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "discord-message",
        "options": {}
      },
      "name": "Webhook Lead",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [640, 300]
    },
    {
      "parameters": {
        "channel": {
          "__rl": true,
          "value": "123456789012345678",
          "mode": "id"
        },
        "text": "Novo lead capturado via webhook!\nNome: {{$json.leadName}}\nEmail: {{$json.leadEmail}}\nEmpresa: {{$json.companyName}}",
        "options": {}
      },
      "name": "Discord Send Message",
      "type": "n8n-nodes-base.discord",
      "typeVersion": 1,
      "position": [900, 300],
      "credentials": {
        "discordApi": {
          "id": "YOUR_DISCORD_CREDENTIAL_ID",
          "name": "Discord Bot"
        }
      }
    }
  ],
  "connections": {
    "Webhook Lead": {
      "main": [
        [
          {
            "node": "Discord Send Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
**Como usar**: Importe este JSON no n8n. Configure suas credenciais do Discord Bot (com permissão para enviar mensagens no canal desejado). A URL do webhook será `https://your.n8n.url/webhook-test/discord-message`. Envie um POST com payload `{"leadName": "Alice", "leadEmail": "alice@exemplo.com", "companyName": "TechCorp"}`.

### Template: Função JavaScript para Filtragem e Transformação de Dados

```javascript
// Recebe um array de itens do nó anterior
const items = $input.all();
const outputItems = [];

for (const item of items) {
  const originalData = item.json;

  // Exemplo 1: Filtrar itens com base em uma condição
  if (originalData.status === 'completed' && originalData.value > 100) {
    // Exemplo 2: Transformar e adicionar novos campos
    outputItems.push({
      json: {
        id: originalData.id,
        description: `Processo ${originalData.name} finalizado.`,
        finalValue: originalData.value * 1.05, // Adiciona 5%
        processedAt: new Date().toISOString()
      }
    });
  }
}

// Retorna o array de itens transformados
return outputItems;
```
**Como usar**: Insira este código em um nó `Function`. Ele processará itens de entrada (espera `id`, `name`, `status`, `value`), filtrará por `status === 'completed'` e `value > 100`, e transformará os dados adicionando `description`, `finalValue` e `processedAt`.

---

## Checklist

- [x] Credenciais sensíveis configuradas com segurança (ex: usar Secrets, não valores hardcoded).
- [x] Testes de execução manual para cada nó do workflow.
- [x] Tratamento de erros configurado (nó `Error Workflow` ou `Continue On Error` nos nós relevantes).
- [x] Utilização de expressões para dinâmica de dados (`{{$json.campo}}`, `{{$node["Nome do Nó"].json.resultado}}`).
- [x] Workflow ativado somente após validação completa em ambiente de teste.
- [x] Monitoramento de logs e execuções para identificar falhas rapidamente.
- [x] Otimização de nós `Function` para evitar sobrecarga de memória em grandes datasets.
- [x] Documentação interna dos workflows complexos com `Notes` para facilitar manutenção.
- [x] Uso de `Set` e `Merge` para manipular a estrutura de dados de forma eficiente.
- [x] Consideração de concorrência e idempotência para webhooks e triggers recorrentes.

---

## Métricas de Referência

| Métrica                      | Benchmark (Ideal) | Meta (Aceitável) |
|------------------------------|-------------------|------------------|
| Latência Média de Execução   | < 500 ms          | < 2000 ms        |
| Taxa de Sucesso do Workflow  | > 99.5%           | > 98%            |
| Consumo de Memória por Exec. | < 256 MB          | < 512 MB         |
| Execuções/Minuto (Webhook)   | > 100             | > 50             |
| Erros de Credenciais/API    | 0%                | < 0.1%           |
| Tempo de Resolução de Erro   | < 30 min          | < 60 min         |

---

## Erros Comuns

1.  **Credenciais Inválidas ou Expiradas**: Ao configurar um nó como `Google Sheets` ou `Slack`, as credenciais OAuth podem expirar ou ter permissões insuficientes.
    *   **Como evitar**: Sempre verificar as permissões no provedor de serviço (Google Cloud Console, Slack Apps) e reautenticar as credenciais no n8n se necessário. Use credenciais com escopo mínimo necessário.
2.  **JSON Malformado em `HTTP Request` ou `Webhook`**: Dados de entrada com chaves ou valores incorretos, ou corpo da requisição não sendo um JSON válido quando esperado.
    *   **Como evitar**: Utilize o painel "Test Webhook" ou "Execute Node" para inspecionar a entrada. Use o nó `JSON` para parsear strings e `Set` para formatar JSON de saída. Valide o payload com ferramentas como `jsonlint.com`.
3.  **Expressões Incorretas ou Caminhos de Dados Ausentes**: Tentar acessar `{{$json.campoInexistente}}` ou `{{$node["Nó que Falhou"].json.dado}}` quando o nó anterior não produziu o dado esperado.
    *   **Como evitar**: Verifique a saída do nó anterior no painel de execução. Use `try...catch` em nós `Function` para lidar com dados ausentes e `IF` para criar branches condicionais baseadas na existência de dados. Use o `dot notation` ou `bracket notation` corretamente, e teste as expressões no editor de expressões do n8n.

---

## Dicas Avançadas

1.  **Orquestração de Sub-Workflows com `Execute Workflow`**: Para workflows complexos e modularização, crie sub-workflows que realizam tarefas específicas (ex: validação de dados, envio de notificação genérica). O nó `Execute Workflow` permite chamar esses sub-workflows, passando dados de entrada e recebendo resultados, mantendo o workflow principal mais limpo e reutilizável.
    *   **Exemplo**: Um workflow `ProcessarPagamento` pode chamar um sub-workflow `EnviarEmailConfirmacao` e `AtualizarEstoque` sequencialmente, cada um com sua própria lógica e tratamento de erros encapsulados.
2.  **Persistência de Dados entre Execuções com `Workflow Static Data`**: O objeto `this.getWorkflowStaticData()` e `this.setWorkflowStaticData()` dentro de um nó `Function` permite armazenar pequenas quantidades de dados que persistem entre as execuções do workflow. Ideal para contadores, estados de máquina, ou valores de referência (como o preço monitorado no exemplo do Telegram).
    *   **Exemplo de Uso**: `this.setWorkflowStaticData('lastRunTimestamp', new Date().toISOString());` para saber quando foi a última execução bem-sucedida para lógica de retry customizada.
3.  **Manipulação de Arrays com `Split In Batches` e `Item Lists`**: Ao lidar com grandes volumes de dados ou arrays complexos, os nós `Split In Batches` e `Item Lists` são cruciais. `Split In Batches` divide um array em pacotes menores para processamento paralelo ou sequencial, evitando timeouts. `Item Lists` permite adicionar, remover ou obter itens de arrays.
    *   **Exemplo**: Dividir uma lista de 1000 emails em batches de 50 para enviar via API de email, controlando limites de taxa.
4.  **Uso de `Webhook Response` para Feedback Síncrono**: Em workflows iniciados por `Webhook`, o nó `Webhook Response` é essencial para enviar uma resposta HTTP de volta ao serviço que disparou o webhook. Você pode configurar o status code (ex: 200, 400), headers e o corpo da resposta (JSON, texto).
    *   **Exemplo**: Após receber um pedido, retornar um `200 OK` com `{"status": "received", "orderId": "XYZ123"}`. Se houver falha na validação, retornar `400 Bad Request` com `{"error": "invalid_data"}`.
5.  **Variáveis de Ambiente para Configurações Dinâmicas**: Utilize variáveis de ambiente no n8n para gerenciar URLs de API, chaves públicas, ou outras configurações que mudam entre ambientes (desenvolvimento, staging, produção). Acesse-as via `{{$env.MY_VARIABLE_NAME}}` nas configurações dos nós.
    *   **Exemplo**: Em vez de hardcodar a URL de uma API, use `{{$env.CRM_API_URL}}`. O valor será injetado do arquivo `.env` do seu n8n.