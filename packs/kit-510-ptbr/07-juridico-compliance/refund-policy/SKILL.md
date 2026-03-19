---
name: refund-policy
description: "Refund Policy — Skill especializada para refund policy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
---

# Refund Policy

Esta skill capacita o Claude a elaborar, analisar e otimizar políticas de reembolso robustas e conformes com a legislação brasileira, garantindo clareza e segurança jurídica para empresas e consumidores.

---

## Keywords

CDC, direito de arrependimento, estorno, chargeback, prazo de devolução, conformidade, e-commerce, serviços digitais, vício do produto, garantia legal, restituição de valores, LGPD, contrato.

---

## Quick Start

1.  **Avaliar Requisitos Legais:** Inicie identificando as obrigações impostas pelo Código de Defesa do Consumidor (CDC) e, se aplicável, o Decreto do E-commerce (Decreto 7.962/2013), focando no direito de arrependimento.
2.  **Definir Critérios de Elegibilidade:** Estabeleça claramente as condições sob as quais um produto ou serviço é elegível para reembolso, como estado do item, prazo de solicitação e apresentação de comprovantes.
3.  **Estruturar o Processo de Solicitação:** Desenhe o fluxo exato que o consumidor deve seguir para solicitar um reembolso, incluindo canais de contato e informações necessárias.
4.  **Determinar Métodos de Reembolso:** Especifique as formas de restituição dos valores, como estorno no cartão de crédito, depósito em conta ou crédito para futuras compras, e os respectivos prazos para processamento.

---

## Core Workflows

### Workflow 1: Elaboração e Implementação de Política de Reembolso para E-commerce

Este workflow detalha a criação de uma política de reembolso para lojas virtuais, com foco na conformidade legal e clareza para o consumidor.

**Passos Detalhados:**

1.  **Análise da Base Legal (CDC e Decreto 7.962/2013):**
    *   **Ação:** Revise o Art. 49 do CDC, que garante o direito de arrependimento em compras fora do estabelecimento comercial (online, por exemplo), com prazo de 7 dias a contar da assinatura do contrato ou do recebimento do produto.
    *   **Ação:** Verifique o Decreto 7.962/2013 para requisitos específicos de informação em e-commerce, como a necessidade de apresentar sumário do contrato antes da contratação e canais de atendimento eficazes.
    *   **Exemplo:** A Loja "TechStore BR" deve garantir que seu processo de checkout exiba claramente a política de reembolso e os 7 dias para arrependimento, conforme exigido.
2.  **Definição dos Critérios de Elegibilidade e Prazos:**
    *   **Ação:** Estabeleça as condições para que um item seja aceito para devolução ou troca, como "produto sem sinais de uso", "na embalagem original, com todos os acessórios e manual", e "acompanhado da Nota Fiscal".
    *   **Ação:** Determine prazos adicionais para vícios ou defeitos de fabricação (30 dias para produtos não duráveis e 90 dias para produtos duráveis, a partir da constatação do vício, conforme CDC Art. 26).
    *   **Exemplo:** Para um smartphone (produto durável) da "TechStore BR", o cliente tem 7 dias para arrependimento após o recebimento. Se o aparelho apresentar um defeito de fabricação após 45 dias de uso, ele ainda estaria coberto pela garantia legal de 90 dias para vícios, desde que o vício não seja decorrente de mau uso.
3.  **Estruturação do Processo de Solicitação e Devolução:**
    *   **Ação:** Crie um canal de comunicação dedicado para solicitações de reembolso (ex: formulário online, e-mail específico, telefone).
    *   **Ação:** Descreva o passo a passo para o cliente devolver o produto: solicitação via portal, geração de código de postagem reversa (sem custo para o consumidor no direito de arrependimento), envio do produto.
    *   **Exemplo:** Um cliente da "TechStore BR" que deseja devolver um fone de ouvido dentro do prazo de 7 dias deve acessar a seção "Minhas Compras" no site, clicar em "Solicitar Devolução" ao lado do pedido, preencher o motivo, e receberá um código de postagem reversa via e-mail para enviar o produto pelos Correios.
4.  **Definição dos Métodos e Prazos de Restituição:**
    *   **Ação:** Especifique como o dinheiro será devolvido (estorno no cartão de crédito, depósito em conta bancária, voucher).
    *   **Ação:** Determine o prazo para a restituição após o recebimento e análise do produto devolvido. O CDC não estabelece um prazo específico para o reembolso após a devolução, mas o bom senso e as práticas de mercado indicam agilidade. O estorno de compras online geralmente leva 3-10 dias úteis para ser processado pela empresa, e mais 1-2 faturas para aparecer no extrato do cliente, dependendo da operadora do cartão.
    *   **Exemplo:** A "TechStore BR" informa que, após o recebimento e conferência do produto devolvido (em até 3 dias úteis), o estorno será solicitado à operadora do cartão de crédito, com o valor aparecendo na fatura do cliente em até 2 ciclos de faturamento. Para pagamentos via Pix, o depósito será efetuado na conta do cliente em até 5 dias úteis.

### Workflow 2: Gestão de Solicitações de Reembolso e Conformidade LGPD

Este workflow aborda a gestão prática das solicitações de reembolso, focando na eficiência operacional e na proteção de dados pessoais.

**Passos Detalhados:**

1.  **Recebimento e Triagem da Solicitação:**
    *   **Ação:** Implemente um sistema para registrar todas as solicitações de reembolso, capturando data, cliente, produto/serviço, motivo e valor.
    *   **Ação:** Classifique a solicitação quanto ao tipo (arrependimento, vício, erro na entrega) e ao canal de origem.
    *   **Exemplo:** A empresa de software "CodeSolutions S.A." recebe uma solicitação de reembolso para uma licença de software devido a "arrependimento" via seu portal de suporte. O sistema atribui um ID de ticket (ex: REF-2024-00123) e notifica a equipe de atendimento.
2.  **Verificação de Elegibilidade e Coleta de Evidências:**
    *   **Ação:** Compare a solicitação com os critérios estabelecidos na política de reembolso da empresa.
    *   **Ação:** Se necessário, solicite informações adicionais ou evidências ao cliente (fotos do produto, descrição detalhada do vício, comprovante de compra).
    *   **Exemplo:** Para a solicitação de "CodeSolutions S.A.", a equipe verifica se a licença foi ativada e se o pedido foi feito dentro dos 7 dias após a compra, conforme a política de software da empresa. Se o software foi ativado e usado por mais de 7 dias, a solicitação pode ser negada com base na política de uso.
3.  **Comunicação Transparente com o Cliente:**
    *   **Ação:** Mantenha o cliente informado sobre o status da sua solicitação em cada etapa (recebida, em análise, aprovada/negada, reembolso processado).
    *   **Ação:** Utilize modelos de comunicação claros e objetivos, explicando os motivos em caso de negação.
    *   **Exemplo:** "CodeSolutions S.A." envia e-mails automáticos ao cliente: 1) Confirmação de recebimento da solicitação; 2) Notificação de que a solicitação está em análise; 3) Notificação de aprovação do reembolso com prazo para estorno, ou notificação de negação com a justificativa baseada na política.
4.  **Processamento do Reembolso e Registro:**
    *   **Ação:** Se aprovado, inicie o processo de estorno ou depósito, integrando-o, se possível, com o gateway de pagamento ou sistema financeiro.
    *   **Ação:** Registre detalhadamente a ação tomada (valor, data, método, ID de transação) para fins de auditoria e conformidade.
    *   **Exemplo:** Para um reembolso aprovado de "CodeSolutions S.A.", o sistema envia uma requisição para o gateway de pagamento (ex: Stripe, PagSeguro) para estornar R$ 199,90 para o cartão de crédito do cliente. O ID da transação de estorno é registrado no ticket REF-2024-00123.
5.  **Conformidade com a LGPD (Lei Geral de Proteção de Dados):**
    *   **Ação:** Assegure que todos os dados pessoais coletados durante o processo de reembolso (nome, CPF, endereço, dados bancários) sejam armazenados de forma segura, com consentimento adequado e apenas pelo tempo necessário.
    *   **Ação:** Implemente políticas de acesso restrito a esses dados e mecanismos para o titular exercer seus direitos (acesso, correção, exclusão).
    *   **Exemplo:** Os dados bancários fornecidos pelo cliente da "CodeSolutions S.A." para um depósito são criptografados no banco de dados e acessíveis apenas pela equipe financeira autorizada. Após a conclusão do reembolso e o período legal de retenção, esses dados são anonimizados ou excluídos, conforme a política de retenção de dados da empresa.

---

## Templates

### Cláusula de Direito de Arrependimento (E-commerce)

```
**Política de Devolução por Arrependimento (Compras Online na [Nome da Empresa])**

De acordo com o Código de Defesa do Consumidor (Lei nº 8.078/90), o cliente da [Nome da Empresa, ex: "Loja Exemplo Online Ltda."] que realiza compras online possui o direito de arrependimento.

**Prazo para Arrependimento:** O prazo para manifestar o arrependimento é de até 7 (sete) dias corridos, a contar da data de recebimento do produto. Para serviços, o prazo é de 7 (sete) dias corridos a contar da data da contratação.

**Condições para Devolução:**
1.  O produto deve ser devolvido em sua embalagem original, sem indícios de uso e com todos os acessórios, manuais e etiquetas intactos.
2.  A Nota Fiscal ou DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) deve acompanhar o produto.
3.  O custo do frete para devolução por arrependimento é de responsabilidade da [Nome da Empresa]. Um código de postagem reversa será fornecido.

**Processo de Solicitação:**
1.  Para solicitar a devolução, o cliente deve entrar em contato com nossa Central de Atendimento através do e-mail [email@exemplo.com.br] ou telefone [número de telefone] informando o número do pedido e o motivo do arrependimento.
2.  Após a solicitação, nossa equipe orientará sobre o procedimento de postagem reversa.

**Restituição de Valores:**
*   **Cartão de Crédito:** O estorno será solicitado à administradora do cartão em até 5 (cinco) dias úteis após o recebimento e análise do produto devolvido. O prazo para o valor constar na fatura pode variar conforme a operadora, geralmente ocorrendo em até 2 (duas) faturas subsequentes.
*   **Pix ou Boleto Bancário:** O reembolso será realizado via depósito bancário na conta corrente do titular da compra em até 7 (sete) dias úteis após a análise do produto. É imprescindível que os dados bancários informados sejam do mesmo titular do pedido.

Produtos devolvidos sem prévia comunicação, fora do prazo ou com ausência de itens/acessórios que o acompanham, serão reenviados ao cliente sem direito a reembolso.
```

### Template de E-mail de Confirmação de Reembolso Aprovado

```
**Assunto: Seu reembolso do pedido #[Número do Pedido] foi processado!**

Prezado(a) [Nome do Cliente],

Confirmamos que sua solicitação de reembolso referente ao pedido #[Número do Pedido], item(ns) [Nome do(s) Produto(s) ou Serviço(s)], foi aprovada e processada com sucesso.

**Detalhes do Reembolso:**
*   **Valor Reembolsado:** R$ [Valor do Reembolso]
*   **Método de Reembolso:** [Estorno no cartão de crédito / Depósito em conta bancária / Crédito em loja]
*   **Detalhes Adicionais:**
    *   **Para Estorno no Cartão de Crédito:** O valor será creditado na fatura do seu cartão utilizado na compra. O prazo para visualização pode variar de 1 a 2 ciclos de faturamento, dependendo da administradora do seu cartão.
    *   **Para Depósito em Conta Bancária:** O valor foi depositado na conta bancária informada por você:
        *   Banco: [Nome do Banco]
        *   Agência: [Número da Agência]
        *   Conta Corrente/Poupança: [Número da Conta]
        *   Titular: [Nome do Titular da Conta]
        *   Data do Depósito: [Data do Depósito]
    *   **Para Crédito em Loja:** Um voucher no valor de R$ [Valor do Reembolso] foi gerado e enviado para seu e-mail, ou adicionado à sua conta em nosso site. Você pode utilizá-lo em sua próxima compra.

Caso tenha qualquer dúvida ou necessite de mais informações, por favor, entre em contato com nossa Central de Atendimento através do e-mail [email@exemplo.com.br] ou telefone [número de telefone], informando o número do seu pedido.

Agradecemos sua compreensão e paciência.

Atenciosamente,

Equipe de Atendimento ao Cliente
[Nome da Empresa]
[Link para o Site da Empresa]
```

---

## Checklist

- [x] Política de reembolso visível e acessível em todas as páginas relevantes do site/aplicativo (rodapé, página do produto, checkout).
- [x] Prazos de arrependimento (7 dias corridos para compras online) e devolução por vícios (30/90 dias) claramente definidos e em conformidade com o CDC.
- [x] Condições para elegibilidade do reembolso (ex: produto sem uso, embalagem original, nota fiscal) explicitadas de forma inequívoca.
- [x] Processo de solicitação de reembolso detalhado, com canais de contato específicos e requisitos de informação para o cliente.
- [x] Meios de restituição de valores (estorno, depósito, crédito em loja) informados, com prazos realistas para cada modalidade.
- [x] Indicação clara de quem arca com os custos de frete na devolução (empresa no caso de arrependimento ou vício).
- [x] Cláusulas específicas para reembolso de produtos digitais, serviços ou itens personalizados, se aplicável.
- [x] Previsão para tratamento de "chargebacks" e disputas de pagamento, com diretrizes internas e externas.
- [x] Política revisada anualmente ou sempre que houver mudanças na legislação (CDC, LGPD, etc.) ou nas operações da empresa.
- [x] Mecanismos para registro e rastreamento de todas as solicitações de reembolso para auditoria e análise de dados.
- [x] Informações sobre o tratamento de dados pessoais (LGPD) no processo de reembolso (ex: dados bancários).
- [x] Canais de comunicação eficazes para dúvidas ou problemas relacionados a reembolsos, com tempo de resposta definido.

---

## Métricas de Referência

| Métrica                         | Benchmark (E-commerce) | Meta (E-commerce) |
|---------------------------------|------------------------|-------------------|
| Taxa de Reembolso (Total Reembolsos / Total Vendas) | 3-5%                   | < 2.5%            |
| Tempo Médio de Processamento de Reembolso | 5 dias úteis           | < 3 dias úteis    |
| Taxa de Disputa/Chargeback (Total Disputas / Total Vendas) | < 0.5%                 | < 0.2%            |
| Satisfação do Cliente Pós-Reembolso (CSAT/NPS) | 70-80%                 | > 85%             |
| Custos de Frete de Devolução (% da receita) | 0.5-1.0%               | < 0.3%            |

---

## Erros Comuns

1.  **Prazos Insuficientes ou Incorretos**: Não respeitar os 7 dias corridos para o direito de arrependimento em compras online, ou não diferenciar prazos para vícios.
    *   **Como evitar**: Sempre iniciar a elaboração da política com a revisão do Art. 49 e Art. 26 do CDC. Exemplo: Uma política que estabelece "3 dias para devolução" para compras online está em desacordo com a lei brasileira.
2.  **Linguagem Ambígua ou Excessivamente Jurídica**: Utilizar termos complexos ou frases vagas que dificultam a compreensão do consumidor sobre seus direitos e o processo de reembolso.
    *   **Como evitar**: Escrever a política em linguagem clara, objetiva e acessível, com exemplos práticos. Evitar jargões jurídicos desnecessários. Exemplo: Em vez de "A restituição pecuniária ocorrerá mediante estorno", use "O valor pago será devolvido por meio de estorno em seu cartão de crédito".
3.  **Processo de Reembolso Obstruído ou Burocrático**: Criar obstáculos intencionais ou não intencionais que dificultam o exercício do direito de reembolso pelo consumidor, como exigir múltiplos contatos, formulários extensos ou custos indevidos.
    *   **Como evitar**: Simplificar o processo de solicitação, oferecendo um canal direto e claro (ex: formulário online dedicado). Assumir os custos de frete na devolução por arrependimento. Exemplo: Exigir que o cliente ligue para 3 números diferentes, envie 5 e-mails e preencha um formulário físico para solicitar um reembolso de um item de baixo valor.

---

## Dicas Avançadas

1.  **Política Dinâmica por Categoria de Produto/Serviço**: Implementar cláusulas de reembolso específicas para diferentes tipos de produtos (ex: eletrônicos, vestuário, softwares, serviços digitais) ou serviços (assinaturas, consultorias), reconhecendo suas particularidades legais e operacionais.
    *   **Exemplo**: Enquanto um eletrônico pode exigir a devolução na caixa lacrada, um software pode ter uma política de reembolso restrita após a ativação da licença, e um serviço de consultoria pode prever reembolso proporcional por horas não utilizadas.
2.  **Análise Preditiva de Reembolsos e Otimização de Produtos**: Utilizar dados históricos de reembolsos (motivos, categorias de produtos, perfil de cliente) para identificar padrões, prever futuras solicitações e, proativamente, otimizar a descrição de produtos, melhorar a qualidade ou ajustar as expectativas do cliente.
    *   **Exemplo**: Se 15% dos reembolsos de um tênis específico são por "tamanho inadequado", a loja pode revisar a tabela de medidas do produto, adicionar fotos com modelos vestindo o tênis ou incluir um guia de como medir o pé.
3.  **Integração Automatizada com Sistemas de Pagamento e CRM/ERP**: Conectar o fluxo de solicitação de reembolso diretamente com o gateway de pagamento e o sistema de gestão (CRM/ERP) para automatizar a verificação de elegibilidade, o processamento do estorno e a atualização do status do pedido, reduzindo erros manuais e tempo de resposta.
    *   **Exemplo**: Um cliente solicita reembolso via portal; o sistema verifica o prazo e o status do pedido no ERP; se elegível, envia um comando de estorno ao Stripe/MercadoPago; o status do pedido no ERP é automaticamente atualizado para "Reembolso Processado".
4.  **Treinamento Avançado da Equipe de Suporte e Cenários Complexos**: Capacitar a equipe de atendimento ao cliente não apenas sobre a política, mas também sobre a legislação (CDC) e como lidar com cenários complexos, como pedidos múltiplos, devoluções parciais, produtos danificados no transporte ou disputas de clientes, utilizando scripts e fluxogramas de decisão.
    *   **Exemplo**: Um treinamento que aborda o que fazer quando um cliente alega um vício oculto após 60 dias de uso de um produto durável, diferenciando a garantia legal da garantia contratual e como documentar a comunicação.
5.  **Auditoria Contínua e Simulações de Cenários de Reembolso**: Realizar auditorias periódicas na execução da política de reembolso e conduzir simulações de cenários (ex: cliente tenta devolver produto fora do prazo, cliente alega não ter recebido o reembolso) para identificar gargalos, pontos de melhoria e garantir a conformidade e a eficácia operacional.
    *   **Exemplo**: Simular uma situação de "chargeback" para testar a agilidade da equipe em fornecer a documentação necessária ao banco para contestar a disputa, minimizando perdas financeiras.