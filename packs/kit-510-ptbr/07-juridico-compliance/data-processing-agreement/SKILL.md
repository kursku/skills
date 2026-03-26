---
name: data-processing-agreement
description: "Data Processing Agreement — Skill especializada para data processing agreement"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: offensive
---

# Data Processing Agreement

Esta skill capacita o Claude a elaborar, revisar e gerenciar Data Processing Agreements (DPAs) em conformidade com a LGPD e GDPR, assegurando a proteção de dados pessoais em relações contratuais.

---

## Keywords

LGPD, GDPR, DPA, Contrato Processamento Dados, Controlador, Processador, Subprocessador, Conformidade, Segurança Dados, Privacidade, Cláusulas Contratuais, Transferência Internacional, Due Diligence.

---

## Quick Start

1.  **Avaliar o Relacionamento:** Determine se a relação entre as partes configura "controlador-processador" ou "processador-subprocessador" para definir a necessidade e a estrutura do DPA.
2.  **Mapear Fluxo de Dados:** Liste os tipos de dados pessoais processados, finalidades, categorias de titulares e duração do processamento (Ex: PII de clientes, dados de uso de plataforma, por 5 anos).
3.  **Elaborar Rascunho Inicial:** Utilize um template padrão de DPA, preenchendo as seções de escopo, obrigações das partes e medidas de segurança, como criptografia e controles de acesso.
4.  **Iniciar Negociação:** Envie o DPA para a outra parte, destacando cláusulas críticas como responsabilidade, auditoria e notificação de incidentes para discussão.
5.  **Assinatura e Registro:** Finalize o texto e obtenha as assinaturas eletrônicas ou físicas, registrando o DPA junto ao contrato principal para referência futura.

---

## Core Workflows

### Workflow 1: Elaboração de DPA para Prestador de Serviço (Processador)

Este workflow detalha a criação de um DPA do ponto de vista de uma empresa que atua como processadora de dados para um cliente (controlador), garantindo conformidade com LGPD/GDPR.

1.  **Identificação do Escopo e Partes:**
    *   **Passo 1.1:** Confirme os papéis: Sua empresa é o **Processador** e o cliente é o **Controlador**.
    *   **Passo 1.2:** Defina o serviço principal que envolve o processamento de dados (Ex: Serviço de CRM em nuvem, Plataforma de e-commerce, Hospedagem de dados).
    *   **Passo 1.3:** Liste as partes envolvidas com seus dados completos (Razão Social, CNPJ/NIF, Endereço).
        *   *Exemplo:* Processador: "Tech Solutions Ltda., CNPJ 00.111.222/0001-33, Av. Paulista, 1000, São Paulo/SP". Controlador: "Varejo Digital S.A., CNPJ 99.888.777/0001-44, Rua da Consolação, 500, São Paulo/SP".

2.  **Mapeamento Detalhado dos Dados Pessoais:**
    *   **Passo 2.1:** Descreva as categorias de dados pessoais que serão processadas.
        *   *Exemplo:* Dados de Clientes (Nome, CPF, RG, Endereço, E-mail, Telefone, Histórico de Compras), Dados de Funcionários do Controlador (Nome, Cargo, E-mail corporativo).
    *   **Passo 2.2:** Especifique as categorias de titulares dos dados.
        *   *Exemplo:* Clientes do Varejo Digital S.A., Funcionários do Varejo Digital S.A.
    *   **Passo 2.3:** Determine a finalidade e a base legal do processamento (sempre indicando que a base legal é de responsabilidade do Controlador).
        *   *Exemplo:* "Finalidade: Prestação do serviço de CRM para gestão de relacionamento com clientes do Controlador. Base Legal: O Controlador declara ter base legal adequada (e.g., consentimento, execução de contrato) para o tratamento."
    *   **Passo 2.4:** Estabeleça a duração do processamento e o destino dos dados após o término.
        *   *Exemplo:* "Duração: Pelo período de vigência do Contrato Principal, mais 90 dias para eventual recuperação. Após, os dados serão excluídos de forma segura ou anonimizados, conforme instrução do Controlador."

3.  **Definição de Medidas de Segurança Técnica e Organizacional:**
    *   **Passo 3.1:** Liste as medidas técnicas implementadas.
        *   *Exemplo:* "Criptografia de dados em repouso (AES-256) e em trânsito (TLS 1.2+); Controle de acesso baseado em função (RBAC) com autenticação multifator (MFA); Monitoramento de segurança 24/7 com SIEM; Testes de penetração anuais por terceiros."
    *   **Passo 3.2:** Descreva as medidas organizacionais.
        *   *Exemplo:* "Políticas internas de segurança da informação e privacidade; Treinamento obrigatório em LGPD/GDPR para todos os colaboradores com acesso a dados; Acordos de confidencialidade (NDAs) com funcionários e terceiros; Plano de Resposta a Incidentes de Segurança da Informação (PRISI)."

4.  **Gestão de Subprocessadores e Transferência Internacional:**
    *   **Passo 4.1:** Inclua a permissão para o uso de subprocessadores e a exigência de que estes cumpram obrigações semelhantes.
        *   *Exemplo:* "O Processador poderá contratar subprocessadores, desde que informe o Controlador previamente e garanta que estes subprocessadores assumam obrigações de proteção de dados substancialmente equivalentes às do presente DPA."
    *   **Passo 4.2:** Especifique como a transferência internacional de dados será tratada, se aplicável.
        *   *Exemplo:* "Caso haja transferência internacional de dados, o Processador se compromete a utilizar mecanismos de conformidade previstos na LGPD/GDPR, como Cláusulas Contratuais Padrão (SCCs) ou Regras Corporativas Vinculativas (BCRs)."

5.  **Cláusulas Essenciais Adicionais:**
    *   **Passo 5.1:** Direitos dos Titulares: Processamento de solicitações (acesso, retificação, exclusão).
        *   *Exemplo:* "O Processador auxiliará o Controlador no cumprimento das obrigações relativas aos direitos dos titulares, encaminhando prontamente qualquer solicitação recebida diretamente e fornecendo as informações necessárias."
    *   **Passo 5.2:** Notificação de Incidentes: Prazos e procedimentos.
        *   *Exemplo:* "O Processador notificará o Controlador de qualquer incidente de segurança envolvendo dados pessoais em até 48 horas após a ciência, fornecendo todas as informações relevantes para que o Controlador possa cumprir suas obrigações legais."
    *   **Passo 5.3:** Auditoria: Direito do Controlador de auditar o Processador.
        *   *Exemplo:* "O Controlador ou auditor independente por ele indicado poderá realizar auditorias anuais, com aviso prévio de 30 dias, para verificar a conformidade do Processador com o DPA e as leis de proteção de dados."
    *   **Passo 5.4:** Responsabilidade e Indenização.
    *   **Passo 5.5:** Disposições Finais (Lei aplicável, foro).

### Workflow 2: Revisão e Gestão de DPA como Contratante (Controlador)

Este workflow descreve o processo de revisão de um DPA proposto por um prestador de serviços (processador) do ponto de vista de uma empresa que atua como controladora de dados, garantindo que o DPA atenda às suas necessidades de conformidade.

1.  **Análise Preliminar do DPA Recebido:**
    *   **Passo 1.1:** Verifique se o DPA é um documento separado ou parte integrante do Contrato Principal.
        *   *Exemplo:* "O DPA foi enviado como Anexo A ao Contrato de Prestação de Serviços de Marketing Digital."
    *   **Passo 1.2:** Confirme os papéis atribuídos: Sua empresa como **Controlador** e o prestador como **Processador**.
        *   *Exemplo:* "O DPA corretamente designa 'Marketing Pro Ltda.' como Processador e 'Minha Empresa S.A.' como Controlador."
    *   **Passo 1.3:** Compare o escopo do DPA com o serviço contratado.
        *   *Exemplo:* "O DPA cobre o processamento de dados para campanhas de e-mail marketing e gestão de leads, alinhado ao serviço de Marketing Digital."

2.  **Validação do Mapeamento de Dados e Finalidades:**
    *   **Passo 2.1:** Revise a descrição das categorias de dados pessoais.
        *   *Exemplo:* "O DPA lista 'Nome, E-mail, Telefone, Preferências de Produto'. Confirmar se estas são as únicas categorias de dados que serão compartilhadas e se não há dados excessivos."
    *   **Passo 2.2:** Avalie as categorias de titulares.
        *   *Exemplo:* "Titulares: 'Clientes e Potenciais Clientes da Minha Empresa S.A.'. Está correto."
    *   **Passo 2.3:** Garanta que a finalidade do processamento esteja alinhada com a base legal que sua empresa possui.
        *   *Exemplo:* "A finalidade 'Envio de comunicações de marketing' está alinhada com o consentimento que coletamos dos nossos titulares."
    *   **Passo 2.4:** Verifique as disposições sobre a duração do processamento e o destino dos dados.
        *   *Exemplo:* "O DPA prevê exclusão em 60 dias após término. Nossa política interna exige 90 dias para backup. Solicitar ajuste para 90 dias."

3.  **Auditoria das Medidas de Segurança Propostas:**
    *   **Passo 3.1:** Analise as medidas técnicas e organizacionais listadas pelo Processador.
        *   *Exemplo:* "O DPA menciona 'criptografia TLS e controles de acesso'. Precisamos que especifique 'AES-256' para dados em repouso e 'MFA' para acesso administrativo."
    *   **Passo 3.2:** Avalie a adequação das medidas em relação à sensibilidade dos dados e aos riscos.
        *   *Exemplo:* "Para dados de saúde (se aplicável), as medidas propostas são insuficientes. Exigir certificações ISO 27001 ou SOC 2."
    *   **Passo 3.3:** Verifique a existência de um Plano de Resposta a Incidentes de Segurança.
        *   *Exemplo:* "Confirmar se o PRISI do Processador inclui notificação imediata ao Controlador e suporte na mitigação do incidente."

4.  **Verificação de Cláusulas Críticas:**
    *   **Passo 4.1:** Subprocessadores: Exija que o Processador informe *previamente* sobre novos subprocessadores e permita sua objeção.
        *   *Exemplo:* "A cláusula atual permite subprocessadores com notificação posterior. Solicitar alteração para 'notificação prévia com direito de objeção fundamentada'."
    *   **Passo 4.2:** Transferência Internacional: Assegure que o Processador utilize mecanismos de conformidade robustos (SCCs, BCRs).
        *   *Exemplo:* "O DPA apenas diz 'cumprirá as leis'. Exigir menção explícita de SCCs ou BCRs se houver transferência para fora do EEE/Brasil."
    *   **Passo 4.3:** Direitos dos Titulares: Confirme que o Processador auxiliará ativamente no atendimento das solicitações.
        *   *Exemplo:* "A cláusula é passiva. Solicitar que o Processador se comprometa a 'fornecer dados em formato estruturado' para portabilidade, se solicitado."
    *   **Passo 4.4:** Auditoria: Mantenha o direito de auditar o Processador ou exigir relatórios de auditoria independentes.
        *   *Exemplo:* "O DPA prevê auditoria apenas 'com custos do Controlador'. Negociar para que a primeira auditoria anual seja sem custos adicionais."
    *   **Passo 4.5:** Notificação de Incidentes: Prazo máximo de 48 horas após a ciência para incidentes de segurança.
        *   *Exemplo:* "O DPA indica 'sem atraso indevido'. Exigir 'em até 48 horas'."
    *   **Passo 4.6:** Responsabilidade e Indenização: Garanta que a responsabilidade do Processador não seja excessivamente limitada em caso de violação de dados.
        *   *Exemplo:* "A responsabilidade do Processador é limitada ao valor do serviço anual. Negociar para que a limitação seja maior em casos de danos por violação de dados, ou que a cobertura do seguro seja compatível."

---

## Templates

### Cláusula de Finalidade e Base Legal

```markdown
**CLÁUSULA X - ESCOPO E FINALIDADE DO PROCESSAMENTO DE DADOS PESSOAIS**

X.1. Para fins deste DPA, o Controlador ("Varejo Digital S.A.") é o responsável por determinar as finalidades e os meios do tratamento dos dados pessoais, e o Processador ("Tech Solutions Ltda.") tratará os dados pessoais em nome e por conta do Controlador, exclusivamente para a prestação dos serviços de [Nome do Serviço, ex: "gestão de relacionamento com clientes (CRM)"] conforme Contrato Principal.

X.2. As categorias de dados pessoais a serem processados incluem, mas não se limitam a: nome completo, CPF, RG, endereço físico, endereço de e-mail, telefone, histórico de compras e dados de navegação no website do Controlador. As categorias de titulares dos dados são os clientes e potenciais clientes do Controlador.

X.3. O Processador declara estar ciente de que o Controlador é o exclusivo responsável por garantir que todas as atividades de tratamento de dados pessoais estejam fundamentadas em bases legais apropriadas, nos termos da Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD) e/ou do Regulamento Geral de Proteção de Dados (EU 2016/679 - GDPR), quando aplicável, e por obter, quando necessário, o consentimento dos titulares dos dados.

X.4. O Processamento dos dados pessoais pelo Processador terá a duração da prestação dos serviços objeto do Contrato Principal. Ao término ou rescisão do Contrato Principal, o Processador deverá, a critério do Controlador, apagar ou devolver todos os dados pessoais, salvo se houver obrigação legal de retenção.
```

### Cláusula de Medidas de Segurança Técnica e Organizacional

```markdown
**CLÁUSULA Y - MEDIDAS DE SEGURANÇA TÉCNICA E ORGANIZACIONAL**

Y.1. O Processador implementará e manterá medidas de segurança técnicas e organizacionais adequadas para proteger os dados pessoais contra acesso não autorizado, destruição, perda, alteração, divulgação ou qualquer forma de tratamento ilícito ou acidental. Tais medidas incluem, mas não se limitam a:

a)  **Criptografia:** Criptografia de dados em repouso utilizando algoritmos de nível governamental (ex: AES-256) e criptografia em trânsito (ex: TLS 1.2 ou superior) para toda comunicação de dados.
b)  **Controle de Acesso:** Implementação de controle de acesso baseado em função (RBAC) com o princípio do menor privilégio, garantindo que apenas pessoal autorizado tenha acesso aos dados pessoais, e autenticação multifator (MFA) para acesso a sistemas críticos.
c)  **Monitoramento e Auditoria:** Sistemas de detecção de intrusão, prevenção de perda de dados (DLP) e monitoramento de segurança 24/7 com uso de Security Information and Event Management (SIEM) para identificação e resposta a ameaças. Registros de auditoria detalhados sobre o acesso e o tratamento de dados.
d)  **Backup e Recuperação:** Rotinas de backup regulares e testadas, com planos de recuperação de desastres (DRP) para assegurar a disponibilidade e resiliência dos dados.
e)  **Gestão de Vulnerabilidades:** Realização de testes de penetração (pentests) e varreduras de vulnerabilidade periódicas (no mínimo anuais) por terceiros independentes, com correção tempestiva das falhas identificadas.
f)  **Políticas e Treinamento:** Implementação de políticas internas de segurança da informação e privacidade de dados, e treinamento obrigatório e contínuo para todos os funcionários com acesso a dados pessoais sobre as leis de proteção de dados e as melhores práticas de segurança.
g)  **Acordos de Confidencialidade:** Celebração de acordos de confidencialidade (NDAs) com todos os funcionários e subprocessadores que tenham acesso aos dados pessoais.

Y.2. O Processador manterá documentação comprobatória da implementação e eficácia das medidas de segurança mencionadas, disponibilizando-a ao Controlador mediante solicitação para fins de auditoria.
```

---

## Checklist

- [x] O DPA identifica claramente os papéis de Controlador e Processador?
- [x] Todas as categorias de dados pessoais a serem processadas estão detalhadas (ex: PII, dados de uso, dados sensíveis)?
- [x] A finalidade do processamento está explicitamente definida e alinhada ao Contrato Principal?
- [x] As medidas de segurança técnica e organizacional (criptografia, controle de acesso, testes de segurança) são específicas e adequadas à sensibilidade dos dados?
- [x] O DPA exige notificação de incidentes de segurança em um prazo máximo de 48 horas após a ciência?
- [x] Há cláusula que regula o uso de subprocessadores, incluindo a necessidade de autorização prévia ou direito de objeção do Controlador?
- [x] O DPA prevê o direito do Controlador de auditar o Processador ou exigir relatórios de auditoria independentes (ex: SOC 2, ISO 27001)?
- [x] As obrigações do Processador em relação aos direitos dos titulares (acesso, retificação, exclusão, portabilidade) estão claras e exigem assistência ao Controlador?
- [x] O que acontece com os dados ao término do contrato (exclusão segura, devolução, anonimização) está especificado?
- [x] Há previsão para transferências internacionais de dados e quais mecanismos de conformidade serão utilizados (ex: SCCs, BCRs)?
- [x] A responsabilidade e indenização em caso de violação do DPA são equilibradas e adequadas aos riscos envolvidos?
- [x] O DPA está em conformidade com as leis de proteção de dados relevantes (LGPD, GDPR)?

---

## Métricas de Referência

| Métrica                                   | Benchmark (Indústria) | Meta (Exemplo) |
|-------------------------------------------|-----------------------|----------------|
| % de DPAs revisados anualmente            | 90-100%               | 100%           |
| Tempo médio para negociação e assinatura  | 10-15 dias            | 7 dias         |
| % de subprocessadores com DPA vigente     | 95-100%               | 100%           |
| Taxa de incidentes de segurança reportados| < 0.1% ao ano         | 0%             |
| % de auditorias de DPA realizadas         | 25-50% dos críticos   | 30% dos críticos |
| % de cláusulas de segurança específicas   | 80-90%                | 95%            |

---

## Erros Comuns

1.  **DPA Genérico e Não Detalhado**: Utilizar um modelo padrão sem personalizá-lo para as especificidades do serviço e dos dados.
    *   **Como evitar**: Sempre mapeie os dados exatos (categorias, finalidades, titulares) e detalhe as medidas de segurança específicas para aquele contexto. *Exemplo de erro*: "O Processador implementará medidas de segurança adequadas." *Correção*: Especificar "criptografia AES-256 para dados em repouso e MFA para acesso administrativo".

2.  **Não Gerenciar Subprocessadores Adequadamente**: Permitir que o Processador contrate subprocessadores sem autorização prévia ou sem exigir que eles cumpram as mesmas obrigações de proteção de dados.
    *   **Como evitar**: Inclua cláusulas que exijam notificação prévia e direito de objeção do Controlador para a contratação de subprocessadores, e que o Processador seja responsável por garantir a conformidade dos subprocessadores. *Exemplo de erro*: DPA omite subprocessadores. *Correção*: Adicionar "O Processador deverá obter consentimento prévio e por escrito do Controlador para contratar qualquer subprocessador."

3.  **Cláusulas de Responsabilidade e Indenização Desequilibradas**: Aceitar ou propor termos de responsabilidade que limitam excessivamente a indenização do Processador em caso de violação de dados.
    *   **Como evitar**: Negocie a cláusula de responsabilidade para que cubra os danos reais resultantes de uma violação, buscando um equilíbrio que não inviabilize o negócio, mas proteja o Controlador e os titulares. Considere a cobertura de seguro cibernético do Processador. *Exemplo de erro*: "A responsabilidade do Processador é limitada ao valor pago nos últimos 3 meses." *Correção*: Negociar para "A responsabilidade do Processador não será limitada em caso de dolo ou culpa grave, ou danos diretos decorrentes de violação das obrigações de proteção de dados."

---

## Dicas Avançadas

1.  **DPA como Documento Vivo**: Considere o DPA como um documento que precisa ser revisado e atualizado periodicamente, especialmente quando há mudanças nas atividades de processamento, nos tipos de dados, nas tecnologias utilizadas ou nas leis de proteção de dados. Agende revisões anuais ou bienais, ou após grandes mudanças contratuais. *Exemplo Prático*: Após a introdução de um novo módulo no sistema CRM que coleta dados biométricos, revise o DPA para incluir essa nova categoria de dados e as medidas de segurança específicas.

2.  **Integração com Due Diligence de Terceiros**: Incorpore a revisão do DPA como parte integrante do processo de due diligence de segurança e conformidade para qualquer novo fornecedor que processará dados pessoais. Antes mesmo da negociação do contrato principal, solicite o DPA ou um questionário de segurança de dados. *Exemplo Prático*: Ao avaliar um novo provedor de hospedagem, exija o DPA e um relatório de auditoria SOC 2 Type II como pré-requisitos para avançar na contratação.

3.  **Considerações para Processamento de Dados de IA/ML**: Para serviços que envolvem inteligência artificial e machine learning, o DPA deve abordar especificamente como os dados são usados para treinamento de modelos, anonimização/pseudonimização, e como a privacidade é garantida em output de IA. *Exemplo Prático*: O DPA para um serviço de análise preditiva deve incluir cláusulas sobre a não reidentificação de dados anonimizados e a exclusão de dados de treinamento após um período definido, ou a garantia de que o modelo não "memoriza" dados sensíveis.

4.  **Diferenciação entre DPA e Cláusulas Contratuais Padrão (SCCs)**: Entenda que o DPA foca nas obrigações de processamento, enquanto as SCCs (Standard Contractual Clauses) são um mecanismo específico para legitimar transferências internacionais de dados. Muitas vezes, um DPA pode *incorporar* as SCCs ou fazer referência a elas. *Exemplo Prático*: Para um Processador sediado nos EUA que processa dados de clientes da UE, o DPA deve fazer referência às SCCs como o mecanismo para a transferência de dados, e o Anexo das SCCs deve ser parte integrante do DPA.

5.  **Gerenciamento de Riscos de Subprocessadores Aninhados**: Em cadeias de suprimentos complexas, onde seu Processador contrata subprocessadores que, por sua vez, contratam outros, é crucial que o DPA exija que seu Processador imponha obrigações de proteção de dados equivalentes a toda a cadeia. *Exemplo Prático*: O DPA deve conter uma cláusula que obrigue o Processador a garantir que "seus subprocessadores e quaisquer subprocessadores subsequentes cumpram obrigações de proteção de dados substancialmente as mesmas deste DPA". Monitore essa cadeia através de auditorias ou certificações.
---