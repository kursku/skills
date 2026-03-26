---
name: redirects-migration
description: "Redirects Migration — Skill especializada para planejamento, execução e validação de migrações de redirecionamentos 301."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Redirects Migration

Esta skill capacita o Claude a planejar, executar e validar migrações de redirecionamentos 301 de forma eficiente, minimizando perdas de tráfego e autoridade SEO.

---

## Keywords

*   Redirecionamento 301
*   Migração de Site SEO
*   Mapeamento de URLs
*   Auditoria de Redirecionamentos
*   Link Equity Preservation
*   HTTP Status Codes
*   Arquivo .htaccess
*   Regex para Redirecionamento
*   Google Search Console Migração
*   Server-side Redirects
*   Cadeias de Redirecionamento
*   Perda de Tráfego Orgânico

---

## Quick Start

1.  **Exportar URLs Atuais**: Utilize o Google Search Console (Relatório "Páginas") e ferramentas de crawl como Screaming Frog para extrair todas as URLs indexadas e internas do domínio antigo ou subdomínio a ser migrado.
2.  **Mapear URL Antiga para Nova**: Crie uma planilha (`URL Antiga` | `URL Nova` | `Tipo de Redirecionamento`) e preencha com os redirecionamentos 1:1, identificando também URLs que retornarão 404 e precisarão de um destino relevante.
3.  **Gerar Regras de Redirecionamento**: Converta o mapeamento em regras de redirecionamento para o servidor (e.g., `.htaccess` para Apache, `nginx.conf` para Nginx). Priorize redirecionamentos 301 permanentes.
4.  **Testar Redirecionamentos em Staging**: Implemente as regras em um ambiente de homologação e utilize ferramentas como `curl -I` ou o verificador de status HTTP do Screaming Frog para validar cada redirecionamento antes da produção.
5.  **Monitorar Pós-Lançamento**: Após a implementação, acompanhe o Google Search Console para erros de rastreamento (404, 5xx) e o tráfego orgânico no Google Analytics para identificar anomalias nas primeiras 48-72 horas.

---

## Core Workflows

### Workflow 1: Auditoria Detalhada e Mapeamento de Redirecionamentos para Migração

Este workflow visa garantir que nenhuma URL importante seja esquecida e que o mapeamento seja o mais otimizado possível para preservar o valor de SEO.

1.  **Coleta Abrangente de URLs Existentes**:
    *   **URLs Indexadas (GSC)**: Acesse o Google Search Console do domínio antigo, vá em "Páginas" (ou "Cobertura" em versões anteriores) e exporte todas as URLs válidas. Priorize estas, pois são as que o Google já conhece e rankeia.
    *   **URLs do Sitemap XML**: Baixe e parse o sitemap.xml do site antigo para complementar a lista.
    *   **URLs de Backlinks (Ahrefs/SEMrush)**: Exporte as URLs com maior número de backlinks externos e maior autoridade. Essas são críticas para a preservação de Link Equity. Exemplo: Utilize Ahrefs Site Explorer, vá em "Best by links" e exporte as top 1000 URLs.
    *   **URLs com Tráfego Orgânico (GA)**: No Google Analytics (Universal Analytics: "Comportamento > Conteúdo do site > Todas as páginas"; GA4: "Engajamento > Páginas e telas"), exporte as URLs com maior tráfego orgânico nos últimos 12 meses.
    *   **URLs de Auditoria (Screaming Frog)**: Faça um crawl completo do site antigo com Screaming Frog para identificar todas as URLs internas, incluindo as que podem não estar no GSC ou sitemap, além de identificar redirecionamentos existentes (301, 302), 404s e 5xxs. Exemplo: configure `Configuração > Spider > Basic` para crawl padrão e exporte o relatório "Internal All".

2.  **Consolidação e Limpeza da Lista de URLs**:
    *   Combine todas as listas em uma única planilha mestre no Google Sheets ou Excel. Remova duplicatas.
    *   Classifique as URLs por prioridade: (1) Backlinks de alta autoridade, (2) Tráfego orgânico elevado, (3) Indexadas no GSC, (4) Outras internas. Utilize filtros e formatação condicional para destacar as de maior prioridade.

3.  **Mapeamento 1:1 e Estratégias de Redirecionamento**:
    *   Para cada `URL Antiga`, determine a `URL Nova` mais relevante. O ideal é um mapeamento 1:1.
    *   **Redirecionamento 301 (Permanente)**: Para URLs que têm um equivalente direto no novo site. Exemplo: `dominioantigo.com.br/produto-x` -> `dominionovo.com.br/categoria/produto-x`.
    *   **Redirecionamento para Categoria/Home**: Se uma página antiga não tiver um equivalente direto, redirecione para uma página de categoria relevante ou, em último caso, para a homepage. Evite redirecionar para a home em massa. Exemplo: `dominioantigo.com.br/antiga-pagina-descontinuada` -> `dominionovo.com.br/categoria-relacionada`.
    *   **Identificação de 404s (e tratativa)**: URLs que não têm equivalente e não se encaixam em nenhuma categoria relevante devem retornar 404. Garanta que o 404 customizado seja útil para o usuário. Monitore 404s no GSC pós-migração.
    *   **Redirecionamentos por Regex**: Para padrões de URLs que mudaram, use expressões regulares para criar regras de redirecionamento em massa. Isso economiza tempo e minimiza erros manuais. Exemplo: Todas as URLs de `/blog/antigo-post-id/` para `/blog/novo-post-slug/` podem ser tratadas com uma única regra regex.

4.  **Validação Pré-Implementação**:
    *   Revise o mapeamento com stakeholders (produto, conteúdo) para garantir a relevância dos destinos.
    *   Faça um "sanity check" manual em amostras de URLs de cada prioridade para confirmar que o mapeamento faz sentido lógico e SEO.

### Workflow 2: Implementação e Validação de Redirecionamentos em Ambientes de Produção

Este workflow aborda a fase de execução, focando na correta implementação e validação dos redirecionamentos para garantir a integridade da migração.

1.  **Geração das Regras de Redirecionamento para Servidor**:
    *   **Apache (.htaccess)**: Para a maioria dos servidores LAMP, o arquivo `.htaccess` é o mais comum. Utilize `Redirect 301` para regras simples e `RewriteRule` com `RewriteCond` para regex. A ordem é crucial: regras mais específicas devem vir antes das mais genéricas.
        ```apache
        # Exemplo de regra 1:1
        RedirectMatch 301 ^/pagina-antiga.html$ https://www.novodominio.com.br/nova-pagina-equivalente/

        # Exemplo de regra Regex para toda uma categoria
        RewriteRule ^antiga-categoria/(.*)$ https://www.novodominio.com.br/nova-categoria/$1 [R=301,L]
        ```
    *   **Nginx (nginx.conf)**: No Nginx, as regras são configuradas diretamente no arquivo `nginx.conf` ou em arquivos de configuração de hosts virtuais.
        ```nginx
        # Exemplo de regra 1:1
        location = /pagina-antiga.html {
            return 301 https://www.novodominio.com.br/nova-pagina-equivalente/;
        }

        # Exemplo de regra Regex para toda uma categoria
        rewrite ^/antiga-categoria/(.*)$ https://www.novodominio.com.br/nova-categoria/$1 permanent;
        ```
    *   **Outros Servidores/CDNs**: Verifique a documentação do seu ambiente (IIS, Cloudflare Page Rules, Azure Front Door, etc.) para a sintaxe correta.

2.  **Implantação em Ambiente de Staging/Homologação**:
    *   Sempre implemente e teste os redirecionamentos em um ambiente de não-produção primeiro.
    *   Garanta que o ambiente de staging replique o mais fielmente possível o ambiente de produção, incluindo o servidor web e a configuração DNS, se aplicável.

3.  **Validação Exaustiva dos Redirecionamentos (Pré-Produção)**:
    *   **Teste de Amostra Crítica**: Use o Screaming Frog em modo "List" ou "Paste" para verificar um subconjunto de URLs críticas (com alto tráfego, muitos backlinks) da sua lista de mapeamento. Exporte a lista de URLs antigas, cole no Screaming Frog e configure para seguir redirecionamentos. Verifique o status HTTP final (deve ser 200) e a URL final.
    *   **`curl` para Validação Pontual**: Para verificações rápidas de URLs específicas, use a linha de comando: `curl -I https://www.dominioantigo.com.br/url-exemplo/`. O cabeçalho `Location` mostrará para onde a URL foi redirecionada, e o código de status deve ser `HTTP/1.1 301 Moved Permanently`.
    *   **Verificação de Cadeias de Redirecionamento**: Ferramentas como `httpstatus.io` ou o relatório de "Redirect Chains" do Screaming Frog são essenciais para identificar e corrigir cadeias de redirecionamento (mais de um 301/302 para chegar ao destino final), que podem atrasar o rastreamento e diluir o PageRank. Idealmente, uma URL deve ter no máximo um redirecionamento.

4.  **Go-Live e Monitoramento Pós-Migração**:
    *   **Atualização de Servidor DNS**: Após a migração de domínio, certifique-se de que os registros DNS do domínio antigo apontem para o novo servidor onde os redirecionamentos estão configurados (se a migração for de domínio completo).
    *   **Google Search Console**:
        *   **Relatório "Páginas"**: Monitore o relatório para identificar picos de erros 404 ou 5xx. URLs antigas com 301 devem gradualmente desaparecer, e as novas devem aparecer.
        *   **Ferramenta de Alteração de Endereço**: Se for uma mudança de domínio, utilize a ferramenta "Alteração de Endereço" no GSC para notificar o Google.
    *   **Google Analytics**:
        *   Monitore o tráfego orgânico geral e por página/grupo de páginas. Compare com períodos anteriores para identificar quedas inesperadas.
        *   Analise o tempo no site, taxa de rejeição e conversões para garantir que a experiência do usuário não foi prejudicada.
    *   **Ferramentas de Auditoria Externa**: Faça um novo crawl completo com Screaming Frog no novo domínio para identificar quaisquer links internos quebrados ou cadeias de redirecionamento que surgiram.

---

## Templates

### Planilha de Mapeamento de URLs para Migração (Google Sheets/Excel)

```csv
"URL Antiga","URL Nova","Tipo de Redirecionamento","Prioridade (1-5)","Observações"
"https://www.dominioantigo.com