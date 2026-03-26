---
name: make-scenario
description: "Make Scenario — Skill especializada para criar, otimizar e depurar fluxos de automação complexos na plataforma Make.com."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Make Scenario

Esta skill capacita o Claude a projetar, implementar e depurar cenários de automação robustos e eficientes na plataforma Make.com (anteriormente Integromat), utilizando módulos, webhooks, APIs e lógica condicional.

---

## Keywords

Make.com, Cenário Make, Automação de Fluxos, Integração API, Webhook Customizado, Módulos Make, Roteador, Filtro Condicional, Agendador, Conexões, Data Stores, Iterator, Array Aggregator, Error Handling, HTTP Request.

---

## Quick Start

1.  **Início de Cenário:** Acesse o painel do Make.com, navegue até "Scenarios" e selecione "Create a new scenario" para começar um novo fluxo de automação.
2.  **Configuração do Gatilho:** Adicione o primeiro módulo, que servirá como gatilho. Por exemplo, selecione "Webhooks" > "Custom webhook" para receber dados de uma fonte externa. Copie o URL gerado e envie um payload de teste (e.g., JSON com `{"nome": "Teste", "email": "teste@exemplo.com"}`) para que o Make detecte a estrutura dos dados.
3.  **Adição de Módulos de Ação:** Conecte módulos subsequentes ao gatilho. Se o objetivo é salvar dados em uma planilha, adicione "Google Sheets" > "Add a Row" e selecione a planilha e a aba de destino.
4.  **Mapeamento de Dados:** No módulo de ação do Google Sheets, arraste os campos detectados pelo Webhook (e.g., `{{1.nome}}`, `{{1.email}}`) para as colunas correspondentes na sua planilha.
5.  **Ativação e Teste:** Salve o cenário e ative o botão "ON". Execute o gatilho novamente com dados reais para confirmar se o fluxo funciona como esperado e os dados são processados corretamente.

---

## Core Workflows

### Workflow 1: Automatização de Captação de Leads de Formulário Web para Google Sheets e Notificação Slack

Este workflow detalha a captura de dados de um formulário web via webhook, salvando-os em uma planilha do Google Sheets e enviando uma notificação em tempo real para um canal do Slack.

1.  **Gatilho - Webhooks: Custom webhook:**
    *   **Propósito:** Receber dados HTTP POST de um formulário web (ex: WordPress com plugin de webhook, Typeform, etc.).
    *   **Configuração:**
        *   Adicione o módulo "Webhooks" e escolha "Custom webhook".
        *   Clique em "Add" para criar um novo webhook, nomeie-o como "LeadFormularioSite".
        *   Copie o "Webhook URL" gerado.
        *   **Teste Inicial:** Envie um POST request para este URL com um JSON payload de exemplo para que o Make detecte a estrutura dos dados.
            ```json
            {
              "nomeCompleto": "Fernanda Lima",
              "emailContato": "fernanda.lima@email.com",
              "telefoneContato": "+5511998877665",
              "origemLead": "Campanha Google Ads"
            }
            ```
        *   Confirme que o Make detectou os campos (`nomeCompleto`, `emailContato`, `telefoneContato`, `origemLead`).

2.  **Ação - Google Sheets: Add a Row:**
    *   **Propósito:** Salvar os dados do lead em uma linha nova em uma planilha Google Sheets.
    *   **Configuração:**
        *   Conecte o módulo "Google Sheets" e selecione "Add a Row".
        *   **Connection:** Selecione sua conexão Google existente.
        *   **Spreadsheet:** Busque e selecione a planilha onde os leads serão armazenados (e.g., "CRM - Leads Site").
        *   **Sheet Name:** Escolha a aba específica (e.g., "Leads Atuais").
        *   **Values:** Mapeie os campos do módulo Webhook (módulo 1) para as colunas da sua planilha:
            *   `Coluna A (Nome)`: `{{1.nomeCompleto}}`
            *   `Coluna B (Email)`: `{{1.emailContato}}`
            *   `Coluna C (Telefone)`: `{{1.telefoneContato}}`
            *   `Coluna D (Origem)`: `{{1.origemLead}}`
            *   `Coluna E (Data Recebimento)`: `{{formatDate(now; "YYYY-MM-DD HH:mm:ss")}}` (função Make para data/hora atual formatada).

3.  **Ação - Slack: Create a Message:**
    *   **Propósito:** Enviar uma notificação para um canal Slack sobre o novo lead.
    *   **Configuração:**
        *   Conecte o módulo "Slack" e selecione "Create a Message".
        *   **Connection:** Selecione sua conexão Slack.
        *   **Channel:** Escolha o canal de destino (e.g., "#leads-novos-negocios").
        *   **Text:** Crie a mensagem personalizada usando os dados do Webhook:
            ```
            ✨ Novo Lead Recebido! ✨
            Nome: {{1.nomeCompleto}}
            Email: {{1.emailContato}}
            Telefone: {{1.telefoneContato}}
            Origem: {{1.origemLead}}
            ```
        *   (Opcional) **As user:** Marque para que a mensagem apareça como sua conta Slack.

4.  **Finalização:** Salve o cenário e certifique-se de que o interruptor "ON" esteja ativado. Teste o formulário web real para confirmar o fluxo completo.

### Workflow 2: Sincronização Condicional de Dados de Clientes de CRM (Pipedrive) para Email Marketing (ActiveCampaign)

Este workflow demonstra como monitorar atualizações de contatos no Pipedrive, filtrar por uma condição específica e sincronizar apenas os contatos relevantes para uma lista no ActiveCampaign.

1.  **Gatilho - Pipedrive: Watch Persons (Instant Trigger):**
    *   **Propósito:** Ser notificado instantaneamente sobre qualquer criação ou atualização de "Person" (contato) no Pipedrive.
    *   **Configuração:**
        *   Adicione o módulo "Pipedrive" e escolha "Watch Persons".
        *   **Connection:** Selecione sua conexão Pipedrive.
        *   **Event:** Mantenha "New or Updated Person". O Make configurará um webhook no Pipedrive automaticamente.
        *   **Limit:** Defina um limite razoável (ex: 100) para o número máximo de itens processados por ciclo, se aplicável.

2.  **Ferramenta - Router:**
    *   **Propósito:** Criar ramificações lógicas para diferentes condições. Neste caso, uma rota para sincronizar com ActiveCampaign e outra (opcional) para outras ações.
    *   **Configuração:** Adicione o módulo "Router" após o módulo "Pipedrive".

3.  **Filtro - Verificar Condições para Sincronização:**
    *   **Propósito:** Permitir que o fluxo continue apenas para contatos que atendam a critérios específicos (e.g., ter um email válido e uma tag específica).
    *   **Configuração:**
        *   Na primeira rota do "Router", clique na linha entre o Router e o próximo módulo para adicionar um filtro.
        *   **Label:** "Email Válido e Tag Newsletter"
        *   **Conditions:**
            *   **Condition 1 (Email Válido):** `{{2.email.[].value}}` (campo do Pipedrive que pode ser um array de emails) **Existis (Operador)**.
            *   **Condition 2 (Tag Específica):** `{{2.tag}}` (o campo pode variar, pode ser `tags_id` ou `label` dependendo de como tags são expostas na saída do Pipedrive) **Contains (Operador)** `Newsletter`.
            *   **Logical operator:** `AND`.

4.  **Ação - ActiveCampaign: Upsert a Contact:**
    *   **Propósito:** Adicionar ou atualizar um contato no ActiveCampaign. "Upsert" garante que um novo contato seja criado se não existir, ou atualizado se já existir.
    *   **Configuração:**
        *   Conecte o módulo "ActiveCampaign" e selecione "Upsert a Contact".
        *   **Connection:** Selecione sua conexão ActiveCampaign.
        *   **Email:** `{{first(2.email.[].value)}}` (utiliza a função `first` para pegar o primeiro email do array, se houver).
        *   **First Name:** `{{2.first_name}}`
        *   **Last Name:** `{{2.last_name}}`
        *   **List:** Selecione a lista de destino (e.g., "Assinantes de Notícias").
        *   **Tags:** Adicione tags adicionais para categorização (e.g., `Pipedrive_Sync`).

5.  **Finalização:** Salve e ative o cenário. Teste criando ou atualizando um contato no Pipedrive com um email e a tag "Newsletter" para verificar a sincronização.

---

## Templates

### Módulo Webhook Customizado - Estrutura JSON para Lead Qualificado

Este template define uma estrutura JSON ideal para receber dados de um lead qualificado, incluindo campos para segmentação e enriquecimento.

```json
{
  "lead_id_externo": "FORM-WEB-12345",
  "nome_completo": "Carlos Eduardo Pereira",
  "email_contato": "carlos.pereira@exemplo.com.br",
  "telefone_principal": "+5511987654321",
  "empresa_nome": "Tech Solutions S.A.",
  "cargo_contato": "Gerente de TI",
  "origem_canal": "LinkedIn Ads",
  "data_envio_formulario": "2024-07-26T10:00:00Z",
  "interesses_produto": ["Automação", "Cloud Computing", "Segurança"],
  "score_lead": 75
}
```

### Função de Mapeamento de Itens (Map) e Agregação (Join) para Email

Este template demonstra como usar as funções `map` e `join` para formatar uma lista de itens (e.g., produtos de um pedido) em uma string legível para um e-mail ou documento.

*   **Cenário:** Você recebe um array de objetos `items` de um pedido (ex: `[{"name": "Produto A", "qty": 2, "price": 100}, {"name": "Produto B", "qty": 1, "price": 50}]`).
*   **Objetivo:** Gerar uma lista formatada como "2x Produto A (R$ 100.00)" para um e-mail de confirmação.

```
{{join(map(1.items; formatText("{{qty}}x {{name}} (R$ {{price}}.00)"); ); "\n")}}
```
*   **Explicação:**
    *   `1.items`: Assume que o array de itens está na saída do módulo 1.
    *   `map(1.items; ...)`: Itera sobre cada objeto no array `1.items`.
    *   `formatText("{{qty}}x {{name}} (R$ {{price}}.00)")`: Para cada item, constrói uma string formatada usando os campos `qty`, `name` e `price` de cada item.
    *   `join(...; "\n")`: Concatena todas as strings resultantes do `map`, separando cada uma por uma quebra de linha (`\n`), criando uma lista vertical.

---

## Checklist

- [x] O gatilho inicial do cenário está configurado corretamente e testado com dados válidos?
- [x] Todas as conexões de serviços (APIs) utilizadas estão ativas e com credenciais atualizadas?
- [x] O mapeamento de dados entre os módulos é preciso, evitando perdas ou erros de tipo?
- [x] Foram implementados filtros e roteadores para direcionar o fluxo de dados conforme a lógica de negócio?
- [x] O tratamento de erros (Error Handling) está configurado para módulos críticos, prevenindo interrupções?
- [x] O cenário foi exaustivamente testado com uma variedade de dados reais e casos de borda?
- [x] O agendamento do cenário (intervalo de execução) está otimizado para a frequência necessária e custos?
- [x] Variáveis, Data Stores ou Loops estão sendo utilizados de forma eficiente para lógica complexa?
- [x] As operações consumidas pelo cenário estão dentro do orçamento e limites da plataforma Make?
- [x] Existem logs ou mecanismos de alerta (e.g., Slack, Email) para monitorar falhas e execuções?

---

## Métricas de Referência

| Métrica | Benchmark (Ideal) | Meta (Aceitável) |
|---|---|---|
| Taxa de Sucesso de Execução | > 99.8% | > 98.5% |
| Latência Média do Cenário | < 300 ms | < 1.5 segundos |
| Custo por Operação (Médio) | < 0.003 USD | < 0.008 USD |
| Volume de Operações/Mês | Varia (Ex: 50k-5M) | Conforme demanda |
| Taxa de Erro Crítico | < 0.05% | < 0.2% |
| Tempo de Resolução de Erro | < 30 minutos | < 2 horas |

---

## Erros Comuns

1.  **Mapeamento Incorreto ou Ausência de Dados**: Campos não são passados corretamente entre os módulos, resultando em dados vazios ou incorretos nos sistemas de destino.
    *   **Como evitar**: Sempre utilize o "Run History" (Histórico de Execuções) para inspecionar a saída de cada módulo e verificar a estrutura exata dos dados. Use funções como `get()` para acessar propriedades aninhadas (`{{get(1.data; "cliente.endereco")}}`) ou `first()` para extrair um item de um array (`{{first(2.emails)}}`).
2.  **Loops Infinitos ou Execuções Duplicadas**: Cenários que disparam outros cenários ou atualizam registros no mesmo sistema que os originou podem criar ciclos, consumindo operações rapidamente.
    *   **Como evitar**: Implemente filtros rigorosos para condições específicas (ex: "se o `ID` do registro já foi processado"). Utilize `Data Stores` para manter um registro de IDs já processados ou timestamps de última execução. Exemplo de filtro: `{{2.last_modified_date}}` **Greater than** `{{get(data_store; "last_run_timestamp")}}`.
3.  **Exceder Limites de API (Rate Limits)**: Fazer muitas requisições para uma API em um curto período pode resultar em erros `429 Too Many Requests`.
    *   **Como evitar**: Use o módulo "Tools" > "Sleep" para inserir pausas estratégicas entre as chamadas de API. Configure o "Maximum number of concurrent executions" nas configurações do cenário para limitar execuções paralelas. Em módulos HTTP, marque a opção "Retry on rate limit errors" se disponível.

---

## Dicas Avançadas

1.  **Utilização Estratégica de Routers e Filtros**: Em vez de criar múltiplos cenários para diferentes condições, use um único cenário com um `Router` e `Filters` em cada rota. Isso centraliza a lógica, facilita a manutenção e otimiza o consumo de operações. Ex: Um webhook genérico pode rotear para "criar lead", "atualizar cliente" ou "notificar falha" com base em um campo `event_type` do payload.
2.  **`Array Aggregators` para Processamento em Lote**: Quando precisar processar múltiplos itens (ex: várias linhas de uma planilha, múltiplos itens de um pedido) em uma única operação para um sistema externo, utilize módulos `Array Aggregator` (como "Text Aggregator", "JSON Aggregator", "Numeric Aggregator"). Eles coletam dados de um `Iterator` e os agrupam, permitindo que um único módulo de ação subsequente envie um payload em lote, economizando operações e tempo.
3.  **`Data Stores` para Persistência e Controle de Estado**: Use `Data Stores` do Make para armazenar e recuperar dados personalizados e persistentes diretamente na plataforma. Ideal para manter contadores, registrar IDs de último processamento (`last_id`), armazenar configurações ou gerenciar o estado de fluxos complexos, eliminando a dependência de bancos de dados externos. Ex: Armazenar o `ID` do último email lido para evitar reprocessamento em gatilhos de polling.
4.  **Funções Personalizadas e Expressões Complexas**: Vá além do mapeamento simples. Utilize as funções embutidas do Make (`if()`, `switch()`, `map()`, `filter()`, `formatDate()`, `split()`, `replace()`, `parseJson()`, `json()`) para transformar, manipular e validar dados. `parseJson()` e `json()` são cruciais para trabalhar com strings JSON dinâmicas ou construir objetos JSON complexos. Ex: `{{if(1.score > 80; "High Priority"; "Normal")}}`.
5.  **Tratamento de Erros Robusto com `Error Handlers`**: Anexe `Error Handlers` (rotas de tratamento de erros) a módulos críticos ou a todo o cenário. Isso permite que o