---
name: seo-reporting
description: "Seo Reporting — Skill especializada para gerar, analisar e apresentar relatórios de desempenho SEO, fornecendo insights acionáveis e estratégias de otimização."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Seo Reporting

Esta skill capacita o Claude a atuar como um analista de SEO avançado, gerando relatórios detalhados com base em dados, identificando tendências, oportunidades e problemas técnicos para otimização contínua.

---

## Keywords

`relatório de desempenho orgânico`, `KPIs SEO`, `análise de tráfego orgânico`, `ranking de palavras-chave`, `auditoria de site`, `visibilidade SERP`, `Google Search Console`, `Google Analytics 4`, `análise de backlinks`, `oportunidades de conteúdo`, `relatório mensal SEO`, `saúde técnica SEO`.

---

## Quick Start

1.  **Conecte-se às Fontes de Dados:** Garanta acesso ao Google Search Console (GSC) e Google Analytics 4 (GA4) para o domínio `exemplo.com.br`.
2.  **Defina o Período de Análise:** Escolha "Últimos 28 dias" no GSC e "Últimos 30 dias" no GA4 para um relatório mensal padrão.
3.  **Extraia Dados Brutos de Desempenho:** Baixe os dados de "Resultados da pesquisa" (Impressões, Cliques, CTR, Posição Média) do GSC e "Aquisição > Tráfego Orgânico" (Sessões, Usuários, Engajamento, Conversões) do GA4.
4.  **Compare as Métricas Chave:** Compare os dados do período atual com o período anterior (Mês vs. Mês) e com o mesmo período do ano anterior (Ano vs. Ano) para identificar tendências e variações significativas.

---

## Core Workflows

### Workflow 1: Geração de Relatório Mensal de Desempenho Orgânico Detalhado

Este workflow orienta a coleta, análise e apresentação de dados de desempenho orgânico, com foco em identificar tendências e oportunidades.

**Passo 1: Coleta e Consolidação de Dados Primários**
Extraia os dados mais relevantes das plataformas primárias de SEO.

*   **Google Search Console (GSC):**
    *   **Ação:** Acesse "Resultados da pesquisa", selecione o período "Últimos 28 dias" e compare com "Período anterior". Filtre por "Tipo de pesquisa: Web".
    *   **Dados a Exportar:** Impressões, Cliques, CTR, Posição Média (geral, por consulta e por página).
    *   **Exemplo:** Para `exemplo.com.br`, exportar a tabela completa de "Consultas" e "Páginas" com as métricas de desempenho para os últimos 28 dias e o período anterior. Observar a consulta `melhores notebooks para programadores` com 15.000 impressões e 1.200 cliques (CTR de 8%), e posição média de 5.3, comparado a 10.000 impressões e 800 cliques (CTR de 8%) e posição média de 6.8 no período anterior.

*   **Google Analytics 4 (GA4):**
    *   **Ação:** Navegue até "Relatórios > Aquisição > Aquisição de tráfego". Ajuste o período para "Últimos 30 dias" e compare com "Período anterior". Adicione "Dimensão secundária: Grupo de canais padrão" e filtre por "Organic Search".
    *   **Dados a Exportar:** Usuários, Sessões, Sessões engajadas, Tempo médio de engajamento, Taxa de engajamento, Eventos de conversão (se configurados), Receita total (se configurado).
    *   **Exemplo:** Para `exemplo.com.br`, exportar dados de tráfego orgânico. O site teve 80.000 usuários orgânicos, 1.500 conversões de "Contato" e um tempo médio de engajamento de 2:15 minutos. No período anterior, foram 70.000 usuários, 1.300 conversões e 2:00 minutos de engajamento.

*   **Ferramentas de Terceiros (Opcional, mas Recomendado):**
    *   **Ação:** Utilize Ahrefs ou SEMrush para dados de ranking de palavras-chave, visibilidade e perfil de backlinks.
    *   **Dados a Exportar:** Posições para as 50 principais palavras-chave, número de domínios de referência, número de backlinks.
    *   **Exemplo:** No Ahrefs, para `exemplo.com.br`, exportar a lista de "Palavras-chave orgânicas" para as top 50 posições. A palavra-chave `curso de python online` está na posição 2, com volume de busca de 5.000, e a URL `exemplo.com.br/curso-python` recebe 30% do tráfego orgânico dessa query.

**Passo 2: Análise de Tendências e Variações de Desempenho**
Compare os dados coletados para identificar crescimentos, quedas e padrões.

*   **Tráfego Orgânico:**
    *   **Ação:** Compare Usuários e Sessões Orgânicas (GA4) Mês vs. Mês (MvM) e Ano vs. Ano (AvA).
    *   **Exemplo:** O tráfego orgânico aumentou 14% MvM (80k vs. 70k usuários) e 22% AvA (80k vs. 65k usuários). Isso indica uma tendência positiva consistente.
*   **Visibilidade e Cliques:**
    *   **Ação:** Analise Impressões, Cliques e CTR (GSC) MvM e AvA.
    *   **Exemplo:** Impressões cresceram 10% MvM (1.2M vs. 1.1M), mas Cliques cresceram 15% MvM (120k vs. 104k), resultando em um aumento da CTR de 0.8% (de 9.4% para 10.2%). Isso sugere que os snippets estão mais atrativos ou as palavras-chave são mais relevantes.
*   **Posição Média:**
    *   **Ação:** Monitore a posição média geral e para um conjunto de 10-15 palavras-chave estratégicas (GSC ou ferramenta de terceiros).
    *   **Exemplo:** A posição média geral melhorou de 8.5 para 7.8. A palavra-chave `consultoria SEO para e-commerce` subiu da posição 12 para 7, gerando um aumento de 30% nos cliques para a página `exemplo.com.br/consultoria-ecommerce`.

**Passo 3: Identificação de Oportunidades e Problemas Acionáveis**
Cruze os dados para transformar observações em recomendações concretas.

*   **Otimização de CTR (GSC):**
    *   **Ação:** Identifique páginas com alta impressão (>10.000) mas baixa CTR (<2.5%).
    *   **Exemplo:** A página `exemplo.com.br/guia-completo-marketing-digital` tem 50.000 impressões mas apenas 800 cliques (CTR de 1.6%). Recomenda-se reescrever o `title tag` e a `meta description` para serem mais convidativos e relevantes, talvez usando CTAs mais fortes ou números/listas.
*   **Melhoria de Conteúdo (GA4 & GSC):**
    *   **Ação:** Localize páginas com alto tráfego orgânico (GA4) mas baixo tempo de engajamento (<1:00 minuto) ou alta taxa de rejeição (>70%) cruzando com consultas relevantes do GSC.
    *   **Exemplo:** A página `exemplo.com.br/ferramentas-seo-gratuitas` atrai 15.000 usuários orgânicos, mas tem um tempo médio de engajamento de 0:45 segundos. Analisando as consultas no GSC, há muitas buscas por `comparativo ferramentas seo`, o que indica que o conteúdo pode ser superficial. Recomenda-se expandir o conteúdo com análises mais aprofundadas e tabelas comparativas.
*   **Identificação de Lacunas de Palavras-chave:**
    *   **Ação:** Utilize dados do GSC (consultas com muitas impressões, mas pouca relevância para conteúdo existente) ou ferramentas de terceiros para encontrar termos que os concorrentes ranqueiam e o site não.
    *   **Exemplo:** O GSC mostra que `exemplo.com.br` recebe 5.000 impressões para `tendências de SEO 2025` mas ranqueia na posição 35. Não há um artigo específico sobre isso. Recomendação: Criar um novo artigo detalhado sobre `Tendências de SEO para 2025` para capturar esse tráfego.

### Workflow 2: Análise de Perfil de Backlinks e Oportunidades de Link Building

Este workflow foca em avaliar o perfil de backlinks do site e de concorrentes para identificar oportunidades estratégicas de construção de links.

**Passo 1: Seleção de Concorrentes e Extração de Dados de Backlinks**
Identifique os principais concorrentes no nicho e extraia seus perfis de backlinks.

*   **Ação:** Selecione 3-5 concorrentes diretos que ranqueiam para suas palavras-chave mais valiosas. Utilize Ahrefs ou SEMrush.
*   **Exemplo:** Concorrentes para `exemplo.com.br` no nicho de marketing digital são `marketingdigitalX.com.br`, `agenciaY.com.br`, `blogZ.com.br`. No Ahrefs, insira cada domínio e exporte os "Referring Domains" e "Backlinks" para cada um, incluindo métricas como DR (Domain Rating) ou DA (Domain Authority) e status do link (dofollow/nofollow).

**Passo 2: Comparação de Métricas de Backlinks e Identificação de Disparidades**
Compare a força e a qualidade do perfil de backlinks do site com os dos concorrentes.

*   **Ação:** Compare o número total de domínios de referência, DR/DA médio, proporção de links dofollow/nofollow e a diversidade de fontes de backlinks.
*   **Exemplo:** `exemplo.com.br` possui 800 domínios de referência e um DR de 55. `marketingdigitalX.com.br` possui 1.500 domínios de referência e um DR de 70, com uma proporção maior de links de alta autoridade (DR > 60). Isso indica que `exemplo.com.br` tem uma lacuna significativa na autoridade de domínio e no número de fontes de links.

**Passo 3: Identificação de Oportunidades de Link Building e Estratégias**
Use os dados comparativos para encontrar sites que linkam para concorrentes, mas não para o seu.

*   **Ação:** Filtre os "Referring Domains" dos concorrentes por alta autoridade (DR > 60) e relevância para o nicho. Cruza essas listas para identificar domínios que linkam para 2 ou mais concorrentes, mas não para o seu site.
*   **Exemplo:** O site `portal-de-noticias-marketing.com.br` (DR 72) linka para `marketingdigitalX.com.br` e `agenciaY.com.br` em artigos sobre "estratégias de SEO avançadas". `exemplo.com.br` possui um artigo abrangente sobre o mesmo tema: `exemplo.com.br/estrategias-seo-avancadas`. Esta é uma oportunidade clara para um outreach de link building, apresentando o conteúdo de `exemplo.com.br` como um recurso valioso.
*   **Identificação de Links Quebrados dos Concorrentes:**
    *   **Ação:** Utilize a ferramenta de "Broken Backlinks" do Ahrefs para os concorrentes.
    *   **Exemplo:** `agenciaY.com.br` tem um link quebrado de `universidade-negocios.edu.br` para um artigo sobre "planejamento de marketing". Se `exemplo.com.br` tem um artigo equivalente (`exemplo.com.br/planejamento-marketing-digital`), pode-se contatar `universidade-negocios.edu.br` oferecendo o link substituto.

---

## Templates

### Resumo Executivo de Relatório SEO Mensal

```
## Relatório de Desempenho SEO - Mês: Maio/2024

**Período Analisado:** 01/05/2024 - 31/05/2024
**Comparativo:** Abril/2024 e Maio/2023
**Domínio:** exemplo.com.br

---

### 1. Resumo Executivo

O mês de Maio/2024 demonstrou um crescimento robusto no desempenho orgânico de `exemplo.com.br`. Registramos um aumento de **+14%** em Usuários Orgânicos Mês vs. Mês (MvM) e **+22%** Ano vs. Ano (AvA). Os Cliques do Google Search Console subiram **+15%** MvM, com a CTR geral melhorando de 9.4% para 10.2%. A posição média geral também apresentou melhora, passando de 8.5 para 7.8.

As conversões orgânicas (formulário de contato) aumentaram **+15.4%** MvM, totalizando 1.500 leads, impulsionadas principalmente pela performance de páginas de serviço.

---

### 2. Destaques Positivos

*   **Crescimento Sustentado:** Tráfego orgânico manteve a trajetória de crescimento, superando tanto o mês anterior quanto o ano anterior.
*   **Melhora da CTR:** Títulos e meta descrições otimizados resultaram em uma maior taxa de cliques, indicando melhor relevância nos resultados de busca.
*   **Palavra-chave Estratégica:** A palavra-chave `consultoria SEO para e-commerce` subiu 5 posições (de 12ª para 7ª), gerando um aumento de 30% nos cliques para a página de serviço correspondente.
*   **Engajamento Aumentado:** O tempo médio de engajamento do tráfego orgânico aumentou para 2:15 minutos, indicando maior qualidade do conteúdo.

---

### 3. Áreas de Oportunidade e Recomendações

*   **Otimização de CTR para Conteúdo:** A página `exemplo.com.br/guia-completo-marketing-digital` tem 50.000 impressões mas apenas 1.6% de CTR.
    *   **Recomendação:** Reescrever o `title tag` e `meta description` com foco em um benefício claro e um CTA forte (ex: "Guia Completo de Marketing Digital: De 0 a Expert em 2024").
*   **Melhoria de Conteúdo e Engajamento:** A página `exemplo.com.br/ferramentas-seo-gratuitas` atrai 15.000 usuários, mas o tempo de engajamento é de 0:45 segundos.
    *   **Recomendação:** Expandir o conteúdo com seções de "comparativo de funcionalidades" e "casos de uso práticos" para aumentar a profundidade e o tempo de permanência.
*   **Oportunidade de Link Building:** Identificamos que `portal-de-noticias-marketing.com.br` (DR 72) linka para nossos concorrentes em artigos de "estratégias de SEO avançadas", mas não para `exemplo.com.br`.
    *   **Recomendação:** Iniciar um outreach para `portal-de-noticias-marketing.com.br`, apresentando nosso artigo `exemplo.com.br/estrategias-seo-avancadas` como um recurso complementar.

---

### 4. Próximos Passos

1.  Implementar as otimizações de `title tag` e `meta description` para `exemplo.com.br/guia-completo-marketing-digital` até 10/06.
2.  Desenvolver plano de expansão de conteúdo para `exemplo.com.br/ferramentas-seo-gratuitas` até 15/06.
3.  Executar a campanha de outreach para `portal-de-noticias-marketing.com.br` na semana de 03/06.
4.  Monitorar o impacto das mudanças no relatório de Junho/2024.
```

### Tabela de Desempenho de Palavras-chave Estratégicas

```
## Desempenho das 10 Palavras-chave Mais Estratégicas - Maio/2024

**Período Analisado:** 01/05/2024 - 31/05/2024
**Comparativo:** Mês Anterior (Abril/2024)
**Fonte:** Google Search Console

| Palavra-chave                 | URL de Destino                                  | Posição Atual | Posição Anterior | Variação | Impressões | Cliques | CTR     |
|-------------------------------|-------------------------------------------------|---------------|------------------|----------|------------|---------|---------|
| consultoria SEO para e-commerce | exemplo.com.br/consultoria-ecommerce          | 7             | 12               | +5       | 25.000     | 1.800   | 7.2%    |
| melhores notebooks para programadores | exemplo.com.br/melhores-notebooks           | 5             | 7                | +2       | 15.000     | 1.200   | 8.0%    |
| curso de python online        | exemplo.com.br/curso-python                     | 2             | 2                | 0        | 10.000     | 3.500   | 35.0%   |
| ferramentas seo gratuitas     | exemplo.com.br/ferramentas-seo-gratuitas        | 9             | 8                | -1       | 50.000     | 1.600   | 3.2%    |
| marketing digital para iniciantes | exemplo.com.br/guia-marketing-digital       | 4             | 4                | 0        | 30.000     | 2.500   | 8.3%    |
| como fazer link building      | exemplo.com.br/o-que-e-link-building            | 11            | 15               | +4       | 8.000      | 320     | 4.0%    |
| auditoria seo completa        | exemplo.com.br/auditoria-seo                    | 6             | 6                | 0        | 12.000     | 720     | 6.0%    |
| seo local para pequenas empresas | exemplo.com.br/seo-local-negocios           | 8             | 10               | +2       | 7.000      | 280     | 4.0%    |
| tendencias de seo 2025        | exemplo.com.br/blog/tendencias-seo-2025         | 35            | 38               | +3       | 5.000      | 50      | 1.0%    |
| conteudo para blog seo        | exemplo.com.br/como-criar-conteudo-seo          | 10            | 9                | -1       | 9.000      | 450     | 5.0%    |
```

---

## Checklist

- [x] Confirmação da coleta de dados de GA4 para o período completo (01/05 - 31/05) e comparativo (Abril/2024 e Maio/2023).
- [x] Verificação de anomalias nos dados de GSC (quedas súbitas de impressões/cliques não explicadas por sazonalidade ou algoritmo).
- [x] Análise da evolução da posição média para as 10 palavras-chave prioritárias, identificando ganhos e perdas.
- [x] Comparativo de tráfego orgânico (usuários e sessões) com o mês anterior e ano anterior, com % de variação.
- [x] Identificação de 3-5 páginas com maior potencial de otimização de CTR no GSC (impressões altas, CTR baixa).
- [x] Avaliação de conversões orgânicas (ex: formulários, vendas) e seu custo por aquisição (se houver dados de investimento).
- [x] Revisão de oportunidades de link building (mínimo 3) baseadas em análise competitiva de backlinks.
- [x] Verificação de novos erros críticos de rastreamento ou indexação no GSC (páginas com erro 404, bloqueadas pelo robots.txt).
- [x] Geração de lista de 3-5 tópicos para criação de conteúdo com base em lacunas de palavras-chave ou baixa performance de engajamento.
- [x] Confirmação de que todas as recomendações são acionáveis e possuem prazos definidos.

---

## Métricas de Referência

| Métrica                         | Benchmark (Nicho Geral) | Meta (exemplo.com.br) |
|---------------------------------|-------------------------|-----------------------|
| Crescimento de Tráfego Orgânico (YoY) | > 15-20%                | > 25%                 |
| Posição Média (Top 10 Keywords) | < 5.0                   | < 4.0                 |
| CTR Média (GSC)                 | 3-5% (Web)              | > 6%                  |
| Tempo Médio de Engajamento (GA4) | > 1:30 minutos          | > 2:30 minutos        |
| Taxa de Conversão Orgânica      | 1-3%                    | > 2.5%                |
| Aumento de Domínios de Referência (YoY) | > 5-10%                 | > 15%                 |

---

## Erros Comuns

1.  **Foco Exclusivo em Rankings e Tráfego Bruto**: Muitos relatórios apenas mostram o número de visitantes e a posição das palavras-chave, sem conectar com o impacto real no negócio.
    *   **Como evitar**: Sempre inclua métricas de engajamento (tempo na página, taxa de engajamento GA4), conversões (leads, vendas orgânicas) e, se possível, o valor financeiro gerado pelo tráfego orgânico. Por exemplo, ao invés de apenas "1.800 cliques para 'consultoria SEO'", mostre "1.800 cliques resultaram em 35 leads qualificados para consultoria, com valor estimado de R$ 7.000".
2.  **Dados Descontextualizados sem Comparativos**: Apresentar números absolutos sem comparação com períodos anteriores ou benchmarks do setor torna difícil entender o real desempenho.
    *   **Como evitar**: Em cada métrica, apresente a variação percentual Mês vs. Mês e Ano vs. Ano. Use tabelas ou gráficos que visualizem claramente essas comparações. Por exemplo, "Tráfego Orgânico: 80.000 usuários (+14% MvM, +22% AvA)".
3.  **Relatórios Descritivos sem Recomendações Acionáveis**: Um relatório que apenas descreve o que aconteceu, sem sugerir próximos passos concretos, tem pouco valor estratégico.
    *   **Como evitar**: Cada insight ou problema identificado deve ser acompanhado por uma ou mais recomendações claras, específicas e com prazos definidos. Transforme "A página X tem baixa CTR" em "Reescrever o título e meta descrição da página X com CTA 'Descubra como [benefício]' até 15/06 para aumentar a CTR".

---

## Dicas Avançadas

1.  **Segmentação de Desempenho por Intenção de Busca**: Em vez de analisar todas as palavras-chave juntas, categorize-as por intenção (informacional, navegacional, transacional, comercial) e analise o desempenho de cada grupo. Isso permite otimizar conteúdo e KPIs de forma mais direcionada. Exemplo: Comparar CTR de palavras-chave informacionais (média 2-4%) versus transacionais (média 8-15%).
2.  **Análise de Cluster de Tópicos e Conteúdo Pilar**: Avalie o desempenho não apenas de páginas individuais, mas de grupos de páginas interligadas por um tópico central (cluster de conteúdo). Isso ajuda a entender a autoridade temática e a performance de estratégias de conteúdo abrangentes. Exemplo: Medir o crescimento de tráfego e conversões para todo o cluster "Marketing Digital para Iniciantes" em vez de apenas um artigo.
3.  **Relatórios de Atribuição de Conversão Orgânica (GA4)**: Utilize os modelos de atribuição do GA4 (linear, baseado em posição, primeiro clique, último clique) para entender o papel do tráfego orgânico em diferentes pontos da jornada do cliente, não apenas como o último ponto de contato. Isso revela o valor estratégico do SEO em estágios iniciais de descoberta.
4.  **Integração de Dados de Negócio e ROI**: Conecte os dados de SEO com dados de vendas, CRM ou valor de vida útil do cliente (LTV). Calcule o Retorno sobre o Investimento (ROI) do SEO, mostrando o valor financeiro direto das otimizações. Exemplo: "O tráfego orgânico gerou R$ 150.000 em vendas diretas, com um ROI de 500% sobre o investimento em SEO".
5.  **Análise de SERP Features e Visibilidade (Rank Tracking Avançado)**: Monitore e reporte a performance em SERP Features como Featured Snippets, People Also Ask, Pacotes Locais, Avaliações. Ferramentas como SEMrush ou Ahrefs permitem rastrear a visibilidade nessas features. Isso vai além da posição média, mostrando a dominância visual e informativa na SERP. Exemplo: "A página `exemplo.com.br/guia-seo-local` conquistou um Featured Snippet para `melhorar ranqueamento local`, gerando um aumento de 25% na visibilidade orgânica total."