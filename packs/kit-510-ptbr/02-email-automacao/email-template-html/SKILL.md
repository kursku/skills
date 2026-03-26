---
name: email-template-html
description: "Email Template Html — Skill especializada para email template html"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Email Template Html

Esta skill capacita o Claude a criar, otimizar e integrar templates HTML de email responsivos para sequências de automação e campanhas de nurturing.

---

## Keywords

HTML email, MJML, responsividade email, email marketing, CSS inline, automação email, litmus testing, dark mode email, design responsivo, boilerplate email, acessibilidade email, AMP for Email.

---

## Quick Start

1.  Escolha uma estrutura HTML base robusta (boilerplate como Cerberus ou framework MJML).
2.  Estruture o layout primário exclusivamente com tabelas aninhadas para compatibilidade universal.
3.  Converta todo o CSS essencial para estilos inline antes do envio para assegurar renderização.
4.  Teste o template em múltiplas plataformas de email (desktop, web, mobile) usando ferramentas de pré-visualização.
5.  Valide o código HTML para erros de sintaxe e implemente as meta tags de Dark Mode.

---

## Core Workflows

### Workflow 1: Criação de Template HTML Responsivo para Sequência de Boas-Vindas

Este workflow detalha a construção de um email HTML responsivo do zero, ideal para a primeira mensagem de uma sequência de boas-vindas, garantindo que seja visualmente atraente e funcional em diversos clientes de email.

1.  **Seleção da Estrutura Base**: Inicie o desenvolvimento utilizando um boilerplate HTML para email, como o "HTML Email Boilerplate" ou o "Cerberus", que já oferece resiliência contra as peculiaridades de diferentes clientes de email. Este passo minimiza a necessidade de "hacks" posteriores.
    *   **Exemplo de Snippet Inicial**:
        ```html
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="x-apple-disable-message-reformatting">
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <title>Bem-vindo à Nossa Comunidade!</title>
            <!-- [Estilos globais e media queries aqui] -->
        </head>
        <body>
            <!-- Conteúdo do email aqui -->
        </body>
        </html>
        ```
2.  **Definição de Layout com Tabelas**: Construa o layout do email utilizando exclusivamente tabelas aninhadas (`<table>`). Divida o email em seções lógicas: cabeçalho, banner principal, bloco de conteúdo, Call-to-Action (CTA) e rodapé. Cada seção deve ser uma nova tabela ou uma célula de tabela.
    *   **Exemplo de Estrutura de Conteúdo Principal**:
        ```html
        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td style="padding: 20px 0;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="margin: 0 auto; background-color: #ffffff;">
                        <tr>
                            <td style="padding: 30px 40px; text-align: center; font-family: Arial, sans-serif; font-size: 24px; color: #333333;">
                                Olá, {{nome_do_cliente}}!
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 0 40px 30px; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.5; color: #555555;">
                                Seja muito bem-vindo(a) à nossa comunidade! Estamos empolgados por ter você conosco. Prepare-se para receber conteúdos exclusivos e as últimas novidades diretamente na sua caixa de entrada.
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        ```
3.  **Otimização e Incorporação de Imagens**: Adicione tags `<img>` para banners e logotipos, sempre especificando `width` e `height` explícitos. Garanta que todas as imagens estejam hospedadas externamente (CDN) e que possuam um `alt` text descritivo para acessibilidade e quando as imagens não carregam.
    *   **Exemplo de Imagem Responsiva**:
        ```html
        <img src="https://assets.exemplo.com/banner-boas-vindas.jpg" alt="Banner de Boas-Vindas à comunidade" width="600" style="display: block; max-width: 100%; height: auto; border: 0;">
        ```
4.  **Estilização Inline Essencial**: Converta todo o CSS que afeta o layout e a aparência crítica (cores, fontes, espaçamento) para estilos inline (`style="..."`). Ferramentas como Premailer ou o inlinador de CSS do Mailchimp podem automatizar este processo, garantindo que os estilos sejam aplicados mesmo em clientes restritivos.
    *   **Exemplo de Estilo Inline**:
        ```html
        <p style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 16px; color: #333333; line-height: 1.6; margin: 0 0 15px;">
            Este é um parágrafo com estilos aplicados diretamente.
        </p>
        ```
5.  **Criação de CTA Responsivo e Acessível**: Desenvolva botões de Call-to-Action (CTA) utilizando tabelas aninhadas para garantir que sejam renderizados como botões clicáveis em todos os clientes, incluindo Outlook. Aplique estilos inline para cores, padding e fonte, e inclua um `target="_blank"` nos links.
    *   **Exemplo de CTA em Tabela**:
        ```html
        <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="margin: 20px auto;">
            <tr>
                <td align="center" bgcolor="#007bff" style="border-radius: 5px;">
                    <a href="https://exemplo.com/recursos" target="_blank" style="font-size: 16px; font-family: Arial, sans-serif; color: #ffffff; text-decoration: none; border-radius: 5px; padding: 12px 24px; border: 1px solid #007bff; display: inline-block;">
                        Explorar Nossos Recursos
                    </a>
                </td>
            </tr>
        </table>
        ```
6.  **Teste de Responsividade e Cliente**: Antes do envio, utilize plataformas como Litmus ou Email on Acid para testar a renderização do email em uma vasta gama de clientes (Gmail, Outlook Desktop, Outlook Web, Apple Mail, iOS Mail, Android Mail). Preste atenção à quebra de layout, sobreposição de texto e funcionalidade dos CTAs.

### Workflow 2: Otimização de Template Existente para Dark Mode e Acessibilidade em Email de Carrinho Abandonado

Este workflow foca em aprimorar um template de email de carrinho abandonado já existente, tornando-o compatível com o modo escuro (Dark Mode) e melhorando sua acessibilidade para todos os usuários.

1.  **Análise de Contraste e Identificação de Problemas**: Analise o template atual para combinações de cores que possam se tornar ilegíveis ou visualmente problemáticas em Dark Mode. Ferramentas como "WebAIM Contrast Checker" podem ajudar a identificar textos com baixo contraste. Observe logos e ícones que podem ter fundos que não se adaptam.
2.  **Implementação de Meta Tags para Dark Mode**: Adicione as meta tags `color-scheme` e `supported-color-schemes` dentro da tag `<head>` do HTML. Estas tags informam aos clientes de email a preferência de esquema de cores do seu email e qual esquema ele suporta.
    *   **Exemplo**:
        ```html
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="x-apple-disable-message-reformatting">
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <title>Seu Carrinho te Espera!</title>
            <!-- [Estilos Dark Mode e media queries aqui] -->
        </head>
        ```
3.  **Uso de Media Queries para Estilos Específicos de Dark Mode**: Dentro da tag `<style>` no `<head>`, implemente media queries `@media (prefers-color-scheme: dark)` para aplicar estilos CSS que invertem cores de fundo e texto, ou ajustam elementos específicos quando o Dark Mode está ativo.
    *   **Exemplo de Media Query**:
        ```html
        <style>
            /* Estilos globais para Light Mode */
            body { background-color: #f6f6f6; color: #333333; }
            .content-area { background-color: #ffffff; }

            /* Estilos para Dark Mode */
            @media (prefers-color-scheme: dark) {
                body { background-color: #1a1a1a !important; color: #e0e0e0 !important; }
                .content-area { background-color: #2c2c2c !important; }
                .darkmode-text { color: #e0e0e0 !important; }
                /* Ajuste de imagem para Dark Mode */
                .dark-img { display: block !important; width: auto !important; overflow: visible !important; float: none !important; max-height: inherit !important; max-width: inherit !important; line-height: auto !important; margin-top: 0px !important; visibility: inherit !important; }
                .light-img { display: none; display: none !important; }
            }
        </style>
        ```
4.  **Otimização de Imagens para Dark Mode**: Para logos ou ícones que não ficam bem em Dark Mode, use uma técnica de "troca de imagem" com classes CSS e media queries, mostrando uma versão clara em Light Mode e uma versão escura em Dark Mode.
    *   **Exemplo de Troca de Imagem**:
        ```html
        <!-- Imagem para Light Mode -->
        <img class="light-img" src="https://assets.exemplo.com/logo-claro.png" alt="Logo da Empresa" width="150" style="display: block;">
        <!-- Imagem para Dark Mode (inicialmente oculta) -->
        <img class="dark-img" src="https://assets.exemplo.com/logo-escuro.png" alt="Logo da Empresa" width="150" style="display: none; mso-hide: all;">
        ```
5.  **Melhorias de Acessibilidade**:
    *   **Textos Alternativos (Alt Text)**: Verifique se todas as imagens têm `alt` text descritivo e conciso. Para imagens puramente decorativas, use `alt=""`.
    *   **Contraste de Cores**: Garanta que o contraste entre texto e fundo seja de no mínimo 4.5:1 (padrão WCAG AA) tanto no Light Mode quanto no Dark Mode.
    *   **Links e Botões Acessíveis**: Assegure que os textos dos links sejam descritivos (evite "clique aqui") e que os botões tenham uma área de clique de pelo menos 44x44 pixels em dispositivos móveis.
    *   **Hierarquia e Semântica**: Embora `<h1>` a `<h6>` não sejam recomendados em emails, use `<strong>` para enfatizar texto e `role="presentation"` em tabelas que servem apenas para layout.
6.  **Validação Cruzada e Testes de Acessibilidade**: Teste o email em clientes que suportam Dark Mode (Gmail mobile, Outlook mobile, Apple Mail) e verifique a renderização. Além disso, utilize ferramentas de teste de acessibilidade e, se possível, leitores de tela (VoiceOver no iOS, NVDA no Windows) para simular a experiência de usuários com deficiência visual.

---

## Templates

### Template de Email de Boas-Vindas Responsivo

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Bem-vindo à Comunidade [Nome da Empresa]!</title>
    <!--[if mso]>
    <noscript>
        <xml>
            <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
    </noscript>
    <![endif]-->
    <style>
        :root {
            color-scheme: light dark;
            supported-color-schemes: light dark;
        }
        @media (prefers-color-scheme: dark) {
            body { background-color: #1a1a1a !important; color: #e0e0e0 !important; }
            .darkmode-text { color: #e0e0e0 !important; }
            .darkmode-bg { background-color: #2c2c2c !important; }
            .button-darkmode { background-color: #0056b3 !important; border-color: #0056b3 !important; }
            .button-darkmode a { color: #ffffff !important; }
        }
    </style>
</head>
<body style="margin: 0; padding: 0; word-spacing: normal; background-color: #f6f6f6;">
    <div role="article" aria-roledescription="email" lang="pt-BR" style="text-size-adjust: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;">
        <table role="presentation" style="width:100%; border-collapse:collapse; border:0; border-spacing:0; background:#f6f6f6;">
            <tr>
                <td align="center" style="padding:0;">
                    <table role="presentation" style="width:600px; border-collapse:collapse; border:1px solid #cccccc; border-spacing:0; text-align:left; background-color: #ffffff;" class="darkmode-bg">
                        <tr>
                            <td align="center" style="padding:40px 0 30px 0; background:#007bff;" class="button-darkmode">
                                <img src="https://assets.exemplo.com/logo-empresa-branca.png" alt="Logo da Empresa" width="160" style="height:auto; display:block;" />
                            </td>
                        </tr>
                        <tr>
                            <td style="padding:36px 30px 42px 30px;">
                                <table role="presentation" style="width:100%; border-collapse:collapse; border:0; border-spacing:0;">
                                    <tr>
                                        <td style="padding:0 0 15px 0; color:#153643; font-family:Arial,sans-serif; font-size:24px; line-height:28px; font-weight:bold;" class="darkmode-text">
                                            Olá, {{nome_do_cliente}}! Seja bem-vindo(a)!
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0 0 15px 0; color:#153643; font-family:Arial,sans-serif; font-size:16px; line-height:24px;" class="darkmode-text">
                                            É um prazer tê-lo(a) conosco na comunidade [Nome da Empresa]. Estamos muito felizes por você ter se juntado a nós!
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0 0 25px 0; color:#153643; font-family:Arial,sans-serif; font-size:16px; line-height:24px;" class="darkmode-text">
                                            Aqui, você encontrará os melhores conteúdos sobre desenvolvimento web, design e marketing digital. Para começar, confira nosso guia exclusivo para novos membros:
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="padding:0;">
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
                                                <tr>
                                                    <td align="center" bgcolor="#007bff" style="border-radius:5px;" class="button-darkmode">
                                                        <a href="https://exemplo.com/guia-inicio" target="_blank" style="font-size:16px; font-family:Arial,sans-serif; color:#ffffff; text-decoration:none; border-radius:5px; padding:12px 24px; border:1px solid #007bff; display:inline-block;">
                                                            Acessar Guia de Início Rápido
                                                        </a>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:30px 0 0 0; color:#153643; font-family:Arial,sans-serif; font-size:14px; line-height:20px;" class="darkmode-text">
                                            Se tiver alguma dúvida, <a href="mailto:suporte@exemplo.com" style="color:#007bff; text-decoration:underline;">entre em contato</a>.
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding:30px; background:#ee4c50;" class="button-darkmode">
                                <table role="presentation" style="width:100%; border-collapse:collapse; border:0; border-spacing:0; font-size:9px; font-family:Arial,sans-serif;">
                                    <tr>
                                        <td style="padding:0; width:50%;" align="left">
                                            <p style="margin:0; font-size:14px; line-height:16px; font-family:Arial,sans-serif; color:#ffffff;">
                                                &copy; 2024 [Nome da Empresa]. Todos os direitos reservados.<br/><a href="https://exemplo.com/politica-privacidade" style="color:#ffffff; text-decoration:underline;">Política de Privacidade</a>
                                            </p>
                                        </td>
                                        <td style="padding:0; width:50%;" align="right">
                                            <table role="presentation" style="border-collapse:collapse; border:0; border-spacing:0;">
                                                <tr>
                                                    <td style="padding:0 0 0 10px; width:38px;">
                                                        <a href="https://twitter.com/exemplo" style="color:#ffffff;"><img src="https://assets.exemplo.com/twitter.png" alt="Twitter" width="38" style="height:auto; display:block; border:0;" /></a>
                                                    </td>
                                                    <td style="padding:0 0 0 10px; width:38px;">
                                                        <a href="https://facebook.com/exemplo" style="color:#ffffff;"><img src="https://assets.exemplo.com/facebook.png" alt="Facebook" width="38" style="height:auto; display:block; border:0;" /></a>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>
```

### Template de Email de Carrinho Abandonado Otimizado para Dark Mode

```html
<!DOCTYPE html>
<html lang="pt-