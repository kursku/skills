---
name: youtube-ads
description: "Youtube Ads — Skill especializada para youtube ads"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Youtube Ads

Esta skill capacita o Claude a planejar, executar e otimizar campanhas de publicidade no YouTube, abrangendo desde a seleção de objetivos e segmentação de público até a análise de métricas e implementação de táticas avançadas para performance.

---

## Keywords

TrueView In-Stream, TrueView Discovery, Bumper Ads, Outstream Ads, CPV, VRC (View Rate), ROAS YouTube, Remarketing de Vídeo, Segmento Personalizado, Canais Concorrentes, Exclusões de Posicionamento, Otimização de Lances.

---

## Quick Start

1.  **Configurar Acompanhamento de Conversões no Google Ads:** Vincule sua conta do YouTube ao Google Ads e garanta que as ações de conversão (e.g., "Compra", "Envio de Formulário") estejam corretamente configuradas e testadas via Google Tag Manager ou gtag.js.
2.  **Selecionar Objetivo de Campanha de Performance:** Crie uma nova campanha no Google Ads, escolhendo "Vendas" ou "Leads" como objetivo, e então selecione "Vídeo" como tipo de campanha.
3.  **Definir Estratégia de Lance e Orçamento:** Para campanhas de performance, utilize "Maximizar Conversões" ou "ROAS Alvo". Estabeleça um orçamento diário mínimo de R$50-100 para permitir aprendizado do algoritmo.
4.  **Criar Segmentos de Público Personalizados:** Desenvolva segmentos com URLs de concorrentes (e.g., `youtube.com/channel/UC...`), termos de pesquisa relevantes (e.g., "melhor software CRM", "curso de marketing digital") e intenção personalizada.
5.  **Desenvolver 2-3 Anúncios em Vídeo Diversos:** Produza vídeos específicos para o YouTube, com durações entre 15-30 segundos para In-Stream e formatos mais longos para Discovery, focando em "hook" nos primeiros 5 segundos e uma clara chamada para ação.

---

## Core Workflows

### Workflow 1: Criação de Campanha de Geração de Leads no YouTube com Formulários de Lead

Este workflow detalha a construção de uma campanha de YouTube Ads focada em capturar leads qualificados diretamente através de formulários nativos do Google Ads, minimizando o atrito do usuário.

**Passos Detalhados:**

1.  **Início da Campanha e Objetivo:**
    *   No Google Ads, clique em `Campanhas` > `+ Nova Campanha` > `+ Nova Campanha`.
    *   Selecione o objetivo `Leads`.
    *   Escolha o tipo de campanha `Vídeo`.
    *   Selecione o subtipo `Gerar leads com formulário de lead` e clique em `Continuar`.
    *   Nomeie a campanha, por exemplo, `YT_Leads_Formulario_CRMSoftware`.

2.  **Definição de Orçamento e Lances:**
    *   **Estratégia de Lance:** Selecione `Maximizar conversões`. Para campanhas de lead, o foco é na quantidade de leads, e essa estratégia otimiza para isso.
    *   **Orçamento:** Defina um `Orçamento diário` de, por exemplo, `R$ 80,00`. Isso permite que o sistema colete dados suficientes para otimização inicial.

3.  **Segmentação de Público Alvo:**
    *   **Localização e Idioma:** Direcione para `Brasil` e `Português`.
    *   **Segmentos de Público:**
        *   **Segmentos Personalizados (Custom Segments):** Crie um novo segmento com "Pessoas que pesquisaram qualquer um destes termos no Google" e inclua termos como "software CRM para pequenas empresas", "ferramenta de gestão de clientes", "comparativo CRM". Crie outro com "Pessoas que visitaram qualquer um destes tipos de sites" e adicione URLs de concorrentes diretos (e.g., `pipedrive.com`, `rdstation.com`).
        *   **Públicos de Intenção Personalizada:** Crie um público com palavras-chave de intenção de compra como "comprar software CRM", "preço CRM online".
        *   **Dados Demográficos:** Ajuste idade e renda familiar se o seu produto/serviço tiver um perfil demográfico específico (e.g., `25-54 anos`, `Renda Familiar Top 10%`).
        *   **Exclusões:** Exclua públicos de remarketing que já converteram (e.g., "Clientes Compradores") para evitar gastar orçamento com quem já é cliente.

4.  **Posicionamentos e Exclusões:**
    *   **Posicionamentos (Opcional):** Para controle granular, você pode segmentar canais específicos (e.g., canais de review de tecnologia, canais de negócios). No entanto, para lead gen, é comum deixar aberto para o Google encontrar as melhores posições.
    *   **Exclusões de Conteúdo:** É CRÍTICO excluir `Conteúdo delicado`, `Transmissões ao vivo`, `Conteúdo incorporado`, `Canais de jogos`, `Vídeos para crianças`. Isso evita impressões em locais de baixa qualidade ou irrelevantes. Exclua também `Tópicos` como "Notícias e Política" ou "Jogos" se não forem relevantes.

5.  **Criação do Anúncio em Vídeo:**
    *   **Vídeo do YouTube:** Cole a URL do seu vídeo (e.g., `https://www.youtube.com/watch?v=ABCDEF123`).
    *   **Formatos:** Use `Anúncio In-stream pulável` para maximizar as visualizações do vídeo e a interação com o formulário.
    *   **URL Final:** A URL da página de destino para quando o usuário clicar no seu anúncio (e.g., `https://seusite.com.br/crm-software`).
    *   **Chamada para Ação (CTA):** `Baixe Agora`, `Saiba Mais`, `Teste Grátis`.
    *   **Título:** `Software CRM Essencial` (90 caracteres).
    *   **Formulário de Lead (Novo):**
        *   **Título do Formulário:** `Solicite seu Teste Grátis de CRM`
        *   **Nome da Empresa:** `Minha Empresa SaaS`
        *   **Descrição:** `Descubra como nosso CRM otimiza suas vendas e atendimento. Preencha e comece hoje!`
        *   **Perguntas:** `Nome Completo`, `Email`, `Telefone`, `Nome da Empresa`. Adicione uma pergunta personalizada como `Quantos funcionários sua empresa possui?` (Múltipla escolha: `1-5`, `6-20`, `21-100`, `100+`).
        *   **URL da Política de Privacidade:** `https://seusite.com.br/politica-de-privacidade`
        *   **Mensagem de Envio:**
            *   **Título:** `Obrigado pelo seu interesse!`
            *   **Descrição:** `Entraremos em contato em breve para agendar sua demonstração.`
            *   **Chamada para Ação:** `Visitar site` ou `Baixar e-book`.

### Workflow 2: Otimização de Campanha de YouTube Ads para E-commerce com ROAS

Este workflow foca em refinar campanhas de YouTube Ads para e-commerce, visando maximizar o Retorno sobre o Investimento em Publicidade (ROAS) através de ajustes de lances, segmentação e criativos.

**Passos Detalhados:**

1.  **Análise Inicial de Performance (7-14 dias após o lançamento):**
    *   **Métricas Primárias:** Observe `ROAS`, `Custo por Conversão (CPA)`, `Taxa de Conversão (CVR)`, `Taxa de Visualização (VTR)` e `Custo por Visualização (CPV)`.
    *   **Relatórios de Segmentação:** Vá em `Campanhas` > `Grupos de anúncios` > `Segmentos`. Analise o desempenho por `Tipo de dispositivo`, `Hora do dia`, `Localização` e `Idade/Gênero`. Identifique segmentos com ROAS abaixo do alvo.
    *   **Relatório de Posicionamentos:** Em `Conteúdo` > `Posicionamentos`, verifique os canais e vídeos onde seus anúncios foram exibidos. Identifique posicionamentos com baixo ROAS, alto CPV e baixa CVR.

2.  **Ajustes de Lances e Estratégia:**
    *   **ROAS Alvo:** Se a campanha está com `Maximizar valor da conversão` ou `ROAS Alvo`, ajuste o `ROAS Alvo` gradualmente. Se o ROAS está abaixo do alvo (e.g., alvo de 300% e está em 200%), aumente o alvo para 320-350% para forçar o sistema a buscar conversões de maior valor. Se o ROAS estiver muito bom, mas com baixo volume, reduza o alvo para 280% para tentar escalar.
    *   **Ajustes de Lance por Dispositivo:** Se dispositivos móveis têm um ROAS muito menor (e.g., 150% vs. desktop 400%), aplique um ajuste de lance negativo (e.g., `-20%` ou `-30%`) para dispositivos móveis.
    *   **Ajustes de Lance por Demografia/Localização:** Se uma faixa etária ou região específica tem baixo desempenho, aplique ajustes de lance negativos ou exclua esses segmentos.

3.  **Refinamento de Público:**
    *   **Exclusão de Públicos:**
        *   **Baixo Desempenho:** Exclua `segmentos demográficos` ou `interesses` que consistentemente apresentam ROAS negativo ou muito baixo.
        *   **Públicos que Já Compraram:** Utilize listas de remarketing de clientes que já fizeram uma compra para excluí-los de campanhas de aquisição, focando o orçamento em novos clientes.
    *   **Adição de Novos Públicos:**
        *   **Segmentos Personalizados:** Crie novos segmentos de intenção com base em termos de pesquisa de produtos específicos ou URLs de reviews de produtos.
        *   **Públicos Semelhantes (Lookalikes):** Crie públicos semelhantes a partir de suas listas de `compradores`, `visitantes de carrinho abandonado` ou `visitantes de página de produto`.

4.  **Otimização de Criativos e Posicionamentos:**
    *   **Teste A/B de Vídeos:** Teste variações de seus anúncios em vídeo (diferentes "hooks" nos primeiros 5 segundos, CTAs, ofertas). Crie novos anúncios com foco em reviews de clientes, demonstrações de produtos ou promoções sazonais.
    *   **Exclusão de Canais/Vídeos de Baixa Qualidade:**
        *   No relatório de `Posicionamentos`, selecione canais/vídeos com baixo ROAS, alto CPV e/ou visualizações de baixa qualidade (e.g., canais infantis, agregadores de conteúdo genérico, vídeos não relacionados ao nicho).
        *   Clique em `Excluir` > `Excluir do grupo de anúncios` ou `Excluir da campanha` para remover esses posicionamentos.
    *   **Teste de Formatos:** Experimente com `Bumper Ads` (6s, não puláveis) para reforçar branding e complementar campanhas de performance, especialmente para produtos de impulso.

5.  **Ajustes de Orçamento:**
    *   **Escalar Campanhas de Sucesso:** Se uma campanha ou grupo de anúncios está entregando um ROAS excelente, considere aumentar o orçamento em `10-20%` a cada 3-5 dias para não desestabilizar o aprendizado do algoritmo.
    *   **Reduzir Orçamento/Pausar Campanhas Fracas:** Se uma campanha não atinge o ROAS alvo após otimizações e um período de aprendizado adequado, reduza o orçamento ou pause-a para realocar recursos.

---

## Templates

### Roteiro de Anúncio em Vídeo para TrueView In-Stream (Performance)

```
[0-5 segundos] HOOK: close-up de uma pessoa frustrada com o computador, cena de um e-commerce lento.
LOCUTOR (VO): "Cansado de perder vendas por um e-commerce travado?"

[5-15 segundos] PROBLEMA/SOLUÇÃO: Transição rápida para gráficos animados mostrando o problema (lentidão, bugs) e a solução (plataforma "FastShop").
LOCUTOR (VO): "Com a FastShop, seu site carrega 3x mais rápido, garantindo que seus clientes finalizem a compra sem atrito."

[15-25 segundos] BENEFÍCIO/PROVA SOCIAL: Depoimento rápido de cliente satisfeito ou números de aumento de conversão.
CLIENTE (na tela): "Depois da FastShop, minhas vendas online explodiram! Incrível!"
TEXTO NA TELA: "+35% CONVERSÕES EM 30 DIAS!"

[25-30 segundos] CHAMADA PARA AÇÃO (CTA): Tela final com logo, URL do site e botão claro.
LOCUTOR (VO): "Não perca mais tempo e vendas! Clique AGORA para um teste grátis e transforme seu e-commerce!"
TEXTO NA TELA: "TESTE GRÁTIS NA FASTSHOP.COM.BR - CLIQUE E VENDA MAIS!"
BOTÃO: "TESTE GRÁTIS"
```

### Estrutura de Segmento Personalizado (Custom Segment) para YouTube Ads

```
Nome do Segmento: "Interesse em Ferramentas de Produtividade B2B"

Tipo de Segmento: Pessoas que pesquisaram qualquer um destes termos no Google
Termos de Pesquisa:
- "melhor software de gestão de projetos"
- "ferramentas de colaboração online"
- "automação de marketing para pequenas empresas"
- "CRM para vendas"
- "sistema ERP cloud"

Tipo de Segmento: Pessoas que visitaram qualquer um destes tipos de sites
URLs de Websites:
- "asana.com"
- "monday.com"
- "hubspot.com"
- "salesforce.com"
- "trello.com"
- "pipefy.com"

Observações: Este segmento combina a intenção de pesquisa ativa com o interesse demonstrado por visitar sites de concorrentes ou líderes do setor, criando um público altamente qualificado para campanhas de SaaS B2B.
```

---

## Checklist

- [x] Vincular conta do YouTube ao Google Ads.
- [x] Configurar acompanhamento de conversões com valores específicos para e-commerce (e.g., `valor da compra`).
- [x] Criar pelo menos 2 segmentos de público personalizado (intenção de pesquisa e URLs de concorrentes).
- [x] Excluir canais de baixa qualidade, tópicos irrelevantes e transmissões ao vivo.
- [x] Desenvolver 3-5 variações de anúncios em vídeo com CTAs claros e "hooks" nos primeiros 5 segundos.
- [x] Implementar uma estratégia de lance baseada em performance (Maximizar conversões ou ROAS Alvo).
- [x] Realizar teste A/B de miniaturas (thumbnails) dos vídeos.
- [x] Configurar relatórios de audiência e posicionamentos para análise pós-lançamento.
- [x] Programar exclusões de listas de remarketing de clientes existentes para campanhas de aquisição.
- [x] Analisar o VTR (View Rate) e CPV (Custo por Visualização) para otimização de criativos e segmentação.

---

## Métricas de Referência

| Métrica | Benchmark (Performance) | Meta (E-commerce/Leads) |
|---------|-------------------------|-------------------------|
| VTR (View Rate) | 20% - 40% (In-Stream) | > 35%                   |
| CPV (Custo por Visualização) | R$ 0,05 - R$ 0,20       | < R$ 0,10               |
| CTR (Click-Through Rate) | 0,5% - 2,0%             | > 1,0%                  |
| CVR (Taxa de Conversão) | 1,0% - 5,0%             | > 2,5%                  |
| ROAS (Retorno sobre Gasto com Anúncios) | 150% - 300%             | > 250%                  |
| CPA (Custo por Aquisição) | R$ 20,00 - R$ 100,00 (Lead) | < R$ 50,00              |

---

## Erros Comuns

1.  **Não Excluir Canais e Tópicos Irrelevantes**: Anúncios aparecendo em vídeos infantis, canais de jogos ou notícias que não têm relação com o produto, gerando impressões e cliques irrelevantes.
    *   **Como evitar**: Sempre utilize as `Exclusões de conteúdo` (canais, tópicos, tipos de conteúdo) no nível da campanha. Por exemplo, exclua `Jogos`, `Conteúdo incorporado`, `Transmissões ao vivo`, e crie listas de canais específicos para exclusão (e.g., canais de desenhos animados).
2.  **Criativos Genéricos ou Não Otimizados para YouTube**: Utilizar vídeos institucionais longos ou anúncios de TV adaptados, sem um "hook" forte nos primeiros segundos ou CTA claro. Isso resulta em baixo VTR e abandono precoce.
    *   **Como evitar**: Desenvolva vídeos curtos (15-30s para In-Stream), dinâmicos, que capturem a atenção nos primeiros 5 segundos. Inclua a proposta de valor e um CTA explícito. Teste diferentes "hooks" e ofertas.
3.  **Orçamento Muito Baixo para Campanhas de Performance**: Definir um orçamento diário irrisório (e.g., R$10-20) para campanhas de "Maximizar conversões" ou "ROAS Alvo". Isso impede o algoritmo de coletar dados suficientes para otimização.
    *   **Como evitar**: Comece com um orçamento diário de no mínimo R$50-R$100 para campanhas de performance. Monitore os custos por conversão e aumente gradualmente o orçamento em 10-20% a cada 3-5 dias se o ROAS estiver positivo.

---

## Dicas Avançadas

1.  **Remarketing com Base em Engajamento com Vídeos do Canal**: Crie listas de remarketing no Google Ads com usuários que assistiram a 25%, 50%, 75% ou 100% dos vídeos do seu canal do YouTube nos últimos 30-90 dias. Direcione anúncios de fundo de funil para quem demonstrou alto interesse.
2.  **Segmentação por Canais Concorrentes ou Influenciadores do Nicho**: Utilize o recurso de `Posicionamentos` e adicione URLs de canais de YouTube de concorrentes diretos ou de influenciadores que seu público-alvo segue. Seus anúncios serão exibidos antes ou durante os vídeos desses canais, capturando a atenção de um público já qualificado.
3.  **Uso de Vídeos Sequenciais (Video Ad Sequencing)**: Crie uma sequência de anúncios em vídeo para guiar o usuário por uma jornada. Por exemplo, primeiro um Bumper Ad de 6 segundos para branding, depois um TrueView In-Stream de 30 segundos com a proposta de valor, e, para quem assistiu ao segundo, um In-Stream de 15 segundos com uma oferta de conversão.
4.  **Exclusão de Públicos que Já Converteram (Listas de Clientes)**: Suba uma lista de e-mails de seus clientes existentes para o Google Ads e use-a como uma `lista de exclusão` em campanhas de aquisição. Isso garante que seu orçamento seja gasto apenas com potenciais novos clientes.
5.  **Análise de Relatório de Termos de Pesquisa do YouTube (Search Terms Report)**: Embora não seja tão robusto quanto no Google Search, o YouTube oferece insights sobre os termos de pesquisa que levaram os usuários a ver seus anúncios (especialmente em Discovery Ads). Use esses termos para refinar segmentos personalizados e entender melhor a intenção do público.