---
name: subscription-pricing
description: "Subscription Pricing — Skill especializada para subscription pricing"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Subscription Pricing

Essa skill capacita o Claude a desenvolver e otimizar estratégias de precificação de assinaturas, focando em modelos de receita recorrente, análise de métricas financeiras e maximização do valor do ciclo de vida do cliente (LTV).

---

## Keywords

MRR, ARR, Churn Rate, LTV, CAC, Payback Period, SaaS Pricing, Tiered Pricing, Freemium, Value-Based Pricing, Análise Cohort, Upgrade, Downgrade, Expansão de Receita, Elasticidade de Preço, Modelagem Financeira.

---

## Quick Start

1.  **Calcular MRR e Churn Atual**: Obtenha o MRR (Monthly Recurring Revenue) do último mês e a taxa de churn de clientes para identificar a saúde da receita recorrente.
2.  **Avaliar LTV/CAC Ratio**: Determine o Lifetime Value (LTV) médio dos seus clientes e o Custo de Aquisição de Cliente (CAC) para verificar a sustentabilidade do modelo de negócio.
3.  **Simular Impacto de Ajuste de Preço**: Escolha um plano existente, como o "Plano Profissional" de R$199/mês, e simule um aumento de 15% para R$228.85/mês, projetando o impacto no MRR e na retenção.
4.  **Identificar Gatilhos de Upsell**: Analise clientes no "Plano Básico" que atingiram limites de uso (ex: 80% do armazenamento) e proponha o "Plano Avançado" com maior capacidade.

---

## Core Workflows

### Workflow 1: Modelagem e Otimização de Precificação por Níveis (Tiered Pricing)

Este workflow guia na estruturação ou otimização de planos de assinatura baseados em diferentes níveis de funcionalidade ou uso, maximizando a cobertura de segmentos de mercado e incentivando upgrades.

*   **Passo 1: Segmentação de Persona por Valor Percebido**:
    *   **Ação**: Identifique no mínimo três segmentos de clientes com diferentes necessidades e disposição a pagar.
    *   **Exemplo**: Para um software de gestão de projetos:
        *   **Segmento 1 (Pequenos Empreendedores)**: Necessitam de funcionalidades básicas de organização e colaboração. Dispostos a pagar pouco.
        *   **Segmento 2 (Equipes Médias)**: Precisam de gestão de tarefas avançada, integrações e relatórios. Dispostos a pagar um valor intermediário.
        *   **Segmento 3 (Grandes Empresas)**: Exigem segurança robusta, suporte dedicado, automações complexas e personalização. Alta disposição a pagar.

*   **Passo 2: Definição de Proposta de Valor e Recursos para Cada Nível**:
    *   **Ação**: Associe conjuntos de funcionalidades e limites de uso a cada segmento, criando uma diferenciação clara entre os planos.
    *   **Exemplo**:
        *   **Plano Básico (R$49/mês)**: 5 usuários, 10 projetos, 1GB armazenamento, suporte por e-mail.
        *   **Plano Pro (R$149/mês)**: 20 usuários, projetos ilimitados, 50GB armazenamento, integrações (Slack, Trello), relatórios avançados, suporte prioritário por chat.
        *   **Plano Enterprise (R$499/mês)**: Usuários ilimitados, projetos ilimitados, 500GB armazenamento, todas as integrações, SSO, auditoria de segurança, consultoria de implementação, suporte 24/7.

*   **Passo 3: Precificação e Ancoragem de Valor**:
    *   **Ação**: Defina os preços de cada nível, utilizando a estratégia de ancoragem (Good-Better-Best) para direcionar os clientes ao plano intermediário.
    *   **Exemplo**: Com os planos acima, o Plano Pro (R$149) é posicionado como a "melhor oferta", oferecendo um salto significativo em valor por um custo que parece razoável em comparação com o Enterprise. O preço do Plano Básico (R$49) atrai a base, e o Enterprise (R$499) atende às necessidades premium.

*   **Passo 4: Análise de Upgrade/Downgrade e Otimização Contínua**:
    *   **Ação**: Monitore as transições entre os planos (upsells, downgrades) e colete feedback para ajustar as funcionalidades e os preços, otimizando a jornada do cliente.
    *   **Exemplo**: Se muitos clientes do Plano Básico estão fazendo downgrade após o 3º mês, investigue se o limite de 10 projetos é muito restritivo ou se a proposta de valor inicial não foi clara. Se o Plano Pro tem alta taxa de upsell, considere adicionar funcionalidades exclusivas para incentivar ainda mais a transição.

### Workflow 2: Projeção Financeira e Análise de Viabilidade para Novos Modelos de Assinatura

Este workflow detalha como construir uma projeção financeira para avaliar a viabilidade de um novo plano de assinatura ou modelo de negócio recorrente, incluindo métricas cruciais como LTV, CAC e Payback Period.

*   **Passo 1: Projeção de Aquisição de Clientes e Crescimento**:
    *   **Ação**: Estime o número de novos clientes mensais e a taxa de crescimento ao longo de um período (ex: 12-24 meses).
    *   **Exemplo**: Para um novo serviço de streaming de nicho:
        *   Mês 1: 500 novos assinantes.
        *   Crescimento Mensal: 10% nos primeiros 6 meses, 5% nos 6 meses seguintes.
        *   Preço do Plano: R$39,90/mês.

*   **Passo 2: Cálculo de MRR (Monthly Recurring Revenue) e ARR (Annual Recurring Revenue)**:
    *   **Ação**: Calcule a receita recorrente mensal e anual com base na aquisição de clientes e no preço do plano.
    *   **Fórmula MRR**: (Número de Clientes Ativos * ARPU) + Receita de Expansão - Receita de Churn.
    *   **Exemplo (Mês 1)**: 500 novos clientes * R$39,90 = R$19.950 MRR.
    *   **Exemplo (Mês 2, com 10% de crescimento e 5% de churn)**:
        *   Clientes Início: 500
        *   Novos Clientes: 500 * 10% = 50
        *   Clientes Churn: 500 * 5% = 25
        *   Clientes Fim: 500 + 50 - 25 = 525
        *   MRR Mês 2: 525 clientes * R$39,90 = R$20.947,50

*   **Passo 3: Projeção de Churn e Expansão (Upsell/Cross-sell)**:
    *   **Ação**: Estime a taxa de churn (clientes que cancelam) e a receita de expansão (clientes que aumentam o gasto) mensalmente.
    *   **Exemplo**:
        *   Taxa de Churn de Clientes: 5% ao mês.
        *   Receita de Expansão (Upsell/Cross-sell): 2% do MRR do mês anterior.

*   **Passo 4: Cálculo de LTV (Lifetime Value) e CAC (Customer Acquisition Cost)**:
    *   **Ação**: Calcule essas métricas cruciais para entender o valor de cada cliente e o custo para adquiri-lo.
    *   **Fórmula LTV (simplificada)**: (ARPU * Margem Bruta) / Churn Rate Mensal
        *   *Exemplo*: ARPU = R$39,90, Margem Bruta = 70%, Churn Rate = 5%. LTV = (R$39,90 * 0,70) / 0,05 = R$27,93 / 0,05 = R$558,60.
    *   **Fórmula CAC**: (Custo Total de Marketing + Custo Total de Vendas) / Número de Novos Clientes Adquiridos no Período.
        *   *Exemplo*: Custo Marketing (Mês 1) = R$10.000, Custo Vendas (Mês 1) = R$5.000. Novos Clientes = 500. CAC = (R$10.000 + R$5.000) / 500 = R$30.

*   **Passo 5: Análise de Payback Period do CAC**:
    *   **Ação**: Determine em quantos meses o investimento para adquirir um cliente é recuperado pela receita gerada por ele.
    *   **Fórmula Payback Period**: CAC / (ARPU * Margem Bruta).
        *   *Exemplo*: CAC = R$30, ARPU = R$39,90, Margem Bruta = 70%. Payback Period = R$30 / (R$39,90 * 0,70) = R$30 / R$27,93 = 1,07 meses. (Idealmente < 12 meses).

---

## Templates

### Template de Planilha de Projeção de MRR e Churn (Valores Anuais)

```
| Mês | Clientes Início | Novos Clientes | Clientes Churn | Clientes Fim | MRR Novo | MRR Churn | MRR Expansão | MRR Total | Churn Rate Clientes | ARPU |
|-----|-----------------|----------------|----------------|--------------|----------|-----------|--------------|-----------|---------------------|------|
| Jan | 1.000           | 100            | 50             | 1.050        | R$10.000 | R$5.000   | R$2.000      | R$107.000 | 4.76%               | R$101.90 |
| Fev | 1.050           | 110            | 53             | 1.107        | R$11.000 | R$5.300   | R$2.140      | R$114.840 | 4.78%               | R$103.74 |
| Mar | 1.107           | 120            | 56             | 1.171        | R$12.000 | R$5.600   | R$2.296      | R$123.536 | 4.78%               | R$105.50 |
| Abr | 1.171           | 130            | 60             | 1.241        | R$13.000 | R$6.000   | R$2.470      | R$132.996 | 4.83%               | R$107.17 |
```
*Observações*:
*   MRR Total = (Clientes Fim * ARPU) + MRR Expansão - MRR Churn (ou outra lógica de cálculo que se adeque, aqui ARPU é um valor médio e MRR Expansão/Churn são valores absolutos projetados).
*   Churn Rate Clientes = Clientes Churn / Clientes Início.
*   ARPU = MRR Total / Clientes Fim.

### Template de Análise LTV/CAC e Payback Period

```
| Métrica                   | Valor Calculado | Benchmark Ideal | Meta Interna | Status |
|---------------------------|-----------------|-----------------|--------------|--------|
| ARPU (Mensal)             | R$120,00        | Varia           | R$130,00     | Bom    |
| Margem Bruta por Cliente  | 75%             | > 70%           | 80%          | Bom    |
| Churn Rate Mensal         | 3%              | < 5%            | < 2%         | Atenção|
| LTV (Lifetime Value)      | R$3.000,00      | Varia           | R$4.000,00   | Bom    |
| CAC (Custo Aquisição)     | R$750,00        | Varia           | R$800,00     | Bom    |
| LTV/CAC Ratio             | 4:1             | > 3:1           | > 5:1        | Bom    |
| Payback Period do CAC     | 8 meses         | < 12 meses      | < 6 meses    | Bom    |
```
*Cálculos Utilizados*:
*   LTV = (ARPU * Margem Bruta) / Churn Rate Mensal (R$120 * 0.75) / 0.03 = R$90 / 0.03 = R$3.000
*   LTV/CAC Ratio = LTV / CAC = R$3.000 / R$750 = 4
*   Payback Period do CAC = CAC / (ARPU * Margem Bruta) = R$750 / (R$120 * 0.75) = R$750 / R$90 = 8.33 meses (arredondado para 8)

---

## Checklist

- [x] Validar a proposta de valor e os recursos oferecidos em cada plano de assinatura.
- [x] Realizar pesquisa de sensibilidade a preço (ex: Price Sensitivity Meter - PSM) com a base de clientes ideal.
- [x] Definir claramente os diferenciais e gatilhos de upgrade entre os planos.
- [x] Modelar o impacto de variações no churn, ARPU e expansão no MRR e LTV.
- [x] Estabelecer benchmarks internos e externos para MRR Growth, Churn Rate e LTV/CAC.
- [x] Planejar a comunicação e os incentivos para upsell, cross-sell e reengajamento de clientes em risco de churn.
- [x] Analisar a estratégia de precificação dos principais concorrentes diretos e indiretos.
- [x] Simular cenários de precificação (otimista, realista, pessimista) para avaliar riscos e oportunidades.
- [x] Desenvolver uma política transparente e justa para reajuste de preços de clientes existentes.
- [x] Identificar e precificar módulos adicionais (add-ons) ou funcionalidades premium (ex: mais armazenamento, suporte prioritário) para monetização extra.

---

## Métricas de Referência

| Métrica | Benchmark (SaaS B2B) | Meta (Empresa em Crescimento) |
|---------|----------------------|--------------------------------|
| MRR Growth | 5-10% Mês/Mês      | > 7% Mês/Mês                   |
| Churn Rate (Clientes Mensal) | < 5%                 | < 2%                           |
| Churn Rate (Receita Mensal)  | < 2%                 | < 1%                           |
| LTV/CAC Ratio | > 3:1                | > 5:1                          |
| Payback Period do CAC | < 12 meses           | < 6 meses                      |
| Net Revenue Retention (NRR) | > 100%               | > 110%                         |

---

## Erros Comuns

1.  **Precificar com base exclusivamente no custo de produção**: Não considerar o valor percebido pelo cliente leva a preços muito baixos (perdendo margem) ou muito altos (perdendo clientes), em vez de capturar o valor que a solução realmente entrega.
    *   **Como evitar**: Realize entrevistas com clientes para entender o ROI da sua solução para eles. Se um cliente economiza R$2.000/mês, cobrar R$150/mês é subestimar o valor.
2.  **Ignorar a taxa de churn**: Focar intensamente na aquisição de novos clientes sem uma estratégia robusta de retenção transforma o negócio em um "balde furado", onde a receita entra e sai rapidamente.
    *   **Como evitar**: Monitore o churn mensalmente, segmentando por cohort. Implemente programas de engajamento, suporte proativo e funcionalidades que promovam a adesão (stickiness). Por exemplo, clientes que não usam uma funcionalidade chave em 30 dias devem receber um e-mail com dicas de uso.
3.  **Diferenciação insuficiente entre os planos**: Oferecer planos de assinatura com funcionalidades muito semelhantes ou com saltos de preço desproporcionais confunde o cliente e não incentiva o upgrade.
    *   **Como evitar**: Crie uma matriz de funcionalidades x planos, garantindo que cada nível ofereça um valor incremental claro e que os preços reflitam esse valor. Por exemplo, o Plano Básico deve ser limitado para que o upgrade para o Pro seja atraente por funcionalidades essenciais.
4.  **Não ter uma estratégia clara de reajuste de preços**: Manter os preços estáticos por anos resulta em perda de receita devido à inflação e ao valor adicionado ao produto, enquanto os custos operacionais aumentam.
    *   **Como evitar**: Defina uma política de reajuste anual ou bienal, comunicando a mudança com antecedência e justificando-a com melhorias no produto. Considere diferentes abordagens, como reajustes apenas para novos clientes ou um reajuste gradual para os existentes.

---

## Dicas Avançadas

1.  **Precificação por Valor de Impacto (Value-Based Pricing)**: Em vez de precificar com base em funcionalidades, quantifique o valor financeiro (economias, ganhos de eficiência) que seu produto gera para o cliente e precifique uma fração desse valor.
    *   **Exemplo**: Se sua plataforma de automação economiza 20 horas de trabalho por mês para uma equipe (custo médio R$100/hora = R$2.000/mês de economia), você pode cobrar R$300-R$500/mês, capturando uma parte desse valor sem ser o custo total da economia.
2.  **Modelos Híbridos de Monetização**: Combine a assinatura base com precificação por uso (usage-based) ou por assento (seat-based) para escalar a receita conforme o cliente cresce e utiliza mais o serviço.
    *   **Exemplo**: Um plano base de R$99/mês (inclui 5 usuários e 1000 créditos de API), mais R$15/usuário adicional e R$0,01 por crédito de API excedente. Isso permite que clientes pequenos comecem com um custo baixo e que a receita cresça junto com o sucesso do cliente.
3.  **Análise Cohort Detalhada de Churn e LTV**: Em vez de observar métricas agregadas, segmente seus clientes por mês de aquisição e analise o comportamento de retenção e receita de cada grupo ao longo do tempo.
    *   **Exemplo**: Uma cohort de clientes adquiridos em janeiro de 2023 pode ter um churn de 8% após 3 meses, enquanto a cohort de março de 2023, após uma mudança na estratégia de onboarding, pode ter um churn de 5% no mesmo período. Isso revela o impacto direto das suas ações.
4.  **Testes de Elasticidade de Preço (Price Elasticity Testing)**: Utilize experimentos controlados (A/B testing, mas com cautela) em segmentos específicos para medir como pequenas variações de preço afetam a demanda e a receita total antes de implementar uma mudança em larga escala.
    *   **Exemplo**: Ofereça o "Plano Pro" por R$149/mês em uma landing page e por R$159/mês em outra landing page para um público-alvo similar, monitorando as taxas de conversão e o MRR gerado para cada preço.
5.  **Estratégias de Pacotes e Add-ons**: Crie pacotes de funcionalidades que resolvam problemas específicos para diferentes segmentos (bundle pricing) e ofereça add-ons opcionais para funcionalidades premium que não se encaixam na oferta base.
    *   **Exemplo**: Além dos planos Básico, Pro e Enterprise, ofereça um "Módulo de Relatórios Avançados" como um add-on de R$50/mês para qualquer plano, ou um "Pacote de Suporte 24/7" por R$100/mês.