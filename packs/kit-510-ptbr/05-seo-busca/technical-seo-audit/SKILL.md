---
name: technical-seo-audit
description: "Technical Seo Audit — Skill especializada para technical seo audit"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Technical Seo Audit

Esta skill capacita o Claude a executar auditorias técnicas de SEO, identificando e propondo soluções para problemas de rastreamento, indexação, performance e estruturação de dados.

---

## Keywords

rastreamento, indexação, Core Web Vitals, schema markup, hreflang, canonicalização, robots.txt, sitemap.xml, log analysis, renderização, servidor, HTTPS, status HTTP, mobile-first, JavaScript SEO, auditoria técnica SEO, otimização de orçamento de rastreamento.

---

## Quick Start

1.  **Configurar ferramenta de rastreamento**: Iniciar um rastreamento completo do site com Screaming Frog SEO Spider (modo 'Spider' ou 'List' para URLs específicas) ou Sitebulb para identificar URLs e seus status HTTP, títulos, meta descrições, cadeias de redirecionamento e links internos.
2.  **Verificar Google Search Console (GSC)**: Acessar a seção "Indexação > Páginas" para identificar erros de indexação (Ex: 'Página rastreada – atualmente não indexada', 'Página com redirecionamento', 'Erro do servidor (5xx)'), e "Experiência > Core Web Vitals" para métricas de performance.
3.  **Analisar arquivo robots.txt**: Acessar `seudominio.com.br/robots.txt` para verificar diretivas `Disallow` que possam estar bloqueando rastreamento de seções importantes do site e a declaração do Sitemap.
4.  **Inspecionar sitemaps XML**: Abrir os sitemaps listados no robots.txt ou no GSC para garantir que todas as URLs canônicas importantes estejam incluídas e que não haja URLs 4xx ou 5xx.
5.  **Executar teste de performance**: Utilizar Google PageSpeed Insights para a homepage e algumas páginas de modelo (categoria, produto, artigo) para identificar problemas de Core Web Vitals e oportunidades de otimização.

---

## Core Workflows

### Workflow 1: Auditoria de Rastreamento e Indexação

Este workflow foca em identificar e resolver problemas que impedem o Googlebot de acessar e indexar o conteúdo de um site.

**Passos:**

1.  **Configuração de Rastreamento Abrangente**:
    *   **Ferramenta**: Screaming Frog SEO Spider.
    *   **Ação**: Configure o Screaming Frog para rastrear o site com as seguintes opções:
        *   `Configuration > Spider > Basic`: Habilitar 'Crawl all subdomains', 'Check external links'.
        *   `Configuration > Spider > Advanced`: Aumentar o limite de rastreamento (Ex: 10 milhões de URLs para sites grandes), 'Extract hreflang', 'Extract structured data'.
        *   `Configuration > API Access > Google Search Console`: Conectar para importar dados de indexação e performance.
    *   **Exemplo**: Para um e-commerce com 50.000 produtos, inicie o rastreamento em `https://www.lojaexemplo.com.br`. O tempo estimado é de 4-6 horas.
2.  **Análise de Status HTTP e Redirecionamentos**:
    *   **Ferramenta**: Relatórios do Screaming Frog ('Response Codes', 'Redirects').
    *   **Ação**:
        *   Filtre por 'Client Error (4xx)' e 'Server Error (5xx)'. Priorize a correção de URLs 404/410 internas, garantindo que links para elas sejam atualizados ou redirecionados para páginas relevantes (301). Ex: `https://www.lojaexemplo.com.br/produto-antigo` (404) deve ser redirecionado para `https://www.lojaexemplo.com.br/categoria-relacionada`.
        *   Analise cadeias de redirecionamento (Ex: A > B > C). O ideal é ter no máximo um redirecionamento (A > C). Ex: `https://www.lojaexemplo.com.br/antigo` (301) para `https://www.lojaexemplo.com.br/novo` (301) para `https://www.lojaexemplo.com.br/pagina-final`. Corrija para `https://www.lojaexemplo.com.br/antigo` (301) para `https://www.lojaexemplo.com.br/pagina-final`.
3.  **Verificação de Diretivas de Indexação**:
    *   **Ferramenta**: Screaming Frog ('Indexability', 'Directives'), Google Search Console ('Indexação > Páginas').
    *   **Ação**:
        *   No Screaming Frog, filtre por 'Non-Indexable' e examine as razões (Ex: 'Noindex', 'Canonicalized', 'Blocked by robots.txt'). Verifique se as páginas importantes estão inadvertidamente marcadas como 'noindex'.
        *   No GSC, filtre por 'Páginas excluídas' e 'Páginas não indexadas'. Investigue a causa de cada status para as URLs críticas. Ex: 'Página rastreada – atualmente não indexada' pode indicar conteúdo de baixa qualidade ou intenção de busca não atendida.
4.  **Análise de Arquivos robots.txt e Sitemaps XML**:
    *   **Ferramenta**: Google Search Console ('Configurações > Rastreamento > robots.txt tester', 'Sitemaps'), Screaming Frog ('Sitemaps').
    *   **Ação**:
        *   Utilize o `robots.txt tester` do GSC para simular o Googlebot e garantir que nenhuma URL importante esteja bloqueada. Ex: `User-agent: * Disallow: /admin/`.
        *   Verifique se os sitemaps XML submetidos no GSC estão atualizados, incluem apenas URLs canônicas e relevantes, e não contêm erros (URLs 4xx/5xx). Exclua URLs com `noindex` ou `canonical` para outras páginas do sitemap.
5.  **Análise de Logs de Servidor (Opcional, mas Recomendado para Sites Grandes)**:
    *   **Ferramenta**: Logfile Analyzer (Ex: Screaming Frog Log File Analyser, GoAccess).
    *   **Ação**: Importe os logs de acesso do servidor para identificar padrões de rastreamento do Googlebot.
        *   Verifique se o Googlebot está rastreando as páginas mais importantes com frequência adequada.
        *   Identifique se o Googlebot está gastando muito orçamento de rastreamento em URLs de baixo valor (parâmetros, páginas não indexáveis). Ex: O Googlebot rastreando 10.000 URLs de paginação como `/categoria?page=1`, `/categoria?page=2`, etc., quando apenas a primeira página é indexável.

### Workflow 2: Otimização de Core Web Vitals e Experiência do Usuário

Este workflow visa melhorar as métricas de performance e usabilidade, cruciais para a experiência do usuário e ranking.

**Passos:**

1.  **Identificação de Páginas Críticas para Análise**:
    *   **Ferramenta**: Google Search Console ('Experiência > Core Web Vitals'), Google Analytics (páginas com alto tráfego e alta taxa de rejeição).
    *   **Ação**: Priorize páginas com status 'URL ruim' no GSC e páginas com alto tráfego orgânico ou conversão, mas com métricas CWV baixas. Ex: A página de produto mais vendida (`/produto/sku123`) e a página de categoria principal (`/categoria/eletronicos`) apresentando LCP acima de 4s.
2.  **Análise Detalhada de Performance com Ferramentas**:
    *   **Ferramenta**: Google PageSpeed Insights, Lighthouse (via Chrome DevTools).
    *   **Ação**: Execute testes para as URLs identificadas.
        *   **LCP (Largest Contentful Paint)**: Identifique o elemento LCP (geralmente uma imagem grande, vídeo ou bloco de texto). Ex: Uma imagem de banner de 2MB em `https://www.lojaexemplo.com.br` pode causar um LCP de 5.2s.
        *   **CLS (Cumulative Layout Shift)**: Observe elementos que causam instabilidade visual. Ex: Banners de anúncios que carregam tardiamente, fontes que mudam de tamanho após carregamento.
        *   **INP (Interaction to Next Paint) / FID (First Input Delay)**: Analise o tempo de bloqueio do thread principal e o tempo de execução de JavaScript. Ex: Um script de chat ao vivo de terceiros bloqueando o thread principal por 800ms.
3.  **Implementação de Otimizações Específicas**:
    *   **Imagens**:
        *   Otimização: Comprimir imagens (Ex: TinyPNG), usar formatos modernos (WebP, AVIF).
        *   Carregamento: Implementar `loading="lazy"` para imagens abaixo da dobra.
        *   Dimensionamento: Definir `width` e `height` explícitos nas tags `<img>` para evitar CLS.
    *   **CSS e JavaScript**:
        *   Minificação: Reduzir tamanho de arquivos CSS/JS.
        *   Concatenação: Combinar arquivos para reduzir requisições (se não houver HTTP/2).
        *   Remoção de CSS/JS não utilizado: Ferramentas como PurgeCSS ou Coverage no DevTools.
        *   Carregamento assíncrono/defer: Para scripts não críticos (Ex: `<script src="analytics.js" defer></script>`).
    *   **Fontes**: Pré-carregar fontes críticas (`<link rel="preload" href="font.woff2" as="font" crossorigin>`). Usar `font-display: swap` para evitar flash de texto invisível (FOIT).
    *   **Servidor e Cache**: Otimizar TTFB (Time To First Byte) com melhorias no servidor (hardware, CDN, cache de servidor).
    *   **Pré-conexão e Pré-busca**: Usar `<link rel="preconnect">` e `<link rel="dns-prefetch">` para recursos de terceiros críticos.
4.  **Validação e Monitoramento**:
    *   **Ferramenta**: Google PageSpeed Insights, Lighthouse, GSC.
    *   **Ação**: Após as implementações, re-execute os testes para verificar melhorias. Monitore o GSC para ver a evolução das métricas de Core Web Vitals ao longo do tempo. Ex: Após otimizar imagens e JS, o LCP da homepage caiu de 5.2s para 2.1s, e o CLS de 0.25 para 0.03.

---

## Templates

### Relatório de Erros de Rastreamento e Indexação

```
# Relatório de Auditoria Técnica SEO: Rastreamento e Indexação

**Data da Auditoria:** 2024-10-27
**Site Auditado:** www.exemplo-ecommerce.com.br
**Ferramentas Utilizadas:** Screaming Frog SEO Spider (v18.0), Google Search Console

## Resumo Executivo

Foram identificados 287 erros críticos de rastreamento e indexação que impactam a visibilidade do site no Google. Os principais problemas incluem 120 URLs 404 quebradas, 55 cadeias de redirecionamento com mais de 2 saltos e 32 páginas importantes com tag `noindex` acidental.

## Detalhes dos Problemas

### 1. Erros de Cliente (4xx) - URLs Quebradas

*   **Identificação:** Screaming Frog - Response Codes > Client Error (4xx)
*   **Quantidade:** 120 URLs
*   **Exemplos Críticos:**
    *   `https://www.exemplo-ecommerce.com.br/produtos/tenis-corrida-antigo` (404) - Link interno de 5 páginas de categoria.
    *   `https://www.exemplo-ecommerce.com.br/ofertas/black-friday-2023` (410) - Ainda linkada na sidebar.
*   **Recomendação:** Implementar redirecionamentos 301 para páginas relevantes ou remover os links internos.

### 2. Cadeias de Redirecionamento

*   **Identificação:** Screaming Frog - Redirects > Redirect Chains
*   **Quantidade:** 55 cadeias (mínimo 3 saltos)
*   **Exemplos Críticos:**
    *   `/categoria-velha` (301) -> `/categoria-nova` (301) -> `/categoria-atualizada` (200)
    *   `/produto/descontinuado-v1` (301) -> `/produto/descontinuado-v2` (301) -> `/produto/similar-atual` (200)
*   **Recomendação:** Consolidar para um único redirecionamento 301 direto (Ex: `/categoria-velha` para `/categoria-atualizada`).

### 3. Páginas Importantes com Diretiva Noindex

*   **Identificação:** Screaming Frog - Indexability > Non-Indexable (Noindex), GSC - Indexação > Páginas (Excluídas por tag 'noindex')
*   **Quantidade:** 32 URLs
*   **Exemplos Críticos:**
    *   `https://www.exemplo-ecommerce.com.br/categoria/promocoes` (noindex) - Página com alto potencial de tráfego.
    *   `https://www.exemplo-ecommerce.com.br/blog/melhores-produtos-2024` (noindex) - Artigo de conteúdo pilar.
*   **Recomendação:** Remover a tag `noindex` dessas páginas e solicitar reindexação no GSC.

### 4. Conteúdo Bloqueado por robots.txt

*   **Identificação:** GSC - Configurações > Rastreamento > robots.txt tester
*   **Quantidade:** 3 pastas bloqueadas acidentalmente.
*   **Exemplos Críticos:**
    *   `Disallow: /assets/css/` (Bloqueia arquivos CSS essenciais para renderização).
    *   `Disallow: /js/` (Bloqueia arquivos JS críticos para interatividade).
*   **Recomendação:** Ajustar o arquivo `robots.txt` para permitir o rastreamento de recursos essenciais (`Allow: /assets/css/`, `Allow: /js/`).

---

### Plano de Ação para Otimização de Core Web Vitals

```
# Plano de Ação: Otimização de Core Web Vitals

**Data do Plano:** 2024-10-27
**Site:** www.exemplo-ecommerce.com.br
**Ferramentas:** Google PageSpeed Insights, Lighthouse, Google Search Console

## Resumo das Métricas Atuais (Exemplo: Homepage)

*   **LCP (Largest Contentful Paint):** 4.8s (Meta: < 2.5s)
*   **CLS (Cumulative Layout Shift):** 0.35 (Meta: < 0.1)
*   **INP (Interaction to Next Paint):** 450ms (Meta: < 200ms)
*   **TTFB (Time To First Byte):** 850ms (Meta: < 600ms)

## Plano de Ação Detalhado

### 1. Otimização de Imagens (Foco no LCP e CLS)

*   **Problema:** Imagem de banner principal (3.5MB, JPG) na homepage e imagens de produtos grandes sem dimensionamento explícito.
*   **Ações:**
    *   **Ação 1.1:** Comprimir todas as imagens JPG/PNG para WebP (Ex: Ferramenta Squoosh.app). **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-05.
    *   **Ação 1.2:** Implementar `srcset` e `sizes` para imagens responsivas. **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-10.
    *   **Ação 1.3:** Adicionar `width` e `height` explícitos em todas as tags `<img>`. **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-15.
    *   **Ação 1.4:** Implementar `loading="lazy"` para imagens abaixo da dobra. **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-15.

### 2. Otimização de CSS e JavaScript (Foco no INP e LCP)

*   **Problema:** Múltiplos arquivos CSS e JS não minificados, scripts de terceiros bloqueando o thread principal.
*   **Ações:**
    *   **Ação 2.1:** Minificar todos os arquivos CSS e JS. **Responsável:** Desenvolvedor Backend/DevOps. **Prazo:** 2024-11-12.
    *   **Ação 2.2:** Deferir ou carregar assincronamente scripts não críticos (Ex: scripts de análise de terceiros, pop-ups). **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-18.
    *   **Ação 2.3:** Identificar e remover CSS e JS não utilizado. **Responsável:** Desenvolvedor Frontend. **Prazo:** 2024-11-22.

### 3. Otimização do Servidor e Cache (Foco no TTFB)

*   **Problema:** Tempo de resposta do servidor elevado.
*   **Ações:**
    *   **Ação 3.1:** Analisar logs do servidor para identificar gargalos de processamento. **Responsável:** DevOps/Infraestrutura. **Prazo:** 2024-11-08.
    *   **Ação 3.2:** Implementar cache de página completa no servidor (Ex: Varnish, Redis). **Responsável:** DevOps/Infraestrutura. **Prazo:** 2024-11-25.
    *   **Ação 3.3:** Avaliar a necessidade de um CDN para recursos estáticos. **Responsável:** DevOps/Infraestrutura. **Prazo:** 2024-11-30.

### 4. Validação e Monitoramento

*   **Ações:**
    *   **Ação 4.1:** Re-executar testes no PageSpeed Insights após cada bloco de otimização. **Responsável:** Analista SEO Técnico. **Prazo:** Contínuo.
    *   **Ação 4.2:** Monitorar tendências das Core Web Vitals no Google Search Console e Google Analytics. **Responsável:** Analista SEO Técnico. **Prazo:** Mensal.

```

---

## Checklist

- [x] Rastreamento completo do site com Screaming Frog ou Sitebulb.
- [x] Verificação de todos os erros 4xx/5xx internos e externos.
- [x] Análise de cadeias de redirecionamento (>1 salto).
- [x] Auditoria de URLs não indexáveis (noindex, canonical, robots.txt) para garantir que páginas importantes não estejam bloqueadas.
- [x] Validação do arquivo `robots.txt` para permissão de rastreamento de recursos críticos (CSS, JS) e páginas importantes.
- [x] Inspeção de sitemaps XML para URLs 4xx/5xx, URLs `noindex` e inclusão de todas as URLs canônicas.
- [x] Teste de Core Web Vitals (LCP, CLS, INP) para páginas críticas via Google PageSpeed Insights/Lighthouse.
- [x] Verificação de canonicalização (tags `rel="canonical"`) para evitar conteúdo duplicado.
- [x] Auditoria de implementação de `hreflang` para sites multi-idioma/multi-região.
- [x] Teste de compatibilidade mobile-first com a ferramenta "Mobile-Friendly Test" do Google.
- [x] Verificação de segurança HTTPS (certificado válido, redirecionamento HTTP para HTTPS).
- [x] Auditoria de Schema Markup (estrutura de dados) com Google Rich Results Test.

---

## Métricas de Referência

| Métrica                         | Benchmark (Bom) | Meta (Exemplo) |
|---------------------------------|-----------------|----------------|
| Taxa de Indexação               | > 90%           | 95%            |
| Erros de Rastreamento (GSC)     | < 1%            | 0.5%           |
| LCP (Largest Contentful Paint)  | < 2.5s          | < 2.0s         |
| CLS (Cumulative Layout Shift)   | < 0.1           | < 0.05         |
| INP (Interaction to Next Paint) | < 200ms         | < 150ms        |
| TTFB (Time To First Byte)       | < 600ms         | < 400ms        |

---

## Erros Comuns

1.  **Bloqueio de recursos críticos via `robots.txt`**: Um `Disallow: /wp-content/themes/` pode impedir o Googlebot de renderizar corretamente as páginas, prejudicando o ranqueamento.
    *   **Como evitar**: Use o `robots.txt tester` do Google Search Console. Sempre teste o impacto de qualquer alteração no `robots.txt` e permita o rastreamento de CSS, JavaScript e imagens que afetam a renderização.
2.  **Canonicalização incorreta em URLs com parâmetros**: Páginas de filtro ou ordenação (Ex: `/?sort=price` ou `/?color=blue`) usando `rel="canonical"` para si mesmas em vez da versão limpa, criando milhares de URLs duplicadas.
    *   **Como evitar**: Implemente `rel="canonical"` apontando para a versão principal/limpa da URL (Ex: `https://www.loja.com/categoria-de-produtos`) em todas as variações com parâmetros que não devem ser indexadas. Use também os "Parâmetros de URL" no GSC para informar ao Google como tratar esses parâmetros.
3.  **Cadeias de redirecionamento longas ou loops**: Múltiplos redirecionamentos (Ex: A > B > C > D) ou redirecionamentos circulares (A > B > A) que desperdiçam orçamento de rastreamento e degradam a experiência do usuário.
    *   **Como evitar**: Monitore o relatório de redirecionamentos de ferramentas de rastreamento como Screaming Frog. Consolide as cadeias para um único redirecionamento 301 (Ex: A > D). Corrija loops imediatamente.

---

## Dicas Avançadas

1.  **Análise de Log de Servidor para Otimização de Orçamento de Rastreamento**: Em vez de apenas confiar no GSC, baixe os logs de acesso do seu servidor e use ferramentas como o Screaming Frog Log File Analyser. Identifique quais URLs o Googlebot está rastreando mais frequentemente, quais são rastreadas com `noindex` ou `canonical` para outras páginas, e quais são raramente visitadas. Isso permite otimizar a estrutura de links internos e o `robots.txt` para direcionar o Googlebot às páginas mais importantes. Ex: Se o Googlebot gasta 30% do rastreamento em URLs de paginação que são `noindex`, ajuste a linkagem interna ou o `robots.txt` para direcionar esse esforço para páginas de produto.
2.  **Implementação de Renderização Dinâmica para Sites JavaScript-Heavy (SPAs/PWAs)**: Para Single Page Applications (SPAs) ou Progressive Web Apps (PWAs) que dependem fortemente de JavaScript para renderizar conteúdo, o Google pode ter dificuldades em rastrear e indexar. Implemente renderização dinâmica configurando um servidor que detecta o Googlebot (via User-Agent) e serve uma versão pré-renderizada em HTML/CSS, enquanto usuários normais recebem a versão JS. Ferramentas como Rendertron ou Puppeteer podem ser usadas para isso. Ex: um site de notícias em React que usa renderização dinâmica para garantir que o Googlebot veja o conteúdo completo do artigo.
3.  **Validação de `hreflang` com Ferramentas Específicas e GSC**: Para sites multilíngues, a implementação de `hreflang` é complexa. Além de verificar a sintaxe com um crawler, utilize o relatório de "Segmentação Internacional" do Google Search Console (se disponível, em propriedades de domínio mais antigas) e ferramentas como o `hreflang.ninja` ou scripts customizados. Verifique reciprocidade (se a página A aponta para B, B deve apontar para A) e consistência entre as URLs. Ex: Garantir que `https://www.exemplo.com/en-us/` e `https://www.exemplo.com/pt-br/` tenham `hreflang` apontando corretamente uma para a outra, incluindo a tag `x-default`.
4.  **Auditoria de Acessibilidade do Crawler (WRS - Web Rendering Service)**: Use a ferramenta de "Inspeção de URL" do Google Search Console na aba "Teste de URL ativa" e depois "Ver página testada" para ver a captura de tela e o HTML renderizado. Compare o HTML renderizado com o HTML bruto para identificar se há conteúdo importante que não está sendo carregado ou se a página está renderizando de forma inesperada para o Googlebot. Isso é crucial para depurar problemas de JavaScript SEO. Ex: Um botão de "ver mais" que carrega produtos via AJAX e cujo conteúdo não aparece no HTML renderizado pode indicar um problema de rastreamento de conteúdo dinâmico.
5.  **Monitoramento Ativo de Mudanças de Servidor e DNS**: Qualquer alteração no servidor (migração, atualização de CMS, mudança de CDN, alteração de DNS) pode ter um impacto técnico profundo no SEO. Utilize ferramentas de monitoramento de disponibilidade (Ex: UptimeRobot) e faça rastreamentos pós-migração completos para verificar se não há novos erros 4xx/5xx, lentidão de carregamento ou problemas de indexação. Ex: Após uma migração de servidor, observe um pico de erros 5xx no GSC e uma queda no TTFB, indicando uma configuração inadequada do novo ambiente.