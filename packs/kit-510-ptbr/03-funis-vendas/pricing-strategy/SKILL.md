---
name: pricing-strategy
description: "Pricing Strategy — Skill especializada para pricing strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 03-funis-vendas
  updated: 2026-03-01
risk: safe
---

# Pricing Strategy

Esta skill equipa o Claude com a capacidade de analisar, formular e otimizar estratégias de precificação para produtos e serviços, visando maximizar receita e lucratividade em funis de vendas.

---

## Keywords

Precificação Dinâmica, Valor Percebido, Custo de Aquisição (CAC), Lifetime Value (LTV), Elasticidade de Preço, Modelos de Assinatura, Freemium, Preço Psicológico, Estratégias de Skimming, Penetração de Mercado, Bundling, Descontos Progressivos, Análise de Ponto de Equilíbrio, Margem de Contribuição.

---

## Quick Start

1.  **Calcule o Custo Total de Propriedade (TCO)** para um produto digital específico, como o "Curso Online de Marketing Digital Avançado", incluindo custos de hospedagem, plataforma, licenças de ferramentas e horas de produção.
2.  **Identifique 3-5 concorrentes diretos** para o "Curso Online de Marketing Digital Avançado" e anote seus preços, formatos de curso e diferenciais.
3.  **Simule três cenários de preço** (ex: R$ 497, R$ 697, R$ 897) para o curso, projetando a receita bruta e a margem de contribuição com uma estimativa de 50 vendas para cada cenário.
4.  **Elabore uma matriz de valor percebido** para o curso, listando os módulos, bônus e suporte, e como cada item agrega valor superior ao dos concorrentes.

---

## Core Workflows

### Workflow 1: Análise de Valor e Posicionamento de Preço para Novo Produto SaaS

Este workflow detalha o processo de definir a precificação ideal para um novo produto SaaS, focando na proposta de valor e no posicionamento de mercado.

1.  **Mapeamento de Custos Diretos e Indiretos**:
    *   **Ação**: Listar todos os custos envolvidos na criação, manutenção e entrega do produto SaaS.
    *   **Exemplo Prático**: Para o "CRM Inteligente para Pequenas Empresas", considere:
        *   **Custos Diretos (Variáveis)**: Taxas de transação de pagamento (2.5% sobre a receita), custo de processamento de dados por usuário (R$ 0,50/GB/mês), custo de suporte por ticket (R$ 5/ticket, estimado 0.1 ticket/usuário/mês).
        *   **Custos Indiretos (Fixos)**: Servidores AWS (R$ 1.500/mês), licenças de software de terceiros (R$ 800/mês), salários da equipe de desenvolvimento e manutenção (R$ 15.000/mês), marketing (R$ 3.000/mês).
    *   **Cálculo**: `Custo Total Fixo = R$ 1.500 + R$ 800 + R$ 15.000 + R$ 3.000 = R$ 20.300/mês`.
    *   `Custo Variável por Usuário (excluindo tx. de pagamento) = R$ 0,50 (dados) + R$ 0,50 (suporte) = R$ 1,00/usuário/mês`.

2.  **Análise de Concorrentes e Preços de Referência**:
    *   **Ação**: Pesquisar e documentar os modelos de precificação, planos e funcionalidades de pelo menos 3-5 concorrentes diretos e indiretos.
    *   **Exemplo Prático**:
        *   **Concorrente A ("SalesFlow")**: Plano Básico R$ 79/mês (até 5 usuários, 1000 contatos), Plano Pro R$ 149/mês (ilimitado, automação).
        *   **Concorrente B ("LeadManager")**: Plano Starter R$ 59/mês (1 usuário, 500 contatos), Plano Business R$ 119/mês (3 usuários, 5000 contatos).
        *   **Nosso "CRM Inteligente"**: Diferencial de IA para qualificação de leads e automação de follow-up, ausente nos concorrentes na mesma faixa de preço.

3.  **Construção da Proposta de Valor e Diferenciação**:
    *   **Ação**: Articular claramente os benefícios únicos do produto e como eles resolvem problemas específicos do público-alvo, justificando um determinado preço.
    *   **Exemplo Prático**: "O CRM Inteligente não é apenas um CRM; ele atua como um assistente de vendas autônomo. Sua IA qualifica leads em tempo real, automatiza e-mails de follow-up personalizados e sugere os próximos passos, economizando até 10 horas/semana por vendedor e aumentando a taxa de conversão em 15%."

4.  **Definição da Estratégia de Precificação Inicial**:
    *   **Ação**: Escolher uma abordagem estratégica (e.g., precificação de penetração, skimming, valor) com base nos custos, concorrência e proposta de valor.
    *   **Exemplo Prático**: Adotar uma estratégia de **precificação baseada em valor** com um toque de **skimming** para o plano mais robusto, aproveitando o diferencial da IA.
        *   **Plano Básico ("Essencial")**: R$ 89/mês (até 3 usuários, 2.000 contatos, CRM básico). Posicionamento competitivo.
        *   **Plano Pro ("Inteligente")**: R$ 179/mês (até 10 usuários, 10.000 contatos, CRM completo + IA de qualificação + automação avançada). Foco no valor entregue pela IA e funcionalidades premium.

5.  **Simulação de Receita e Ponto de Equilíbrio**:
    *   **Ação**: Projetar a quantidade de clientes necessária para cobrir os custos e começar a gerar lucro.
    *   **Exemplo Prático**:
        *   **Ponto de Equilíbrio (PE)**: `Custos Fixos / (Receita Média por Cliente - Custo Variável por Cliente)`.
        *   Se esperarmos 70% de clientes no Plano Essencial e 30% no Plano Inteligente:
            *   `ARPU (Receita Média por Usuário) = (0.7 * R$ 89) + (0.3 * R$ 179) = R$ 62,30 + R$ 53,70 = R$ 116,00`.
            *   `Custo Variável por Usuário = R$ 1,00 (dados/suporte) + (ARPU * 0.025 - taxa de pagamento) = R$ 1,00 + R$ 2,90 (2.5% de 116) = R$ 3,90`.
            *   `Margem de Contribuição por Usuário = R$ 116,00 - R$ 3,90 = R$ 112,10`.
            *   `PE em Usuários = R$ 20.300 / R$ 112,10 ≈ 181 usuários`.
        *   **Conclusão**: Precisamos de aproximadamente 181 usuários pagantes para cobrir todos os custos fixos e variáveis.

### Workflow 2: Otimização de Precificação para Funil de Vendas Existente (A/B Testing)

Este workflow foca em como testar e otimizar preços para produtos ou serviços já existentes, utilizando dados de conversão do funil de vendas.

1.  **Identificação de Pontos de Fricção e Perda no Funil**:
    *   **Ação**: Analisar as métricas do funil para identificar onde os usuários estão desistindo, especialmente na etapa de precificação.
    *   **Exemplo Prático**: Para um e-commerce de cursos:
        *   `Taxa de Visitas na Página de Preços -> Início do Checkout: 25%`.
        *   `Taxa de Início do Checkout -> Compra Concluída: 40%`.
        *   **Problema**: Uma queda significativa entre a página de preços e o início do checkout, sugerindo que o preço pode ser um obstáculo inicial.

2.  **Geração de Hipóteses de Precificação para Teste A/B**:
    *   **Ação**: Formular diferentes variações de preço, bundling ou apresentação para testar.
    *   **Exemplo Prático**:
        *   **Hipótese A (Preço Mais Baixo)**: Reduzir o preço do "Curso de Lançamento de Produtos Digitais" de R$ 997 para R$ 797.
        *   **Hipótese B (Bundling de Valor)**: Manter o preço de R$ 997, mas adicionar um bônus exclusivo (e.g., "Template de Landing Page de Alta Conversão" + "Sessão de Mentoria em Grupo") avaliado em R$ 400.
        *   **Hipótese C (Parcelamento Estendido)**: Manter R$ 997, mas oferecer 12x sem juros (antes era 6x).

3.  **Configuração do Teste A/B no Funil**:
    *   **Ação**: Implementar as variantes usando ferramentas de A/B testing (e.g., Google Optimize, VWO, Unbounce) na página de vendas ou checkout.
    *   **Exemplo Prático**:
        *   Dividir o tráfego da Landing Page do curso em 3 grupos iguais (33% cada).
        *   Grupo 1: Página de vendas com preço R$ 797 (Hipótese A).
        *   Grupo 2: Página de vendas com preço R$ 997 + bônus (Hipótese B).
        *   Grupo 3: Página de vendas com preço R$ 997 e opção de 12x sem juros (Hipótese C).
        *   **Duração do Teste**: Mínimo de 2-4 semanas ou até atingir significância estatística.

4.  **Monitoramento e Análise de Resultados**:
    *   **Ação**: Coletar e analisar métricas chave como taxa de conversão (visita -> compra), ARPU (Average Revenue Per User), LTV (Lifetime Value) e margem de lucro.
    *   **Exemplo Prático**: Após 3 semanas:
        *   **Hipótese A (R$ 797)**: Taxa de conversão subiu para 3,8% (antes 2,5%), mas o ARPU caiu 20%. Margem de lucro total estável devido ao volume.
        *   **Hipótese B (R$ 997 + Bônus)**: Taxa de conversão subiu para 3,2%, ARPU manteve-se, LTV projetado aumentou ligeiramente devido à percepção de valor.
        *   **Hipótese C (R$ 997, 12x)**: Taxa de conversão subiu para 3,0%, ARPU estável, LTV estável.
        *   **Conclusão Parcial**: A Hipótese B parece oferecer o melhor equilíbrio entre conversão e manutenção do ARPU/LTV.

5.  **Iteração e Implementação**:
    *   **Ação**: Decidir qual variante implementar ou se novos testes são necessários, com base nos dados.
    *   **Exemplo Prático**: Implementar a **Hipótese B (R$ 997 com bônus)** como padrão, pois aumentou a conversão de forma sustentável sem sacrificar o ARPU, e ainda fortaleceu a percepção de valor do produto, contribuindo para o LTV. Planejar um novo teste focado em novos bônus para otimização futura.

---

## Templates

### Matriz de Valor Percebido (Produto SaaS "GerenciadorPro")

```
# Matriz de Valor Percebido - GerenciadorPro Plano Premium

**Produto/Serviço:** GerenciadorPro - Plano Premium (SaaS)
**Público-Alvo:** Pequenas e Médias Empresas (PMEs) com equipe de vendas.
**Concorrente Principal:** "SalesFlow Business"

| Funcionalidade/Benefício             | Valor para o Cliente (Percebido)                                            | Diferencial do GerenciadorPro                                               | Preço do Concorrente (SalesFlow Business) | Preço Sugerido GerenciadorPro |
|--------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------|-------------------------------|
| Automação de follow-up (e-mail, WhatsApp) | Economia de tempo da equipe de vendas, maior taxa de resposta               | IA integrada para sugestão de mensagens personalizadas                     | Incluído no plano de R$129/mês            | R$149/mês                     |
| CRM Integrado (gestão de leads)      | Centralização de dados, visão 360 do cliente                               | Interface intuitiva, relatórios customizáveis por arrastar e soltar         | R$99/mês (básico)                         | R$149/mês                     |
| Relatórios de Performance de Vendas  | Tomada de decisão baseada em dados, identificação de gargalos               | Dashboards preditivos com machine learning para previsão de vendas          | R$129/mês (avançado)                      | R$149/mês                     |
| Suporte 24/7 (chat e telefone)       | Resolução rápida de problemas, minimiza interrupções operacionais           | Suporte prioritário com SLA de 30 minutos para chamados críticos            | Apenas por e-mail no plano básico         | R$149/mês                     |
| Integração com ERP (SAP, Bling)      | Redução de erros manuais, fluxo de trabalho otimizado                       | Conectores nativos para os 5 principais ERPs do mercado brasileiro         | Integração via API (requer dev)           | R$149/mês                     |

**Justificativa do Preço Sugerido (R$149/mês):**
O GerenciadorPro oferece funcionalidades de automação com IA e relatórios preditivos, que o SalesFlow Business não possui ou oferece de forma mais complexa. Além disso, a facilidade de uso e o suporte prioritário justificam um preço ligeiramente superior, posicionando-lo como uma solução premium para PMEs que buscam eficiência e inovação. O bundling de funcionalidades essenciais por um preço fixo oferece um valor percebido alto.
```

### Script de Precificação para Ligação de Vendas (Objeção: "Preço Alto")

```
# Script de Precificação - Ligação de Vendas (Objeção: "Preço Alto")

**Contexto:** Cliente potencial expressa que o "Plano Avançado" do nosso SaaS (R$199/mês) é caro.

**Vendedor:** Olá [Nome do Cliente], entendo perfeitamente sua preocupação com o investimento. O valor de R$199/mês para o Plano Avançado pode parecer alto à primeira vista, mas permita-me detalhar o que ele realmente entrega e como isso se traduz em retorno financeiro para sua empresa.

**Cliente:** É muito mais do que esperávamos. Vi outras soluções por R$120-R$150.

**Vendedor:** Excelente ponto, [Nome do Cliente]. Existem muitas opções no mercado. A diferença fundamental do nosso Plano Avançado é que ele inclui [Mencionar funcionalidade PRINCIPAL e EXCLUSIVA] e [Mencionar BENEFÍCIO RESULTANTE]. Por exemplo, a funcionalidade de "Otimização de Campanhas por IA" que você não encontra nas soluções de R$120-R$150, gera em média um aumento de 20% na taxa de conversão de leads e uma redução de 15% no Custo Por Lead (CPL) para nossos clientes.

**Vendedor:** Se você considerar que um aumento de 20% na conversão de leads pode significar [X] vendas adicionais por mês, e que economizar 15% no CPL pode representar [Y] reais de economia em seu orçamento de marketing, o investimento extra de R$49-R$79/mês se paga rapidamente, não acha?

**Vendedor:** Além disso, o suporte prioritário 24/7 incluso garante que sua equipe nunca ficará parada, resolvendo qualquer questão em menos de 30 minutos. Quanto custaria para sua empresa ter a equipe parada por horas esperando uma solução?

**Vendedor:** Podemos até simular um ROI rápido com base nos seus números atuais de leads e vendas. Qual o seu CPL médio e sua taxa de conversão atual? Assim, podemos ver juntos o impacto direto do nosso Plano Avançado no seu resultado final.

**Vendedor:** Se o foco é realmente no preço, podemos explorar o Plano Básico de R$99/mês, mas ele não inclui [funcionalidades chave do Plano Avançado]. Minha sugestão é que, para atingir seus objetivos de [mencionar objetivo do cliente], o Plano Avançado é o que trará o maior e mais rápido retorno. O que você acha de vermos essa simulação agora mesmo?
```

---

## Checklist

- [x] Calculei o LTV (Lifetime Value) médio dos meus clientes por segmento.
- [x] Analisei a elasticidade-preço da demanda para meus produtos carro-chefe.
- [x] Mapeei todos os custos diretos e indiretos associados à entrega do produto/serviço.
- [x] Pesquisei e documentei os modelos de precificação de pelo menos 3 concorrentes diretos.
- [x] Criei uma matriz de valor percebido para cada plano/produto ofertado.
- [x] Defini uma proposta de valor clara para cada ponto de preço.
- [x] Configurei um teste A/B para, no mínimo, dois pontos de preço diferentes na landing page.
- [x] Estabeleci um processo de revisão periódica (trimestral/semestral) da estratégia de precificação.
- [x] Treinei a equipe de vendas com scripts específicos para lidar com objeções de preço.
- [x] Avaliei o impacto da precificação na taxa de churn e no ARPU (Average Revenue Per User).

---

## Métricas de Referência

| Métrica                         | Benchmark (