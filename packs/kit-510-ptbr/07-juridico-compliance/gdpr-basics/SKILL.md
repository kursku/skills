---
name: gdpr-basics
description: "Gdpr Basics — Skill especializada para gdpr basics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: safe
---

# Gdpr Basics

Esta skill equipa o Claude com conhecimento prático e acionável sobre os princípios fundamentais do Regulamento Geral de Proteção de Dados (GDPR) e sua aplicação em contextos empresariais digitais.

---

## Keywords

GDPR, Proteção de Dados, LGPD, DPO, Consentimento, Direitos do Titular, DPIA, Pseudonimização, Anonimização, Controlador, Operador, Violação de Dados, Cláusulas Contratuais Padrão, ROPA, Compliance Digital.

---

## Quick Start

1.  **Mapear fluxos de dados pessoais:** Identificar e documentar onde e como os dados pessoais são coletados, armazenados, processados e compartilhados dentro da organização, utilizando uma ferramenta ou planilha para o Registro de Atividades de Tratamento (ROPA).
2.  **Revisar bases legais:** Para cada atividade de tratamento identificada no mapeamento, determinar e documentar a base legal apropriada conforme o Art. 6º do GDPR (ex: consentimento, execução de contrato, legítimo interesse, obrigação legal).
3.  **Implementar Aviso de Privacidade:** Desenvolver e publicar um aviso de privacidade claro, conciso e acessível no site e/ou aplicativo, detalhando as práticas de tratamento de dados da empresa.
4.  **Estabelecer canais para Direitos dos Titulares:** Criar um formulário online ou um endereço de e-mail dedicado (`privacidade@suaempresa.com`) para que os titulares de dados possam exercer seus direitos (acesso, retificação, exclusão, etc.).

---

## Core Workflows

### Workflow 1: Implementação e Manutenção de um Registro de Atividades de Tratamento (ROPA)

Este workflow detalha a criação e gestão de um ROPA, documento fundamental para demonstrar conformidade com o GDPR (Art. 30).

**Passo 1: Identificação de Atividades de Tratamento de Dados.**
Percorrer todos os departamentos da empresa (RH, Marketing, Vendas, TI, Suporte) e listar todas as operações que envolvem dados pessoais.
*   **Exemplo:**
    *   Departamento de RH: Processamento de dados de funcionários para folha de pagamento, recrutamento.
    *   Departamento de Marketing: Envio de newsletters, segmentação de anúncios, gestão de leads.
    *   Departamento de Vendas: Gestão de clientes em CRM, histórico de compras.
    *   Departamento de Suporte: Atendimento ao cliente, registro de tickets.

**Passo 2: Levantamento Detalhado para Cada Atividade.**
Para cada atividade identificada, coletar as seguintes informações:
*   **Finalidade do Tratamento:** Por que os dados são processados.
    *   *Exemplo:* "Gestão de relacionamento com cliente e suporte técnico."
*   **Categorias de Dados Pessoais:** Tipos de dados coletados.
    *   *Exemplo:* "Nome completo, e-mail, telefone, endereço de entrega, histórico de compras, dados de pagamento (tokenizado)."
*   **Categorias de Titulares dos Dados:** Quem são as pessoas cujos dados são processados.
    *   *Exemplo:* "Clientes, clientes potenciais, usuários do site, funcionários."
*   **Bases Legais para o Tratamento (Art. 6º GDPR):** Justificativa legal.
    *   *Exemplo:* "Execução de contrato (para compras), Consentimento (para newsletter), Legítimo Interesse (para melhoria de serviço)."
*   **Categorias de Destinatários:** Com quem os dados são compartilhados.
    *   *Exemplo:* "Provedor de CRM (Salesforce), Processador de pagamentos (Stripe), Plataforma de e-mail marketing (Mailchimp), Empresas de logística."
*   **Transferências Internacionais (se houver):** Para quais países fora do EEE e qual o mecanismo de salvaguarda (SCCs, Decisão de Adequação).
    *   *Exemplo:* "EUA (Provedor de CRM Salesforce, utilizando Cláusulas Contratuais Padrão da UE)."
*   **Prazos de Retenção:** Por quanto tempo os dados são armazenados.
    *   *Exemplo:* "Dados de clientes: 5 anos após o último contato ou término do contrato, conforme legislação fiscal. Dados de newsletter: Até a revogação do consentimento."
*   **Medidas de Segurança Técnicas e Organizacionais:** Como os dados são protegidos.
    *   *Exemplo:* "Criptografia de dados em trânsito (TLS) e em repouso (AES-256), controle de acesso baseado em função (RBAC), autenticação multifator."

**Passo 3: Documentação no ROPA.**
Consolidar todas as informações em um formato estruturado, como uma planilha ou software de conformidade.
*   **Exemplo de Entrada no ROPA:**
    | Atividade | Finalidade | Dados Pessoais | Titulares | Base Legal | Destinatários | Transf. Intern. | Retenção | Medidas Segurança |
    |---|---|---|---|---|---|---|---|---|
    | Gestão de Clientes CRM | Gerenciar relacionamento, vendas, suporte | Nome, e-mail, telefone, endereço, histórico de compras | Clientes | Execução de Contrato, Legítimo Interesse | Equipe de vendas, suporte, Salesforce | EUA (SCCs) | 5 anos pós-contrato | Criptografia, RBAC, MFA |
    | Envio de Newsletter | Marketing de produtos e promoções | Nome, e-mail | Leads, Clientes | Consentimento | Mailchimp | EUA (SCCs) | Até revogação consentimento | Criptografia |

**Passo 4: Revisão e Atualização Contínua.**
O ROPA não é estático. Revisá-lo anualmente e sempre que houver mudanças significativas nos processos de tratamento de dados, introdução de novos sistemas ou serviços.

### Workflow 2: Resposta a uma Solicitação de Direito do Titular (DSAR - Data Subject Access Request)

Este workflow descreve os passos para gerenciar e responder a solicitações de direitos dos titulares de dados de forma eficaz e dentro do prazo legal.

**Passo 1: Recebimento e Registro da Solicitação.**
A solicitação pode chegar por e-mail, formulário web, carta ou telefone. Registrar imediatamente a data de recebimento para monitorar o prazo de 30 dias.
*   **Exemplo:** Cliente "Ana Souza" envia um e-mail para `privacidade@suaempresa.com` solicitando a exclusão de todos os seus dados pessoais (direito ao esquecimento).

**Passo 2: Verificação da Identidade do Solicitante.**
É crucial confirmar que a pessoa que faz a solicitação é realmente o titular dos dados. Evitar pedir documentos excessivos.
*   **Exemplo:** Enviar um e-mail de retorno para o endereço registrado de Ana Souza, solicitando a confirmação de alguns dados específicos que só ela saberia (ex: os últimos 4 dígitos do CPF usado na compra, um número de pedido recente).

**Passo 3: Localização e Coleta dos Dados Pessoais Relevantes.**
Pesquisar em todos os sistemas onde os dados do titular podem estar armazenados (CRM, banco de dados de marketing, sistema de e-commerce, histórico de suporte, logs, backups).
*   **Exemplo:** Para Ana Souza, buscar em Salesforce, Mailchimp, Stripe, e-commerce Magento, Zendesk. Se a solicitação for de exclusão, identificar todos os locais onde os dados precisam ser removidos ou anonimizados.

**Passo 4: Preparação da Resposta.**
*   **Para Acesso (Direito de Acesso):** Compilar todos os dados coletados em um formato claro, conciso e inteligível (ex: PDF ou JSON). Incluir informações sobre finalidades, categorias de dados, destinatários e prazos de retenção.
*   **Para Exclusão (Direito ao Esquecimento):** Excluir ou anonimizar permanentemente os dados. Se a exclusão não for possível devido a obrigações legais (ex: dados fiscais), explicar o motivo ao titular e o período de retenção necessário.
*   **Para Retificação (Direito de Retificação):** Corrigir os dados conforme a solicitação do titular e notificar terceiros com quem os dados foram compartilhados sobre a retificação.

**Passo 5: Envio da Resposta e Monitoramento do Prazo.**
Enviar a resposta ao titular dentro do prazo legal de 30 dias (prorrogável por mais 60 dias em casos complexos, com notificação prévia ao titular). A comunicação deve ser segura.
*   **Exemplo:** Enviar um e-mail criptografado ou um link para um portal seguro onde Ana Souza possa baixar o arquivo com seus dados ou receber a confirmação da exclusão. Se a exclusão não foi total, explicar as razões e os passos restantes.

---

## Templates

### Modelo de Política de Privacidade (Seção sobre Direitos do Titular)

```
// ... (preâmbulo e outras seções)

## 6. Seus Direitos como Titular de Dados Pessoais

De acordo com o GDPR, você, como titular dos dados, possui direitos específicos em relação aos seus dados pessoais. Estamos comprometidos em garantir que você possa exercê-los. Você pode exercer seus direitos entrando em contato conosco através do e-mail [privacidade@suaempresa.com] ou pelo nosso formulário de contato em [www.suaempresa.com/contato].

Seus direitos incluem:

*   **Direito de Acesso (Art. 15 GDPR):** Você tem o direito de solicitar e obter uma cópia dos dados pessoais que mantemos sobre você.
    *   *Exemplo:* Solicitar um relatório com todo o seu histórico de compras e dados de contato.
*   **Direito de Retificação (Art. 16 GDPR):** Você tem o direito de solicitar a correção de dados incompletos, inexatos ou desatualizados.
    *   *Exemplo:* Corrigir um endereço de entrega ou um número de telefone em seu cadastro.
*   **Direito ao Esquecimento / Exclusão (Art. 17 GDPR):** Você pode solicitar a exclusão de seus dados pessoais quando não houver mais base legal para seu tratamento.
    *   *Exemplo:* Pedir para que seus dados sejam removidos de nossas listas de marketing após cancelar uma assinatura.
*   **Direito à Limitação do Tratamento (Art. 18 GDPR):** Você pode solicitar a suspensão do tratamento de seus dados em certas situações, como quando a exatidão dos dados é contestada.
    *   *Exemplo:* Solicitar que não usemos seus dados para novas campanhas enquanto você verifica a precisão das informações.
*   **Direito à Portabilidade dos Dados (Art. 20 GDPR):** Você tem o direito de receber seus dados pessoais em um formato estruturado, de uso comum e legível por máquina, e de transferir esses dados para outro controlador.
    *   *Exemplo:* Receber um arquivo CSV com seu histórico de transações para migrar para outro serviço.
*   **Direito de Oposição (Art. 21 GDPR):** Você pode se opor ao tratamento de seus dados pessoais, especialmente quando o tratamento se baseia em legítimo interesse ou para fins de marketing direto.
    *   *Exemplo:* Recusar-se a receber e-mails de marketing, mesmo que tenha dado consentimento anteriormente.
*   **Direito de Retirar o Consentimento (Art. 7(3) GDPR):** Se o tratamento de seus dados for baseado em seu consentimento, você tem o direito de retirá-lo a qualquer momento, sem afetar a legalidade do tratamento anterior à retirada.
    *   *Exemplo:* Desinscrever-se de uma newsletter clicando no link "cancelar inscrição".
*   **Direito de Reclamar à Autoridade de Controle (Art. 77 GDPR):** Você tem o direito de apresentar uma reclamação a uma autoridade de supervisão se considerar que o tratamento de seus dados pessoais viola o GDPR. No Brasil, esta é a Autoridade Nacional de Proteção de Dados (ANPD).

Responderemos a todas as solicitações válidas dentro de 30 dias a partir da data de recebimento, podendo estender esse prazo por mais 60 dias em casos de alta complexidade, mediante notificação.

// ... (outras seções)
```

### Modelo de Cláusula para Acordo de Processamento de Dados (DPA - Data Processing Agreement)

```
// Exemplo de Cláusula Essencial em um Acordo de Processamento de Dados (DPA)

**ACORDO DE PROCESSAMENTO DE DADOS**

Este Acordo de Processamento de Dados ("DPA") é celebrado entre:

**CONTROLADOR DE DADOS:** [Nome Completo da Empresa Controladora], com sede em [Endereço Completo], inscrita no CNPJ/NIF sob o nº [Número], doravante denominado "Controlador".

E

**PROCESSADOR DE DADOS:** [Nome Completo da Empresa Processadora], com sede em [Endereço Completo], inscrita no CNPJ/NIF sob o nº [Número], doravante denominado "Processador".

(O Controlador e o Processador serão doravante denominados individualmente "Parte" e coletivamente "Partes").

**CONSIDERANDO QUE:**
*   O Controlador engaja o Processador para prestar serviços conforme o Contrato de Serviços principal (o "Contrato Principal").
*   No âmbito da prestação desses serviços, o Processador tratará dados pessoais em nome do Controlador.
*   As Partes desejam estabelecer os termos e condições para o tratamento de dados pessoais de acordo com as exigências do Regulamento (UE) 2016/679 (Regulamento Geral de Proteção de Dados - "GDPR") e demais leis de proteção de dados aplicáveis.

**AS PARTES CONCORDAM NO SEGUINTE:**

**1. Objeto do DPA**

Este DPA define as obrigações e direitos das Partes no que diz respeito ao tratamento de Dados Pessoais pelo Processador em nome do Controlador, em conexão com a prestação dos serviços descritos no Contrato Principal.

**2. Detalhes do Tratamento de Dados Pessoais**

2.1. **Categorias de Dados Pessoais:** [**Exemplo: Nome, e-mail, telefone, endereço, dados de uso do serviço, dados de localização, informações de faturamento, dados de perfil de usuários finais.**]

2.2. **Categorias de Titulares dos Dados:** [**Exemplo: Clientes do Controlador, usuários do site/aplicativo do Controlador, funcionários do Controlador.**]

2.3. **Finalidades do Tratamento:** O Processador tratará os Dados Pessoais exclusivamente para as finalidades especificadas no Contrato Principal, que incluem, mas não se limitam a: [**Exemplo: Hospedagem de dados, envio de e-mails transacionais, processamento de pagamentos, análise de desempenho de aplicativos, suporte técnico.**]

2.4. **Duração do Tratamento:** O tratamento dos Dados Pessoais será realizado pelo período em que o Contrato Principal estiver em vigor e, após seu término, conforme as instruções do Controlador e as obrigações legais de retenção.

**3. Obrigações do Processador**

O Processador concorda em:

3.1. **Agir Apenas sob Instrução Documentada do Controlador:** O Processador tratará os Dados Pessoais apenas de acordo com as instruções documentadas do Controlador, a menos que seja exigido por lei da União ou do Estado-Membro a que o Processador esteja sujeito. Nesse caso, o Processador informará o Controlador sobre essa exigência legal antes do tratamento, salvo se a lei proibir tal informação por motivos relevantes de interesse público.

3.2. **Confidencialidade:** Garantir que as pessoas autorizadas a tratar os Dados Pessoais se comprometam a manter a confidencialidade ou estejam sujeitas a uma obrigação legal de confidencialidade apropriada.

3.3. **Segurança do Tratamento:** Implementar medidas técnicas e organizacionais adequadas para garantir um nível de segurança apropriado ao risco, incluindo, quando apropriado:
    *   Pseudonimização e criptografia de dados pessoais.
    *   Capacidade de garantir a confidencialidade, integridade, disponibilidade e resiliência contínuas dos sistemas e serviços de tratamento.
    *   Capacidade de restaurar a disponibilidade e o acesso aos dados pessoais em tempo hábil em caso de incidente físico ou técnico.
    *   Um processo para testar, avaliar e avaliar regularmente a eficácia das medidas técnicas e organizacionais para garantir a segurança do tratamento.
    *   [**Exemplo de Medidas:** Criptografia AES-256 para dados em repouso; TLS 1.2+ para dados em trânsito; controle de acesso baseado em função (RBAC); autenticação multifator (MFA); auditorias de segurança regulares; planos de recuperação de desastres; treinamento de segurança para funcionários.]

3.4. **Subcontratação:** Não contratar outro processador (subprocessador) sem a autorização específica ou geral por escrito do Controlador. Se autorizada uma subcontratação geral, o Processador informará o Controlador sobre quaisquer mudanças pretendidas na adição ou substituição de subprocessadores. O Processador garantirá que o subprocessador esteja sujeito às mesmas obrigações de proteção de dados que as estabelecidas neste DPA.

3.5. **Assistência ao Controlador:** Prestar assistência razoável ao Controlador para o cumprimento das obrigações do Controlador em relação a:
    *   Resposta a solicitações de direitos dos titulares dos dados.
    *   Avaliações de Impacto sobre a Proteção de Dados (DPIA).
    *   Notificação de violações de dados pessoais à autoridade de controle e aos titulares dos dados.

3.6. **Notificação de Violações de Dados Pessoais:** Notificar o Controlador sem demora indevida após tomar conhecimento de uma violação de dados pessoais.

3.7. **Devolução ou Exclusão de Dados:** Após o término da prestação dos serviços relacionados ao tratamento, o Processador, a critério do Controlador, deverá excluir ou devolver todos os Dados Pessoais ao Controlador e apagar as cópias existentes, a menos que a lei exija a retenção dos Dados Pessoais.

**4. Auditorias**

O Processador disponibilizará ao Controlador todas as informações necessárias para demonstrar o cumprimento das obrigações