---
name: vendor-management
description: "Vendor Management — Skill especializada para vendor management"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Vendor Management

Esta skill capacita o Claude a atuar como um especialista em Vendor Management, fornecendo orientação prática e ferramentas para otimizar a seleção, contratação, gestão e avaliação de fornecedores estratégicos.

---

## Keywords

Gestão de Fornecedores, SRM, Contratos de Fornecimento, SLA, KPIs de Fornecedor, Due Diligence, Avaliação de Desempenho, Negociação de Contratos, Risco de Fornecedor, Onboarding de Fornecedor, Offboarding de Fornecedor, Compliance de Fornecedores.

---

## Quick Start

1.  **Avaliar Fornecedor Crítico**: Inicie a avaliação de um fornecedor de infraestrutura de cloud, solicitando os relatórios de uptime e latência dos últimos 6 meses e verificando sua certificação ISO 27001.
2.  **Gerar RFI para Novo Serviço**: Crie um modelo de RFI para um novo serviço de facilities (limpeza e manutenção), focando em experiência da equipe, planos de contingência e adesão a normas de segurança do trabalho.
3.  **Analisar Desvio de Orçamento**: Analise o histórico de pagamentos de fornecedores de software que apresentaram desvio acima de 7% do valor contratado nos últimos três meses, investigando as causas dos aditivos.
4.  **Criar Plano de Mitigação**: Desenvolva um plano de mitigação para o fornecedor de logística X, com base na queda de 15% no KPI de On-Time Delivery (OTD) identificada no último scorecard mensal, propondo reuniões semanais de acompanhamento e revisão de rotas.
5.  **Revisar Cláusula Contratual**: Revise a cláusula de penalidades de um contrato de telecomunicações, garantindo que as multas por indisponibilidade de serviço sejam proporcionais ao impacto no negócio e claramente definidas.

---

## Core Workflows

### Workflow 1: Seleção e Onboarding de Novos Fornecedores Estratégicos

Este workflow detalha o processo para identificar, avaliar, contratar e integrar fornecedores que impactam diretamente as operações ou a estratégia da empresa.

1.  **Definição de Requisitos Detalhados**:
    *   **Ação**: Elabore um documento de requisitos técnicos e de negócio específico para o serviço ou produto.
    *   **Exemplo Prático**: Para a contratação de um provedor de SaaS para gestão de RH, especifique: "Plataforma deve suportar 500 usuários ativos simultaneamente; integração via API RESTful com o ERP (SAP S/4HANA); conformidade com LGPD; certificação SOC 2 Tipo II; módulo de folha de pagamento para Brasil; suporte 24/7 com tempo de resposta máximo de 2 horas para incidentes críticos."
2.  **Due Diligence e Análise de Risco Abrangente**:
    *   **Ação**: Conduza uma investigação aprofundada sobre a saúde financeira, conformidade legal, reputação e capacidade operacional dos potenciais fornecedores.
    *   **Exemplo Prático**: Para um fornecedor de matéria-prima crítica, solicite: "demonstrações financeiras auditadas dos últimos 3 anos, certidões negativas de débitos (federais, estaduais, municipais, FGTS), política de ESG, plano de continuidade de negócios, referências de 3 clientes de porte similar e visite as instalações de produção para verificar capacidade e qualidade."
3.  **Elaboração de RFI/RFP e Avaliação de Propostas**:
    *   **Ação**: Desenvolva um Request for Information (RFI) ou Request for Proposal (RFP) detalhado e analise as respostas de forma estruturada.
    *   **Exemplo Prático**: Para um serviço de manutenção de infraestrutura de data center, o RFP deve incluir: "escopo detalhado (preventiva, corretiva, emergencial), SLAs para tempo de resposta e resolução (ex: 1 hora para P1, 4 horas para P2), estrutura de equipe técnica, cronograma de implementação, e detalhamento da estrutura de custos (mensal fixo, custos por chamada avulsa, peças)." Analise as propostas comparando não apenas o preço, mas a aderência aos SLAs, experiência da equipe e tecnologia empregada.
4.  **Negociação de Contrato e Acordo de Nível de Serviço (SLA)**:
    *   **Ação**: Negocie os termos contratuais e defina um SLA robusto que proteja os interesses da empresa.
    *   **Exemplo Prático**: Para um contrato de serviço de segurança da informação (SOC as a Service), negocie: "cláusulas de proteção de dados e propriedade intelectual, penalidades financeiras por violação de dados (ex: 5% do valor anual do contrato por incidente de P1 não resolvido no SLA), direito de auditoria, prazos de pagamento de 45 dias, e um SLA com uptime do serviço de 99.9% e tempo de detecção de ameaças de 15 minutos."
5.  **Onboarding Estruturado e Transição Operacional**:
    *   **Ação**: Implemente um plano detalhado para integrar o novo fornecedor às operações da empresa.
    *   **Exemplo Prático**: Para o onboarding de um novo parceiro de logística, execute: "reunião de kick-off com as equipes de suprimentos, vendas e TI; configuração de acessos ao sistema de rastreamento de cargas; treinamento das equipes internas sobre os novos procedimentos de solicitação e despacho; estabelecimento de canais de comunicação para escalonamento (e-mail, telefone de emergência); e monitoramento intensivo dos primeiros 60 dias de operação, com relatórios semanais de performance."

### Workflow 2: Monitoramento Contínuo e Otimização de Desempenho de Fornecedores Existentes

Este workflow foca em manter e aprimorar o relacionamento e o desempenho de fornecedores já contratados, garantindo valor contínuo e mitigação de riscos.

1.  **Coleta e Análise de Dados de Desempenho (KPIs)**:
    *   **Ação**: Estabeleça um processo regular para coletar e analisar dados de desempenho do fornecedor em relação aos SLAs e KPIs definidos.
    *   **Exemplo Prático**: Para um fornecedor de serviço de contact center, colete mensalmente: "Average Handling Time (AHT) < 300 segundos, First Call Resolution (FCR) > 85%, Customer Satisfaction Score (CSAT) > 4.2 (escala 1-5), Adherence to Schedule > 90% e tempo de espera na fila < 60 segundos." Utilize um dashboard de Power BI para visualizar tendências e identificar desvios.
2.  **Condução de Reuniões de Revisão de Negócios (QBRs)**:
    *   **Ação**: Realize reuniões periódicas com fornecedores estratégicos para revisar desempenho, discutir desafios e planejar o futuro.
    *   **Exemplo Prático**: Na QBR trimestral com o provedor de serviços de cloud computing, apresente: "o consumo de recursos x custo, o cumprimento dos SLAs de uptime (99.99%) e latência, os incidentes críticos do trimestre e suas resoluções, e discuta o roadmap de novas funcionalidades do provedor. Proponha otimizações de custos através de instâncias reservadas para o próximo semestre."
3.  **Gerenciamento Proativo de Riscos e Não Conformidades**:
    *   **Ação**: Monitore riscos emergentes e implemente ações corretivas para não conformidades.
    *   **Exemplo Prático**: Se o fornecedor de componentes eletrônicos apresentar um atraso de 3 dias em duas entregas consecutivas (KPI de On-Time Delivery abaixo de 90%), abra um "Plano de Ação Corretiva (CAPA)" formal. Exija um relatório detalhado da causa raiz, um plano de melhoria com prazos definidos (ex: implementação de nova linha de produção em 30 dias) e defina reuniões semanais para acompanhamento da execução do plano.
4.  **Identificação de Oportunidades de Otimização e Inovação**:
    *   **Ação**: Colabore com fornecedores para identificar e implementar melhorias de processo, redução de custos ou introdução de novas tecnologias.
    *   **Exemplo Prático**: Trabalhe com o fornecedor de embalagens para explorar materiais mais sustentáveis que também reduzam o custo por unidade em 5% sem comprometer a proteção do produto. Ou, em parceria com o fornecedor de impressão, implemente um portal de pedidos online que automatize o processo de solicitação e aprovação, reduzindo o tempo de ciclo em 20%.
5.  **Planejamento de Renovação de Contrato ou Offboarding**:
    *   **Ação**: Prepare-se para o término do contrato, decidindo pela renovação ou pelo offboarding do fornecedor.
    *   **Exemplo Prático**: Seis meses antes do término do contrato de licenças de software de design, avalie: "a satisfação dos usuários, o custo-benefício em relação a alternativas de mercado (ex: software open-source com funcionalidades similares), e a necessidade de renegociar termos. Se optar pelo offboarding, crie um plano detalhado de migração de dados, desativação de acessos, devolução de equipamentos e comunicação interna e externa."

---

## Templates

### RFP (Request for Proposal) Simplificado para Serviço de Segurança Patrimonial

```markdown
# Request for Proposal (RFP) - Serviço de Segurança Patrimonial

**Data de Emissão:** 2024-03-01
**Prazo para Envio de Propostas:** 2024-03-20, 17:00 BRT
**Contato para Dúvidas:** [email@empresa.com.br]

## 1. Introdução
A [Nome da Empresa], uma empresa líder no setor de [setor], com sede em [Cidade/Estado], busca contratar um fornecedor especializado em serviços de segurança patrimonial para sua unidade principal. Nosso objetivo é garantir a proteção de ativos, colaboradores e visitantes, mantendo um ambiente seguro e controlado.

## 2. Escopo do Serviço
O serviço de segurança patrimonial deverá ser prestado na unidade localizada em [Endereço Completo da Unidade], com as seguintes características:

*   **Horário de Cobertura:** 24 horas por dia, 7 dias por semana, incluindo feriados.
*   **Postos de Serviço:**
    *   Portaria Principal: 2 vigilantes (diurno/noturno), controle de acesso de veículos e pedestres, registro de visitantes.
    *   Recepção Administrativa: 1 vigilante (horário comercial), controle de acesso de visitantes e apoio à recepção.
    *   Ronda Interna/Externa: 1 vigilante (noturno), rondas preventivas, monitoramento de perímetro.
*   **Atividades Incluídas:**
    *   Controle de acesso (identificação, cadastro, crachá de visitante).
    *   Monitoramento de câmeras de segurança (CCTV).
    *   Inspeção de veículos e volumes (quando aplicável).
    *   Atendimento a emergências (primeiro contato com autoridades, evacuação).
    *   Elaboração de relatórios diários de ocorrências.
    *   Treinamento e capacitação da equipe.
*   **Tecnologia Requerida:** Sistema de controle de ronda eletrônico, rádio comunicadores para a equipe.

## 3. Requisitos Técnicos e Operacionais
*   A empresa proponente deve possuir licença de funcionamento e todas as certificações exigidas pela Polícia Federal (Portaria 3.233/2012-DG/DPF).
*   Experiência comprovada de no mínimo 5 anos no mercado de segurança patrimonial.
*   Equipe de vigilantes com curso de formação e reciclagem em dia, com registro na Polícia Federal.
*   Plano de contingência para substituição de pessoal em caso de ausência ou emergência (tempo máximo de resposta: 2 horas).
*   Fornecimento de uniformes padronizados e equipamentos de proteção individual (EPIs).
*   Seguro de Responsabilidade Civil com cobertura mínima de R$ 5.000.000,00.

## 4. Requisitos Contratuais
*   Contrato inicial de 12 meses, renovável.
*   Faturamento mensal, com prazo de pagamento de 30 dias após emissão da nota fiscal.
*   Cláusula de confidencialidade e proteção de dados.
*   Penalidades por descumprimento de SLAs (ex: multa de 1% do valor mensal por cada ocorrência grave não atendida no prazo).

## 5. Estrutura de Custos
Apresentar a proposta de custos detalhada, incluindo:
*   Custo mensal por vigilante (discriminando salário, encargos, benefícios, equipamentos).
*   Custo total mensal do serviço.
*   Custos adicionais para serviços extras (ex: cobertura de eventos, escolta).
*   Previsão de reajuste anual (índice sugerido).

## 6. Cronograma de Avaliação
*   **Envio de Propostas:** até 20/03/2024
*   **Análise Interna:** 21/03/2024 - 28/03/2024
*   **Entrevistas/Apresentações:** 01/04/2024 - 05/04/2024
*   **Notificação do Vencedor:** 10/04/2024
*   **Início do Contrato:** 01/05/2024

## 7. Critérios de Avaliação
As propostas serão avaliadas com base nos seguintes critérios:
*   **Qualificação e Experiência do Fornecedor:** 30%
*   **Estrutura de Custo e Competitividade de Preço:** 30%
*   **Aderência ao Escopo e Requisitos Operacionais:** 25%
*   **Plano de Contingência e Suporte:** 10%
*   **Referências de Clientes:** 5%
```

### Scorecard de Avaliação de Desempenho de Fornecedor (Mensal)

```markdown
# Scorecard de Avaliação de Desempenho de Fornecedor - Serviço de Limpeza e Conservação

**Fornecedor:** Limpeza Brilhante Ltda.
**Período de Avaliação:** Fevereiro/2024
**Gerente Responsável:** Ana Paula Silva
**Data da Avaliação:** 2024-03-05

| Métrica de Desempenho | Descrição Detalhada | Peso (%) | Pontuação (1-5) | Comentários e Evidências | Ação Corretiva (se <3) |
|:----------------------|:--------------------|:---------|:----------------|:-------------------------|:-----------------------|
| **Qualidade do Serviço** | Salas limpas, banheiros higienizados, lixeiras esvaziadas, ausência de pó, vidros limpos. | 40% | 4 | "Alguns vidros da área de convivência apresentaram manchas persistentes. Salas de reunião sempre impecáveis." | Treinamento específico sobre limpeza de vidros. |
| **Adesão ao Cronograma** | Serviços realizados nos horários acordados, sem interrupções à operação. | 25% | 5 | "Equipe sempre pontual, sem atrasos nas rotinas de limpeza diária." | N/A |
| **Disponibilidade da Equipe** | Número de funcionários alocados conforme contrato, taxa de absenteísmo. | 15% | 3 | "Um funcionário esteve de atestado por 3 dias e a substituição demorou 1 dia útil para ser providenciada, causando acúmulo de serviço no setor de TI." | Fornecedor deve garantir substituição em no máximo 4 horas úteis. |
| **Relacionamento e Comunicação** | Prontidão em atender solicitações, feedback proativo, facilidade de contato. | 10% | 4 | "Boa comunicação com o supervisor, mas houve atraso na resposta a uma solicitação de limpeza extra na cozinha." | Melhorar tempo de resposta para solicitações não urgentes. |
| **Saúde e Segurança** | Uso correto de EPIs, cumprimento das normas de segurança do trabalho. | 10% | 5 | "Todos os funcionários utilizam os EPIs adequados; sem incidentes de segurança reportados." | N/A |
| **Pontuação Total** | | **100%** | **4.0** | | |

**Recomendações e Próximos Passos:**
*   Agendar reunião de alinhamento com o supervisor da Limpeza Brilhante para discutir a melhoria na limpeza de vidros e o processo de substituição de pessoal.
*   Monitorar de perto o KPI de Disponibilidade da Equipe no próximo mês.
*   Elogiar a equipe pela pontualidade e qualidade geral da limpeza das salas.

**Status Geral:** Satisfatório com pontos de atenção.
```

---

## Checklist

- [X] Validar certidões negativas (fiscal, trabalhista, federal) do fornecedor principal para os últimos 6 meses.
- [ ] Confirmar a existência de uma cláusula de penalidade por atraso na entrega de 1% do valor do pedido por dia, limitada a 10% do valor total.
- [X] Agendar reuniões trimestrais de revisão de negócios (QBRs) com os 5 principais fornecedores por volume de gastos.
- [ ] Verificar a conformidade do fornecedor de software com a LGPD através de auditoria de segurança de dados e análise de DPA (Data Processing Agreement).
- [X] Atualizar o cadastro de contatos de emergência do fornecedor de TI no sistema interno e comunicar as equipes impactadas.
- [ ] Analisar os relatórios de CSAT do fornecedor de suporte técnico dos últimos 3 meses, buscando tendências de insatisfação abaixo de 4.0.
- [ ] Documentar o plano de offboarding para o fornecedor X (licenças de software), incluindo migração de dados, desativação de acessos e devolução de ativos físicos.
- [X] Confirmar que todas as faturas do fornecedor Y (manutenção predial) estão alinhadas com os termos contratuais e os serviços prestados.
- [ ] Realizar uma análise de mercado anual para os serviços de telecomunicações, buscando benchmarks de preços e inovações tecnológicas.
- [ ] Validar a apólice de seguro de responsabilidade civil do fornecedor de logística para cobrir o escopo do serviço de transporte de alto valor.

---

## Métricas de Referência

| Métrica | Benchmark do Mercado | Meta Interna (Anual) |
|:---------------------------|:---------------------|:--------------------|
| On-Time Delivery (OTD) | >95% | 98.5% |
| Qualidade do Serviço (SLA Adherence) | >98% | 99.7% |
| Redução Custo Total de Propriedade (TCO) | 3-5% anualmente | 6% |
| Tempo Médio de Resposta a Incidentes (P1) | < 1 hora | < 30 minutos |
| CSAT Fornecedor (escala 1-5) | >4.0 | 4.6 |
| Conformidade Regulatória (Auditorias) | 100% | 100% |

---

## Erros Comuns

1.  **Não Realizar Due Diligence Completa**: Contratar fornecedores sem uma verificação minuciosa de sua saúde financeira, conformidade legal ou histórico de conformidade pode levar a interrupções operacionais, riscos legais e financeiro.
    *   **Como evitar**: Sempre solicite balanços financeiros auditados dos últimos 3 anos, certidões negativas de débitos (federais, estaduais, municipais, FGTS), e referências de, no mínimo, dois clientes. Exemplo: Uma empresa contratou um fornecedor de serviços de TI sem verificar sua estabilidade financeira, resultando na interrupção abrupta dos serviços quando o fornecedor decretou falência, causando perda de dados e tempo de inatividade de 48 horas.
2.  **Focar Exclusivamente no Preço Mais Baixo**: Priorizar o menor custo sem considerar a qualidade do serviço, a capacidade de suporte, a robustez do SLA e o risco associado pode resultar em custos ocultos elevados e insatisfação das áreas internas.
    *   **Como evitar**: Adote uma abordagem de Custo Total de Propriedade (TCO), considerando não apenas o preço de compra, mas também custos de manutenção, treinamento, suporte e potenciais penalidades. Exemplo: Optar pelo serviço de limpeza mais barato pode levar a uma queda na qualidade e frequência, exigindo retrabalho da equipe interna ou causando reclamações de funcionários, que, somados, superam a economia inicial.
3.  **Falha na Gestão de Relacionamento Pós-Contrato**: Assinar o contrato e não monitorar ativamente o desempenho e o relacionamento com o fornecedor após a contratação. Isso leva à perda de oportunidades de otimização, escalonamento de problemas e desalinhamento estratégico.
    *   **Como evitar**: Implemente um programa de Vendor Relationship Management (VRM) com reuniões de desempenho regulares (QBRs), scorecards e canais de comunicação claros. Exemplo: Não realizar QBRs periódicas com o provedor de infraestrutura de cloud resultou na empresa pagando por recursos subutilizados por seis meses, perdendo a chance de otimizar gastos e renegociar termos.

---

## Dicas Avançadas

1.  **Implementação de um Programa de Inovação Colaborativa com Fornecedores**: Vá além da gestão transacional. Crie um programa estruturado para convidar fornecedores estratégicos a co-criar soluções, compartilhar conhecimento e inovar.
    *   **Exemplo Prático**: Convide seu fornecedor de embalagens para sessões de brainstorming anuais focadas em materiais sustentáveis e otimização de custos de transporte, resultando no desenvolvimento de uma embalagem 100% reciclável que reduziu o custo logístico em 8% e a pegada de carbono do produto.
2.  **Utilização de Análise Preditiva para Gestão de Risco de Fornecedor**: Em vez de reagir a falhas, use dados para prever riscos potenciais. Integre dados de desempenho histórico, notícias financeiras, indicadores de mercado e relatórios de agências de crédito.
    *   **Exemplo Prático**: Utilize um software de GRC (Governance, Risk, and Compliance) que monitora a saúde financeira de fornecedores-chave e envia alertas se o rating de crédito de um fornecedor crítico cair abaixo de um limiar pré-definido, permitindo que a empresa ative um plano de contingência (ex: buscar fornecedores alternativos, aumentar estoque de segurança) antes que o problema de liquidez se manifeste.
3.  **Estratégia de Multi-Sourcing e Resiliência da Cadeia de Suprimentos**: Para reduzir a dependência de um único fornecedor e aumentar a resiliência operacional, adote uma estratégia de multi-sourcing para componentes ou serviços essenciais.
    *   **Exemplo Prático**: Em vez de ter um único fornecedor para todos os componentes eletrônicos críticos