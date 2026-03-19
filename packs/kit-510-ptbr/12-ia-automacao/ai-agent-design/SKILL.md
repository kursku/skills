---
name: ai-agent-design
description: "Ai Agent Design — Skill especializada para ai agent design"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Ai Agent Design

Esta skill capacita o Claude a projetar, implementar e otimizar arquiteturas de agentes autônomos baseados em LLMs, integrando loops de raciocínio, uso de ferramentas e gestão de memória para automações complexas.

---

## Keywords

Agente Autônomo, ReAct, Loop OODA, Planejamento de Agente, Ferramentas de Agente, Memória de Agente, Reflexão de Agente, Prompt Engineering para Agentes, Orquestração de LLM, Chain of Thought, Função de Chamada, Vector Database, Agente Hierárquico.

---

## Quick Start

1.  **Estruturar Prompt ReAct Inicial:** Construa um prompt que instrua o agente a `Pensar` (raciocinar), `Agir` (usar ferramentas) e `Observar` (analisar resultados da ação) em um loop contínuo para uma tarefa específica.
2.  **Definir Ferramentas Essenciais:** Liste as ferramentas que o agente pode usar (e.g., `api_weather_check(city)`, `db_query_product(id)`) com suas descrições e parâmetros, explicitando-as no prompt ou via função de chamada.
3.  **Configurar Webhook de Ação:** Crie um endpoint de webhook (ex: Make/N8N) que receba o nome da ferramenta e seus argumentos do agente, execute a lógica externa (API, DB) e retorne o resultado ao agente.
4.  **Implementar Loop de Interação:** Configure o ambiente para que o agente receba um objetivo, execute seu ciclo ReAct, e o resultado da ação da ferramenta seja reintroduzido no próximo turno do prompt como `Observação`.
5.  **Teste de Cenário Base:** Teste o agente com um cenário simples e direto, observando o `Pensamento`, a `Ação` e a `Observação` para garantir que o fluxo básico de raciocínio e uso de ferramentas esteja correto.

---

## Core Workflows

### Workflow 1: Design de Agente ReAct para Automação de Atendimento ao Cliente

Este workflow detalha a criação de um agente autônomo focado em resolver requisições comuns de clientes, como verificar status de pedido ou saldo de conta, utilizando o padrão ReAct para raciocínio e execução de ferramentas.

**Passos Detalhados:**

1.  **Definição do Objetivo do Agente:** O agente deve ser capaz de responder a perguntas sobre pedidos e contas, interagir com sistemas de backend via API e informar o cliente de forma concisa.
    *   **Exemplo:** Um cliente pergunta "Qual o status do meu pedido #12345?" ou "Quanto de saldo tenho na minha conta?".

2.  **Identificação e Definição de Ferramentas:** Mapeie as ações que o agente precisa executar externamente. Cada ferramenta deve ter um nome claro, uma descrição de sua função e uma especificação de seus parâmetros.
    *   `get_order_status(order_id: str)`: Consulta o status de um pedido.
    *   `get_account_balance(customer_id: str)`: Consulta o saldo da conta de um cliente.
    *   `send_customer_message(customer_id: str, message: str)`: Envia uma mensagem ao cliente.
    *   **Exemplo de Prompt para Ferramentas:**
        ```
        Ferramentas disponíveis:
        - get_order_status(order_id: str): Consulta o status de um pedido. Retorna 'PENDENTE', 'ENVIADO', 'ENTREGUE'.
        - get_account_balance(customer_id: str): Consulta o saldo da conta de um cliente. Retorna o valor em BRL.
        - send_customer_message(customer_id: str, message: str): Envia uma mensagem final ao cliente.

        Formato da resposta:
        Thought: Você deve sempre pensar no que fazer.
        Action: a_ferramenta(param1=valor1, param2=valor2)
        Observation: O resultado da ação.
        ... (Este ciclo Thought/Action/Observation pode se repetir)
        Thought: Pensamento final antes de enviar a resposta.
        Action: send_customer_message(customer_id="[ID_CLIENTE]", message="[SUA_RESPOSTA_FINAL]")
        ```

3.  **Implementação da Camada de Execução de Ferramentas (Webhook/API Gateway):** Crie um serviço (ex: usando Make, N8N, ou um microsserviço em Python/Node.js) que atue como um proxy entre o agente (LLM) e os sistemas de backend reais. Este serviço deve:
    *   Receber a `Action` do agente (nome da ferramenta e parâmetros).
    *   Validar os parâmetros.
    *   Chamar a API ou banco de dados correspondente.
    *   Retornar o resultado para o agente como `Observation`.
    *   **Exemplo de Webhook (N8N/Make):**
        *   **Trigger:** Webhook POST com corpo `{ "tool_name": "get_order_status", "parameters": { "order_id": "12345" } }`
        *   **Node 1 (Router/Switch):** Direciona com base em `tool_name`.
        *   **Node 2 (HTTP Request - get_order_status):** Chama `GET https://api.meusistema.com/orders/{order_id}`.
        *   **Node 3 (HTTP Request - get_account_balance):** Chama `GET https://api.meusistema.com/accounts/{customer_id}/balance`.
        *   **Node X (Return Webhook):** Retorna o JSON com o resultado da chamada.

4.  **Loop de Interação e State Management:** O sistema orquestrador (ex: Claude Code CLI com um script customizado) deve gerenciar o histórico da conversa e o estado do agente.
    *   Recebe a pergunta do cliente.
    *   Envia a pergunta + histórico + ferramentas para o LLM.
    *   Recebe a resposta do LLM (Thought/Action).
    *   Se for `Action`: Chama o webhook de ferramentas e espera o `Observation`.
    *   Adiciona o `Observation` ao histórico e envia novamente para o LLM.
    *   Repete até que o LLM decida enviar uma mensagem final ao cliente (e.g., usando `send_customer_message`).
    *   **Exemplo de Prompt com Histórico:**
        ```
        Você é um agente de atendimento. Responda ao cliente usando as ferramentas.
        <history>
        Cliente: Qual o status do meu pedido #12345?
        </history>
        Thought: Preciso consultar o status do pedido 12345. A ferramenta get_order_status é a mais adequada.
        Action: get_order_status(order_id="12345")
        Observation: ENVIADO
        Thought: O pedido está enviado. Posso informar o cliente.
        Action: send_customer_message(customer_id="ABC", message="Seu pedido #12345 está atualmente com status ENVIADO.")
        ```

### Workflow 2: Implementação de Memória Persistente e Reflexão para Agentes de Planejamento

Este workflow foca em dar ao agente a capacidade de "aprender" com interações passadas, armazenar informações relevantes (memória de longo prazo) e refinar suas estratégias (reflexão), melhorando seu desempenho ao longo do tempo.

**Passos Detalhados:**

1.  **Estruturação da Memória de Curto Prazo (Contexto Conversacional):** Mantenha o histórico da interação atual do agente como parte do prompt para o LLM. Isso inclui a pergunta inicial, pensamentos, ações, observações e respostas parciais.
    *   **Métrica de Referência:** Max-Tokens de contexto em 4096-8192 tokens. Exceder isso requer sumarização.

2.  **Criação da Memória de Longo Prazo (Vector Database):** Implemente um banco de dados vetorial (ex: ChromaDB, Pinecone, Weaviate) para armazenar informações duradouras que o agente possa consultar.
    *   **Tipos de Dados:**
        *   **Conhecimento Base:** Documentação de produtos, FAQs, políticas da empresa.
        *   **Experiências Passadas:** Resoluções de problemas complexos, planos de sucesso, feedback de usuários.
        *   **Perfis de Usuários:** Preferências, histórico de compras.
    *   **Processo:**
        *   Texto é dividido em `chunks`.
        *   Cada `chunk` é transformado em um vetor (embedding) usando um modelo de embedding (ex: `text-embedding-ada-002`).
        *   Vetor e texto original são armazenados no Vector DB.

3.  **Mecanismo de Recuperação de Memória (Retrieval-Augmented Generation - RAG):** Antes de cada turno de raciocínio, o agente consulta a memória de longo prazo para informações relevantes.
    *   **Ferramenta de Recuperação:** Adicione uma ferramenta como `search_long_term_memory(query: str)` ao agente.
    *   **Implementação:** Quando o agente invoca esta ferramenta, a `query` é vetorizada e usada para buscar `k` documentos mais similares no Vector DB. O conteúdo desses documentos é retornado como `Observation`.
    *   **Exemplo de Prompt para RAG:**
        ```
        Ferramentas disponíveis:
        - search_long_term_memory(query: str): Busca informações relevantes na base de conhecimento. Retorna trechos de texto.

        Thought: A tarefa requer informações sobre a política de devolução. Preciso consultar a memória de longo prazo.
        Action: search_long_term_memory(query="política de devolução de produtos")
        Observation: "Nossa política de devolução permite trocas em até 30 dias com nota fiscal e produto intacto. Para produtos eletrônicos, o prazo é de 7 dias."
        Thought: Com base na informação, posso responder ao cliente.
        ```

4.  **Loop de Reflexão e Auto-Correção:** O agente deve ser capaz de avaliar seu próprio desempenho e refinar seu plano ou conhecimento.
    *   **Trigger de Reflexão:** Pode ser ativado após uma falha na tarefa, um feedback negativo do usuário, ou periodicamente.
    *   **Prompt de Reflexão:** O agente recebe seu histórico de interações e é instruído a:
        *   Identificar pontos de falha ou ineficiências.
        *   Propor melhorias para o plano ou uso de ferramentas.
        *   Gerar novos "conhecimentos" ou "regras" a serem armazenadas na memória de longo prazo.
    *   **Exemplo de Prompt de Reflexão:**
        ```
        Você falhou na tarefa de "resolver problema X" após 3 tentativas. Analise o histórico abaixo e responda:
        1. Qual foi a principal razão da falha?
        2. Que estratégia alternativa poderia ter sido usada?
        3. Há alguma informação nova que deveria ser adicionada à memória de longo prazo para evitar essa falha no futuro?

        <history>
        [Histórico completo da interação, incluindo Thought/Action/Observation]
        </history>
        ```
    *   **Ação de Atualização de Memória:** O resultado da reflexão (novas regras, insights) pode ser inserido no Vector DB para futuras consultas ou usado para refinar o prompt inicial do agente. Uma ferramenta `add_to_long_term_memory(content: str, tags: list)` pode ser utilizada.

---

## Templates

### Prompt ReAct para Agente de Suporte Técnico

```
Você é um Agente de Suporte Técnico, seu objetivo é diagnosticar e resolver problemas de conectividade de rede para usuários.
Você tem acesso às seguintes ferramentas:

1.  `diagnose_network_issue(user_id: str)`: Executa um diagnóstico de rede no dispositivo do usuário. Retorna um JSON com `{"status": "OK" | "ERROR", "details": "string", "suggested_fix": "string"}`.
2.  `restart_router(user_id: str)`: Envia um comando para reiniciar o roteador do usuário. Retorna `{"success": true | false, "message": "string"}`.
3.  `escalate_to_level2(user_id: str, issue_summary: str)`: Encaminha o problema para um técnico de nível 2. Retorna `{"ticket_id": "string", "message": "string"}`.
4.  `inform_user(user_id: str, message: str)`: Envia uma mensagem final ao usuário.

Use o formato ReAct:

Thought: Você deve sempre pensar no que fazer.
Action: a_ferramenta(param1=valor1, param2=valor2)
Observation: O resultado da ação.
... (Este ciclo Thought/Action/Observation pode se repetir até a resolução ou escalada)
Thought: Pensamento final antes de enviar a resposta ao usuário.
Action: inform_user(user_id="[ID_USUARIO]", message="[SUA_RESPOSTA_FINAL]")

<history>
Usuário: Minha internet está muito lenta, não consigo assistir vídeos. Meu ID é usuario123.
</history>
```

### Definição de Ferramenta para Automação N8N/Make

```json
{
  "tool_name": "create_jira_ticket",
  "description": "Cria um novo ticket no Jira com um resumo e descrição. Requer autenticação.",
  "parameters": {
    "type": "object",
    "properties": {
      "summary": {
        "type": "string",
        "description": "Um breve resumo do problema ou solicitação."
      },
      "description": {
        "type": "string",
        "description": "Uma descrição detalhada do problema, incluindo passos para reprodução ou contexto."
      },
      "project_key": {
        "type": "string",
        "description": "A chave do projeto Jira (ex: 'SUPORTE', 'DEV').",
        "enum": ["SUPORTE", "DEV", "INFRA"]
      },
      "issue_type": {
        "type": "string",
        "description": "O tipo de issue (ex: 'Bug', 'Task', 'Story').",
        "enum": ["Bug", "Task", "Story"]
      }
    },
    "required": ["summary", "description", "project_key", "issue_type"]
  },
  "webhook_endpoint": "https://webhook.site/abcdef12-3456-7890-abcd-ef1234567890"
}
```

---

## Checklist

- [x] Agente opera em um loop de raciocínio (ex: ReAct, OODA).
- [x] Todas as ferramentas externas são claramente definidas com descrições e parâmetros.
- [x] Mecanismo de execução de ferramentas (webhook/API Gateway) está implementado e testado.
- [x] O tratamento de erros das ferramentas é propagado de volta ao agente como `Observation`.
- [x] Estratégia de gestão de memória de curto prazo (histórico de contexto) está definida e otimizada.
- [x] Estratégia de gestão de memória de longo prazo (Vector DB) está implementada para RAG.
- [x] Mecanismo de reflexão/auto-correção está presente para refinar o comportamento do agente.
- [x] Cenários de teste para falhas e recuperações foram definidos e executados.
- [x] O custo por interação do agente é monitorado para otimização de tokens.
- [x] A segurança das chamadas de API e dados sensíveis é garantida nas ferramentas.

---

## Métricas de Referência

| Métrica                      | Benchmark (Bom) | Meta (Excelente) |
|------------------------------|-----------------|------------------|
| Taxa de Sucesso da Tarefa    | 80%             | 95%              |
| Latência de Resposta Média   | < 5 segundos    | < 2 segundos     |
| Custo por Interação (tokens) | < 1000 tokens   | < 500 tokens     |
| Taxa de Reflexão Bem-Sucedida| 70%             | 90%              |
| Recall de Memória (RAG)      | 0.75            | 0.90             |

---

## Erros Comuns

1.  **Over-reliance em um único prompt de raciocínio**: Agentes que usam um prompt monolítico para todas as etapas do raciocínio tendem a se confundir em tarefas complexas.
    *   **Como evitar**: Modularize o raciocínio. Use prompts específicos para `Planejamento`, `Execução de Ferramentas`, `Avaliação` e `Reflexão`. Por exemplo, um prompt inicial para gerar um plano de alto nível, e prompts menores para cada passo do plano.
2.  **Ferramentas mal definidas ou ambíguas**: Descrições de ferramentas vagas ou parâmetros inconsistentes levam o agente a fazer chamadas incorretas ou inválidas.
    *   **Como evitar**: Forneça descrições concisas e exemplos de uso para cada ferramenta. Use tipagem estrita para parâmetros (string, int, enum) e valide-os na camada de execução (webhook). Ex: `get_product_info(product_id: string)` em vez de `get_info(item)`.
3.  **Falta de tratamento de erros das ferramentas**: Se uma chamada de ferramenta falha e o agente não é informado ou não consegue processar o erro, ele entra em um loop infinito ou gera uma resposta sem sentido.
    *   **Como evitar**: A camada de execução de ferramentas deve sempre retornar um `Observation` útil, mesmo em caso de erro. Por exemplo, `{ "status": "ERROR", "message": "Produto não encontrado com ID 123" }` ou `{ "status": "FAILURE", "error_code": 404, "details": "API de estoque indisponível" }`. O agente deve ser instruído a lidar com esses `status` em seu `Thought`.

---

## Dicas Avançadas

1.  **Agentes Hierárquicos (Sub-Agentes)**: Para tarefas complexas, divida o problema em sub-tarefas e designe sub-agentes especializados para cada uma. Um agente "orquestrador" delega e integra os resultados.
    *   **Exemplo**: Um agente principal de "Gestão de Projeto" pode delegar "Geração de Requisitos" a um sub-agente, "Desenvolvimento de Código" a outro, e "Teste" a um terceiro.
2.  **Otimização de Contexto com Resumos Dinâmicos**: Em vez de passar o histórico completo em cada turno, implemente um mecanismo que resume partes antigas da conversa à medida que o contexto se torna muito grande, mantendo os detalhes mais recentes intocados.
    *   **Exemplo**: Use um LLM para gerar um "Resumo da Conversa até o Momento" a cada 10 turnos, substituindo os turnos antigos por esse resumo, liberando tokens para o raciocínio atual.
3.  **Técnicas de Árvore de Pensamento (Tree of Thought - ToT)**: Permite que o agente explore múltiplos caminhos de raciocínio, avalie a viabilidade de cada um e selecione o melhor antes de agir, simulando uma busca em árvore.
    *   **Exemplo**: Para um problema de planejamento logístico, o agente pode gerar 3-5 possíveis planos (`Thought: Opção A: ...`, `Thought: Opção B: ...`), e então usar uma ferramenta de "simulação" ou um prompt de "avaliação" para escolher o plano ótimo.
4.  **Meta-Prompting para Adaptação Dinâmica**: Use um meta-prompt (um prompt que gera ou modifica outro prompt) para ajustar dinamicamente o comportamento do agente com base no contexto, no usuário ou no ambiente.
    *   **Exemplo**: Um agente de vendas pode ter seu prompt de persona ajustado (ex: "seja mais assertivo" vs. "seja mais empático") com base no perfil do cliente recuperado da memória de longo prazo.
5.  **Encapsulamento de Ferramentas Complexas**: Agrupe múltiplas operações de API ou automações complexas em uma única "ferramenta de alto nível" para o agente. Isso simplifica o raciocínio do agente e reduz o número de tokens.
    *   **Exemplo**: Em vez de `fetch_product_details`, `check_stock`, `calculate_shipping`, crie uma ferramenta `get_full_product_availability(product_id, shipping_address)` que orquestra essas chamadas internamente e retorna um resumo consolidado.