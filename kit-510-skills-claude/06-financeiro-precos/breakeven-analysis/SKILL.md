---
name: breakeven-analysis
description: "Breakeven Analysis — Skill especializada para calcular e analisar o ponto de equilíbrio financeiro e operacional de negócios."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
---

# Breakeven Analysis

Esta skill capacita o Claude a realizar análises completas de ponto de equilíbrio, auxiliando na precificação, projeção de vendas e avaliação da viabilidade financeira de produtos ou serviços.

---

## Keywords

Ponto de Equilíbrio, Margem de Contribuição, Custos Fixos, Custos Variáveis, Volume de Vendas, Receita Mínima, Análise de Viabilidade, Precificação Estratégica, Margem de Segurança, Grau de Alavancagem Operacional, Mix de Vendas, Custo Unitário.

---

## Quick Start

1.  **Discriminar Custos Fixos Totais**: Liste e some todos os gastos que não variam com o volume de produção ou vendas, como aluguel da fábrica, salários administrativos e depreciação de equipamentos. Exemplo: R$ 25.000/mês.
2.  **Identificar Custo Variável Unitário**: Determine o custo direto associado à produção ou aquisição de uma única unidade do produto/serviço, como matéria-prima, comissão de vendas e embalagem. Exemplo: R$ 15,00 por unidade.
3.  **Estabelecer Preço de Venda Unitário**: Defina o valor pelo qual cada unidade do produto/serviço será comercializada no mercado. Exemplo: R$ 40,00 por unidade.
4.  **Calcular Margem de Contribuição Unitária**: Subtraia o Custo Variável Unitário do Preço de Venda Unitário. Exemplo: R$ 40,00 - R$ 15,00 = R$ 25,00.
5.  **Calcular Ponto de Equilíbrio em Unidades**: Divida os Custos Fixos Totais pela Margem de Contribuição Unitária. Exemplo: R$ 25.000 / R$ 25,00 = 1.000 unidades.

---

## Core Workflows

### Workflow 1: Cálculo do Ponto de Equilíbrio Contábil para Produto Único

Este workflow é essencial para determinar o volume mínimo de vendas (em unidades e em receita) que uma empresa precisa atingir para cobrir todos os seus custos, sem gerar lucro nem prejuízo, focando em um único produto ou serviço. É a base para qualquer decisão de precificação ou projeção de vendas.

**Passos Detalhados:**

1.  **Coletar Dados de Custos Fixos**: Liste e some todos os custos operacionais que permanecem constantes independentemente do volume de produção ou vendas em um período específico (ex: um mês).
    *   *Exemplo*: Uma pequena fábrica de camisetas artesanais tem os seguintes custos fixos mensais: Aluguel do ateliê (R$ 2.000), Salário do designer (R$ 3.000), Salário do administrador (R$ 2.500), Contas de internet/telefone (R$ 300), Depreciação de máquinas (R$ 200).
    *   *Custo Fixo Total*: R$ 2.000 + R$ 3.000 + R$ 2.500 + R$ 300 + R$ 200 = R$ 8.000.
2.  **Determinar Custo Variável Unitário**: Calcule todos os custos que variam diretamente com a