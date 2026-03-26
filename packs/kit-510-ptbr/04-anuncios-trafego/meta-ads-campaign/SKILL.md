---
name: meta-ads-campaign
description: "Meta Ads Campaign — Skill especializada para criação, otimização e gestão de campanhas de anúncios no Meta (Facebook e Instagram)."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Meta Ads Campaign

Esta skill capacita o Claude a estruturar, lançar e otimizar campanhas de anúncios no Meta, focando em resultados como vendas, leads e tráfego qualificado, utilizando as melhores práticas da plataforma.

---

## Keywords

Campanhas de Conversão, Públicos Personalizados, Lookalike Audiences, Otimização de Orçamento de Campanha (CBO), Advantage+ Placements, Eventos de Pixel, ROAS (Retorno sobre o Investimento em Anúncios), CPC (Custo por Clique), CTR (Taxa de Cliques), Anúncios Dinâmicos de Produtos (DPA), Teste A/B Meta, Gerenciador de Eventos.

---

## Quick Start

1.  **Configurar Pixel e Eventos**: Instalar o Pixel Meta no site e configurar eventos de conversão "Purchase", "Add to Cart" e "ViewContent" no Gerenciador de Eventos, priorizando "Purchase" para campanhas de vendas.
2.  **Criar Campanha de Vendas (Conversão)**: Iniciar uma nova campanha no Gerenciador de Anúncios, selecionando o objetivo "Vendas" e ativando a Otimização de Orçamento de Campanha (CBO) com um orçamento diário de R$ 150.
3.  **Segmentar Públicos Estratégicos**: Criar um conjunto de anúncios com público Lookalike 1% de compradores existentes e outro com interesses detalhados (ex: "e-commerce", "moda feminina"), excluindo compradores existentes de ambos.
4.  **Desenvolver Criativos e Copies**: Upload de 3-5 variações de criativos (imagens estáticas, vídeos curtos, carrossel) e 2-3 textos de anúncio diferentes, cada um com um CTA claro como "Comprar Agora".
5.  **Ativar e Monitorar**: Publicar a campanha e iniciar o monitoramento das métricas principais (ROAS, CPA, CTR) após 72 horas para identificar os anúncios e conjuntos com melhor desempenho.

---

## Core Workflows

### Workflow 1: Lançamento de Campanha de Vendas para E-commerce com Pixel Otimizado

Este workflow detalha a criação de uma campanha focada em gerar vendas diretas para um e-commerce, utilizando o Pixel Meta para otimização.

1.  **Verificação e Configuração do Pixel Meta**:
    *   Acessar o Gerenciador de Eventos no Meta Business Suite.
    *   Confirmar que o Pixel está ativo e recebendo dados para os eventos "Purchase", "Add to Cart" e "ViewContent".
    *   No painel de "Configurações de Eventos Agregados", verificar se o evento "Purchase" está priorizado como o evento de otimização de maior valor para o domínio do e-commerce.

2.  **Estrutura da Campanha no Gerenciador de Anúncios**:
    *   **Nível Campanha**:
        *   Clicar em "Criar", selecionar o objetivo "Vendas" (Conversões).
        *   Nomear a campanha: `CAM_VENDAS_PRODUTO_PRINCIPAL_20240720_CBO`.
        *   Ativar "Otimização de Orçamento de Campanha (CBO)".
        *   Definir o orçamento diário da campanha em R$ 250.

3.  **Configuração do Conjunto de Anúncios (Nível 1: Lookalike de Compradores)**:
    *   **Nome**: `CONJ_LLK1%COMPRADORES_EXC_COMPRADORES_ADVTPLUS`.
    *   **Evento de Conversão**: Selecionar "Website" e escolher o evento "Purchase".
    *   **Público**:
        *   Selecionar um Público Personalizado de "Lookalike 1% de Compradores Existentes" (baseado em um arquivo de clientes ou eventos "Purchase" do pixel).
        *   Em "Excluir", adicionar o Público Personalizado de "Compradores nos últimos 180 dias" para evitar impactar clientes recentes.
    *   **Posicionamentos**: Selecionar "Advantage+ Placements" (Recomendado).
    *   **Controle de Lance**: Deixar em aberto para o algoritmo otimizar automaticamente (Estratégia de Lance de Menor Custo).

4.  **Configuração do Conjunto de Anúncios (Nível 2: Interesses Detalhados)**:
    *   **Nome**: `CONJ_INTERESSES_MODA_ONLINE_25-55_ADVTPLUS`.
    *   **Evento de Conversão**: Selecionar "Website" e escolher o evento "Purchase".
    *   **Público**:
        *   **Idade**: 25-55 anos.
        *   **Gênero**: Mulheres (ou ambos, dependendo do produto).
        *   **Segmentação Detalhada**: Incluir interesses como "E-commerce", "Compras online", "Moda feminina", "Roupa", "Loja virtual".
        *   Em "Excluir", adicionar o Público Personalizado de "Compradores nos últimos 180 dias".
    *   **Posicionamentos**: Selecionar "Advantage+ Placements".
    *   **Controle de Lance**: Deixar em aberto.

5.  **Criação dos Anúncios (3-5 por Conjunto)**:
    *   Para cada conjunto, criar 3-5 anúncios distintos.
    *   **Formato**: Variar entre imagem única, vídeo e carrossel.
    *   **Criativos**: Utilizar imagens de alta qualidade de produtos em uso, vídeos curtos (15-30s) demonstrando benefícios.
    *   **Texto Principal**: Escrever 2-3 variações de copy, destacando diferentes propostas de valor (ex: "conforto", "estilo", "promoção").
    *   **Título**: Curto e impactante (ex: "Nova Coleção!", "Frete Grátis!").
    *   **Descrição**: Opcional, para complementar o título.
    *   **Chamada para Ação (CTA)**: "Comprar Agora".
    *   **URL do Site**: Link direto para a página do produto ou categoria.
    *   **Nome do Anúncio**: `ANUNCIO_VIDEO_PROD_MODELO_CTA_COMPRAR`.

### Workflow 2: Otimização Pós-Lançamento para ROAS Elevado

Este workflow foca em como analisar e otimizar uma campanha de vendas que já está ativa, buscando melhorar o Retorno sobre o Investimento em Anúncios (ROAS).

1.  **Análise de Dados Agregados (após 5-7 dias de campanha)**:
    *   **Gerenciador de Anúncios**: Acessar o painel de "Quebras" (Breakdowns) e analisar o desempenho por "Conjunto de Anúncios", "Anúncio", "Idade", "Gênero" e "Posicionamento".
    *   **Métricas Focais**: ROAS, Custo por Aquisição (CPA), CTR (Taxa de Cliques no Link), CPM (Custo por Mil Impressões), Frequência.

2.  **Identificação e Pausa de Ineficiências**:
    *   **Anúncios com Baixo Desempenho**: Pausar criativos com CTR inferior a 1.0% e CPA significativamente acima da meta de referência (ex: CPA > R$ 120).
    *   **Conjuntos de Anúncios com ROAS Baixo**: Se um conjunto de anúncios tem um ROAS consistentemente abaixo de 1.5x e está gastando muito, considere pausá-lo ou refiná-lo drasticamente.

3.  **Duplicação e Expansão de Sucesso**:
    *   **Conjuntos Vencedores**: Duplicar conjuntos de anúncios com ROAS superior a 3.0x. Ao duplicar, faça pequenas alterações:
        *   **Variação 1**: Manter o mesmo público, testar novos criativos.
        *   **Variação 2**: Testar um Lookalike de 1-2% com base no público original, ou expandir ligeiramente a segmentação de interesse.
    *   **Criativos Vencedores**: Pegar os criativos com maior CTR e menor CPA e criar novas variações deles (ex: mudar a música do vídeo, alterar o texto principal).

4.  **Ajuste de Orçamento (CBO)**:
    *   Se a campanha como um todo está performando bem (ROAS acima da meta), aumentar o orçamento da campanha em 10-20% a cada 3-4 dias para permitir que o algoritmo escale sem desestabilizar a otimização.
    *   Se a campanha está com ROAS abaixo da meta, mas alguns conjuntos estão bem, o CBO já está realocando. Não reduzir o orçamento drasticamente, mas sim focar em pausar os elementos de baixo desempenho.

5.  **Testes A/B (A/B Test) Estruturados**:
    *   Utilizar a ferramenta de Teste A/B do Meta para comparar variações críticas. Exemplo:
        *   **Hipótese**: Um novo vídeo de unboxing gerará um CTR 50% maior do que a imagem estática atual.
        *   **Configuração**: Criar um Teste A/B comparando o anúncio com a imagem estática (Controle) e o anúncio com o vídeo de unboxing (Variação). O Meta dividirá a audiência e o orçamento igualmente.
        *   **Análise**: Após 7-10 dias, analisar os resultados para ver qual variação entregou melhor ROAS e CTR.

---

## Templates

### Template de Copy de Anúncio de Vendas (Produto Físico)

```
[Nome do Produto] - Transforme seu [Área de Benefício]!

Cansado de [Dor do Cliente]? Conheça o [Nome do Produto], a solução perfeita para [Benefício 1] e [Benefício 2].

✨ **Características Principais:**
- Material premium para [Vantagem Material]
- Design ergonômico para [Conforto/Facilidade]
- [Característica única] que te garante [Benefício Exclusivo]

🔥 **Oferta Exclusiva por Tempo Limitado!**
De R$ [Preço Antigo] por apenas **R$ [Preço Novo]**!
🚚 Frete GRÁTIS para todo o Brasil.

Clique em "Comprar Agora" e garanta o seu antes que o estoque acabe!
#MetaAds #Ecommerce #OfertaEspecial #[NomeMarca] #[NomeProduto] #Transformacao
```

### Template de Estrutura de Nomenclatura para Campanhas Meta Ads

```
**Nomenclatura de Campanha:**
CAM_OBJETIVO_PRODUTO/SERVIÇO_DATA_ESTRATEGIA

Exemplo: `CAM_VENDAS_CURSO_MARKETING_20240720_CBO_LLK`
(Campanha de Vendas para um Curso de Marketing, iniciada em 20/07/2024, usando Otimização de Orçamento de Campanha e público Lookalike)

**Nomenclatura de Conjunto de Anúncios:**
CONJ_PUBLICO_TIPO_POSICIONAMENTO_OTIMIZACAO

Exemplo: `CONJ_LLK1%COMPRADORES_EXC_COMPRADORES_ADVTPLUS_PURCHASE`
(Conjunto de Anúncios para Lookalike 1% de Compradores, excluindo Compradores, com Advantage+ Placements, otimizando para Purchase)

**Nomenclatura de Anúncio:**
ANUNCIO_CRIATIVO_COPY_CTA

Exemplo: `ANUNCIO_VIDEO_DEPOIMENTO_BENEFICIO_1_COMPRAR`
(Anúncio com Criativo de Vídeo de Depoimento, Copy focada no Benefício 1, com CTA Comprar Agora)
```

---

## Checklist

- [x] Pixel Meta instalado e verificando eventos de "Page View", "Add to Cart" e "Purchase" corretamente.
- [x] Domínio verificado no Gerenciador de Negócios para otimização de eventos agregados.
- [x] Campanhas configuradas com o objetivo correto (Vendas para conversões, Leads para formulários, Tráfego para visitas).
- [x] Otimização de Orçamento de Campanha (CBO) ativada para campanhas com múltiplos conjuntos de anúncios.
- [x] Públicos Personalizados (visitantes do site, engajados com perfil) e Lookalikes (1-3% de compradores ou leads) criados e atualizados.
- [x] Mínimo de 3 criativos diversos (vídeo, imagem, carrossel) por conjunto de anúncios para teste.
- [x] Textos de anúncio (copy) com clareza, chamadas para ação (CTAs) fortes e alinhados ao objetivo.
- [x] Links de destino (URL) funcionando, direcionando para a página correta e rastreados com parâmetros UTM.
- [x] Posicionamentos Advantage+ Placements selecionados para maximizar alcance e otimização automática.
- [x] Exclusão de públicos irrelevantes (ex: clientes existentes em campanhas de prospecção, público Lookalike de visitantes em campanhas de Retargeting).

---

## Métricas de Referência

| Métrica               | Benchmark (e-commerce - Brasil) | Meta (e-commerce - Brasil) |
|-----------------------|---------------------------------|----------------------------|
| ROAS (Retorno sobre Gasto em Anúncios) | 2.0x - 3.0x                     | 3.5x - 5.0x                |
| CPA (Custo por Aquisição/Compra) | R$ 50 - R$ 150                  | R$ 30 - R$ 80              |
| CTR (Link Click-Through Rate) | 1.5% - 2.5%                     | 2.8% - 4.5%                |
| CPM (Custo por Mil Impressões) | R$ 15 - R$ 40                   | R$ 10 - R$ 30              |
| Taxa de Conversão (do clique à compra) | 1.5% - 2.5%                     | 2.8% - 4.0%                |
| Frequência (Campanhas de Prospecção) | 2.0 - 3.5                       | 2.5 - 4.0                  |

---

## Erros Comuns

1.  **Pixel Meta mal configurado ou eventos não priorizados**: Causa otimização ineficaz e relatórios imprecisos, resultando em conversões perdidas ou campanhas gastando em eventos errados.
    *   **Como evitar**: Acessar o "Gerenciador de Eventos", usar a ferramenta "Testar Eventos" para simular ações no site (ex: adicionar ao carrinho, finalizar compra) e verificar se o Meta registra os eventos corretamente. No painel de "Configurações de Eventos Agregados", certificar-se de que "Purchase" é o evento de maior prioridade para campanhas de vendas.

2.  **Públicos muito amplos sem segmentação ou muito restritos com baixo volume**: Leva a gastos ineficientes ao atingir pessoas desinteressadas ou a uma escala limitada que impede o crescimento.
    *   **Como evitar**: Para prospecção, começar com públicos Lookalike de 1% de clientes de alto valor ou interesses detalhados com Alcance Potencial entre 1 milhão e 5 milhões. Para remarketing, usar públicos personalizados de "Visitantes do site nos últimos 30-90 dias" ou "Pessoas que adicionaram ao carrinho mas não compraram". Monitorar o tamanho do público no Gerenciador de Anúncios para garantir que não esteja abaixo de 500 mil para prospecção, o que pode limitar a entrega.

3.  **Não realizar testes de criativos e copies suficientes ou não os renovar**: Resulta em fadiga de anúncio, queda do CTR e aumento do CPM/CPA ao longo do tempo, pois a mesma audiência vê os mesmos anúncios repetidamente.
    *   **Como evitar**: Sempre iniciar conjuntos de anúncios com pelo menos 3-5 variações de criativos (vídeos, imagens, carrossel) e 2-3 variações de texto principal. Monitorar a "Frequência" da campanha. Quando a frequência ultrapassar 3.5-4.0 em campanhas de prospecção, e o CTR começar a cair, é um sinal claro para criar novos criativos e copies, ou testar novos ângulos nos anúncios existentes.

---

## Dicas Avançadas

1.  **Utilização Estratégica de Anúncios Dinâmicos de Produtos (DPA) para Funil Completo**: Não limite os DPAs apenas ao remarketing. Crie campanhas de prospecção com DPA, segmentando públicos Lookalike ou de interesse amplo. O Meta mostrará os produtos mais relevantes do seu catálogo para novos usuários, aumentando a chance de conversão inicial. Certifique-se de ter um catálogo de produtos robusto e atualizado no Gerenciador de Comércio.

2.  **Otimização de Orçamento de Campanha (CBO) com Estrutura de Funil (TOFU/MOFU/BOFU)**: Estruture uma única campanha com CBO e crie conjuntos de anúncios representando as etapas do funil:
    *   **TOFU (Topo de Funil)**: Público Lookalike 1-3% de visitantes/engajados, Interesses amplos.
    *   **MOFU (Meio de Funil)**: Retargeting de visitantes do site 7-30 dias, engajados com Instagram/Facebook 30-90 dias.
    *   **BOFU (Fundo de Funil)**: Retargeting de "Adicionou ao carrinho mas não comprou", Lookalike 1% de compradores de alto valor.
    O CBO alocará o orçamento para os conjuntos que geram mais resultados, otimizando o gasto entre as fases do funil.

3.  **Implementação de Regras Automatizadas para Gestão Proativa**: Configure regras automatizadas no Gerenciador de Anúncios para otimizar campanhas sem intervenção manual constante. Exemplos:
    *   `Pausar Anúncio`: Se o ROAS nos últimos 3 dias for < 1.0 e gastos > R$ 50.
    *   `Aumentar Orçamento`: Se o ROAS da campanha nos últimos 7 dias for > 4.0, aumentar o orçamento diário em 15% (limitar a um aumento por semana).
    *   `Notificar`: Se o CPM de um conjunto de anúncios exceder R$ 50 nos últimos 24 horas, enviar notificação.

4.  **Audiências de Valor (Value-Based Lookalikes) para Escalabilidade Qualificada**: Ao criar um público Lookalike, use uma fonte de dados de clientes que inclua o "Valor do Cliente" (Lifetime Value - LTV). O Meta então encontrará usuários semelhantes aos seus clientes mais lucrativos, permitindo uma expansão de público que mantém a qualidade das conversões e o ROAS elevado.

5.  **Testes A/B com Variações de Lances ou Otimização**: Além de criativos e públicos, utilize a ferramenta de Teste A/B do Meta para comparar diferentes estratégias de lance (ex: menor custo vs. teto de lance de R$ 80 por compra) ou diferentes eventos de otimização (ex: otimizar para "Purchase" vs. "Add to Cart" em um funil complexo). Isso fornece insights sobre qual abordagem de lances ou otimização maximiza seu ROAS e volume de conversões.