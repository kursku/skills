---
name: google-search-console
description: "Google Search Console — Skill especializada para otimização e monitoramento de performance em busca orgânica do Google."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Google Search Console

Esta skill capacita o Claude a operar como um especialista em Google Search Console, realizando análises, identificando problemas técnicos de SEO e otimizando a presença de sites na busca orgânica do Google.

---

## Keywords

`GSC`
`Search Console`
`indexação`
`rastreamento`
`sitemap`
`Core Web Vitals`
`HTTPS`
`erros 404`
`rich snippets`
`dados estruturados`
`desempenho de busca`
`cobertura de indexação`
`usabilidade mobile`
`remoção de URLs`
`parâmetros de URL`

---

## Quick Start

1.  **Verificar Propriedade**: Acesse `search.google.com/search-console` e adicione/verifique uma propriedade usando o método "Prefixo do URL" ou "Domínio" (DNS).
2.  **Enviar Sitemap**: No menu lateral, navegue até `Sitemaps`, insira a URL do seu sitemap XML (ex: `https://www.seusite.com.br/sitemap.xml`) e clique em `Enviar`.
3.  **Inspecionar URL**: Cole uma URL específica do seu site na barra de pesquisa superior para verificar seu status de indexação e rastreamento.
4.  **Analisar Desempenho**: Acesse o relatório `Desempenho` para monitorar cliques, impressões, CTR e posição média de suas páginas e consultas.
5.  **Checar Cobertura**: Verifique o relatório `Páginas` para identificar URLs com erros de indexação, excluídas ou indexadas com avisos.

---

## Core Workflows

### Workflow 1: Diagnóstico e Correção de Problemas de Indexação

Este workflow detalha o processo para identificar e resolver problemas que impedem suas páginas de serem indexadas ou aparecerem corretamente nos resultados de pesquisa.

**Passos Detalhados:**

1.  **Acessar Relatório de Cobertura (Páginas)**: No menu lateral do GSC, clique em `Páginas`.
2.  **Identificar Padrões de Erros**: Observe o gráfico e a tabela "Por que as páginas não estão indexadas?". Filtre por categorias como "Erro", "Válida com avisos" ou "Excluída".
    *   **Exemplo**: O relatório mostra 50 URLs como "Bloqueada pelo robots.txt".
3.  **Detalhar URLs Afetadas**: Clique na categoria de erro (ex: "Bloqueada pelo robots.txt") para ver a lista de URLs impactadas.
    *   **Exemplo**: URLs como `https://www.seusite.com.br/area-restrita/`, `https://www.seusite.com.br/carrinho-de-compras/` e `https://www.seusite.com.br/tags/internas/` aparecem na lista.
4.  **Inspecionar URL Individualmente**: Copie uma das URLs problemáticas e cole-a na barra de pesquisa superior do GSC (Ferramenta de Inspeção de URL).
    *   **Exemplo**: Inspecionar `https://www.seusite.com.br/area-restrita/`.
5.  **Analisar o Motivo da Não Indexação**: A ferramenta de inspeção mostrará detalhes como "Rastreamento permitido? Não", "Indexação permitida? Não" e o motivo específico (ex: "Bloqueada por robots.txt"). Ela também pode indicar a linha exata no seu arquivo `robots.txt` que está causando o bloqueio.
    *   **Exemplo**: A inspeção de `https://www.seusite.com.br/area-restrita/` confirma "Indexação não permitida: Bloqueada por robots.txt" e indica que a regra `Disallow: /area-restrita/` no `robots.txt` é a causa.
6.  **Implementar Correção**: Com base na análise, aplique a correção necessária no seu site.
    *   **Exemplo**: Se a intenção é que `/area-restrita/` não seja indexada, a regra no `robots.txt` está correta. Se, por engano, uma página importante (ex: `https://www.seusite.com.br/blog/novo-post/`) foi bloqueada, remova ou ajuste a regra `Disallow` no `robots.txt`. Para um erro 404, verifique se a URL existe ou se houve um redirecionamento. Para `noindex`, remova a meta tag `noindex` do HTML da página.
7.  **Validar Correção no GSC**: Após a implementação da correção, retorne ao relatório `Páginas`, clique na categoria de erro corrigida (ex: "Bloqueada pelo robots.txt") e clique em `Validar correção`. O Google re-rastreará e reavaliará as URLs afetadas.
    *   **Exemplo**: Após corrigir o `robots.txt` para `https://www.seusite.com.br/blog/novo-post/`, clique em `Validar correção` para que o Google tente rastrear e indexar a página novamente.

### Workflow 2: Otimização de Desempenho de Busca para Conteúdo Existente

Este workflow foca em como usar os dados de desempenho do GSC para melhorar a visibilidade e o CTR de páginas já existentes.

**Passos Detalhados:**

1.  **Acessar Relatório de Desempenho**: No menu lateral do GSC, clique em `Desempenho` > `Resultados da pesquisa`.
2.  **Configurar Período e Métricas**: Selecione um período de tempo relevante, como "Últimos 12 meses". Certifique-se de que "Cliques totais", "Impressões totais", "CTR médio" e "Posição média" estejam marcados.
3.  **Identificar Oportunidades por Página**: Na aba `Páginas`, ordene por `Impressões` (decrescente) e procure páginas com muitas impressões, mas baixo CTR (ex: < 2%) e/ou posição média entre 8 e 20. Estas são páginas com potencial para subir no ranking e gerar mais cliques.
    *   **Exemplo**: A página `https://www.seusite.com.br/blog/guia-completo-de-marketing-digital/` tem 250.000 impressões, 1.8% de CTR e posição média 12.
4.  **Analisar Queries Associadas**: Clique na página identificada. Em seguida, clique na aba `Consultas` para ver as palavras-chave que estão acionando essa página nos resultados de pesquisa.
    *   **Exemplo**: Para a página "Guia Completo de Marketing Digital", as queries incluem: "marketing digital para iniciantes" (posição 8, CTR 3%), "estratégias de marketing digital" (posição 15, CTR 1%), "o que é marketing digital" (posição 5, CTR 4%), "curso marketing digital online" (posição 22, CTR 0.5%).
5.  **Analisar Intenção de Busca e Otimizar**:
    *   Para queries com boa posição (ex: "o que é marketing digital"), mas que podem ter um CTR melhor, revise o título e a meta descrição da página para torná-los mais atraentes e relevantes.
    *   Para queries com alta impressão, baixo CTR e posição média (ex: "estratégias de marketing digital"), revise o conteúdo da página para incorporar mais profundamente essas palavras-chave, expandir a seção relevante ou adicionar um subtítulo específico.
    *   Para queries de cauda longa com poucas impressões e baixa posição (ex: "curso marketing digital online"), avalie se vale a pena criar um novo conteúdo específico ou se a página atual pode ser otimizada para capturar essa intenção.
    *   **Exemplo de Ação**: Para "estratégias de marketing digital", adicione uma seção no guia detalhando 5 estratégias essenciais, com exemplos práticos. Para "curso marketing digital online", considere adicionar uma seção de "Recursos Adicionais" com recomendações de cursos.
6.  **Monitorar Impacto**: Após implementar as otimizações, use o recurso de comparação de datas no relatório de Desempenho (ex: comparar o mês anterior à mudança com o mês posterior) para avaliar o impacto nas impressões, cliques, CTR e posição média das queries e da página.

---

## Templates

### Solicitação de Reindexação de URL Corrigida

```
Assunto: Solicitação de Reindexação de URL Corrigida - [Nome do Site]

Prezada Equipe / Para Mim Mesmo,

Por favor, agende a reindexação da seguinte URL no Google Search Console após a correção de um problema de indexação:

URL Corrigida: https://www.seusite.com.br/blog/artigo-de-exemplo-corrigido/
Problema Original: Página bloqueada por robots.txt (regra "Disallow: /blog/artigo-de-exemplo-corrigido/" removida).
Data da Correção no Site: 2024-10-26

A correção foi implementada e a página agora está acessível para rastreamento. Aguardo a validação da correção via GSC.

Atenciosamente,
[Seu Nome/Nome da Equipe SEO]
```

### Análise Rápida de Desempenho de Query

```
Análise de Desempenho - Query Específica

Data da Análise: 2024-10-26
Analista: [Seu Nome]

Query Analisada: "melhores fones de ouvido sem fio custo benefício"

Dados do GSC (Últimos 90 dias):
- Cliques: 1.250
- Impressões: 85.000
- CTR Médio: 1.47%
- Posição Média: 18.2

Página Associada: https://www.seusite.com.br/review/fones-bluetooth-baratos/

Observações:
A query tem um volume de impressão significativo, indicando interesse do público. No entanto, o CTR e a posição média são baixos para uma query de fundo de funil com alta intenção de compra. A página atual aborda o tema, mas pode não estar otimizada para a especificidade "custo benefício" ou para atrair cliques na SERP.

Recomendações de Otimização:
1.  **Título e Meta Descrição**: Revisar o `title` e a `meta description` da página para incluir a frase exata "custo benefício" e elementos que incentivem o clique (ex: "Descubra os Melhores Fones de Ouvido Sem Fio Custo-Benefício de 2024!").
2.  **Conteúdo**: Adicionar uma seção específica ou um parágrafo introdutório que aborde diretamente a questão do "custo benefício" de forma explícita, talvez com uma tabela comparativa rápida.
3.  **Rich Snippets**: Verificar se a página pode se beneficiar de schema markup de `Product` ou `Review` para destacar preços, avaliações, etc., o que pode aumentar o CTR.

Prazo para Implementação: 2024-11-05
Monitoramento Pós-Otimização: Acompanhar o CTR e a posição média para esta query nas próximas 4-8 semanas no GSC.
```

---

## Checklist

- [x] Propriedade do site verificada em todas as suas variações (com/sem www, HTTP/HTTPS) no GSC.
- [x] Sitemap XML principal enviado e status "Sucesso" no relatório de Sitemaps.
- [x] Relatório de Páginas (Cobertura) verificado semanalmente para novos erros ou quedas de indexação.
- [x] Relatório de Core Web Vitals (Experiência na página) avaliado para URLs "Boas" (>75% é ideal) tanto para desktop quanto para mobile.
- [x] Status HTTPS verificado no relatório `Experiência na página` e `HTTPS` (se disponível) para garantir que todas as URLs canônicas são HTTPS.
- [x] Relatório de Usabilidade Mobile sem erros para todas as páginas.
- [x] Relatório de Resultados Otimizados (Dados Estruturados) checado regularmente para warnings ou erros em rich snippets implementados.
- [x] Relatório de Desempenho (Resultados da pesquisa) analisado mensalmente para identificar oportunidades de otimização de cliques e posição.
- [x] Mensagens do GSC (Ações Manuais, Problemas de Segurança, Avisos Gerais) revisadas e tratadas imediatamente.
- [x] URLs desatualizadas ou de baixo valor removidas do índice via ferramenta de Remoções, se necessário.

---

## Métricas de Referência

| Métrica                         | Benchmark (Varia) | Meta (Exemplo) |
|---------------------------------|-------------------|----------------|
| Taxa de Cliques (CTR) Média     | 2% - 5% (Geral)   | > 3.5%         |
| Páginas Indexadas / Sitemapped  | > 90%             | > 95%          |
| Core Web Vitals (URLs "Boas")   | > 75%             | > 85%          |
| Erros de Cobertura (Excluídas)  | < 1%              | < 0.5%         |
| Usabilidade Mobile (URLs "Boas")| 100%              | 100%           |
| Posição Média de Queries Chave  | Varia             | Melhorar em 3 posições |

---

## Erros Comuns

1.  **Não verificar todas as variações do domínio**: É comum registrar apenas `https://www.meusite.com.br` e esquecer `https://meusite.com.br` (sem www) ou as versões HTTP. Isso leva à perda de dados valiosos e à impossibilidade de diagnosticar problemas que afetam outras variações. **Como evitar**: Sempre adicione a propriedade do domínio completo (via DNS) ou todas as variações de prefixo de URL para garantir uma visão holística.
2.  **Ignorar avisos de "Páginas com redirecionamento" ou "Páginas com erro 404" no relatório de Cobertura**: Muitos veem essas categorias como "normais" e não as investigam. Picos nessas métricas indicam links quebrados internos ou externos, redirecionamentos em loop ou cadeias, que desperdiçam orçamento de rastreamento e prejudicam a experiência do usuário. **Como evitar**: Monitore essas categorias. Um aumento súbito de 404s pode indicar um erro no servidor ou na estrutura de links. Um grande número de redirecionamentos pode apontar para uma otimização necessária na arquitetura do site.
3.  **Não submeter o sitemap XML ou submeter um sitemap desatualizado**: Um sitemap é crucial para que o Google descubra novas páginas e entenda a estrutura do seu site. Um sitemap desatualizado omite URLs importantes ou inclui URLs que não existem mais. **Como evitar**: Certifique-se de que seu CMS ou ferramenta de sitemap gere automaticamente e atualize o sitemap. Submeta-o no GSC e verifique regularmente a data da última leitura e a contagem de URLs descobertas.

---

## Dicas Avançadas

1.  **Análise de "Discovered - currently not indexed"**: Este status no relatório de Cobertura indica que o Googlebot encontrou a página, mas decidiu não indexá-la ainda. Em vez de ignorar, analise essas URLs. Elas podem ser páginas de baixo valor (ex: tags com pouco conteúdo) ou páginas importantes que precisam de mais links internos, conteúdo de maior qualidade ou correção de problemas técnicos menores. Focar nelas pode revelar oportunidades de indexação para conteúdo relevante.
2.  **Uso da ferramenta de Remoções para conteúdo sensível ou desatualizado**: Além de simplesmente desindexar com `noindex`, a ferramenta de remoções do GSC é útil para remover temporariamente URLs que contêm informações sensíveis ou para acelerar a desindexação de conteúdo obsoleto que não deve aparecer na busca, mesmo que por um curto período. É uma medida de emergência, não uma solução de longo prazo para desindexação.
3.  **Comparação de desempenho pré e pós-implementação**: Utilize o recurso de comparação de datas no relatório de Desempenho para isolar o impacto de otimizações de conteúdo, mudanças técnicas ou campanhas específicas. Por exemplo, compare o CTR de uma página nos 30 dias antes e 30 dias depois de otimizar seu título e meta descrição. Isso fornece dados concretos sobre o sucesso das suas ações de SEO.
4.  **Integração de dados do GSC via API**: Para análises mais complexas e automatizadas, explore a API do Google Search Console. Ela permite extrair grandes volumes de dados de desempenho (queries, páginas, países, dispositivos) programaticamente e integrar com ferramentas de Business Intelligence (BI) como Google Data Studio (Looker Studio), Power BI ou planilhas para criar dashboards personalizados e relatórios automatizados, economizando tempo e fornecendo insights mais profundos.
5.  **Segmentação de dados por tipo de pesquisa e dispositivo**: No relatório de Desempenho, filtre por `Tipo de pesquisa` (Imagens, Vídeo, Notícias) e `Dispositivo` (Desktop, Mobile, Tablet). Isso pode revelar oportunidades nicho. Por exemplo, se seu site tem muitas impressões em "Imagens" mas baixo CTR, você pode otimizar os `alt tags` e legendas das imagens. Se o desempenho mobile é inferior ao desktop, as Core Web Vitals mobile ou a usabilidade podem precisar de atenção prioritária.