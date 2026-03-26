---
name: app-install-campaign
description: "App Install Campaign — Skill especializada para app install campaign"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# App Install Campaign

Esta skill capacita o Claude a planejar, executar e otimizar campanhas de instalação de aplicativos em Meta Ads, Google Ads e TikTok Ads, focando em resultados de aquisição e retenção de usuários.

---

## Keywords

Campanha de Instalação de App, UAC (Universal App Campaigns), GAC (Google App Campaigns), Meta App Ads, TikTok App Install, Mobile Measurement Partner (MMP), Deep Linking, SKAdNetwork, CPI (Custo Por Instalação), ROAS (Retorno sobre Anúncios), Eventos Pós-Instalação, Otimização de Lances, Atribuição de Mobile, ASO (App Store Optimization).

---

## Quick Start

1.  **Configurar MMP e SDKs**: Instalar e configurar um Mobile Measurement Partner (MMP) como AppsFlyer, Adjust ou Branch, garantindo que o SDK esteja integrado ao aplicativo e enviando eventos de `App Install` e `App Open` (mínimo) para as plataformas de anúncios.
2.  **Criar Campanha Meta Ads**: Lançar uma campanha no Gerenciador de Anúncios do Meta com o objetivo `Instalações do Aplicativo`, utilizando criativos de vídeo e imagens verticais.
3.  **Lançar Google App Campaign (GAC)**: Configurar uma Google App Campaign focada em `Instalações de aplicativo`, fornecendo o máximo de ativos de texto, imagem e vídeo.
4.  **Monitoramento Inicial**: Acompanhar o Custo por Instalação (CPI) e o volume de instalações nas primeiras 48-72 horas pós-lançamento, ajustando orçamentos se o volume estiver abaixo do esperado ou o CPI acima do alvo.

---

## Core Workflows

### Workflow 1: Lançamento e Otimização de Campanha de App Install no Meta Ads

Este workflow detalha a criação e otimização de uma campanha no Meta Ads com foco em instalações e eventos pós-instalação.

1.  **Verificação da Fonte de Dados e SDK**:
    *   **Ação**: Confirmar que o SDK do Facebook (ou integração via MMP) está implementado e enviando os eventos de conversão de aplicativo para o Gerenciador de Eventos.
    *   **Exemplo**: Acessar o Gerenciador de Eventos > Fontes de Dados > SDK do App. Verificar se os eventos `fb_mobile_activate_app` (instalação), `fb_mobile_app_open` (primeira abertura) e, se aplicável, eventos de valor como `fb_mobile_purchase` ou `fb_mobile_complete_registration` estão sendo recebidos ativamente.
    *   **Importância**: Sem dados precisos, a otimização da campanha será comprometida.
2.  **Estrutura da Campanha no Gerenciador de Anúncios**:
    *   **Criação**: Iniciar uma nova campanha.
    *   **Objetivo**: Selecionar `Instalações do aplicativo` para a fase inicial de aquisição ou `Eventos do aplicativo` se o objetivo primário for otimizar para ações de valor dentro do app (ex: compra, registro).
    *   **Orçamento**: Definir um orçamento diário ou total.
        *   **Exemplo**: Orçamento diário de R$ 350,00.
    *   **Conjunto de Anúncios - Otimização de Entrega**:
        *   Para `Instalações do aplicativo`: Manter a otimização para `Instalações do aplicativo`.
        *   Para `Eventos do aplicativo`: Escolher o evento de maior valor (ex: `Completar Registro`, `Compra no Aplicativo`).
    *   **Conjunto de Anúncios - Público-Alvo**:
        *   **Ação**: Criar públicos específicos para maximizar a aquisição de usuários qualificados.
        *   **Exemplo**:
            *   `Lookalike 1% de Compradores Recentes (últimos 30 dias)`: Utiliza uma lista de clientes que realizaram compras no app.
            *   `Interesses`: Segmentar por interesses em `Aplicativos de [Categoria do App]`, `Concorrentes Diretos`, ou `Tecnologia Mobile`.
            *   `Público Amplo`: Para apps com grande volume de dados, testar um público sem segmentação detalhada (idade, gênero, localização) e deixar o algoritmo do Meta encontrar os usuários mais propensos a instalar.
    *   **Conjunto de Anúncios - Posicionamentos**:
        *   **Recomendação**: Utilizar `Posicionamentos Advantage+` (automáticos) para permitir que o algoritmo distribua os anúncios onde há maior probabilidade de conversão.
    *   **Anúncios - Criativos e Chamada para Ação (CTA)**:
        *   **Ação**: Desenvolver criativos que demonstrem claramente o valor do aplicativo.
        *   **Exemplo**: Vídeos curtos (15-30 segundos) mostrando a interface do app em uso, carrosséis com os principais recursos, e imagens estáticas de alta qualidade.
        *   **CTA**: Usar `Instalar Agora`, `Baixar App` ou `Abrir App` (para reengajamento).
3.  **Monitoramento e Otimização Contínua**:
    *   **Ação**: Acompanhar métricas chave e realizar ajustes.
    *   **Exemplo**: Se o CPI estiver alto, testar novos criativos ou refinar o público. Se o ROAS D7 (7 dias pós-instalação) estiver baixo, ajustar a otimização para um evento de valor maior ou reduzir o lance máximo. Verificar relatórios de criativos para pausar os de baixo desempenho e escalar os campeões.

### Workflow 2: Otimização de Google App Campaigns (GAC) para ROAS e Eventos Pós-Instalação

Este workflow foca em como configurar e otimizar campanhas de aplicativo no Google Ads para maximizar o retorno sobre o investimento em publicidade.

1.  **Integração Google Analytics 4 (GA4) e Eventos de Conversão**:
    *   **Ação**: Assegurar que o Google Analytics 4 esteja configurado no aplicativo e que os eventos de conversão relevantes (ex: `first_open`, `in_app_purchase`, `subscription_start`, `ad_impression`) estejam sendo enviados para o Google Ads.
    *   **Exemplo**: No Google Ads, navegar até `Ferramentas e Configurações` > `Medição` > `Conversões`. Verificar se os eventos do GA4 estão importados e marcados como "Primária" para lances.
    *   **Importância**: O GAC depende fortemente desses dados para otimização por machine learning.
2.  **Estrutura da Google App Campaign**:
    *   **Tipo de Campanha**: Selecionar `Aplicativo`.
    *   **Subtipo**:
        *   `Instalações de aplicativo`: Para maximizar o volume de instalações.
        *   `Valor da conversão no aplicativo`: Essencial para otimização de ROAS, focando em eventos de compra ou assinatura.
        *   `Engajamento com o aplicativo`: Para reativar usuários existentes ou incentivar ações em usuários ativos.
    *   **Lances e Orçamento**:
        *   **Otimização por ROAS**: Definir um `ROAS desejado` (tROAS).
            *   **Exemplo**: Orçamento diário de R$ 600,00 com tROAS de 250%.
        *   **Otimização por Evento**: Se o ROAS ainda não tiver dados suficientes, usar `CPA desejado` (tCPA) para um evento de valor intermediário (ex: `Registro Concluído`).
            *   **Exemplo**: Orçamento diário de R$ 400,00 com tCPA de R$ 15,00 para `Complete Registration`.
    *   **Ativos de Anúncio**:
        *   **Ação**: Fornecer uma ampla variedade de ativos criativos para o Google testar e otimizar.
        *   **Exemplo**:
            *   **Títulos (até 30)**: "App de [Categoria] N°1", "Descontos Exclusivos", "Gerencie suas Finanças Fácil".
            *   **Descrições (até 20)**: "Milhares de produtos, entrega rápida", "Economize tempo e dinheiro em suas compras diárias".
            *   **Imagens (até 20)**: Capturas de tela da interface do app, imagens de estilo de vida que representem o uso do app.
            *   **Vídeos (até 20)**: Demos de recursos, depoimentos, animações curtas.
3.  **Análise de Desempenho e Ajustes**:
    *   **Relatórios de Ativos**: Acompanhar o desempenho de cada ativo (títulos, descrições, imagens, vídeos) no relatório de ativos da campanha.
    *   **Ação**: Pausar ativos com classificação "Baixa" e substituí-los por novas variações.
    *   **Exemplo**: Se um título como "Baixe Grátis!" tiver baixo desempenho, testar "Comece a Economizar Hoje!".
    *   **Ajuste de Lances**: Se o tROAS não estiver sendo atingido após um período de aprendizado (geralmente 7-14 dias), ajustar o valor do tROAS para cima ou para baixo em incrementos de 10-20%.
    *   **Monitoramento de Eventos**: Verificar regularmente se os eventos de conversão estão sendo atribuídos corretamente e se o volume de eventos de pós-instalação está crescendo.

---

## Templates

### Template de Briefing para Criativos de App Install (Meta/TikTok)

```
Título da Campanha: Lançamento App [Nome do App] - Verão 2025
Objetivo Principal: Aumentar Instalações e Ativações (Primeiro Login)
Plataformas de Veiculação: Meta Ads (Facebook/Instagram), TikTok Ads
Público-Alvo: Usuários de smartphones interessados em [Categoria do App, ex: fitness, jogos casuais, finanças], 18-35 anos, Região Sudeste do Brasil.
Call-to-Action Primário: Instalar Agora / Baixar App / Comece Já
Mensagem Chave: "Transforme sua rotina com [Nome do App]! [Benefício Principal do App] está a um toque."
Elementos Visuais Obrigatórios:
  - Logo do App sempre visível (canto superior/inferior)
  - Demonstração clara da interface do App em uso (cenários reais de uso)
  - Texto na tela com o benefício principal ou uma oferta
  - Cores da marca predominantes
Elementos Opcionais:
  - Prova social (ex: "Mais de 1 milhão de downloads!")
  - Depoimentos curtos de usuários
  - Elementos de urgência (se houver promoção)
Formatos Desejados:
  - Vídeo Vertical (9:16, 15-30s)
  - Vídeo Quadrado (1:1, 10-20s)
  - Carrossel (3-5 imagens/vídeos, 1:1)
  - Imagem Estática (1:1, 9:16)
Exemplos de Copy para Anúncio:
  - Título/Cabeçalho: "[Nome do App]: Seu Personal Trainer no Bolso!"
  - Descrição/Corpo: "Alcance seus objetivos de fitness com treinos personalizados e acompanhamento diário. Instale agora e ganhe 7 dias grátis!"
  - Texto no vídeo: "Treinos em Casa. Resultados Reais."
```

### Template de URL de Rastreamento (Deep Link) para Campanha de App Install

```
Objetivo: Rastrear instalações de forma precisa e direcionar usuários para uma tela específica dentro do aplicativo após a instalação.

Exemplo de Construção de Deep Link (Usando um MMP como AppsFlyer/Adjust):

1.  **Base Link do MMP (Link Universal/OneLink)**:
    *   URL: https://[seu-subdominio-mmp].onelink.me/[ID_TEMPLATE_MMP]
    *   Exemplo: https://meuapp.onelink.me/abc12345

2.  **Parâmetros de Atribuição (Essenciais para o MMP identificar a fonte)**:
    *   `pid`: Fonte de mídia (ex: `facebook_int`, `googleadwords_int`, `tiktok_int`)
    *   `c`: Nome da campanha (ex: `bf_campanha_app_install_br`)
    *   `af_adset`: Nome do conjunto de anúncios (ex: `publico_lookalike_compradores`)
    *   `af_ad`: Nome do anúncio/criativo (ex: `video_oferta_principal_bf`)
    *   `af_channel`: Canal de mídia (ex: `facebook`, `instagram`, `tiktok`)
    *   `af_siteid`: Local de veiculação (ex: `facebook_mobile_feed`, `tiktok_for_you`)
    *   `af_c_id`: ID da campanha (Meta Ads: `{{campaign.id}}`)
    *   `af_adset_id`: ID do conjunto de anúncios (Meta Ads: `{{adset.id}}`)
    *   `af_ad_id`: ID do anúncio (Meta Ads: `{{ad.id}}`)

3.  **Parâmetros de Deep Linking (Para direcionar o usuário dentro do app)**:
    *   `af_dp`: URI Scheme do seu app e rota desejada (ex: `meuapp://home?tab=ofertas_bf`)
    *   `af_web_dp`: URL de fallback para web caso o app não esteja instalado ou o deep link falhe (ex: `https://www.meuapp.com/promocao-bf`)
    *   `deep_link_value`: Parâmetro customizado para o app processar (ex: `promocao_black_friday_2024`)

**URL Final Construída (Exemplo para Meta Ads com AppsFlyer):**
```
https://meuapp.onelink.me/abc12345?pid=facebook_int&c={{campaign.name}}&af_adset={{adset.name}}&af_ad={{ad.name}}&af_channel={{publisher_platform}}&af_siteid={{site_source_name}}&af_dp=meuapp://home?tab=ofertas_bf&af_web_dp=https://www.meuapp.com/promocao-bf&deep_link_value=promocao_black_friday_2024
```
*Note: O Meta Ads substitui `{{campaign.name}}`, etc., pelos valores reais da campanha no momento do clique.*
```

---

## Checklist

- [x] MMP (Mobile Measurement Partner) configurado e SDKs integrados (ex: Adjust, AppsFlyer, Branch).
- [x] Eventos de pós-instalação (App Open, Registro, Compra) mapeados e enviados corretamente para as plataformas de anúncios.
- [x] Deep Links configurados e testados para garantir o direcionamento correto pós-instalação para usuários novos e existentes.
- [x] Criativos (vídeos, imagens, carrosséis) otimizados para mobile (principalmente verticais) e com CTA claro e visível.
- [x] Orçamento diário ou vitalício definido com base no CPI alvo, volume desejado e LTV projetado.
- [x] Campanha Meta Ads configurada com objetivo "Instalações do Aplicativo" ou "Eventos do Aplicativo" (se houver dados suficientes).
- [x] Google App Campaign (GAC) com no mínimo 5 títulos, 5 descrições, 5 imagens e 5 vídeos carregados para maximizar o desempenho.
- [x] TikTok App Campaign configurada com objetivo "Instalações do aplicativo" e otimização por VCP (Value Cost Per Install) ou CPI.
- [x] Monitoramento diário de CPI, CVR (Taxa de Conversão de Instalação) e ROAS pós-instalação (D7, D30).
- [x] Exclusão de público de usuários existentes (se aplicável) para campanhas de aquisição de novos usuários.
- [x] Verificação da compatibilidade com SKAdNetwork para campanhas em iOS 14.5+ e mapeamento de "conversion values".
- [x] Configuração de públicos Lookalike baseados em eventos de alto valor dentro do app.

---

## Métricas de Referência

| Métrica               | Benchmark (Brasil - Varia por Categoria) | Meta (Exemplo) |
|-----------------------|------------------------------------------|----------------|
| CPI (Android)         | R$ 2,50 - R$ 9,0