---
name: user-behavior-analysis
description: "User Behavior Analysis — Skill especializada para user behavior analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# User Behavior Analysis

Esta skill capacita a analisar profundamente o comportamento do usuário em plataformas digitais, utilizando Google Analytics 4 (GA4) para otimizar funis, engajamento e atribuição de marketing.

---

## Keywords

GA4, Análise Comportamental, Jornada do Usuário, Segmentação GA4, Funil de Conversão, Atribuição de Marketing, Eventos GA4, Explorações GA4, Engajamento Digital, Retenção de Usuários, LTV (Lifetime Value), Otimização CRO, BigQuery, DebugView GA4.

---

## Quick Start

1.  **Valide a Implementação de Eventos Essenciais no GA4**: Utilize o "DebugView" do GA4 (Administrador > DebugView) para confirmar que eventos padrão como `page_view`, `session_start`, `first_visit`, e eventos personalizados de conversão (ex: `add_to_cart`, `lead_submission`) estão sendo disparados corretamente e com os parâmetros esperados.
2.  **Crie uma Exploração de Funil de Conversão**: Acesse o GA4 > Explorações > Galeria de Modelos > Funil de Conversão. Defina os passos chave para uma jornada crítica (ex: Visualização de Produto > Adição ao Carrinho > Início de Checkout > Compra) e observe as taxas de queda entre cada etapa, identificando os gargalos imediatos.
3.  **Monitore o Engajamento e Retenção por Coorte**: No GA4, navegue até Relatórios > Retenção para analisar a taxa de retorno de usuários por coorte. Complemente esta análise com as métricas "Sessões Engajadas" e "Tempo de Engajamento Médio" em Relatórios > Engajamento > Visão geral para identificar tendências de interação.
4.  **Analise a Atribuição de Canais no GA4**: Consulte Relatórios > Publicidade > Modelos de atribuição > Compar