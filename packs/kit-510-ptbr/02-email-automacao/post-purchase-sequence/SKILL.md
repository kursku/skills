---
name: post-purchase-sequence
description: "Post Purchase Sequence — Skill especializada para post purchase sequence"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Post Purchase Sequence

Esta skill capacita o Claude a arquitetar e implementar sequências de email pós-compra que maximizam a satisfação do cliente, promovem a recompra e fortalecem o relacionamento com a marca.

---

## Keywords

Pós-venda, automação de email, retenção de clientes, upsell, cross-sell, feedback, fidelização, nutrição pós-compra, prova social, customer success, onboarding de produto, ciclo de vida do cliente.

---

## Quick Start

1.  **Configurar Gatilho de Compra Concluída**: Estabeleça o evento "Compra Concluída" (ex: "Pedido pago" no Shopify, "Status do pedido = Entregue" no Bling) como o disparador inicial da automação na ferramenta de email marketing (ex: ActiveCampaign, RD Station).
2.  **Primeiro Email Instantâneo**: Programe o envio imediato de um email de confirmação de pedido, contendo detalhes da compra, endereço de entrega e link de rastreamento.
3.  **Email de Onboarding/Dicas (D+2)**: Agende um email para 2 dias após a compra com dicas de uso do produto, instruções de montagem ou um guia rápido de primeiros passos para produtos digitais.
4.  **Solicitação de Review (D+7)**: Envie um email solicitando a avaliação do produto 7 dias após a data de entrega (ou 7 dias após a compra para produtos digitais/serviços).
5.  **Oferta de Complementares (D+14)**: Programe um email com sugestões de produtos complementares (cross-sell) ou upgrades (upsell) baseados no item comprado.

---

## Core Workflows

### Workflow 1: Onboarding e Construção da Satisfação Imediata

Este workflow foca em tranquilizar o cliente, fornecer informações essenciais e iniciar a experiência positiva logo após a compra, especialmente para produtos físicos.

*   **Gatilho**: O cliente finaliza o pagamento do Pedido #987654.
*   **Passo 1 (0 horas)**: **Email de Confirmação Detalhada do Pedido.**
    *   **Assunto**: "Seu Pedido #987654 na [Nome da Loja] foi Confirmado! Detalhes e Rastreamento."
    *   **Conteúdo**: Boas-vindas, agradecimento pela compra, número do pedido, lista dos itens comprados, valor total, endereço de entrega, forma de pagamento, e um link claro para rastreamento (ex: `https://rastreamento.transportadora.com/987654`). Incluir uma estimativa de entrega e canais de contato para suporte.
    *   **Exemplo de Ação**: Automação dispara ao status "Pagamento Aprovado" na plataforma de e-commerce.
*   **Passo 2 (24 horas)**: **Email de Agradecimento e Expectativa.**
    *   **Assunto**: "Obrigado por escolher a [Nome da Loja]! Preparamos algo especial para você."
    *   **Conteúdo**: Reforça a decisão de compra, apresenta brevemente os valores da marca ou a missão, e comunica o próximo passo (ex: "Seu pedido está sendo preparado com carinho e logo estará a caminho!"). Pode incluir um link para a seção de FAQ ou um artigo de blog relacionado ao produto adquirido.
    *   **Exemplo de Ação**: Email enviado com um atraso de 24 horas após o primeiro.
*   **Passo 3 (48-72 horas ou na entrega)**: **Email de Dicas de Uso ou Notificação de Envio/Entrega.**
    *   **Assunto (Produto Físico)**: "Seu [Nome do Produto] da [Nome da Loja] está a caminho! Aproveite estas dicas." ou "Seu [Nome do Produto] foi entregue! Veja como tirar o máximo proveito."
    *   **Assunto (Produto Digital/Serviço)**: "Bem-vindo(a) ao [Nome do Serviço/Produto Digital]! Comece por aqui."
    *   **Conteúdo (Produto Físico)**: Se o produto ainda não foi entregue, oferece dicas de "como se preparar para receber" ou "primeiros passos após desembalar". Se entregue, foca em "como usar", "montagem" ou "cuidados básicos". Inclui novamente o link de rastreamento.
    *   **Conteúdo (Produto Digital/Serviço)**: Link direto para o painel de controle, tutoriais de vídeo, guia de primeiros passos, e informações de contato para suporte técnico.
    *   **Exemplo de Ação**: Este email pode ter um gatilho condicional: se o status do pedido for "Enviado", enviar dicas de uso pré-entrega; se "Entregue", enviar dicas pós-entrega.

### Workflow 2: Engajamento, Feedback e Estratégias de Recompra

Este workflow visa manter o cliente engajado, coletar feedback valioso e incentivar novas compras, transformando compradores em clientes fiéis.

*   **Gatilho**: 7 dias após a data de entrega (para produtos físicos) ou 7 dias após a compra (para produtos digitais/serviços).
*   **Passo 1 (D+7)**: **Solicitação de Avaliação do Produto e Prova Social.**
    *   **Assunto**: "Sua Opinião Vale Ouro! Avalie seu [Nome do Produto] e Ajude Outros Clientes da [Nome da Loja]!"
    *   **Conteúdo**: Convite direto para o cliente avaliar o produto que comprou. Incluir um link clicável que leva diretamente para a página de avaliação do produto no site. Pode oferecer um incentivo sutil (ex: "sua avaliação pode te render um cupom surpresa na próxima compra").
    *   **Exemplo de Ação**: Configurar um link de avaliação personalizado (ex: `https://nomedaloja.com/produto/SKU123/avaliar`).
    *   **Métrica Esperada**: Taxa de cliques no link de avaliação de 5-10%.
*   **Passo 2 (D+14)**: **Dicas Avançadas de Uso ou Sugestões de Produtos Complementares (Cross-sell/Upsell).**
    *   **Assunto**: "Tirando o Máximo do seu [Nome do Produto]? Conheça Acessórios Que Vão Mudar Tudo!"
    *   **Conteúdo**: Baseado no produto comprado, sugere itens complementares (ex: se comprou uma cafeteira, sugere cápsulas gourmet, um moedor ou canecas térmicas) ou um upgrade (ex: se comprou o plano básico, sugere o plano premium). Inclui links diretos para as páginas dos produtos sugeridos. Pode apresentar depoimentos de outros clientes que compraram os produtos complementares.
    *   **Exemplo de Ação**: Usar blocos dinâmicos na ferramenta de email marketing para exibir produtos "Quem comprou X também comprou Y".
*   **Passo 3 (D+30)**: **Oferta de Recompra ou Convite para Programa de Fidelidade.**
    *   **Assunto**: "Um Presente Especial para Você, Cliente [Nome da Loja]! 15% OFF na Próxima Compra."
    *   **Conteúdo**: Agradecimento pela fidelidade e um cupom de desconto exclusivo (ex: `RECOMPRA15`) para a próxima compra, com validade limitada. Alternativamente, um convite para o programa de fidelidade da marca, destacando os benefícios de ser um membro.
    *   **Exemplo de Ação**: Gerar um código de cupom único para cada cliente ou um cupom genérico com rastreamento de uso.
    *   **Métrica Esperada**: Taxa de conversão de recompra de 5-8%.

---

## Templates

### Email de Confirmação de Pedido

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Confirmação de Pedido - [Nome da Loja]</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
        .container { width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .header { text-align: center; padding-bottom: 20px; border-bottom: 1px solid #eeeeee; }
        .header img { max-width: 150px; }
        .content { padding: 20px 0; }
        .content h1 { font-size: 24px; color: #333333; }
        .content p { font-size: 16px; line-height: 1.5; color: #666666; }
        .order-details { background-color: #f9f9f9; border: 1px solid #eeeeee; padding: 15px; margin-top: 20px; }
        .order-details h2 { font-size: 20px; color: #333333; margin-top: 0; }
        .order-details ul { list-style: none; padding: 0; }
        .order-details ul li { margin-bottom: 10px; }
        .order-details .item { display: flex; justify-content: space-between; margin-bottom: 5px; }
        .order-details .item span { font-size: 15px; color: #555555; }
        .tracking-button { display: block; width: 200px; margin: 20px auto; padding: 12px 20px; background-color: #007bff; color: #ffffff; text-align: center; text-decoration: none; border-radius: 5px; font-size: 16px; }
        .footer { text-align: center; padding-top: 20px; border-top: 1px solid #eeeeee; font-size: 14px; color: #999999; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://www.suaempresa.com.br"><img src="https://www.suaempresa.com.br/logo.png" alt="Logo da [Nome da Loja]"></a>
        </div>
        <div class="content">
            <h1>Olá, {{customer.first_name}}!</h1>
            <p>Seu pedido na [Nome da Loja] foi confirmado com sucesso e estamos muito felizes em tê-lo(a) conosco!</p>
            <p>Seu número de pedido é: <strong>#{{order.id}}</strong></p>

            <div class="order-details">
                <h2>Detalhes do Pedido</h2>
                <ul>
                    <li><strong>Data do Pedido:</strong> {{order.date}}</li>
                    <li><strong>Total:</strong> R$ {{order.total}}</li>
                    <li><strong>Forma de Pagamento:</strong> {{payment.method}}</li>
                    <li><strong>Endereço de Entrega:</strong> {{shipping.address_line_1}}, {{shipping.address_line_2}}, {{shipping.city}} - {{shipping.state}}, {{shipping.zip_code}}</li>
                </ul>
                <h3>Itens do Pedido:</h3>
                <!-- Loop para cada item do pedido -->
                <div class="item">
                    <span>1x Caneca Térmica Inox - 500ml</span>
                    <span>R$ 79,90</span>
                </div>
                <div class="item">
                    <span>1x Porta-copos de Bambu (Kit 4)</span>
                    <span>R$ 39,90</span>
                </div>
                <!-- Fim do loop -->
            </div>

            <p>Você pode acompanhar o status do seu pedido a qualquer momento através do link abaixo:</p>
            <a href="{{tracking.url}}" class="tracking-button">Rastrear Meu Pedido</a>

            <p>A previsão de entrega é de 5 a 7 dias úteis. Em caso de dúvidas, nossa equipe de suporte está à disposição.</p>
            <p>Agradecemos a sua confiança e esperamos que você adore seus novos produtos!</p>
            <p>Atenciosamente,<br>A Equipe [Nome da Loja]</p>
        </div>
        <div class="footer">
            <p>[Nome da Loja] | [Endereço da Loja] | [Telefone] | [Email de Suporte]</p>
            <p><a href="https://www.suaempresa.com.br/privacidade">Política de Privacidade</a> | <a href="https://www.suaempresa.com.br/termos">Termos de Uso</a></p>
        </div>
    </div>
</body>
</html>
```

### Email de Solicitação de Avaliação do Produto

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Sua Opinião Importa! - [Nome da Loja]</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
        .container { width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .header { text-align: center; padding-bottom: 20px; border-bottom: 1px solid #eeeeee; }
        .header img { max-width: 150px; }
        .content { padding: 20px 0; text-align: center; }
        .content h1 { font-size: 26px; color: #333333; margin-bottom: 15px; }
        .content p { font-size: 16px; line-height: 1.6; color: #666666; margin-bottom: 20px; }
        .product-card { background-color: #f9f9f9; border: 1px solid #eeeeee; padding: 15px; margin: 20px auto; max-width: 400px; text-align: left; display: flex; align-items: center; }
        .product-card img { width: 80px; height: 80px; object-fit: cover; margin-right: 15px; border-radius: 4px; }
        .product-card .details h3 { margin: 0; font-size: 18px; color: #333333; }
        .product-card .details p { margin: 5px 0 0; font-size: 14px; color: #888888; }
        .review-button { display: inline-block; padding: 15px 25px; background-color: #28a745; color: #ffffff; text-align: center; text-decoration: none; border-radius: 5px; font-size: 18px; font-weight: bold; margin-top: 25px; }
        .footer { text-align: center; padding-top: 20px; border-top: 1px solid #eeeeee; font-size: 14px; color: #999999; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://www.suaempresa.com.br"><img src="https://www.suaempresa.com.br/logo.png" alt="Logo da [Nome da Loja]"></a>
        </div>
        <div class="content">
            <h1>Olá, {{customer.first_name}}!</h1>
            <p>Esperamos que você esteja adorando seu novo(a) <strong>{{product.name}}</strong>!</p>
            <p>Sua opinião é fundamental para nós e ajuda outros clientes a fazerem as melhores escolhas. Que tal compartilhar sua experiência?</p>

            <div class="product-card">
                <img src="https://www.suaempresa.com.br/imagens/caneca-termica.jpg" alt="Caneca Térmica Inox">
                <div class="details">
                    <h3>Caneca Térmica Inox - 500ml</h3>
                    <p>Qualidade premium para suas bebidas.</p>
                </div>
            </div>

            <a href="https://www.suaempresa.com.br/produto/caneca-termica/avaliar?order={{order.id}}" class="review-button">Deixar Minha Avaliação Agora</a>

            <p style="margin-top: 30px;">Leva apenas alguns minutos e faz uma grande diferença! Se tiver qualquer problema, por favor, entre em contato conosco.</p>
            <p>Atenciosamente,<br>A Equipe [Nome da Loja]</p>
        </div>
        <div class="footer">
            <p>[Nome da Loja] | [Endereço da Loja] | [Telefone] | [Email de Suporte]</p>
            <p><a href="https://www.suaempresa.com.br/privacidade">Política de Privacidade</a> | <a href="https://www.suaempresa.com.br/termos">Termos de Uso</a></p>
        </div>
    </div>
</body>
</html>
```

---

## Checklist

-   [x] Gatilho de "Compra Concluída" ou "Pagamento Aprovado" configurado na ferramenta de automação.
-   [x] Email de confirmação de pedido enviado instantaneamente com número do pedido e itens detalhados.
-   [x] Link de rastreamento de pedido funcional e visível no email de confirmação.
-   [x] Personalização de nome do cliente e detalhes específicos do produto em todos os emails da sequência.
-   [x] Email de "Dicas de Uso" ou "Boas-Vindas" agendado para o momento ideal (24-72h após compra/entrega).
-   [x] Solicitação de avaliação do produto enviada após um período adequado de uso (ex: 7 dias pós-entrega).
-   [x] Segmentação de clientes para ofertas de upsell/cross-sell baseada nos produtos comprados.
-   [x] Testes A/B em linhas de assunto e calls-to-action para otimização da taxa de abertura e cliques.
-   [x] Exclusão de clientes que já avaliaram o produto de emails de solicitação de review subsequentes.
-   [x] Monitoramento contínuo das métricas de abertura, cliques, conversão e feedback de reviews.

---

## Métricas de Referência

| Métrica                      | Benchmark (Varejo Online) | Meta (Otimizado) |
|------------------------------|---------------------------|------------------|
| Taxa de Abertura             | 25-35%                    | 35-45%           |
| Taxa de Cliques (CTR)        | 3-6%                      | 6-10%            |
| Taxa de Conversão (Recompra) | 2-5%                      | 5-8%             |
| Taxa de Avaliações Recebidas | 5-10% (do total de emails) | 10-15%           |
| Taxa de Cancelamento (Churn) | 20-30% (geral)            | 10-15%           |
| LTV (Lifetime Value)         | Varia muito               | Aumento de 15-20% |

---

## Erros Comuns

1.  **Emails Genéricos e Despersonalizados**: Enviar o mesmo email padrão para todos os clientes, sem referência ao produto específico comprado ou ao nome do cliente.
    *   **Como evitar**: Utilize tags de personalização (`{{customer.name}}`, `{{order.product_name}}`) e segmente as automações por tipo de produto ou categoria. Por exemplo, um cliente que comprou um curso online deve receber um email de onboarding com links para as aulas, não um guia de montagem de móveis.
2.  **Sobrecarga de Emails ou Timing Inadequado**: Bombardear o cliente com muitos emails em um curto período ou enviar mensagens fora do momento ideal (ex: pedir avaliação antes mesmo do produto ser entregue).
    *   **Como evitar**: Defina espaçamentos lógicos entre os emails (ex: 0h, 24h, 7 dias, 14 dias após a compra/entrega). Priorize a entrega de valor em cada comunicação, em vez da quantidade. Use atrasos baseados no status do pedido (ex: "após entrega").
3.  **Falta de Call to Action (CTA) Claro**: Emails sem um propósito específico ou um botão/link óbvio para a próxima ação desejada pelo cliente.
    *   **Como evitar**: Cada email deve ter um único CTA principal e claro. Por exemplo, um email de confirmação deve ter "Rastrear Meu Pedido", um de avaliação deve ter "Deixar Minha Avaliação Agora", e um de cross-sell deve ter "Explorar Acessórios Complementares".
4.  **Ignorar o Feedback Negativo**: Não ter um processo estabelecido para coletar e responder a avaliações ou comentários negativos.
    *   **Como evitar**: Configure alertas para avaliações negativas e tenha uma equipe pronta para responder e resolver problemas rapidamente. Uma resposta atenciosa a um feedback negativo pode transformar uma experiência ruim em uma oportunidade de fidelização.

---

## Dicas Avançadas

1.  **Segmentação Pós-Engajamento Condicional**: Crie ramificações dinâmicas na sequência com base no engajamento do cliente. Se um cliente abriu o email de cross-sell, mas não clicou, envie um lembrete com um benefício adicional (ex: "Última chance: 10% OFF nos acessórios!"). Se clicou e comprou, inicie uma nova sequência de nutrição específica para o novo produto adquirido.
2.  **Automação de Resgate de Carrinho Pós-Primeira Compra**: Implemente uma automação que identifica clientes que fizeram uma primeira compra, mas abandonaram um segundo carrinho em um curto período. Acione uma sequência específica com um incentivo (ex: frete grátis na segunda compra) para capitalizar o momento de satisfação pós-compra.
3.  **Uso de Prova Social Dinâmica e Personalizada**: Integre reviews e depoimentos de outros clientes (com consentimento) diretamente nos emails da sequência, especialmente nos de cross-sell/upsell. Mostre depoimentos de clientes que compraram produtos similares ou complementares ao que o cliente já possui, aumentando a confiança e a relevância.
4.  **Sequências Baseadas no LTV (Lifetime Value) ou Comportamento de Compra**: Desenvolva caminhos de automação distintos para clientes de alto LTV ou para aqueles que demonstram padrões de compra recorrentes. Ofereça a esses segmentos ofertas exclusivas, acesso antecipado a lançamentos ou convites para eventos VIP, reforçando o status de cliente valorizado.
5.  **Personalização Hiper-contextual com IA**: Utilize ferramentas de inteligência artificial para analisar o histórico completo de navegação e compra do cliente, não apenas o último item. Com base nesses dados, gere recomendações de produtos e conteúdos nos emails de upsell/cross-sell que são altamente preditivos e relevantes para o perfil individual do cliente, superando a simples sugestão de "quem comprou X também comprou Y".