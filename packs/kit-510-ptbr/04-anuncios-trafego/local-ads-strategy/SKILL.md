---
name: local-ads-strategy
description: "Local Ads Strategy — Skill especializada para local ads strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Local Ads Strategy

Esta skill capacita o Claude a desenvolver, lançar e otimizar campanhas de anúncios locais altamente direcionadas em plataformas como Meta Ads, Google Ads e TikTok Ads, maximizando o retorno sobre o investimento para negócios físicos.

---

## Keywords

Anúncios locais, Meta Ads local, Google Meu Negócio Ads, Tráfego para loja física, Geotargeting avançado, Campanhas de alcance local, Otimização de CPA local, ROAS de vendas físicas, TikTok Local Ads, Audiência de proximidade, Extensões de local Google Ads, Performance Max local.

---

## Quick Start

1.  **Otimização GMB**: Assegurar que o perfil Google Meu Negócio esteja 100% preenchido, verificado e com fotos de alta qualidade, incluindo horário de funcionamento e telefone.
2.  **Campanha Performance Max Local**: Lançar uma campanha Performance Max no Google Ads com o objetivo "Visitas à loja física e promoções locais", vinculando o GMB e adicionando extensões de local.
3.  **Campanha de Alcance Meta Ads**: Configurar uma campanha de "Tráfego para o Estabelecimento" no Meta Ads, segmentando um raio de 3-8 km ao redor do endereço físico com criativos de oferta.
4.  **Monitoramento Básico**: Habilitar o rastreamento de chamadas e solicitações de rota no Google Ads e monitorar o Custo por Visita à Loja (CPVL) no Meta Ads como métricas primárias.

---

## Core Workflows

### Workflow 1: Aquisição de Clientes Locais com Meta Ads

Este workflow foca em atrair novos clientes para um estabelecimento físico através de campanhas segmentadas no Facebook e Instagram.

1.  **Estrutura da Campanha**: Criar uma nova campanha no Gerenciador de Anúncios da Meta.
    *   **Objetivo**: Selecionar "Tráfego para o Estabelecimento" para negócios com múltiplas lojas ou "Conversões" se o pixel estiver configurado para registrar visitas à loja via dados de localização, ou se o objetivo for preenchimento de formulário de agendamento local.
    *   **Orçamento**: Iniciar com um orçamento diário de R$50-R$100 (exemplo para uma pequena empresa). Utilizar CBO (Otimização de Orçamento da Campanha) para que a Meta distribua o orçamento entre os conjuntos de anúncios com melhor performance.
2.  **Configuração do Conjunto de Anúncios**:
    *   **Localização**: Definir o raio de segmentação. Para um restaurante em um bairro movimentado, um raio de 3-5 km é ideal. Para um serviço especializado, pode-se expandir para 8-10 km, excluindo áreas de baixa densidade populacional ou irrelevantes. Exemplo: "Rua Augusta, 2000, São Paulo" com raio de 4km.
    *   **Idade e Gênero**: Ajustar conforme o perfil do cliente ideal. Ex: Salão de beleza premium -> Mulheres, 28-55 anos. Academia de bairro -> Ambos, 18-45 anos.
    *   **Segmentação Detalhada**: Adicionar interesses relevantes que complementam a segmentação geográfica, sem restringir demais. Ex: Para uma cafeteria, incluir "Café", "Padaria", "Foodie", "Pequenas empresas". Utilizar públicos personalizados de engajamento com a página do Facebook/Instagram.
    *   **Posicionamentos**: Selecionar posicionamentos manuais, priorizando Feed do Facebook, Feed do Instagram, Stories e Reels. Desativar Audience Network, Messenger para controle de qualidade.
3.  **Criação de Criativos**:
    *   **Formato**: Vídeos curtos (15-30 segundos) mostrando o ambiente, o produto ou o serviço em ação, ou imagens de alta qualidade com pessoas reais interagindo.
    *   **Conteúdo**: Destacar ofertas exclusivas para clientes locais (Ex: "Desconto 15% para quem mora no [Bairro]!"), horários especiais ou um diferencial que incentive a visita imediata. Incluir elementos visuais reconhecíveis da região.
    *   **Call-to-Action (CTA)**: "Obter Direções", "Agendar Agora", "Ligar Agora", "Saiba Mais" (direcionando para uma landing page local ou WhatsApp).
4.  **Monitoramento e Otimização**:
    *   Acompanhar o Custo por Visita à Loja (CPVL) se configurado, ou o Custo por Clique no CTA "Obter Direções".
    *   Realizar testes A/B com diferentes ofertas, criativos ou CTAs.
    *   Ajustar o raio de segmentação se a frequência estiver muito alta ou o alcance muito baixo.

### Workflow 2: Otimização de Visibilidade Local com Google Ads (Performance Max)

Este workflow visa maximizar a presença de um negócio físico nas propriedades do Google (Search, Maps, YouTube, Display, Discover, Gmail) para usuários em proximidade geográfica.

1.  **Configuração Inicial**:
    *   **Vincular GMB**: Essencial vincular o perfil Google Meu Negócio verificado à conta do Google Ads.
    *   **Objetivo de Campanha**: Criar uma nova campanha Performance Max, selecionando "Visitas à loja física e promoções locais" como objetivo principal.
    *   **Orçamento**: Definir um orçamento diário inicial de R$70-R$150, dependendo da competitividade local.
    *   **Estratégia de Lance**: Utilizar "Maximizar valor da conversão" ou "Maximizar conversões", atribuindo valores para chamadas e visitas à loja.
2.  **Configuração do Grupo de Ativos**:
    *   **Ativos de Texto**:
        *   **Títulos**: Escrever títulos cativantes que incluam o nome do negócio, o serviço/produto e a localização. Ex: "Hamburgueria Artesanal em Pinheiros", "Melhor Salão de Beleza na Vila Olímpia", "Entregas Rápidas em Santana".
        *   **Descrições**: Detalhar diferenciais locais, promoções e benefícios. Ex: "Prove o melhor burger com pão brioche feito na casa. Perto da estação Faria Lima.", "Equipe especializada e ambiente exclusivo. Agende seu horário!".
    *   **Ativos de Imagem e Vídeo**:
        *   **Imagens**: Upload de 5-10 imagens de alta resolução do exterior e interior do estabelecimento, produtos, equipe e clientes. Imagens com dimensões 1200x628 e 1200x1200 são cruciais.
        *   **Vídeos**: Incluir pelo menos um vídeo de 15-30 segundos mostrando o ambiente, depoimentos de clientes ou o processo de um serviço.
    *   **Sinais de Público**: Fornecer ao Google informações sobre o público-alvo para guiar a IA.
        *   **Listas de Clientes**: Fazer upload de listas de clientes existentes (e-mails, telefones) para que o Google encontre perfis semelhantes.
        *   **Interesses**: Adicionar interesses e dados demográficos relevantes. Ex: "Comida japonesa", "Spa", "Serviços automotivos".
3.  **Extensões de Anúncios**:
    *   **Extensões de Localização**: Certificar-se de que estão ativas e vinculadas ao GMB.
    *   **Extensões de Chamada**: Permitir que os usuários liguem diretamente para o negócio.
    *   **Extensões de Frase de Destaque**: Adicionar frases como "Atendimento Premium", "Estacionamento Gratuito", "Wi-Fi Disponível".
4.  **Monitoramento e Otimização**:
    *   Acompanhar métricas como o número de chamadas diretas, solicitações de rota, cliques no site e visitas à loja (se configurado).
    *   Analisar os relatórios de "Insights" da Performance Max para entender quais ativos e canais estão gerando os melhores resultados.
    *   Ajustar o orçamento e os valores das conversões conforme a performance.

---

## Templates

### Template de Anúncio Meta Ads para Oferta Local

```
Título: [Nome da Loja] - Sua Oferta Exclusiva em [Bairro/Cidade]!
Texto Principal: Não perca! [Produto/Serviço] com [Desconto/Benefício] *apenas para clientes locais*. Válido até [Data]. Visite-nos em [Endereço] ou clique para saber mais!
Descrição do Link: [Breve detalhe da oferta e localização]
Call-to-Action: Obter Direções / Agendar Agora / Ligar Agora / Saiba Mais
URL de Destino: [Link para WhatsApp/Landing Page Local/Perfil Google Meu Negócio]

Exemplo Preenchido:
Título: Padaria Delícia - Seu Café da Manhã Fresquinho na Vila Mariana!
Texto Principal: Acabou de sair do forno! Pão de queijo quentinho + café coado por R$9,90 *exclusivo para vizinhos da Vila Mariana*. Válido até 30/06. Venha nos visitar na Rua Vergueiro, 1234!
Descrição do Link: Café da manhã completo na Vila Mariana!
Call-to-Action: Obter Direções
URL de Destino: https://g.page/padariadelicia?share
```

### Template de Ativos de Texto para Google Ads Performance Max (Segmento Local)

```
Títulos (Mínimo 5, ideal 15):
1. [Serviço/Produto] em [Cidade/Bairro]
2. A [Sua Empresa] é [Diferencial Local]
3. Melhor [Serviço/Produto] Perto de Você
4. Oferta Exclusiva para [Cidade/Bairro]
5. Visite Nosso [Tipo de Negócio] em [Endereço Breve]

Descrições (Mínimo 3, ideal 5):
1. [Diferencial 1] + [Diferencial 2]. Venha nos conhecer em [Bairro/Cidade]!
2. Experiência [Adjetivo] garantida. Estamos esperando você!
3. Localização privilegiada e atendimento personalizado.
4. Descontos especiais para a comunidade de [Bairro/Cidade].

Exemplo Preenchido:
Títulos:
1. Manicure e Pedicure em Moema
2. O Salão Luxo Moema é Referência em Unhas
3. Melhor Esmalteria Perto de Você
4. Desconto de 15% para Moradores de Moema
5. Salão Luxo Moema na Av. Ibirapuera, 2000

Descrições:
1. Unhas impecáveis e ambiente relaxante. Venha nos conhecer em Moema!
2. Experiência de beleza garantida com produtos premium. Estamos esperando você!
3. Localização privilegiada ao lado do Shopping Ibirapuera e atendimento personalizado.
4. Descontos especiais de terça a quinta para a comunidade de Moema.
```

---

## Checklist

-   [ ] Perfil Google Meu Negócio (GMB) completamente preenchido e verificado.
-   [ ] Extensões de local e afiliadas ativas no Google Ads, vinculadas ao GMB.
-   [ ] Raio de geolocalização ajustado para máxima relevância (3-8km), com exclusão de áreas irrelevantes.
-   [ ] Criativos de anúncios contendo elementos visuais do local e ofertas exclusivas para a região.
-   [ ] Monitoramento de ligações e solicitações de rota configuradas como conversões primárias no Google Ads.
-   [ ] Campanhas de Meta Ads configuradas com objetivo "Tráfego para o Estabelecimento" ou "Conversões" (com pixel de visita física).
-   [ ] Teste A/B de diferentes ofertas, CTAs e formatos de criativo com apelo local.
-   [ ] Uso de públicos personalizados (clientes existentes, engajamento com a página) ou Lookalike Audiences no Meta Ads.
-   [ ] Integração do pixel do Facebook e da tag de conversão do Google Ads no site ou landing page (se aplicável).
-   [ ] Revisão da velocidade de carregamento da landing page para dispositivos móveis.

---

## Métricas de Referência

| Métrica                 | Benchmark (Negócios Locais) | Meta (Exemplo) |
| :---------------------- | :-------------------------- | :------------- |
| CTR (Google Search Ads) | 3.5% - 7%                   | > 5.5%         |
| CPC Médio (Google Ads)  | R$2,80 - R$7,50             | < R$4,50       |
| Custo por Ligação       | R$18,00 - R$45,00           | < R$30,00      |
| Custo por Visita à Loja | R$25,00 - R$70,00           | < R$40,00      |
| ROAS (Vendas Offline)   | 2.5:1 - 6:1                 | > 3.5:1        |
| Taxa de Conversão (Ligação) | 6% - 18%                    | > 10%          |

---

## Erros Comuns

1.  **Geotargeting muito amplo ou restritivo**: Segmentar uma cidade inteira para um negócio de bairro dilui o orçamento e o impacto. Segmentar apenas 1km para um serviço especializado pode limitar o alcance desnecessariamente.
    *   **Como evitar**: Iniciar com um raio de 3-5 km para negócios de varejo ou serviços diários, ajustando gradualmente com base nos dados de alcance, impressões e cliques. Utilizar as opções de exclusão de localização para remover áreas irrelevantes ou de baixa densidade populacional dentro do raio. Exemplo: Para um pet shop em Pinheiros, começar com 4km e excluir áreas comerciais que não são residenciais.

2.  **Criativos genéricos sem apelo local**: Utilizar imagens de banco de dados ou vídeos que não refletem a fachada, o interior ou a comunidade do negócio. Isso falha em criar conexão com o público local.
    *   **Como evitar**: Produzir anúncios com fotos e vídeos reais do estabelecimento, da equipe e de clientes locais interagindo. Incluir menções a pontos de referência próximos, nomes de bairros ou eventos locais nos textos e legendas. Exemplo: Em vez de "Melhor Café", usar "Experimente o melhor café da Rua dos Pinheiros, perto da Praça do Sol!".

3.  **Não vincular o Google Meu Negócio (GMB) no Google Ads**: Este é um erro crítico que impede a exibição de extensões de local e o uso de dados de visitas à loja para otimização de lances.
    *   **Como evitar**: Sempre verificar e conectar o perfil GMB verificado à conta do Google Ads antes de criar qualquer campanha local, especialmente as campanhas Performance Max e campanhas de pesquisa com foco em tráfego para a loja física. Isso garante que o endereço, telefone e horário sejam exibidos corretamente e que as visitas à loja sejam mensuradas.

---

## Dicas Avançadas

1.  **Otimização de Horário de Exibição Localizada**: Analisar os picos de demanda para o seu tipo de negócio no contexto local (ex: restaurantes antes do almoço/jantar, academias no começo da manhã/final da tarde) e ajustar os horários de exibição dos anúncios para concentrar o orçamento nesses períodos. Ex: Uma pizzaria pode desativar anúncios das 0h às 17h, ativando-os apenas para o período de pico do jantar.

2.  **Campanhas de Retargeting por Proximidade**: Criar públicos personalizados no Meta Ads com base em pessoas que estiveram fisicamente próximas ao seu estabelecimento nos últimos 30-90 dias (utilizando dados de localização do app, se disponível e consentido, ou por meio de parceiros de dados). Segmentar esses públicos com ofertas de retorno ou lembretes.

3.  **Aproveitamento de Dados de Primeiros Clientes (1st-Party Data)**: Importar listas de e-mails e telefones de clientes locais existentes para as plataformas de anúncios (Meta Ads, Google Ads). Use essas listas para criar públicos semelhantes (Lookalike Audiences) altamente segmentados na sua área geográfica, expandindo o alcance para perfis com alta probabilidade de conversão.

4.  **Integração com Eventos Comunitários e Sazonais**: Desenvolver campanhas de anúncios locais específicas para coincidir com eventos comunitários, feriados locais ou promoções sazonais. Utilize criativos que mencionem diretamente o evento ou a sazonalidade, criando um senso de oportunidade e pertencimento. Ex: "Desconto especial para o dia do bairro em [Nome do Bairro]!" ou "Promoção de Páscoa, venha buscar seu chocolate artesanal!".

5.  **Testes A/B de Gatilhos de Escassez e Urgência Local**: Experimentar criativos que incorporem gatilhos de escassez ou urgência com um toque local. Frases como "Últimas vagas para moradores de [Bairro]!", "Oferta válida apenas esta semana para nossa comunidade!", ou "Poucas unidades restantes na loja de [Endereço]" podem aumentar significativamente a taxa de cliques e conversões para negócios físicos.