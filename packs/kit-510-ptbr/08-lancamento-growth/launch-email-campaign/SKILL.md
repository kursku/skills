---
name: launch-email-campaign
description: "Launch Email Campaign — Skill especializada para launch email campaign"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Launch Email Campaign

Esta skill capacita o Claude Code a orquestrar campanhas de e-mail de lançamento de produtos ou funcionalidades, focando em aquisição, ativação e retenção de usuários através de sequências estratégicas e automação.

---

## Keywords

Segmentação de Lista, Automação de E-mail, A/B Testing, Lead Scoring, Onboarding Flow, Drip Campaign, Deliverability, Open Rate, Click-Through Rate (CTR), Conversion Rate, Customer Lifetime Value (LTV), Email Service Provider (ESP), Pré-lançamento, Pós-lançamento.

---

## Quick Start

1.  **Configurar Plataforma ESP**: Conectar o domínio principal do produto ao ActiveCampaign ou SendGrid, garantindo a autenticação (SPF, DKIM, DMARC) para otimizar a entregabilidade.
2.  **Importar Lista de Contatos Qualificados**: Carregar a lista de e-mails de leads que se pré-registraram ou demonstraram interesse explícito no produto via landing page específica.
3.  **Criar Sequência de Boas-Vindas Pós-Cadastro**: Desenvolver uma sequência automatizada de 3 e-mails para novos cadastros (e-mail de confirmação, e-mail de "primeiros passos", e-mail de "valor principal").
4.  **Agendar Envio Estratégico**: Configurar o envio dos e-mails de lançamento para coincidir com o fuso horário predominante da base de usuários ou no horário de pico de engajamento identificado em testes anteriores (ex: terças e quintas, 10h AM local).

---

## Core Workflows

### Workflow 1: Sequência de Lançamento e Onboarding de Produto SaaS

Este workflow detalha a orquestração de e-mails desde o anúncio oficial do lançamento até os primeiros passos do usuário para garantir a ativação inicial.

**Passos Detalhados:**

1.  **Segmentação Inicial para Lançamento**:
    *   **Ação**: Criar um segmento no ESP chamado "Leads de Pré-Lançamento" incluindo contatos que se registraram na landing page do produto antes do lançamento oficial. Outro segmento, "Novos Cadastros Lançamento", para quem se cadastrar no dia do lançamento.
    *   **Exemplo**: O segmento "Leads de Pré-Lançamento" contém 1.500 contatos que preencheram o formulário "Inscreva-se para Acesso Antecipado ao [Nome do Produto]" nos últimos 60 dias.

2.  **E-mail de Anúncio Oficial (Dia 0)**:
    *   **Ação**: Enviar o primeiro e-mail da sequência no dia exato do lançamento, anunciando que o produto está disponível. O CTA deve ser direto para o cadastro ou login.
    *   **Conteúdo Sugerido**: Título impactante, valor-chave do produto, convite para experimentar.
    *   **Exemplo**:
        *   **Assunto**: 🎉 É Hoje! Seu Acesso ao [Nome do Produto SaaS] Chegou!
        *   **Corpo**: Breve introdução ao problema que o produto resolve e como ele oferece a solução. Destacar 1-2 benefícios principais.
        *   **CTA**: "Experimente Agora Grátis!" ou "Comece a Transformar seu [Área de Atuação]!"
    *   **Métrica Esperada**: Open Rate de 30-35%, CTR de 8-10% para o CTA de cadastro/login.

3.  **E-mail de Valor/Benefício Focado (Dia 2)**:
    *   **Ação**: Para usuários que se cadastraram mas não realizaram a "primeira ação de ativação" (ex: criar projeto, convidar membro da equipe), enviar um e-mail focando em um benefício específico ou caso de uso.
    *   **Conteúdo Sugerido**: Explicar uma funcionalidade chave e seu impacto.
    *   **Exemplo**:
        *   **Assunto**: Desbloqueie [Benefício #1] com a Feature X do [Nome do Produto]!
        *   **Corpo**: "Percebemos que você se cadastrou, mas talvez não tenha explorado a fundo a [Feature X]. Com ela, você pode [descrever o benefício tangível]. Veja como é fácil começar: [link para tutorial]."
        *   **CTA**: "Assista ao Tutorial Rápido" ou "Comece seu Primeiro Projeto Aqui!"
    *   **Métrica Esperada**: Aumento de 10-15% na taxa de ativação (usuários que completam a primeira ação crítica) para o segmento que recebeu este e-mail.

4.  **E-mail de Prova Social e Escassez (Dia 4)**:
    *   **Ação**: Para usuários que ainda não ativaram, enviar um e-mail com depoimentos de early adopters ou beta testers, e mencionar um bônus por tempo limitado para os primeiros usuários.
    *   **Conteúdo Sugerido**: Citação de cliente real, número de usuários satisfeitos, oferta exclusiva.
    *   **Exemplo**:
        *   **Assunto**: Não Perca! Veja o que nossos Beta Testers dizem sobre [Nome do Produto] + Bônus!
        *   **Corpo**: "Mais de 500 empresas já estão otimizando seus [área] com [Nome do Produto]! '[Citação impactante de um beta tester sobre um resultado real]'. Como agradecimento por ser um dos primeiros, use o código [BÔNUS10] para 10% de desconto nos primeiros 3 meses, válido só até [Data Limite]."
        *   **CTA**: "Resgate seu Desconto e Comece Agora!"
    *   **Métrica Esperada**: Elevação da taxa de conversão (assinatura paga) em 5-7% para o grupo impactado pela oferta.

### Workflow 2: Reengajamento Pós-Lançamento de Usuários Inativos

Este workflow foca em trazer de volta usuários que se cadastraram ou usaram o produto inicialmente, mas ficaram inativos após um período.

**Passos Detalhados:**

1.  **Identificação de Usuários Inativos**:
    *   **Ação**: Configurar uma automação no ESP para identificar usuários que não fizeram login ou não realizaram nenhuma ação chave (ex: criar relatório, publicar conteúdo) nos últimos 30 dias após sua primeira ativação.
    *   **Exemplo**: Um segmento "Inativos 30 Dias" é criado, com 800 usuários que se cadastraram há mais de 30 dias e não registraram nenhuma atividade essencial no produto.

2.  **E-mail de Reconexão e Valor (Dia 0 da Inatividade)**:
    *   **Ação**: Enviar um e-mail amigável, expressando que "sentimos falta" do usuário e lembrando o valor principal do produto, sem pressão.
    *   **Conteúdo Sugerido**: Tom empático, lembrança do problema resolvido pelo produto.
    *   **Exemplo**:
        *   **Assunto**: Sentimos sua falta no [Nome do Produto]! 😔
        *   **Corpo**: "Olá [Nome], percebemos que você não tem usado o [Nome do Produto] ultimamente. Queríamos apenas lembrar como ele pode te ajudar a [benefício principal]. O que achou da sua experiência inicial?"
        *   **CTA**: "Voltar ao [Nome do Produto]" ou "Compartilhe seu Feedback"

3.  **E-mail de Novidade/Recurso Recente (Dia 3 da Inatividade)**:
    *   **Ação**: Para aqueles que não reagiram ao primeiro e-mail, destacar uma nova funcionalidade ou uma atualização recente que poderia resolver uma dor específica.
    *   **Conteúdo Sugerido**: Apresentar um novo recurso relevante.
    *   **Exemplo**:
        *   **Assunto**: Novidade: [Nome da Feature Recente] chegou no [Nome do Produto]!
        *   **Corpo**: "Desde sua última visita, lançamos a [Nome da Feature Recente] que permite [benefício da feature]. Muitos usuários estão adorando! Que tal dar uma olhada?"
        *   **CTA**: "Explorar a Nova Feature" ou "Ver Todas as Atualizações"

4.  **E-mail de Suporte Personalizado/Oferta (Dia 7 da Inatividade)**:
    *   **Ação**: Para quem ainda não reengajou, oferecer ajuda personalizada (demo, suporte) ou um incentivo final de reativação.
    *   **Conteúdo Sugerido**: Opção de agendar chamada, acesso a base de conhecimento, ou desconto para reativar.
    *   **Exemplo**:
        *   **Assunto**: Precisa de Ajuda para Aproveitar o [Nome do Produto]?
        *   **Corpo**: "Sabemos que o começo pode ser desafiador. Nossa equipe de sucesso do cliente está pronta para te ajudar. Que tal agendarmos uma rápida demonstração gratuita para tirar suas dúvidas? Ou, se preferir, use [CÓDIGO_REATIVAR] para 20% de desconto no próximo mês e experimente sem compromisso."
        *   **CTA**: "Agendar Demo Gratuita" ou "Reativar Minha Conta com Desconto"
    *   **Métrica Esperada**: Taxa de reativação (usuários que voltam a usar o produto) de 5-10% para o segmento de inativos.

---

## Templates

### E-mail de Anúncio de Lançamento Oficial (Dia 0)

```
Assunto: 🎉 É Hoje! Seu Acesso Exclusivo ao ScaleUp CRM Chegou!

Olá [Nome do Lead],

A espera acabou! Temos o prazer de anunciar que o ScaleUp CRM está oficialmente disponível para transformar a gestão de clientes da sua empresa.

Desenvolvido para equipes de vendas e marketing que buscam otimização e resultados reais, o ScaleUp CRM centraliza todos os seus dados de clientes, automatiza tarefas repetitivas e oferece insights poderosos para fechar mais negócios.

Com o ScaleUp CRM, você poderá:
- Gerenciar pipelines de vendas de forma visual e intuitiva.
- Automatizar e-mails de follow-up e tarefas.
- Analisar performance de vendas com relatórios detalhados.

Centenas de empresas já estão testando e vendo resultados!
"O ScaleUp CRM mudou a forma como nossa equipe de vendas trabalha. Mais organização e 30% de aumento nas conversões!" - Ana Lúcia, Gerente Comercial na InovaTech.

Não perca tempo! Comece a otimizar suas vendas hoje mesmo.

👉 Experimente o ScaleUp CRM Grátis por 14 Dias!
[Link para Página de Cadastro/Login]

Qualquer dúvida, nossa equipe de suporte está pronta para ajudar.

Atenciosamente,
Time ScaleUp CRM
[Link para o Site]
[Link para o Blog]
[Link para o LinkedIn]
```

### E-mail de Ativação Pós-Cadastro (Primeiros Passos)

```
Assunto: Bem-vindo(a) ao GrowFlow! Seus Primeiros Passos para o Sucesso 🚀

Olá [Nome do Usuário],

Bem-vindo(a) ao GrowFlow! Estamos muito animados em tê-lo(a) conosco.

Para começar a transformar sua estratégia de marketing digital, sugerimos que você dê seus primeiros passos agora mesmo:

1.  **Conecte suas Redes Sociais**: Integrações rápidas com Facebook, Instagram e LinkedIn para agendar suas publicações em segundos.
    👉 [Link para Conectar Redes Sociais]

2.  **Crie seu Primeiro Cronograma de Conteúdo**: Organize suas ideias e planeje suas postagens com nossa ferramenta intuitiva.
    👉 [Link para Criar Cronograma]

3.  **Explore a Biblioteca de Templates**: Acesse centenas de templates prontos para turbinar suas campanhas.
    👉 [Link para Biblioteca de Templates]

Se precisar de ajuda, temos um tutorial rápido de 5 minutos que cobre o essencial:
📺 [Link para o Vídeo Tutorial]

Ou, se preferir, nossa equipe está sempre disponível no chat de suporte!

Vamos juntos(as) escalar seus resultados!

Com carinho,
Equipe GrowFlow
[Link para Central de Ajuda]
[Link para o Blog GrowFlow]
```

---

## Checklist

- [x] Plataforma de e-mail marketing (ESP) configurada e integrada com o produto (ex: ActiveCampaign, SendGrid).
- [x] Domínio de envio autenticado (SPF, DKIM, DMARC) para máxima entregabilidade.
- [x] Lista de contatos segmentada por comportamento e interesse (pré-registros, cadastrados, inativos).
- [x] Linhas de assunto otimizadas e testadas (A/B testing pronto para variações).
- [x] Conteúdo dos e-mails personalizado com tags dinâmicas (ex: `[Nome do Usuário]`, `[Nome da Empresa]`).
- [x] Call-to-action (CTA) claro, único e visível em cada e-mail.
- [x] Design dos e-mails responsivo e testado em diferentes dispositivos (mobile-first).
- [x] Links de rastreamento (UTM parameters) configurados em todos os CTAs para análise de tráfego e conversão.
- [x] Conformidade com regulamentações de privacidade de dados (GDPR, LGPD) garantida (opt-in explícito, opção de opt-out fácil).
- [x] Teste de deliverability e spam score realizado em ferramentas como Mail-tester.com ou GlockApps.
- [x] Automações de e-mail configuradas para os diferentes estágios do funil (lançamento, onboarding, reengajamento).
- [x] Cronograma de envio definido e revisado para evitar sobrecarga ou lacunas de comunicação.

---

## Métricas de Referência

| Métrica               | Benchmark (Indústria SaaS) | Meta (Lançamento) |
|-----------------------|----------------------------|-------------------|
| Open Rate             | 20-25%                     | 30-35%            |
| Click-Through Rate (CTR) | 2-3%                       | 5-8%              |
| Conversion Rate (Email -> Cadastro/Assinatura) | 1-2%                       | 3-5%              |
| Activation Rate (Pós-e-mail de onboarding) | 15-20%                     | 25-30%            |
| Unsubscribe Rate      | <0.5%                      | <0.3%             |
| Deliverability Rate   | >95%                       | >98%              |

---

## Erros Comuns

1.  **Não Segmentar a Lista de E-mails**: Enviar a mesma mensagem genérica para todos os contatos, independentemente de seu estágio no funil ou interesse.
    *   **Como evitar**: Crie segmentos detalhados com base em dados de pré-lançamento (ex: visitantes da landing page A vs. landing page B), comportamento no site, ou interações anteriores. Por exemplo, leads que se inscreveram para um webinar sobre "novas funcionalidades" devem receber e-mails focados nessas funcionalidades, não em um overview genérico do produto.

2.  **Focar Apenas em Vendas Imediatas**: Bombardear os leads com ofertas de compra ou assinaturas desde o primeiro e-mail, sem antes entregar valor ou construir relacionamento.
    *   **Como evitar**: Adote uma abordagem de "valor primeiro". Nos e-mails de pré-lançamento e nos primeiros e-mails pós-lançamento, concentre-se em educar, resolver problemas e mostrar como o produto pode beneficiar o usuário. Um bom equilíbrio é 80% valor (dicas, tutoriais, casos de uso) e 20% promoção (CTA para experimentar ou comprar).

3.  **Negligenciar o Pós-Lançamento e Onboarding**: Parar a comunicação após o anúncio de lançamento ou o cadastro inicial, assumindo que o usuário se virará sozinho.
    *   **Como evitar**: Implemente sequências de e-mail de onboarding robustas que guiam o usuário passo a passo através das principais funcionalidades e benefícios. Monitore as métricas de ativação e crie fluxos de reengajamento para usuários que não progrediram ou ficaram inativos, oferecendo ajuda personalizada ou conteúdo relevante, como no Workflow 2.

---

## Dicas Avançadas

1.  **Warm-up de IP e Domínio Progressivo**: Para novos domínios ou provedores de serviço de e-mail (ESPs), evite enviar volumes muito grandes de uma vez. Comece com volumes pequenos e aumente gradualmente para construir uma reputação de remetente positiva com os provedores de e-mail (ISPs), garantindo melhor entregabilidade. Ex: 500 e-mails no dia 1, 1000 no dia 2, 2000 no dia 3, etc.
2.  **Personalização Hiper-Segmentada por Evento/Comportamento**: Vá além do `[Nome]` e use dados comportamentais. Configure automações para disparar e-mails com base em eventos específicos no produto. Ex: Se um usuário visualizou a página de "Recursos Pro" mas não assinou, envie um e-mail com um case de sucesso de um cliente que utiliza esses recursos, ou um desconto para upgrade.
3.  **Testes Multivariados de Elementos Chave**: Em vez de apenas A/B tests simples (ex: duas linhas de assunto), experimente testar múltiplas variáveis simultaneamente (linha de assunto, corpo do e-mail, imagem, CTA) para identificar a combinação mais eficaz. Ferramentas como o "Content Testing" do ActiveCampaign permitem isso.
4.  **Integração com CRM e Automação de Vendas**: Conecte seu ESP com seu CRM (ex: HubSpot, Salesforce). Quando um lead atinge um certo nível de engajamento com os e-mails (ex: abriu 3 e-mails, clicou em 2 CTAs), marque-o automaticamente como "Lead Quente" no CRM e crie uma tarefa para a equipe de vendas entrar em contato.
5.  **Ciclo de Feedback Automatizado Pós-Ativação**: Após o usuário completar a ação principal de ativação (ex: primeiro projeto criado, primeira venda realizada), envie um e-mail automatizado solicitando feedback (ex: pesquisa NPS, pergunta aberta "O que você achou?"). Isso não só melhora o produto, mas também demonstra que a empresa valoriza a opinião do cliente, fortalecendo a retenção.