---
name: tax-planning-digital
description: "Tax Planning Digital — Skill especializada para tax planning digital"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Tax Planning Digital

Esta skill capacita o Claude a atuar como um especialista em otimização tributária para negócios digitais, focando em análise de dados, regimes fiscais e ferramentas para maximizar a eficiência fiscal.

---

## Keywords

Planejamento tributário digital, e-commerce, SaaS, infoprodutos, Lucro Real, Lucro Presumido, Simples Nacional, elisão fiscal, recuperação de créditos, análise fiscal automatizada, tributação de serviços digitais, cross-border taxation, NCM, CST, DIFAL, Fator R.

---

## Quick Start

1.  **Integrar sistemas fiscais:** Conecte o ERP ou plataforma de e-commerce (ex: Shopify, Bling) a uma ferramenta de tax compliance (ex: TaxManager, e-Auditoria) para automatizar a coleta de dados de vendas e despesas.
2.  **Gerar relatório fiscal detalhado:** Exporte um relatório consolidado de vendas e custos com NCM/CST dos produtos e UF de destino, cobrindo os últimos 12 meses.
3.  **Simular regimes tributários:** Utilize a ferramenta para projetar o impacto fiscal do Lucro Real vs. Lucro Presumido para o próximo ano fiscal, considerando o faturamento e as margens esperadas.
4.  **Analisar PIS/COFINS monofásico:** Execute uma verificação na base de produtos para identificar itens com PIS/COFINS monofásico ou alíquota zero, garantindo a correta aplicação e recuperação de créditos.
5.  **Verificar elegibilidade a incentivos:** Consulte a base de dados de incentivos fiscais para o seu setor e localização, como a Lei do Bem para P&D ou regimes especiais de ICMS.

---

## Core Workflows

### Workflow 1: Análise e Otimização da Estrutura Tributária para E-commerce

Este workflow detalha os passos para que um e-commerce otimize sua carga tributária, desde a coleta de dados até a recuperação de créditos.

1.  **Coleta de Dados Automatizada e Mapeamento Fiscal:**
    *   **Ação:** Conectar o ERP (ex: Tiny, Omie) ou plataforma de e-commerce (ex: Vtex, Loja Integrada) a uma solução de automação fiscal (ex: Bling com módulo fiscal, ou integração com TaxManager). Configure a extração diária ou semanal de dados de vendas (NF-e), NCM dos produtos, CEST, CST/CSOSN, CFOP, origem (Nacional/Importado) e destino (UF do cliente).
    *   **Exemplo:** Um e-commerce que vende eletrônicos integra seu ERP com o TaxManager. O sistema automatiza a extração das NF-e emitidas, identificando que um "Smartphone XYZ" (NCM 8517.12.31) foi vendido para um consumidor final na Bahia (UF destino diferente da origem) e que um "Fone de Ouvido ABC" (NCM 8518.30.00) foi vendido para um contribuinte do ICMS em São Paulo.

2.  **Classificação Fiscal e Revisão de Cadastros de Produtos:**
    *   **Ação:** Utilize a ferramenta de tax planning para auditar e validar os NCMs e CSTs/CSOSNs cadastrados para cada produto. Priorize produtos com maior volume de vendas ou maior margem.
    *   **Exemplo:** Durante a auditoria, a ferramenta identifica que um "Suplemento Vitamínico" (NCM 2106.90.30) estava cadastrado com CST 000 (Tributado Integralmente) para PIS/COFINS. A análise revela que este NCM é sujeito a alíquota zero de PIS/COFINS, gerando uma economia imediata ao corrigir o cadastro para CST 006 (Operação Tributada a Alíquota Zero). A empresa estava pagando PIS/COFINS desnecessariamente sobre este produto.

3.  **Simulação de Regimes Tributários e Impacto no Lucro:**
    *   **Ação:** Com base na receita bruta projetada e na estrutura de custos/despesas, simule o impacto financeiro de permanecer ou migrar entre Lucro Presumido e Lucro Real. Considere o lucro líquido real e a possibilidade de créditos.
    *   **Exemplo:** Para um e-commerce com projeção de faturamento de R$ 10 milhões/ano e margem de lucro de 12% (R$ 1.2 milhão de lucro), a simulação mostra que no Lucro Presumido (comércio), o IRPJ+CSLL seria baseado em 8% e 12% da receita, respectivamente, totalizando aproximadamente R$ 220 mil. No Lucro Real, se as despesas operacionais dedut