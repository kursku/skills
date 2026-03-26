---
name: win-loss-analysis
description: "Win Loss Analysis — Skill especializada para analisar e otimizar estratégias de vendas e produto com base em feedback de oportunidades ganhas e perdidas."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
risk: safe
---

# Win Loss Analysis

Esta skill capacita o Claude a conduzir e analisar processos de Win Loss, identificando padrões de sucesso e insucesso em vendas para otimizar estratégias comerciais e de produto de forma prática.

---

## Keywords

*   Win Loss Analysis
*   Análise de Perda
*   Análise de Ganho
*   Feedback de Clientes
*   Ciclo de Vendas
*   Decisão de Compra
*   Motivos de Perda
*   Motivos de Ganho
*   Proposta de Valor
*   Inteligência Competitiva
*   Otimização de ICP
*   Customer Insights

---

## Quick Start

1.  Filtrar no CRM 5 oportunidades fechadas (3 perdidas, 2 ganhas) dos últimos 45 dias com ticket médio anual acima de R$60k, excluindo perdas por "Não Respondeu".
2.  Agendar entrevistas de 25-30 minutos com os decisores-chave de cada oportunidade, utilizando um convite focado em feedback para melhoria.
3.  Transcrever as entrevistas e categorizar os comentários em temas como "Preço", "Produto", "Vendas", "Concorrência", "Necessidade".
4.  Consolidar os dados e apresentar os 3 principais fatores de perda e os 3 principais fatores de ganho para a liderança comercial e de produto.

---

## Core Workflows

### Workflow 1: Análise de Perdas para Refinamento de Estratégia de Produto e Vendas

Este workflow detalha a metodologia para investigar por que oportunidades de alto valor são perdidas, gerando insights acionáveis para o desenvolvimento de produto e o processo de vendas.

1.  **Seleção Estratégica de Oportunidades Perdidas**: Filtrar no sistema CRM todas as oportunidades com status "Perdido" nos últimos 90 dias que:
    *   Possuíam um valor de contrato anual (ARR) superior a R$50.000.
    *   Tiveram pelo menos 3 interações qualificadas com a equipe de vendas.
    *   Não foram perdidas por "Não Respondeu" ou "Contato Inválido".
    *   Priorizar perdas para concorrentes diretos ou perdas por "No Decision" em segmentos estratégicos.
    *   *Exemplo*: Selecionar 8 oportunidades de SaaS B2B com ARR médio de R$75.000, onde 5 foram perdidas para o Concorrente X e 3 por "Decisão Adiada".
2.  **Identificação e Contato com Decisores-Chave**: Para cada oportunidade, localizar o contato que teve o maior poder de decisão (e.g., Diretor de TI, C-Level, Gerente de Projeto Sênior). Enviar um e-mail personalizado (não do vendedor original) explicando o propósito da pesquisa e oferecendo um pequeno incentivo.
    *   *Exemplo*: "Olá [Nome], sou [Seu Nome] da equipe de insights de mercado da [Sua Empresa]. Gostaríamos de entender sua perspectiva sobre a avaliação de [Nossa Solução] em relação às suas necessidades, para aprimorarmos nosso produto e serviço. Sua opinião é valiosa e nos ajudaria muito. Poderia dedicar 25 minutos para uma breve conversa por vídeo na próxima semana? Como agradecimento, oferecemos um voucher de R$150 para sua próxima refeição."
3.  **Condução de Entrevistas Imparciais**: Utilizar o "Script de Entrevista Win Loss (Perda)" fornecido nesta skill. O entrevistador deve ser um membro da equipe de pesquisa, produto ou marketing, nunca o vendedor que atendeu a oportunidade. Focar em perguntas abertas para entender a percepção do valor, a experiência com a equipe de vendas, a competitividade da oferta e os critérios de decisão. Gravar a chamada (com consentimento).
    *   *Exemplo de Pergunta*: "Quais foram os fatores mais importantes que sua equipe considerou ao tomar a decisão final, e como nossa solução se alinhou a esses fatores, ou não?"
4.  **Análise e Categorização Detalhada dos Insights**: Transcrever as entrevistas. Criar uma taxonomia de motivos de perda:
    *   **Produto**: #FuncionalidadeFaltante:[NomeRecurso], #UsabilidadeComplexa, #RoadmapInadequado
    *   **Preço**: #PrecoAlto, #CustoBeneficioInferior, #ModeloLicenciamentoInflexivel
    *   **Vendas**: #ProcessoVendasLento, #FaltaConhecimentoSetor, #FaltaAcompanhamento
    *   **Concorrência**: #ConcorrenteX_MelhorUX, #ConcorrenteY_MaisRecursos, #ConcorrenteZ_MelhorPreco
    *   **Outros**: #NoDecision_FaltaUrgencia, #MudancaPrioridadeInterna
    *   Quantificar a frequência de cada motivo e o valor total das oportunidades associadas.
5.  **Geração de Relatório e Recomendações Acionáveis**: Compilar os dados no "Resumo Executivo Win Loss Semanal". Apresentar os 3-5 principais motivos de perda, acompanhados de exemplos de depoimentos e sugestões de ações concretas para as equipes de Produto, Vendas e Marketing.
    *   *Exemplo de Recomendação*: Se "#PrecoAlto" e "#CustoBeneficioInferior" forem recorrentes (30% das perdas de alto valor), o time de produto pode explorar uma versão "Lite" com menos funcionalidades ou o marketing pode desenvolver um material que demonstre o ROI de longo prazo da solução. Se "#FuncionalidadeFaltante:RelatoriosCustomizados" aparecer em 25% das perdas, a equipe de produto deve avaliar a inclusão no próximo quarter.

### Workflow 2: Análise de Ganhos para Otimização de ICP e Mensagens de Marketing

Este workflow foca em entender os drivers de sucesso para replicar os resultados e refinar o Perfil de Cliente Ideal (ICP) e a comunicação de valor.

1.  **Seleção de Oportunidades Ganhas de Alto Valor**: Filtrar no CRM as 5-7 maiores oportunidades fechadas como "Ganhas" nos últimos 60 dias. Priorizar clientes que representam o "cliente ideal" (alto potencial de LTV, bom fit com a solução, segmento estratégico).
    *   *Exemplo*: Selecionar 6 clientes recém-onboardados de grande porte (faturamento > R$100 milhões/ano) no setor de manufatura, que adquiriram a versão Enterprise da solução.
2.  **Identificação do Campeão Interno e Contato para Feedback**: Entrar em contato com o Customer Success Manager (CSM) ou o Account Executive (AE) para identificar o principal defensor ou decisor-chave que impulsionou a compra. Enviar um convite de entrevista com foco em entender o sucesso e a experiência de compra.
    *   *Exemplo*: "Olá [Nome], sou [Seu Nome] e faço parte da equipe de insights da [Sua Empresa]. Parabéns por sua recente implementação de [Nossa Solução]! Gostaríamos muito de entender o que mais o atraiu em nossa solução e como foi sua jornada de compra, para que possamos continuar a ajudar empresas como a sua de forma ainda mais eficaz. Poderíamos agendar 25 minutos para uma conversa?"
3.  **Condução de Entrevistas Focadas em Valor**: Utilizar um roteiro de entrevista que explore:
    *   Qual problema específico nossa solução resolveu.
    *   Quais foram os 2-3 diferenciais percebidos em relação aos concorrentes.
    *   Como a equipe de vendas contribuiu para a decisão.
    *   Os critérios internos que levaram à escolha.
    *   *Exemplo de Pergunta*: "Em retrospecto, qual funcionalidade ou benefício de [Nossa Solução] foi o fator decisivo para a sua escolha, e por quê?"
4.  **Análise de Padrões de Sucesso e Geração de Insights**: Categorizar as respostas em temas como:
    *   **Produto**: #ResolucaoProblemaX, #FacilidadeUso, #RecursoUnicoY, #IntegracaoZ
    *   **Vendas**: #ConsultoriaEspecializada, #AgilidadeProposta, #ConfiancaEquipe
    *   **Valor**: #ROIClaro, #ReducaoCustosOperacionais, #AumentoProdutividade
    *   **Concorrência**: #MelhorQueConcorrenteA, #UnicoComSolucaoB
    *   Quantificar a prevalência de cada motivo e correlacionar com o perfil do cliente (setor, tamanho, maturidade digital).
5.  **Otimização de ICP, Proposta de Valor e Mensagens de Marketing**: Com base nos insights, ajustar a descrição do Perfil de Cliente Ideal (ICP). Refinar a proposta de valor e as mensagens de marketing para destacar os diferenciais mais impactantes e os problemas que a solução resolve de forma mais eficaz.
    *   *Exemplo de Otimização*: Se #ConsultoriaEspecializada e #ResolucaoProblemaX (para o setor financeiro) forem os principais motivos de ganho, o marketing deve criar estudos de caso específicos para o setor financeiro, e o treinamento de vendas deve focar em como posicionar a equipe como consultores especializados nesse segmento. O ICP pode ser refinado para "Empresas do setor financeiro com >R$200 milhões de faturamento anual, buscando otimização de processos de compliance".

---

## Templates

### Script de Entrevista Win Loss (Perda)

```
Assunto: Feedback sobre sua avaliação de [Nossa Solução]

Prezado(a) [Nome do Contato],

Meu nome é [Seu Nome] e faço parte da equipe de pesquisa de mercado da [Sua Empresa]. Soubemos que sua empresa, [Nome da Empresa do Contato], avaliou recentemente nossa solução [Nome da Solução] para [Problema Principal que a Solução Resolve].

Gostaríamos muito de entender sua perspectiva sobre o processo de avaliação e a decisão final. Seu feedback é crucial para aprimorarmos continuamente nossa oferta e o atendimento. Não há intenção de reverter sua decisão, apenas aprender.

Seria possível agendarmos uma breve conversa de 25-30 minutos na próxima semana? Sua opinião é extremamente valiosa para nós. Como agradecimento, oferecemos um voucher de R$150 da [Empresa de Vouchers].

Atenciosamente,
[Seu Nome]
[Seu Cargo, e.g., Analista de Inteligência de Mercado]

---

Roteiro da Entrevista Win Loss (30 min):

1.  **Introdução (2 min)**
    *   Agradecer o tempo e reforçar o objetivo: coletar feedback para melhoria, sem intenção de reverter a decisão.
    *   Garantir confidencialidade das informações e que não será usado para vendas.
2.  **Contexto da Busca (5 min)**
    *   "Qual problema principal sua empresa estava buscando resolver ao considerar uma nova solução como a nossa?"
    *   "Quais eram os 2-3 objetivos cruciais que vocês tinham em mente para essa nova solução?"
    *   "Quem mais esteve envolvido no processo de decisão (stakeholders) e quais eram os seus papéis e prioridades?"
3.  **Avaliação da Nossa Solução (10 min)**
    *   "Como nossa solução [Nome da Solução] se alinhou (ou não se alinhou) às suas necessidades específicas?"
    *   "Quais aspectos da nossa proposta de valor, produto ou demonstração mais o impressionaram positivamente?"
    *   "Quais foram os pontos fracos ou áreas de preocupação que surgiram durante sua avaliação da nossa solução?"
    *   "Como você avaliaria a experiência de trabalhar com nossa equipe de vendas? Houve algo que poderia ter sido melhor?"
4.  **Avaliação de Alternativas e Decisão (8 min)**
    *   "Quais outras soluções ou alternativas (incluindo a opção de 'não fazer nada' ou solução interna) vocês consideraram seriamente?"
    *   "O que fez com que a solução escolhida (ou a decisão de não prosseguir) fosse a melhor opção para sua empresa, considerando todos os fatores?"
    *   "Como nossa solução se comparou aos concorrentes em termos de [Preço/Custo-benefício, Funcionalidades, Suporte, Facilidade de Uso ou Implementação]?"
5.  **Fator Decisivo e Sugestões (5 min)**
    *   "Se houvesse um único fator que selou a decisão final, qual seria?"
    *   "Se pudéssemos ter feito uma coisa diferente para ganhar o seu negócio, qual seria?"
    *   "Você teria alguma outra sugestão para nós, baseada na sua experiência?"
6.  **Encerramento (1 min)**
    *   Agradecer novamente pelo tempo e feedback valioso.
    *   Oferecer-se para responder a quaisquer perguntas.
```

### Resumo Executivo Win Loss Semanal

```
Relatório Win Loss - Semana de 2024-11-04 a 2024-11-08

**Entrevistas Realizadas:** 6 (3 Perdas, 3 Ganhos)
**Oportunidades Analisadas (Valor Médio):** R$ 72.000 ARR

---

**Principais Motivos de PERDA (Top 3):**

1.  **Custo-Benefício Percebido (50% das perdas, totalizando R$210k ARR)**
    *   *Exemplo de Feedback*: "A solução do concorrente X, embora com menos funcionalidades, tinha um preço 30% menor e parecia atender ao nosso requisito mínimo, tornando o investimento de vocês difícil de justificar para a diretoria."
    *   *Sugestão de Ação*:
        *   **Produto**: Desenvolver uma versão "Lite" da solução ou pacotes mais flexíveis.
        *   **Marketing**: Criar estudos de caso e materiais focados em ROI de longo prazo e valor agregado, não apenas no preço inicial.
        *   **Vendas**: Treinamento para justificar o valor em relação ao custo total de propriedade (TCO).

2.  **Integração com ERP Específico (35% das perdas, totalizando R$150k ARR)**
    *   *Exemplo de Feedback*: "Precisávamos de uma integração nativa e robusta com o SAP Business One, e a solução de vocês exigiria um desenvolvimento customizado dispendioso e demorado, enquanto o concorrente Y já a oferecia."
    *   *Sugestão de Ação*:
        *   **Produto**: Avaliar a prioridade de desenvolver integração nativa com SAP Business One no roadmap do próximo ano.
        *   **Vendas**: Desenvolver uma alternativa de integração via API com parceiro ou processo manual claro para as interações imediatas.

3.  **Processo de Vendas Lento (15% das perdas, totalizando R$60k ARR)**
    *   *Exemplo de Feedback*: "Adoramos a solução, mas o processo para obter a proposta final e o contrato foi muito lento. Precisávamos de agilidade e o concorrente entregou tudo em 3 dias."
    *   *Sugestão de Ação*:
        *   **Vendas**: Revisar o SLA interno para emissão de propostas e contratos. Otimizar a comunicação entre AE e equipe de pré-vendas/jurídico.

---

**Principais Motivos de GANHO (Top 3):**

1.  **Expertise e Consultoria da Equipe de Vendas (40%