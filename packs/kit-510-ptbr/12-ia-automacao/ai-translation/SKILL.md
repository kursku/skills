---
name: ai-translation
description: "Ai Translation — Skill especializada para ai translation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Ai Translation

Esta skill capacita o Claude a projetar, implementar e otimizar fluxos de trabalho de tradução automatizada usando APIs de IA e ferramentas de automação.

---

## Keywords

NMT, CAT Tools, LLM translation, API translation, localization, MTPE, prompt engineering, linguistic quality assurance, neural machine translation, domain adaptation, glossary management, context preservation, webhook integration, DeepL API, Google Cloud Translation, OpenAI GPT, Make.com, N8N.

---

## Quick Start

1.  **Obtenha Chaves de API**: Adquira chaves de API para um serviço de tradução como DeepL (ex: `dl_auth_key_xxxxxxxxxxxxxxxxxxxxxx`) ou Google Cloud Translation.
2.  **Configure um Cliente HTTP**: Utilize `curl` ou uma ferramenta como Postman para testar a conectividade básica com a API de tradução.
3.  **Envie um Texto Simples**: Faça uma requisição POST com um texto em português para ser traduzido para o inglês.
4.  **Analise a Resposta**: Verifique o JSON retornado para extrair a tradução e identificar possíveis erros.
5.  **Integre em um Script Básico**: Crie um script Python ou Node.js para automatizar o envio de alguns parágrafos para tradução.

---

## Core Workflows

### Workflow 1: Tradução Automatizada de Conteúdo Web via API e Webhook (Make/N8N)

Este workflow detalha a automação da tradução de novos artigos de blog ou páginas de produto assim que são publicados ou atualizados, utilizando um webhook e uma API de tradução.

**Passo 1: Configuração do Webhook de Origem**
Um evento em um CMS (ex: WordPress, Shopify) dispara um webhook POST contendo os dados do novo conteúdo.
*   **Exemplo de Payload JSON (CMS para Webhook):**
    ```json
    {
      "event_type": "post_published",
      "post_id": "54321",
      "title": "Guia Completo para Automação de Marketing",
      "content_html": "<p>Neste artigo, exploramos as estratégias mais eficazes para alavancar a automação de marketing...</p>",
      "source_lang": "pt",
      "target_languages": ["en", "es"],
      "author": "Marketing Team"
    }
    ```
*   **Configuração no Make.com/N8N:**
    *   Módulo "Webhooks" > "Custom webhook".
    *   Copie o URL do webhook fornecido.

**Passo 2: Pré-processamento e Segmentação no Make/N8N**
Antes de enviar para a API de tradução, o HTML é limpo e segmentado para otimização e tratamento de placeholders.
*   **Ações no Make/N8N:**
    *   **Módulo "Text Parser" ou "Code (JS/Python)":**
        *   **Remoção de Tags Indesejadas:** Remover `<script>`, `<style>`, atributos `class`, `id`.
        *   **Extração de Conteúdo:** Isolar o texto principal do `content_html`.
        *   **Segmentação:** Dividir o texto em parágrafos ou frases para enviar à API em blocos menores (geralmente mais eficiente e preciso).
        *   **Identificação de Placeholders:** Substituir elementos como `{{nome_cliente}}` ou `[CALL_TO_ACTION_BTN]` por marcadores temporários (ex: `__PLACEHOLDER_1__`) para evitar tradução indesejada.
*   **Exemplo de Prompt para LLM (se usado para limpeza):**
    ```
    Remova todas as tags HTML e JavaScript do texto abaixo, mantendo apenas o conteúdo textual puro. Mantenha os parágrafos separados por duas quebras de linha. Identifique e preserve qualquer texto entre {{ }} como um placeholder.

    Texto:
    "<h1>Título do Artigo</h1><script>alert('oi');</script><p>Olá, {{nome_do_cliente}}! Este é um parágrafo. <img src='img.jpg'> Mais texto aqui.</p>"

    Saída Esperada:
    Título do Artigo

    Olá, {{nome_do_cliente}}! Este é um parágrafo. Mais texto aqui.
    ```

**Passo 3: Chamada à API de Tradução (DeepL Pro)**
Iterar sobre os idiomas alvo e os segmentos de texto, enviando cada um para a API de tradução.
*   **Módulo no Make/N8N:** "HTTP" > "Make a request" ou módulo específico do DeepL.
*   **Exemplo de Requisição (DeepL API):**
    ```http
    POST https://api-free.deepl.com/v2/translate
    Headers:
      Authorization: DeepL-Auth-Key YOUR_DEEPL_AUTH_KEY
      Content-Type: application/json
    Body:
    {
      "text": ["Neste artigo, exploramos as estratégias mais eficazes para alavancar a automação de marketing.", "Descubra como otimizar suas campanhas e gerar leads qualificados."],
      "source_lang": "PT",
      "target_lang": "EN",
      "split_sentences": "1",
      "tag_handling": "html",
      "formality": "less"
    }
    ```
*   **Tratamento de Múltiplos Idiomas:** Usar um iterador no Make/N8N para processar cada idioma em `target_languages`.

**Passo 4: Pós-processamento e Reconstrução**
Após receber as traduções, remontar o texto, reinserir placeholders e formatar para o destino.
*   **Ações no Make/N8N:**
    *   **Remontagem:** Unir os segmentos traduzidos.
    *   **Reinserção de Placeholders:** Substituir `__PLACEHOLDER_1__` de volta para `{{nome_cliente}}`.
    *   **Reconstrução HTML:** Reaplicar as tags HTML originais ou gerar um novo HTML/Markdown.

**Passo 5: Armazenamento/Publicação do Conteúdo Traduzido**
Enviar o conteúdo traduzido para o CMS de destino, banco de dados ou outro sistema.
*   **Módulo no Make/N8N:** "HTTP" > "Make a request" (para API do CMS) ou módulos específicos (ex: WordPress > "Create a Post").
*   **Exemplo de Payload (para CMS de destino):**
    ```json
    {
      "post_id": "54321",
      "language": "en",
      "title": "Complete Guide to Marketing Automation",
      "content_html": "<p>In this article, we explore the most effective strategies to leverage marketing automation...</p>",
      "status": "draft"
    }
    ```

### Workflow 2: Tradução Orientada a Glossário com LLM para Localização de Produtos

Este workflow foca em garantir a consistência terminológica e o tom de voz em traduções de materiais de produto (interfaces de usuário, manuais), utilizando um LLM e um glossário.

**Passo 1: Criação e Gestão de Glossário Terminológico**
Desenvolver um glossário detalhado com termos específicos da empresa/produto e suas traduções preferenciais.
*   **Formato:** CSV, JSON ou uma base de dados interna.
*   **Exemplo de Entrada de Glossário:**
    *   `Source: "Dashboard", Target (PT): "Painel de Controle"`
    *   `Source: "Feature", Target (PT): "Funcionalidade"`
    *   `Source: "Onboarding", Target (PT): "Integração de Usuários"`
    *   `Source: "Cloud Computing", Target (PT): "Computação em Nuvem"`

**Passo 2: Preparação do Prompt para LLM (Claude 3 Opus/GPT-4)**
O prompt é construído para instruir a LLM a usar o glossário e adotar uma persona específica para a tradução.
*   **Componentes do Prompt:**
    *   **Persona:** "Você é um tradutor sênior da equipe de localização da [Nome da Empresa X], especializado em software SaaS."
    *   **Instruções de Tradução:** "Traduza o texto do [idioma_fonte] para o [idioma_alvo]. Mantenha a concisão, clareza e o tom formal/informal (conforme definido). Utilize estritamente o glossário fornecido."
    *   **Inclusão do Glossário:** O glossário é inserido diretamente no prompt ou referenciado.
    *   **Contexto Adicional:** Informações sobre o tipo de texto (UI, manual, marketing).

**Passo 3: Execução da Tradução via API da LLM**
O texto-fonte e o prompt são enviados para a API da LLM.
*   **Exemplo de Chamada de API (OpenAI/Anthropic):**
    ```python
    # Usando a biblioteca 'anthropic' para Claude
    import anthropic

    client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")

    glossary = """
    - "Dashboard": "Painel de Controle"
    - "Feature": "Funcionalidade"
    - "Onboarding": "Integração de Usuários"
    - "Cloud Computing": "Computação em Nuvem"
    - "User Experience": "Experiência do Usuário"
    """

    source_text = "Our new Dashboard features enhanced Cloud Computing capabilities. The onboarding process ensures a smooth User Experience."
    source_lang = "English"
    target_lang = "Brazilian Portuguese"
    tone = "formal e técnico"

    prompt_template = f"""
    Você é um tradutor sênior da equipe de localização da TechSolutions, especializado em software SaaS.
    Sua tarefa é traduzir o texto a seguir do {source_lang} para o {target_lang}.
    Mantenha um tom {tone} e seja extremamente preciso.
    É MANDATÓRIO que você utilize o seguinte glossário para os termos específicos:
    {glossary}

    Texto a Traduzir:
    {source_text}

    Tradução:
    """

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt_template}
        ]
    )
    print(message.content)
    ```

**Passo 4: Revisão Humana (Machine Translation Post-Editing - MTPE)**
Um linguista nativo do idioma alvo revisa a saída da LLM, corrigindo erros de fluência, terminologia ou adequação cultural.
*   **Ferramentas:** CAT Tools (SDL Trados, MemoQ) com integração de MT.
*   **Foco da Revisão:**
    *   **Terminologia:** Conformidade com o glossário.
    *   **Coerência:** Manutenção do contexto e fluxo.
    *   **Fluência:** Sonoridade natural para o público.
    *   **Adequação Cultural:** Expressões e referências apropriadas.

**Passo 5: Feedback e Iteração Contínua**
As correções da MTPE são usadas para refinar o glossário e ajustar o prompt da LLM.
*   **Ações:**
    *   Atualizar o glossário com termos novos ou revisados.
    *   Modificar as instruções do prompt para abordar padrões de erro recorrentes.
    *   Coletar feedback qualitativo dos revisores para melhoria contínua.

---

## Templates

### Prompt para Tradução Contextual com Glossário (Claude/GPT)

```
Você é um tradutor especialista para a indústria de Fintech.
Seu objetivo é traduzir o texto a seguir do Inglês para o Português do Brasil, mantendo um tom formal, técnico e preciso, adequado para documentação de APIs e termos de serviço.
É crucial que você siga ESTRITAMENTE o glossário fornecido para garantir a consistência terminológica.

Glossário Obrigatório:
- "API Key": "Chave de API"
- "Endpoint": "Ponto de Acesso"
- "Rate Limit": "Limite de Requisições"
- "Wallet": "Carteira Digital"
- "KYC (Know Your Customer)": "Identificação de Cliente"
- "Transaction Ledger": "Livro Razão de Transações"

Contexto Adicional: O texto é parte da documentação técnica para desenvolvedores que integram nossa plataforma de pagamentos.

Texto a Traduzir:
"To access our services, you must obtain an API Key. Be aware of the Rate Limit on each Endpoint. Users can manage their funds in their digital Wallet, but KYC verification is required for certain operations. All transactions are recorded in the Transaction Ledger."

Tradução:
```

### Configuração de Webhook para Tradução Automatizada (Make/N8N)

```json
{
  "url": "https://hook.eu1.make.com/your_unique_webhook_id",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "X-CMS-Secret": "your_secure_cms_secret_token"
  },
  "body": {
    "document_id": "PRD-SPEC-V2.1",
    "document_type": "product_specification",
    "source_language": "en",
    "target_languages": ["pt-BR", "fr", "de"],
    "content": {
      "title": "Product Specification for Quantum Leap Device",
      "sections": [
        {
          "id": "intro",
          "heading": "Introduction",
          "text_html": "<p>This document details the technical specifications of the Quantum Leap Device.</p>"
        },
        {
          "id": "features",
          "heading": "Key Features",
          "text_html": "<ul><li>Real-time data synchronization</li><li>Low latency communication</li></ul>"
        }
      ]
    },
    "metadata": {
      "author": "Engineering Team",
      "version": "2.1",
      "priority": "high"
    }
  }
}
```

---

## Checklist

- [X] Selecionar a API de tradução adequada (DeepL, Google, OpenAI, AWS Translate, etc.) com base em custo, qualidade e recursos.
- [X] Configurar e gerenciar chaves de API de forma segura (variáveis de ambiente, gerenciadores de segredos).
- [X] Definir claramente os idiomas fonte e alvo, incluindo variantes regionais (ex: `pt-BR`, `es-MX`).
- [X] Implementar um estágio de pré-processamento para limpeza de texto, segmentação e tratamento de placeholders.
- [X] Criar e manter glossários terminológicos específicos do domínio ou da empresa.
- [X] Desenvolver prompts otimizados para LLMs, incluindo instruções de persona, tom e glossário.
- [X] Implementar mecanismos de tratamento de erros e retries com backoff exponencial para chamadas de API.
- [X] Planejar a pós-edição (MTPE) para controle de qualidade linguística e cultural em conteúdos críticos.
- [X] Monitorar os custos e o uso das APIs de tradução para evitar surpresas no orçamento.
- [X] Testar o fluxo de ponta a ponta com diferentes tipos e volumes de conteúdo.

---

## Métricas de Referência

| Métrica                      | Benchmark (Bom) | Meta (Excelente) |
|------------------------------|-----------------|------------------|
| **BLEU Score (Qualidade MT)**| 40-60           | >60              |
| **TER Score (Esforço MTPE)** | 10-25%          | <10%             |
| **Custo por Milhão de Caracteres** | $15-$30         | <$15             |
| **Latência da API (Texto Curto)** | <500ms          | <200ms           |
| **Taxa de Aceitação MTPE**   | >85%            | >95%             |
| **Economia de Tempo (vs. Humana)** | 30-60%          | >70%             |

---

## Erros Comuns

1.  **Ignorar o Contexto ou Segmentação Inadequada**: Traduzir frases isoladas ou blocos muito grandes pode levar a perdas de contexto e traduções incoerentes, ou exceder limites de tokens da API.
    *   **Como evitar**: Implementar segmentação inteligente por parágrafos ou frases. Para LLMs, enviar blocos de texto contextuais maiores ou passar contexto adicional no prompt, mesmo que o texto principal seja menor.
2.  **Não Utilizar Glossários ou Memórias de Tradução**: Resulta em inconsistência terminológica, especialmente em nomes de produtos, termos técnicos e branding, exigindo maior esforço de pós-edição.
    *   **Como evitar**: Desenvolver e integrar glossários rigorosamente no processo de tradução (via recursos da API, como o DeepL Glossaries, ou diretamente no prompt da LLM). Para traduções repetitivas, considere Memory Translation (TM) como uma camada prévia à MT.
3.  **Configuração Inadequada de Idiomas ou Variantes**: Usar `es` em vez de `es-MX` pode resultar em traduções culturalmente inapropriadas para o público-alvo.
    *   **Como evitar**: Sempre especificar o código de idioma completo com a variante regional (ex: `pt-BR`, `en-US`, `es-ES`). Validar a lista de códigos suportados pela API.
4.  **Tratar Conteúdo Dinâmico como Texto Estático**: Variáveis, URLs, códigos ou nomes próprios são traduzidos incorretamente ou corrompidos pela MT.
    *   **Como evitar**: Utilizar placeholders (ex: `{{USER_NAME}}`, `[LINK_TO_DOCS]`) antes da tradução e reinseri-los após. Muitos serviços de MT e LLMs suportam `tag_handling` para HTML ou XML.

---

## Dicas Avançadas

1.  **Adaptação de Domínio com LLMs**: Para nichos altamente especializados ou com vocabulário proprietário, considere usar LLMs para gerar "dados sintéticos" de tradução com base em glossários existentes para criar um modelo de tradução mais ajustado ao seu domínio, ou para fazer fine-tuning em modelos menores.
2.  **Tradução Zero-Shot com LLMs Multilingues para Idiomas de Baixos Recursos**: Em vez de APIs de MT tradicionais, utilize LLMs avançadas como Claude 3 Opus ou GPT-4 para traduzir idiomas com menos recursos (low-resource languages) ou para tarefas que exigem nuances culturais e criatividade, como marketing e transcriação. O prompt se torna a chave.
3.  **Processamento em Lotes Assíncrono para Grandes Volumes**: Para traduzir grandes volumes de documentos, implemente uma arquitetura de mensagens (ex: AWS SQS, RabbitMQ) onde os documentos são adicionados a uma fila, processados em lotes por workers em segundo plano e os resultados são armazenados ou notificados, evitando timeouts e gerenciando limites de taxa da API de forma eficiente.
4.  **Enriquecimento Pós-Tradução com NLP**: Após a tradução, aplique ferramentas de Processamento de Linguagem Natural (NLP) para realizar verificações adicionais, como análise de sentimento, extração de entidades nomeadas (NER) ou classificação de tópicos, garantindo que o significado e o tom original foram preservados e que não há vieses indesejados na tradução.
5.  **Detecção de Idioma Dinâmica**: Em vez de assumir o idioma fonte, use APIs de detecção de idioma (ex: Google Cloud Natural Language, AWS Comprehend) para identificar automaticamente o idioma de entrada antes de enviar para a tradução, aumentando a robustez do workflow para conteúdo de fontes diversas.