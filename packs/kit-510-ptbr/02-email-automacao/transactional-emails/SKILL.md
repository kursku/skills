---
name: transactional-emails
description: "Transactional Emails — Skill especializada para transactional emails"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Transactional Emails

Esta skill capacita o Claude a projetar, implementar e otimizar comunicações automatizadas essenciais que respondem a ações específicas do usuário ou eventos do sistema.

---

## Keywords

Confirmação de Pedido, Redefinição de Senha, Notificação de Envio, Ativação de Conta, Fatura, Recibo de Pagamento, Atualização de Status, Notificação Legal, Carrinho Abandonado, Boas-vindas.

---

## Quick Start

1.  **Integrar Provedor SMTP/API**: Conecte sua aplicação a um serviço de envio de e-mails transacionais (ex: SendGrid, Mailgun, AWS SES) para garantir alta entregabilidade.
2.  **Mapear Eventos e Triggers**: Identifique cada ação do usuário ou evento do sistema que necessita de uma comunicação imediata (ex: `compra_finalizada`, `senha_solicitada`, `envio_pacote`).
3.  **Desenvolver Templates HTML/AMP Responsivos**: Crie modelos de e-mail pré-aprovados com design limpo, branding consistente e otimizados para visualização em dispositivos móveis, sem elementos de marketing intrusivos.
4.  **Configurar Webhooks de Status de Entrega**: Implemente callbacks para receber notificações sobre a entrega, abertura, cliques, rejeições (bounces) e denúncias de spam, alimentando um dashboard de monitoramento.

---

## Core Workflows

### Workflow 1: Confirmação de Pedido com Rastreamento e Fatura

Este workflow automatiza a comunicação pós-compra, garantindo que o cliente receba todas as informações necessárias e acompanhe seu pedido.

1.  **Trigger de Compra Concluída**: O sistema de e-commerce detecta a finalização e aprovação de um pedido. Imediatamente, ele aciona o envio de um e-mail de confirmação.
    *   **Exemplo de Ação**: Após o pagamento ser aprovado para o `Pedido #PX123456789`, o microsserviço de pedidos envia uma mensagem para a fila de eventos `sqs.ecommerce.order_confirmed` com o JSON do pedido completo.
2.  **Envio do E-mail de Confirmação de Pedido**: Um serviço de e-mail transacional (ex: `notification-service`) consome o evento e renderiza um template HTML com os dados do pedido.
    *   **Conteúdo Necessário**: Número do pedido, itens comprados (nome, quantidade, preço), subtotal, frete, total, endereço de entrega e cobrança, forma de pagamento, e um link direto para a fatura (PDF) e para a página de status do pedido.
    *   **Exemplo de Assunto**: `Seu Pedido #PX123456789 na Loja XYZ foi Confirmado!`
3.  **Atualização de Status para "Enviado"**: Quando o pedido é despachado pela transportadora, o status é atualizado no sistema. Este evento dispara o segundo e-mail.
    *   **Exemplo de Ação**: O sistema de logística atualiza o `Pedido #PX123456789` para `status: shipped` e gera um código de rastreamento `BR123456789BR`. Um evento `sqs.ecommerce.order_shipped` é emitido.
4.  **Envio do E-mail de Notificação de Envio**: O serviço de e-mail consome o evento `order_shipped` e envia uma notificação com o código de rastreamento.
    *   **Conteúdo Necessário**: Confirmação do envio, código de rastreamento clicável, link direto para a página de rastreamento da transportadora, e uma estimativa de entrega.
    *   **Exemplo de Assunto**: `Boas Notícias! Seu Pedido #PX123456789 foi Enviado!`
5.  **Monitoramento de Entregabilidade**: Utilize webhooks do provedor de e-mail para registrar aberturas, cliques e eventuais bounces ou denúncias, ajustando a base de dados de clientes conforme necessário.
    *   **Exemplo de Ação**: Um webhook do SendGrid envia um POST para `/api/email-status` quando o e-mail de envio é aberto, atualizando o `last_opened_at` no registro do cliente.

### Workflow 2: Redefinição de Senha Segura e Confirmação de Alteração

Este workflow garante um processo seguro e claro para usuários que precisam redefinir suas senhas, minimizando riscos de segurança.

1.  **Solicitação de Redefinição de Senha**: O usuário acessa a página "Esqueci minha senha", insere seu e-mail e envia a solicitação.
    *   **Exemplo de Ação**: O frontend envia um `POST /api/password/forgot` com `{ "email": "usuario@exemplo.com" }`. O backend gera um token único e de curta duração (ex: 15 minutos de validade, 1 uso), associado ao e-mail do usuário.
2.  **Envio do E-mail de Redefinição**: Um serviço de autenticação envia um e-mail com um link seguro contendo o token gerado.
    *   **Conteúdo Necessário**: Instrução clara para clicar no link, aviso sobre a validade do link, e uma nota de segurança informando que, se não foi o usuário quem solicitou, ele deve ignorar o e-mail.
    *   **Exemplo de Assunto**: `Redefinição de Senha para sua conta na Loja XYZ`
    *   **Regra de Ouro**: Nunca inclua a nova senha no e-mail; o link deve levar a uma página onde o usuário define a nova senha.
3.  **Validação do Token e Definição da Nova Senha**: O usuário clica no link e é redirecionado para uma página onde pode inserir a nova senha. O sistema valida o token antes de permitir a alteração.
    *   **Exemplo de Ação**: O usuário envia um `POST /api/password/reset` com `{ "token": "abc123def456", "new_password": "SenhaSegura123!" }`. O backend verifica a validade e expiração do token, hasheia a nova senha e a armazena. O token é invalidado imediatamente após o uso.
4.  **Envio do E-mail de Confirmação de Senha Alterada (Opcional, mas Recomendado)**: Após a redefinição bem-sucedida, um e-mail de confirmação é enviado.
    *   **Conteúdo Necessário**: Confirmação da alteração, data/hora da alteração e um aviso para entrar em contato se o usuário não reconhecer a ação.
    *   **Exemplo de Assunto**: `Sua senha na Loja XYZ foi alterada com sucesso.`
    *   **Benefício**: Aumenta a segurança, notificando o usuário sobre uma possível atividade não autorizada em sua conta.

---

## Templates

### Confirmação de Pedido Loja XYZ

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Seu Pedido #PX123456789 foi Confirmado!</title>
    <style type="text/css">
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .header { background-color: #f8f8f8; padding: 10px 20px; text-align: center; border-bottom: 1px solid #ddd; }
        .header img { max-width: 150px; }
        .content { padding: 20px 0; }
        .product-list { width: 100%; border-collapse: collapse; margin-top: 15px; }
        .product-list th, .product-list td { border: 1px solid #eee; padding: 8px; text-align: left; }
        .product-list th { background-color: #f2f2f2; }
        .total { text-align: right; margin-top: 20px; font-size: 1.1em; font-weight: bold; }
        .footer { text-align: center; margin-top: 30px; font-size: 0.8em; color: #777; border-top: 1px solid #eee; padding-top: 15px; }
        .button { display: inline-block; background-color: #007bff; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://www.loja-xyz.com/logo.png" alt="Loja XYZ">
            <h1>Confirmação de Pedido</h1>
        </div>
        <div class="content">
            <p>Olá **Maria Silva**,</p>
            <p>Agradecemos por sua compra na Loja XYZ! Seu pedido **#PX123456789** foi confirmado e está sendo processado.</p>
            <p>Detalhes do seu pedido:</p>
            <table class="product-list">
                <thead>
                    <tr>
                        <th>Produto</th>
                        <th>Qtd.</th>
                        <th>Preço Unit.</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Café Especial Blend da Casa 250g</td>
                        <td>2</td>
                        <td>R$ 35,00</td>
                        <td>R$ 70,00</td>
                    </tr>
                    <tr>
                        <td>Xícara Cerâmica Exclusiva</td>
                        <td>1</td>
                        <td>R$ 49,90</td>
                        <td>R$ 49,90</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3" style="text-align:right;">Subtotal:</td>
                        <td>R$ 119,90</td>
                    </tr>
                    <tr>
                        <td colspan="3" style="text-align:right;">Frete (Expresso):</td>
                        <td>R$ 15,00</td>
                    </tr>
                    <tr>
                        <td colspan="3" style="text-align:right;">Total:</td>
                        <td>R$ 134,90</td>
                    </tr>
                </tfoot>
            </table>

            <p><strong>Forma de Pagamento:</strong> Cartão de Crédito (final **** 1234)</p>
            <p><strong>Endereço de Entrega:</strong><br>
            Rua das Flores, 123, Ap 45<br>
            Bairro Jardins, São Paulo - SP<br>
            CEP: 01234-567</p>

            <a href="https://www.loja-xyz.com/meus-pedidos/PX123456789" class="button">Ver Status do Pedido</a>
            <p>Você pode acessar sua fatura em PDF <a href="https://www.loja-xyz.com/fatura/PX123456789.pdf">clicando aqui</a>.</p>
            <p>Em caso de dúvidas, entre em contato com nosso suporte.</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 Loja XYZ. Todos os direitos reservados.</p>
            <p>Este é um e-mail transacional e não contém publicidade.</p>
        </div>
    </div>
</body>
</html>
```

### Redefinição de Senha Segura Loja XYZ

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Redefinição de Senha para Loja XYZ</title>
    <style type="text/css">
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .header { background-color: #f8f8f8; padding: 10px 20px; text-align: center; border-bottom: 1px solid #ddd; }
        .header img { max-width: 150px; }
        .content { padding: 20px 0; }
        .button { display: inline-block; background-color: #dc3545; color: #ffffff; padding: 12px 25px; text-decoration: none; border-radius: 5px; margin-top: 20px; font-weight: bold; }
        .security-note { background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; margin-top: 25px; font-size: 0.9em; color: #856404; }
        .footer { text-align: center; margin-top: 30px; font-size: 0.8em; color: #777; border-top: 1px solid #eee; padding-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://www.loja-xyz.com/logo.png" alt="Loja XYZ">
            <h1>Redefinição de Senha</h1>
        </div>
        <div class="content">
            <p>Olá,</p>
            <p>Recebemos uma solicitação para redefinir a senha da sua conta na Loja XYZ.</p>
            <p>Para criar uma nova senha, clique no botão abaixo:</p>
            <p style="text-align: center;">
                <a href="https://www.loja-xyz.com/redefinir-senha?token=abc123def456789ghi" class="button">Redefinir Minha Senha</a>
            </p>
            <p>Este link é válido por **15 minutos**. Por motivos de segurança, ele só poderá ser utilizado uma única vez.</p>
            <div class="security-note">
                <p><strong>Importante:</strong> Se você não solicitou a redefinição de senha, por favor, ignore este e-mail. Sua senha atual permanecerá segura e inalterada.</p>
            </div>
            <p>Em caso de dúvidas, entre em contato com nosso suporte.</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 Loja XYZ. Todos os direitos reservados.</p>
            <p>Este é um e-mail transacional e não contém publicidade.</p>
        </div>
    </div>
</body>
</html>
```

---

## Checklist

- [x] O e-mail é disparado imediatamente após a ação relevante do usuário ou evento do sistema.
- [x] O remetente (`From` e `Reply-To`) é um endereço de e-mail reconhecível e profissional (ex: `noreply@suaempresa.com.br`, `atendimento@suaempresa.com.br`).
- [x] DKIM e SPF estão configurados corretamente para o domínio do remetente, garantindo autenticidade e entregabilidade.
- [x] O conteúdo do e-mail é 100% focado na informação transacional, sem elementos de marketing ou promoções.
- [x] Todos os links (rastreamento, fatura, redefinição) são seguros (HTTPS) e específicos para a transação ou usuário.
- [x] O design do e-mail é responsivo e otimizado para visualização em dispositivos móveis.
- [x] Existe uma versão em texto plano do e-mail para clientes de e-mail que não renderizam HTML.
- [x] Os templates são personalizáveis com dados dinâmicos do usuário e da transação (nome, ID do pedido, itens, valores).
- [x] São implementados webhooks para monitorar aberturas, cliques, bounces e denúncias de spam.
- [x] Em casos de redefinição de senha, o link é de uso único e tem tempo de expiração curto (ex: 15-30 minutos).

---

## Métricas de Referência

| Métrica               | Benchmark (Indústria) | Meta (Atingível) |
|-----------------------|-----------------------|------------------|
| Taxa de Abertura      | 70% - 90%             | > 85%            |
| Taxa de Cliques (CTR) | 15% - 30%             | > 20%            |
| Taxa de Rejeição      | < 2%                  | < 1%             |
| Taxa de Reclamação    | < 0.1%                | < 0.05%          |
| Tempo de Entrega      | < 5 segundos          | < 2 segundos     |

---

## Erros Comuns

1.  **Misturar Conteúdo Transacional com Marketing**: Enviar uma confirmação de pedido que também inclui banners de "confira nossos outros produtos" ou "promoções do mês". Isso dilui a mensagem principal, pode violar regulamentações de privacidade (LGPD/GDPR para opt-out) e aumentar a taxa de denúncias de spam, prejudicando a reputação do remetente para e-mails críticos.
2.  **Links de Redefinição de Senha Permanentes ou Não Únicos**: Gerar um link de redefinição de senha que não expira ou que pode ser usado múltiplas vezes. Isso cria uma grave vulnerabilidade de segurança, permitindo que um invasor com acesso ao e-mail redefina a senha indefinidamente ou em momentos futuros. A solução é tokens de uso único e com validade de 15-30 minutos.
3.  **Não Enviar Confirmação Imediata de Pedido/Registro**: Demorar para enviar e-mails críticos como confirmação de pedido, registro de conta ou redefinição de senha. A expectativa do usuário é de gratificação instantânea. Atrasos geram ansiedade, chamados desnecessários ao suporte e uma percepção negativa da marca, como "Meu pagamento foi processado?" ou "Será que meu registro deu certo?".
4.  **Ausência de Versão em Texto Plano**: Não incluir uma versão `text/plain` no e-mail. Alguns clientes de e-mail (especialmente em ambientes corporativos ou mais antigos) podem não renderizar HTML, resultando em um e-mail em branco ou ilegível. Sempre forneça uma alternativa em texto simples que contenha as informações essenciais.

---

## Dicas Avançadas

1.  **Personalização Dinâmica Baseada em Comportamento**: Utilize dados do CRM ou CDP para enriquecer e-mails transacionais. Por exemplo, em um e-mail de "Boas-vindas" para um novo usuário, inclua sugestões de produtos ou recursos baseados em seu histórico de navegação ou nos itens que ele visualizou antes de se registrar. Ex: "Olá, [Nome do Cliente]! Vimos que você se interessou por [Produto X], que tal explorar mais?"
2.  **Testes A/B Contínuos para Micro-Otimizações**: Em vez de testar grandes mudanças, realize testes A/B em elementos sutis de e-mails transacionais. Teste diferentes frases no pré-header para e-mails de notificação de envio (ex: "Seu pacote está a caminho!" vs "Acompanhe seu pedido agora!"). Pequenas melhorias na taxa de abertura ou clique em e-mails de alto volume podem gerar resultados significativos.
3.  **Implementação de AMP for Email para Interatividade**: Para e-mails como "Confirmação de Agendamento" ou "Pesquisa de Satisfação Pós-Compra", utilize AMP for Email. Isso permite que o usuário confirme um horário ou responda a uma pesquisa diretamente dentro do e-mail, sem precisar sair para um site externo, aumentando a taxa de engajamento e conversão.
4.  **Monitoramento Ativo da Reputação do Remetente**: Utilize ferramentas como Google Postmaster Tools, Outlook SNDS e Sender Score para acompanhar a reputação do seu IP e domínio. Métricas como taxa de spam, rejeição e erros de autenticação são cruciais. Uma reputação baixa pode levar seus e-mails transacionais a caírem na caixa de spam, mesmo sendo críticos. Configure alertas para desvios.
5.  **Gerenciamento de Fluxos de "Carrinho Abandonado" com Gatilhos Específicos**: Para e-mails de recuperação de carrinho, não use um "lembrete genérico". Integre com o histórico de navegação e o valor do carrinho. Se o carrinho abandonado tiver itens de alto valor, o e-mail pode incluir um CTA para "Falar com um especialista" ou "Revisar itens no carrinho". Se o cliente já visualizou a página de frete, o e-mail pode focar em "Frete grátis para sua compra!".