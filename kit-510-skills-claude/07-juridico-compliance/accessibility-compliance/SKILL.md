---
name: accessibility-compliance
description: "Accessibility Compliance — Skill especializada para auxiliar na conformidade com padrões de acessibilidade digital e física, mitigando riscos legais e promovendo inclusão."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
---

# Accessibility Compliance

Esta skill capacita o Claude a atuar como um especialista em conformidade de acessibilidade, fornecendo diretrizes, templates e workflows para garantir que produtos digitais e ambientes físicos atendam aos padrões legais e técnicos.

---

## Keywords

WCAG 2.1, WCAG 2.2, ABNT NBR 9050, Lei Brasileira de Inclusão (LBI), ADA Compliance, VPAT (Voluntary Product Accessibility Template), eMAG (Modelo de Acessibilidade em Governo Eletrônico), Contrato de Acessibilidade, Auditoria de Acessibilidade, Design Inclusivo, Conformidade Digital, Legislação de Acessibilidade, Testes de Usabilidade Acessível.

---

## Quick Start

1.  **Auditar Conformidade WCAG 2.1 AA:** Utilize ferramentas como Lighthouse (Chrome DevTools) ou WAVE (Web Accessibility Evaluation Tool) para uma análise inicial de um website ou aplicação web, focando nos critérios de sucesso nível AA.
2.  **Verificar NBR 9050 para Ambientes Físicos:** Revise a planta arquitetônica ou o layout de um espaço físico para garantir a existência de rampas com inclinação adequada (máx. 8,33%), sinalização tátil e visual, e sanitários acessíveis conforme a ABNT NBR 9050.
3.  **Avaliar VPAT de Software de Terceiros:** Solicite e analise o VPAT de qualquer software a ser adquirido ou integrado, verificando a aderência aos padrões de acessibilidade relevantes para seu contexto (e.g., WCAG 2.1, Section 508).
4.  **Elaborar Cláusula Contratual de Acessibilidade:** Inclua nos contratos com fornecedores de serviços digitais uma cláusula obrigando a entrega de produtos e serviços em conformidade com WCAG 2.1 AA e eMAG, com penalidades claras em caso de não-conformidade.

---

## Core Workflows

### Workflow 1: Auditoria de Conformidade WCAG 2.1 AA para Conteúdo Web

Este workflow detalha o processo para verificar a aderência de um website ou aplicação web aos Critérios de Sucesso do WCAG 2.1 Nível AA, essencial para mitigar riscos legais e ampliar o acesso.

**Passos Detalhados:**

1.  **Planejamento e Escopo:**
    *   **Definição de Páginas-Chave:** Selecione um conjunto representativo de páginas (homepage, páginas de formulário, páginas de conteúdo dinâmico, fluxo de compra) para auditoria. Para um e-commerce, inclua a página de produto, carrinho e checkout.
    *   **Seleção de Ferramentas:** Escolha as ferramentas de análise automatizada (ex: Lighthouse, AXE DevTools, WAVE) e defina quais leitores de tela serão utilizados para testes manuais (ex: NVDA para Windows, VoiceOver para macOS/iOS, TalkBack para Android).
    *   **Alocação de Equipe:** Designe um testador com conhecimento em acessibilidade e, idealmente, um usuário com deficiência visual ou motora para testes de usabilidade.

2.  **Execução da Auditoria Automatizada:**
    *   **Lighthouse (Chrome):** Abra o Chrome DevTools (F12), vá para a aba "Lighthouse", selecione "Acessibilidade" e gere o relatório. Regist