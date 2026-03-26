---
name: growth-experiment
description: "Growth Experiment — Skill especializada para growth experiment"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Growth Experiment

Esta skill capacita a idealizar, planejar, executar e analisar experimentos de growth focados em alavancar métricas de funil, otimizando a aquisição, ativação, retenção, receita e recomendação de produtos.

---

## Keywords

A/B Testing, Hipótese de Growth, Métrica North Star, Funil Pirata (AARRR), Cohort Analysis, Validação de Hipótese, Iteração Rápida, Feature Flag, Experimentação Contínua, PMF (Product-Market Fit), Ciclo HEART (Happiness, Engagement, Adoption, Retention, Task Success), Otimização de Conversão.

---

## Quick Start

1.  **Formular Hipótese Acionável**: Elabore uma hipótese clara, mensurável e com potencial impacto em uma métrica específica do funil AARRR, como "Se simplificarmos o fluxo de cadastro, aumentaremos a ativação em 15%".
2.  **Desenhar o Experimento**: Estruture um teste A/B definindo grupo de controle (A) e variante (B), métrica primária, tamanho da amostra, duração e ferramenta (ex: VWO, Optimizely).
3.  **Implementar e Monitorar**: Configure o experimento na plataforma escolhida, assegure a correta segmentação do tráfego e monitore proativamente a coleta de dados e quaisquer anomalias.
4.  **Analisar Resultados Estatisticamente**: Avalie os dados coletados para determinar a significância estatística do impacto da variante sobre a métrica primária, usando ferramentas como testes t ou qui-quadrado.
5.  **Decidir e Iterar**: Baseado na análise, decida se a variante será implementada, descartada ou se servirá como base para uma nova hipótese e um próximo experimento.

---

## Core Workflows

### Workflow 1: Validação de Hipótese de Ativação via A/B Testing em Onboarding

Este workflow detalha o processo de usar um A/B test para validar uma hipótese que visa melhorar a taxa de ativação de novos usuários em um SaaS de gerenciamento de projetos. A ativação, neste contexto, é definida como a criação do primeiro projeto.

1.  **Identificação de Gargalo**: A equipe de Growth observou que a taxa de usuários que completam o onboarding e criam seu primeiro projeto é de apenas 35%, enquanto o benchmark do setor é de 50%. Há um abandono significativo após o cadastro inicial.
2.  **Formulação de Hipótese**: Baseado em feedback de usuários e análise de funil, a equipe hipotetiza: "Se adicionarmos um 'Tour Guiado' interativo de 3 passos após o cadastro e antes da tela principal, então a taxa de criação do primeiro projeto aumentará de 35% para 45% nos próximos 21 dias."
    *   **Métrica Primária**: Taxa de ativação (usuários que criam o primeiro projeto).
    *   **Métrica Secundária**: Tempo para ativação, taxa de abandono na tela pós-cadastro.
3.  **Design do Experimento**:
    *   **Variante A (Controle)**: Fluxo de onboarding atual (cadastro -> tela principal).
    *   **Variante B (Experimento)**: Fluxo com "Tour Guiado" de 3 passos (cadastro -> tour -> tela principal).
    *   **Ferramenta de A/B Testing**: Optimizely Web.
    *   **Amostra Necessária**: Calculada em 3.000 usuários por grupo (com base em significância estatística de 95%, poder de 80% e um aumento esperado de 10 pontos percentuais).
    *   **Duração Estimada**: 21 dias para atingir a amostra mínima e observar o impacto.
    *   **Segmentação**: 50% do tráfego de novos cadastros para o Grupo A, 50% para o Grupo B.
4.  **Implementação e Lançamento**:
    *   Desenvolvedores implementam o "Tour Guiado" e integram com o Optimizely via feature flag.
    *   O experimento é lançado gradualmente, começando com 10% do tráfego, monitorando erros, e escalando para 100% após 24h sem problemas.
5.  **Monitoramento e Análise**:
    *   Acompanhamento diário das métricas primária e secundária através do dashboard do Optimizely e Google Analytics.
    *   Após