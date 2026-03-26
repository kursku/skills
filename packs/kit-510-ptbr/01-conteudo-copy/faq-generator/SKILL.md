---
name: faq-generator
description: "Faq Generator — Skill especializada em conteúdo & copywriting"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 01-conteudo-copy
  domain: conteúdo-copywriting
  updated: 2026-03-01
risk: safe
---

# Faq Generator

Esta skill capacita o Claude a gerar FAQs abrangentes, persuasivas e otimizadas para SEO, respondendo às principais dúvidas de usuários e clientes sobre produtos, serviços ou tópicos específicos, com o objetivo de reduzir chamados de suporte e aumentar a conversão.

---

## Keywords

Geração de FAQ, Perguntas Frequentes, Conteúdo de Suporte, Otimização SEO FAQ, Copywriting para FAQ, Respostas a Dúvidas, Conteúdo Explicativo, Engajamento do Cliente, Redução de Suporte, Conteúdo Persuasivo.

---

## Quick Start

1.  **Forneça o Tópico/Produto/Serviço**: Indique o assunto principal da FAQ (ex: "Plano de Assinatura Premium da Soft SaaS", "Lançamento do Smartphone X", "Serviço de Consultoria de Marketing Digital").
2.  **Liste Dúvidas Comuns (Opcional)**: Se tiver, forneça uma lista inicial de perguntas que os usuários costumam fazer. Caso contrário, o Claude as inferirá com base no tópico.
3.  **Defina o Tom de Voz**: Especifique o tom desejado (ex: "formal e informativo", "amigável e acessível", "técnico e direto", "persuasivo e motivador").
4.  **Especifique o Objetivo Principal**: Qual o principal objetivo da FAQ? (ex: "Reduzir chamados de suporte em 20%", "Aumentar a taxa de conversão da página de vendas em 5%", "Educar sobre um novo recurso de forma clara").

---

## Core Workflows

### Workflow 1: Geração de FAQ Completa a partir de Tópico Único

Este workflow é ideal para criar uma FAQ do zero, cobrindo as dúvidas mais comuns e importantes sobre um tema específico, com foco em clareza e persuasão.

**Passos Detalhados:**

1.  **Entrada**: O usuário fornece o tópico principal (ex: "Plano de Assinatura Premium da Soft SaaS"), o tom de voz ("amigável e informativo") e o objetivo ("reduzir dúvidas e incentivar upgrade").
2.  **Pesquisa de Dúvidas (Simulada)**: O Claude simulará uma pesquisa de intenção de busca e identificará as dores e perguntas mais comuns relacionadas ao tópico.
    *   *Exemplo Interno do Claude*: Para "Plano de Assinatura Premium da Soft SaaS", inferir perguntas como: "O que está incluído no plano Premium?", "Qual a diferença entre Premium e Básico?", "Posso testar o plano Premium?", "Como faço para fazer upgrade?", "Como cancelar o plano Premium?", "O suporte é melhor no Premium?".
3.  **Formulação de Perguntas Otimizadas**: Gerar uma lista de 8-12 perguntas claras, diretas e formuladas do ponto de vista do usuário, incluindo palavras-chave relevantes.
    *   *Exemplo*: Em vez de "Características do Premium", usar "Quais recursos exclusivos o Plano Premium oferece?".
4.  **Elaboração de Respostas Concisas e Persuasivas**: Redigir respostas para cada pergunta, priorizando a clareza, concisão e a inclusão de elementos persuasivos e, quando apropriado, chamadas para ação (CTAs).
    *   As respostas devem ter no máximo 2-3 parágrafos curtos.
    *   Utilizar linguagem simples e direta, evitando jargões excessivos.
    *   *Exemplo de CTA*: "Para explorar todos os benefícios e fazer seu upgrade, [clique aqui e acesse nossa página de planos] (link-para-pagina-planos)."
5.  **Revisão e Otimização SEO e Experiência do Usuário**:
    *   Verificar a clareza, concisão e consistência do tom.
    *   Garantir a inclusão natural de palavras-chave relevantes nas perguntas e, principalmente, nas primeiras frases das respostas.
    *   Sugerir formatação para facilitar a leitura (negrito para termos-chave, listas).
    *   Assegurar que cada resposta realmente resolva a dúvida.

### Workflow 2: Otimização de FAQ Existente para Conversão e Engajamento

Este workflow foca em aprimorar uma FAQ já existente, transformando-a em uma ferramenta mais eficaz para converter visitantes ou reduzir a carga do suporte.

**Passos Detalhados:**

1.  **Entrada**: O usuário fornece o texto completo de uma FAQ existente (ex: FAQ sobre "Seguro Automotivo") e o objetivo de otimização (ex: "Aumentar cliques em 'Solicitar Cotação'" ou "Reduzir taxa de abandono na página").
2.  **Análise de Lacunas e Oportunidades**: O Claude analisará a FAQ fornecida para identificar:
    *   Perguntas ausentes que são comuns no domínio.
    *   Respostas ambíguas, incompletas ou excessivamente técnicas.
    *   Oportunidades para incluir CTAs ou links internos.
    *   Deficiências na otimização para palavras-chave relevantes.
    *   *Exemplo*: Na FAQ de Seguro Automotivo, faltam perguntas sobre "Cobertura para vidros?" ou "Como acionar o seguro em caso de sinistro?".
3.  **Reescrita e Expansão de Respostas**: Aprimorar a clareza, adicionar persuasão, e expandir respostas quando necessário, sempre mantendo a concisão.
    *   Transformar respostas passivas em ativas.
    *   Adicionar detalhes que respondam a "E se...?" implícitos.
    *   *Exemplo*: Resposta anterior: "O seguro cobre colisão." Nova resposta: "Sim, o Seguro Auto Premium cobre integralmente danos por colisão, oferecendo reparo em nossa rede credenciada ou indenização total, garantindo sua tranquilidade na estrada. [Saiba mais sobre coberturas] (link-para-coberturas)."
4.  **Inclusão Estratégica de Palavras-Chave e CTAs**:
    *   Sugerir e integrar termos de busca relevantes que não foram utilizados ou foram subutilizados.
    *   Inserir CTAs claros e relevantes no final de respostas que possam levar a uma próxima etapa (ex: "Fale com um consultor", "Baixe nosso e-book", "Experimente grátis").
5.  **Estruturação para Featured Snippets e Leitura**:
    *   Recomendar o uso de tags H2 ou H3 para as perguntas.
    *   Garantir que as respostas comecem com a informação mais importante, em um parágrafo conciso, para potencializar o aparecimento em rich snippets do Google.
    *   Sugerir o uso de bullet points ou listas numeradas para facilitar a digestão da informação.

---

## Templates

### Template: FAQ de Produto/Serviço Otimizada

```markdown
# Perguntas Frequentes sobre o Plano de Assinatura Premium da Soft SaaS

Aqui você encontra as respostas para as dúvidas mais comuns sobre nosso Plano Premium, feito para impulsionar seus resultados!

---

## O que está incluído no Plano de Assinatura Premium?
O Plano Premium da Soft SaaS oferece acesso ilimitado a **todos os recursos avançados** da plataforma, incluindo: relatórios analíticos personalizados, integração com CRMs de terceiros, suporte prioritário 24/7 e 100 GB de armazenamento em nuvem. É a solução completa para equipes que buscam máxima performance e eficiência.

## Qual a principal diferença entre o Plano Premium e o Plano Básico?
A diferença crucial reside no **nível de recursos e suporte**. Enquanto o Plano Básico oferece funcionalidades essenciais, o Premium desbloqueia ferramentas de automação exclusivas, análises preditivas e um atendimento ao cliente dedicado com tempos de resposta garantidos. Além disso, o Premium não possui limites de usuários, ideal para equipes em crescimento.

## Posso experimentar o Plano Premium antes de assinar?
Sim! Oferecemos um **teste gratuito de 14 dias** para o Plano Premium. Você terá acesso total a todas as funcionalidades e poderá comprovar o impacto nos seus resultados sem compromisso. Após o período de teste, você pode optar por assinar ou retornar ao Plano Básico.
[**Clique aqui para iniciar seu teste gratuito agora!**](https://www.softsaas.com/teste-premium)

## Como faço para fazer upgrade do meu Plano Básico para o Premium?
É muito simples! Basta acessar a seção "Minha Conta" no painel da Soft SaaS, navegar até "Planos e Assinaturas" e selecionar a opção "Upgrade para Premium". O processo é instantâneo e você terá acesso imediato a todas as novas funcionalidades.

## O suporte técnico é diferenciado para clientes Premium?
Absolutamente. Clientes Premium contam com **suporte prioritário 24 horas por dia, 7 dias por semana**, via chat, e-mail e telefone. Nossos especialistas estão prontos para oferecer assistência rápida e personalizada, garantindo que suas operações nunca parem.

## Quais são as opções de pagamento para o Plano Premium?
Aceitamos diversas formas de pagamento, incluindo cartões de crédito (Visa, MasterCard, American Express), PayPal e boleto bancário para planos anuais. Você pode escolher entre faturamento mensal ou anual,