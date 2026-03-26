---
name: cookie-policy
description: "Cookie Policy — Skill especializada para cookie policy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: safe
---

# Cookie Policy

Esta skill capacita o Claude a criar, revisar e implementar políticas de cookies em conformidade com as leis de privacidade, como LGPD e GDPR.

---

## Keywords

LGPD, GDPR, Cookies, Consentimento de Cookies, Opt-in, Opt-out, Privacidade de Dados, Rastreamento Online, DPO, CMP, E-privacy, Política de Privacidade, Retenção de Dados, Aviso de Cookies.

---

## Quick Start

1.  **Mapear Cookies Atuais**: Utilize uma ferramenta de auditoria de cookies para identificar todos os cookies (próprios e de terceiros) ativos no site.
2.  **Classificar e Justificar**: Categorize cada cookie (necessário, funcional, analítico, marketing) e determine a base legal para seu uso.
3.  **Elaborar Rascunho da Política**: Redija as seções essenciais da política de cookies, detalhando os tipos, finalidades e como os usuários podem gerenciá-los.
4.  **Integrar CMP**: Configure uma Plataforma de Gestão de Consentimento (CMP) para exibir o banner de consentimento e gerenciar as preferências do usuário.
5.  **Publicar e Monitorar**: Publique a política em local visível no site e estabeleça um processo de revisão periódica e re-mapeamento.

---

## Core Workflows

### Workflow 1: Criação e Implementação de uma Nova Política de Cookies

Este workflow detalha a construção de uma política de cookies do zero para um novo website ou aplicação, garantindo conformidade desde o início.

**Passo 1: Mapeamento Detalhado de Cookies e Tecnologias de Rastreamento**
*   **Ação**: Realize uma varredura completa no site utilizando ferramentas como Cookiebot, OneTrust ou TrustArc. Esta etapa visa identificar todos os cookies, pixels, tags e outras tecnologias de rastreamento em uso, tanto de primeira parte quanto de terceiros.
*   **Exemplo Prático**: Para o domínio `www.minhaempresa.com.br`, a varredura revelou:
    *   `_ga` (Google Analytics): Cookie de terceiros, analítico, persistente.
    *   `_fbp` (Facebook Pixel): Cookie de terceiros, marketing, persistente.
    *   `sessionid`: Cookie de primeira parte, estritamente necessário, de sessão.
    *   `__cfduid` (Cloudflare): Cookie de terceiros, funcional, persistente.
    *   `_gcl_au` (Google Ads): Cookie de terceiros, marketing, persistente.
*   **Dados Concretos**: Registre o nome do cookie, provedor, finalidade, categoria, expiração e se é de primeira ou terceira parte.

**Passo 2: Definição da Base Legal para Cada Categoria de Cookie**
*   **Ação**: Com base no mapeamento, determine a base legal aplicável para cada categoria de cookie, conforme LGPD e GDPR. Cookies estritamente necessários geralmente se baseiam no legítimo interesse (ou execução de contrato), enquanto cookies analíticos, de funcionalidade e de marketing exigem consentimento explícito.
*   **Exemplo Prático**:
    *   **Cookies Estritamente Necessários** (`sessionid`): Legítimo interesse da empresa para garantir a funcionalidade básica do site.
    *   **Cookies de Performance/Analíticos** (`_ga`): Consentimento explícito do usuário.
    *   **Cookies de Funcionalidade** (`__cfduid`): Consentimento explícito do usuário, pois afetam a experiência personalizada.
    *   **Cookies de Publicidade/Marketing** (`_fbp`, `_gcl_au`): Consentimento explícito do usuário.

**Passo 3: Redação da Política de Cookies com Cláusulas Essenciais**
*   **Ação**: Elabore o texto da política, garantindo que seja claro, conciso e em linguagem acessível. Inclua todas as seções obrigatórias por lei.
*   **Estrutura da Política (Exemplo):**
    *   **Introdução**: Breve explicação sobre o que é a política e seu propósito.
    *   **O que são Cookies**: Definição simples de cookies e tecnologias similares.
    *   **Tipos de Cookies Utilizados**: Classificação e descrição detalhada dos cookies mapeados (ver Template 1).
    *   **Como Gerenciar Suas Preferências de Cookies**: Instruções claras sobre como o usuário pode aceitar, rejeitar ou alterar seu consentimento (ver Template 2).
    *   **Período de Retenção**: Informação sobre por quanto tempo os dados dos cookies são armazenados.
    *   **Alterações na Política de Cookies**: Aviso sobre revisões futuras.
    *   **Contato**: Dados de contato do Controlador de Dados ou DPO.

**Passo 4: Implementação e Configuração de uma Plataforma de Gerenciamento de Consentimento (CMP)**
*   **Ação**: Escolha e configure um CMP (ex: OneTrust, Cookiebot, TrustArc, Usercentrics) que se integre ao seu site. O CMP deve exibir um banner de consentimento no primeiro acesso do usuário, permitindo opt-in/opt-out granular para diferentes categorias de cookies, e bloquear cookies não essenciais antes do consentimento.
*   **Exemplo Prático**: No OneTrust, configure um banner que aparece na parte inferior da tela, com as opções "Aceitar Todos", "Rejeitar Não Essenciais" e "Gerenciar Preferências". Certifique-se de que, ao selecionar "Rejeitar Não Essenciais", os scripts de Google Analytics e Facebook Pixel sejam bloqueados automaticamente pelo CMP.
*   **Requisito de Bloqueio**: A CMP deve garantir que nenhum cookie não essencial seja carregado antes do consentimento explícito do usuário (pré-consentimento).

**Passo 5: Publicação, Teste e Auditoria Contínua**
*   **Ação**: Publique a política de cookies em um local facilmente acessível no site (ex: rodapé). Realize testes rigorosos para garantir que o CMP funcione corretamente em diferentes navegadores e dispositivos. Implemente auditorias regulares para verificar a conformidade.
*   **Teste Concreto**: Acesse o site em modo anônimo, rejeite cookies de marketing e verifique se as requisições de rede para `google-analytics.com` ou `facebook.com/tr` não são iniciadas. Verifique também se a política está linkada corretamente no banner de consentimento.

### Workflow 2: Revisão e Atualização Periódica de uma Política de Cookies Existente

Este workflow foca em manter a política de cookies atualizada e em conformidade com as mudanças legais e tecnológicas.

**Passo 1: Verificação de Alterações Legislativas e Regulatórias**
*   **Ação**: Monitore ativamente as atualizações na LGPD (ANPD), GDPR (EDPB) e outras regulamentações de privacidade relevantes. Isso inclui novas diretrizes sobre o que constitui consentimento válido ou sobre o uso de certas tecnologias.
*   **Exemplo Prático**: A ANPD publicou uma nova orientação sobre a necessidade de um botão "Rejeitar Todos" visível no primeiro nível do banner de consentimento. A política existente e o CMP devem ser revisados para incorporar essa exigência, caso não a tenham.

**Passo 2: Re-mapeamento de Cookies e Tecnologias de Rastreamento no Site**
*   **Ação**: Realize uma nova varredura completa no site, idealmente a cada 3-6 meses, ou sempre que houver grandes mudanças no site (adição de novos plugins, ferramentas de marketing, etc.). Esta etapa é crucial para identificar novos cookies ou alterações nos existentes.
*   **Exemplo Prático**: Uma nova ferramenta de chat online (ex: Tawk.to) foi implementada e, na varredura, descobriu-se que ela adiciona um cookie funcional (`tawk_uuid`) e um cookie de sessão. A política e o CMP precisam ser atualizados para incluir e gerenciar este novo cookie.

**Passo 3: Análise da Validade da Base Legal e Descrições**
*   **Ação**: Compare o novo mapeamento com a política existente e o CMP para assegurar que a base legal e as descrições de cada cookie ainda são precisas e válidas. Verifique se o período de retenção ainda faz sentido.
*   **Exemplo Prático**: Anteriormente, cookies de análise eram baseados em legítimo interesse, mas a orientação atual da ANPD/EDPB exige consentimento explícito. A política deve ser atualizada para refletir essa mudança e o CMP reconfigurado para solicitar consentimento para esses cookies.

**Passo 4: Atualização do Texto da Política e Configurações do CMP**
*   **Ação**: Modifique o texto da política de cookies para refletir quaisquer novos cookies, alterações nas suas finalidades, bases legais ou períodos de retenção. Atualize também as descrições no CMP.
*   **Exemplo Prático**: Adicionar uma nova seção ou item na lista de cookies para `tawk_uuid`, descrevendo sua finalidade (suporte ao cliente) e informando que seu uso requer consentimento explícito. As configurações do CMP devem ser ajustadas para que o `tawk_uuid` seja classificado como "funcional" e bloqueado até o consentimento.

**Passo 5: Comunicação das Alterações e Registro da Nova Versão**
*   **Ação**: Se as alterações na política forem significativas (ex: mudança na forma como os dados são coletados ou utilizados), considere notificar os usuários ativos. Registre a data da atualização, a nova versão da política e as principais mudanças.
*   **Exemplo Prático**: Após uma atualização importante na política, exiba um banner "Nossa Política de Cookies foi atualizada. Por favor, revise-a." na próxima visita do usuário ou envie um e-mail para usuários registrados. Mantenha um histórico de versões da política para fins de auditoria.

---

## Templates

### Seção "Tipos de Cookies Utilizados"

```markdown
Nossa plataforma utiliza diferentes tipos de cookies para otimizar sua experiência e garantir a segurança dos nossos serviços:

1.  **Cookies Estritamente Necessários**: Estes cookies são essenciais para o funcionamento básico do site, permitindo que você navegue e utilize suas funcionalidades, como acessar áreas seguras da plataforma ou realizar compras. Sem eles, o site não funcionaria corretamente.
    *   **Exemplo**: `sessionid` (mantém o usuário logado), `csrftoken` (proteção contra ataques CSRF).
    *   **Provedor**: MinhaEmpresa.
    *   **Expiração**: Sessão.

2.  **Cookies de Desempenho e Análise**: Estes cookies coletam informações sobre como os visitantes usam o site (ex: páginas mais visitadas, tempo gasto em cada página, erros encontrados). Eles nos ajudam a entender e melhorar o desempenho e o design do nosso site.
    *   **Exemplo**: `_ga` (Google Analytics - coleta dados anonimizados sobre o uso do site), `_gid` (Google Analytics - distingue usuários).
    *   **Provedor**: Google LLC.
    *   **Expiração**: `_ga` (2 anos), `_gid` (24 horas).

3.  **Cookies de Funcionalidade**: Estes cookies permitem que o site se lembre de suas escolhas (como nome de usuário, idioma ou região) e ofereça funcionalidades aprimoradas e mais personalizadas. Eles podem ser definidos por nós ou por provedores terceiros cujos serviços adicionamos às nossas páginas.
    *   **Exemplo**: `__cfduid` (Cloudflare - identifica dispositivos confiáveis para segurança), `lang` (armazena a preferência de idioma).
    *   **Provedor**: Cloudflare Inc., MinhaEmpresa.
    *   **Expiração**: `__cfduid` (30 dias), `lang` (1 ano).

4.  **Cookies de Publicidade e Marketing**: Estes cookies são usados para fornecer anúncios mais relevantes para você e seus interesses. Eles também são usados para limitar o número de vezes que você vê um anúncio, bem como ajudar a medir a eficácia de uma campanha publicitária. Eles geralmente são colocados por redes de publicidade com a nossa permissão.
    *   **Exemplo**: `_fbp` (Facebook Pixel - rastreia interações para publicidade no Facebook), `_gcl_au` (Google Ads - mede a eficácia de anúncios).
    *   **Provedor**: Facebook Ireland Ltd., Google LLC.
    *   **Expiração**: `_fbp` (3 meses), `_gcl_au` (90 dias).
```

### Cláusula de Gestão de Consentimento

```markdown
**Como Gerenciar Suas Preferências de Cookies**

Você tem o direito de decidir se aceita ou rejeita cookies. Para exercer esse direito, você pode:

1.  **Através do Nosso Banner de Consentimento**: Ao acessar nosso site pela primeira vez, um banner de consentimento será exibido. Você pode:
    *   Clicar em "Aceitar Todos" para permitir o uso de todos os cookies.
    *   Clicar em "Rejeitar Não Essenciais" para desativar cookies que não são estritamente necessários para o funcionamento do site.
    *   Clicar em "Gerenciar Preferências" para personalizar suas escolhas, ativando ou desativando categorias específicas de cookies (ex: apenas cookies de análise).
    Você pode rever e alterar suas preferências a qualquer momento clicando no ícone de "Configurações de Cookies" (geralmente um ícone de cookie ou escudo de privacidade) localizado no rodapé ou lateral do nosso site.

2.  **Através das Configurações do Seu Navegador**: A maioria dos navegadores de internet permite controlar cookies através de suas configurações. Você pode configurar seu navegador para:
    *   Recusar todos os cookies.
    *   Aceitar apenas certos tipos de cookies.
    *   Notificá-lo quando um cookie for enviado.
    Para mais informações sobre como gerenciar cookies no seu navegador, consulte os links abaixo:
    *   [Chrome](https://support.google.com/chrome/answer/95647)
    *   [Firefox](https://support.mozilla.org/pt-BR/kb/gerencie-cookies-configuracoes-privacidade-seguranca)
    *   [Safari](https://support.apple.com/pt-br/guide/safari/sfri11471/mac)
    *   [Edge](https://support.microsoft.com/pt-br/windows/excluir-e-gerenciar-cookies-168dab11-0753-043d-7c16-ede5947fc64d)

Lembre-se que a desativação de certos cookies pode impactar a funcionalidade e a experiência de uso do nosso site.
```

---

## Checklist

-   [x] Mapeamento completo de todos os cookies e tecnologias de rastreamento (próprios e de terceiros).
-   [x] Classificação dos cookies por categoria (necessários, funcionais, analíticos, marketing).
-   [x] Identificação da base legal para cada tipo de cookie, conforme LGPD/GDPR.
-   [x] Texto da política claro, conciso e acessível, em português brasileiro.
-   [x] Informações sobre o controlador de dados e DPO (se aplicável) na política.
-   [x] Instruções claras sobre como o usuário pode gerenciar suas preferências de cookies.
-   [x] Implementação de um banner de consentimento (CMP) com opção de "Aceitar Todos", "Rejeitar Não Essenciais" e "Gerenciar Preferências".
-   [x] Bloqueio de cookies não essenciais antes do consentimento explícito do usuário (pré-consentimento).
-   [x] Registro e prova do consentimento dos usuários (data, hora, preferências).
-   [x] Período de retenção dos dados dos cookies e do consentimento claramente definido.
-   [x] Mecanismo para o usuário revogar ou alterar o consentimento a qualquer momento.
-   [x] Processo de atualização regular da política e re-mapeamento de cookies documentado.

---

## Métricas de Referência

| Métrica                                | Benchmark Global (Médio) | Meta para Conformidade/Otimização |
| :------------------------------------- | :----------------------- | :-------------------------------- |
| Taxa de Aceitação de Cookies (Geral)   | 70-85%                   | > 80%                             |
| Taxa de Rejeição de Cookies (Marketing)| 10-25%                   | < 15% (com consentimento explícito)|
| Tempo de Carregamento da Página (Pós-CMP) | < 2 segundos             | < 1.5 segundos                    |
| Conformidade com LGPD/GDPR (Auditoria) | 90-95%                   | 98-100%                           |
| Taxa de Revogação de Consentimento     | 2-5%                     | < 3%                              |
| Frequência de Re-mapeamento de Cookies | Trimestral               | Mensal para sites dinâmicos       |

---

## Erros Comuns

1.  **Não mapear todos os cookies**: Deixar de fora cookies de terceiros inseridos por plugins ou scripts externos, levando a lacunas na política e no controle de consentimento.
    *   **Como evitar**: Utilize ferramentas de varredura de cookies com frequência e inspecione manualmente as requisições de rede do navegador em diferentes páginas do site.
2.  **Pré-ativar cookies não essenciais**: Carregar cookies de análise, funcionalidade ou marketing antes que o usuário conceda seu consentimento explícito, violando LGPD/GDPR.
    *   **Como evitar**: Configure o CMP para implementar o bloqueio pré-consentimento (prioritário) e teste em ambiente de produção para garantir que nenhum script de rastreamento seja executado antes da interação do usuário com o banner.
3.  **Linguagem jurídica complexa e genérica**: Utilizar termos excessivamente técnicos ou descrições vagas que dificultam a compreensão do usuário sobre o uso de seus dados.
    *   **Como evitar**: Simplifique a linguagem, use exemplos concretos de cookies e suas finalidades, e evite jargões. A política deve ser compreensível para um leigo.
4.  **Não registrar o consentimento de forma auditável**: Falhar em manter um registro detalhado e prova do consentimento concedido por cada usuário (data, hora, IP, preferências).
    *   **Como evitar**: Utilize um CMP que armazene logs de consentimento com carimbo de tempo, ID de usuário (anonimizado, se possível) e as escolhas específicas do usuário, facilitando a comprovação em caso de auditoria.
5.  **Não oferecer opção "Rejeitar Todos" de forma clara**: Dificultar ou omitir a opção de o usuário rejeitar todos os cookies não essenciais no primeiro nível do banner de consentimento.
    *   **Como evitar**: Garanta que o botão "Rejeitar Não Essenciais" ou "Rejeitar Todos" tenha a mesma proeminência visual que o botão "Aceitar Todos" no banner inicial, conforme diretrizes da ANPD e EDPB.

---

## Dicas Avançadas

1.  **Auditoria Automatizada Regular e Integrada**: Configure ferramentas de varredura de cookies (ex: Cookiebot, OneTrust) para rodar automaticamente em intervalos regulares (ex: semanalmente) e enviar alertas sobre novos cookies ou mudanças. Integre esses alertas com sistemas de gerenciamento de tarefas para a equipe de privacidade.
2.  **A/B Testing do Banner de Consentimento**: Experimente diferentes designs, textos, posições e opções no banner de consentimento para otimizar as taxas de opt-in para cookies analíticos e de marketing, sem comprometer a conformidade. Por exemplo, teste um banner na parte inferior versus um pop-up central.
3.  **Integração da Política de Cookies com a Política de Privacidade Geral**: Garanta que a política de cookies seja um anexo ou uma seção clara da política de privacidade principal, mantendo a consistência nas informações sobre tratamento de dados e direitos do titular. Evite duplicações desnecessárias, mas garanta referências cruzadas.
4.  **Segmentação Geográfica para Legislação Específica**: Se o site atende a usuários de diferentes jurisdições (Brasil, UE, Califórnia), utilize um CMP que possa adaptar o texto da política, o design do banner e as categorias de cookies exibidas com base na geolocalização do usuário, garantindo conformidade com LGPD, GDPR, CCPA, etc.
5.  **Explicar o Impacto da Rejeição com Clareza e Objetividade**: Ao invés de apenas informar que "a funcionalidade pode ser afetada", detalhe quais funcionalidades específicas serão limitadas ao rejeitar certas categorias de cookies. Por exemplo, "Ao rejeitar cookies de funcionalidade, suas preferências de idioma não serão salvas e você precisará selecioná-las a cada visita."