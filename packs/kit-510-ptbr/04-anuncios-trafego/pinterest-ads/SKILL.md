---
name: pinterest-ads
description: "Pinterest Ads — Skill especializada para planejamento, criação, otimização e análise de campanhas de anúncios no Pinterest."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Pinterest Ads

Esta skill capacita o Claude a planejar, criar, otimizar e analisar campanhas de anúncios no Pinterest para impulsionar tráfego, engajamento e vendas, utilizando as funcionalidades específicas da plataforma.

---

## Keywords

Pinterest Ads Manager, Pinterest Tag, Shopping Ads, Idea Ads, Anúncios de Coleção, Otimização de Lances, Públicos Personalizados Pinterest, Lookalikes Pinterest, Segmentação por Interesses, Pinterest Analytics, Retargeting Pinterest, Catálogo de Produtos Pinterest.

---

## Quick Start

1.  **Acessar Pinterest Ads Manager**: Navegue até `ads.pinterest.com` e faça login com sua conta comercial do Pinterest.
2.  **Iniciar Nova Campanha**: Clique em `Anúncios` no menu superior, depois em `Criar Campanha` e selecione o objetivo `Consideração (Tráfego)` para direcionar visitas ao seu site.
3.  **Configurar Orçamento e Agendamento**: Defina um `Orçamento Diário` de R$ 75,00 e uma `Data de Início` imediata, sem data de término.
4.  **Instalar Pinterest Tag**: No painel de campanha, localize a seção para `Pinterest Tag` e insira o ID da Tag para rastreamento de eventos em `www.minhaloja.com.br`.

---

## Core Workflows

### Workflow 1: Criação e Lançamento de Campanha de Conversão para E-commerce

Este workflow detalha a configuração de uma campanha de Shopping Ads no Pinterest, focada em vendas diretas, utilizando um catálogo de produtos sincronizado.

1.  **Acesso e Objetivo**:
    *   No Pinterest Ads Manager, clique em `Criar Campanha`.
    *   Selecione o objetivo `Conversões` para otimizar a campanha para compras, adições ao carrinho ou checkouts.
    *   Dê um nome à campanha, como `Campanha Vendas Verão 2025 - Decoracao`.
2.  **Configuração de Orçamento e Agendamento**:
    *   Escolha `Orçamento Diário` e defina R$ 150,00.
    *   Defina `Data de Início` para hoje e deixe sem `Data de Término` para monitoramento contínuo.
3.  **Configuração do Grupo de Anúncios (Ad Group)**:
    *   Nomeie o grupo de anúncios como `Ad Group Retargeting Carrinho Abandonado`.
    *   Em `Estratégia de Lance`, selecione `Lance Automático` para que o Pinterest otimize os lances para conversões.
    *   **Público-Alvo**:
        *   Em `Públicos Personalizados`, selecione um público previamente criado de `Visitantes do Site que Adicionaram ao Carrinho nos Últimos 30 Dias`.
        *   Para expansão, adicione um público de `Lookalike de Compradores (Top 5%)` baseado nos seus clientes existentes.
        *   Em `Segmentação Detalhada`, adicione interesses como `Decoração de Interiores`, `Design de Móveis` e `Organização de Casa` para capturar novos usuários com alta intenção.
        *   Exclua públicos como `Compradores Recorrentes (Últimos 7 Dias)` para evitar desperdício de impressões em quem já comprou recentemente.
    *   **Posicionamentos**: Deixe `Todos os Posicionamentos` ativados para maximizar o alcance.
4.  **Seleção e Criação de Anúncios**:
    *   Em `Formato do Anúncio`, escolha `Shopping Ads`.
    *   **Catálogo de Produtos**: Verifique se o `Catálogo de Produtos` está sincronizado e ativo.
    *   Selecione os produtos para anunciar. Por exemplo, filtre por produtos da categoria `Decoração Rústica` ou `Móveis de Área Externa`.
    *   O Pinterest criará anúncios automaticamente a partir dos seus produtos. Você pode personalizar os `títulos e descrições dos Pins` para incluir CTAs como "Compre Agora" ou "Descubra a Coleção".
    *   **URL de Destino**: Certifique-se de que as URLs de destino dos produtos estejam corretas e direcionem para as páginas de produto específicas.
5.  **Revisão e Publicação**:
    *   Revise todas as configurações da campanha, grupo de anúncios e anúncios individuais.
    *   Clique em `Publicar` para lançar a campanha.

### Workflow 2: Otimização Contínua de Campanha de Tráfego para Blog Post

Este workflow descreve as etapas para otimizar uma campanha de tráfego existente, visando aumentar o número de cliques qualificados para um artigo de blog.

1.  **Monitoramento Inicial e Métricas Chave**:
    *   Acesse o `Painel de Campanhas` no Pinterest Ads Manager.
    *   Filtre pela campanha `Tráfego Blog Tendências 2024`.
    *   Monitore as métricas de `CTR (Click-Through Rate)`, `CPC (Custo por Clique)` e `Cliques de Saída` nos primeiros 7 dias. Um CTR abaixo de 0,8% ou um CPC acima de R$ 2,00 para este tipo de campanha indica necessidade de otimização.
2.  **Otimização de Criativos (Pins)**:
    *   Navegue até a aba `Anúncios` dentro do grupo de anúncios.
    *   Identifique os pins com menor `CTR`.
    *   Pause os 20% piores pins.
    *   Crie 3-5 novos pins com variações de imagem (ex: lifestyle vs. produto isolado), texto (ex: "5 Dicas Essenciais" vs. "Guia Completo") e chamada para ação (ex: "Leia Mais" vs. "Acesse o Artigo").
    *   Utilize imagens verticais (proporção 2:3, 1000x1500px) e com texto sobreposto claro.
3.  **Refinamento de Segmentação**:
    *   Acesse as configurações do `Grupo de Anúncios`.
    *   Em `Segmentação Detalhada`, analise os `Interesses` e `Palavras-chave` que estão gerando cliques, mas com baixo engajamento pós-clique (alta taxa de rejeição no Google Analytics).
    *   Remova interesses como `Decoração Geral` e adicione termos mais específicos como `Decoração Sustentável`, `DIY para Casa` ou `Arquitetura de Interiores` se o artigo for sobre nichos mais específicos.
    *   Utilize o `Relatório de Termos de Busca` para identificar palavras-chave irrelevantes e adicioná-las como `Palavras-chave Negativas`. Exemplo: se o artigo é sobre "decoração de interiores", adicione `decoração de festas` como negativa.
4.  **Ajuste de Lances e Orçamento**:
    *   Se o `CPC` estiver alto e o `CTR` baixo, considere diminuir o `Lance Máximo` se estiver em manual, ou ajustar a `Estratégia de Lance` para `Lance Automático` com uma meta de `Custo por Clique` (se disponível para o objetivo).
    *   Se a campanha estiver performando bem (alto CTR, baixo CPC), aumente o `Orçamento Diário` em 10-20% a cada 2-3 dias para escalar os resultados sem desestabilizar o aprendizado da campanha.
5.  **Teste A/B de Landing Page**:
    *   Crie uma variação da página de destino do blog post com um título diferente ou um layout otimizado para mobile.
    *   Duplique o grupo de anúncios e direcione o novo grupo para a variação da Landing Page.
    *   Monitore as métricas de `Tempo na Página` e `Taxa de Rejeição` no Google Analytics para determinar qual versão da Landing Page gera mais engajamento.

---

## Templates

### Estrutura de Campanha Pinterest Ads (Conversão)

```
Campanha: Vendas Inverno - Moda Feminina (Objetivo: Conversões)
  Grupo de Anúncios 1: Retargeting Carrinho Abandonado (Público: Visitantes que Adicionaram ao Carrinho 30D)
    Anúncio 1.1: Coleção Verão - Vestido Floral (Pin ID: 123456789)
    Anúncio 1.2: Coleção Verão - Saia Midi (Pin ID: 987654321)
  Grupo de Anúncios 2: Lookalike Compradores - Roupas Casuais (Público: Lookalike de Compradores 1%)
    Anúncio 2.1: Promoção Jeans - Nova Coleção (Pin ID: 112233445)
    Anúncio 2.2: Blusas Femininas - Últimas Tendências (Pin ID: 554433221)
```

### Copy de Anúncio Pinterest (Shopping Ad - Exemplo)

```
Título do Pin: Vestido Midi Floral - Perfeito para o Verão!
Descrição do Pin: Deslumbre-se com a leveza e elegância do nosso Vestido Midi Floral. Confeccionado em tecido premium, ideal para qualquer ocasião. Clique e garanta o seu! #VestidoFloral #ModaVerão #EstiloFeminino #CompreAgora
URL de Destino: https://www.minhaloja.com.br/vestido-midi-floral
```

---

## Checklist

- [x] Pinterest Tag instalada e verificada com eventos de conversão (PageView, AddToCart, Checkout)?
- [x] Catálogo de produtos sincronizado, atualizado e sem erros no Pinterest Merchant Center?
- [x] Públicos personalizados (visitantes do site, engajadores de pins) criados e atualizados?
- [x] Públicos de Lookalike configurados para escala (compradores, adicionaram ao carrinho)?
- [x] Criativos (pins) em formato vertical (2:3 ou 1000x1500px) e com alta resolução?
- [x] Textos dos pins claros, concisos, com palavras-chave relevantes e um CTA explícito?
- [x] URLs de destino de todos os anúncios corretas, funcionando e direcionando para páginas otimizadas?
- [x] Orçamento diário/total alinhado com o objetivo da campanha e o ciclo de vendas do produto?
- [x] Segmentação por interesses, palavras-chave e dados demográficos refinada para o público ideal?
- [x] Exclusão de públicos irrelevantes (ex: clientes recorrentes recentes, IPs internos) aplicada?
- [x] Monitoramento das métricas de campanha (CTR, CPC, CPA, ROAS) agendado para análise regular?
- [x] Testes A/B para criativos, públicos ou lances planejados para otimização contínua?

---

## Métricas de Referência

| Métrica               | Benchmark          | Meta               |
|-----------------------|--------------------|--------------------|
| CTR (Click-Through Rate) | 0.8% - 1.5%        | > 1.2%             |
| CPC (Custo por Clique)  | R$ 0.70 - R$ 2.50  | < R$ 1.80          |
| ROAS (Return on Ad Spend) | 2.0x - 3.5x        | > 2.8x             |
| CPA (Custo por Aquisição)| R$ 30 - R$ 120     | < R$ 80            |
| Taxa de Conversão      | 1.0% - 2.5%        | > 2.0%             |
| Custo por Mille (CPM) | R$ 15 - R$ 40      | < R$ 30            |

---

## Erros Comuns

1.  **Não Verificar a Pinterest Tag**: Lançar campanhas de conversão sem a tag instalada corretamente e os eventos verificados resulta em perda total de dados de conversão e impossibilidade de otimização eficaz. **Como evitar**: Após a instalação, use o `Pinterest Tag Helper` (extensão do Chrome) e o próprio `Pinterest Ads Manager` (na seção de Tags) para verificar se os eventos de `PageView`, `AddToCart` e `Checkout` estão disparando corretamente em seu site antes de ativar a campanha.
2.  **Uso de Criativos Não-Otimizados para Pinterest**: Publicar pins com proporções incorretas (ex: horizontais 16:9), baixa resolução ou sem sobreposição de texto claro. O Pinterest é visual; pins que não se destacam no feed do usuário têm CTRs muito baixos. **Como evitar**: Sempre utilize a proporção vertical 2:3 (1000x1500px é o ideal) para imagens e vídeos. Inclua texto conciso e legível sobre a imagem com uma chamada para ação clara. Teste diferentes ângulos e estilos visuais que ressoem com a estética do Pinterest (inspiração, DIY, aspiração).
3.  **Segmentação Ampla Demais para Objetivos de Funil Inferior**: Campanha de conversão com segmentação apenas por "Interesses amplos" sem públicos personalizados ou lookalikes, resultando em cliques caros e baixas taxas de conversão. **Como evitar**: Para campanhas de conversão (vendas), priorize públicos de retargeting (visitantes, adicionaram ao carrinho), lookalikes de clientes existentes ou segmentação por palavras-chave com alta intenção de compra. Use interesses amplos com moderação e apenas para objetivos de funil superior (awareness, tráfego).

---

## Dicas Avançadas

1.  **Otimização por Atributos do Catálogo de Produtos**: No Pinterest, é possível criar grupos de anúncios baseados em atributos específicos do seu catálogo (preço, marca, categoria, estoque). **Exemplo**: Crie um grupo de anúncios focado apenas em produtos com `Preço > R$ 300` e `Categoria = Calçados Premium`, com um lance mais agressivo, pois esses itens geralmente têm maior margem de lucro.
2.  **Aproveitar Idea Pins para Awareness e Tráfego Qualificado**: Os Idea Pins (formato de storytelling multi-páginas) podem ser promovidos como anúncios. Eles são excelentes para educar ou inspirar. **Exemplo**: Crie um Idea Pin promovendo "5 Receitas Veganas Rápidas para o Dia a Dia" e adicione um link de saída (deep link) para o seu blog post completo ou página de produto de ingredientes. Monitore o `Engajamento` e `Cliques de Saída` para otimizar.
3.  **Teste A/B com Landing Pages Específicas para Pinterest**: Não direcione todo o tráfego para a homepage. Crie landing pages otimizadas especificamente para o público do Pinterest, com um design mais visual, menos texto e uma jornada de usuário mais direta. **Exemplo**: Para um anúncio de "Decoração Boho Chic", crie uma LP com um carrossel de produtos nesse estilo, depoimentos de clientes e um botão "Compre a Coleção" em destaque, em vez de uma página de categoria genérica.
4.  **Uso de Públicos de Engajamento com Pins Específicos para Retargeting**: Além de visitantes do site, crie públicos personalizados de usuários que salvaram, comentaram ou clicaram em pins *específicos* da sua conta. **Exemplo**: Se você tem um pin viral sobre "Ideias para Jardinagem Vertical", crie um público de `Engajadores do Pin X` e direcione anúncios de produtos relacionados à jardinagem vertical para eles, com uma mensagem altamente relevante.
5.  **Análise de Tendências do Pinterest Trends para Criação de Conteúdo e Segmentação**: Utilize a ferramenta `Pinterest Trends` (trends.pinterest.com) para identificar termos de busca em alta. **Exemplo**: Se "Decoração Minimalista Japandi" está em ascensão, crie novos pins e anúncios com esse tema, utilizando essas palavras-chave na descrição e na segmentação. Isso garante que seu conteúdo esteja alinhado com o que os usuários já estão procurando ativamente na plataforma.