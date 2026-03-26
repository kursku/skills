---
name: lead-magnet-delivery
description: "Lead Magnet Delivery — Skill especializada para lead magnet delivery"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Lead Magnet Delivery

Esta skill capacita o Claude a projetar e executar automações de email eficazes para a entrega e nutrição de leads após o download de um lead magnet.

---

## Keywords

Automação de email, entrega de lead magnet, sequência de boas-vindas, nurturing de leads, segmentação de email, email marketing, jornada do cliente, taxa de abertura, taxa de cliques, CTA, página de obrigado, automação de marketing, funil de vendas, nutrição de conteúdo.

---

## Quick Start

1.  **Configure o gatilho de inscrição**: Na ferramenta de automação (ex: ActiveCampaign, Mailchimp, RD Station), crie um formulário de captura ou integre o formulário existente do site (ex: via Landing Page Builder) para adicionar novos contatos a uma lista específica ou aplicar uma tag como "Baixou_Ebook_X".
2.  **Crie o email de entrega imediata**: Redija um email com o link de download do lead magnet e instruções claras. Garanta que o link esteja ativo e seja facilmente acessível. Use um remetente reconhecível como "Marketing [Nome da Empresa]" ou "Nome do Autor/Especialista".
3.  **Desenhe a sequência de nutrição**: Planeje 3-5 emails adicionais para os dias seguintes, focando em agregar valor e guiar o lead pelo funil, com intervalos de 2-3 dias entre eles, complementando o conteúdo do lead magnet.
4.  **Ative a automação**: Revise todo o fluxo (gatilho, emails, atrasos, condições de saída) e ative a automação na plataforma escolhida para que novos inscritos recebam o conteúdo automaticamente.
5.  **Monitore as métricas iniciais**: Acompanhe as taxas de abertura e clique do email de entrega e dos primeiros emails de nutrição para identificar pontos de otimização na linha de assunto ou no corpo do email, ajustando conforme necessário.

---

## Core Workflows

### Workflow 1: Automação de Entrega Imediata de Ebook "Guia Completo de Email Marketing"

Este workflow detalha a configuração e o conteúdo para a entrega de um ebook, garantindo que o lead receba o material de forma instantânea e inicie um relacionamento de valor com a marca.

**Passos Detalhados:**

1.  **Gatilho da Automação**: Um novo contato preenche um formulário na landing page "Guia Completo de Email Marketing" (`https://www.marketingpro.com.br/guia-email-marketing`) e é adicionado à lista "Interessados em Email Marketing" ou recebe a tag "Baixou_Ebook_EmailMarketing".
2.  **Ação 1: Enviar Email de Boas-Vindas e Entrega**:
    *   **Assunto do Email**: "Seu Guia Completo de Email Marketing Chegou! [Nome do Lead]" (Personalização com o nome aumenta a taxa de abertura em 26%)
    *   **Remetente**: "João da MarketingPro <joao@marketingpro.com.br>"
    *   **Corpo do Email**:
        *   Saudação personalizada: "Olá, [Nome do Lead],"
        *   Confirmação e agradecimento: "Muito obrigado por baixar nosso 'Guia Completo de Email Marketing'! Estamos felizes em ter você conosco nesta jornada."
        *   Instruções de acesso: "Seu material está pronto para ser acessado. Clique no botão abaixo para fazer o download imediato:"
        *   Botão CTA: "BAIXAR SEU GUIA AGORA" (link para `https://www.marketingpro.com.br/download/guia-email-marketing.pdf`)
        *   Breve contextualização: "Este guia foi cuidadosamente elaborado para ajudar você a dominar as estratégias mais eficazes de email marketing, desde a criação de listas segmentadas até a otimização de campanhas para conversão."
        *   Chamada para engajamento futuro: "Fique atento aos nossos próximos emails, pois traremos dicas exclusivas, estudos de caso e ferramentas que complementarão seu aprendizado e acelerarão seus resultados."
        *   Assinatura: "Atenciosamente, Equipe MarketingPro"
3.  **Ação 2: Adicionar Tag de Engajamento**: Aplique a tag "Recebeu_Ebook_EmailMarketing" ao perfil do lead para rastrear a progressão e permitir futuras segmentações.
4.  **Ação 3: Espera Programada**: Configure uma espera de 2 dias. Este tempo permite que o lead consuma o conteúdo do ebook sem sentir-se sobrecarregado por uma enxurrada de emails.
5.  **Ação 4: Iniciar Sequência de Nurturing**: Direcione o lead para o "Workflow 2: Sequência de Nurturing Pós-Download", que continuará a jornada do lead com conteúdo de valor.

### Workflow 2: Sequência de Nurturing Pós-Download "Dominando Email Marketing"

Este workflow foca em nutrir leads que já baixaram o material, oferecendo conteúdo complementar, aprofundando o relacionamento e guiando-os para a próxima etapa do funil (ex: demonstração de produto, consultoria).

**Passos Detalhados:**

1.  **Gatilho da Automação**: Lead entra neste workflow após completar o "Workflow 1: Automação de Entrega Imediata de Ebook" (especificamente, após a espera de 2 dias).
2.  **Email 1 (Dia 3 pós-download): Dica Prática de Segmentação Avançada**:
    *   **Assunto do Email**: "3 Dicas Essenciais de Segmentação que o Guia Não Cobriu [Nome do Lead]"
    *   **Corpo do Email**:
        *   Relembrar o guia: "Esperamos que você esteja aproveitando ao máximo o 'Guia Completo de Email Marketing'!"
        *   Conteúdo de valor: "Para complementar o que você aprendeu e levar seus resultados a um novo patamar, separamos 3 táticas avançadas de segmentação que podem, comprovadamente, dobrar suas taxas de cliques e conversão."
        *   Exemplo concreto: "Por exemplo, a segmentação por comportamento de compra (quem clicou em um produto específico mas não comprou) supera em 7x a segmentação demográfica em termos de conversão. Você pode implementar isso criando automações que rastreiam cliques em links específicos de produtos no seu site."
        *   CTA para blog/webinar: "Quer aprofundar ainda mais? Leia nosso artigo sobre 'Segmentação Inteligente para E-commerce' [link para blog post: `https://www.marketingpro.com.br/blog/segmentacao-ecommerce`] ou assista ao nosso webinar gravado 'O Poder da Segmentação Dinâmica' [link para webinar: `https://www.marketingpro.com.br/webinar-segmentacao`]."
3.  **Ação 1: Espera Programada**: Aguarde 3 dias.
4.  **Email 2 (Dia 6 pós-download): Estudo de Caso de Sucesso Inspirador**:
    *   **Assunto do Email**: "Caso de Sucesso: Como a Empresa X Aumentou as Vendas em 40% com Email Marketing"
    *   **Corpo do Email**:
        *   Conexão com o interesse: "Você sabia que muitas empresas, como a sua, estão transformando seus resultados de vendas aplicando as estratégias que ensinamos no guia?"
        *   Apresentar caso de sucesso: "Apresentamos o caso da Empresa X (e-commerce de moda), que, aplicando os princípios de automação e personalização que você está aprendendo, viu suas vendas diretas via email marketing saltarem 40% em apenas 6 meses. Detalhamos o processo, as ferramentas e os resultados neste estudo de caso:"
        *   Link para estudo de caso: "Leia o Estudo de Caso Completo [link para estudo de caso no site: `https://www.marketingpro.com.br/casos-de-sucesso/empresa-x`]."
        *   CTA para demonstração/consultoria: "Pense em como um impacto similar pode transformar seu negócio. Gostaria de uma análise gratuita da sua estratégia atual de email marketing e um plano personalizado? [link para agendamento de demo/consultoria: `https://www.marketingpro.com.br/agendar-consultoria`]."
5.  **Ação 2: Espera Programada**: Aguarde 4 dias.
6.  **Email 3 (Dia 10 pós-download): Oferta Direcionada e Call to Action Forte**:
    *   **Assunto do Email**: "Leve seu Email Marketing ao Próximo Nível com a Plataforma MarketingPro!"
    *   **Corpo do Email**:
        *   Relembrar valor: "Você já dominou os fundamentos com o nosso guia e viu os resultados impressionantes que outros negócios estão alcançando. Que tal ir além e automatizar todo esse poder?"
        *   Apresentar solução: "Nossa plataforma MarketingPro foi projetada para otimizar suas campanhas de email marketing, com segmentação avançada, testes A/B inteligentes, automações poderosas e relatórios completos, tudo em um só lugar."
        *   Benefício claro: "Comece a construir sequências de email que convertem leads em clientes fiéis, economizando tempo, recursos e aumentando significativamente seu ROI. Não perca mais vendas por falta de automação!"
        *   CTA Forte e com urgência (se couber): "Experimente a Plataforma MarketingPro Gratuitamente por 14 Dias! Sem compromisso e sem cartão de crédito. [link para trial gratuito: `https://www.marketingpro.com.br/trial-gratuito`]."
7.  **Ação 3: Segmentação Final e Transição**: Marque o lead com a tag "Nutrido_EmailMarketing_Oferta" e, se não clicou na oferta, adicione-o a uma lista para outra automação de reengajamento mais branda (ex: newsletter mensal, convite para evento) ou para um pipeline de vendas de baixo prioridade. Se clicou, notifique a equipe de vendas.

---

## Templates

### Email de Entrega de Lead Magnet (Ebook: "Dominando o SEO Local")

```
Assunto: Seu Ebook "Dominando o SEO Local" Chegou! [Nome do Lead]

Olá, [Nome do Lead],

Muito obrigado por baixar nosso ebook "Dominando o SEO Local: O Guia Essencial para Negócios Locais"! Estamos muito felizes em compartilhar esse conhecimento valioso com você.

Para acessar seu material exclusivo e começar a transformar sua presença online, basta clicar no botão abaixo:

[ BOTÃO: BAIXAR MEU EBOOK AGORA ]
(Link para: https://www.marketinglocalexperts.com.br/downloads/ebook-seo-local.pdf)

Este guia foi cuidadosamente elaborado para ajudar você a posicionar seu negócio no topo dos resultados de busca locais do Google, atraindo mais clientes para sua porta (física ou virtual). Você encontrará estratégias práticas, exemplos reais e um checklist de implementação para começar hoje mesmo.

Aproveite a leitura! E fique de olho em nossos próximos emails, pois traremos dicas valiosas para complementar seu aprendizado sobre SEO e marketing digital, especialmente focadas em resultados locais.

Se tiver qualquer dúvida ou precisar de ajuda, é só responder a este email. Estamos aqui para ajudar!

Um abraço,

Equipe Marketing Local Experts
www.marketinglocalexperts.com.br
```

### Email de Nurturing - Dica Relacionada (Pós-download do Ebook de SEO Local)

```
Assunto: [Dica Bônus] 3 Ferramentas