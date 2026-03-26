---
name: micro-copy
description: "Micro Copy — Skill especializada em conteúdo & copywriting"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 01-conteudo-copy
  domain: conteúdo-copywriting
  updated: 2026-03-01
risk: safe
---

# Micro Copy

Esta skill capacita o Claude a criar textos concisos, eficazes e persuasivos para interfaces de usuário, focando em usabilidade e conversão em pontos de contato digitais.

---

## Keywords

UX Writing, UI Copy, Call-to-Action (CTA), Mensagens de Erro, Feedback, Onboarding, Empty States, Tooltips, Conteúdo Conciso, Persuasão Digital.

---

## Quick Start

1.  **Analise o Contexto da Interface**: Identifique a tela, o objetivo do usuário e o propósito da ação.
2.  **Defina o Tom de Voz**: Alinhe a micro copy com a persona da marca (ex: formal, amigável, direto).
3.  **Rascunhe Variações**: Crie pelo menos 3 opções diferentes para cada peça de micro copy.
4.  **Priorize Clareza e Concisão**: Elimine palavras desnecessárias e garanta que a mensagem seja instantaneamente compreendida.
5.  **Simule a Experiência do Usuário**: Leia a micro copy em voz alta, imaginando-se como o usuário interagindo com a interface.

---

## Core Workflows

### Workflow 1: Criação de Call-to-Action (CTA) de Alta Conversão

Este workflow guia o Claude na elaboração de CTAs que impulsionam a ação do usuário, otimizando taxas de clique e conversão.

**Passos Detalhados:**

1.  **Entendimento da Etapa do Funil**:
    *   **Ação do Claude**: Perguntar: "Em qual etapa do funil de vendas/jornada do usuário este CTA será inserido (ex: descoberta, consideração, decisão, retenção)?"
    *   **Exemplo**: Se for "decisão", o CTA deve ser mais direto e focado na finalização.
2.  **Identificação do Benefício Principal**:
    *   **Ação do Claude**: Analisar a funcionalidade ou oferta e extrair o maior benefício para o usuário.
    *   **Exemplo**: Em vez de "Comprar", pensar no benefício: "Receba seu produto em casa", "Economize agora".
3.  **Uso de Verbos de Ação Fortes e Específicos**:
    *   **Ação do Claude**: Selecionar um verbo que descreva claramente a ação e seja motivador. Evitar verbos passivos ou genéricos.
    *   **Exemplo**: Em vez de "Clique aqui", usar "Baixe o Ebook", "Comece Grátis", "Agende uma Demonstração".
4.  **Criação de Senso de Urgência ou Exclusividade (se aplicável)**:
    *   **Ação do Claude**: Inserir gatilhos mentais que incentivem a ação imediata, sem ser agressivo.
    *   **Exemplo**: "Últimas Vagas", "Por Tempo Limitado", "Acesso Exclusivo", "Só Hoje".
5.  **Teste de Clareza e Expectativa**:
    *   **Ação do Claude**: Avaliar se o CTA comunica claramente o que acontecerá após o clique e se a expectativa do usuário será atendida.
    *   **Exemplo**: Um CTA "Saiba Mais" pode ser vago demais; "Saiba Como Otimizar Sua Campanha" é mais claro.
6.  **Geração de Variações para Teste A/B**:
    *   **Ação do Claude**: Criar pelo menos 3 versões diferentes do CTA, alterando verbos, benefícios ou gatilhos, para permitir otimização contínua.
    *   **Exemplo**:
        *   V1: "Garanta Sua Vaga Agora!"
        *   V2: "Inscreva-se e Aprenda!"
        *   V3: "Comece Sua Jornada de Aprendizado Hoje!"

### Workflow 2: Redação de Mensagens de Erro e Sucesso Empáticas

Este workflow orienta o Claude na criação de micro copy para feedback do sistema, garantindo clareza, utilidade e um tom de voz que fortaleça a relação com o usuário.

**Passos Detalhados:**

1.  **Identificação do Tipo de Feedback**:
    *   **Ação do Claude**: Determinar se a mensagem é de erro, sucesso, aviso ou informação.
    *   **Exemplo**: Erro de validação de formulário, sucesso de envio, aviso de sessão expirada.
2.  **Clareza na Explicação do Problema ou Sucesso**:
    *   **Ação do Claude**: Descrever o ocorrido de forma direta, sem jargões técnicos ou termos ambíguos.
    *   **Exemplo**: Em vez de "Erro 404", usar "Página não encontrada". Em vez de "Processado", usar "Seu pedido foi recebido!".
3.  **Orientação para o Próximo Passo (para erros e avisos)**:
    *   **Ação do Claude**: Oferecer uma solução clara ou uma ação que o usuário pode tomar para resolver o problema ou prosseguir.
    *   **Exemplo**: Para um erro de senha, "Verifique sua senha e tente novamente" ou "Esqueceu sua senha?".
4.  **Reforço Positivo (para sucessos)**:
    *   **Ação do Claude**: Celebrar a conclusão da ação e, se possível, indicar o que o usuário pode esperar em seguida.
    *   **Exemplo**: "Cadastro realizado com sucesso! Verifique seu e-mail para ativar sua conta."
5.  **Manutenção do Tom de Voz da Marca**:
    *   **Ação do Claude**: Assegurar que a mensagem esteja alinhada com a personalidade da marca, seja ela mais formal, amigável ou neutra.
    *   **Exemplo**: Uma fintech pode usar um tom mais direto, enquanto um aplicativo de meditação pode ser mais acolhedor.
6.  **Conciseness e Visibilidade**:
    *   **Ação do Claude**: Escrever a mensagem para ser breve, de fácil leitura e que se destaque na interface sem ser intrusiva.
    *   **Exemplo**: Evitar blocos de texto longos; usar frases curtas e diretas.

---

## Templates

### Template: CTA Otimizado

```
[Verbo de Ação Forte] [Benefício ou Resultado Claro] [Gatilho de Urgência/Exclusividade - Opcional]

Exemplo 1 (E-commerce):
COMPRE AGORA e Garanta 30% OFF em Toda a Coleção!

Exemplo 2 (Serviço SaaS):
EXPERIMENTE GRÁTIS por 7 Dias e Transforme Sua Gestão!

Exemplo 3 (Evento/Webinar):
INSCREVA-SE JÁ e Reserve Sua Vaga para o Workshop Exclusivo!
```

### Template: Mensagem de Erro Construtiva

```
Ops, [O que deu errado de forma clara]. Por favor, [O que fazer para corrigir] ou [Alternativa/Próximo passo].

Exemplo 1 (Login):
Ops, seu e-mail ou senha estão incorretos. Por favor, verifique suas credenciais e tente novamente ou clique em "Esqueci minha senha".

Exemplo 2 (Formulário):
Ops, o campo "Telefone" precisa ser preenchido com 11 dígitos. Por favor, revise e tente novamente.

Exemplo 3 (Servidor):
Ops, algo deu errado com nossos servidores. Por favor, tente novamente em alguns instantes. Se o problema persistir, entre em contato com o suporte.
```

### Template: Mensagem de Sucesso Clara

```
[Confirmação da Ação] com sucesso! [Próximo passo ou o que esperar].

Exemplo 1 (Cadastro):
Cadastro realizado com sucesso! Um e-mail de confirmação foi enviado para você.

Exemplo 2 (Compra):
Sua compra foi aprovada! Você receberá os detalhes do pedido em seu e-mail.

Exemplo 3 (Envio de Mensagem):
Sua mensagem foi enviada! Responderemos em breve.
```

---

## Checklist

- [X] A micro copy é clara e fácil de entender?
- [X] Está concisa, sem palavras desnecessárias?
- [X] O tom de voz está alinhado com a marca?
- [X] O CTA é explícito e direciona para uma ação clara?
- [X] Mensagens de erro oferecem uma solução ou próximo passo?
- [X] Mensagens de sucesso confirmam a ação e indicam o que esperar?
- [X] Não há jargões técnicos ou ambíguos?
- [X] A micro copy é acessível e otimizada para diferentes dispositivos (mobile first)?
- [X] Há consistência na terminologia e no estilo em toda a interface?
- [X] A micro copy evita acusações ou culpar o usuário em caso de erro?

---

## Métricas de Referência

| Métrica                         | Valor Bom     | Valor Excelente |
|---------------------------------|---------------|-----------------|
| Taxa de Cliques (CTR) em CTAs   | 2% - 5%       | > 5%            |
| Taxa de Conclusão de Formulário | 50% - 70%     | > 70%           |
| Taxa de Rejeição (páginas chave)| < 40%         | < 20%           |
| Taxa de Abertura de Notificação | 15% - 25%     | > 25%           |
| Taxa de Engajamento em Onboarding | 60% - 80%     | > 80%           |

*Nota: Estes valores são referências e podem variar significativamente por setor, tipo de produto/serviço e público-alvo. O ideal é comparar com benchmarks do seu próprio segmento e histórico.*

---

## Erros Comuns

1.  **Jargões Técnicos ou Corporativos**: O usuário não entende termos internos da empresa ou linguagem de programador.
    *   **Como evitar**: Use linguagem simples, acessível e focada no usuário. Teste a compreensão com pessoas leigas.
2.  **CTAs Ambíguos ou Vagos**: "Clique aqui", "Saiba mais" não informam o que acontecerá após a ação.
    *   **Como evitar**: Seja específico sobre o resultado da ação. Ex: "Baixe o Relatório Completo", "Agende Sua Consulta Grátis".
3.  **Mensagens de Erro Acusatórias**: "Você digitou errado" ou "Sua senha é inválida" culpam o usuário.
    *   **Como evitar**: Adote um tom empático e neutro. Foque na solução. Ex: "A senha inserida não corresponde. Tente novamente."
4.  **Falta de Consistência**: Usar diferentes termos para a mesma ação ou objeto em telas distintas.
    *   **Como evitar**: Crie um glossário de termos chave e um guia de estilo de voz e tom para toda a micro copy.
5.  **Excesso de Informação**: Textos longos em espaços curtos, sobrecarregando o usuário.
    *   **Como evitar**: Seja conciso. Priorize a informação essencial. Use ferramentas como o "teste de 5 segundos" para garantir a clareza imediata.

---

## Dicas Avançadas

1.  **Micro Copy Contextualizada por Persona**: Crie variações de micro copy para diferentes segmentos de usuários ou personas, adaptando o tom e a linguagem para ressoar melhor com cada grupo específico, aumentando a relevância e o engajamento.
2.  **Otimização para Acessibilidade**: Utilize micro copy que seja clara para leitores de tela e usuários com deficiências cognitivas, evitando sarcasmo, gírias excessivas e fornecendo descrições alt text significativas para ícones e imagens.
3.  **Testes de Usabilidade com Protótipos de Baixa Fidelidade**: Integre a micro copy desde as fases iniciais do design, testando-a com usuários em protótipos simples (wireframes) para identificar falhas de comunicação antes do desenvolvimento completo.
4.  **Aproveitar Micro Interações**: Use a micro copy em conjunto com animações sutis e feedback tátil para criar uma experiência mais rica e intuitiva, como um breve texto de "Carregando..." que muda para "Pronto!" com uma animação de sucesso.
5.  **Análise de Dados Comportamentais**: Monitore não apenas as taxas de conversão, mas também o comportamento do usuário (mapas de calor, gravações de sessão) em áreas com micro copy para entender como o texto influencia a navegação e a tomada de decisão, ajustando com base em dados qualitativos.
---