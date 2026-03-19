---
name: client-reporting
description: "Client Reporting — Skill especializada para client reporting"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Client Reporting

Esta skill capacita o Claude a gerar relatórios de performance consultiva, analisar dados de projetos e comunicar valor de forma estratégica para clientes.

---

## Keywords

Relatório de Performance, ROI do Cliente, Dashboard de Projeto, Health Score do Cliente, SLA de Relatórios, Feedback do Cliente, Análise de Valor, Apresentação de Resultados, Métricas Consultivas, Comunicação Estratégica, Gestão de Expectativas, Otimização Contínua.

---

## Quick Start

1.  **Coletar Dados Brutos**: Extrair dados de performance (ex: Google Analytics, CRM, ERP financeiro) referentes ao período do relatório para o cliente "E-commerce Essencial".
2.  **Consolidar e Analisar**: Organizar os dados em uma planilha mestra (`Relatorio_EE_JUN2024.xlsx`), identificando tendências, anomalias e oportunidades para o cliente.
3.  **Elaborar Visualizações Chave**: Criar gráficos de linha para tendências de vendas, gráficos de barras para performance por canal e tabelas comparativas de custos/receitas.
4.  **Redigir Narrativa de Valor**: Construir um resumo executivo que destaque o ROI, o impacto nos objetivos do cliente e as recomendações estratégicas.
5.  **Validar e Apresentar**: Revisar o relatório com a equipe interna e agendar a reunião de apresentação, com foco em dialogar sobre os resultados e próximos passos.

---

## Core Workflows

### Workflow 1: Elaboração do Relatório Mensal de Performance para Cliente de Marketing Digital

Este workflow detalha a criação de um relatório mensal abrangente para um cliente de marketing digital, focando na demonstração de valor e no alinhamento com os objetivos de negócio.

**Cenário**: Cliente "MegaStore Esportiva", objetivo: Aumentar vendas online e otimizar custo de aquisição de clientes (CAC).

1.  **Extração de Dados Multiplataforma (Dia 1-3 do mês seguinte)**
    *   **Google Analytics 4 (GA4)**: Extrair dados de tráfego (orgânico, pago, direto), sessões, usuários, taxa de conversão, receita e eventos de conversão (ex: "compra_efetuada", "adicionar_carrinho"). Período: Mês anterior completo.
        *   *Exemplo*: Exportar relatório "Aquisição de Tráfego" e "Monetização > Visão geral" do GA4 para CSV.
    *   **Google Ads**: Coletar métricas de campanha (cliques, impressões, custo, conversões, ROAS) para todas as campanhas ativas.
        *   *Exemplo*: Baixar relatório de "Campanhas" com segmentação por "Mês" e "Conversões" detalhadas.
    *   **Meta Ads (Facebook/Instagram)**: Obter dados de performance de campanhas (alcance, frequência, custo por resultado, compras, valor de compra).
        *   *Exemplo*: Exportar dados do "Gerenciador de Anúncios" para as campanhas de vendas e branding.
    *   **Ferramenta de SEO (ex: SEMrush, Ahrefs)**: Extrair dados de posicionamento de palavras-chave, tráfego orgânico estimado e backlinks adquiridos.
        *   *Exemplo*: Coletar relatório de "Posições" e "Visão Geral do Domínio" para acompanhar a evolução do SEO.

2.  **Consolidação e Limpeza de Dados (Dia 3-4)**
    *   Criar uma planilha mestra no Google Sheets (`Relatorio_MegaStore_JUL2024.xlsx`) com abas para cada fonte de dados.
    *   Padronizar nomes de colunas e formatos.
    *   Combinar dados de custo de mídia e receita total para calcular o ROAS geral e o CAC.
        *   *Exemplo*: Na aba 'Consolidado', ter colunas como 'Canal', 'Investimento Total (R$)', 'Receita Total (R$)', 'Transações', 'CAC (R$)', 'ROAS'.
        *   *Cálculo de Exemplo*: Se o investimento total em Google Ads foi R$ 15.000 e gerou R$ 45.000 em receita, o ROAS de Google Ads é 3x. Se gerou 150 vendas, o CAC de Google Ads é R$ 100.

3.  **Análise e Geração de Insights (Dia 4-5)**
    *   Identificar tendências significativas:
        *   **Crescimento**: Aumento de 15% no tráfego orgânico, resultando em 10% mais vendas.
        *   **Quedas**: Diminuição de 8% no ROAS de campanhas de display, indicando fadiga criativa.
        *   **Anomalias**: Pico inesperado de tráfego direto devido a menção em blog influente.
    *   Cruzar dados para encontrar correlações:
        *   *Exemplo*: Concluir que a otimização de palavras-chave de cauda longa no blog aumentou o tráfego orgânico e, consequentemente, as conversões.
    *   Formular insights acionáveis que se conectem diretamente aos objetivos do cliente.
        *   *Exemplo*: "A queda no ROAS de display exige uma renovação imediata dos criativos para reverter a tendência e manter a eficiência do investimento."

4.  **Criação de Visualizações e Dashboard (Dia 5-6)**
    *   Utilizar ferramentas como Looker Studio (antigo Google Data Studio) ou Power BI para criar um dashboard interativo.
    *   **Gráficos Essenciais**:
        *   Gráfico de linha: Tendência de Receita Mensal (últimos 12 meses).
        *   Gráfico de barras: Comparativo de ROAS por Canal (Google Ads, Meta Ads).
        *   Gráfico de pizza: Distribuição de Tráfego por Canal.
        *   Tabela: KPIs principais (Receita, Investimento, ROAS, CAC, Vendas) com comparação mês a mês e variação percentual.
        *   *Exemplo*: Um gráfico de linha mostrando a Receita de R$ 80.000 (Abril), R$ 95.000 (Maio), R$ 110.000 (Junho), com uma projeção para Julho.

5.  **Redação da Narrativa e Recomendações (Dia 6-7)**
    *   Elaborar o Resumo Executivo, destacando os principais resultados e o impacto direto no negócio.
        *   *Exemplo de Resumo*: "No mês de Junho, a MegaStore Esportiva alcançou um ROAS geral de 3.2x, superando a meta de 3.0x, impulsionado por um aumento de 18% nas vendas via tráfego orgânico. O CAC foi otimizado para R$ 98,00, mantendo a lucratividade. Identificamos, no entanto, a necessidade de renovação criativa em campanhas de display para sustentar a performance."
    *   Detalhar as seções de "Destaques do Mês", "Análise de Canais" e "Próximos Passos/Recomendações".
        *   *Exemplo de Recomendação*: "Lançar 3 novos conjuntos de criativos para campanhas de display na próxima semana, com foco em vídeos curtos e depoimentos de clientes, para testar a performance e otimizar o ROAS."

6.  **Revisão Interna e Preparação para Apresentação (Dia 7-8)**
    *   O Gerente de Projeto e um especialista em dados revisam o relatório para garantir precisão e clareza.
    *   Preparar slides de apresentação com os pontos chave e a narrativa.
    *   Agendar a reunião com o cliente para o dia 10-12 do mês.

### Workflow 2: Condução da Reunião Estratégica de Reporte e Alinhamento

Este workflow foca na etapa crítica de apresentação do relatório, coleta de feedback e planejamento do próximo ciclo, garantindo que o valor percebido pelo cliente seja maximizado.

**Cenário**: Cliente "Serviços Financeiros Alpha", objetivo: Otimizar processos internos e reduzir custos operacionais.

1.  **Preparação da Agenda Focada em Valor (1 dia antes da reunião)**
    *   Estruturar uma agenda clara e focada nos objetivos estratégicos do cliente, não apenas nos números.
    *   **Itens da Agenda**:
        *   **Revisão do Último Período (15 min)**: Apresentar resultados chave do relatório (economia de R$ 50.000, redução de 15% no tempo de processamento de solicitações).
        *   **Análise de Desafios e Oportunidades (10 min)**: Discutir gargalos identificados (ex: 20% das solicitações ainda exigem intervenção manual) e novas possibilidades.
        *   **Plano de Ação para o Próximo Ciclo (15 min)**: Apresentar as propostas da consultoria (ex: automação de 30% das aprovações de crédito).
        *   **Discussão e Feedback (10 min)**: Abrir para perguntas e coletar percepções do cliente.
        *   **Próximos Passos e Responsabilidades (5 min)**: Definir ações concretas e prazos.
    *   Enviar a agenda prévia ao cliente, permitindo que ele se prepare e adicione tópicos relevantes.

2.  **Condução da Reunião (Durante a reunião)**
    *   **Início Estratégico**: Começar com o "Porquê" e o "Impacto" para o cliente, não com a metodologia.
        *   *Exemplo*: "Na reunião de hoje, vamos revisar como nossa parceria resultou em uma economia de R$ 50.000 no último trimestre e como podemos ampliar esse impacto para o próximo período."
    *   **Apresentação dos Dados com Narrativa**: Utilizar o dashboard interativo, mas sempre contextualizando os números com a história de sucesso ou o desafio superado.
        *   *Exemplo*: Em vez de "O tempo médio de processamento caiu de 7 para 5 dias", dizer: "A otimização de processos que implementamos reduziu o tempo médio de processamento de solicitações de 7 para 5 dias, liberando sua equipe para focar em atividades de maior valor estratégico."
    *   **Foco nos Insights e Recomendações**: Passar mais tempo discutindo o "o quê fazer" e "porquê" do que apenas o "o quê aconteceu".
        *   *Exemplo*: "Observamos que 20% das solicitações ainda demandam validação manual. Nossa recomendação é implementar um sistema de automação de regras para reduzir esse índice para 5% no próximo mês, economizando cerca de 40 horas de trabalho da equipe."

3.  **Coleta Ativa de Feedback (Durante a reunião)**
    *   Fazer perguntas abertas para entender a percepção do cliente.
        *   *Exemplo*: "Dos resultados apresentados, qual teve o maior impacto para a equipe de vocês?" ou "Há alguma métrica que gostariam de ver com mais profundidade no próximo relatório?"
    *   Anotar os pontos de feedback, mesmo que sejam apenas percepções ou sugestões. Isso demonstra engajamento e valorização da opinião do cliente.

4.  **Definição de Próximos Passos e Ações (Final da reunião)**
    *   Resumir claramente as ações acordadas, quem é o responsável e o prazo para cada uma.
        *   *Exemplo*: "Ação 1: Consultoria enviará proposta detalhada para automação de validação até 25/07. Responsável: [Nome do Consultor]. Ação 2: Cliente fornecerá acesso ao sistema X para análise de integração até 28/07. Responsável: [Nome do Contato do Cliente]."
    *   Reafirmar o compromisso com os objetivos do cliente.

5.  **Follow-up Pós-Reunião (Até 24h após a reunião)**
    *   Enviar um e-mail de agradecimento com a ata da reunião, o relatório em PDF e quaisquer materiais complementares discutidos.
    *   Garantir que as ações definidas sejam registradas no sistema de gestão de projetos (ex: Asana, Trello) e atribuídas aos responsáveis.

---

## Templates

### Template de Resumo Executivo para Relatório Mensal

```
RELATÓRIO DE PERFORMANCE - RESUMO EXECUTIVO
Período: Junho/2024
Cliente: Soluções Digitais Inovadoras Ltda.
Gerente de Projeto: Ana Paula Mendes

**OBJETIVO PRINCIPAL:** Aumentar a geração de leads qualificados e otimizar o custo por lead (CPL).

**DESTAQUES DO MÊS:**
*   **Aumento de Leads Qualificados**: Geração de **320 novos leads**, um crescimento de **18%** em relação ao mês anterior (meta: +15%).
*   **Otimização do CPL**: Redução do Custo Por Lead para **R$ 35,00**, uma melhoria de **10%** (meta: -8%).
*   **Engajamento de Conteúdo**: Artigo "Tendências de IA para Negócios" gerou **85 leads** via download de e-book, superando expectativas.
*   **Performance de Campanhas de Busca**: Campanhas de Google Ads focadas em termos de alta intenção apresentaram um **ROAS de 4.1x**, contribuindo significativamente para a receita.

**ANÁLISE E INSIGHTS:**
A estratégia de conteúdo, combinada com a segmentação refinada em Google Ads, foi o principal motor dos resultados positivos. O aumento de 18% nos leads qualificados demonstra o alinhamento efetivo entre conteúdo e intenção de busca. A otimização contínua de lances e palavras-chave nas campanhas de busca permitiu a redução do CPL, tornando o investimento mais eficiente. Identificamos uma oportunidade para replicar o sucesso do artigo sobre IA em outros pilares de conteúdo.

**DESAFIOS:**
*   **Performance de Campanhas de Display**: O CPL em campanhas de display aumentou 15% (para R$ 52,00), indicando fadiga de criativos e segmentação menos eficiente.

**PRÓXIMOS PASSOS E RECOMENDAÇÕES:**
1.  **Renovação Criativa**: Lançar **5 novos conjuntos de anúncios** para campanhas de display até 15/07, com foco em vídeos curtos e depoimentos.
2.  **Otimização de Conteúdo**: Desenvolver **2 novos e-books** sobre temas de "Automação de Marketing" e "Cibersegurança" para replicar o sucesso do artigo de IA.
3.  **Análise de Landing Pages**: Conduzir um **teste A/B** em 3 landing pages de alta performance para buscar um aumento de 5% na taxa de conversão até 31/07.

**CONCLUSÃO:**
Junho foi um mês de forte crescimento e otimização para a Soluções Digitais Inovadoras, com resultados consistentes na geração de leads qualificados e eficiência de custos. Nosso foco para o próximo ciclo será manter este momentum, abordando os desafios identificados e explorando novas oportunidades de crescimento.
```

### Template de Ata de Reunião de Reporte (Pós-Reunião)

```
ATA DE REUNIÃO DE REPORTE E ALINHAMENTO
Data: 10 de Julho de 2024
Horário: 10:00 - 11:00
Plataforma: Google Meet
Cliente: Consultoria RH Inteligente S.A.
Gerente de Projeto (Consultoria): Lucas Pereira
Participantes (Consultoria): Lucas Pereira, Mariana Costa (Especialista em Dados)
Participantes (Cliente): Dr. Ricardo Silva (CEO), Dra. Patrícia Gomes (Gerente de RH)

**1. TÓPICOS DISCUTIDOS:**
*   **Revisão de Performance do Q2/2024**: Apresentação dos resultados do projeto "Otimização do Processo Seletivo", destacando a redução de 25% no tempo de contratação e 15% nos custos de recrutamento.
*   **Análise de Feedback dos Candidatos**: Discussão sobre o aumento de 10% no índice de satisfação dos candidatos, conforme pesquisa pós-entrevista.
*   **Desafios Atuais**: Identificação de um gargalo na etapa de "onboarding digital", onde 12% dos novos colaboradores demoram a completar a documentação inicial.
*   **Propostas para o Próximo Ciclo**: Apresentação de um plano para automatizar 70% da fase de onboarding digital e implementar um sistema de acompanhamento de performance pós-contratação.

**2. DECISÕES CHAVE:**
*   **Aprovação do Plano de Onboarding Digital**: Cliente aprovou a proposta para otimização do onboarding digital para o Q3.
*   **Priorização de Módulos**: Decidido priorizar a automação de documentação e treinamentos iniciais na primeira fase do projeto de onboarding.
*   **Benchmarking Adicional**: Cliente solicitou um estudo de benchmarking sobre as melhores práticas de acompanhamento de performance de novos colaboradores em empresas de tecnologia.

**3. AÇÕES DEFINIDAS:**
| Item | Descrição da Ação | Responsável | Prazo |
|------|-------------------|-------------|-------|
| 3.1  | Enviar proposta detalhada de "Automação de Onboarding Digital" (Fase 1) | Lucas Pereira (Consultoria) | 15/07/2024 |
| 3.2  | Fornecer acesso à plataforma de RH atual para análise de integração | Dra. Patrícia Gomes (Cliente) | 17/07/2024 |
| 3.3  | Iniciar estudo de benchmarking para "Acompanhamento de Performance Pós-Contratação" | Mariana Costa (Consultoria) | 26/07/2024 |
| 3.4  | Agendar próxima reunião de alinhamento para apresentar o estudo de benchmarking | Lucas Pereira (Consultoria) | 02/08/2024 |

**4. PRÓXIMOS PASSOS:**
*   Foco na implementação da Fase 1 do projeto de Automação de Onboarding Digital.
*   Preparação do estudo de benchmarking para discussão na próxima reunião.

**5. OBSERVAÇÕES:**
*   Cliente expressou satisfação com a redução de custos e tempo de contratação, reforçando o valor percebido da consultoria.
*   Foi levantada a possibilidade de expandir a parceria para otimização de "Employer Branding" no Q4.

**Assinaturas:**
_________________________
Lucas Pereira
Gerente de Projeto - Consultoria RH Inteligente S.A.

_________________________
Dr. Ricardo Silva
CEO - Consultoria RH Inteligente S.A.
```

---

## Checklist

-   [x] Dados brutos de todas as fontes extraídos e verificados para consistência e integridade.
-   [x] Métricas e KPIs do relatório alinhadas diretamente aos objetivos estratégicos e de negócio do cliente.
-   [x] Relatório contém um resumo executivo claro, focado em valor e com narrativa envolvente.
-   [x] Visualizações de dados são intuitivas, limpas, e sem ruído, facilitando a compreensão.
-   [x] Recomendações e próximos passos são acionáveis, específicos e baseados em evidências.
-   [x] Relatório revisado por um par ou gerente para garantir precisão técnica e clareza da mensagem.
-   [x] Material de apresentação (slides, dashboard interativo) preparado, testado e adaptado ao público-alvo.
-   [x] Próximos passos e responsabilidades definidos e comunicados claramente no follow-up.
-   [x] Feedback do cliente coletado ativamente e incorporado na estratégia de relatórios futuros.
-   [x] O SLA de entrega do relatório foi respeitado e o cliente foi notificado da disponibilidade.
-   [x] O relatório inclui uma seção de "desafios" ou "oportunidades de melhoria" de forma construtiva.
-   [x] Os dados são contextualizados com comparações (mês a mês, ano a ano, metas) para demonstrar progresso.

---

## Métricas de Referência

| Métrica                         | Benchmark (Consultoria) | Meta (Exemplo)       |
|:--------------------------------|:------------------------|:---------------------|
| Net Promoter Score (NPS) Cliente| 7-8 (Bom); 9-10 (Excl.) | > 8                  |
| Client Churn Rate (Anual)       | < 5%                    | < 3%                 |
| ROAS (Retorno sobre Gasto Anúncios)| 2x-4x (Varia por setor) | > 3.5x               |
| Margem de Lucro por Projeto     | 20%-35%                 | > 28%                |
| Tempo Médio de Entrega de Relatório | 5-7 dias úteis (mês seg.) | 5 dias úteis (mês seg.) |
| Health Score do Cliente         | > 75 (Saudável)         | > 80                 |

---

## Erros Comuns

1.  **Excesso de Dados Brutos sem Contexto**: Apresentar tabelas gigantescas ou planilhas inteiras de dados técnicos sem uma análise ou resumo executivo claro.
    *   **Como evitar**: Focar em KPIs e insights chave que respondam diretamente aos objetivos do cliente. Utilize visualizações (gráficos, dashboards) para resumir os dados e reserve os detalhes técnicos para apêndices ou discussões aprofundadas on-demand.
    *   *Exemplo*: Em vez de mostrar todas as linhas de um extrato de Google Analytics, apresente um gráfico de linha da tendência de tráfego orgânico e um KPI de taxa de conversão, explicando o que esses números significam para o negócio do cliente.
2.  **Narrativa Focada no "O Quê Foi Feito" em vez do "Qual o Impacto"**: Descrever as atividades realizadas pela consultoria sem conectar explicit