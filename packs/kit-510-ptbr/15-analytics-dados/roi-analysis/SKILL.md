---
name: roi-analysis
description: "Roi Analysis — Skill especializada para calcular e otimizar o Retorno sobre Investimento (ROI) de campanhas e ações de marketing digital."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Roi Analysis

Esta skill capacita o Claude a realizar análises completas de Retorno sobre Investimento (ROI) para campanhas de marketing digital, integrando dados de Google Analytics, plataformas de custo e CRM, focando na otimização de performance.

---

## Keywords

ROI Marketing Digital, Análise de Performance, GA4 Attribution, Custo de Aquisição de Cliente (CAC), Valor de Tempo de Vida do Cliente (LTV), ROAS (Return on Ad Spend), CPA (Custo Por Aquisição), Modelagem de Atribuição de Marketing, Otimização de Orçamento, Google Analytics 4, Funil de Conversão, Data Import GA4, Receita de Vendas, Margem Bruta, Cohort Analysis.

---

## Quick Start

1.  **Configurar Eventos de Conversão no GA4**: Garanta que eventos críticos como `purchase` (compra), `generate_lead` (gerar lead) e `form_submit` (envio de formulário) estejam configurados no Google Analytics 4 com seus respectivos valores de receita ou potencial de receita.
2.  **Vincular Contas de Mídia ao GA4**: Conecte Google Ads, Search Console e outras plataformas de custo suportadas diretamente ao GA4 para importação automática de dados de custo e impressões. Para plataformas não nativas (e.g., Facebook Ads), prepare um arquivo CSV para Data Import.
3.  **Acessar Relatório de Aquisição no GA4**: Navegue até `Relatórios > Aquisição > Aquisição de tráfego` no GA4. Personalize este relatório para incluir métricas de receita e custo se já tiver importado os dados de custo.
4.  **Exportar Dados de Custo e Receita**: Exporte os dados de custo das plataformas de mídia e os dados de receita/conversão do GA4 para um Google Sheet para consolidação.
5.  **Calcular o ROI Inicial**: Utilize a fórmula `(Receita Total - Custo Total) / Custo Total * 100%` para obter uma visão primária do ROI de uma campanha ou canal específico.

---

## Core Workflows

### Workflow 1: Cálculo e Otimização de ROI de Campanhas de Google Ads com GA4

Este workflow detalha o processo para calcular o ROI de campanhas de Google Ads usando dados de receita do GA4 e otimizar o investimento.

**Passos detalhados:**

1.  **Verificação de Vinculação GA4 e Google Ads**:
    *   No GA4, vá em `Administrador > Vinculações de produtos > Vinculações do Google Ads`.
    *   Confirme se a conta de Google Ads está vinculada e que as configurações de importação de dados estão ativas. Isso garante que os dados de custo do Google Ads apareçam nos relatórios do GA4.
    *   **Exemplo**: A conta 'Minha Loja Online' (ID 123-456-7890) está vinculada e a opção 'Ativar a publicidade personalizada' está marcada.

2.  **Configuração de Eventos de Conversão no GA4**:
    *   Acesse `Administrador > Eventos > Conversões`.
    *   Verifique se o evento `purchase` (para e-commerce) ou `generate_lead` (para geração de leads) está marcado como conversão e possui um valor monetário associado, se aplicável. Para `purchase`, o valor é enviado automaticamente. Para `generate_lead`, um valor padrão pode ser atribuído via GTM ou no GA4 se o lead tiver um valor médio de venda conhecido.
    *   **Exemplo**: O evento `purchase` está ativo como conversão e o evento `generate_lead` tem um valor de US$ 50,00 atribuído manualmente no GA4 para leads qualificados.

3.  **Análise de Dados de Aquisição no GA4**:
    *   Navegue para `Relatórios > Aquisição > Aquisição de tráfego`.
    *   Adicione uma dimensão secundária `Campanha` (para Google Ads) ou `Origem/Meio` (para uma visão mais ampla).
    *   Verifique as colunas `Receita total` (ou `Receita da compra` para e-commerce), `Conversões` e `Custo`. Se a vinculação do Google Ads estiver correta, a coluna `Custo` para o tráfego do Google Ads será preenchida.
    *   **Exemplo**: Relatório mostra a campanha "Oferta Black Friday 2023" do Google Ads com um custo de R$ 7.500,00, gerando 150 conversões de `purchase` e R$ 25.000,00 em receita.

4.  **Cálculo do ROI da Campanha**:
    *   Utilize a fórmula `ROI = ((Receita Total - Custo Total) / Custo Total) * 100%`.
    *   **Exemplo**: Para a campanha "Oferta Black Friday 2023":
        *   Receita Total = R$ 25.000,00
        *   Custo Total = R$ 7.500,00
        *   ROI = ((25.000 - 7.500) / 7.500) * 100% = (17.500 / 7.500) * 100% = 233,33%

5.  **Otimização Baseada no ROI**:
    *   Campanhas com ROI > 100% são lucrativas. Concentre esforços em otimizar as que têm ROI mais alto, escalando o investimento ou melhorando a segmentação.
    *   Campanhas com ROI < 100% estão gerando prejuízo. Analise as palavras-chave, criativos, páginas de destino e segmentação para identificar gargalos. Considere pausar ou reestruturar.
    *   **Exemplo**: A campanha "Oferta Black Friday 2023" com 233,33% de ROI indica que há espaço para aumentar o orçamento, mantendo um ROAS saudável. Outra campanha "Liquidacao Inverno", com ROI de 80%, precisa de revisão imediata na segmentação de público ou nas palavras-chave negativas.

### Workflow 2: Análise de LTV/CAC e Atribuição Multicanal para Otimização de Investimento

Este workflow foca em entender o valor de longo prazo do cliente e o custo de aquisição, usando modelos de atribuição para alocar o orçamento de forma mais inteligente.

**Passos detalhados:**

1.  **Cálculo do Custo de Aquisição de Cliente (CAC)**:
    *   Consolide o custo total de marketing (Google Ads, Facebook Ads, SEO, etc.) em um período específico (e.g., último trimestre).
    *   Conte o número de novos clientes adquiridos no mesmo período (disponível via CRM ou eventos de `first_purchase`/`new_user` no GA4).
    *   Fórmula: `CAC = Custo Total de Marketing / Número de Novos Clientes`.
    *   **Exemplo**: No último trimestre, o investimento total em marketing foi de R$ 30.000,00 e foram adquiridos 300 novos clientes. CAC = R$ 30.000,00 / 300 = R$ 100,00 por cliente.

2.  **Cálculo do Valor de Tempo de Vida do Cliente (LTV)**:
    *   **LTV Simples**: `LTV = (Receita Média por Cliente * Margem Bruta Média) / Taxa de Churn`.
        *   `Receita Média por Cliente`: Total de receita de vendas / Número de clientes.
        *   `Margem Bruta Média`: (Receita - Custo dos produtos vendidos) / Receita.
        *   `Taxa de Churn`: (Número de clientes perdidos em um período / Número de clientes no início do período) * 100%.
    *   **Exemplo**: Uma loja de assinaturas tem uma receita média por cliente de R$ 150,00/mês, margem bruta de 60% e taxa de churn mensal de 5%.
        *   LTV Mensal = (150 * 0.60) / 0.05 = 90 / 0.05 = R$ 1.800,00.
        *   Este LTV deve ser comparado com o CAC.

3.  **Análise da Razão LTV/CAC**:
    *   Compare o LTV com o CAC. Uma razão LTV/CAC de 3:1 ou superior é geralmente considerada saudável.
    *   **Exemplo**: LTV de R$ 1.800,00 e CAC de R$ 100,00. LTV/CAC = 1800/100 = 18:1. Este é um excelente resultado, indicando que o investimento em marketing está gerando um retorno muito alto no longo prazo.

4.  **Utilização da Modelagem de Atribuição no GA4**:
    *   Acesse `Publicidade > Atribuição > Comparação de modelos` no GA4.
    *   Selecione os eventos de conversão (e.g., `purchase`).
    *   Compare diferentes modelos de atribuição: "Último clique (pago e orgânico)" vs. "Baseado em dados" (se disponível) ou "Linear".
    *   **Exemplo**: Ao comparar o modelo "Último clique" com o "Baseado em dados" para o evento `purchase`, observa-se que o canal "Display" tem 10% mais conversões atribuídas no modelo "Baseado em dados" do que no "Último clique". Isso sugere que Display tem um papel importante na parte superior do funil, contribuindo para conversões posteriores, e deve receber mais crédito e talvez mais orçamento.

5.  **Otimização de Orçamento Baseada em LTV/CAC e Atribuição**:
    *   Alocar mais orçamento para canais que demonstram ter um baixo CAC e um alto LTV/CAC, ajustando as métricas de acordo com a atribuição "Baseada em dados".
    *   Redirecionar investimentos de canais com alto CAC e baixo LTV/CAC, ou que contribuem pouco nos modelos de atribuição mais sofisticados.
    *   **Exemplo**: Com um LTV/CAC de 18:1 e a análise de atribuição mostrando que "Display" tem um papel inicial importante, a decisão é aumentar o orçamento para campanhas de Display, pois elas estão contribuindo para um LTV alto e a atribuição "Baseada em dados" valida seu papel na jornada do cliente.

---

## Templates

### Template de Relatório de ROI por Canal (Mensal)

```
# Relatório de Performance de Marketing - [Mês/Ano]

## Visão Geral de ROI por Canal

| Canal de Marketing | Custo Total (R$) | Receita Atribuída (R$) | ROI (%) | ROAS (R$) | CAC (R$) |
|--------------------|------------------|------------------------|---------|-----------|----------|
| Google Ads (Search)| 12.000,00        | 38.000,00              | 216,67% | 3,17:1    | 95,00    |
| Google Ads (Display)| 5.000,00         | 12.000,00              | 140,00% | 2,40:1    | 120,00   |
| Facebook Ads        | 10.000,00        | 28.000,00              | 180,00% | 2,80:1    | 112,00   |
| SEO (Orgânico)     | 2.000,00*        | 25.000,00              | 1150,00%| 12,50:1   | 40,00    |
| E-mail Marketing    | 1.500,00         | 15.000,00              | 900,00% | 10,00:1   | 50,00    |
| **Total Geral**    | **30.500,00**    | **118.000,00**         | **286,89%**| **3,87:1** | **85,00**|

*Custo SEO considera investimento em ferramentas e agência, não diretamente por aquisição individual.

## Análise de LTV/CAC

*   **LTV Médio por Cliente**: R$ 350,00
*   **CAC Médio por Cliente**: R$ 85,00
*   **Razão LTV/CAC**: 4,12:1 (Ideal > 3:1)

## Recomendações:
*   **Google Ads (Search)**: Manter investimento, explorar expansão de palavras-chave de cauda longa, otimizar lances para termos de alta performance.
*   **Google Ads (Display)**: Aumentar o budget em 15% devido ao papel de topo de funil e ROI positivo, focar em públicos semelhantes e in-market.
*   **Facebook Ads**: Revisar criativos e segmentação para melhorar a taxa de cliques e conversão, buscando reduzir o CAC e aumentar o ROI.
*   **SEO (Orgânico)**: Continuar investimento em conteúdo e link building, pois apresenta o maior ROI e menor CAC, indicando sustentabilidade a longo prazo.
*   **E-mail Marketing**: Explorar automações de funil e segmentação mais granular para escalar o volume de conversões.
```

### Template de Cálculo de ROI Detalhado (Projeto Específico)

```
# Análise Detalhada de ROI - Lançamento Produto X (Período: 01/01/2024 - 31/03/2024)

## Entradas de Dados:

*   **Receita Bruta Gerada (GA4)**: R$ 50.000,00
*   **Número de Unidades Vendidas**: 500
*   **Preço Médio por Unidade**: R$ 100,00
*   **Custo de Mercadoria Vendida (CMV) por Unidade**: R$ 30,00
*   **Custo Total de Mídia (Google Ads, Facebook Ads)**: R$ 15.000,00
*   **Custo de Produção de Criativos/Conteúdo**: R$ 2.000,00
*   **Custo de Agência/Gestão de Campanhas**: R$ 3.000,00
*   **Outros Custos Diretos (Landing Page, Ferramentas)**: R$ 500,00

## Cálculos:

1.  **Custo Total de Mercadoria Vendida (CMV Total)**:
    *   `CMV Total = Número de Unidades Vendidas * CMV por Unidade`
    *   `CMV Total = 500 * R$ 30,00 = R$ 15.000,00`

2.  **Custo Total de Marketing**:
    *   `Custo Marketing = Custo Total de Mídia + Custo de Produção + Custo de Agência`
    *   `Custo Marketing = R$ 15.000,00 + R$ 2.000,00 + R$ 3.000,00 = R$ 20.000,00`

3.  **Custo Total do Projeto**:
    *   `Custo Total = CMV Total + Custo Marketing + Outros Custos Diretos`
    *   `Custo Total = R$ 15.000,00 + R$ 20.000,00 + R$ 500,00 = R$ 35.500,00`

4.  **Lucro Líquido do Projeto**:
    *   `Lucro Líquido = Receita Bruta Gerada - Custo Total do Projeto`
    *   `Lucro Líquido = R$ 50.000,00 - R$ 35.500,00 = R$ 14.500,00`

5.  **Retorno sobre Investimento (ROI)**:
    *   `ROI = (Lucro Líquido / Custo Total do Projeto) * 100%`
    *   `ROI = (R$ 14.500,00 / R$ 35.500,00) * 100% = 40,85%`

## Conclusão:
O lançamento do Produto X obteve um ROI de 40,85%. Embora positivo, este valor indica que há espaço significativo para otimização, especialmente na redução dos custos de marketing ou no aumento do preço médio/unidades vendidas. Recomenda-se analisar a fundo a performance de cada canal de mídia e a rentabilidade do produto em si.
```

---

## Checklist

- [ ] Google Analytics 4 implementado corretamente e coletando dados de tráfego e engajamento.
- [ ] Eventos de conversão (e.g., `purchase`, `generate_lead`) configurados no GA4 com valores de receita ou potencial de receita.
- [ ] Vinculações de contas de mídia (Google Ads, Search Console) com o GA4 estabelecidas e ativas.
- [ ] Dados de custo de outras plataformas de mídia (e.g., Facebook Ads) importados para o GA4 via Data Import (CSV) ou API.
- [ ] Período de análise definido e consistente entre todas as fontes de dados (GA4, plataformas de mídia, CRM).
- [ ] Receita bruta total da campanha ou projeto apurada, preferencialmente via GA4 ou CRM.
- [ ] Custos diretos da campanha (mídia, produção de criativos, gerenciamento) consolidados.
- [ ] Custo de Aquisição de Cliente (CAC) calculado por canal ou segmento.
- [ ] Valor de Tempo de Vida do Cliente (LTV) calculado ou estimado para os segmentos de clientes relevantes.
- [ ] Modelos de atribuição no GA4 (e.g., "Baseado em dados", "Linear") analisados para entender a contribuição de cada canal.
- [ ] Margem bruta dos produtos/serviços considerada nos cálculos de rentabilidade.
- [ ] Dashboards de ROI e performance construídos em ferramentas como Looker Studio (Google Data Studio) para acompanhamento contínuo.

---

## Métricas de Referência

| Métrica               | Benchmark (Indústria Geral) | Meta (E-commerce/SaaS B2C) |
|-----------------------|-----------------------------|----------------------------|
| ROI (Marketing Digital)| 150% - 400%                 | 250% - 500%                |
| ROAS (e-commerce)     | 3:1 - 5:1                   | 4:1 - 6:1                  |
| CAC (serviços digitais)| R$ 50 - R$ 300              | R$ 70 - R$ 180             |
| LTV/CAC Ratio         | 3:1 ou superior             | 4:1 ou superior            |
| Taxa de Conversão (e-commerce) | 1% - 3%                     | 2% - 5%                    |
| CPA (Custo por Aquisição) | R$ 20 - R$ 150 (Lead)       | R$ 30 - R$ 80 (Lead Qualificado)|

---

## Erros Comuns

1.  **Atribuição Incorreta/Simplista**: Basear toda a análise no modelo de "Último Clique" ignora o papel de outros pontos de contato na jornada do cliente.
    *   **Como evitar**: Sempre utilize o relatório de `Comparação de modelos` no GA4, comparando "Último Clique" com "Baseado em dados" ou "Linear". Isso revela quais canais contribuem no topo e meio do funil, permitindo uma alocação de orçamento mais estratégica. Por exemplo, um canal de Display pode ter baixo ROI no último clique, mas alto impacto em um modelo "Baseado em dados" que reconhece sua influência inicial.
2.  **Ignorar Custos Indiretos**: Considerar apenas o custo de mídia (e.g., Google Ads) e desconsiderar custos de criação de conteúdo, gestão de agência, ferramentas de marketing e horas de equipe interna.
    *   **Como evitar**: Mantenha um registro detalhado de *todos* os custos associados à campanha ou ao projeto de marketing, incluindo salários da equipe dedicada, licenças de software, custos de design e produção de vídeo. Use o "Template de Cálculo de ROI Detalhado" para garantir que todos os custos sejam contabilizados. Por exemplo, a produção de um vídeo para uma campanha de YouTube Ads custou R$ 5.000,00 e este valor deve ser somado ao custo da mídia.
3.  **Período de Análise Inconsistente**: Comparar dados de custo de um mês com dados de receita do GA4 de outro período, ou de diferentes janelas de atribuição.
    *   **Como evitar**: Padronize rigorosamente o período de análise para todas as fontes de dados. Se estiver analisando o ROI de uma campanha de janeiro, os dados de custo e receita (e as conversões) devem ser exclusivamente de janeiro. Além disso, esteja ciente da janela de atribuição do GA4 (padrão de 90 dias para aquisição e 30 dias para outros eventos) ao analisar o impacto de longo prazo.

---

## Dicas Avançadas

1.  **Segmentação de Audiências por LTV no GA4**: Crie audiências personalizadas no GA4 baseadas no LTV estimado ou histórico de compras dos usuários. Use essas audiências para retargeting com ofertas personalizadas ou para exclusão em campanhas de aquisição. Por exemplo, uma audiência de "Clientes de Alto LTV" pode receber campanhas de upsell exclusivas, enquanto é excluída de campanhas de prospecção para não gastar orçamento desnecessariamente.
2.  **Análise de Cohort para LTV e Retenção**: Utilize os relatórios de `Explorações > Análise de cohort` no GA4 para entender como o LTV e a retenção de clientes evoluem ao longo do tempo para grupos de usuários adquiridos em diferentes períodos ou por diferentes canais. Isso ajuda a identificar quais canais trazem clientes mais leais e de maior valor. Por exemplo, um cohort de clientes adquiridos via SEO em março pode ter um LTV 20% maior após 6 meses do que um cohort adquirido via Facebook Ads no mesmo período.
3.  **Integração de Dados de CRM com GA4 via User-ID**: Implemente o User-ID no GA4 para unificar a jornada do cliente online e offline. Ao enviar dados de vendas e interações do CRM (e.g., Salesforce, HubSpot) para o GA4 via Measurement Protocol ou Data Import, é possível ter uma visão completa do ROI, incluindo o impacto de vendas assistidas por marketing digital que se concretizam offline. Isso permite calcular o ROI real de ponta a ponta.
4.  **Modelagem de Atribuição Preditiva com Machine Learning**: Para cenários mais complexos, vá além dos modelos de atribuição padrão do GA4. Utilize ferramentas de Machine Learning (e.g., Python com bibliotecas como `sklearn` ou plataformas de ML) para construir modelos de atribuição personalizados que consideram centenas de variáveis e interações, fornecendo uma distribuição de crédito de conversão mais precisa e otimizada para o seu negócio específico. Isso pode revelar canais que são subvalorizados por modelos mais simples.
5.  **Simulação de Orçamento Baseada em ROI/ROAS**: Use os dados históricos de ROI e ROAS para criar modelos de simulação que projetam o impacto de diferentes alocações de orçamento. Ferramentas como o "Planejador de Performance" do Google Ads, ou planilhas mais avançadas, podem ajudar a visualizar como um aumento ou diminuição no investimento em um canal específico pode afetar o ROI geral e o volume de conversões, auxiliando na tomada de decisões estratégicas de alocação de verba.