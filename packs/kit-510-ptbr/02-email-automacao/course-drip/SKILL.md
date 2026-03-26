---
name: course-drip
description: "Course Drip — Skill especializada para course drip"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Course Drip

Esta skill capacita o Claude a projetar, implementar e otimizar sequências de email automatizadas para engajar, educar e converter alunos em funis de cursos online, desde a pré-inscrição até a pós-compra.

---

## Keywords

*   Email Drip Course
*   Automação de Marketing Educacional
*   Sequência de Boas-Vindas Aluno
*   Funil de Vendas de Cursos EAD
*   Engajamento Pós-Compra EAD
*   Nutrição de Leads Educacionais
*   Segmentação de Alunos Online
*   Recuperação de Carrinho Curso
*   Relacionamento com Aluno EAD
*   Lançamento de Curso por Email
*   Retenção de Alunos EAD
*   Jornada do Aluno Digital

---

## Quick Start

1.  **Mapear a Jornada do Aluno**: Desenhe o caminho completo do lead, desde o primeiro contato (ex: download de e-book gratuito) até a conclusão do curso e potenciais upsells.
2.  **Definir Gatilhos e Ações**: Determine os eventos específicos que dispararão cada email (ex: inscrição na landing page, compra efetuada, 7 dias de inatividade no curso, conclusão de módulo).
3.  **Estruturar Sequências de Email**: Crie um fluxo lógico de mensagens, definindo o objetivo de cada email, seu conteúdo, frequência de envio e o CTA principal.
4.  **Configurar Plataforma**: Implemente as automações na ferramenta de email marketing (ex: ActiveCampaign, Mailchimp, Leadlovers) e integre-a com a plataforma de cursos (ex: Hotmart, Kiwify, Eduzz).
5.  **Testar o Fluxo Completo**: Simule a jornada de um aluno de teste para garantir que todos os emails são entregues corretamente, os links funcionam e os gatilhos estão ativos.

---

## Core Workflows

### Workflow 1: Sequência de Boas-Vindas para Novo Lead (Pré-Inscrição)

**Objetivo**: Aquecer leads que demonstraram interesse inicial, apresentando o valor do seu método/curso e construindo autoridade antes da oferta principal.
**Gatilho**: Inscrição em landing page para download de isca digital (ex: e-book gratuito "Os 5 Passos para Aprender Python", acesso a webinar "Desvendando o Marketing Digital").

*   **Dia 0 - Email 1: Boas-vindas e Entrega do Recurso**
    *   **Assunto**: "Seu E-book '5 Passos para Python' está aqui! Bem-vindo(a) à Escola DevPro"
    *   **Corpo**: Agradecer a inscrição, entregar o link para o recurso prometido. Introduzir brevemente a Escola DevPro e o problema que o e-book começa a resolver (ex: "Entendemos a dificuldade de começar a programar e nosso e-book é o primeiro passo para descomplicar isso.").
    *   **CTA**: "Baixar E-book Agora", "Assistir ao Webinar".

*   **Dia 2 - Email 2: O Problema, a Solução e a Conexão Pessoal**
    *   **Assunto**: "Você também se sente travado ao programar? Minha história com Python pode te inspirar!"
    *   **Corpo**: Contar uma história pessoal ou de um aluno que enfrentou o problema que o e-book aborda e como encontrou a solução. Conectar a história com a metodologia da Escola DevPro.
    *   **CTA**: "Conheça mais sobre nossa metodologia", "Leia outros depoimentos".

*   **Dia 4 - Email 3: Prova Social e Próximo Passo de Valor**
    *   **Assunto**: "Veja como o João aprendeu Python em 30 dias com a DevPro e você também pode!"
    *   **Corpo**: Apresentar um depoimento detalhado ou um mini-case de sucesso de um aluno. Convidar o lead para um conteúdo mais aprofundado e gratuito (ex: uma mini-aula no YouTube, um convite para um grupo exclusivo).
    *   **CTA**: "Assista à mini-aula gratuita de Python", "Entre para nosso grupo de estudos".

### Workflow 2: Reengajamento de Aluno Inativo no Curso

**Objetivo**: Estimular alunos que pararam de acessar o curso a retomar o aprendizado, prevenindo a evasão e aumentando a taxa de conclusão.
**Gatilho**: Aluno não acessa a área de membros do curso "[Nome do Curso]" por 7 dias, estando com menos de 75% de progresso.

*   **Dia 0 (7 dias de inatividade) - Email 1: Lembrete Amigável e Apoio**
    *   **Assunto**: "Sentimos sua falta! Que tal retomar o curso [Nome do Curso]?"
    *   **Corpo**: Mensagem empática, reconhecendo a pausa. Lembrar o aluno do último módulo ou aula que ele acessou (ex: "Percebemos que você parou no Módulo 3: Fundamentos da Análise de Dados."). Reforçar os benefícios de concluir o curso.
    *   **CTA**: "Retomar de onde parou", "Acessar o Curso Agora".

*   **Dia 3 (10 dias de inatividade) - Email 2: Superando Barreiras e Conteúdo Chave**
    *   **Assunto**: "Dica rápida para superar o desafio de [Tópico do Módulo Anterior] em [Nome do Curso]"
    *   **Corpo**: Abordar uma possível dificuldade comum no módulo onde o aluno parou. Oferecer uma dica prática, um vídeo complementar curto ou um trecho relevante do material. Perguntar se o aluno precisa de ajuda.
    *   **CTA**: "Revisar o Módulo [Número do Módulo]", "Precisa de ajuda? Fale conosco!".

*   **Dia 6 (13 dias de inatividade) - Email 3: Incentivo e Benefício Final**
    *   **Assunto**: "Não perca a transformação: O que você ganha ao concluir o [Nome do Curso]!"
    *   **Corpo**: Focar nos resultados e benefícios de longo prazo da conclusão do curso (ex: "Imagine dominar a análise de dados e impulsionar sua carreira!"). Mencionar a comunidade, o suporte ou o certificado de conclusão. Criar um senso de urgência ou oportunidade.
    *   **CTA**: "Concluir sua Jornada de Aprendizado", "Acesse a Área de Membros".

---

## Templates

### Email de Boas-Vindas Pós-Compra e Acesso Imediato

```
Assunto: Bem-vindo(a) à sua jornada em [Nome do Curso]! Seu acesso está aqui!

Olá [Nome do Aluno],

Parabéns por dar o primeiro passo e se matricular no curso "[Nome do Curso]"! Estamos muito animados em ter você conosco e ver sua transformação em [Benefício principal do curso, ex: "um expert em marketing digital"].

Para começar sua jornada de aprendizado AGORA, acesse sua área de membros exclusiva clicando no link abaixo:

[Link para Área de Membros]
Seu login é: [Email do Aluno]
Sua senha inicial é: [Senha Gerada/Instrução para Criar Senha]

Recomendamos fortemente que você comece pelo Módulo 0: Boas-Vindas e Orientações. Lá, explicamos como aproveitar ao máximo o curso, nossa comunidade de alunos no Telegram e o suporte disponível.

Se tiver qualquer dúvida, dificuldade ou precisar de suporte técnico, nossa equipe está pronta para ajudar. Responda a este email ou entre em contato via WhatsApp: [Número de WhatsApp da Escola].

Desejamos a você um excelente aprendizado e mal podemos esperar para ver seus resultados!

Com carinho,
Equipe [Nome da Escola/Professor]
[Link para Site da Escola]
[Link para Redes Sociais]
```

### Email de Recuperação de Carrinho - Última Chance com Bônus

```
Assunto: [ÚLTIMA CHANCE]: Seu BÔNUS especial para [Nome do Curso] expira hoje!

Olá [Nome do Aluno],

Percebemos que você iniciou sua matrícula no curso "[Nome do Curso]", mas ainda não finalizou. Queríamos te dar uma última chance de aproveitar a oferta e garantir seu acesso!

Além de todo o conteúdo incrível de [Mencionar 2-3 benefícios do curso, ex: "dominar as estratégias de tráfego pago e criar campanhas que realmente convertem"], reservamos um BÔNUS EXCLUSIVO para você que está nessa lista:

🎁 Acesso GRATUITO ao [Nome do Bônus, ex: "Workshop Intensivo de Otimização de Anúncios"] - Valor de R$197!

Este bônus, que complementa perfeitamente o curso principal, estará disponível APENAS até a meia-noite de hoje, [Data]. Não perca a oportunidade de acelerar seus resultados!

Clique no link abaixo para finalizar sua matrícula e garantir seu bônus agora:

[Link Direto para o Carrinho de Compras]

Se tiver qualquer dúvida sobre o curso ou precisar de ajuda para finalizar a compra, nossa equipe está online para te ajudar: [Link para Chat/WhatsApp de Suporte].

Não deixe essa oportunidade de transformação escapar!

Um abraço,
[Nome do Professor/Fundador]
[Nome da Escola]
```

---

## Checklist

- [x] Mapear todas as etapas da jornada do aluno (pré-venda, venda, pós-venda, inatividade).
- [x] Definir gatilhos claros para cada automação (ex: inscrição na LP, compra, 7 dias de inatividade, conclusão de módulo).
- [x] Escrever subject lines que geram curiosidade e taxas de abertura acima da média (ex: "Seu acesso ao curso [X] está aqui!").
- [x] Criar conteúdo relevante e de valor para cada etapa do funil (educativo, inspiracional, de vendas, suporte, celebração).
- [x] Incluir CTAs claros e únicos em cada email (ex: "Acessar Módulo X", "Comprar Agora", "Fale com Suporte", "Baixar Certificado").
- [x] Personalizar emails com nome do aluno, nome do curso e progresso sempre que possível para maior engajamento.
- [x] Configurar testes A/B para subject lines, CTAs e horários de envio para otimizar desempenho.
- [x] Definir a frequência e o espaçamento ideal entre os emails para evitar sobrecarga ou esquecimento.
- [x] Integrar a plataforma de email marketing com a plataforma de cursos para sincronização de dados.
- [x] Configurar tags ou segmentações baseadas no comportamento do aluno (ex: "aluno ativo", "aluno inativo", "comprou curso X", "interessado em Y").
- [x] Implementar uma sequência de follow-up para alunos que finalizaram o curso, oferecendo próximos passos ou depoimentos.
- [x] Incluir links para a política de privacidade e opção de descadastro em todos os emails.

---

## Métricas de Referência

| Métrica               | Benchmark (Educação Online) | Meta (Excelência) |
|-----------------------|-----------------------------|-------------------|
| Taxa de Abertura      | 25-30%                      | 35%+              |
| Taxa de Cliques (CTR) | 2-4%                        | 5%+               |
| Taxa de Conversão     | 1-3% (venda)                | 4%+ (venda)       |
| Taxa de Descadastro   | < 0.2%                      | < 0.1%            |
| Taxa de Conclusão     | 10-20% (curso pago)         | 30%+ (curso pago) |
| Receita por Email     | R$ 0.10 - R$ 0.30           | R$ 0.40+          |

---

## Erros Comuns

1.  **Emails genéricos sem personalização**: Enviar mensagens que não usam o nome do aluno, o nome do curso específico ou que não se referem ao seu progresso individual, diminuindo drasticamente o engajamento.
    *   **Como evitar**: Utilize campos dinâmicos (`{{nome_aluno}}`, `{{nome_curso}}`, `{{modulo_parado}}`) da sua plataforma de email marketing. Integre-a com a plataforma de cursos para puxar esses dados e criar mensagens altamente relevantes.
2.  **Frequência inadequada de envio**: Bombardear leads com emails diários logo após o primeiro contato (spam) ou deixar grandes lacunas entre as mensagens, resultando em perda de interesse e esquecimento do curso.
    *   **Como evitar**: Planeje a cadência da sequência de forma estratégica. Para nutrição, um espaçamento de 2-3 dias é comum. Para recuperação de carrinho, a frequência pode ser maior (4h, 24h, 48h). Monitore as taxas de abertura e descadastro para ajustar.
3.  **Falta de um CTA claro e único**: O email apresenta múltiplos links ou nenhuma instrução clara sobre o que o aluno deve fazer em seguida, gerando confusão e baixa taxa de cliques.
    *   **Como evitar**: Cada email deve ter um objetivo principal e um CTA proeminente (botão ou link em destaque) que guie o aluno para a próxima ação desejada (ex: "Acessar o Módulo 5", "Finalizar Minha Matrícula", "Agendar Suporte").

---

## Dicas Avançadas

1.  **Micro-segmentação por progresso e comportamento**: Crie automações ultra-específicas para alunos que atingiram marcos (ex: 25%, 50%, 75% de conclusão) ou demonstraram comportamentos específicos (ex: assistiram a todas as aulas de um módulo mas não fizeram o quiz).
    *   **Exemplo**: Aluno que concluiu 75% do "Curso de Edição de Vídeos Profissional" recebe um email com um convite exclusivo para um workshop ao vivo de "Edição Avançada com DaVinci Resolve", ativando um upsell inteligente.
2.  **Utilização de Webhooks para gatilhos complexos**: Aproveite webhooks para disparar automações baseadas em eventos que não são nativamente integrados, como a participação em uma aula ao vivo específica na plataforma de webinar, o download de um material complementar de um link externo ou a submissão de um projeto.
    *   **Exemplo**: Um webhook da ferramenta de gestão de projetos (ex: Trello) envia um sinal para o ActiveCampaign quando um aluno marca seu projeto final como "concluído", disparando uma sequência de celebração e pedido de depoimento.
3.  **Sequências de "upsell" e "cross-sell" baseadas em perfil**: Após a conclusão de um curso, analise o perfil do aluno e o conteúdo consumido para oferecer cursos mais avançados (upsell) ou complementares (cross-sell) que maximizem o valor percebido e a jornada de aprendizado.
    *   **Exemplo**: Aluno que finalizou "Introdução à Programação Front-End" recebe uma sequência de 4 emails promovendo "Desenvolvimento Back-End com Node.js" (cross-sell) ou "Frameworks Front-End Avançados: React e Vue" (upsell), com um desconto de fidelidade.
4.  **Testes A/B/n e Otimização com IA para Personalização Preditiva**: Vá além dos testes A/B simples. Utilize ferramentas que empregam Machine Learning para otimizar automaticamente as entregas e o conteúdo dos emails, aprendendo qual mensagem, assunto ou horário de envio funciona melhor para diferentes segmentos de alunos.
    *   **Exemplo**: O sistema de automação identifica que alunos da faixa etária 20-25 anos, interessados em design, engajam mais com emails enviados às quintas-feiras às 14h com subject lines que prometem "novas tendências", enquanto alunos 30-40 anos preferem emails às terças-feiras às 9h com foco em "produtividade e carreira".