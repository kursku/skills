---
name: prompt-engineering
description: "Prompt Engineering — Skill especializada para prompt engineering"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Prompt Engineering

Esta skill capacita o Claude a criar, refinar e otimizar prompts para modelos de linguagem grandes, visando automação de tarefas e integração via APIs em plataformas como Make, N8N e Zapier.

---

## Keywords

Engenharia de Prompt, LLM, Automação, Make.com, N8N, Zapier, API REST, Webhooks, Few-Shot Prompting, Chain-of-Thought, System Prompt, Persona AI, JSON Output, LangChain.

---

## Quick Start

1.  **Defina Persona e Formato de Saída**: Comece todo prompt estabelecendo a identidade do LLM (ex: "Você é um especialista em marketing digital") e o formato de resposta desejado (ex: "Responda em JSON").
2.  **Use Exemplos (Few-Shot)**: Forneça 2-3 pares de entrada/saída para guiar o modelo, mesmo para tarefas simples como "Traduza 'Olá' para 'Hello'".
3.  **Restrições Explícitas**: Inclua limitações claras como "A resposta não deve exceder 50 palavras" ou "Utilize apenas termos técnicos de TI".
4.  **Teste em Ambiente Real**: Integre o prompt inicial em um fluxo de automação (ex: Make.com) e observe o comportamento em diferentes cenários de entrada.
5.  **Iteração com Feedback**: Analise as saídas, identifique falhas e ajuste o prompt adicionando novas instruções, exemplos ou refinando a persona.

---

## Core Workflows

### Workflow 1: Geração de Rascunho de Artigo para Blog via API (Make.com)

Este workflow detalha a criação e otimização de um prompt para gerar rascunhos de artigos de blog, integrando o LLM a um fluxo de automação que pode ser ativado por um webhook ou agendamento.

**Passo 1: Definição da Persona e Contexto Operacional**
*   **Ação**: Instrua o LLM a adotar uma persona específica e compreenda o contexto de sua operação em um fluxo de automação.
*   **Exemplo de System Prompt**:
    ```
    Você é um redator de conteúdo sênior especializado em SEO e marketing digital. Sua tarefa é gerar rascunhos de artigos de blog a partir de títulos fornecidos. O conteúdo deve ser otimizado para legibilidade, engajamento e SEO. Você opera em um ambiente de automação onde as entradas são concisas e as saídas precisam ser estruturadas para processamento posterior.
    ```

**Passo 2: Construção do Prompt Few-Shot com Chain-of-Thought e Formato JSON**
*   **Ação**: Crie um prompt que inclua exemplos (few-shot), instrua o LLM a pensar passo a passo (chain-of-thought) e defina um formato de saída JSON rigoroso para fácil parseamento no Make.com.
*   **Prompt Real**:
    ```
    **Instruções**:
    Você é um redator de conteúdo sênior especializado em SEO e marketing digital. Gere um rascunho de artigo de blog completo a partir do título fornecido, seguindo a estrutura especificada. O artigo deve ser entre 800 e 1000 palavras, otimizado para SEO, com um tom informativo e envolvente. Inclua introdução, 3-4 seções principais com subtítulos, e uma conclusão.

    **Exemplo de Entrada (Título)**: "As 5 Melhores Ferramentas de Automação para Marketing Digital em 2024"

    **Exemplo de Saída (JSON)**:
    ```json
    {
      "titulo": "As 5 Melhores Ferramentas de Automação para Marketing Digital em 2024",
      "slug": "melhores-ferramentas-automacao-marketing-2024",
      "introducao": "No cenário dinâmico do marketing digital, a automação tornou-se um pilar essencial...",
      "secoes": [
        {
          "subtitulo": "1. Make.com: Flexibilidade e Integração Total",
          "conteudo": "Make (anteriormente Integromat) destaca-se pela sua interface visual intuitiva...",
          "palavras_chave": ["Make.com", "automação marketing", "integração"]
        },
        {
          "subtitulo": "2. ActiveCampaign: CRM e Automação de E-mail Marketing",
          "conteudo": "Para quem busca uma solução robusta de e-mail marketing e CRM, ActiveCampaign é ideal...",
          "palavras_chave": ["ActiveCampaign", "email marketing", "CRM"]
        },
        {
          "subtitulo": "3. Zapier: A Ponte para Milhares de Aplicações",
          "conteudo": "Zapier é a ferramenta mais conhecida para conectar aplicativos e automatizar fluxos...",
          "palavras_chave": ["Zapier", "integração apps", "automação"]
        },
        {
          "subtitulo": "4. Semrush: SEO e Automação de Conteúdo",
          "conteudo": "Embora conhecido por SEO, Semrush oferece recursos para automatizar a pesquisa de palavras-chave e análise de conteúdo...",
          "palavras_chave": ["Semrush", "SEO", "marketing de conteúdo"]
        }
      ],
      "conclusao": "A escolha da ferramenta certa depende das suas necessidades...",
      "cta": "Quer otimizar suas campanhas? Clique aqui para conhecer nossos planos de consultoria!"
    }
    ```

    **Pense passo a passo**:
    1.  Entender o título e as palavras-chave implícitas.
    2.  Estruturar o artigo com introdução, 3-4 seções e conclusão.
    3.  Para cada seção, identificar um subtítulo relevante e desenvolver o conteúdo, incluindo palavras-chave secundárias.
    4.  Garantir que o tom de voz seja informativo e envolvente.
    5.  Formatar a saída estritamente como JSON, conforme o exemplo.

    **Título para o Artigo**: "Como a Inteligência Artificial Transforma a Gestão de Projetos"
    ```

**Passo 3: Integração no Make.com via Módulo HTTP (Make a request)**
*   **Ação**: Configure o módulo HTTP no Make.com para enviar o prompt ao endpoint da API do Claude, passando o título do artigo como parte do corpo da requisição.
*   **Configuração de Módulo HTTP (Make a request)**:
    *   **URL**: `https://api.anthropic.com/v1/messages` (ou outro endpoint LLM)
    *   **Method**: `POST`
    *   **Headers**:
        *   `x-api-key`: `{{sua_chave_api}}`
        *   `anthropic-version`: `2023-06-01`
        *   `content-type`: `application/json`
    *   **Body Type**: `Raw`
    *   **Content Type**: `JSON (application/json)`
    *   **Request Content**:
        ```json
        {
          "model": "claude-3-opus-20240229",
          "max_tokens": 4000,