---
name: age-verification
description: "Age Verification — Skill especializada para implementar e auditar sistemas de verificação de idade, garantindo conformidade legal e minimizando riscos."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Age Verification

Esta skill capacita o Claude a projetar, implementar e auditar soluções de verificação de idade, garantindo conformidade com leis como LGPD, GDPR e ECA, e protegendo menores de acesso a conteúdos ou produtos restritos.

---

## Keywords

Verificação de Idade Digital, Age Gating, Conformidade LGPD, Conformidade GDPR, Proteção de Crianças Online (COPPA/ECA), KYC (Know Your Customer) Idade, Consentimento Parental, Sistemas de Idade Mínima, Políticas de Dados Infantis, Digital Identity Verification, Biometric Age Estimation, Document Verification, Proxy Detection.

---

## Quick Start

1.  **Mapear Requisitos Legais**: Identificar leis aplicáveis (ex: ECA para Brasil, GDPR Art. 8 para UE, COPPA para EUA) e a idade mínima específica para seu produto/serviço.
2.  **Escolher Método de Verificação**: Selecionar a abordagem mais adequada ao risco do negócio (ex: autodeclaração para conteúdo informativo, verificação de documento com IA para venda de álcool/tabaco).
3.  **Integrar Fluxo de Usuário**: Inserir o processo de verificação de idade em pontos críticos da jornada do cliente (ex: antes do acesso a conteúdo restrito, antes de adicionar produtos ao carrinho, no registro).
4.  **Elaborar Termos de Uso e Política de Privacidade**: Atualizar documentos legais para refletir claramente o processo de verificação, dados coletados, finalidade e base legal.
5.  **Implementar Auditoria e Monitoramento**: Configurar logs para registrar tentativas de verificação, sucessos e falhas, além de um processo para revisões periódicas da eficácia do sistema.

---

## Core Workflows

### Workflow 1: Implementação de Verificação de Idade para E-commerce de Produtos Restritos

Este workflow detalha a implementação de um sistema robusto de verificação de idade para um e-commerce que comercializa produtos com restrição de idade, como bebidas alcoólicas ou jogos para maiores.

1.  **Classificação de Produtos**:
    *   **Ação**: Categorizar todos os produtos do catálogo com base em sua restrição de idade (ex: `+18`, `+16`, `Sem Restrição`).
    *   **Exemplo**: O sistema de gerenciamento de produtos (ERP/PIM) deve ter um campo `idade_minima_legal` para cada SKU. Para uma garrafa de vinho, `idade_minima_legal: 18`. Para um jogo de tabuleiro infantil, `idade_minima_legal: 0`.

2.  **Seleção da Tecnologia de Verificação**:
    *   **Ação**: Avaliar e contratar um provedor de Identity Verification (IDV) que suporte verificação de documentos (OCR + biometria facial) e/ou consulta a bancos de dados públicos.
    *   **Exemplo**: Integração com APIs de empresas como `idwall` (Brasil) ou `Onfido` (global). Para produtos de alto risco, priorizar soluções com prova de vida e validação de autenticidade de documento. A escolha deve considerar a latência da API e a cobertura de documentos do país.

3.  **Desenho do Fluxo de Usuário na Jornada de Compra**:
    *   **Ação**: Definir os pontos de interrupção para a verificação de idade.
    *   **Exemplo**:
        *   **Cenário 1 (Produto no Carrinho)**: Ao adicionar o primeiro item `+18` ao carrinho, um modal é exibido solicitando a verificação de idade.
        *   **Cenário 2 (Checkout)**: A verificação é obrigatória no primeiro passo do checkout, antes da seleção de endereço ou pagamento, caso o carrinho contenha itens restritos e o usuário não tenha idade verificada.
        *   **Detalhe Técnico**: A verificação deve ser persistente via token JWT ou sessão de usuário, evitando re-verificação para o mesmo usuário dentro de um período razoável (ex: 6 meses, 1 ano).

4.  **Coleta e Tratamento de Dados Pessoais**:
    *   **Ação**: Coletar apenas os dados estritamente necessários para a verificação e com base legal clara (consentimento explícito ou cumprimento de obrigação legal).
    *   **Exemplo**: Para verificação de documento, o usuário faz upload de RG/CNH. A API do provedor IDV extrai nome, data de nascimento e foto. O e-commerce armazena apenas o **status** da verificação (Aprovado/Reprovado), a **data de nascimento validada** e um **ID único de transação** do provedor. A imagem do documento e dados sensíveis devem ser processados e retidos pelo provedor IDV sob contrato, conforme exigências regulatórias, e não pelo e-commerce, a menos que haja uma necessidade legal explícita e base legal para tal.
    *   **Base Legal**: Para a maioria das jurisdições (LGPD, GDPR), a base legal para processar dados de verificação de idade para produtos restritos é o "cumprimento de obrigação legal" (Art. 7, V da LGPD; Art. 6, 1, c do GDPR) ou "exercício regular de direitos em processo" (LGPD Art. 7, VI).

5.  **Gerenciamento de Falhas e Recusas**:
    *   **Ação**: Estabelecer procedimentos claros para usuários que falham na verificação ou se recusam a fornecê-la.
    *   **Exemplo**: Se a verificação falhar (ex: documento ilegível, idade insuficiente), o usuário é impedido de prosseguir com a compra dos itens restritos. Uma mensagem clara deve informar o motivo e as opções (ex: tentar novamente, remover item do carrinho). Não permitir o acesso ao conteúdo/produto restrito.

### Workflow 2: Auditoria de Conformidade LGPD/GDPR para Sistemas de Verificação de Idade

Este workflow orienta a realização de uma auditoria para garantir que o sistema de verificação de idade esteja em total conformidade com a LGPD e o GDPR, focando na proteção de dados e direitos dos titulares.

1.  **Mapeamento e Inventário de Dados (Data Mapping)**:
    *   **Ação**: Identificar todos os dados pessoais coletados, processados e armazenados durante o processo de verificação de idade.
    *   **Exemplo**: Criar uma planilha detalhada com campos como: `Dado Coletado` (Nome, CPF, Data Nascimento, Imagem Documento), `Finalidade` (Verificação de Idade, Prevenção Fraude), `Base Legal` (Obrigação Legal, Consentimento), `Local de Armazenamento` (BD Interno, Provedor IDV), `Período de Retenção`, `Quem tem Acesso`.

2.  **Avaliação da Base Legal e Consentimento**:
    *   **Ação**: Verificar se a base legal escolhida para o tratamento dos dados é adequada e se o consentimento (quando aplicável) é livre, informado e inequívoco.
    *   **Exemplo**: Para autodeclaração de idade, o consentimento deve ser explícito e preceder a coleta. Para verificação de documento para cumprimento de obrigação legal (ex: venda de álcool), a base legal pode ser "obrigação legal". Confirmar que os termos de uso e política de privacidade detalham essa base. Para dados biométricos, verificar se há consentimento específico e separado ou base legal robusta, dada a sensibilidade dos dados.

3.  **Avaliação de Segurança dos Dados (Data Security)**:
    *   **Ação**: Revisar as medidas técnicas e organizacionais de segurança para proteger os dados coletados.
    *   **Exemplo**:
        *   **Criptografia**: Dados em trânsito (TLS 1.2+) e em repouso (AES-256).
        *   **Controle de Acesso**: Acesso restrito apenas a funcionários autorizados, via autenticação multifator (MFA) e princípio do menor privilégio.
        *   **Anonimização/Pseudonimização**: Avaliar a possibilidade de técnicas que minimizem a identificação direta, quando possível.
        *   **Backup e Recuperação**: Planos de disaster recovery e backups regulares criptografados.
        *   **Contratos com Terceiros**: Garantir que os provedores de IDV tenham cláusulas contratuais de segurança e proteção de dados equivalentes ou superiores.

4.  **Exercício dos Direitos dos Titulares (Data Subject Rights)**:
    *   **Ação**: Confirmar que os mecanismos para os titulares de dados exercerem seus direitos (acesso, correção, exclusão, oposição) estão implementados.
    *   **Exemplo**: No portal do usuário, oferecer uma seção para solicitar cópia dos dados de verificação ou retificação (se aplicável). Para exclusão, o sistema deve ter um processo para remover os dados, respeitando os prazos legais de retenção.

5.  **Revisão da Política de Retenção e Descarte**:
    *   **Ação**: Verificar se os dados são retidos apenas pelo tempo necessário para a finalidade original e se há um processo seguro de descarte.
    *   **Exemplo**: Dados de verificação de idade podem ser retidos pelo período mínimo exigido pela legislação (ex: 5 anos para registros fiscais de vendas) ou pelo tempo necessário para comprovar a conformidade. Após esse período, os dados devem ser permanentemente excluídos ou anonimizados de forma irreversível.

6.  **Avaliação de Impacto à Proteção de Dados (DPIA/RIPD)**:
    *   **Ação**: Se o sistema de verificação envolver alto risco (ex: uso de biometria, grande escala, dados de crianças), verificar se uma DPIA (GDPR) ou RIPD (LGPD) foi realizada e revisada.
    *   **Exemplo**: A DPIA deve identificar riscos como vazamento de dados biométricos, discriminação algorítmica ou falha na identificação de menores, e propor medidas mitigadoras.

---

## Templates

### Cláusula de Termos de Uso - Verificação de Idade

```markdown
**Cláusula X - Verificação de Idade e Capacidade Legal**

1.  **Exigência de Idade Mínima**: Ao utilizar os serviços oferecidos por [Nome da Empresa/Plataforma], você declara expressamente ser maior de 18 (dezoito) anos ou ter a idade mínima legal exigida em sua jurisdição para adquirir e consumir os produtos ou acessar os conteúdos restritos aqui disponibilizados. Caso sua legislação local exija idade superior a 18 anos, você deverá respeitar a idade mínima legal aplicável.

2.  **Processo de Verificação**: Para garantir a conformidade com as leis aplicáveis, [Nome da Empresa/Plataforma] poderá, a seu exclusivo critério e em qualquer etapa da sua interação com a plataforma (incluindo, mas não se limitando, ao registro, acesso a conteúdo restrito ou finalização de compra de produtos específicos), solicitar a verificação da sua idade. Este processo poderá envolver:
    *   Autodeclaração de data de nascimento.
    *   Upload de documentos de identificação com foto (ex: RG, CNH, Passaporte) para validação via tecnologias de reconhecimento óptico de caracteres (OCR) e, eventualmente, biometria facial para prova de vida, por meio de parceiros especializados em verificação de identidade.
    *   Consultas a bancos de dados públicos ou privados, quando permitido por lei.

3.  **Consequências da Não Verificação ou Falha**: A recusa em fornecer as informações ou documentos solicitados para a verificação de idade, ou a falha no processo de verificação (incluindo, mas não se limitando, à constatação de que o usuário possui idade inferior à mínima exigida), impedirá o acesso a conteúdos restritos e/ou a aquisição de produtos com restrição de idade. [Nome da Empresa/Plataforma] reserva-se o direito de suspender ou encerrar contas que violem esta Cláusula.

4.  **Privacidade dos Dados**: Os dados coletados durante o processo de verificação de idade serão tratados em conformidade com nossa Política de Privacidade, tendo como base legal o cumprimento de obrigação legal e/ou o legítimo interesse, visando proteger menores e garantir a conformidade regulatória. Não armazenaremos dados biométricos ou imagens de documentos em nossos servidores, mas sim os resultados da verificação (data de nascimento validada e status de aprovação) e um identificador único da transação, sob estritas medidas de segurança.
```

### Política de Privacidade - Seção Verificação de Idade

```markdown
**Seção Y - Tratamento de Dados para Verificação de Idade**

1.  **Finalidade da Verificação de Idade**: Coletamos e processamos dados para verificação de idade com o objetivo primordial de garantir a conformidade com a legislação aplicável (como o Estatuto da Criança e do Adolescente - Lei nº 8.069/90 no Brasil, o General Data Protection Regulation - GDPR na União Europeia, ou leis específicas de cada jurisdição para a venda de produtos ou acesso a serviços restritos por idade, como bebidas alcoólicas, jogos para adultos ou conteúdo sensível). Esta medida visa proteger menores de idade e mitigar riscos legais e operacionais para [Nome da Empresa/Plataforma].

2.  **Dados Coletados para Verificação**: Dependendo do nível de risco e da legislação aplicável, poderemos coletar os seguintes dados para fins de verificação de idade:
    *   **Autodeclaração**: Data de nascimento.
    *   **Documentos de Identificação**: Imagem ou cópia de documentos de identificação oficiais (ex: RG, CNH, Passaporte) que contenham seu nome completo, data de nascimento e foto.
    *   **Dados Biométricos**: Em casos de alto risco e com seu consentimento explícito, poderemos utilizar tecnologias de reconhecimento facial para prova de vida (liveless check) para comparar com a foto do documento e verificar a autenticidade da pessoa.

3.  **Base Legal para o Tratamento**: O tratamento de seus dados pessoais para fins de verificação de idade é fundamentado, principalmente, nas seguintes bases legais:
    *   **Cumprimento de Obrigação Legal ou Regulatória**: Quando a legislação exige a verificação de idade para a oferta de determinados produtos ou serviços (Art. 7, V da LGPD; Art. 6, 1, c do GDPR).
    *   **Exercício Regular de Direitos em Processo**: Para nos defendermos em eventuais processos administrativos, judiciais ou arbitrais (Art. 7, VI da LGPD).
    *   **Consentimento**: Em situações em que a lei não exige a verificação, mas é do nosso legítimo interesse ou há uma necessidade específica que requer seu consentimento livre, informado e inequívoco (Art. 7, I da LGPD; Art. 6, 1, a do GDPR).

4.  **Compartilhamento de Dados para Verificação**: Para realizar a verificação de idade, podemos compartilhar seus dados com prestadores de serviços terceirizados especializados em verificação de identidade (ex: empresas de IDV), que atuam como operadores de dados sob nossas instruções e em conformidade com rigorosos contratos de proteção de dados. Esses parceiros são avaliados quanto às suas práticas de segurança e privacidade.

5.  **Retenção e Descarte de Dados de Verificação**: Os dados coletados para verificação de idade serão retidos apenas pelo período estritamente necessário para cumprir a finalidade para a qual foram coletados e as obrigações legais ou regulatórias. Após este período, seus dados serão eliminados de forma segura ou anonimizados. Por exemplo, informações sobre o status de verificação (aprovado/reprovado) e a data de nascimento validada podem ser retidas por [ex: 5 anos] para fins de auditoria e conformidade. Imagens de documentos e dados biométricos, se coletados, são geralmente retidos pelo tempo mínimo necessário para a validação e, em seguida, descartados pelos nossos parceiros, sem serem armazenados em nossos sistemas.

6.  **Seus Direitos**: Você tem o direito de solicitar acesso, correção, eliminação, oposição ao tratamento e outros direitos relacionados aos seus dados de verificação de idade, conforme detalhado na Seção [Número da Seção Geral de Direitos].
```

---

## Checklist

- [X] Classificação de todos os produtos/serviços com restrição de idade.
- [X] Documentação das bases legais para o tratamento de dados na verificação de idade.
- [X] Cláusula de verificação de idade incluída nos Termos de Uso e Política de Privacidade.
- [X] Processo de verificação de idade implementado em todos os pontos de acesso relevantes.
- [X] Acordo de Processamento de Dados (DPA) em vigor com todos os provedores de IDV.
- [X] Mecanismos de segurança (criptografia, controle de acesso) aplicados aos dados de verificação.
- [X] Política de retenção e descarte de dados específicos para informações de verificação de idade.
- [X] Fluxo de tratamento para tentativas de verificação falhas ou recusadas.
- [X] Capacidade de registrar e auditar todas as tentativas e resultados de verificação de idade.
- [X] Avaliação de Impacto à Proteção de Dados (RIPD/DPIA) realizada, se aplicável ao risco do tratamento.

---

## Métricas de Referência

| Métrica | Benchmark (Indústria) | Meta (Exemplo) |
| :-------------------------------- | :-------------------- | :------------------- |
| **Taxa de Abandono (Age Gating)** | 5-15%                 | < 8%                 |
| **Tempo Médio de Verificação**    | 15-45 segundos        | < 20 segundos        |
| **Taxa de Falsos Negativos**      | < 0.5%                | < 0.1%               |
| **Taxa de Falsos Positivos**      | < 3%                  | < 1%                 |
| **Taxa de Sucesso na 1ª Tentativa**| 85-95%                | > 92%                |
| **Custo por Verificação (CPV)**   | R$ 0.80 - R$ 5.00     | R$ 1.50              |

---

## Erros Comuns

1.  **Verificação Inadequada ao Risco**: Usar apenas autodeclaração para venda de produtos de alto risco (ex: álcool, tabaco).
    *   **Como evitar**: Implementar métodos progressivamente mais robustos conforme o risco. Para alto risco, utilize verificação de documentos com biometria facial e prova de vida. Para baixo risco, autodeclaração pode ser aceitável, mas sempre com aviso legal claro.
2.  **Armazenamento Excessivo ou Inseguro de Dados**: Reter imagens de documentos ou dados biométricos diretamente nos servidores da empresa sem necessidade legal ou medidas de segurança adequadas.
    *   **Como evitar**: Priorizar provedores de IDV que processam e retêm dados sensíveis em conformidade com as leis, devolvendo apenas o status de verificação e a data de nascimento validada. Se for essencial reter, anonimizar, criptografar e aplicar controles de acesso estritos.
3.  **Não Considerar Múltiplas Jurisdições**: Implementar um único padrão de verificação de idade para operações em diferentes países com leis e idades mínimas distintas.
    *   **Como evitar**: Desenvolver uma arquitetura flexível que permita configurar as regras de verificação (idade mínima, método) por país ou região, usando geolocalização para aplicar a regra correta.
4.  **Experiência do Usuário (UX) Pobre**: Um processo de verificação de idade complexo, demorado ou com muitas etapas pode frustrar o usuário e aumentar a taxa de abandono.
    *   **Como evitar**: Otimizar o fluxo para ser o mais intuitivo e rápido possível. Fornecer instruções claras, feedback instantâneo e opções de suporte. Testar a usabilidade com usuários reais.

---

## Dicas Avançadas

1.  **Verificação Contínua e Contextual**: Em vez de uma única verificação no registro, implementar verificações contextuais. Por exemplo, re-verificar a idade se o usuário tentar comprar um produto de risco mais alto do que o previamente acessado, ou após um período de inatividade prolongado. Utilize sinais comportamentais ou de dispositivo como gatilhos para reavaliação de risco.
2.  **Uso de IA para Detecção de Fraudes e Anomalías**: Implementar soluções de machine learning que analisam padrões de dados e metadados (IP, dispositivo, comportamento de navegação) durante a verificação para identificar tentativas de fraude (ex: uso de VPN para burlar geolocalização, repetição de documentos falsos).
3.  **Privacy-Preserving Age Verification (PPAV)**: Explorar tecnologias como Zero-Knowledge Proofs (ZKP) onde a verificação de idade pode ocorrer sem revelar a data de nascimento exata do usuário. O sistema apenas confirma se o usuário é "maior ou menor que X anos" (ex: "maior de 18") sem expor o dado sensível. Isso aumenta drasticamente a privacidade.
4.  **Integração com Ecossistemas de Identidade Digital**: Conectar o sistema de verificação a plataformas de identidade digital governamentais (ex: gov.br no Brasil, eID na UE) ou privadas confiáveis. Isso pode simplificar o processo para o usuário (single sign-on de identidade) e aumentar a confiabilidade da verificação, reduzindo a necessidade de upload de documentos.
5.  **Abordagem em Camadas (Layered Approach)**: Combinar diferentes métodos de verificação para criar um sistema mais robusto. Por exemplo, começar com autodeclaração, e apenas para acessos ou compras de alto risco, escalar para verificação de documento com biometria. Isso otimiza a UX para a maioria dos usuários, enquanto mantém a segurança onde é mais crítica.