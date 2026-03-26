---
name: ai-code-review
description: "Ai Code Review — Skill especializada para ai code review"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Ai Code Review

Esta skill capacita o Claude a atuar como um engenheiro de software sênior, realizando revisões de código automatizadas e contextuais com foco em qualidade, segurança e performance.

---

## Keywords

Revisão de Código IA, Code Quality, Segurança de Código, Análise Estática, Pull Request Automation, GitHub Webhook, Claude API, Prompts de Revisão, Refatoração, Automação N8N, Make.com, CI/CD, Testes Unitários, Vulnerabilidade, Boas Práticas.

---

## Quick Start

1.  **Configurar Webhook no GitHub**: Crie um webhook no seu repositório GitHub para eventos `pull_request` apontando para um endpoint de automação (Make/N8N).
2.  **Desenvolver Fluxo de Automação (Make/N8N)**: Crie um cenário/workflow que receba o payload do webhook, extraia as alterações do PR e chame a API do Claude.
3.  **Elaborar Prompt de Revisão**: Construa um prompt detalhado para o Claude, incluindo contexto do projeto, padrões de codificação e áreas de foco (segurança, performance, legibilidade).
4.  **Processar Resposta do Claude**: Configure o fluxo para formatar a resposta do Claude e postar os comentários da revisão diretamente no Pull Request do GitHub via API.

---

## Core Workflows

### Workflow 1: Revisão Automática de Pull Request com GitHub, N8N e Claude API

Este workflow automatiza a revisão inicial de Pull Requests (PRs) para identificar problemas comuns antes mesmo de um revisor humano intervir, acelerando o ciclo de desenvolvimento.

**Passos Detalhados:**

1.  **Configuração do Webhook GitHub**:
    *   No seu repositório GitHub, vá em `Settings` > `Webhooks` > `Add webhook`.
    *   **Payload URL**: `https://your-n8n-instance.com/webhook/github-pr-review` (substitua pelo seu endpoint N8N).
    *   **Content type**: `application/json`.
    *   **Secret**: `SUA_CHAVE_SECRETA_WEBHOOK` (opcional, mas recomendado para segurança).
    *   **Which events would you like to trigger this webhook?**: Selecione `Let me select individual events.` e marque `Pull requests`.
    *   Clique em `Add webhook`.

2.  **Criação do Fluxo N8N (Exemplo):**
    *   **Nó 1: Webhook N8N**:
        *   Tipo: `Webhook`.
        *   Modo: `POST`.
        *   `Webhook URL`: Copie o URL gerado pelo N8N para usar no GitHub.
        *   `Authentication`: Configure conforme a `Secret` do GitHub (ex: `Header Auth` com `X-Hub-Signature-256`).
    *   **Nó 2: Extrair Detalhes do PR e Obter Diff**:
        *   Tipo: `Code` (JavaScript) para processar o payload inicial.
        *   Objetivo: Extrair o URL do PR, o número do PR, o nome completo do repositório e, crucialmente, fazer uma chamada HTTP para obter o diff das alterações.
        *   Exemplo de código (assumindo que você tem um token GitHub armazenado em credenciais N8N):
            ```javascript
            const prUrl = $json.pull_request.url;
            const repoFullName = $json.pull_request.head.repo.full_name;
            const prNumber = $json.number;
            const prDiffUrl = $json.pull_request.diff_url; // URL para obter o diff

            // Retorna o URL do diff para o próximo nó HTTP Request
            return [{ json: { prUrl, repoFullName, prNumber, prDiffUrl } }];
            ```
    *   **Nó 3: Obter Diff do PR via GitHub API**:
        *   Tipo: `HTTP Request`.
        *   Método: `GET`.
        *   URL: `{{ $json.prDiffUrl }}`
        *   Headers:
            *   `Authorization`: `token YOUR_GITHUB_TOKEN` (token pessoal com permissões `repo`).
            *   `Accept`: `application/vnd.github.v3.diff`
        *   Salvar a resposta RAW (o diff) para o próximo nó.
    *   **Nó 4: Chamar Claude API para Revisão**:
        *   Tipo: `HTTP Request`.
        *   Método: `POST`.
        *   URL: `https://api.anthropic.com/v1/messages`
        *   Headers:
            *   `x-api-key`: `{{ sua_claude_api_key }}`
            *   `anthropic-version`: `2023-06-01`
            *   `Content-Type`: `application/json`
        *   Body (RAW JSON):
            ```json
            {
              "model": "claude-3-opus-20240229",
              "max_tokens": 2000,
              "messages": [
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "Você é um revisor de código sênior para projetos JavaScript/TypeScript, focado em performance, segurança, legibilidade (ESLint/Prettier), e conformidade com boas práticas de Node.js. Analise o seguinte diff de Pull Request e forneça um feedback construtivo, listando os pontos de melhoria com exemplos de código quando aplicável. Use um tom profissional e objetivo. Priorize problemas críticos e sugestões de refatoração, especialmente em segurança e performance.\n\nDiff do PR:\n```diff\n{{ $node["Obter Diff do PR via GitHub API"].data.text }}\n```\n\nFormato esperado da resposta:\n\n### Sumário da Revisão\n[Resumo geral e impacto]\n\n### Pontos de Melhoria\n\n1.  **[Título do Problema]**\n    *   **Severidade**: [Crítico/Alto/Médio/Baixo]\n    *   **Descrição**: [Explicação detalhada do problema e por que é um problema.]\n    *   **Localização**: [Arquivo:Linha(s)]\n    *   **Sugestão**: [Exemplo de como corrigir ou refatorar.]\n\n2.  **[Outro Título do Problema]**\n    *   ...\n\n### Observações Adicionais\n[Comentários gerais ou