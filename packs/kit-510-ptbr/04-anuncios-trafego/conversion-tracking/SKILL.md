---
name: conversion-tracking
description: "Conversion Tracking — Skill especializada para configurar, validar e otimizar o rastreamento de conversões em plataformas de anúncios como Meta Ads, Google Ads e TikTok Ads."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Conversion Tracking

Esta skill habilita o Claude a configurar, validar e solucionar problemas de rastreamento de conversões em Meta Ads, Google Ads e TikTok Ads para otimizar campanhas de performance e maximizar o retorno sobre o investimento em publicidade.

---

## Keywords

Pixel Meta, Tag Google Ads, API de Conversões, GTM Server-Side, Eventos Personalizados, Google Analytics 4, Metas Google Ads, TikTok Pixel, Deduplicação de Eventos, Atribuição de Conversões, ROAS, Custo por Aquisição (CPA), Eventos Padrão, Enhanced Conversions.

---

## Quick Start

1.  **Instalar o Google Tag Manager (GTM)**: Inserir os snippets do GTM no `<head>` e `<body>` de todas as páginas do site imediatamente após a abertura das tags.
2.  **Configurar Pixels/Tags Base**: Adicionar o Pixel Meta Ads e a Tag Google Ads (ID de configuração GA4 ou Tag Google) no GTM com disparador `All Pages`.
3.  **Implementar Eventos de Conversão Essenciais**: Configurar eventos como `Purchase`, `Lead` ou `AddToCart` no GTM, utilizando variáveis de Data Layer para capturar valores dinâmicos como `value` e `currency`.
4.  **Testar e Validar Eventos**: Utilizar o Meta Pixel Helper, Google Tag Assistant e a ferramenta "Testar Eventos" do Gerenciador de Eventos do Facebook para verificar o disparo correto e a recepção dos dados.
5.  **Ativar a API de Conversões (CAPI) Meta Ads**: Integrar a CAPI via GTM Server-Side ou diretamente no backend, garantindo a deduplicação de eventos com o mesmo `event_id` do Pixel do navegador.

---

## Core Workflows

### Workflow 1: Implementação e Validação de Evento de Compra para E-commerce (Meta Ads & Google Ads via GTM)

Este workflow detalha a configuração de um evento de compra robusto, essencial para e-commerce, utilizando o Google Tag Manager para Meta Ads e Google Ads.

1.  **Preparar o Google Tag Manager (GTM)**:
    *   Assegurar que o snippet do GTM esteja instalado corretamente no `head` e `body` de *todas* as páginas do site.
    *   Verificar se o Data Layer está ativo e pronto para receber dados de e-commerce na página de confirmação de compra.

2.  **Configurar o Pixel Base do Meta Ads no GTM**:
    *   No GTM, criar uma nova Tag do tipo `Meta Pixel`.
    *   Inserir o ID do seu Pixel Meta (Ex: `123456789012345`).
    *   Definir o Evento Padrão como `PageView`.
    *   Configurar o Disparador: `Initialization - All Pages` ou `Consent Initialization - All Pages` (se houver gerenciamento de consentimento).

3.  **Configurar a Tag Google Ads Base (ou GA4) no GTM**:
    *   No GTM, criar uma nova Tag do tipo `Google Tag` (ID de configuração GA4 ou Google Ads).
    *   Inserir o ID da sua Tag Google (Ex: `G-ABCDEFG123` para GA4 ou `AW-123456789` para Google Ads).
    *   Configurar o Disparador: `Initialization - All Pages`.

4.  **Configurar o Evento de Compra (`Purchase`) para Meta Ads via GTM**:
    *   No GTM, criar uma nova Tag do tipo `Meta Pixel`.
    *   Inserir o mesmo ID do Pixel Meta (`123456789012345`).
    *   Definir o Evento Padrão: `Purchase`.
    *   **Configurar Parâmetros Personalizados:**
        *   `value`: Criar uma variável de Data Layer (Ex: `ecommerce.purchase.value`) que capture o valor total da compra.
        *   `currency`: Criar uma variável de Data Layer (Ex: `ecommerce.purchase.currency`) que capture a moeda da transação (Ex: `BRL`).
        *   `content_ids`: Variável de Data Layer para IDs dos produtos (Ex: `ecommerce.purchase.items.map(item => item.item_id)`).
        *   `content_type`: `product`.
    *   **Configurar o Disparador:** Criar um Disparador de `Evento Personalizado` com o Nome do Evento `purchase` (Este evento deve ser enviado ao Data Layer na página de confirmação de compra, Ex: `dataLayer.push({event: 'purchase', ...})`).

5.  **Configurar o Evento de Compra para Google Ads via GTM (Conversão Específica)**:
    *   No GTM, criar uma nova Tag do tipo `Google Ads Conversion Tracking`.
    *   Inserir o ID da Conversão do Google Ads (Ex: `AW-123456789`).
    *   Inserir o Rótulo da Conversão (Label) do Google Ads (Ex: `AbCdEfGhIjkLmnOpQrStUv`).
    *   **Configurar Valor da Conversão**:
        *   Selecionar `Usar um valor diferente para cada conversão`.
        *   Campo `Valor`: Utilizar a mesma variável de Data Layer `ecommerce.purchase.value`.
        *   Campo `Moeda`: Utilizar a mesma variável de Data Layer `ecommerce.purchase.currency`.
    *   **Configurar o Disparador:** Usar o mesmo Disparador de `Evento Personalizado` `purchase` criado anteriormente.

6.  **Publicar as Alterações no GTM**: Enviar as alterações do contêiner GTM para o ambiente de produção.

7.  **Testar e Validar os Eventos**:
    *   Abrir o site no modo de `Visualização` do GTM.
    *   Simular uma compra completa.
    *   Verificar no console de depuração do GTM se as Tags `Meta Pixel - Purchase` e `Google Ads Conversion Tracking` dispararam no evento `purchase` com os parâmetros corretos.
    *   Utilizar o **Meta Pixel Helper** (extensão Chrome) para verificar os eventos do Meta Ads.
    *   Utilizar o **Google Tag Assistant** (extensão Chrome) para verificar os eventos do Google Ads.
    *   No **Gerenciador de Eventos do Facebook**, acessar a seção "Testar Eventos" e verificar a recepção do evento `Purchase`.
    *   No **Google Ads**, verificar a seção "Diagnóstico de Tags" ou "Resumo de Conversões" para confirmar a recepção.

### Workflow 2: Implementação da API de Conversões do Meta (CAPI) para Deduplicação e Resiliência

Este workflow foca na implementação da API de Conversões do Meta (CAPI) para garantir um rastreamento mais preciso e resiliente, complementando o Pixel do navegador e prevenindo perdas de dados.

1.  **Compreender a CAPI e a Deduplicação**:
    *   A CAPI permite enviar eventos de conversão diretamente do servidor para o Meta, contornando bloqueadores de anúncios e problemas de carregamento de navegador.
    *   Para evitar contagens duplicadas, é crucial enviar um `event_id` *idêntico* para o mesmo evento de conversão, tanto do Pixel do navegador quanto da CAPI. O Meta Ads Manager fará a deduplicação automaticamente com base neste ID.

2.  **Escolher o Método de Implementação**:
    *   **GTM Server-Side**: Recomendado para a maioria dos casos, pois centraliza o controle e permite transformar dados antes de enviá-los.
    *   **Integração Direta no Backend**: Requer desenvolvimento e manutenção por uma equipe de engenharia.

3.  **Configuração via GTM Server-Side (Exemplo para Evento de Compra)**:
    *   **Criar um Contêiner Server-Side no GTM**: Na interface do GTM, criar um novo contêiner do tipo `Server`.
    *   **Prover um Servidor de Tag**: Configurar um servidor de tag (Ex: Google Cloud Run, App Engine) e vincular ao contêiner Server-Side do GTM.
    *   **Enviar Dados do Navegador para o Contêiner Server-Side**:
        *   Modificar a Tag Google Ads (ou GA4) no GTM Client-Side para enviar dados para o seu novo servidor de tag. No `Google Tag` (Tag de configuração GA4), adicione o parâmetro `server_container_url` com o URL do seu servidor de tag (Ex: `https://gtm.seusite.com`).
        *   Para eventos do Meta Pixel, você pode usar uma Tag HTML Personalizada no GTM Client-Side para enviar os dados para o servidor de tag via um endpoint personalizado, ou confiar que a Tag Google já está enviando os dados necessários que serão interceptados no servidor.

    *   **No Contêiner Server-Side do GTM**:
        *   **Cliente**: Configurar um `Cliente` (Ex: `GA4` ou `Universal Analytics`) para receber os dados enviados do navegador.
        *   **Tag da API de Conversões do Facebook**:
            *   Criar uma nova Tag do tipo `Facebook Conversions API` (disponível na Galeria de Templates da Comunidade).
            *   Inserir o ID do seu Pixel Meta (`123456789012345`) e o Token de Acesso da API de Conversões (gerado no Gerenciador de Eventos do Facebook > Configurações > API de Conversões).
            *   **Mapear Parâmetros de Evento**:
                *   `Event Name`: Mapear para o nome do evento recebido (Ex: `{{Event Name}}` do cliente GA4).
                *   `Event Time`: `{{Event Time}}`.
                *   `Event ID`: **CRUCIAL para Deduplicação**. Este deve ser o mesmo `event_id` gerado e enviado pelo Pixel do navegador. Geralmente, você precisará capturar o `_fbc` e `_fbp` do navegador e usar uma variável para gerar um `event_id` consistente ou passá-lo explicitamente via Data Layer. Uma forma comum é usar um `event_id` que seja uma combinação do `transaction_id` com um timestamp ou um GUID gerado no navegador e passado para o servidor.
                *   `User Data`: Mapear dados de usuário (email com hash SHA256, telefone, `fbp`, `fbc`). Ex: `user_data.em` (email com hash), `user_data.ph` (telefone com hash), `user_data.fbp` (variável `_fbp` do cookie do navegador), `user_data.fbc` (variável `_fbc` do cookie do navegador).
                *   `Custom Data`: Mapear `value` e `currency` do evento de compra (Ex: `custom_data.value`, `custom_data.currency`).

    *   **Configurar o Disparador no Server-Side**: Criar um disparador para a Tag da CAPI que reaja aos eventos que você quer enviar (Ex: `Custom Event` com `event_name` `purchase`).

4.  **Teste e Validação da Deduplicação**:
    *   Após publicar as alterações no GTM Client-Side e Server-Side, simule uma compra.
    *   No **Gerenciador de Eventos do Facebook**, vá para a seção "Testar Eventos".
    *   Você deve ver os eventos `Purchase` chegando duas vezes (um do navegador e um da API de Conversões), mas o status deve ser "Deduplicado" para um deles. Isso confirma que a CAPI está funcionando e que o `event_id` está correto.

---

## Templates

### Evento de Compra Data Layer (Exemplo E-commerce)

Este é um exemplo de como o `dataLayer.push` deve ser formatado na página de confirmação de compra para enviar dados detalhados da transação, que serão capturados pelo GTM.

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "ORDEM-123456789", // ID único da transação
    value: 149.90, // Valor total da compra
    currency: "BRL", // Moeda da transação
    shipping: 15.00, // Custo de frete
    tax: 0.00, // Impostos
    coupon: "DESCONTO10", // Código do cupom, se houver
    items: [
      {
        item_id: "PROD-SKU001",
        item_name: "Camiseta Algodão Premium",
        item_category: "Vestuário",
        item_variant: "Azul Marinho - G",
        price: 99.90,
        quantity: 1
      },
      {
        item_id: "PROD-SKU002",
        item_name: "Boné Esportivo Ajustável",
        item_category: "Acessórios",
        item_variant: "Preto",
        price: 50.00,
        quantity: 1
      }
    ]
  },
  // Opcional: Dados do usuário para Enhanced Conversions (Google Ads) ou CAPI (Meta Ads)
  user_data: {
    email: "usuario@email.com", // Enviar email com hash SHA256 para produção
    phone_number: "+5511987654321" // Enviar telefone com hash SHA256 para produção
  }
});
```

### Configuração de Conversão Google Ads (Interface)

Este template reflete as configurações típicas ao criar uma nova ação de conversão manualmente na interface do Google Ads para um evento de `Lead` ou `Compra`.

```
Nome da Conversão: Lead - Contato Comercial
Categoria: Lead
Valor: Usar o mesmo valor para cada conversão (R$ 50,00)
Contagem: Uma (recomendado para leads)
Janela de Conversão (clique): 30 dias
Janela de Conversão (visualização engajada): 3 dias
Janela de Conversão (visualização): 1 dia
Modelo de Atribuição: Baseada em dados (recomendado)
Incluir em "Conversões": Sim
```

---

## Checklist

-   [x] Pixel Meta Ads (Base `PageView`) instalado via GTM em todas as páginas.
-   [x] Tag Google Ads (Base `config` ou GA4) instalada via GTM em todas as páginas.
-   [x] Eventos de conversão primários (Ex: `Purchase`, `Lead`, `CompleteRegistration`) configurados no GTM com parâmetros dinâmicos (`value`, `currency`, `content_ids`).
-   [x] Eventos padrão Meta e Metas Google Ads criados e mapeados para os eventos do GTM.
-   [x] API de Conversões (CAPI) Meta Ads implementada (GTM Server-Side ou backend) para deduplicação.
-   [x] `event_id` configurado e validado para garantir a deduplicação correta entre Pixel e CAPI.
-   [x] Google Analytics 4 configurado para receber eventos de e-commerce e leads para análise.
-   [x] Teste completo de eventos realizado com Meta Pixel Helper, Google Tag Assistant e ferramenta "Testar Eventos" do Gerenciador de Eventos.
-   [x] Diagnóstico de tags/pixels sem erros críticos ou avisos nas plataformas de anúncios.
-   [x] Configurações de janela de atribuição revisadas e alinhadas com o ciclo de vendas (ex: 7 dias clique, 1 dia view).
-   [x] Implementação de Enhanced Conversions (Google Ads) para melhorar a precisão do rastreamento.
-   [x] Priorização de eventos no TikTok Ads configurada para otimização de campanha.

---

## Métricas de Referência

| Métrica               | Benchmark (E-commerce) | Benchmark (Geração de Leads) |
|-----------------------|------------------------|------------------------------|
| ROAS (Retorno sobre Anúncios) | 3.0x - 5.0x            | N/A                          |
| CPA (Custo por Aquisição) | R$ 30 - R$ 150         | R$ 15 - R$ 50                |
| Taxa de Conversão (TC) | 1.0% - 3.0%            | 5.0% - 15.0%                 |
| CTR (Taxa de Cliques) | 1.5% - 3.5%            | 0.8% - 2.0%                  |
| CPC (Custo por Clique) | R$ 0.80 - R$ 2.50      | R$ 1.50 - R$ 4.00            |
| Frequência (Meta Ads) | 1.8 - 3.5              | 1.5 - 2.5                    |

---

## Erros Comuns

1.  **Deduplicação Falha na API de Conversões**: O `event_id` enviado via CAPI não corresponde ao `event_id` gerado pelo Pixel no navegador para o mesmo evento. Isso resulta em conversões duplicadas no Gerenciador de Eventos.
    *   **Como evitar**: Garanta que o `event_id` seja gerado de forma consistente e única para cada evento de conversão e que seja passado *exatamente* o mesmo ID tanto para o Pixel do navegador (via Data Layer ou variável GTM) quanto para a chamada da CAPI (seja via GTM Server-Side ou integração direta). Ex: Ao invés de gerar um novo GUID no servidor, use o `_fbc` ou o `transaction_id` com um timestamp como base para um `event_id` consistente.

2.  **Eventos Sem Parâmetros Dinâmicos Essenciais**: Eventos de `Purchase` ou `Lead` são disparados, mas faltam parâmetros cruciais como `value`, `currency` ou `content_ids`. Isso impede a otimização baseada em valor e a criação de públicos dinâmicos.
    *   **Como evitar**: Sempre configure os eventos de conversão no GTM para capturar e enviar todos os parâmetros relevantes do Data Layer. Para `Purchase`, `value` e `currency` são obrigatórios. Para `Lead`, mesmo que seja um valor fixo, atribua um para permitir a otimização por valor. Ex: Um evento de `Lead` pode ter `value: 25.00, currency: "BRL"`.

3.  **Conflito ou Disparo Incorreto de Pixels/Tags**: Múltiplos pixels ou tags de conversão do mesmo tipo disparam na mesma página ou um evento é disparado em um local incorreto (Ex: `Purchase` disparando em `AddToCart`). Isso causa dados inflacionados e otimização errônea.
    *   **Como evitar**: Utilize o GTM para centralizar e controlar o disparo das tags. Crie disparadores altamente específicos para cada evento. Revise as condições dos disparadores (`Page Path`, `Event Name`, `URL`) para garantir que cada tag dispare apenas quando e onde deve. Ex: O disparador para `Purchase` deve ser `Page Path` contém `/confirmacao-compra` E `Event` é `purchase`.

---

## Dicas Avançadas

1.  **Otimização por Valor de Conversão (OVV)**: Para e-commerce, configure as campanhas para otimizar por valor de conversão (ROAS). Garanta que seus eventos de `Purchase` enviem o `value` e `currency` corretos. Isso permite que as plataformas de anúncios busquem usuários com maior propensão a gastar mais, não apenas a converter. Ex: Em Meta Ads, selecione "Valor" como seu objetivo de otimização para campanhas de vendas.

2.  **Rastreamento Cross-Domain/Subdomínio com GTM e GA4**: Se seu funil de conversão abrange múltiplos domínios (Ex: loja.com e checkout.meupagamento.com) ou subdomínios (Ex: blog.site.com e loja.site.com), configure o GTM para permitir que o mesmo pixel/tag rastreie o usuário de forma contínua. Para GA4, configure `cookie_domain: auto` e `linker.domains: ['loja.com', 'checkout.meupagamento.com']` no seu `Google Tag`.

3.  **Implementação de User-Provided Data (UPD) / Enhanced Conversions (Google Ads)**: Para melhorar a precisão do rastreamento de conversões, envie dados de clientes com hash (email, telefone, nome) para o Google Ads. Isso ajuda a associar conversões mesmo em cenários com restrições de cookies. Configure no GTM para coletar esses dados do Data Layer ou de campos do formulário no momento da conversão e enviá-los junto com o evento.

4.  **Eventos Personalizados e Micro-Conversões (Meta Ads)**: Além dos eventos padrão, crie eventos personalizados para interações chave que indicam alto interesse, mas não são uma conversão final. Ex: `ScrollProfundo` (para quem rola 75% da página de produto), `VisualizacaoVideoProduto` (para quem assiste 75% de um vídeo). Use esses eventos para construir públicos de remarketing altamente qualificados ou para otimizar campanhas de topo de funil.

5.  **Testes A/B de Configurações de Atribuição**: Experimente diferentes janelas de atribuição (ex: 7 dias clique vs. 1 dia clique)