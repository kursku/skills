---
name: privacy-policy-generator
description: "Privacy Policy Generator — Skill especializada para privacy policy generator"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
---

# Privacy Policy Generator

Esta skill capacita o Claude a gerar políticas de privacidade personalizadas e conformes com a LGPD e GDPR, adaptadas às operações de coleta e tratamento de dados de qualquer empresa ou projeto digital.

---

## Keywords

LGPD, GDPR, Política de Privacidade, Termos de Uso, Dados Pessoais, Consentimento, Direitos do Titular, Transferência Internacional de Dados, Cookies, DPO, Conformidade Digital, Segurança da Informação, Aviso de Privacidade.

---

## Quick Start

1.  Descrever o tipo de negócio: E-commerce de moda, SaaS de gestão financeira, blog de culinária, aplicativo mobile de fitness.
2.  Listar as categorias de dados pessoais coletados: Nome, e-mail, CPF, endereço, dados de pagamento, IP, histórico de navegação.
3.  Indicar as finalidades primárias para o tratamento desses dados: Processamento de pedidos, envio de newsletter, análise de uso, suporte ao cliente, personalização de conteúdo.
4.  Mencionar os principais terceiros com quem os dados são compartilhados: Transportadoras, gateways de pagamento, provedores de cloud, ferramentas de analytics.
5.  Gerar o rascunho inicial da política de privacidade, solicitando ao Claude focar na clareza e na conformidade legal.

---

## Core Workflows

### Workflow 1: Geração de Política de Privacidade para E-commerce com LGPD/GDPR

Este workflow guia a criação de uma política de privacidade detalhada para um e-commerce, considerando as especificidades da coleta de dados de clientes para vendas, marketing e logística, em conformidade com a LGPD e o GDPR.

1.  **Identificar o Controlador e o DPO/Encarregado**:
    *   **Exemplo**: O e-commerce "Jardim Secreto Flores Online" é o controlador. O Encarregado de Dados (DPO) é "Mariana Costa", contato: dpo@jardimsecreto.com.br.
2.  **Categorizar os Dados Pessoais Coletados**:
    *   **Exemplo**:
        *   **Dados de Cadastro**: Nome completo, CPF, RG, e-mail, telefone, endereço de entrega e cobrança.
        *   **Dados de Pagamento**: Informações de cartão de crédito (coletadas via gateway de pagamento, sem armazenamento direto), status da transação.
        *   **Dados de Navegação**: Endereço IP, geolocalização aproximada, tipo de navegador, sistema operacional, páginas visitadas, produtos visualizados, tempo de permanência, cookies e tecnologias de rastreamento.
        *   **Dados de Histórico de Compras**: Produtos adquiridos, datas, valores, métodos de pagamento.
3.  **Definir as Finalidades Específicas do Tratamento**:
    *   **Exemplo**:
        *   **Processamento de Pedidos**: Para viabilizar a compra, faturamento e entrega (Base Legal: Execução de contrato).
        *   **Comunicação com o Cliente**: Para suporte, informações sobre o pedido (Base Legal: Execução de contrato, Legítimo Interesse).
        *   **Marketing Direcionado**: Envio de newsletters, promoções personalizadas (Base Legal: Consentimento).
        *   **Análise de Desempenho do Site**: Melhoria da experiência do usuário, otimização de campanhas (Base Legal: Legítimo Interesse).
        *   **Cumprimento de Obrigações Legais**: Emissão de notas fiscais, atendimento a requisições judiciais (Base Legal: Obrigação Legal).
4.  **Listar Terceiros com Compartilhamento de Dados**:
    *   **Exemplo**:
        *   **Transportadoras**: Correios, Loggi (para entrega dos produtos).
        *   **Gateways de Pagamento**: PagSeguro, Mercado Pago (para processamento de transações financeiras).
        *   **Provedores de Cloud**: AWS (para hospedagem do site e dados).
        *   **Ferramentas de Marketing**: Mailchimp (para envio de e-mails marketing, apenas com consentimento).
        *   **Ferramentas de Análise**: Google Analytics (para análise de tráfego e comportamento do usuário).
5.  **Estabelecer o Prazo de Retenção dos Dados**:
    *   **Exemplo**: Dados de cadastro e histórico de compras serão retidos por 5 anos após a última compra para fins fiscais e legais, ou enquanto for necessário para as finalidades para as quais foram coletados, respeitando os direitos do titular. Dados de navegação (cookies) por 12 meses.
6.  **Descrever Medidas de Segurança Adotadas**:
    *   **Exemplo**: Criptografia SSL/TLS em todas as comunicações, autenticação de dois fatores para acesso administrativo, controle de acesso baseado em função, backups regulares, treinamento de privacidade para funcionários.
7.  **Estruturar a Seção de Direitos do Titular**:
    *   **Exemplo**: Detalhar direitos como acesso, retificação, eliminação, portabilidade e revogação do consentimento, com o contato do DPO para exercer esses direitos.
8.  **Gerar o Texto Completo da Política**: Com base nas informações coletadas, o Claude irá redigir a política de privacidade, garantindo clareza, objetividade e aderência às normativas.

### Workflow 2: Atualização de Política de Privacidade para SaaS B2B devido a Nova Funcionalidade

Este workflow aborda a revisão e atualização de uma política de privacidade existente para uma plataforma SaaS B2B, que implementou uma nova funcionalidade de integração com sistemas de terceiros, exigindo a inclusão de novas cláusulas e a revisão das existentes.

1.  **Identificar a Nova Funcionalidade e seu Impacto nos Dados**:
    *   **Exemplo**: A plataforma SaaS "Gestão Ágil CRM" introduziu um módulo de "Integração com Ferramentas de Marketing Digital" (Ex: RD Station, HubSpot).
    *   **Impacto**: Agora, dados de contato e comportamento de leads dos clientes do "Gestão Ágil CRM" podem ser sincronizados entre a plataforma e as ferramentas de marketing.
2.  **Identificar Novos Dados Pessoais Coletados/Processados**:
    *   **Exemplo**: Adicionalmente aos dados de uso da plataforma, a nova funcionalidade pode processar: nome do lead, e-mail do lead, telefone do lead, histórico de interação do lead com materiais de marketing (e-mails abertos, cliques).
3.  **Definir Novas Finalidades de Tratamento**:
    *   **Exemplo**: Otimização de campanhas de marketing digital, automação de fluxos de nutrição de leads, segmentação de público-alvo para comunicação.
4.  **Identificar Novos Terceiros Envolvidos e Suas Funções**:
    *   **Exemplo**: RD Station, HubSpot (operadores de dados, para quem os dados são transferidos ou sincronizados conforme as instruções do cliente do SaaS).
5.  **Revisar a Base Legal Existente e Determinar Novas Bases**:
    *   **Exemplo**: A base legal para o tratamento dos dados dos leads será primariamente o consentimento (obtido pelo cliente do SaaS) ou o legítimo interesse (do cliente do SaaS), conforme o caso. A política deve deixar claro que o "Gestão Ágil CRM" atua como operador para seus clientes.
6.  **Adicionar Cláusulas Específicas à Política Existente**:
    *   **Exemplo**:
        *   **Nova Cláusula**: "4.5. Dados Processados Via Integrações de Terceiros: Ao utilizar a funcionalidade de integração com ferramentas de marketing digital, o 'Gestão Ágil CRM' atuará como operador, processando dados de contato e comportamento de leads (e.g., nome, e-mail, histórico de interação) em nome de seus clientes. A responsabilidade pela obtenção do consentimento ou pela legitimidade da base legal para o tratamento desses dados é do cliente do 'Gestão Ágil CRM'."
        *   **Atualização em "Compartilhamento de Dados"**: Incluir os novos parceiros (RD Station, HubSpot) e as condições de compartilhamento.
7.  **Revisar Cláusulas de Segurança e Direitos do Titular**:
    *   **Exemplo**: As medidas de segurança devem ser robustas para as novas transferências. Os direitos dos titulares devem ser mantidos, com a ressalva de que, para dados de leads, o cliente do SaaS é o controlador primário.
8.  **Elaborar um Comunicado de Atualização**:
    *   **Exemplo**: Preparar um e-mail ou notificação in-app para informar os usuários sobre as mudanças na política de privacidade e os novos termos relacionados à funcionalidade.

---

## Templates

### Cláusula de Dados Pessoais Coletados (Exemplo E-commerce)

```
Cláusula 3. Tipos de Dados Pessoais Coletados

A "Jardim Secreto Flores Online" coleta os seguintes tipos de dados pessoais de seus usuários e clientes:

3.1. Dados de Identificação e Contato: Nome completo, CPF, RG, e-mail, telefone, endereço completo (para entrega e cobrança). Estes dados são essenciais para o processamento de pedidos, faturamento, comunicação sobre o status da compra e entrega.
3.2. Dados de Pagamento: Informações de cartão de crédito (número, validade, código de segurança) são coletadas diretamente por gateways de pagamento (e.g., PagSeguro, Mercado Pago) e não são armazenadas pela "Jardim Secreto Flores Online", exceto informações parciais para identificação da transação (e.g., últimos 4 dígitos do cartão).
3.3. Dados de Navegação e Uso: Endereço IP, localização geográfica aproximada, tipo de navegador, sistema operacional, páginas visitadas, produtos visualizados, tempo de permanência, cliques, dados de cookies e outras tecnologias de rastreamento. Estes dados são coletados para melhorar a experiência do usuário, personalizar conteúdo, analisar o desempenho do site e direcionar ofertas relevantes.
3.4. Dados de Histórico de Compras: Produtos adquiridos, valores, datas das transações, métodos de pagamento utilizados. Utilizados para gerenciamento de pedidos, suporte pós-venda, ofertas personalizadas e análise de tendências de consumo.

A coleta desses dados é realizada mediante o consentimento do usuário, para execução de contrato de compra e venda, para atender a legítimos interesses da "Jardim Secreto Flores Online" ou para cumprimento de obrigações legais.
```

### Cláusula de Direitos do Titular (Exemplo Geral)

```
Cláusula 7. Direitos do Titular dos Dados Pessoais

Conforme a Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018) e o Regulamento Geral de Proteção de Dados (GDPR - Regulamento UE 2016/679), o titular dos dados pessoais possui os seguintes direitos em relação aos seus dados tratados pela [Nome da Empresa]:

7.1. Confirmação e Acesso: Obter a confirmação da existência de tratamento de seus dados e acesso a eles.
7.2. Retificação: Solicitar a correção de dados incompletos, inexatos ou desatualizados.
7.3. Anonimização, Bloqueio ou Eliminação: Requisitar a anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com a LGPD.
7.4. Portabilidade: Solicitar a portabilidade dos dados a outro fornecedor de serviço ou produto, mediante requisição expressa, observados os segredos comercial e industrial.
7.5. Eliminação: Requisitar a eliminação dos dados pessoais tratados com o seu consentimento, exceto nas hipóteses previstas em lei (e.g., cumprimento de obrigação legal ou regulatória).
7.6. Informação sobre Compartilhamento: Obter informações sobre as entidades públicas e privadas com as quais o [Nome da Empresa] realizou uso compartilhado de dados.
7.7. Informação sobre Revogação do Consentimento: Ser informado sobre a possibilidade de não fornecer consentimento e sobre as consequências da negativa.
7.8. Revogação do Consentimento: Revogar o consentimento a qualquer momento, sem que isso afete a legalidade do tratamento realizado antes da revogação.
7.9. Oposição: Opor-se ao tratamento de dados pessoais quando houver descumprimento à LGPD ou GDPR.

Para exercer qualquer um desses direitos, o titular pode entrar em contato com nosso Encarregado de Dados (DPO) através do e-mail: dpo@nomedaempresa.com.br. Responderemos às solicitações no prazo legal aplicável.
```

---

## Checklist

- [x] Dados de contato completos do controlador e, se aplicável, do DPO/Encarregado.
- [x] Listagem clara e específica das categorias de dados pessoais coletados.
- [x] Descrição detalhada das finalidades para cada categoria de dados coletados.
- [x] Indicação da base legal para cada finalidade de tratamento (e.g., consentimento, execução de contrato, legítimo interesse, obrigação legal).
- [x] Lista de terceiros com quem os dados são compartilhados, incluindo o tipo de terceiro e a finalidade do compartilhamento.
- [x] Informações sobre o prazo de retenção dos dados pessoais para cada finalidade.
- [x] Seção clara sobre os direitos dos titulares (acesso, retificação, eliminação, portabilidade, revogação do consentimento, etc.).
- [x] Descrição das medidas de segurança técnicas e organizacionais adotadas para proteger os dados.
- [x] Informações detalhadas sobre o uso de cookies e outras tecnologias de rastreamento, incluindo como o usuário pode gerenciá-los.
- [x] Cláusula específica para transferência internacional de dados, se aplicável, com as garantias adotadas.
- [x] Procedimento explícito para revogação de consentimento e suas consequências.
- [x] Data da última atualização da política, visível e de fácil acesso.
- [x] Linguagem clara, objetiva e acessível, evitando jargões jurídicos excessivos.

---

## Métricas de Referência

| Métrica | Benchmark | Meta |
|:-------------------------------------------|:----------|:-----|
| Taxa de consentimento para marketing digital | 70-85%    | >80% |
| Tempo médio para resposta a solicitações de direitos do titular (DSAR) | < 15 dias | < 10 dias |
| Número de incidentes de segurança de dados reportados/ano | < 1 (PME) | 0    |
| Percentual de políticas de privacidade revisadas anualmente | 100%      | 100% |
| Pontuação em auditoria de conformidade com LGPD/GDPR | > 85%     | >90% |
| Taxa de opt-out de cookies de marketing (via banner/ferramenta) | < 10%     | < 7% |

---

## Erros Comuns

1.  **Linguagem Excessivamente Jurídica e Obscura**: Utilizar termos técnicos do direito de forma densa, dificultando a compreensão do usuário comum sobre como seus dados são tratados.
    *   **Como evitar**: Substituir "O Controlador reserva-se o direito de proceder à anonimização irreversível dos conjuntos de dados tratados" por "Podemos tornar seus dados anônimos para análises estatísticas, impossibilitando sua identificação futura."
2.  **Omissão de Finalidades Reais de Tratamento de Dados**: Não listar todas as finalidades para as quais os dados são realmente utilizados, especialmente para marketing, remarketing ou análise de comportamento.
    *   **Como evitar**: Se o site utiliza Google Analytics para direcionar campanhas de remarketing, não basta dizer "melhora do site". Deve-se especificar "análise de padrões de navegação para otimizar a usabilidade do site e direcionar campanhas de marketing personalizadas baseadas em seu interesse".
3.  **Não Atualizar a Política após Novas Funcionalidades ou Parcerias**: Lançar um novo recurso ou integrar-se a um novo parceiro que envolve tratamento de dados sem atualizar a política de privacidade.
    *   **Como evitar**: Se uma empresa SaaS adiciona uma integração com um novo CRM (Ex: Pipedrive), é crucial incluir esse parceiro e os dados compartilhados na política antes de disponibilizar a funcionalidade. Além disso, comunicar proativamente os usuários sobre a atualização.

---

## Dicas Avançadas

1.  **Mapeamento de Dados Detalhado e Contínuo (Data Mapping)**: Implemente um inventário robusto de todos os dados pessoais coletados, armazenados, processados e compartilhados. Utilize uma matriz que inclua "Dado Coletado", "Finalidade", "Base Legal", "Tempo de Retenção", "Terceiros Envolvidos" e "Medidas de Segurança". Isso garante que a política reflita a realidade operacional.
2.  **Privacidade por Design (Privacy by Design)**: Incorpore os princípios de privacidade desde o estágio inicial do design de qualquer novo produto, serviço ou funcionalidade. Por exemplo, ao desenvolver um novo formulário de cadastro, questione quais dados são estritamente necessários (minimização de dados) e projete o sistema para obter consentimento granular e claro.
3.  **Implementação de Política de Privacidade em Camadas**: Para melhorar a clareza e a usabilidade, apresente a política em diferentes níveis. Um aviso conciso (primeira camada) no banner de cookies ou no momento da coleta de dados essenciais, com um link para a política completa e detalhada (segunda camada). Isso permite que o usuário acesse a informação de forma progressiva.
4.  **Auditorias de Conformidade e Testes de Vulnerabilidade Periódicos**: Além da revisão jurídica anual, realize auditorias técnicas de segurança (pentests, varreduras de vulnerabilidade) e auditorias de conformidade com a LGPD/GDPR para identificar e corrigir falhas antes que se tornem incidentes. Contrate empresas especializadas para uma análise externa e imparcial.
5.  **Gerenciamento de Consentimento Granular (Consent Management Platform - CMP)**: Para sites e aplicativos complexos, invista em uma plataforma de gerenciamento de consentimento que permita aos usuários aceitar ou recusar categorias específicas de cookies e tratamentos de dados (e.g., marketing, desempenho, funcionalidade). Isso demonstra respeito pela autonomia do titular e facilita a prova de conformidade.