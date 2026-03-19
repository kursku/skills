---
name: offboarding-process
description: "Offboarding Process — Skill especializada para offboarding process"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Offboarding Process

Esta skill capacita o Claude a gerenciar de forma proativa e estratégica o processo de offboarding de clientes de consultoria, minimizando churn, protegendo dados e otimizando o feedback pós-engajamento.

---

## Keywords

Churn prevention, client retention, exit interview, knowledge transfer, data offboarding, contract termination, feedback loop, win-back strategy, relationship management, client transition, pós-venda, encerramento de contrato, reengajamento.

---

## Quick Start

1.  **Agende a Reunião de Desengajamento Final**: Proponha esta reunião com o cliente entre 15 e 30 dias antes da data efetiva de término do contrato para alinhar expectativas e próximos passos.
2.  **Revise o Status Financeiro e Contratual**: Verifique todas as faturas emitidas, pagamentos recebidos e pendências, além das cláusulas de rescisão, com pelo menos 10 dias de antecedência.
3.  **Configure a Migração de Dados Essenciais**: Inicie a compilação e exportação de todos os dados, relatórios e entregáveis do cliente para um formato acessível e seguro em até 7 dias após a notificação oficial de offboarding.
4.  **Envie o Formulário de Feedback de Offboarding**: Direcione a pesquisa de satisfação detalhada para o contato principal do cliente 48 horas após a reunião final, focando na experiência geral e pontos de melhoria.
5.  **Revogue Acessos e Permissões**: Desative todos os acessos do cliente às plataformas internas da consultoria (CRM, ferramentas de colaboração, ambientes de desenvolvimento) no dia útil seguinte à data de término do contrato.

---

## Core Workflows

### Workflow 1: Gestão Proativa do Desengajamento e Potencial Retenção

Este workflow foca na identificação precoce de sinais de saída e na tentativa estratégica de retenção ou, alternativamente, na preparação para um offboarding suave, transformando uma potencial perda em oportunidade futura.

1.  **Monitoramento Contínuo de Sinais de Risco (Churn Signals)**:
    *   **Ação**: Implementar um sistema de monitoramento de KPIs de engajamento e satisfação. Exemplos incluem:
        *   **Engajamento**: Redução de 25% na participação em reuniões semanais, abertura de relatórios abaixo de 50% nos últimos 2 meses, menos de 3 interações proativas mensais por parte do cliente.
        *   **Satisfação**: Queda de 2 pontos no NPS trimestral (ex: de 8 para 6), aumento de reclamações sobre tempo de resposta ou qualidade das entregas em 15% no último mês.
        *   **Uso do Serviço**: Diminuição de 30% na utilização de funcionalidades específicas ou módulos da consultoria.
    *   **Exemplo Concreto**: Para o cliente "TecnoSolutions", o gerente de contas notou que o NPS caiu de 9 para 6 no último trimestre e o cliente não abriu os últimos 3 relatórios de performance, além de ter diminuído a frequência de reuniões de alinhamento.

2.  **Reunião de Alinhamento e Sondagem (Pré-Offboarding)**:
    *   **Ação**: Ao identificar sinais de risco, agendar proativamente uma reunião com o cliente para entender as causas. O objetivo é ouvir ativamente e identificar possíveis insatisfações ou mudanças de necessidade.
    *   **Script de Abordagem**: "Prezado(a) [Nome do Contato], notamos algumas mudanças recentes no engajamento com o projeto [Nome do Projeto] e gostaríamos de agendar uma breve conversa. Nosso objetivo é garantir que estamos entregando o máximo valor e que suas necessidades de negócio continuam sendo atendidas, ou entender se houve alguma mudança estratégica de sua parte. O que seria um bom dia e horário para conversarmos na próxima semana?"
    *   **Exemplo Concreto**: Após a reunião, a TecnoSolutions revelou que sua estratégia de mercado mudou, e o foco agora é mais em desenvolvimento interno do que em consultoria externa.

3.  **Proposta de Valor Reforçada ou Plano de Transição**:
    *   **Ação**: Com base no feedback da reunião de sondagem, preparar uma proposta de valor revisada que aborde as novas necessidades ou preocupações do cliente, ou um plano de transição para um serviço mais adequado.
    *   **Exemplo de Retenção**: Se a TecnoSolutions estivesse insatisfeita com o custo, a consultoria poderia propor um "Pacote Essencial" focado apenas nos pilares críticos (ex: monitoramento de KPIs e relatórios executivos) com uma redução de 20% no valor mensal, ou um plano de 3 meses para capacitar a equipe interna a assumir as tarefas.
    *   **Exemplo de Transição**: Se a decisão de offboarding for irreversível, apresentar um plano de transição claro, enfatizando a continuidade do suporte até a data final e a transferência de conhecimento.

4.  **Formalização e Comunicação do Offboarding**:
    *   **Ação**: Se a decisão de offboarding for mantida, formalizar o processo. Enviar um e-mail de confirmação que detalhe as datas, próximos passos e uma lista de pendências para ambas as partes.
    *   **Exemplo Concreto**: Enviar o `E-mail de Confirmação de Offboarding e Próximos Passos` (vide seção de Templates) para a TecnoSolutions, estabelecendo a data de término em 30/06/2025 e listando as ações de transferência de dados e encerramento financeiro.

### Workflow 2: Execução Técnica e Administrativa do Offboarding

Este workflow aborda as ações práticas e operacionais necessárias para garantir um encerramento eficiente, seguro e profissional da parceria com o cliente.

1.  **Criação e Execução do Plano de Offboarding Detalhado**:
    *   **Ação**: Desenvolver um plano de ação interno com todas as tarefas específicas, responsáveis e prazos. Este plano deve ser compartilhado internamente e monitorado.
    *   **Exemplo Concreto**: Utilizar o `Plano de Ação de Offboarding de Cliente (Interno)` (vide seção de Templates) para o cliente "TecnoSolutions", delegando a exportação de dados ao analista João, a revisão financeira à Gerente Ana, e a revogação de acessos ao TI Pedro.

2.  **Gerenciamento de Acessos e Dados**:
    *   **Revogação de Acessos**:
        *   **Ação**: Remover o cliente e seus colaboradores de todas as plataformas internas (CRM, sistemas de gestão de projetos como Asana/Jira, canais de comunicação como Slack/Microsoft Teams) e revogar acessos a ferramentas de consultoria compartilhadas (ex: Power BI Dashboards, Google Analytics, ferramentas de SEO).
        *   **Prazo**: Agendar para o dia útil seguinte à data oficial de término do contrato.
        *   **Exemplo Concreto**: No dia 01/07/2025, o time de TI desativa as contas de "Maria Silva" e "Carlos Almeida" de todas as plataformas internas da consultoria e remove seu acesso ao dashboard de performance no Power BI.
    *   **Transferência/Backup de Dados**:
        *   **Ação**: Exportar e organizar todos os dados relevantes (relatórios, análises, documentos de projeto, apresentações finais, credenciais de acesso temporárias) em um formato universal e seguro. Entregar ao cliente por meio de um link seguro ou mídia física.
        *   **Exemplo Concreto**: Compilar todos os relatórios mensais de marketing, análises de mercado e documentos estratégicos do projeto "Otimização de Vendas" da TecnoSolutions em um arquivo ZIP de 3.2 GB e enviar um link de download seguro via Google Drive com validade de 15 dias.

3.  **Encerramento Financeiro e Contratual**:
    *   **Última Fatura**:
        *   **Ação**: Emitir a última fatura, incluindo quaisquer serviços pendentes, horas extras aprovadas ou taxas de rescisão (se aplicável, conforme contrato).
        *   **Exemplo Concreto**: Enviar fatura final de R$ 7.800,00 para a TecnoSolutions, referente ao mês de junho e 10 horas extras de consultoria aprovadas, com vencimento em 05/07/2025.
    *   **Confirmação de Encerramento**:
        *   **Ação**: Enviar um e-mail formal confirmando o encerramento do contrato e a quitação de todas as obrigações financeiras (após o pagamento da última fatura).
        *   **Exemplo Concreto**: Após o recebimento do pagamento da última fatura da TecnoSolutions em 05/07/2025, enviar e-mail confirmando que todas as obrigações contratuais e financeiras foram cumpridas por ambas as partes.

4.  **Coleta de Feedback e Oportunidades de Reengajamento Futuro**:
    *   **Pesquisa de Satisfação de Offboarding**:
        *   **Ação**: Enviar uma pesquisa detalhada (ex: via Typeform ou SurveyMonkey) para o contato principal do cliente, focando em sua experiência geral, pontos fortes e fracos da consultoria, e motivos para o offboarding.
        *   **Exemplo Concreto**: Enviar o questionário "Feedback de Encerramento de Parceria" para o diretor de projetos da TecnoSolutions, com perguntas como "Qual o principal motivo para o encerramento da parceria?", "Qual foi o maior valor que você obteve?", "Em uma escala de 0 a 10, qual a probabilidade de você nos indicar?".
    *   **Manutenção do Relacionamento e Reengajamento Futuro**:
        *   **Ação**: Agendar um "check-in" informal ou follow-up em 6 a 12 meses para avaliar novas necessidades do cliente ou oportunidades de reengajamento. Adicionar o cliente a uma lista de e-mail de "Alumni" ou "Ex-Clientes" para updates relevantes.
        *   **Exemplo Concreto**: Criar um lembrete no CRM para contatar a TecnoSolutions em janeiro de 2026 para um "café virtual" e adicionar o e-mail de "Maria Silva" à lista de newsletter mensal sobre tendências de mercado.

---

## Templates

### E-mail de Confirmação de Offboarding e Próximos Passos

```
Assunto: Confirmação de Encerramento Contratual e Próximos Passos - [Nome da Empresa Cliente]

Prezado(a) [Nome do Contato do Cliente],

Este e-mail serve para formalizar o encerramento de nossa parceria de consultoria referente ao projeto "[Nome do Projeto/Serviço]" a partir de [Data de Término Efetiva: ex: 30/06/2025]. Gostaríamos de expressar nossa gratidão pela confiança depositada em nossa equipe durante [Período de Parceria: ex: os últimos 18 meses].

Para garantir uma transição suave e completa, detalhamos os próximos passos:

1.  **Migração e Acesso aos Dados:**
    *   Todos os relatórios finais, análises e documentos gerados durante nossa parceria (totalizando 2.5 GB) foram compilados na pasta "Dados Finais - [Nome da Empresa Cliente]" em nosso Google Drive. Um link de download seguro será enviado separadamente em até 24 horas. Este link estará ativo até [Data + 15 dias: ex: 15/07/2025].
    *   O acesso aos dashboards de Power BI/Tableau e Google Analytics que foram compartilhados será mantido até [Data + 7 dias: ex: 07/07/2025], permitindo tempo para sua equipe replicar ou baixar dados históricos relevantes.

2.  **Revogação de Acessos:**
    *   Os acessos de sua equipe às nossas plataformas internas (Ex: Asana do projeto, Slack de comunicação direta, CRM de suporte) serão revogados em [Data + 1 dia útil: ex: 01/07/2025].
    *   Informamos que os acessos à nossa base de conhecimento exclusiva (Wiki interna) serão desativados na mesma data.

3.  **Questões Financeiras:**
    *   A última fatura, cobrindo o período até [Data de Término Efetiva: ex: 30/06/2025], no valor de R$ 5.500,00, será emitida e enviada para [Email Financeiro do Cliente: ex: financeiro@cliente.com.br] até [Data da Emissão da Fatura: ex: 03/07/2025]. Não há pendências ou multas de rescisão aplicáveis.

4.  **Feedback de Offboarding:**
    *   Valorizamos muito sua perspectiva. Um breve formulário de feedback sobre sua experiência com nossa consultoria será enviado em [Data de Envio do Feedback: ex: 02/07/2025]. Seu retorno nos ajudará a aprimorar nossos serviços.

Permanecemos à disposição para quaisquer dúvidas remanescentes até [Data + 15 dias: ex: 15/07/2025]. Desejamos muito sucesso em seus futuros empreendimentos.

Atenciosamente,

[Seu Nome/Nome da Consultoria]
[Seu Cargo]
[Contato]
```

### Plano de Ação de Offboarding de Cliente (Interno)

```
# Plano de Ação de Offboarding - Cliente: [Nome da Empresa Cliente]

**Data de Início do Offboarding:** [Ex: 15/06/2025]
**Data de Término Efetiva do Contrato:** [Ex: 30/06/2025]
**Motivo do Offboarding:** [Ex: Mudança de estratégia interna do cliente, Custos elevados, Necessidade atendida, Insatisfação com serviço X]
**Responsável Principal:** [Ex: Gerente de Contas: Laura Costa]

| Categoria                | Tarefa Específica                                        | Responsável  | Prazo Final       | Status        | Observações