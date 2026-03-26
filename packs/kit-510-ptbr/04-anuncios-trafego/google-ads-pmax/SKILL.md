---
name: google-ads-pmax
description: "Google Ads Pmax — Skill especializada para google ads pmax"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Google Ads Pmax

Esta skill capacita o Claude a criar, otimizar e analisar campanhas Google Ads Performance Max (PMax), maximizando o ROAS e a aquisição de clientes através de automação.

---

## Keywords

Performance Max, PMax, Google Ads, Automação de Lances, ROAS Alvo, CPA Alvo, Grupos de Ativos, Feeds de Produtos, Metas de Conversão, Sinais de Público, Exclusões de Marca, Otimização de Criativos, Estratégia Omnichannel.

---

## Quick Start

1.  **Configurar Rastreamento de Conversões**: Certifique-se de que o Google Analytics 4 (GA4) está integrado ao Google Ads e que todas as conversões relevantes (e-commerce, leads) estão importadas com valores precisos.
2.  **Criar Nova Campanha PMax**: Acesse a interface do Google Ads, clique em "Nova Campanha", selecione um objetivo como "Vendas" ou "Geração de Leads" e escolha "Performance Max" como tipo de campanha.
3.  **Adicionar Feed de Produtos (se e-commerce)**: Conecte sua conta do Google Merchant Center e selecione o feed de produtos para campanhas de varejo.
4.  **Configurar Grupos de Ativos**: Preencha o primeiro grupo de ativos com um mínimo de 5 títulos curtos, 3 descrições, 10 imagens de alta qualidade e 1 vídeo relevante.
5.  **Definir Sinais de Público Iniciais**: Inclua listas de remarketing (visitantes do site), listas de clientes (CRM) e segmentos personalizados de intenção (termos de pesquisa relevantes) para guiar o aprendizado do algoritmo.

---

## Core Workflows

### Workflow 1: Lançamento de PMax para E-commerce com Otimização de ROAS

Este workflow detalha a configuração e o lançamento de uma campanha PMax focada em maximizar o Retorno Sobre o Investimento em Anúncios (ROAS) para um negócio de e-commerce.

1.  **Validação do Rastreamento de Conversões e Feed de Produtos**:
    *   **Ação**: No Google Ads, navegue até "Ferramentas e Configurações" > "Medição" > "Conversões". Verifique se as ações de conversão de "Compra" estão ativas, com o status "Registrando" e com um valor atribuído (ex: "Usar o valor fornecido pela transação").
    *   **Ação**: Acesse o Google Merchant Center e certifique-se de que o feed de produtos está atualizado, com todos os produtos aprovados e sem avisos críticos. A qualidade dos dados do feed é crucial.
    *   **Exemplo**: Para uma loja de roupas, o feed deve conter títulos descritivos (ex: "Vestido Floral Verão", "Tênis Esportivo Masculino"), preços corretos, links para imagens de alta resolução e categorias de produtos bem definidas.

2.  **Criação da Campanha PMax**:
    *   **Ação**: No Google Ads, clique em `+ Nova Campanha`. Selecione `Vendas` como objetivo. Escolha `Performance Max` como tipo de campanha.
    *   **Ação**: Vincule a conta do Google Merchant Center e selecione o feed de produtos.
    *   **Ação**: Defina o orçamento diário. Para uma fase inicial de aprendizado, considere um orçamento de pelo menos 5x o CPA alvo ou R$150,00/dia.
    *   **Ação**: Escolha a estratégia de lance `Maximizar o valor da conversão` com um `ROAS Alvo`.
    *   **Exemplo**: Orçamento diário de R$250,00. ROAS Alvo de 400% (significa que para cada R$1,00 gasto, espera-se R$4,00 em receita).

3.  **Configuração de Grupos de Ativos de Alta Qualidade**:
    *   **Ação**: Dentro do grupo de ativos, forneça os seguintes criativos:
        *   **Títulos (até 15)**: Varie entre curtos (30 caracteres) e longos (90 caracteres). Use palavras-chave relevantes e benefícios.
        *   **Descrições (até 5)**: Duas curtas (60 caracteres) e três longas (90 caracteres). Destaque diferenciais e chamadas para ação.
        *   **Nomes da Empresa (até 5)**: Variações do nome da sua marca.
        *   **Imagens (até 20)**: Mínimo 3 quadrados (1200x1200), 3 paisagem (1200x628) e 3 retrato (960x1200). Imagens de produtos de alta qualidade e lifestyle.
        *   **Logotipos (até 5)**: Quadrado (1200x1200) e paisagem (1200x300).
        *   **Vídeos (até 5)**: Mínimo 1 vídeo de 15 a 30 segundos. Vídeos curtos de produtos, demonstrações ou depoimentos.
        *   **Call-to-Action (CTA)**: "Comprar Agora", "Ver Produtos", "Saiba Mais".
    *   **Exemplo**:
        *   Títulos: "Ofertas Imperdíveis", "Frete Grátis Brasil", "Novidades da Coleção", "Sapatos Confortáveis", "Até 50% OFF".
        *   Descrições: "Renove seu estilo com nossa coleção exclusiva de sapatos femininos. Conforto e elegância em cada passo.", "Descubra as tendências da moda e aproveite descontos incríveis. Envio rápido e seguro para todo o país."
        *   CTA: "Comprar Agora".

4.  **Adição de Sinais de Público Estratégicos**:
    *   **Ação**: Adicione listas de remarketing (todos os visitantes do site nos últimos 30 dias), listas de clientes (upload de e-mails de compradores anteriores) e segmentos personalizados (pesquisas recentes por "tênis de corrida preto", "vestido de festa azul").
    *   **Exemplo**:
        *   Listas de Remarketing: "Visitantes do Site - Últimos 30 Dias", "Carrinhos Abandonados".
        *   Listas de Clientes: "Compradores Recorrentes", "Newsletter Subscribers".
        *   Segmentos Personalizados: Pessoas que pesquisaram por "sapatilha feminina couro", "bolsa transversal pequena", "promoção calçados".

5.  **Exclusões Essenciais**:
    *   **Ação**: Nas configurações da conta (não da campanha, para exclusões de palavras-chave negativas), ou nas configurações de marca na campanha, adicione palavras-chave negativas para termos irrelevantes e exclusões de marca para proteger sua marca e evitar canibalização de campanhas de Busca existentes.
    *   **Exemplo**: Excluir termos como "vagas de emprego", "reclamações", "grátis" (se não for o caso). Excluir o nome exato da sua marca se você já tem uma campanha de Busca de marca.

### Workflow 2: Otimização Contínua e Expansão de PMax para Geração de Leads

Este workflow foca em como monitorar, otimizar e expandir uma campanha PMax cujo objetivo principal é gerar leads qualificados.

1.  **Análise de Desempenho dos Ativos**:
    *   **Ação**: Após 2-3 semanas de campanha ativa, acesse `Grupos de Ativos` na campanha PMax e clique em `Ver detalhes`. Analise a coluna `Performance` para cada ativo (títulos, descrições, imagens, vídeos).
    *   **Ação**: Identifique os ativos classificados como "Baixo", "Bom" ou "Excelente". Priorize a substituição ou melhoria dos ativos com performance "Baixo".
    *   **Exemplo**: Um título como "Conheça Nossos Serviços" pode ter performance "Baixa". Substitua por algo mais específico e com benefício, como "Otimize Sua Geração de Leads - Agende Demo Grátis". Uma imagem de stock genérica pode ser trocada por uma foto real da equipe ou de um case de sucesso.

2.  **Ajuste de Lances e Orçamento**:
    *   **Ação**: Monitore o CPA (Custo por Aquisição) médio e compare-o com sua meta. Se o CPA estiver muito alto, ajuste o `CPA Alvo` para baixo (ex: de R$150 para R$130). Se o CPA estiver bom e houver espaço para mais volume, aumente o `CPA Alvo` ligeiramente ou aumente o orçamento diário.
    *   **Ação**: Observe o volume de conversões. Se a campanha está limitada pelo orçamento, considere aumentá-lo para capturar mais leads qualificados.
    *   **Exemplo**: Se o CPA Alvo era R$100 e o CPA real está em R$120, ajuste o CPA Alvo para R$95 e monitore. Se o volume de leads é bom, mas a campanha está com "Orçamento Limitado", aumente o orçamento diário de R$200 para R$300.

3.  **Refinamento dos Sinais de Público**:
    *   **Ação**: No relatório de `Insights` da campanha PMax, analise os segmentos de público que estão performando melhor. Use esses insights para criar novos segmentos personalizados ou refinar os existentes.
    *   **Ação**: Adicione novas listas de clientes (ex: clientes que interagiram com um webinar específico) ou segmentos de intenção baseados em termos de pesquisa que geraram leads de alta qualidade em outras campanhas.
    *   **Exemplo**: Se o relatório de insights mostra que "Profissionais de Marketing Digital" são um público de alta conversão, crie um novo segmento personalizado com termos como "ferramentas de automação de marketing", "estratégias de SEO", "geração de leads B2B".

4.  **Expansão e Teste de Criativos e Extensões**:
    *   **Ação**: Crie novos grupos de ativos focando em diferentes propostas de valor ou segmentos de público, se a estrutura de uma única campanha PMax permitir.
    *   **Ação**: Teste diferentes Call-to-Actions (ex: "Baixe o Ebook Grátis", "Solicite uma Demonstração", "Agende Sua Consulta").
    *   **Ação**: Garanta que todas as extensões de anúncio relevantes (sitelinks, frases de destaque, snippets estruturados, formulários de lead) estejam preenchidas e otimizadas para a geração de leads.
    *   **Exemplo**: Para uma empresa de software SaaS, adicione sitelinks como "Recursos do Produto", "Preços", "Suporte 24/7". Use frases de destaque como "Teste Grátis 7 Dias", "Sem Compromisso", "Resultados Comprovados".

5.  **Monitoramento de Termos de Pesquisa e Exclusões**:
    *   **Ação**: Embora a PMax não ofereça relatórios detalhados de termos de pesquisa como as campanhas de Busca, use a seção `Insights` e o relatório de `Termos de Pesquisa` (disponível em algumas contas/regiões) para identificar termos irrelevantes.
    *   **Ação**: Adicione essas palavras-chave como exclusões negativas em nível de conta ou utilize a funcionalidade de exclusão de URL para páginas irrelevantes que a PMax possa estar direcionando tráfego.
    *   **Exemplo**: Se a campanha PMax está gerando tráfego para termos como "software pirata" ou "emprego em [nome da empresa]", adicione esses termos como exclusões negativas na sua lista de palavras-chave negativas da conta.

---

## Templates

### Estrutura de Grupo de Ativos PMax para SaaS

```
Nome do Grupo de Ativos: Software CRM para Pequenas Empresas

URLs Finais:
- https://www.seusite.com.br/crm-pequenas-empresas
- https://www.seusite.com.br/demo-crm

Títulos (Max. 15):
1. CRM para Pequenas Empresas
2. Gerencie Seus Clientes Fácil
3. Aumente Suas Vendas Hoje
4. Teste Grátis CRM SaaS
5. Solução Completa de CRM
6. CRM Intuitivo e Poderoso
7. Automatize Seu Atendimento
8. Otimize Processos de Vendas
9. Comece a Usar Agora!
10. Seu CRM na Nuvem
11. Suporte Especializado
12. Economize Tempo e Dinheiro
13. CRM com Melhor Custo-Benefício
14. Acompanhe Cada Lead
15. Integração Simples

Descrições (Max. 5):
1. Nosso CRM otimiza sua gestão de clientes e vendas. Teste grátis e veja a diferença!
2. Simplifique seu dia a dia com um CRM intuitivo, focado no crescimento da sua pequena empresa.
3. Obtenha insights valiosos, automatize tarefas e melhore o relacionamento com seus clientes.
4. Experimente a plataforma CRM líder para pequenas empresas. Funcionalidades completas.
5. Deixe a burocracia de lado. Nosso CRM foi feito para você focar no que realmente importa: vender.

Nomes da Empresa (Max. 5):
1. Sua Empresa CRM
2. Empresa de Software Ltda.
3. Seu CRM Online
4. Soluções CRM
5. [Nome da Sua Marca]

Imagens (Max. 20):
- 3x Quadradas (1200x1200): Interface do CRM, Pessoas usando notebook, Gráfico de vendas.
- 3x Paisagem (1200x628): Dashboard do CRM, Equipe colaborando, Case de sucesso.
- 3x Retrato (960x1200): Smartphone com app CRM, Benefícios em texto, Depoimento.

Logotipos (Max. 5):
- 1x Quadrado (1200x1200): Logotipo principal.
- 1x Paisagem (1200x300): Logotipo estendido.

Vídeos (Max. 5):
- 1x Vídeo de Demonstração do Produto (15-30s)
- 1x Vídeo de Depoimento de Cliente (15-30s)

Call-to-Action:
- Solicite uma Demonstração
```

### Plano de Exclusão de Marca e Palavra-Chave Negativa (Nível de Conta) para PMax

```
Lista de Exclusões de Marca (para proteger campanhas de marca existentes):
- "[Nome da Sua Marca]"
- "[Seu Dominio.com.br]"
- "[Nome da Marca com Erro de Digitação Comum]"
- "[Nome da Sua Marca] login"
- "[Nome da Sua Marca] suporte"

Lista de Palavras-Chave Negativas Genéricas (Nível de Conta, para evitar tráfego irrelevante em PMax):
- grátis
- gratuito
- emprego
- vagas
- download (se não for o objetivo)
- pirata
- torrent
- reclamações
- reclame aqui
- wiki
- wikipedia
- como fazer (se o objetivo é venda e não tutorial)
- curso (se não for um curso)
- o que é
- pdf

Lista de Exclusões de URL Final (para evitar que PMax direcione tráfego para páginas não transacionais):
- https://www.seusite.com.br/blog/*
- https://www.seusite.com.br/contato
- https://www.seusite.com.br/institucional/*
- https://www.seusite.com.br/termos-de-uso
- https://www.seusite.com.br/politica-de-privacidade
```

---

## Checklist

- [x] Rastreamento de conversões configurado corretamente com valores dinâmicos ou fixos.
- [x] Google Merchant Center vinculado e feed de produtos atualizado (se e-commerce).
- [x] Grupos de ativos preenchidos com mínimo de 5 títulos, 3 descrições, 10 imagens e 1 vídeo.
- [x] Sinais de público relevantes adicionados (listas de remarketing, listas de clientes, segmentos personalizados de intenção).
- [x] ROAS Alvo ou CPA Alvo definido e alinhado ao objetivo de negócio e margens.
- [x] Exclusões de marca e palavras-chave negativas irrelevantes adicionadas em nível de conta.
- [x] Extensões de anúncio (sitelinks, frases de destaque, snippets estruturados) preenchidas e relevantes.
- [x] Orçamento diário adequado para fase de aprendizado (mínimo 5x CPA/dia esperado ou R$150,00).
- [x] URL final expandida desativada OU exclusões de URL configuradas para evitar páginas de destino indesejadas.
- [x] Geo-segmentação e idiomas configurados para o público-alvo correto.

---

## Métricas de Referência

| Métrica               | Benchmark (E-commerce) | Benchmark (Geração de Leads) | Meta (Exemplo E-commerce) | Meta (Exemplo Leads) |
|-----------------------|------------------------|------------------------------|---------------------------|----------------------|
| ROAS (Retorno s/ Ads) | 300% - 500%            | N/A                          | 450%                      | N/A                  |
| CPA (Custo por Aquisição) | R$30 - R$150           | R$80 - R$300                 | R$45                      | R$120                |
| Taxa de Conversão     | 1.5% - 4.0%            | 3.0% - 8.0%                  | 3.0%                      | 6.0%                 |
| Custo por Clique (CPC)| R$0.80 - R$3.50        | R$1.50 - R$5.00              | R$1.20                    | R$2.80               |
| CTR (Taxa de Cliques) | 2.5% - 6.0%            | 2.0% - 5.0%                  | 4.0%                      | 3.5%                 |

---

## Erros Comuns

1.  **Não Utilizar Exclusões de Marca/Palavra-Chave Negativa**: A PMax pode exibir anúncios para termos de marca ou palavras-chave irrelevantes, canibalizando campanhas de Busca existentes ou gerando tráfego de baixa qualidade.
    *   **Como evitar**: Crie uma lista de palavras-chave negativas em nível de conta (acessível em "Ferramentas e Configurações" > "Listas de palavras-chave negativas") com o nome da sua marca e termos genéricos irrelevantes. Adicione também as exclusões de URL para páginas não transacionais.

2.  **Grupos de Ativos Incompletos ou de Baixa Qualidade**: Deixar campos vazios ou usar criativos genéricos/de baixa resolução limita o potencial de performance da PMax, impedindo que o algoritmo encontre as melhores combinações para o público.
    *   **Como evitar**: Preencha todos os campos dos grupos de ativos com uma variedade de títulos, descrições, imagens de alta qualidade e vídeos relevantes. Busque ter pelo menos uma classificação "Boa" ou "Excelente" para a intensidade do grupo de ativos.

3.  **URL Final Expandida Ativa Sem Controle**: A PMax pode enviar tráfego para qualquer URL no seu domínio, incluindo páginas de blog, contato ou institucional, que não são ideais para conversão direta, desperdiçando orçamento.
    *   **Como evitar**: Nas configurações da campanha PMax, em "URL final", desative a opção "Enviar tráfego para URLs adicionais no seu site" ou, preferencialmente, use as exclusões de URL específicas para direcionar o tráfego apenas para páginas de destino otimizadas para conversão.

---

## Dicas Avançadas

1.  **Segmentação de PMax por Tipo de Produto/Serviço**: Em vez de uma única PMax para todo o catálogo, crie campanhas PMax separadas para categorias de produtos ou serviços com ROAS/CPA alvo distintos. Por exemplo, uma PMax para "Produtos de Alta Margem" e outra para "Produtos de Entrada". Isso permite otimização de lances mais granular.

2.  **Estratégia "PMax com Feed + PMax sem Feed"**: Para e-commerce, utilize uma PMax com feed de produtos para cobrir o inventário. Adicionalmente, crie uma PMax *sem* feed (desativando o inventário do Merchant Center) focando em termos de pesquisa mais amplos, geração de leads ou produtos ainda não no feed, com criativos baseados em lifestyle ou benefícios.

3.  **Utilização de Relatórios de Diagnóstico e Insights**: Explore a seção "Insights" da PMax para entender tendências de busca, segmentos de público e como seus ativos estão performando. Use o "Diagnóstico da Campanha" para identificar problemas de entrega, aprovação de anúncios ou status do feed de produtos que impactam a performance.

4.  **Teste de Propostas de Valor em Grupos de Ativos**: Não apenas altere imagens e textos, mas teste diferentes ângulos de venda em grupos de ativos distintos. Por exemplo, um grupo de ativos focando em "Preço Competitivo" versus outro em "Qualidade Premium" ou "Suporte Excepcional" para ver qual ressoa mais com a audiência.

5.  **Otimização do Valor da Conversão e Modelagem de Atribuição**: Para maximizar o valor, certifique-se de que o valor das conversões é o mais preciso possível. Além disso, experimente com diferentes modelos de atribuição (ex: Data-driven) para garantir que a PMax esteja recebendo o crédito justo pelas conversões assistidas e otimizando com base nesses dados.