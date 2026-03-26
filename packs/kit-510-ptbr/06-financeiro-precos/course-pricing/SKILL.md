---
name: course-pricing
description: "Course Pricing — Skill especializada para course pricing"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Course Pricing

Esta skill capacita o Claude a desenvolver e otimizar estratégias de precificação para cursos online e presenciais, utilizando análises financeiras e projeções de mercado.

---

## Keywords

Precificação de cursos, Análise de ROI educacional, Modelo de precificação, Estratégia de valor percebido, Markup educacional, Margem de lucro curso, Break-even cursos, LTV/CAC educação, Projeção de vendas cursos, Pricing psicológico, Escala de preços, Análise de concorrência educacional.

---

## Quick Start

1.  Calcular custos diretos e indiretos detalhados do desenvolvimento e entrega do curso.
2.  Analisar os preços praticados por, no mínimo, 5 concorrentes diretos para cursos com temas e qualidade similares.
3.  Definir o valor percebido que o curso entrega ao aluno e o posicionamento de mercado desejado (ex: premium, acessível).
4.  Aplicar uma estratégia de markup ou margem de lucro bruta desejada para chegar a um preço inicial.
5.  Simular cenários de volume de vendas para atingir o ponto de equilíbrio financeiro e projetar lucros.

---

## Core Workflows

### Workflow 1: Precificação Baseada em Custos, Margem e Valor Percebido

Este workflow guia o processo de determinar um preço inicial para o curso, considerando seus custos reais, a margem de lucro desejada e o valor que o mercado está disposto a pagar.

*   **Passo 1: Levantamento de Custos Detalhado.**
    *   **Custos Fixos (CF):** Despesas que não variam com o número de alunos. Exemplo: R$5.000 para desenvolvimento inicial do conteúdo, R$1.200 anuais para licenças de software de edição de vídeo, R$3.000 mensais para marketing institucional fixo, R$3.600 mensais de rateio de salário do coordenador pedagógico.
    *   **Custos Variáveis por Aluno (CVA):** Despesas que aumentam com cada novo aluno. Exemplo: R$30 para material didático digital/impresso por aluno, R$20 para acesso à plataforma EAD por licença de aluno, R$10 para suporte individualizado por aluno, 10% de comissão de vendas sobre o Preço de Venda (PV) por matrícula.
    *   Exemplo: Para um curso de "Marketing Digital para Iniciantes", os CF totalizam R$12.800/mês (considerando rateio anual de desenvolvimento e licenças). Os CVA somam R$60 + 10% do PV.

*   **Passo 2: Definição da Margem de Lucro Bruta Desejada.**
    *   A margem de lucro bruta desejada para cursos online pode variar amplamente, de 30% a 70%, dependendo do nível de exclusividade, público-alvo e custos de aquisição. Para um curso de alto valor percebido, o objetivo pode ser 60%.
    *   Fórmula do Preço de Venda (PV) baseado em Margem: `PV = CVA / (1 - Margem de Lucro Desejada - %ComissãoVendas)`. Ou, de forma mais simples, usando a Margem de Contribuição: `MC = PV - CVA` e `Margem Bruta = MC / PV`.
    *   Exemplo: Se o CVA é R$89,70 (R$60 fixos + 10% de comissão) e a margem bruta desejada é de 60%, então o preço de venda é calculado por tentativa e erro ou por `PV = CVA_sem_comissao / (1 - Margem_Desejada - %Comissao)`. Vamos usar a forma mais direta via Ponto de Equilíbrio para o PV. Para fins de margem, podemos projetar um PV e verificar a margem. Se o PV projetado for R$297, o CVA será R$60 + R$29,70 (10% de 297) = R$89,70. A Margem de Contribuição (MC) é R$297 - R$89,70 = R$207,30. A Margem Bruta é R$207,30 / R$297 = 0,6979, ou seja, 69,79%.

*   **Passo 3: Análise de Valor Percebido e Posicionamento de Mercado.**
    *   Realizar pesquisa com potenciais alunos para entender quanto eles valorizariam e estariam dispostos a pagar pelo conteúdo, os diferenciais do curso e os resultados prometidos. Utilizar enquetes ou entrevistas.
    *   Comparar com cursos de 5 a 10 concorrentes diretos e indiretos: Qual o preço médio? Quais diferenciais eles oferecem? Como o nosso curso se posiciona em relação a eles (mais premium, mais acessível)?
    *   Ajuste do PV: Se o mercado percebe um valor superior (ex: R$397) devido à qualidade dos instrutores, material bônus exclusivo e suporte, o preço inicial de R$297 pode ser ajustado para cima, aumentando a margem de lucro sem comprometer a demanda.

### Workflow 2: Análise de Ponto de Equilíbrio e Projeção de Vendas para Cursos

Este workflow foca em garantir a viabilidade financeira do curso, calculando quantas matrículas são necessárias para cobrir os custos e projetando cenários de vendas para otimizar o lucro.

*   **Passo 1: Cálculo do Ponto de Equilíbrio (PE).**
    *   **Custos Fixos Totais (CFT):** Somatório de todos os custos fixos mensais identificados no Workflow 1. Exemplo: R$12.800/mês.
    *   **Custos Variáveis por Aluno (CVA):** Somatório de todos os custos variáveis por aluno. Exemplo: R$89,70/aluno (considerando PV de R$297 e 10% de comissão).
    *   **Preço de Venda por Aluno (PV):** O preço final de venda do curso. Exemplo: R$297.
    *   **Margem de Contribuição por Aluno (MC):** `MC = PV - CVA`. Exemplo: R$297 - R$89,70 = R$207,30.
    *   **Ponto de Equilíbrio em Unidades (PEu):** `PEu = CFT / MC`. Exemplo: R$12.800 / R$207,30 ≈ 61.74 alunos. Arredondar para 62 alunos. Isso significa que 62 matrículas são necessárias para cobrir todos os custos.

*   **Passo 2: Projeção de Vendas e Análise de Cenários.**
    *   **Cenário Otimista:** Projeção de 150 alunos/mês. Receita = 150 * R$297 = R$44.550. Lucro = (150 * R$207,30) - R$12.800 = R$31.095 - R$12.800 = R$18.295.
    *   **Cenário Realista:** Projeção de 100 alunos/mês. Receita = 100 * R$297 = R$29.700. Lucro = (100 * R$207,30) - R$12.800 = R$20.730 - R$12.800 = R$7.930.
    *   **Cenário Pessimista:** Projeção de 40 alunos/mês. Receita = 40 * R$297 = R$11.880. Lucro = (40 * R$207,30) - R$12.800 = R$8.292 - R$12.800 = -R$4.508 (