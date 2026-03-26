---
name: service-package-pricing
description: "Service Package Pricing — Skill especializada para service package pricing"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Service Package Pricing

Esta skill capacita o Claude a estruturar, precificar e otimizar pacotes de serviços, garantindo rentabilidade e competitividade no mercado.

---

## Keywords

Precificação de pacotes, bundling de serviços, análise de custos, markup, margem de lucro, LTV/CAC, break-even point, valor percebido, estratégia de preços, otimização de preços, precificação por valor, tiers de serviços, ROI de pacotes.

---

## Quick Start

1.  **Listar Componentes de Serviço**: Detalhar cada serviço individual (ex: 'Criação de 5 posts/mês', 'Suporte Nível 1') e seus custos diretos estimados (horas de equipe, licenças).
2.  **Agrupar Pacotes Iniciais**: Combinar serviços complementares para formar 2-3 pacotes lógicos (ex: Essencial, Profissional, Premium) baseados em níveis de necessidade do cliente.
3.  **Calcular Custo e Margem Alvo**: Somar os custos diretos de cada pacote e aplicar uma margem bruta alvo de 35% para determinar o preço de venda inicial.
4.  **Validar Preços com Mercado**: Pesquisar e comparar a proposta de valor e preço dos pacotes iniciais com 3-5 concorrentes diretos, ajustando onde necessário.
5.  **Analisar Ponto de Equilíbrio**: Projetar quantos pacotes de cada tipo precisam ser vendidos mensalmente para cobrir os custos fixos da operação.

---

## Core Workflows

### Workflow 1: Estruturação e Precificação Base de Pacotes de Serviços

Este workflow detalha a criação de pacotes de serviços a partir do custo, garantindo rentabilidade desde o início.

1.  **Mapeamento Detalhado de Custos por Serviço Componente**:
    *   **Ação**: Identificar todos os custos diretos e indiretos associados a cada serviço que compõe um pacote. Custos diretos incluem mão de obra (horas por serviço \* custo/hora), licenças de software específicas, ferramentas necessárias. Custos indiretos (administrativos, marketing, aluguel) devem ser rateados e alocados proporcionalmente (ex: por hora de serviço ou como uma porcentagem dos custos diretos).
    *   **Exemplo Prático**:
        *   Serviço: "Gestão de Redes Sociais" (componente de um pacote de marketing).
        *   Tempo estimado: 8 horas/mês.
        *   Custo de Mão de Obra (analista): R$ 80/hora.
        *   Custo Ferramenta de Agendamento/Relatório: R$ 50/mês (licença proporcional).
        *   Custo Direto Total: (8h \* R$ 80/h) + R$ 50 = R$ 640 + R$ 50 = R$ 690.
        *   Alocação de Custos Indiretos (20% do custo direto): R$ 690 \* 0.20 = R$ 138.
        *   Custo Total por Componente "Gestão de Redes Sociais": R$ 690 + R$ 138 = R$ 828.

2.  **Definição de Conteúdo e Níveis dos Pacotes Estratégicos**:
    *   **Ação**: Agrupar os serviços componentes em 2 a 4 pacotes distintos (ex: Básico, Essencial, Profissional, Premium) que atendam a diferentes segmentos de clientes ou necessidades. Cada pacote deve ter uma proposta de valor clara e diferenciais tangíveis.
    *   **Exemplo Prático**:
        *   **Pacote Essencial - Marketing Digital**: Inclui "Gestão de Redes Sociais" (8h/mês) e "Criação de 5 Posts" (5h/mês).
        *   **Pacote Profissional - Marketing Digital**: Inclui "Gestão de Redes Sociais" (12h/mês), "Criação de 10 Posts" (10h/mês), "Relatório de Performance Mensal" (3h/mês) e "Otimização SEO On-Page" (4h/mês).

3.  **Cálculo de Custo Total por Pacote e Aplicação de Markup**:
    *   **Ação**: Somar os custos totais de todos os serviços componentes de cada pacote. Em seguida, aplicar a fórmula de markup para definir o preço de venda, considerando a margem bruta alvo desejada.
    *   **Fórmula Markup**: `Preço de Venda do Pacote = Custo Total do Pacote / (1 - Margem Bruta Alvo)`
    *   **Exemplo Prático**:
        *   **Pacote Essencial - Marketing Digital**:
            *   Custo "Gestão de Redes Sociais": R$ 828.
            *   Custo "Criação de 5 Posts" (estimado similar ao exemplo anterior, R$ 500 custo direto + R$ 100 indireto): R$ 600.
            *   Custo Total do Pacote Essencial: R$ 828 + R$ 600 = R$ 1428.
            *   Margem Bruta Alvo: 30%.
            *   Preço de Venda do Pacote Essencial = R$ 1428 / (1 - 0.30) = R$ 1428 / 0.70 = **R$ 2040.00**.

### Workflow 2: Otimização de Precificação de Pacotes com Análise de Valor e Desempenho

Este workflow foca em ajustar e otimizar os preços dos pacotes com base em fatores de mercado, valor percebido e métricas de desempenho.

1.  **Análise de Valor Percebido e Posicionamento Competitivo**:
    *   **Ação**: Avaliar o valor que cada pacote entrega ao cliente em comparação com a concorrência e as alternativas do mercado. Isso envolve pesquisa de mercado, entrevistas com clientes e análise de diferenciais.
    *   **Exemplo Prático**: O "Pacote Profissional - Marketing Digital" oferece relatórios detalhados e otimização SEO, que a concorrência não inclui no mesmo nível de preço. Este diferencial permite posicionar o pacote como de alto valor, justificando um preço ligeiramente superior ou igual com mais entregas. Ajustar o preço de R$ 3800 para R$ 4200 pode ser aceitável se o valor percebido for significativamente maior, aumentando a margem.

2.  **Cálculo do Ponto de Equilíbrio (Break-even Point) para Pacotes**:
    *   **Ação**: Determinar a quantidade mínima de pacotes que precisam ser vendidos para cobrir os custos fixos da operação, considerando o preço e o custo variável médio por pacote.
    *   **Fórmula Ponto de Equilíbrio (em unidades de pacote)**: `PE (Pacotes) = Custos Fixos Totais / (Preço Médio do Pacote - Custo Variável Médio por Pacote)`
    *   **Exemplo Prático**:
        *   Custos Fixos Mensais da Operação (aluguel, salários administrativos, softwares gerais): R$ 18.000.
        *   Preço Médio Ponderado dos Pacotes Vendidos (ex: R$ 2040 Essencial, R$ 4200 Profissional, média R$ 3000).
        *   Custo Variável Médio por Pacote (mão de obra direta, licenças por cliente): R$ 1200.
        *   Ponto de Equilíbrio = R$ 18.000 / (R$ 3000 - R$ 1200) = R$ 18.000 / R$ 1800 = **10 pacotes**. A empresa precisa vender 10 pacotes por mês para não ter prejuízo.

3.  **Projeção de LTV/CAC (Lifetime Value / Custo de Aquisição de Cliente) por Segmento de Pacote**:
    *   **Ação**: Avaliar a rentabilidade a longo prazo de cada tipo de pacote, comparando o valor total que um cliente gera (LTV) com o custo para adquiri-lo (CAC).
    *   **Fórmula LTV (simplificada)**: `LTV = (Receita Média Mensal por Pacote * Margem Bruta do Pacote) / Taxa de Churn Mensal`
    *   **Fórmula CAC**: `CAC = Custo Total de Marketing e Vendas / Número de Novos Clientes Adquiridos`
    *   **Exemplo Prático**:
        *   **Pacote Profissional - Marketing Digital**:
            *   Receita Média Mensal por Pacote: R$ 4200.
            *   Margem Bruta do Pacote: 40% (R$ 1680).
            *   Taxa de Churn Mensal para este tipo de cliente: 4%.
            *   LTV = (R$ 4200 \* 0.40) / 0.04 = R$ 1680 / 0.04 = **R$ 42.000**.
            *   Se o CAC para clientes deste pacote for R$ 5.000 (custo de campanha de marketing + vendas para adquirir um cliente Profissional).
            *   Relação LTV/CAC = R$ 42.000 / R$ 5.000 = **8.4**. Uma relação de 3:1 ou superior é considerada saudável, indicando que este pacote é altamente lucrativo a longo prazo.

---

## Templates

### Estrutura de Pacote de Serviços e Cálculo de Preço Base

```
# Pacote de Serviços: [Nome do Pacote - Ex: Marketing Digital Essencial]

## Descrição do Pacote:
[Breve descrição do valor e objetivo do pacote. Ex: Ideal para pequenas empresas que buscam presença digital e engajamento inicial.]

## Componentes do Pacote:

| Serviço Componente       | Qtd. Horas/Unidades | Custo Mão de Obra (R$/h ou un) | Custo Ferramentas/Licenças (R$) | Custo Direto Total (R$) | Alocação Indiretos (20%) (R$) | Custo Total Componente (R$) |
|--------------------------|---------------------|-------------------------------|---------------------------------|-------------------------|-------------------------------|-----------------------------|
| Gestão de Redes Sociais  | 8 horas/mês         | 80,00                         | 50,00                           | 690,00                  | 138,00                        | 828,00                      |
| Criação de 5 Posts       | 5 horas/mês         | 80,00                         | 0,00                            | 400,00                  | 80,00                         | 480,00                      |
| Relatório Mensal Básico  | 2 horas/mês         | 80,00                         | 0,00                            | 160,00                  | 32,00                         | 192,00                      |
| **Custo Total Bruto do Pacote:**                                                                                                                                                                                            | **1500,00**                 |
| **Margem Bruta Alvo:**   | **30%**                                                                                                                                                                                          |                             |
| **Fórmula de Preço:**    | Custo Total / (1 - Margem Alvo) = 1500 / (1 - 0.30)                                                                                                                                                 |                             |
| **Preço Sugerido do Pacote:**                                                                                                                                                                                                | **R$ 2142,86**              |

## Valor Agregado/Diferenciais:
[Ex: Suporte via WhatsApp, Acesso a dashboard básico de resultados.]
```

### Análise de Sensibilidade de Precificação de Pacote

```
# Análise de Sensibilidade para [Nome do Pacote - Ex: Pacote Profissional de Marketing]

## Preço Base Atual: R$ 4200,00
## Custos Variáveis por Pacote: R$ 1680,00 (40% do preço)
## Custos Fixos Mensais Totais: R$ 18000,00

## Cenário 1: Redução de Preço de 5%

| Métrica               | Valor Base Atual | Novo Preço (-5%) | Variação (%) | Impacto na Receita (se vendas = 10 pacotes) | Impacto no Lucro (se vendas = 10 pacotes) |
|-----------------------|------------------|------------------|--------------|--------------------------------------------|------------------------------------------|
| Preço do Pacote       | R$ 4200,00       | R$ 3990,00       | -5,0%        |                                            |                                          |
| Margem Bruta (R$)     | R$ 2520,00       | R$ 2310,00       | -8,3%        |                                            |                                          |
| Ponto de Equilíbrio   | 7,1 pacotes      | 7,8 pacotes      | +9,9%        |                                            |                                          |
| Receita Mensal (10 pacotes) | R$ 42000,00      | R$ 39900,00      | -5,0%        | -R$ 2100,00                                |                                          |
| Lucro Mensal (10 pacotes) | R$ 7200,00       | R$ 5100,00       | -29,2%       |                                            | -R$ 2100,00                              |

## Cenário 2: Aumento de Preço de 5%

| Métrica               | Valor Base Atual | Novo Preço (+5%) | Variação (%) | Impacto na Receita (se vendas = 10 pacotes) | Impacto no Lucro (se vendas = 10 pacotes) |
|-----------------------|------------------|------------------|--------------|--------------------------------------------|------------------------------------------|
| Preço do Pacote       | R$ 4200,00       | R$ 4410,00       | +5,0%        |                                            |                                          |
| Margem Bruta (R$)     | R$ 2520,00       | R$ 2730,00       | +8,3%        |                                            |                                          |
| Ponto de Equilíbrio   | 7,1 pacotes      | 6,5 pacotes      | -8,5%        |                                            |                                          |
| Receita Mensal (10 pacotes) | R$ 42000,00      | R$ 44100,00      | +5,0%        | +R$ 2100,00                                |                                          |
| Lucro Mensal (10 pacotes) | R$ 7200,00       | R$ 9300,00       | +29,2%       |                                            | +R$ 2100,00                              |

## Observações:
[Ex: Uma redução de preço requer um aumento de vendas de X% para manter o mesmo lucro. Um aumento de preço de 5% aumenta o lucro em quase 30% se o volume de vendas for mantido.]
```

---

## Checklist

-   [x] Todos os custos diretos (mão de obra, licenças, ferramentas) por serviço componente foram mapeados?
-   [x] Custos indiretos (administrativos, operacionais) foram alocados e incluídos no custo total de cada pacote?
-   [x] Margem bruta alvo foi definida (ex: 30-45%) e aplicada consistentemente a todos os pacotes?
-   [x] Pesquisa de preços e proposta de valor de 3-5 concorrentes diretos foi realizada para posicionamento?
-   [x] O ponto de equilíbrio (Break-even Point) em número de pacotes foi calculado para a operação?
-   [x] A relação LTV/CAC foi projetada para os principais segmentos de clientes de pacotes?
-   [x] Cada pacote possui uma proposta de valor única e clara, evitando canibalização interna?
-   [x] Existe um plano para revisão periódica (trimestral ou semestral) da estrutura e preços dos pacotes?
-   [x] A equipe de vendas e marketing compreende os diferenciais e valor de cada pacote?
-   [x] Estratégias de upsell e cross-sell entre os pacotes ou com serviços avulsos foram consideradas?

---

## Métricas de Referência

| Métrica                     | Benchmark Típico | Meta Específica (Exemplo) |
|-----------------------------|------------------|---------------------------|
| Margem Bruta Média por Pacote | 30% - 50%        | 40%                       |
| Relação LTV/CAC (Pacotes)   | 3:1              | 5:1                       |
| Taxa de Churn de Pacotes    | 5% - 10% mês     | <3% mês                   |
| Receita Média por Pacote (ARPA) | R$ 1.500 - R$ 5.000 | R$ 3.000 (Mix de Pacotes) |
| ROI de Promoções de Pacotes | >1.5             | >2.0                      |
| Taxa de Conversão de Pacotes | 10% - 25% (Propostas) | 20%                       |

---

## Erros Comuns

1.  **Ignorar Custos Indiretos na Precificação**: Apenas considerar custos diretos (mão de obra, licenças) leva a pacotes subprecificados e margens insustentáveis.
    *   **Como evitar com exemplo**: Um "Pacote de Desenvolvimento de Website" pode ter um custo direto de R$ 3.000 (horas de desenvolvedor, licenças de tema). Se os custos indiretos (aluguel, administrativo, marketing geral) não forem rateados e adicionados (ex: R$ 1.000), o preço final será muito baixo, corroendo a lucratividade. Sempre adicione uma porcentagem (ex: 20-30% do custo direto) ou um valor fixo por projeto/pacote para cobrir esses custos.
2.  **Precificação Exclusivamente Baseada no Concorrente**: Copiar preços da concorrência sem entender a própria estrutura de custos, proposta de valor e mercado-alvo.
    *   **Como evitar com exemplo**: Se um concorrente oferece um "Pacote de Suporte de TI" por R