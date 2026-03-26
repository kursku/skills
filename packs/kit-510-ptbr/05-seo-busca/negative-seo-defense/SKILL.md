---
name: negative-seo-defense
description: "Negative Seo Defense — Skill especializada para negative seo defense"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Negative Seo Defense

Esta skill capacita o Claude a identificar, mitigar e recuperar-se eficazmente de ataques de SEO negativo, protegendo a integridade e o ranking de sites.

---

## Keywords

Disavow Tool, Spam Backlinks, Negative SEO Audit, SERP Monitoring, Google Search Console Alerts, De-ranking Attacks, Content Scraping Defense, Fake Reviews Mitigation, Competitor Negative SEO Analysis, Link Spam Detection, Manual Actions Recovery, Cloaking Detection, DDoS Mitigation, Brand Reputation Monitoring.

---

## Quick Start

1.  **Configurar Alertas Críticos no GSC**: Ative notificações por e-mail para "Ações Manuais", "Problemas de Segurança" e "Novas Páginas Indexadas" no Google Search Console, direcionando para um e-mail monitorado diariamente.
2.  **Monitoramento Diário de Backlinks**: Utilize Ahrefs ou Semrush para varrer novos backlinks diariamente, aplicando filtros para "Domain Rating (DR) < 10" e "Spam Score > 50%" para identificar padrões suspeitos.
3.  **Implementar Verificação de Conteúdo Raspado**: Configure alertas do Google ou utilize ferramentas como Copyscape para detectar conteúdo idêntico publicado em outros domínios, com foco em URLs recém-publicadas do seu site.
4.  **Monitorar Log de Servidor e Tráfego**: Revise os logs de acesso do servidor e gráficos de tráfego (Google Analytics/Cloudflare) em busca de picos incomuns de requisições por IP ou tentativas de acesso a URLs inexistentes, que podem indicar ataques DDoS ou crawling malicioso.

---

## Core Workflows

### Workflow 1: Detecção e Disavow Proativo de Backlinks Tóxicos

Este workflow detalha o processo para identificar e neutralizar ataques de link building negativo antes que causem danos significativos ao ranking.

**Passos Detalhados:**

1.  **Coleta de Dados de Backlinks**:
    *   **Ferramentas**: Ahrefs, Semrush, Majestic, Google Search Console (GSC).
    *   **Ação**: Exportar todos os novos backlinks detectados nas últimas 24-48 horas. Priorize ferramentas que ofereçam métricas de toxicidade ou spam score.
    *   **Exemplo**: No Ahrefs, vá para "Backlinks" > "New" e exporte links com "DR < 10" e "Traffic < 100". No Semrush, use a ferramenta "Link Audit" para identificar backlinks com "Toxic Score" alto.
2.  **Análise de Padrões Suspeitos**:
    *   **Foco**: Identificar links de domínios irrelevantes, de baixa qualidade, geograficamente distantes sem contexto, com excesso de âncoras exatas ou de PBNs (Private Blog Networks).
    *   **Métricas Chave**:
        *   **Domain Rating (DR) / Authority Score (AS)**: Baixo (0-10).
        *   **Trust Flow (TF) / Citation Flow (CF)**: Desproporcionalmente baixo TF em relação ao CF.
        *   **IPs e Nomes de Domínio**: Padrões de IPs de baixa qualidade, domínios com nomes aleatórios ou temáticos de spam (farmácia, cassino).
        *   **Conteúdo do Site de Origem**: Conteúdo genérico, irrelevante ou em idioma estrangeiro sem contexto.
    *   **Exemplo Concreto**: Você detecta 5.000 novos backlinks de 300 domínios diferentes, todos com DR 0-5, Trust Score 0 e hospedados em IPs de países como Rússia e China. As âncoras são 100% "melhor seguro auto", "comprar carro barato". Isso é um ataque clássico.
3.  **Criação do Arquivo Disavow**:
    *   **Formato**: Arquivo `.txt` listando URLs ou domínios. Recomenda-se desautorizar domínios inteiros para ataques em massa.
    *   **Regra**: Cada URL ou `domain:` em uma nova linha. Adicione comentários com `#`.
    *   **Exemplo**: Se identificar que `farmaciarussa.ru` e `cassinoonline.net` estão enviando múltiplos links tóxicos, adicione `domain:farmaciarussa.ru` e `domain:cassinoonline.net` ao arquivo. Se apenas uma página específica for o problema, use a URL completa.
4.  **Upload no Google Search Console**:
    *   **Ferramenta**: Google Disavow Tool (https://search.google.com/search-console/disavow-links).
    *   **Ação**: Selecione a propriedade do site e carregue o arquivo `.txt`. O Google pode levar semanas para processar.
    *   **Exemplo**: Após criar `disavow-2024-07-26.txt` com a lista de domínios tóxicos, acesse a ferramenta, selecione `meusite.com.br` e faça o upload.
5.  **Monitoramento Pós-Disavow**:
    *   **Ação**: Continue monitorando o perfil de backlinks e o GSC para verificar se novos links tóxicos surgem e se o ranking está se estabilizando ou recuperando.
    *   **Exemplo**: Após 3-4 semanas, verifique no GSC se a seção "Links para o seu site" mostra menos links dos domínios desautorizados e se houve recuperação de posições para as keywords afetadas.

### Workflow 2: Resposta a Ataques de Conteúdo Raspado (Scraping) e Duplicado

Este workflow descreve como agir quando seu conteúdo original é copiado e publicado em outros sites, potencialmente diluindo a autoridade do seu domínio.

**Passos Detalhados:**

1.  **Detecção de Conteúdo Duplicado**:
    *   **Ferramentas**: Google Alerts (para títulos e frases-chave), Copyscape, Siteliner (para conteúdo interno).
    *   **Ação**: Configure alertas para os títulos exatos e trechos de parágrafos de seus artigos mais importantes. Realize varreduras semanais com Copyscape.
    *   **Exemplo**: Um novo artigo "Guia Completo de SEO para E-commerce 2024" é publicado. Configure um Google Alert para a frase exata. Uma semana depois, o alerta notifica que `ecommerce-pirata.com/seo-guia` publicou o mesmo conteúdo.
2.  **Verificação da Data de Publicação Original**:
    *   **Ação**: Confirme que seu conteúdo é o original. Verifique a data de publicação no seu site, no GSC (data de rastreamento/indexação) e use o operador `inurl:` ou `site:` no Google para verificar a data de indexação do conteúdo raspado.
    *   **Exemplo**: Seu artigo foi publicado em `meusite.com.br/guia-seo` em 01/07/2024. O site `ecommerce-pirata.com` publicou em 20/07/2024. A prova de originalidade é clara.
3.  **Primeira Tentativa de Contato (se possível)**:
    *   **Ação**: Se o site raspador tiver informações de contato claras, envie um e-mail amigável solicitando a remoção do conteúdo ou a inclusão de um link canônico para sua URL original.
    *   **Exemplo**: Envie um e-mail para `contato@ecommerce-pirata.com` explicando que o conteúdo foi copiado e solicitando a remoção ou um `rel="canonical"` apontando para `https://meusite.com.br/guia-seo`.
4.  **Envio de Notificação DMCA (Digital Millennium Copyright Act)**:
    *   **Ação**: Se o contato inicial falhar ou não houver dados de contato, identifique o provedor de hospedagem do site infrator (via Whois lookup) e envie uma notificação DMCA formal. Muitos provedores têm formulários específicos.
    *   **Exemplo**: Use `whois.com` para descobrir que `ecommerce-pirata.com` é hospedado pela Hostinger. Vá ao site da Hostinger, procure por "DMCA Takedown Request" e preencha o formulário, anexando provas da sua autoria.
5.  **Bloqueio de IPs Maliciosos (Opcional, mas Avançado)**:
    *   **Ação**: Se um scraper específico estiver causando problemas recorrentes, você pode bloquear seu endereço IP via `.htaccess` ou através do firewall do seu CDN (ex: Cloudflare WAF).
    *   **Exemplo**: Os logs do servidor mostram que o IP `192.168.1.100` está fazendo milhares de requisições por hora, baixando todas as suas páginas. Adicione `Deny from 192.168.1.100` ao seu `.htaccess` ou crie uma regra de bloqueio no Cloudflare.
6.  **Uso de `rel="canonical"` (para conteúdo autorizado/sindicado)**:
    *   **Ação**: Se você autorizou a republicação do seu conteúdo em outro site (sindicação), garanta que eles usem a tag `<link rel="canonical" href="https://seusite.com.br/url-original/">` apontando para sua versão.
    *   **Exemplo**: Você permite que um parceiro republique seu artigo. Eles devem incluir `<link rel="canonical" href="https://meusite.com.br/guia-seo">` na seção `<head>` da página deles.

---

## Templates

### Template de Arquivo Disavow para GSC

```
# Lista de domínios e URLs para desautorizar devido a Negative SEO
# Data da atualização: 2024-07-26
# Motivo: Ataque de Backlinks Tóxicos (Negative SEO) detectado via Semrush Link Audit.
# Domínios com Trust Score <= 10 e mais de 500 links para meu domínio.
domain:spamsite-farmacia.ru
domain:badlink-casino.xyz
domain:generico-linkfarm.net
https://blog-spammy.com/post-com-ancora-exata-indesejada
domain:pharma-russia-links.info
domain:free-money-now.biz
# URL específica de um diretório de artigos com links irrelevantes
https://directory-articles.com/category/seo-tips/link-aleatorio-para-meu-site.html
```

### Template de Solicitação DMCA para Provedor de Hospedagem

```
ASSUNTO: Notificação de Violação de Direitos Autorais - Conteúdo Raspado de [Seu Nome da Empresa/Site]

PARA: [Nome do Provedor de Hospedagem, ex: Hostinger Abuse Department]
EMAIL: [Endereço de e-mail de abuso do provedor, ex: abuse@hostinger.com]
DE: [Seu Nome/Nome da Empresa]
EMAIL: [Seu Email, ex: contato@meusite.com.br]
TELEFONE: [Seu Telefone (Opcional)]

Prezado(a) [Nome do Provedor de Hospedagem],

Esta é uma notificação formal de violação de direitos autorais sob a Digital Millennium Copyright Act (DMCA), 17 U.S.C. § 512.

Eu sou o(a) [proprietário(a)/representante legal] do conteúdo original protegido por direitos autorais localizado em:
[URL do seu conteúdo original (exemplo): https://meusite.com.br/melhores-praticas-seo-2024]
Data de publicação original no meu site: [Exemplo: 15 de Junho de 2024]

O site [Nome do Site Infrator], hospedado em seus servidores e localizado em [URL do site infrator (exemplo): https://siteinfrator.com.br/artigo-seo-copiado], está publicando uma cópia exata ou substancialmente similar do meu trabalho sem autorização. O conteúdo violador pode ser encontrado em:
[URL do conteúdo infrator (exemplo): https://siteinfrator.com.br/artigo-seo-copiado]

Anexo a esta notificação, incluo evidências da autoria e data de publicação original do meu conteúdo (ex: capturas de tela, metadados do artigo, URL do Google Search Console com data de indexação).

Solicito a remoção imediata deste conteúdo violador de seus servidores para que o site [siteinfrator.com.br] esteja em conformidade com a DMCA.

Tenho boa-fé que o uso do material protegido por direitos autorais, conforme descrito acima, não é autorizado pelo proprietário dos direitos autorais, seu agente ou pela lei. As informações contidas nesta notificação são precisas e, sob pena de perjúrio, sou o(a) proprietário(a) ou estou autorizado(a) a agir em nome do proprietário de um direito exclusivo que está sendo supostamente infringido.

Agradeço a sua pronta atenção a este assunto.

Atenciosamente,

[Sua Assinatura Digital/Nome Completo]
[Data: 26 de Julho de 2024]
```

---

## Checklist

- [x] Configurar alertas de segurança e ações manuais no Google Search Console para todas as propriedades.
- [x] Monitorar novos backlinks diariamente via Ahrefs/Semrush, aplicando filtros de toxicidade.
- [x] Auditar periodicamente o perfil de backlinks completo para identificar padrões de ataque persistentes (ex: links de PBNs, comentários spam de domínios específicos).
- [x] Verificar logs de servidor e relatórios de tráfego para picos incomuns de requisições que possam indicar DDoS ou crawling malicioso.
- [x] Implementar ferramentas de monitoramento de conteúdo duplicado (ex: Copyscape, Siteliner) para artigos recém-publicados e páginas de alto valor.
- [x] Revisar regularmente a indexação de páginas no GSC para detectar injeção de spam, páginas não autorizadas ou desindexações inesperadas.
- [x] Monitorar menções da marca e do site em fóruns, redes sociais e sites de avaliação para identificar ataques de reputação ou avaliações falsas.
- [x] Manter um arquivo `disavow.txt` atualizado e pronto para upload em caso de ataque de link building negativo.
- [x] Implementar ou revisar medidas de segurança web (WAF, CDN, plugin de segurança) para mitigar ataques DDoS e tentativas de injeção de malware.
- [x] Realizar backups regulares e seguros do site para garantir uma rápida recuperação em caso de comprometimento.

---

## Métricas de Referência

| Métrica | Benchmark (Pré-Ataque) | Meta (Pós-Defesa) |
|-------------------------------------|----------------------------------|-----------------------------------|
| Taxa de Links Tóxicos (Semrush/Ahrefs) | < 0.5% do total de backlinks | 0% (domínios desautorizados) |
| Duração Média de Ataque Ativo (Dias) | N/A | < 7 dias (detecção/disavow) |
| Queda de Posição Média (Top 10 Keywords) | Estável (variação < 2 posições) | Recuperação para variação < 2 posições |
| Tempo de Resolução de Ação Manual (GSC) | N/A | < 30 dias |
| % de Conteúdo Raspado Detectado | 0% | 0% (após ação DMCA/bloqueio) |
| Variação Inesperada de Tráfego Orgânico | +/- 2% semanal | Retorno à variação +/- 2% |

---

## Erros Comuns

1.  **Ignorar alertas do Google Search Console**: Não configurar ou não agir prontamente em alertas de segurança, ações manuais ou problemas de indexação pode levar a danos prolongados.
    *   **Como evitar**: Configure notificações por e-mail para todos os tipos de alertas críticos no GSC (Ações Manuais, Problemas de Segurança, Problemas de Core Web Vitals) e designe um responsável para revisá-los diariamente. Por exemplo, um alerta de "Problemas de segurança" pode indicar injeção de spam em páginas existentes, exigindo ação imediata.
2.  **Disavow excessivo ou incorreto**: Desautorizar links que não são tóxicos, que foram adquiridos naturalmente, ou não seguir o formato correto do arquivo `disavow.txt` pode prejudicar o SEO ao remover links válidos.
    *   **Como evitar**: Use ferramentas de análise de backlinks (Ahrefs, Semrush, Majestic) para identificar links com scores de spam muito altos e domínios notoriamente ruins. Analise manualmente cada domínio antes de adicionar ao disavow. Exemplo: links de domínios com DR 0, Trust Score 0, milhares de links externos e conteúdo irrelevante são candidatos. Evite desautorizar domínios que você não tem certeza se são maliciosos.
3.  **Não documentar ataques**: A falha em registrar datas, tipos de ataque, URLs afetadas e ações tomadas dificulta a análise, a comunicação com o Google e a recuperação futuras.
    *   **Como evitar**: Mantenha um log detalhado em uma planilha ou sistema de gerenciamento de projetos. Exemplo de entrada: "2024-07-25: Início de ataque de backlinks tóxicos (5k links de farmácias russas). GSC Manual Action alert esperado. Ação: Análise e preparação de disavow. Responsável: João. Status: Disavow enviado 2024-07-26."
4.  **Acreditar que o Disavow é uma solução instantânea**: O processo de disavow leva tempo para ser processado pelo Google, e a recuperação do ranking não é imediata.
    *   **Como evitar**: Gerencie as expectativas. O Google leva semanas ou até meses para reavaliar o perfil de links após um disavow. Continue monitorando e considere outras estratégias de SEO positivo (link building white hat, melhoria de conteúdo) para acelerar a recuperação.

---

## Dicas Avançadas

1.  **Monitoramento Preditivo de SERP para Desindexação**: Utilize ferramentas de rastreamento de ranking que monitoram as SERPs para variações bruscas de ranking em keywords cruciais (quedas de 10+ posições em 24h), mesmo antes que o GSC notifique uma ação manual. Isso pode indicar um ataque de desindexação, cloaking ou remoção de páginas do índice.
    *   **Exemplo Prático**: Um site que estava consistentemente na posição 5 para "melhor software ERP" cai para a posição 25 da noite para o dia sem nenhuma alteração no site. Isso pode ser um sinal de que concorrentes estão tentando desindexar seu conteúdo ou que o Google detectou algo. A investigação deve incluir `site:seusite.com.br palavra-chave` para verificar a indexação.
2.  **Análise de Padrões de Ataque de Concorrentes (Forensic SEO)**: Não apenas desautorize links, mas tente identificar os PBNs (Private Blog Networks) ou padrões de ataque que um concorrente pode estar usando contra você ou outros. Isso pode envolver analisar os domínios de referência de outros concorrentes que também foram atacados.
    *   **Exemplo Prático**: Você percebe que vários sites de nicho similar ao seu recebem links de um grupo específico de 20-30 domínios com conteúdo genérico, sem tráfego e com links ocultos para diversos alvos. Isso sugere uma PBN e, ao identificar os domínios principais, você pode prever futuros ataques ou até mesmo denunciá-los.
3.  **Honeypots para Scrapers de Conteúdo**: Crie conteúdo "isca" (honeypots) com links ocultos, tags específicas ou strings de texto únicas que, quando raspados e publicados, denunciam o scraper. Isso permite rastrear e bloquear os IPs dos infratores ou enviar DMCA mais rapidamente.
    *   **Exemplo Prático**: Em um parágrafo que você suspeita ser frequentemente raspado, inclua um link `nofollow` para um domínio de rastreamento controlado (`tracking.seusite.com`) que registra os IPs de quem o acessa. Ao ver o link em um site raspador, você sabe o IP do agressor.
4.  **Uso de Content Delivery Networks (CDN) com Web Application Firewalls (WAF) Avançados**: CDNs como Cloudflare ou Sucuri oferecem WAFs que podem identificar e mitigar ataques DDoS, injeção de SQL, XSS e outros ataques de segurança que podem ser parte de uma estratégia de SEO negativo.
    *   **Exemplo Prático**: Configure regras no WAF para bloquear IPs com mais de 100 requisições por segundo para páginas específicas, que tentem acessar URLs não existentes (`404`) de forma massiva ou que usem user-agents suspeitos. Isso previne o esgotamento de recursos do servidor e o crawling malicioso.
5.  **Hardening de Segurança do Servidor e da Aplicação**: Além das ferramentas de SEO, garanta que seu servidor e aplicação web (WordPress, Magento, etc.) estejam robustos contra vulnerabilidades. Ataques de SEO negativo podem incluir injeção de malware para desfigurar o site, criar backdoors ou redirecionar usuários.
    *   **Exemplo Prático**: Mantenha todos os plugins e temas atualizados, utilize senhas fortes, desative XML-RPC se não for necessário, e implemente cabeçalhos de segurança HTTP (X-XSS-Protection, Content-Security-Policy). Um site comprometido pode ser usado para hospedar spam ou links tóxicos para outros sites, resultando em uma ação manual do Google.