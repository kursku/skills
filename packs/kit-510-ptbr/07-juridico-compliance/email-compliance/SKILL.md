---
name: email-compliance
description: "Email Compliance — Skill especializada para email compliance"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Email Compliance

Esta skill capacita o Claude a implementar e auditar estratégias de conformidade legal e regulatória para comunicações por email, focando em LGPD, GDPR e melhores práticas anti-SPAM.

---

## Keywords

LGPD, GDPR, CAN-SPAM, ePrivacy, Opt-in, Opt-out, DMARC, SPF, DKIM, Consentimento, Retenção de Dados, Anti-SPAM, Direitos do Titular, Privacidade por Design.

---

## Quick Start

1.  Analisar a base de dados de emails para identificar e documentar a origem e a base legal do consentimento de cada contato existente.
2.  Implementar um mecanismo de dupla confirmação (double opt-in) obrigatório para todas as novas inscrições em newsletters ou listas de marketing.
3.  Revisar todos os modelos de email marketing e transacionais para garantir a inclusão de links de descadastro claros, visíveis e funcionais no rodapé.
4.  Configurar e validar os registros de autenticação de email (SPF, DKIM, DMARC) nos servidores de envio para melhorar a reputação e entregabilidade.
5.  Documentar e comunicar a política de retenção de dados para emails e logs de comunicação, garantindo a conformidade com solicitações de exclusão.

---

## Core Workflows

### Workflow 1: Implementação e Gestão de Consentimento para Email Marketing (LGPD/GDPR)

Este workflow detalha a criação e manutenção de um processo robusto de coleta e gestão de consentimento para emails de marketing, essencial para conformidade com LGPD e GDPR.

1.  **Mapeamento de Bases Legais por Tipo de Comunicação:**
    *   **Ação:** Identificar a base legal específica para cada tipo de comunicação por email antes do envio.
    *   **Exemplo:** Para newsletters promocionais, a base legal é o **consentimento** explícito. Para notificações de transação (ex: confirmação de compra), a base legal é a **execução de contrato**. Para atualizações de política de privacidade, pode ser **legítimo interesse** ou **obrigação legal**.
2.  **Desenho de Formulários de Captação com Consentimento Explícito:**
    *   **Ação:** Garantir que todos os formulários de inscrição para listas de email marketing (website, landing pages) contenham checkboxes *não pré-marcadas* para consentimento de marketing. O texto deve ser claro, específico e vincular à política de privacidade.
    *   **Exemplo:** Em um formulário de cadastro, apresentar a opção: `[ ] Concordo em receber comunicações de marketing e ofertas exclusivas da [Nome da Empresa] e li a Política de Privacidade.` O checkbox deve ser explicitamente clicado pelo usuário.
3.  **Implementação de Double Opt-in (Confirmação Dupla):**
    *   **Ação:** Após o preenchimento inicial do formulário, enviar um email de confirmação para o endereço fornecido. O usuário deve clicar em um link contido neste email para validar e ativar sua inscrição.
    *   **Exemplo:** O sistema de email marketing envia automaticamente um email com o assunto "Confirme sua inscrição na newsletter de [Nome da Empresa]" e um link único de confirmação. A inscrição só é ativada após o clique.
4.  **Registro Auditável de Consentimento:**
    *   **Ação:** Armazenar de forma segura e auditável todos os detalhes do consentimento: data e hora exatas, endereço IP do usuário, URL do formulário de origem, e o texto exato da declaração de consentimento aceita.
    *   **Exemplo:** Um registro de banco de dados para o contato 'joao.silva@email.com' deve conter: `ID_Contato: 12345, Email: joao.silva@email.com, Consentimento_Marketing: TRUE, Data_Hora_Consentimento: 2023-10-27 14:35:01 BRT, IP_Origem: 192.168.1.10, Formulario_Origem: /cadastro-newsletter, Texto_Consentimento: "Concordo em receber comunicações de marketing..."`
5.  **Auditoria Periódica da Base de Dados de Consentimento:**
    *   **Ação:** Revisar trimestralmente os registros de consentimento para garantir a precisão, identificar contatos sem base legal clara e remover aqueles que solicitaram descadastro ou exclusão definitiva.
    *   **Exemplo:** Executar um script que identifica contatos na lista de marketing cuja data de consentimento é anterior à data de implementação do double opt-in e não possuem registro de consentimento explícito, marcando-os para reengajamento com pedido de novo consentimento ou remoção.

### Workflow 2: Gerenciamento de Descadastro, Retenção e Direitos do Titular (LGPD/CAN-SPAM)

Este workflow foca em garantir que os usuários possam facilmente exercer seus direitos de descadastro e exclusão, e que a empresa cumpra as políticas de retenção de dados.

1.  **Garantia de Link de Descadastro Claro e Visível:**
    *   **Ação:** Todos os emails promocionais e de marketing devem conter um link de descadastro (unsubscribe) em destaque, geralmente no rodapé, com texto claro e fácil de entender.
    *   **Exemplo:** No rodapé do email, incluir o texto: "Não deseja mais receber nossos emails? Cancele sua inscrição aqui." [Link de Descadastro]
2.  **Processo de Descadastro Imediato e Simplificado:**
    *   **Ação:** O descadastro deve ser processado imediatamente após a solicitação do usuário, sem a necessidade de login, preenchimento de formulários adicionais ou múltiplas etapas. A conformidade com CAN-SPAM exige no máximo 10 dias úteis, mas a boa prática e LGPD/GDPR sugerem imediaticidade.
    *   **Exemplo:** Ao clicar no link de descadastro, o usuário é direcionado para uma página de confirmação simples "Sua solicitação de descadastro foi processada com sucesso." e é removido da lista de envios em tempo real.
3.  **Confirmação Opcional de Descadastro e Gestão de Preferências:**
    *   **Ação:** Opcionalmente, enviar um email de confirmação de descadastro. Oferecer uma página de gerenciamento de preferências permite que o usuário pause ou reduza a frequência em vez de descadastrar totalmente.
    *   **Exemplo:** Após o descadastro, o sistema envia: "Confirmamos que você foi descadastrado de nossa lista de marketing. Se desejar, você pode gerenciar suas preferências aqui [Link para Preferências] ou se inscrever novamente a qualquer momento."
4.  **Política de Retenção de Dados Pós-descadastro:**
    *   **Ação:** Manter um registro do descadastro por um período razoável (ex: 5 anos) para fins de auditoria e para garantir que o contato não seja reincluído acidentalmente em campanhas futuras. Os dados de marketing ativo devem ser marcados como "não contatar".
    *   **Exemplo:** O sistema mantém o registro do email 'maria.souza@email.com' com um status 'DESCADASTRADO' e a data de descadastro '2024-01-15', garantindo que não seja alvo de envios futuros, mas mantendo a prova do consentimento anterior para auditoria.
5.  **Processo de Exclusão Definitiva (Direito ao Esquecimento):**
    *   **Ação:** Implementar um procedimento claro para atender às solicitações de exclusão definitiva de dados pessoais (Direito ao Esquecimento) dos titulares, removendo todos os dados não essenciais para obrigações legais ou contratuais.
    *   **Exemplo:** Ao receber uma solicitação de exclusão para 'carlos.pereira@email.com', o DPO inicia um processo para remover todos os dados de marketing e, se não houver obrigações legais de retenção, também os dados transacionais associados a esse email, confirmando a exclusão ao titular.

---

## Templates

### Email de Confirmação Double Opt-in

```
Assunto: Confirme sua inscrição na newsletter de [Nome da Empresa]

Olá [Nome do Cliente],

Agradecemos o seu interesse! Para completar sua inscrição na newsletter de [Nome da Empresa] e começar a receber nossas últimas novidades, promoções exclusivas e conteúdos relevantes, por favor, clique no link abaixo para confirmar seu email:

>>> [Link de Confirmação Único e Válido por 24h] <<<

Ao clicar, você confirma que leu e concorda com nossa Política de Privacidade.

Se você não se inscreveu em nossa newsletter, por favor, ignore este email.

Atenciosamente,

Equipe [Nome da Empresa]
[Link para a Política de Privacidade da Empresa]
[Endereço do Site da Empresa]
```

### Rodapé de Email Marketing com Compliance

```
Este email foi enviado por:
[Nome Legal da Empresa]
[Endereço Completo da Empresa: Rua Exemplo, 123, Bairro Fictício, Cidade - UF, CEP 00000-000]
[CNPJ da Empresa: XX.XXX.XXX/XXXX-XX]

Você recebeu este email porque se inscreveu na newsletter de [Nome da Empresa] em [Data de Inscrição ou Mês/Ano].

Não deseja mais receber nossos emails?
[Link de Descadastro] | Gerenciar suas preferências de email aqui. [Link para Preferências de Email]

Leia nossa Política de Privacidade completa para entender como tratamos seus dados:
[Link para a Política de Privacidade da Empresa]

© [Ano Atual] [Nome da Empresa]. Todos os direitos reservados.
```

---

## Checklist

-   [x] Todos os formulários de captação de email possuem checkbox de consentimento não pré-marcada para marketing?
-   [x] Os termos de consentimento nos formulários são claros, específicos e vinculam à Política de Privacidade da empresa?
-   [x] O processo de double opt-in está ativo e funcionando para todas as novas inscrições de marketing por email?
-   [x] Há um registro auditável de data, hora, endereço IP e texto exato do consentimento para cada contato na base de dados?
-   [x] Todos os emails de marketing e promocionais contêm um link de descadastro claro, visível e funcional no rodapé?
-   [x] O processo de descadastro é imediato, não exige login e não envolve múltiplas etapas para o usuário?
-   [x] Existe uma política de retenção de dados documentada para emails, especificando o tempo de armazenamento pós-descadastro e exclusão?
-   [x] Os registros SPF, DKIM e DMARC estão corretamente configurados, publicados e monitorados para todos os domínios de envio de email da empresa?
-   [x] A empresa possui um DPO (Encarregado de Dados) ou um ponto de contato claro para solicitações de titulares de dados via email?
-   [x] São realizadas auditorias periódicas na base de emails para remover contatos sem base legal clara ou que solicitaram descadastro/exclusão?

---

## Métricas de Referência

| Métrica                         | Benchmark | Meta     |
|:--------------------------------|:----------|:---------|
| Taxa de Conclusão Double Opt-in | 60-75%    | > 70%    |
| Taxa de Descadastro (Unsubscribe)| < 0.2%    | < 0.15%  |
| Taxa de Reclamação SPAM         | < 0.08%   | < 0.05%  |
| Conformidade SPF/DKIM/DMARC     | 100%      | 100%     |
| Tempo para Processar Descadastro| < 24h     | Imediato (<1h) |
| Taxa de Abertura (Marketing)    | 15-25%    | > 20%    |

---

## Erros Comuns

1.  **Coleta de consentimento implícito ou pré-marcado**: Preencher automaticamente a checkbox de "aceito receber comunicações" ou inferir consentimento de ações não relacionadas.
    *   **Como evitar**: Sempre deixe a checkbox de consentimento desmarcada, exigindo uma ação explícita e afirmativa do usuário.
    *   **Exemplo**: Um formulário de contato onde a opção de "receber newsletter" já vem ticada por padrão, sem que o usuário a marque.
2.  **Ausência ou dificuldade no processo de descadastro**: Esconder o link de descadastro no email, exigir login ou múltiplas etapas para cancelar a inscrição.
    *   **Como evitar**: Garanta que o link "Cancelar inscrição" esteja em tamanho legível e contraste adequado no rodapé de cada email, e que o processo de descadastro seja de um clique, sem barreiras.
    *   **Exemplo**: Um email marketing com o link de descadastro minúsculo, cinza claro em fundo branco, ou que redireciona para uma página de login antes de permitir o cancelamento.
3.  **Não registrar ou não conseguir comprovar o consentimento**: Falha em armazenar a prova do consentimento (data, hora, IP, texto exato) ou em recuperá-la para auditoria.
    *   **Como evitar**: Implemente um sistema que capture e armazene automaticamente todos os detalhes do consentimento no momento da inscrição, garantindo que esses registros sejam facilmente acessíveis para demonstração de conformidade.
    *   **Exemplo**: Uma empresa que usa apenas uma lista de emails sem registrar como e quando cada contato deu consentimento, impossibilitando a comprovação em caso de fiscalização.

---

## Dicas Avançadas

1.  **Segmentação Aprofundada por Preferência de Conteúdo e Frequência**: Além do opt-in geral para marketing, ofereça aos usuários a possibilidade de escolher tipos específicos de conteúdo (ex: promoções, notícias do setor, eventos, atualizações de produto) e a frequência desejada (semanal, mensal). Isso não apenas aumenta a satisfação do usuário, mas também reduz as taxas de descadastro e aumenta o engajamento.
    *   **Exemplo**: Uma página de "Gerenciar Preferências" onde o usuário pode marcar "Receber apenas notícias sobre produtos X", "Receber ofertas especiais" e selecionar "Frequência mensal" para cada categoria.
2.  **Auditoria Contratual e de Segurança de Fornecedores de Email Marketing (ESP)**: Vistoriar não apenas as funcionalidades, mas também os contratos (DPA - Data Processing Addendum) e as certificações de segurança (ex: ISO 27001, SOC 2) dos seus provedores de serviços de email marketing (ESP). Assegure que eles também estejam em conformidade com LGPD/GDPR e que a responsabilidade pela proteção de dados esteja claramente definida.
    *   **Exemplo**: Revisar o DPA do Mailchimp, SendGrid ou ActiveCampaign, verificando cláusulas sobre subcontratados, localização de dados e medidas de segurança implementadas.
3.  **Implementação de "Privacy by Design" em Novos Fluxos de Email**: Ao desenvolver qualquer novo fluxo de comunicação por email (seja uma nova campanha, automação ou funcionalidade), integre as considerações de privacidade e conformidade desde o estágio de concepção, não como um afterthought. Pense na necessidade, base legal e minimização de dados desde o rascunho.
    *   **Exemplo**: Antes de lançar uma nova série de emails de onboarding, realizar uma Avaliação de Impacto à Proteção de Dados (AIPD) para garantir que a coleta e uso dos dados durante o fluxo estão em conformidade e são estritamente necessários.
4.  **Monitoramento Proativo de Reclamações e Listas Negras com Feedback Loops (FBLs)**: Utilize ferramentas de monitoramento de reputação de IP/domínio e configure alertas para Feedback Loops (FBLs) de provedores de email como Gmail, Outlook, Yahoo. Isso permite identificar rapidamente usuários que marcam seus emails como SPAM e removê-los proativamente, mitigando danos à sua reputação de envio antes que afetem gravemente a entregabilidade.
    *   **Exemplo**: Utilizar o Google Postmaster Tools para monitorar a reputação do domínio de envio e a taxa de reclamações, ou integrar-se a serviços como Return Path para acesso a FBLs e remoção automática de reclamantes.
5.  **Políticas de Retenção Dinâmicas Baseadas em Engajamento**: Automaticamente desengajar ou remover contatos da lista de marketing que permanecem inativos por um longo período (ex: 12-24 meses sem abertura ou clique) e não demonstram mais interesse, mesmo que tenham dado consentimento inicial. Isso melhora a qualidade da lista, a entregabilidade e reduz o risco de dados obsoletos.
    *   **Exemplo**: Configurar uma automação que, após 9 meses de inatividade, envia um email de "Última Chance" para reengajar. Se o contato não interagir, ele é automaticamente removido da lista de marketing ativa após 12 meses.