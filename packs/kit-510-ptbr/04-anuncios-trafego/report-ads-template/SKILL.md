---
name: report-ads-template
description: "Report Ads Template — Skill especializada para report ads template"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Report Ads Template

Esta skill capacita o usuário a construir, analisar e apresentar relatórios de performance de campanhas de anúncios digitais em Meta Ads, Google Ads e TikTok Ads, focando em insights acionáveis para otimização.

---

## Keywords

Relatório de Anúncios, Performance de Ads, Otimização de Campanhas, Análise de Dados, Meta Ads Report, Google Ads Report, TikTok Ads Report, ROAS, CPC, CTR, CPA, Dashboard de Marketing, Métricas de Anúncios, Relatório de Tráfego Pago, Gestão de Campanhas.

---

## Quick Start

1.  **Extração de Dados Brutos**: Baixe os dados de performance do período desejado (ex: semanal) do Meta Ads Manager (Relatórios -> Personalizar colunas e quebras), Google Ads (Relatórios -> Personalizado -> Tabela) e TikTok Ads (Relatórios -> Customizado).
2.  **Consolidação em Planilha**: Importe os arquivos CSV/XLSX para um Google Sheets ou Excel, criando abas separadas para cada plataforma (ex: `Meta_Semanal`, `Google_Semanal`, `TikTok_Semanal`).
3.  **Cálculo de Métricas Chave**: Insira colunas calculadas para ROAS (`Valor Conversão / Custo`), CPA (`Custo / Conversões`) e CTR (`Cliques / Impressões`) em cada aba, garantindo que os dados sejam consistentes.
4.  **Criação de Resumo Consolidado**: Na primeira aba do seu documento (ex: `Dashboard_Geral`), monte uma tabela resumo que agregue as métricas mais importantes de todas as plataformas para o período analisado.
5.  **Identificação de Destaques e Pontos de Atenção**: Revise o resumo consolidado e as abas detalhadas para identificar rapidamente campanhas, conjuntos de anúncios ou anúncios com performance excepcional ou que necessitam de otimização urgente.

---

## Core Workflows

### Workflow 1: Análise Semanal de Performance Detalhada (Meta Ads e Google Ads)

Este workflow foca em dissecar a performance de campanhas no nível de conjunto de anúncios/grupo de anúncios e anúncio para identificar problemas e oportunidades.

*   **Passo 1: Exportação de Dados Nivelada**:
    *   **Meta Ads Manager**: Acesse "Relatórios", crie um relatório personalizado com as colunas: "Campanha", "Conjunto de Anúncios", "Anúncio", "Impressões", "Cliques", "CTR (Taxa de Cliques no Link)", "CPM (Custo por 1.000 impressões)", "CPC (Custo por Clique no Link)", "Gastos", "Resultados (Compras)", "Custo por Resultado (CPA)", "Valor de Conversão (Compras)". Defina o período para "Últimos 7 dias".
    *   **Google Ads**: Acesse "Relatórios", "Personalizado", "Tabela". Adicione "Campanha", "Grupo de Anúncios", "Anúncio", "Impressões", "Cliques", "CTR", "CPC Méd.", "Custo", "Conversões", "Valor de Conversão". Defina o período para "Últimos 7 dias".
    *   Exporte ambos os relatórios em formato CSV.

*   **Passo 2: Consolidação e Preparação da Planilha**:
    *   Crie um novo Google Sheets. Renomeie a primeira aba como `Meta_Semanal` e importe o CSV do Meta Ads.
    *   Renomeie a segunda aba como `Google_Semanal` e importe o CSV do Google Ads.
    *   **Cálculo de KPIs Derivados**:
        *   Na aba `Meta_Semanal`, adicione as colunas:
            *   `ROAS Meta = [Valor de Conversão (Compras)] / [Gastos]`
            *   `CPA Meta = [Gastos] / [Resultados (Compras)]` (apenas se `Resultados (Compras)` > 0)
        *   Na aba `Google_Semanal`, adicione as colunas:
            *   `ROAS Google = [Valor de Conversão] / [Custo]`
            *   `CPA Google = [Custo] / [Conversões]` (apenas se `Conversões` > 0)

*   **Passo 3: Análise Pormenorizada e Identificação de Ações**:
    *   **Meta Ads**:
        *   Filtre a aba `Meta_Semanal` por ROAS < 2.0 (para e-commerce com margem de 50%) ou CPA > R$ 60,00. Analise os conjuntos de anúncios e anúncios dentro dessas campanhas de baixa performance.
        *   Identifique criativos com CTR < 0.8% e CPC > R$ 2,50.
        *   *Exemplo de Análise*: Campanha "Lançamento Produto X" teve ROAS de 1.5. O conjunto de anúncios "Interesses Moda Feminina" gastou R$ 400,00 com ROAS de 0.9. O anúncio "Vídeo Dicas Estilo" nesse conjunto apresentou CTR de 0.6% e CPC de R$ 3,20.
        *   *Ação Proposta*: Pausar o anúncio "Vídeo Dicas Estilo" no conjunto "Interesses Moda Feminina". Criar e testar um novo anúncio em formato de carrossel com prova social de clientes.
    *   **Google Ads**:
        *   Filtre a aba `Google_Semanal` por ROAS < 2.5 (para busca) ou CPA > R$ 50,00.
        *   Analise os termos de pesquisa (em relatório de termos de pesquisa, se houver) que geraram custo alto e 0 conversões.
        *   *Exemplo de Análise*: Campanha "Busca Termo Principal" teve CPA de R$ 75,00. O grupo de anúncios "Sapatos Femininos" continha o termo de pesquisa "sapato barato" que gerou R$ 100,00 em cliques sem nenhuma conversão.
        *   *Ação Proposta*: Adicionar "barato" como palavra-chave negativa de correspondência exata na campanha "Busca Termo Principal".

### Workflow 2: Criação de Dashboard Mensal Consolidado com Insights Estratégicos (Meta, Google, TikTok)

Este workflow visa fornecer uma visão macro da performance, comparando plataformas e identificando tendências.

*   **Passo 1: Extração de Dados Mensais Agregados**:
    *   Exporte os dados do mês anterior de Meta Ads, Google Ads e TikTok Ads.
    *   Para **TikTok Ads**, use o "Customized Report" incluindo "Campaign", "Ad Group", "Ad", "Spend", "Impressions", "Clicks", "Conversions" (ou "Purchases"), "Conversion Value".
    *   Certifique-se de que as colunas de métricas tenham nomes padronizados (ex: "Gastos", "Impressões", "Cliques", "Conversões", "Valor de Conversão").

*   **Passo 2: Estrutura da Planilha Principal e Consolidação**:
    *   Crie uma nova aba no Google Sheets chamada `Dashboard_Mensal`.
    *   Crie abas auxiliares `Dados_Meta_Mensal`, `Dados_Google_Mensal`, `Dados_TikTok_Mensal` e importe os dados brutos de cada plataforma.
    *   Na aba `Dashboard_Mensal`, crie uma tabela resumo que agregue os totais para cada plataforma. Utilize funções como `SUMIFS` ou `QUERY` para puxar os dados das abas auxiliares.
    *   **Tabela de Exemplo (aba `Dashboard_Mensal`):**
        | Plataforma | Gastos Totais | Impressões | Cliques | Conversões | Valor Conversões | CTR Médio | CPC Médio | CPA Médio | ROAS Médio |
        |------------|---------------|------------|---------|------------|------------------|-----------|-----------|-----------|------------|
        | Meta Ads   | R$ 8.200,00   | 1.8M       | 30.000  | 180        | R$ 27.000,00     | 1,67%     | R$ 0,27   | R$ 45,56  | 3,29       |
        | Google Ads | R$ 5.800,00   | 950K       | 15.000  | 120        | R$ 21.600,00     | 1,58%     | R$ 0,39   | R$ 48,33  | 3,72       |
        | TikTok Ads | R$ 3.500,00   | 1.2M       | 22.000  | 70         | R$ 8.400,00      | 1,83%     | R$ 0,16   | R$ 50,00  | 2,40       |
        | **TOTAL**  | **R$ 17.500,00**| **3.95M**  | **67.000**| **370**    | **R$ 57.000,00** | **1,70%** | **R$ 0,26** | **R$