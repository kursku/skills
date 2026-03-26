---
name: scope-creep-prevention
description: "Skill especializada para mitigar e prevenir o desvio de escopo em projetos de consultoria, focando em alinhamento contratual, gestão de mudanças e comunicação contínua."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
risk: caution
---

# Scope Creep Prevention

Esta skill capacita o Claude a atuar como um especialista em prevenção de desvio de escopo, fornecendo estratégias, workflows e ferramentas para garantir a entrega de projetos de consultoria dentro dos limites acordados, protegendo a rentabilidade e a satisfação do cliente.

---

## Keywords

Gestão de Escopo, Aditivo Contratual, Termo de Abertura de Projeto (TAP), Request for Change (RFC), Alinhamento de Expectativas, Matriz RACI, Baseline do Projeto, Comunicação Pró-Ativa, Mitigação de Riscos, Gerenciamento de Partes Interessadas, Acordos de Nível de Serviço (SLA), Desvio de Escopo.

---

## Quick Start

1.  **Revisar TAP do Projeto**: Confirmar que o Termo de Abertura de Projeto detalha entregáveis, não-entregáveis, critérios de aceitação e exclusões explícitas antes de qualquer atividade de execução, solicitando assinatura formal do cliente.
2.  **Identificar Stakeholders Chave**: Mapear os decisores e influenciadores do cliente e da consultoria, estabelecendo um plano de comunicação formal com frequência e formato definidos para cada grupo.
3.  **Estabelecer Baseline de Escopo**: Validar e congelar o escopo inicial com o cliente via assinatura formal do TAP, utilizando-o como referência imutável para todas as futuras solicitações de mudança.
4.  **Implementar Processo de RFC**: Configurar um fluxo para Solicitações de Mudança de Escopo (RFC) que inclua submissão formal, análise de impacto detalhada, aprovação formal (preferencialmente por comitê) e atualização de toda a documentação do projeto.
5.  **Comunicação Proativa de Desvios**: Integrar uma seção fixa sobre "Desvios de Escopo e RFCs" em todos os relatórios de status e agendas de reunião, garantindo visibilidade contínua e discussão tempestiva.

---

## Core Workflows

### Workflow 1: Validação Contratual e Estruturação do TAP para Prevenção Ativa

**Objetivo**: Assegurar que os documentos iniciais do projeto sirvam como barreiras robustas e formalizadas contra o desvio de escopo, estabelecendo expectativas claras desde o início.

**Passos Detalhados**:

1.  **Pré-venda e Entendimento da Necessidade (até D-30 antes do contrato)**: Durante a fase de prospecção, o consultor deve ir além da apresentação da solução, preenchendo um "Formulário de Entendimento de Necessidade" rigoroso. Este formulário deve conter campos como "Problema Central a Ser Resolvido (Visão do Cliente)", "Resultados Esperados Quantificáveis (KPIs)", e, crucialmente, "Entregáveis Exclusos (mencione o que o cliente *pode* esperar, mas *não será* entregue)".
    *   **Exemplo Prático**: Se o cliente manifesta interesse em "otimização de processos de RH", o consultor deve perguntar diretamente: "Esta otimização incluirá a implementação de um novo sistema de folha de pagamento ou gestão de talentos?" Se a resposta for negativa, registrar imediatamente na proposta e no formulário: "Implementação de sistema de folha de pagamento e gestão de talentos *excluída* do escopo deste projeto."
2.  **Elaboração Contratual com Cláusulas de Escopo Explícitas (D-15 antes do contrato)**: Trabalhar em conjunto com o departamento jurídico para inserir cláusulas contratuais que blindem o escopo.
    *   **Exemplos de Cláusulas Obrigatórias**:
        *   "**Cláusula de Escopo Fixo**": "Os serviços a serem prestados por [Nome da Consultoria] estão estritamente limitados aos descritos na Cláusula X 'Descrição dos Serviços' e no Anexo A 'Termo de Abertura de Projeto' anexo. Qualquer alteração, adição ou exclusão ao escopo aqui definido deverá ser formalizada por Aditivo Contratual específico, com reavaliação de prazos, custos e recursos."
        *   "**Cláusula de Critérios de Aceitação**": "A aceitação de cada entregável será baseada nos critérios específicos definidos no Anexo A, sendo responsabilidade do Cliente fornecer feedback formal e aprovação/rejeição dentro de X dias úteis após a entrega para revisão."
3.  **Desenvolvimento do Termo de Abertura de Projeto (TAP) Detalhado (D+5 após contrato)**: Converter o contrato em um TAP com granularidade suficiente para evitar ambiguidades.
    *   **Seção "Entregáveis Específicos"**: Listar cada item com seu respectivo critério de aceitação, quantificável e verificável.
        *   **Exemplo**: "Relatório de Análise de Processos de Vendas - Critério de Aceitação: Aprovação formal do Gerente de Vendas em até 5 dias úteis, com base na cobertura de *todos* os subprocessos mapeados (prospecção, qualificação, proposta, fechamento) e na identificação de *pelo menos* 3 gargalos de eficiência."
    *   **Seção "Não-Entregáveis / Exclusões"**: Ser explícito sobre o que não será feito. Esta seção é tão importante quanto a dos entregáveis.
        *   **Exemplo**: "Não será fornecido suporte técnico para sistemas legados do cliente (ex: ERP 'Sistema X' versão 2008) após a fase de implementação da nova metodologia." ou "Treinamento para equipe de TI do cliente na manutenção da solução desenvolvida não está incluído no escopo; apenas treinamento de usuários finais."
    *   **Seção "Responsabilidades e Partes Interessadas"**: Utilizar uma matriz RACI (Responsible, Accountable, Consulted, Informed) para as principais atividades e entregáveis, definindo claramente os papéis da equipe da consultoria e do cliente.
4.  **Reunião de Kick-off e Validação Formal do TAP (D+10 após contrato)**: Conduzir uma reunião formal de kick-off com todos os stakeholders chave do cliente e da consultoria. Apresentar o TAP, item por item, solicitando validação e assinatura formal. Registrar todas as dúvidas e esclarecimentos em ata, anexando-a ao TAP. Isso cria um "contrato social" sobre o escopo.

### Workflow 2: Gerenciamento Ativo de Mudanças e Comunicação para Sustentar o Escopo

**Objetivo**: Manter o escopo sob controle durante a execução do projeto, respondendo proativamente a solicitações de mudança e garantindo que qualquer desvio seja formalmente avaliado e aprovado.

**Passos Detalhados**:

1.  **Estabelecimento de Linha de Base (Baseline) (D+15 após contrato)**: Após a validação e assinatura do TAP na reunião de kick-off, o escopo, cronograma e orçamento iniciais são "congelados". Comunicar formalmente a ambas as equipes que qualquer solicitação de mudança a partir deste ponto seguirá um processo estruturado de Request for Change (RFC).
2.  **Processo de Solicitação de Mudança (RFC) (Contínuo)**:
    *   **Submissão**: Qualquer solicitação de alteração (nova funcionalidade, modificação de requisito, extensão de prazo por motivo do cliente, etc.) deve ser submetida usando um formulário de RFC padronizado (ver seção de Templates). O solicitante (geralmente do lado do cliente) deve descrever a mudança, a razão da solicitação e o benefício esperado.
    *   **Análise de Impacto**: A equipe da consultoria (gerente de projeto, especialistas técnicos/funcionais) analisa a RFC. Isso