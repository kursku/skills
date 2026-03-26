---
name: api-terms
description: "Api Terms — Skill especializada para api terms"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: offensive
---

# Api Terms

Esta skill capacita o Claude a elaborar, analisar e gerenciar Termos de Uso e Políticas de Privacidade para APIs, assegurando conformidade legal e mitigando riscos operacionais e jurídicos.

---

## Keywords

Termos de API, Licenciamento de API, Política de Uso Aceitável (AUP), LGPD, GDPR, Compliance Digital, Contrato de API, Propriedade Intelectual em API, Limitação de Responsabilidade, SLA de API, Proteção de Dados, Monitoramento de Uso de API, Rescisão de Acesso, Notificação de Violação de Dados.

---

## Quick Start

1.  **Mapear Funcionalidades e Dados da API**: Liste os endpoints, recursos acessados (ex: `/users`, `/products/{id}`), e os tipos de dados processados (ex: dados pessoais, financeiros, transacionais).
2.  **Definir Modelo de Licenciamento**: Escolha entre licença gratuita, freemium, paga, ou por assinatura, especificando os direitos e restrições de uso para cada modelo.
3.  **Estabelecer Política de Uso Aceitável**: Detalhe proibições claras como engenharia reversa, uso para fins ilícitos, scraping massivo, e limites de requisição (rate limits).
4.  **Identificar Requisitos Regulatórios**: Determine as leis de proteção de dados (LGPD, GDPR) e regulamentações setoriais aplicáveis com base na origem e destino dos dados e usuários.
5.  **Esboçar Cláusulas Essenciais**: Comece com cláusulas de propriedade intelectual, limitação de responsabilidade, indenização, e as disposições sobre lei aplicável e foro.

---

## Core Workflows

### Workflow 1: Elaboração de Termos de Uso para API Pública de SaaS

Este workflow detalha o processo de criação de Termos de Uso abrangentes para uma API de um serviço SaaS que permite a integração de funcionalidades de gestão de clientes e vendas com sistemas de terceiros.

1.  **Análise de Escopo da API e Tratamento de Dados**:
    *   **Identificação de Endpoints e Recursos**: Mapear todos os endpoints expostos, como `GET /customers`, `POST /orders`, `PUT /products/{id}`, e `DELETE /users/{id}`.
    *   **Tipos de Dados Processados**: Listar os dados que transitam pela API, especificando se são dados pessoais (nome, email, CPF, endereço), dados de transação (valor, data, produtos), ou dados técnicos (IP, user-agent).
    *   **Finalidade do Tratamento**: Descrever como cada tipo de dado é utilizado (ex: `GET /customers` para sincronizar lista de clientes; `POST /orders` para registrar novas vendas).
    *   **Exemplo Prático**: Para a API `CRMConnect` que expõe `GET /customers` e `POST /leads`, os dados processados incluem `nome`, `email`, `telefone`, `empresa` (pessoais) e `origem_lead`, `status_lead` (transacionais). O objetivo é permitir que parceiros integrem seus sistemas para gerenciar contatos e oportunidades de vendas.

2.  **Definição de Regras de Acesso e Uso Aceitável**:
    *   **Mecanismos de Autenticação**: Especificar o protocolo de segurança (ex: OAuth 2.0, API Keys) e requisitos para a gestão de credenciais.
    *   **Limites de Requisição (Rate Limiting)**: Estabelecer limites claros para evitar abusos e garantir a estabilidade do serviço (ex: "máximo de 100 requisições por minuto por chave de API").
    *   **Proibições Explícitas**: Listar atividades estritamente proibidas, como engenharia reversa, tentar acessar dados não autorizados, uso para fins de spam, scraping massivo, revenda não autorizada da API, ou introdução de malware.
    *   **Exemplo Prático**: "O acesso à API `CRMConnect` requer autenticação via `OAuth 2.0` com tokens de acesso de curta duração. O uso é limitado a `100 requisições/minuto/aplicação`. É expressamente proibida a utilização da API para envio de mensagens de marketing não solicitado ('spam'), para mineração de dados ('data scraping') de forma massiva, ou para a criação de serviços concorrentes diretos sem permissão expressa."

3.  **Elaboração de Cláusulas de Propriedade Intelectual**:
    *   **Titularidade da API**: Declarar que a API, seu código-fonte, documentação e todos os direitos de propriedade intelectual associados pertencem exclusivamente ao provedor.
    *   **Licença de Uso Concedida**: Conceder ao desenvolvedor uma licença limitada, revogável, não exclusiva, intransferível para usar a API estritamente de acordo com os termos.
    *   **Exemplo Prático**: "O PROVEDOR detém todos os direitos, títulos e interesses sobre a API `CRMConnect`, incluindo, mas não se limitando, a direitos autorais, patentes, marcas registradas e segredos comerciais. O CONSUMIDOR recebe uma licença limitada, não exclusiva e intransferível para acessar e usar a API exclusivamente para os fins permitidos nestes Termos."

4.  **Inclusão de Cláusulas de Privacidade e Proteção de Dados (LGPD/GDPR)**:
    *   **Referência à Política de Privacidade Principal**: Vincular os Termos de API à Política de Privacidade geral da empresa para detalhes sobre o tratamento de dados pessoais.
    *   **Definição de Papéis (Controlador/Operador)**: Esclarecer as responsabilidades de cada parte em relação aos dados pessoais processados via API, geralmente o provedor como Operador e o consumidor como Controlador.
    *   **Medidas de Segurança**: Exigir que o consumidor implemente medidas de segurança adequadas ao manusear dados obtidos pela API.
    *   **Exemplo Prático**: "O tratamento de dados pessoais realizado através da API `CRMConnect` está sujeito à Política de Privacidade do PROVEDOR, disponível em [URL da Política de Privacidade]. Para os dados pessoais acessados e processados pelo CONSUMIDOR via API, o CONSUMIDOR atua como CONTROLADOR e o PROVEDOR como OPERADOR, sendo o CONSUMIDOR o único responsável por garantir a base legal para o tratamento e a conformidade com a LGPD e o GDPR, quando aplicável. O CONSUMIDOR deverá implementar medidas técnicas e organizacionais robustas para proteger os dados pessoais."

5.  **Definição de Limitação de Responsabilidade e Indenização**:
    *   **"As Is" Clause**: Declarar que a API é fornecida "no estado em que se encontra", sem garantias de funcionalidade ininterrupta ou livre de erros.
    *   **Limitação de Danos**: Restringir a responsabilidade do provedor a danos diretos e excluir responsabilidades por lucros cessantes, danos indiretos ou consequenciais.
    *   **Obrigação de Indenizar**: Exigir que o consumidor indenize o provedor por quaisquer danos decorrentes do uso indevido da API ou violação dos termos.
    *   **Exemplo Prático**: "A API `CRMConnect` é fornecida 'no estado em que se encontra' e 'conforme disponível', sem garantias de qualquer tipo. Em nenhuma circunstância o PROVEDOR será responsável por quaisquer danos indiretos, incidentais, especiais, consequenciais ou punitivos, incluindo lucros cessantes, resultantes do uso ou incapacidade de usar a API. O CONSUMIDOR concorda em indenizar e isentar o PROVEDOR de todas e quaisquer reivindicações, responsabilidades, danos, perdas e despesas decorrentes de seu uso da API que viole estes Termos."

### Workflow 2: Revisão de Conformidade LGPD/GDPR para API Existente de Pagamentos

Este workflow foca na auditoria e ajuste dos termos e da operação de uma API de processamento de pagamentos para garantir conformidade com a LGPD e o GDPR, dadas as sensibilidades dos dados financeiros e pessoais envolvidos.

1.  **Mapeamento Detalhado de Dados Pessoais e Sensíveis**:
    *   **Identificação de Dados**: Listar todos os dados pessoais e sensíveis que a API `PaymentGateway` processa (ex: nome do titular do cartão, CPF/CNPJ, número do cartão, data de validade, CVV, endereço de cobrança, IP do comprador).
    *   **Fluxo de Dados**: Desenhar o fluxo de dados desde a coleta pelo sistema do parceiro, passando pela API, até o processamento interno e armazenamento.
    *   **Exemplo Prático**: A API `PaymentGateway` recebe `nome_cliente`, `cpf_cnpj`, `numero_cartao`, `validade_cartao`, `cvv`, `endereco_cobranca` e `ip_transacao`. Estes dados são enviados via endpoint `POST /transactions` para processamento e repassados a adquirentes e bancos.

2.  **Verificação de Base Legal e Consentimento**:
    *   **Base Legal para Cada Tratamento**: Para cada tipo de dado pessoal, verificar qual a base legal aplicável (art. 7 LGPD / art. 6 GDPR): execução de contrato, cumprimento de obrigação legal, consentimento, legítimo interesse, etc.
    *   **Consentimento Explícito para Dados Sensíveis**: Confirmar se o consentimento explícito é obtido do titular para dados sensíveis ou para tratamentos que não se encaixam em outras bases legais robustas.
    *   **Exemplo Prático**: Para `numero_cartao`, a base legal é `execução de contrato` (processar o pagamento solicitado). Para `IP_transacao`, pode ser `legítimo interesse` (prevenção de fraude) ou `cumprimento de obrigação legal` (registros de acesso). Se a API coletar dados biométricos para autenticação, o `consentimento explícito` do titular seria obrigatório, com um termo de consentimento específico.

3.  **Implementação e Documentação dos Direitos dos Titulares**:
    *   **Mecanismos para Exercício de Direitos**: Garantir que a API e sistemas relacionados suportam requisições de titulares de dados (ex: acesso, retificação, exclusão, portabilidade).
    *   **Exemplo Prático**: O endpoint `DELETE /customers/{id}` deve ser capaz de remover dados de clientes, ou pelo menos anonimizá-los, conforme requisição de exclusão. A documentação da API e os Termos devem descrever como os parceiros devem encaminhar ou processar tais requisições dos titulares.

4.  **Avaliação das Medidas de Segurança da Informação**:
    *   **Padrões de Segurança**: Verificar se a API e a infraestrutura seguem padrões como PCI DSS (para pagamentos), ISO 27001, e utilizam criptografia forte (TLS 1.2+, criptografia em repouso para dados sensíveis).
    *   **Monitoramento e Auditoria**: Confirmar que existem logs de acesso e auditoria para todas as operações críticas da API.
    *   **Exemplo Prático**: A API `PaymentGateway` deve impor o uso de TLS 1.2+ para todas as comunicações. Dados de cartão devem ser tokenizados ou criptografados em repouso. Os logs de acesso devem registrar `IP`, `timestamp`, `usuário_api` e `endpoint_acessado` para todas as chamadas.

5.  **Revisão de Transferência Internacional de Dados**:
    *   **Identificação de Transferências**: Se dados pessoais são transferidos para fora da jurisdição original (ex: EUA, Europa), identificar os países de destino.
    *   **Mecanismos de Adequação**: Verificar a existência de mecanismos de adequação (Cláusulas Contratuais Padrão da UE, certificações, decisões de adequação) e a sua inclusão nos Termos de API ou em aditivos contratuais.
    *   **Exemplo Prático**: Se os dados de `PaymentGateway` são processados por um parceiro na Irlanda (membro da UE) para clientes brasileiros, a transferência é interna ao regime GDPR. Se o processador for nos EUA, cláusulas contratuais padrão da UE (SCCs) ou outro mecanismo de adequação devem estar em vigor e explicitados nos termos.

6.  **Necessidade de Relatório de Impacto à Proteção de Dados (RIPD/DPIA)**:
    *   **Avaliação de Risco**: Determinar se o tratamento de dados pela API apresenta alto risco aos direitos e liberdades dos titulares, exigindo um RIPD (art. 38 LGPD / art. 35 GDPR).
    *   **Exemplo Prático**: Uma API de pagamentos que processa grande volume de dados sensíveis e pode resultar em danos significativos em caso de violação, como a `PaymentGateway`, provavelmente exige a elaboração de um RIPD detalhado, que deve ser referenciado nos termos ou sua conclusão sumarizada.

---

## Templates

### Cláusula de Licenciamento de API e Uso Aceitável

```markdown
**3. LICENÇA DE USO DA API E RESTRIÇÕES**

3.1. O PROVEDOR concede ao CONSUMIDOR, por meio deste Termo e mediante estrita conformidade com suas disposições, uma licença limitada, revogável, não exclusiva, intransferível e não sublicenciável para acessar e utilizar a API [Nome da API, ex: "CRMConnect"] e a documentação associada, exclusivamente para o desenvolvimento e operação de aplicações que se integrem aos serviços do PROVEDOR e para fins legítimos e compatíveis com a proposta da API.

3.2. É expressamente proibido ao CONSUMIDOR, direta ou indiretamente:
    a) Realizar engenharia reversa, descompilar, desmontar ou de qualquer outra forma tentar derivar o código-fonte da API;
    b) Utilizar a API para enviar spam, mensagens não solicitadas ou qualquer conteúdo ilícito, difamatório, ameaçador, obsceno ou que viole direitos de terceiros;
    c) Exceder os limites de requisição ('rate limits') estabelecidos pelo PROVEDOR (atualmente, 100 requisições por minuto por chave de API), ou tentar contornar quaisquer medidas de segurança ou restrições de acesso;
    d) Usar a API para propósitos de mineração de dados ('data scraping') de forma massiva ou sistemática;
    e) Comercializar, revender, alugar, sublicenciar ou de qualquer outra forma disponibilizar a API ou qualquer de suas funcionalidades a terceiros sem a expressa autorização por escrito do PROVEDOR;
    f) Desenvolver ou operar aplicações que concorram diretamente com os serviços do PROVEDOR utilizando a API, sem prévia autorização.

3.3. Qualquer uso da API que viole estas condições resultará na suspensão imediata e/ou rescisão do acesso do CONSUMIDOR, sem prejuízo das medidas legais cabíveis.
```

### Cláusula de Proteção de Dados (LGPD/GDPR para APIs)

```markdown
**7. PROTEÇÃO DE DADOS PESSOAIS**

7.1. As partes reconhecem que, no âmbito da utilização da API [Nome da API, ex: "PaymentGateway"], dados pessoais poderão ser processados. O tratamento de tais dados estará em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD) e, quando aplicável, com o Regulamento Geral de Proteção de Dados (UE) 2016/679 (GDPR).

7.2. Para os dados pessoais acessados, coletados e/ou processados pelo CONSUMIDOR através da API, o CONSUMIDOR atuará como **CONTROLADOR** e o PROVEDOR como **OPERADOR**, nos termos da legislação aplicável. O CONSUMIDOR é o único responsável por garantir que possui base legal adequada para o tratamento dos dados pessoais que encaminha ou acessa via API, incluindo, se necessário, o consentimento explícito dos titulares.

7.3. O PROVEDOR, como OPERADOR, compromete-se a tratar os dados pessoais estritamente de acordo com as instruções do CONSUMIDOR e as finalidades estabelecidas neste Termo e na Política de Privacidade do PROVEDOR, implementando medidas técnicas e organizacionais de segurança da informação apropriadas para proteger os dados contra acesso não autorizado, alteração, divulgação ou destruição.

7.4. O CONSUMIDOR compromete-se a implementar e manter medidas de segurança da informação robustas para proteger os dados pessoais obtidos através da API e a notificar o PROVEDOR em até 48 (quarenta e oito) horas sobre qualquer incidente de segurança envolvendo dados acessados via API que possa resultar em risco ou dano aos titulares, nos termos do Art. 48 da LGPD.

7.5. O CONSUMIDOR deverá responder prontamente a quaisquer requisições de titulares de dados referentes ao exercício de seus direitos (acesso, retificação, exclusão, portabilidade, etc.) relacionados aos dados processados via API, e, se aplicável, solicitar o apoio do PROVEDOR para tais requisições, conforme os procedimentos estabelecidos na documentação da API ou acordos de suporte.
```

---

## Checklist

- [x] API Terms vinculados à Política de Privacidade principal da organização?
- [x] Propriedade Intelectual da API e dados gerados claramente definida (titularidade e licenciamento)?
- [x] Limitações de uso da API (rate limits, scraping, uso comercial) explícitas e detalhadas?
- [x] Cláusula de responsabilidade civil e indenização presente, com escopo de danos limitado?
- [x] Lei aplicável e foro de resolução de disputas definidos de forma inequívoca?
- [x] Conformidade com LGPD/GDPR para todos os dados pessoais processados via API, com papéis (controlador/operador) claros?
- [x] Mecanismos para atendimento aos direitos dos titulares de dados (acesso, retificação, exclusão) implementados e documentados?
- [x] Políticas de segurança da informação (ex: criptografia TLS, armazenamento seguro de credenciais) mencionadas ou requeridas para o consumidor?
- [x] Processo de notificação de incidentes de segurança ou violação de dados especificado para ambas as partes?
- [x] Termos de rescisão do acesso à API claros, incluindo as consequências para os dados e a aplicação do consumidor?
- [x] Cláusulas sobre monitoramento do uso da API pelo provedor para fins de conformidade e segurança?
- [x] Versionamento dos Termos de API e política de notificação de mudanças aos usuários documentados?

---

## Métricas de Referência

| Métrica                                | Benchmark        | Meta             |
|----------------------------------------|------------------|------------------|
| Tempo médio de revisão legal de ToS    | 5-7 dias úteis   | <4 dias úteis    |
| Índice de conformidade LGPD/GDPR (auditoria) | >90%             | >98%             |
| % de APIs com ToS customizados         | >80%             | >95%             |
| % de usuários que aceitam ToS (novas contas) | >99%             | >99.5%           |
| Nível de incidentes de uso indevido/mês | <0.1% do total de usuários ativos | <0.05%          |
| % de cláusulas de segurança da informação robustas | >70%             | >90%             |

---

## Erros Comuns

1.  **Termos genéricos não alinhados à funcionalidade da API**: Utilizar templates de Termos de Uso que não refletem as especificidades da API, seus endpoints, tipos de dados ou modelo de negócio.
    *   **Como evitar**: Detalhar minuciosamente as funcionalidades da API, os tipos de dados que trafegam, e os casos de uso esperados. Por exemplo, em vez de "uso indevido", especificar "uso para scraping massivo de dados de perfil" ou "tentativa de acesso a recursos não autorizados via endpoint `/admin`".

2.  **Ausência de cláusulas claras sobre segurança e notificação de incidentes de dados**: Falha em especificar as responsabilidades de ambas as partes sobre a segurança dos dados e o procedimento em caso de uma violação.
    *   **Como evitar**: Incluir cláusulas que exijam que o consumidor implemente medidas de segurança adequadas e notifique o provedor em um prazo específico (ex: 48 horas) sobre qualquer incidente de segurança envolvendo dados acessados via API. Ex: "O CONSUMIDOR compromete-se a implementar e manter medidas de segurança da informação compatíveis com as melhores práticas de mercado e a notificar o PROVEDOR em até 48 (quarenta e oito) horas sobre qualquer incidente de segurança envolvendo dados acessados via API, fornecendo todos os detalhes relevantes para a investigação."

3.  **Não abordar a distinção entre controlador e operador de dados na LGPD/GDPR**: A confusão sobre os papéis pode levar a lacunas de responsabilidade e não conformidade, especialmente com APIs que processam dados pessoais.
    *   **Como evitar**: Deixar explícito nos termos qual parte assume o papel de Controlador e qual o de Operador para os dados pessoais processados pela API, e as respectivas responsabilidades. Ex: "Para os dados pessoais processados via API [Nome da API], o PROVEDOR atua como OPERADOR e o CONSUMIDOR como CONTROLADOR, sendo este último o responsável principal pelas decisões de tratamento e pela garantia da base legal em conformidade com a LGPD/GDPR."

---

## Dicas Avançadas

1.  **Versionamento e Notificação Proativa de Mudanças**: Mantenha um sistema claro de versionamento para seus Termos de API e políticas relacionadas. Notifique os desenvolvedores e usuários com um prazo razoável (ex: 30 a 60 dias) antes que as mudanças significativas entrem em vigor, utilizando e-mail, dashboard do desenvolvedor e canais de comunicação da comunidade. Isso minimiza surpresas e permite que os usuários se adaptem.
2.  **Integração com Ferramentas de Gerenciamento de Consentimento (CMP)**: Para APIs que lidam com dados pessoais e exigem consentimento explícito, considere integrar a aceitação dos termos e políticas com uma plataforma de Gerenciamento de Consentimento (CMP). Isso automatiza a coleta, registro e gerenciamento dos consentimentos, facilitando a comprovação de conformidade e o atendimento aos direitos dos titulares.
3.  **Cláusulas de Auditoria e Monitoramento de Conformidade**: Inclua nos Termos o direito do provedor de auditar o uso da API pelo consumidor, seja por meio de logs de acesso, relatórios do próprio consumidor ou auditorias externas, para garantir a conformidade com as regras de uso e segurança. Além disso, reserve o direito de monitorar o tráfego da API para detecção de abusos e padrões de uso inadequados.
4.  **SLA (Service Level Agreement) Separado para APIs Críticas**: Para APIs que são mission-critical para os negócios dos consumidores, considere elaborar um SLA detalhado em um documento anexo aos Termos de Uso. O SLA deve abordar métricas de disponibilidade (ex: 99.9% uptime), tempo de resposta do suporte, e penalidades por não cumprimento. Referencie este SLA nos Termos principais, garantindo que o consumidor esteja ciente das condições de serviço.
5.  **Gerenciamento de Jurisdição e Disputas Multiterritoriais**: Para APIs com alcance global, a cláusula de lei aplicável e foro pode ser complexa. Considere incluir uma cláusula de arbitragem vinculativa como método primário de resolução de disputas, ou especificar foros que minimizem a complexidade legal em diferentes jurisdições, como a escolha de um tribunal em uma jurisdição neutra ou de renome internacional para disputas comerciais.