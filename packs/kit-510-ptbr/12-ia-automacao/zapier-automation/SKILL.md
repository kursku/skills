---
name: zapier-automation
description: "Zapier Automation — Skill especializada para zapier automation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Zapier Automation

Esta skill capacita o Claude a criar, otimizar e depurar workflows de automação utilizando a plataforma Zapier, integrando mais de 5.000 aplicativos para fluxos de trabalho eficientes e sem código.

---

## Keywords

Zapier, Automação, Zaps, Triggers, Actions, Filters, Paths, Webhooks, Formatter, Delay, Looping, Code by Zapier, Webhooks by Zapier, Data Transfer, Integrations, Task History, Zap Editor, Multi-Step Zaps.

---

## Quick Start

1.  **Conectar Aplicativos Essenciais**: Acesse `My Apps` no Zapier e conecte suas contas de Google Sheets, Slack, Gmail e seu CRM principal (ex: Pipedrive, Salesforce) fornecendo as credenciais solicitadas.
2.  **Configurar o Primeiro Trigger**: Crie um novo Zap, selecione "Google Sheets" como app e "New Spreadsheet Row" como evento de trigger. Escolha uma planilha e uma aba específica para monitorar novas entradas.
3.  **Definir a Primeira Action**: Adicione um passo de "Action", selecione "Slack" como app e "Send Channel Message" como evento. Configure o canal de destino e um texto de mensagem simples como "Nova linha adicionada na planilha!"
4.  **Testar e Ativar o Zap**: Utilize o botão "Test Trigger" para buscar dados de uma linha existente e depois teste a "Action" do Slack. Verifique se a mensagem aparece no canal correto. Ative o Zap.
5.  **Monitorar o Histórico de Tarefas**: Navegue até "Task History" no Zapier para acompanhar as execuções do seu Zap, verificar sucessos, falhas e inspecionar os dados processados em cada etapa.

---

## Core Workflows

### Workflow 1: Automação Completa de Qualificação e Notificação de Leads de Formulário

Este workflow automatiza a captura de leads de um formulário online (Google Forms), qualifica-os com base em critérios específicos, envia dados para um CRM, notifica a equipe de vendas no Slack e adiciona o contato a uma lista de email marketing.

**Passos Detalhados:**

1.  **Trigger: Novo Envio de Formulário (Google Forms)**
    *   **App & Event**: Google Forms, "New Response in Spreadsheet".
    *   **Conta**: Selecione a conta Google Forms conectada.
    *   **Configuração**: Escolha a planilha específica onde as respostas do formulário são salvas e a aba onde os dados estão.
    *   **Teste**: Envie um formulário de teste para garantir que o Zapier consiga buscar os dados corretamente. Exemplo de dados: `{"Nome": "João Silva", "Email": "joao.silva@exemplo.com", "Empresa": "Tech Solutions", "Interesse": "Automação", "Cargo": "Diretor", "Orçamento": "Alto"}`.

2.  **Action: Filtrar Leads Qualificados (Filter by Zapier)**
    *   **App & Event**: Filter by Zapier, "Only continue if...".
    *   **Configuração**:
        *   Campo 1: `Interesse` (do Google Forms) `(Text) Contains` `Automação, Consultoria`.
        *   E
        *   Campo 2: `Orçamento` (do Google Forms) `(Text) Contains` `Alto, Médio`.
    *   **Exemplo**: Apenas leads com interesse em "Automação" ou "Consultoria" E orçamento "Alto" ou "Médio" prosseguirão. Leads com "Orçamento: Baixo" ou "Interesse: Suporte" serão ignorados neste fluxo.

3.  **Action: Criar/Atualizar Lead no CRM (Pipedrive)**
    *   **App & Event**: Pipedrive, "Find Person" (para evitar duplicatas) ou "Create Person".
    *   **Configuração**:
        *   **Find Person**: Use `Email` do formulário como campo de busca. Marque "Create Pipedrive Person if not found?".
        *   **Create Person (se não encontrado)**:
            *   `Name`: `{{Nome}}` (do Google Forms)
            *   `Email`: `{{Email}}` (do Google Forms)
            *   `Organization`: `{{Empresa}}` (do Google Forms)
            *   `Custom Field: Cargo`: `{{Cargo}}`
    *   **Exemplo**: Se "joao.silva@exemplo.com" já existir, o Zapier atualizará a pessoa; caso contrário, criará um novo contato com os dados fornecidos.

4.  **Action: Criar Negócio no CRM (Pipedrive)**
    *   **App & Event**: Pipedrive, "Create Deal".
    *   **Configuração**:
        *   `Title`: `Novo Lead - {{Nome}} - {{Empresa}}`
        *   `Person`: Selecione o ID da pessoa criada/encontrada no passo anterior.
        *   `Organization`: Selecione o ID da organização criada/encontrada no passo anterior.
        *   `Stage`: `Lead In`
        *   `Value`: (Opcional, pode ser mapeado de `Orçamento` ou um valor padrão)
    *   **Exemplo**: Um negócio intitulado "Novo Lead - João Silva - Tech Solutions" é criado e associado ao contato e empresa corretos no Pipedrive.

5.  **Action: Notificar Equipe de Vendas (Slack)**
    *   **App & Event**: Slack, "Send Channel Message".
    *   **Configuração**:
        *   `Channel`: `#leads-qualificados`
        *   `Message Text`:
            ```
            🔥 NOVO LEAD QUALIFICADO! 🔥
            Nome: {{Nome}}
            Email: {{Email}}
            Empresa: {{Empresa}}
            Interesse: {{Interesse}}
            Orçamento: {{Orçamento}}
            Ver no Pipedrive: [Link para o Negócio Criado no Pipedrive]
            ```
        *   `Send as a bot?`: Sim
        *   `Bot Name`: `LeadBot`
    *   **Exemplo**: Uma mensagem formatada é enviada para o canal `#leads-qualificados` com todos os detalhes importantes do lead e um link direto para o negócio no Pipedrive.

6.  **Action: Adicionar Contato à Lista de Email Marketing (Mailchimp)**
    *   **App & Event**: Mailchimp, "Add/Update Subscriber".
    *   **Configuração**:
        *   `Audience`: `Lista de Prospecção`
        *   `Email Address`: `{{Email}}` (do Google Forms)
        *   `First Name`: `{{Nome}}` (do Google Forms)
        *   `Tags`: `Lead Qualificado, {{Interesse}}`
        *   `Update Existing?`: Sim
    *   **Exemplo**: O email "joao.silva@exemplo.com" é adicionado ou atualizado na lista "Lista de Prospecção" do Mailchimp, com as tags "Lead Qualificado" e "Automação", pronto para receber campanhas segmentadas.

### Workflow 2: Processamento e Distribuição de Dados de Planilha para Múltiplas Ferramentas

Este workflow demonstra como pegar uma linha de dados de uma planilha, processá-la usando funções avançadas do Zapier e distribuir esses dados para diferentes ferramentas com base em condições, além de enviar um email personalizado.

**Passos Detalhados:**

1.  **Trigger: Nova Linha em Planilha (Google Sheets)**
    *   **App & Event**: Google Sheets, "New Spreadsheet Row".
    *   **Configuração**: Escolha a planilha `Contatos_Newsletter` e a aba `Novos_Cadastros`.
    *   **Exemplo de dados**: `{"Nome Completo": "Maria Oliveira", "Email": "maria.o@exemplo.com", "Segmento": "Marketing", "Data Cadastro": "2024-02-29", "Opt-in Newsletter": "Sim"}`.

2.  **Action: Formatar Nome e Email (Formatter by Zapier)**
    *   **App & Event**: Formatter by Zapier, "Text".
    *   **Transform 1 (Split Name)**:
        *   `Transform`: `Split Text`
        *   `Input`: `{{Nome Completo}}`
        *   `Separator`: ` ` (espaço)
        *   `Segment Index`: `First` para `Primeiro_Nome` e `Last` para `Sobrenome`.
    *   **Transform 2 (Lowercase Email)**:
        *   `Transform`: `Lowercase`
        *   `Input`: `{{Email}}`
        *   `Output`: `Email_Minusculo`
    *   **Exemplo**: "Maria Oliveira" vira `Primeiro_Nome: "Maria"`, `Sobrenome: "Oliveira"`. "maria.o@exemplo.com" vira `Email_Minusculo: "maria.o@exemplo.com"`.

3.  **Action: Lógica Condicional (Paths by Zapier)**
    *   **App & Event**: Paths by Zapier, "A/B Path".
    *   **Path A: Segmento Marketing**
        *   **Rule**: `Segmento` (do Google Sheets) `(Text) Exactly Matches` `Marketing`.
        *   **Ações dentro do Path A**:
            *   **Action A.1: Adicionar Contato ao ActiveCampaign (Marketing)**
                *   **App & Event**: ActiveCampaign, "Create/Update Contact".
                *   **Configuração**:
                    *   `Email`: `{{Email_Minusculo}}` (do Formatter)
                    *   `First Name`: `{{Primeiro_Nome}}` (do Formatter)
                    *   `Last Name`: `{{Sobrenome}}` (do Formatter)
                    *   `Tags`: `Newsletter, Marketing`
                    *   `List`: `Lista Marketing`
            *   **Action A.2: Notificar Gerente de Marketing (Gmail)**
                *   **App & Event**: Gmail, "Send Email".
                *   **Configuração**:
                    *   `To`: `gerente.marketing@empresa.com`
                    *   `Subject`: `Novo Contato Marketing: {{Primeiro_Nome}} {{Sobrenome}}`
                    *   `Body`: `Olá Gerente, um novo contato de marketing se cadastrou: {{Email_Minusculo}}`
    *   **Path B: Outros Segmentos**
        *   **Rule**: `Segmento` (do Google Sheets) `(Text) Does Not Exactly Match` `Marketing`.
        *   **Ações dentro do Path B**:
            *   **Action B.1: Adicionar Contato ao ActiveCampaign (Geral)**
                *   **App & Event**: ActiveCampaign, "Create/Update Contact".
                *   **Configuração**:
                    *   `Email`: `{{Email_Minusculo}}`
                    *   `First Name`: `{{Primeiro_Nome}}`
                    *   `Last Name`: `{{Sobrenome}}`
                    *   `Tags`: `Newsletter, Geral`
                    *   `List`: `Lista Geral`
            *   **Action B.2: Adicionar Tarefa para CRM (Pipedrive)**
                *   **App & Event**: Pipedrive, "Create Activity".
                *   **Configuração**:
                    *   `Subject`: `Revisar Novo Contato: {{Primeiro_Nome}} {{Sobrenome}}`
                    *   `Type`: `Tarefa`
                    *   `Due Date`: `+3 days` (usando modificador de data)
                    *   `Assigned To`: `ID do Usuário Padrão`
                    *   `Note`: `Email: {{Email_Minusculo}}, Segmento: {{Segmento}}`
    *   **Exemplo**: Se o `Segmento` for "Marketing", o contato vai para a "Lista Marketing" no ActiveCampaign e o gerente é notificado. Se for qualquer outro segmento, vai para a "Lista Geral" e uma tarefa de revisão é criada no Pipedrive.

---

## Templates

### Template de Mensagem de Boas-Vindas Personalizada para Slack

```
🎉 Novo membro na equipe de Vendas! 🎉
Seja bem-vindo(a), {{Primeiro Nome}} {{Sobrenome}}! 👋
Cargo: {{Cargo}}
Email Corporativo: {{Email Corporativo}}
Gerente Direto: {{Nome do Gerente}}
Data de Início: {{Data de Início (formato AAAA-MM-DD)}}
Por favor, deem as boas-vindas e ajudem o(a) {{Primeiro Nome}} a se integrar!
```

### Template de Requisição HTTP POST para Webhook Personalizado (JSON)

```json
{
  "event": "novo_pedido_ecommerce",
  "data": {
    "pedido_id": "{{id_do_pedido_ecommerce}}",
    "cliente": {
      "nome": "{{nome_do_cliente_ecommerce}}",
      "email": "{{email_do_cliente_ecommerce}}",
      "telefone": "{{telefone_do_cliente_ecommerce}}"
    },
    "itens": [
      {
        "sku": "{{sku_item_1}}",
        "nome": "{{nome_item_1}}",
        "quantidade": "{{quantidade_item_1}}",
        "preco_unitario": "{{preco_item_1}}"
      },
      {
        "sku": "{{sku_item_2}}",
        "nome": "{{nome_item_2}}",
        "quantidade": "{{quantidade_item_2}}",
        "preco_unitario": "{{preco_item_2}}"
      }
    ],
    "valor_total": "{{valor_total_do_pedido}}",
    "status": "processando",
    "data_hora_pedido": "{{data_hora_do_pedido}}"
  },
  "source": "Zapier Ecommerce Integration"
}
```

---

## Checklist

-   [ ] Conectar todas as contas de aplicativos necessárias no Zapier (CRM, Email Marketing, Comunicação, Planilhas).
-   [ ] Testar cada passo do Zap individualmente após a configuração para validar a transferência e transformação dos dados.
-   [ ] Configurar filtros (`Filter by Zapier`) para garantir que apenas os dados relevantes continuem no fluxo de automação.
-   [ ] Utilizar o `Formatter by Zapier` para padronizar formatos de dados (texto, números, datas) antes de enviar para aplicativos de destino.
-   [ ] Implementar `Paths by Zapier` para criar lógicas condicionais complexas e ramificar o fluxo de automação com base em diferentes cenários.
-   [ ] Considerar o uso de `Delay by Zapier` para cadências de follow-up ou para aguardar a sincronização de dados entre sistemas.
-   [ ] Configurar notificações de erro (via Slack, Email) para Zaps críticos, garantindo que falhas sejam rapidamente identificadas e corrigidas.
-   [ ] Revisar o `Task History` regularmente para monitorar a saúde dos Zaps, identificar gargalos ou erros recorrentes e otimizar o consumo de tarefas.
-   [ ] Documentar a finalidade, os aplicativos envolvidos e a lógica de cada Zap complexo para facilitar a manutenção e a colaboração da equipe.
-   [ ] Definir limites de uso e orçamentos para tarefas do Zapier, evitando surpresas com custos e garantindo a escalabilidade.

---

## Métricas de Referência

| Métrica                         | Benchmark     | Meta          |
|---------------------------------|---------------|---------------|
| Taxa de Sucesso de Tarefas      | > 99.5%       | > 99.9%       |
| Tempo Médio de Processamento    | 2-5 segundos  | < 2 segundos  |
| Custo por Automação (mensal)    | US$ 0.01-0.05 | US$ 0.005-0.02|
| Redução de Tempo Manual         | 20%-80%       | > 50%         |
| Zaps Ativos por Equipe/Mês      | 5-15          | 15-30+        |
| Erros de Tarefa por Mês         | < 0.5%        | < 0.1%        |

---

## Erros Comuns

1.  **Credenciais de Aplicativos Expiradas ou Inválidas**: Isso impede que o Zapier se conecte aos seus aplicativos e execute as ações.
    *   **Como evitar**: Sempre que um Zap falhar com erro de autenticação, vá em `My Apps` e reconecte o aplicativo. Para integrações críticas, considere usar tokens de API ou chaves de serviço de longa duração, se disponíveis. Exemplo: Se o Zapier não consegue postar no Slack, verifique se o token de acesso da sua conta Slack não foi revogado ou expirou.

2.  **Dados Incompatíveis ou Ausentes entre Passos**: Tentativa de mapear um campo numérico para um campo de texto que espera uma string, ou um campo obrigatório que está vazio.
    *   **Como evitar**: Utilize o `Formatter by Zapier` para garantir que os dados estejam no formato correto (ex: `Text` para formatar números como strings, `Date/Time` para converter formatos de data). Mapeie campos cuidadosamente, testando cada passo. Exemplo: Tentar enviar um `Preço Total (numérico)` para um campo `Descrição (texto)` em outro app sem conversão pode gerar erros ou dados ilegíveis.

3.  **Loop Infinito ou Consumo Excessivo de Tarefas**: Um Zap que desencadeia outro Zap, ou o mesmo Zap, criando um ciclo sem fim de execuções.
    *   **Como evitar**: Seja extremamente cauteloso ao criar Zaps bidirecionais (A atualiza B, e B atualiza A). Use `Filters by Zapier` para verificar se os dados já foram processados ou se a mudança foi iniciada pelo próprio Zapier. Exemplo: Um Zap que monitora uma planilha para novas linhas e, ao adicionar uma linha, outro Zap é ativado para adicionar uma linha na mesma planilha. Adicione um filtro que verifica se o campo `Status` da linha é `Processado por Zapier` antes de permitir a continuação.

---

## Dicas Avançadas

1.  **Uso Estratégico de `Webhooks by Zapier`**: Para integração com APIs personalizadas ou sistemas legados que não possuem um conector nativo no Zapier, utilize "Webhooks by Zapier". Configure um "Catch Hook" para receber dados de sistemas externos e um "Custom Request" para enviar dados via POST/GET/PUT/DELETE. Isso é ideal para disparar fluxos de automação a partir de eventos em sistemas internos ou para consumir dados de APIs complexas. Exemplo: Criar um Catch Hook para receber notificações de pagamento de um gateway de pagamento personalizado e, em seguida, usar um Custom Request para atualizar o status do pedido em um sistema ERP interno via API.

2.  **Lógica Complexa com `Code by Zapier` (Python/JavaScript)**: Para transformações de dados que vão além do `Formatter`, ou para fazer múltiplas chamadas de API encadeadas dentro de um único passo, use a funcionalidade "Code by Zapier". Isso permite escrever pequenos snippets de código Python ou JavaScript.
    *   **Exemplo (Python)**: Calcular impostos ou descontos complexos, ou combinar múltiplos campos em uma string JSON formatada de forma específica antes de enviar para um webhook.
    ```python
    # Entrada: input_data = {"valor_bruto": 100.0, "desconto_percentual": 0.1, "taxa_imposto": 0.15}
    valor_liquido = input_data['valor_bruto'] * (1 - input_data['desconto_percentual'])
    valor_final = valor_liquido * (1 + input_data['taxa_imposto'])
    output = {"valor_final_com_imposto": round(valor_final, 2)}
    ```

3.  **Encadeamento de Zaps e `Storage by Zapier` para Persistência**: Para fluxos de trabalho muito longos ou que precisam de um "estado" persistente, divida-os em vários Zaps e use `Storage by Zapier` para armazenar e recuperar informações entre eles. `Storage` pode ser usado como um contador, um indicador de status ou para guardar chaves de API temporárias.
    *   **Exemplo**: Um Zap 1 recebe um evento e armazena um `contador_leads_mes` no Storage. Um Zap 2, disparado por um cronograma, lê esse contador, envia um relatório e o zera no final do mês.

4.  **Uso de `Delay by Zapier` para Cadências e Follow-ups**: Em vez de disparar todas as ações instantaneamente, use o "Delay" para criar cadências de comunicação ou aguardar por um evento externo. Isso é crucial para fluxos de nutrição de leads ou sequências de onboarding.
    *   **Exemplo**: Após um novo lead se inscrever, use "Delay For" por `3 days`, depois envie um email de follow-up. Se o lead não responder, use outro "Delay For" por `5 days` e crie uma tarefa para o vendedor ligar.

5.  **Re-run Tasks e Replay para Depuração Eficaz**: Se um Zap falhar, em vez de recriar o cenário, vá para `Task History`, localize a tarefa falha, inspecione os dados e o erro, corrija o problema no Zap (ex: mapeamento, credenciais) e use `Re-run` ou `Replay` para tentar executar a tarefa novamente com os mesmos dados. Isso economiza tempo valioso na depuração.