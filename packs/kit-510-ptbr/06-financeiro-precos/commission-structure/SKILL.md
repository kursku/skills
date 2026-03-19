---
name: commission-structure
description: "Commission Structure — Skill especializada para criação, otimização e gestão de estruturas de comissão de vendas."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
---

# Commission Structure

Esta skill capacita o Claude Code a projetar, implementar e analisar planos de comissão de vendas eficazes, alinhando incentivos com metas estratégicas de negócios.

---

## Keywords

Comissão de Vendas, Pay Mix, Quota de Vendas, OTE (On-Target Earnings), Clawback, SPIFF, Estrutura Tiered, Flat Rate Commission, Comissão Residual, Draw contra Comissão, Aceleradores de Comissão, Cap de Comissão, Attainment, Custo de Vendas, LTV/CAC, Margem de Contribuição.

---

## Quick Start

1.  **Analise o desempenho histórico da equipe de vendas:** Colete dados de vendas, atingimento de quotas e OTEs de períodos anteriores para identificar padrões e benchmarks internos.
2.  **Defina o Pay Mix ideal (Salário Base vs. Comissão):** Para vendas B2B SaaS, um pay mix de 60/40 (60% salário base, 40% comissão) é um bom ponto de partida, enquanto para vendas transacionais pode ser 50/50.
3.  **Escolha um modelo de comissão primário:** Decida entre flat rate (taxa fixa), tiered (camadas de desempenho) ou um modelo híbrido, simulando o impacto financeiro de cada um.
4.  **Estabeleça quotas de vendas SMART:** Defina metas de receita ou volume que sejam Específicas, Mensuráveis, Alcançáveis, Relevantes e com Prazo Definido, baseadas em capacidade de mercado e dados históricos.

---

## Core Workflows

### Workflow 1: Design de uma Estrutura de Comissão Tiered para Vendas B2B SaaS com ACV

Este workflow detalha a criação de um plano de comissão baseado em tiers de atingimento de Annual Contract Value (ACV) para uma equipe de vendas B2B SaaS, visando incentivar alto desempenho e vendas de maior valor.

1.  **Análise de Desempenho Histórico e Mercado:**
    *   **Coleta de Dados Internos:** Reúna dados dos últimos 12-24 meses sobre o ACV médio por vendedor, taxa de conversão, duração do ciclo de vendas e o desempenho em relação às quotas passadas. Ex: Vendedor A (ACV médio R$75.000, 85% de atingimento de quota), Vendedor B (ACV médio R$110.000, 115% de atingimento de quota).
    *   **Pesquisa de Mercado:** Consulte relatórios de mercado (ex: SaaS Sales Benchmark Report) para entender os pay mixes e OTEs competitivos para a função de Sales Executive em SaaS. Ex: OTE médio para Sales Executive com 3-5 anos de experiência em São Paulo é R$180.000/ano.

2.  **Definição de Quotas e OTE (On-Target Earnings):**
    *   **Cálculo do OTE:** Determine o OTE total que um vendedor "on-target" deve ganhar. Ex: OTE anual = R$180.000.
    *   **Definição do Pay Mix:** Adote um pay mix de 60/40. Salário Base = R$180.000 * 0.60 = R$108.000/ano (R$9.000/mês). Comissão On-Target = R$180.000 * 0.40 = R$72.000/ano (R$6.000/mês).
    *   **Estabelecimento da Quota Anual de ACV:** Se a comissão on-target é R$72.000 e a taxa base de comissão é 10%, a Quota Anual de ACV = R$72.000 / 0.10 = R$720.000.

3.  **Estrutura de Tiers e Aceleradores:**
    *   **Tier 1 (0-80% da Quota):** Comissionamento de 8% sobre o ACV. Serve para incentivar vendas desde o início.
    *   **Tier 2 (81-100% da Quota):** Comissionamento de 10% sobre o ACV. Taxa padrão para atingimento da meta.
    *   **Tier 3 (101-120% da Quota):** Comissionamento de 12% sobre o ACV (Acelerador). Recompensa o alto desempenho.
    *   **Tier 4 (Acima de 120% da Quota):** Comissionamento de 15% sobre o ACV (Super Acelerador). Maximiza o incentivo para vendas excepcionais.

4.  **Exemplo de Cálculo de Comissão:**
    *   **Vendedor A:** Atinge 95% da quota anual (R$684.000 de ACV).
        *   Até 80% da quota (R$576.000): R$576.000 * 0.08 = R$46.080
        *   81-95% da quota (R$684.000 - R$576.000 = R$108.000): R$108.000 * 0.10 = R$10.800
        *   **Comissão Total Vendedor A:** R$46.080 + R$10.800 = R$56.880
    *   **Vendedor B:** Atinge 110% da quota anual (R$792.000 de ACV).
        *   Até 80% da quota (R$576.000): R$576.000 * 0.08 = R$46.080
        *   81-100% da quota (R$720.000 - R$576.000 = R$144.000): R$144.000 * 0.10 = R$14.400
        *   101-110% da quota (R$792.000 - R$720.000 = R$72.000): R$72.000 * 0.12 = R$8.640
        *   **Comissão Total Vendedor B:** R$46.080 + R$14.400 + R$8.640 = R$69.120

### Workflow 2: Implementação de Plano de Comissão com Clawback e SPIFFs para Vendas de Hardware B2C

Este workflow foca na gestão de comissões para vendas de hardware de alto valor no varejo, incluindo mecanismos para proteger a empresa contra devoluções e incentivos de curto prazo.

1.  **Definição do Gatilho de Pagamento da Comissão:**
    *   A comissão para a venda de um produto de hardware é paga após a confirmação da entrega ao cliente e o faturamento total, geralmente 30 dias após a compra, para permitir o processamento de eventuais devoluções iniciais. Ex: Venda realizada em 10/03, entrega em 15/03, comissão paga no contracheque de 30/04.

2.  **Implementação da Cláusula de Clawback (Estorno de Comissão):**
    *   **Definição:** Se um produto vendido for devolvido ou o cliente cancelar a compra dentro de um período específico após a venda (ex: 90 dias), a comissão correspondente será estornada do vendedor.
    *   **Exemplo:** Vendedor recebe R$300 de comissão pela venda de um laptop em 15/05. O cliente devolve o laptop em 10/07 (dentro do período de 90 dias). No contracheque de 30/07 ou 15/08, será aplicado um débito de R$300. Caso o vendedor não tenha comissões a receber ou o valor seja insuficiente, o débito será levado para o mês seguinte ou negociado um plano de pagamento.

3.  **Criação de SPIFFs (Sales Performance Incentive Funds):**
    *   **Objetivo:** Incentivos de curto prazo para impulsionar vendas de produtos específicos, escoar estoque antigo ou focar em categorias de alta margem.
    *   **Exemplo 1 (Lançamento de Produto):** "SPIFF Lançamento Modelo X": Adicional de R$150 por cada unidade do novo "Smartphone Ultra" vendida no mês de lançamento (01/04 a 30/04).
    *   **Exemplo 2 (Estoque Antigo):** "SPIFF Queima de Estoque Modelo Y": Bônus de R$100 por cada "Tablet Pro 2022" vendido em um período de 15 dias (05/05 a 20/05).
    *   **Exemplo 3 (Acessórios de Alto Valor):** "SPIFF Combo Premium": R$50 por cada venda de um combo de "Console + 2 Controles + Jogo A".
    *   **Regra:** SPIFFs são pagos separadamente da comissão regular e não estão sujeitos a clawback, a menos que especificado explicitamente na política do SPIFF.

4.  **Acompanhamento e Relatórios de Transparência:**
    *   Gere um extrato de comissão mensal detalhado para cada vendedor, incluindo:
        *   Vendas brutas elegíveis para comissão.
        *   Valores de comissão por venda.
        *   Total de comissões acumuladas.
        *   Quaisquer clawbacks aplicados com referência à venda original.
        *   SPIFFs ganhos e o período a que se referem.
        *   Total líquido a receber.
    *   Ex: Relatório mostrando "Venda Laptop X - R$300", "Venda Smartphone Ultra (SPIFF) - R$150", "Clawback Laptop Z (Venda 2 meses atrás) - R$250", "Total a Pagar: R$200".

---

## Templates

### Template de Planilha de Cálculo de Comissão Tiered Mensal

```
PLANILHA DE CÁLCULO DE COMISSÃO DE VENDAS MENSAL - EQUIPE B2B SAAS

Mês de Referência: Setembro/2025
Quota Anual por Vendedor: R$ 720.000
Quota Mensal Alvo por Vendedor: R$ 60.000 (R$ 720.000 / 12)

Estrutura de Comissão Tiered (Base ACV):
- Tier 1 (0-80% da Quota Mensal): 8%
- Tier 2 (81-100% da Quota Mensal): 10%
- Tier 3 (101-120% da Quota Mensal): 12%
- Tier 4 (Acima de 120% da Quota Mensal): 15%

| Vendedor | Salário Base Mensal | Quota Mensal (R$) | Vendas Brutas (ACV - R$) | % Atingido da Quota | Comissão Tier 1 (R$) | Comissão Tier 2 (R$) | Comissão Tier 3 (R$) | Comissão Tier 4 (R$) | Total Comissão (R$) | OTE Projetado (R$) |
|----------|---------------------|-------------------|--------------------------|---------------------|----------------------|----------------------|----------------------|----------------------|---------------------|--------------------|
| Ana Silva| R$ 9.000            | R$ 60.000         | R$ 45.000                | 75%                 | R$ 3.600             | R$ 0                 | R$ 0                 | R$ 0                 | R$ 3.600            | R$ 12.600          |
| Bruno Vaz| R$ 9.000            | R$ 60.000         | R$ 57.000                | 95%                 | R$ 3.840             | R$ 1.800             | R$ 0                 | R$ 0                 | R$ 5.640            | R$ 14.640          |
| Carla Melo| R$ 9.000            | R$ 60.000         | R$ 66.000                | 110%                | R$ 3.840             | R$ 2.400             | R$ 720               | R$ 0                 | R$ 6.960            | R$ 15.960          |
| Daniel Luz| R$ 9.000            | R$ 60.000         | R$ 78.000                | 130%                | R$ 3.840             | R$ 2.400             | R$ 1.440             | R$ 1.800             | R$ 9.480            | R$ 18.480          |
```
*Cálculos de Exemplo (Bruno Vaz - 95%):*
- Vendas Brutas: R$ 57.000
- 80% da Quota: R$ 48.000 (R$ 60.000 * 0.80)
- Comissão Tier 1: R$ 48.000 * 0.08 = R$ 3.840
- Vendas restantes para Tier 2: R$ 57.000 - R$ 48.000 = R$ 9.000
- Comissão Tier 2: R$ 9.000 * 0.10 = R$ 900
- Total Comissão: R$ 3.840 + R$ 900 = R$ 4.740 (Erro no exemplo preenchido acima, ajustando aqui para R$ 3.840 + R$ 900 = R$ 4.740 para Bruno Vaz. O preenchimento está incorreto para Bruno. Vamos corrigir o template.)

**CORREÇÃO DO TEMPLATE:**

```
PLANILHA DE CÁLCULO DE COMISSÃO DE VENDAS MENSAL - EQUIPE B2B SAAS

Mês de Referência: Setembro/2025
Quota Anual por Vendedor: R$ 720.000
Quota Mensal Alvo por Vendedor: R$ 60.000 (R$ 720.000 / 12)

Estrutura de Comissão Tiered (Base ACV):
- Tier 1 (0-80% da Quota Mensal): 8% (até R$ 48.000)
- Tier 2 (81-100% da Quota Mensal): 10% (de R$ 48.001 a R$ 60.000)
- Tier 3 (101-120% da Quota Mensal): 12% (de R$ 60.001 a R$ 72.000)
- Tier 4 (Acima de 120% da Quota Mensal): 15% (acima de R$ 72.000)

| Vendedor | Salário Base Mensal | Quota Mensal (R$) | Vendas Brutas (ACV - R$) | % Atingido da Quota | Comissão Tier 1 (R$) | Comissão Tier 2 (R$) | Comissão Tier 3 (R$) | Comissão Tier 4 (R$) | Total Comissão (R$) | OTE Projetado (R$) |
|----------|---------------------|-------------------|--------------------------|---------------------|----------------------|----------------------|----------------------|----------------------|---------------------|--------------------|
| Ana Silva| R$ 9.000            | R$ 60.000         | R$ 45.000                | 75%                 | R$ 3.600             | R$ 0                 | R$ 0                 | R$ 0                 | R$ 3.600            | R$ 12.600          |
| Bruno Vaz| R$ 9.000            | R$ 60.000         | R$ 57.000                | 95%                 | R$ 3.840             | R$ 900               | R$ 0                 | R$ 0                 | R$ 4.740            | R$ 13.740          |
| Carla Melo| R$ 9.000            | R$ 60.000         | R$ 66.000                | 110%                | R$ 3.840             | R$ 1.200             | R$ 720               | R$ 0                 | R$ 5.760            | R$ 14.760          |
| Daniel Luz| R$ 9.000            | R$ 60.000         | R$ 78.000                | 130%                | R$ 3.840             | R$ 1.200             | R$ 1.440             | R$ 900               | R$ 7.380            | R$ 16.380          |
```

### Template de Política de Clawback de Comissão

```
POLÍTICA DE CLAWBACK DE COMISSÃO DE VENDAS

**Data de Efetividade:** 1 de Outubro de 2025
**Versão:** 1.0

**1. Objetivo:**
Esta política estabelece as condições sob as quais as comissões de vendas pagas a representantes de vendas podem ser estornadas ("clawback") pela [Nome da Empresa]. O objetivo é garantir a sustentabilidade financeira da empresa e alinhar os incentivos de vendas com a retenção de clientes e a qualidade das transações.

**2. Definição de Clawback:**
Clawback refere-se ao processo de recuperação, por parte da empresa, de comissões previamente pagas a um vendedor, quando a transação subjacente à qual a comissão estava vinculada não se concretiza ou é revertida.

**3. Cenários de Aplicação:**
O clawback será aplicado nos seguintes cenários:

*   **Cancelamento de Venda:** Se um cliente cancelar um contrato ou devolver um produto dentro de [90 dias] da data de faturamento/entrega.
*   **Inadimplência Crônica:** Se um cliente se tornar inadimplente e a dívida for considerada irrecuperável pela equipe financeira, após [120 dias] da data de vencimento da primeira parcela ou fatura.
*   **Fraude ou Erro:** Se a comissão for paga com base em dados fraudulentos ou erros de cálculo.
*   **Downgrade Significativo:** Para contratos de serviço, se houver um downgrade de plano que resulte em uma redução de [25% ou mais] do valor original dentro de [6 meses] da ativação.

**4. Período de Clawback:**
O período de elegibilidade para clawback é de [90 dias] a partir da data de faturamento ou entrega do produto/serviço, exceto para casos de inadimplência crônica ou fraude.

**5. Cálculo do Valor do Clawback:**
O valor do clawback será igual ao valor total da comissão paga ao vendedor para a transação específica que foi cancelada, devolvida ou que resultou em inadimplência/fraude. Em casos de downgrade, o clawback será proporcional à redução da comissão original.

**6. Processo de Notificação:**
O vendedor será notificado por escrito sobre qualquer aplicação de clawback com pelo menos [15 dias] de antecedência da data em que o valor será deduzido do seu contracheque ou de futuras comissões. A notificação incluirá detalhes da transação afetada e o valor do estorno.

**7. Dedução da Comissão:**
O valor do clawback será deduzido das futuras comissões a serem pagas ao vendedor. Caso o vendedor não tenha comissões futuras suficientes para cobrir o valor do clawback, a empresa se reserva o direito de deduzir o valor de outras remunerações permitidas por lei.

**8. Exceções:**
Quaisquer exceções a esta política devem ser aprovadas por escrito pela [Diretoria de Vendas e Departamento Financeiro].

**9. Revisão da Política:**
Esta política será revisada anualmente ou conforme a necessidade para garantir sua relevância e eficácia.

**Declaração de Aceitação:** Ao assinar seu contrato de trabalho ou aceitar seu plano de comissão, o vendedor concorda com os termos desta política de clawback.
```

---

## Checklist

- [x] Analisar o custo total de vendas (salário base + comissão + bônus) como % da receita para garantir sustentabilidade.
- [x] Definir um "pay mix" (salário base vs. comissão) que seja competitivo no mercado e alinhado com o ciclo de vendas do produto.
- [x] Estabelecer quotas de vendas SMART (Specific, Measurable, Achievable, Relevant, Time-bound) baseadas em dados históricos e projeções realistas.
- [x] Validar a estrutura de comissão através de simulações de cenários (vendedor abaixo da quota, on-target, acima da quota) para prever o impacto financeiro e motivacional.
- [x] Incluir cláusulas de clawback claras para proteger a empresa contra devoluções, cancelamentos ou inadimplência, especificando o período e as condições.
- [x] Comunicar a estrutura de comissão de forma transparente e detalhada a toda a equipe de vendas, garantindo que todos compreendam como seus ganhos são calculados.
- [x] Implementar um sistema de tracking e relatórios de comissão preciso e acessível, que permita aos vendedores acompanhar seu desempenho em tempo real.
- [x] Prever SPIFFs ou bônus de curto prazo para incentivar comportamentos específicos (ex: venda de produtos de alto valor, novos clientes, renovações).
- [x] Considerar a relação LTV/CAC (Lifetime Value do Cliente / Custo de Aquisição de Cliente) ao definir o custo de vendas e o teto de comissão.
- [x] Assegurar que a estrutura de comissão esteja em conformidade com as leis trabalhistas e regulamentações fiscais aplicáveis.
- [x] Realizar revisões periódicas (trimestrais ou anuais) da estrutura de comissão, coletando feedback da equipe e ajustando conforme as metas de negócio e o desempenho.
- [x] Avaliar se a estrutura incentiva a venda de produtos de maior margem ou estratégicos, em vez de apenas volume bruto.

---

## Métricas de Referência

| Métrica |