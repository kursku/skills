---
name: testimonial-release
description: "Testimonial Release — Skill especializada para testimonial release"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Testimonial Release

Esta skill capacita o Claude a gerar, revisar e gerenciar documentos de Termo de Autorização de Uso de Depoimento (Testimonial Release) em conformidade com as leis de privacidade e direitos de imagem.

---

## Keywords

Testimonial Release, Termo de Autorização, Direito de Imagem, LGPD, GDPR, Marketing de Conteúdo, Consentimento Informado, Uso de Dados Pessoais, Declaração de Uso, Propriedade Intelectual, Compliance Jurídico, Marketing Digital.

---

## Quick Start

1.  **Coleta Inicial de Dados**: Solicitar nome completo, CPF e e-mail do depoente para registro e contato.
2.  **Definição do Escopo de Uso**: Delimitar claramente as mídias (ex: Instagram, site institucional), o período (ex: 3 anos) e o território (ex: Brasil) para o depoimento.
3.  **Geração do Termo de Autorização**: Utilizar o template pré-configurado, preenchendo as informações coletadas e o escopo definido.
4.  **Envio para Assinatura Eletrônica**: Submeter o documento gerado para assinatura digital do depoente via plataforma segura (ex: Clicksign, DocuSign).
5.  **Arquivamento e Registro**: Salvar o termo assinado em diretório seguro e registrar seus metadados (data de assinatura, expiração, escopo) em sistema de gestão.

---

## Core Workflows

### Workflow 1: Elaboração e Conformidade de um Termo de Autorização de Depoimento

Este workflow detalha a criação de um Testimonial Release, assegurando sua validade jurídica e conformidade com a LGPD e o direito de imagem.

1.  **Coleta de Dados Primários do Depoente**:
    *   **Ação**: Obter as informações essenciais do indivíduo que fornecerá o depoimento.
    *   **Exemplo Concreto**: Para o cliente "Maria Silva", solicitar "Nome Completo: Maria Silva", "CPF: 123.456.789-00", "E-mail: maria.silva@email.com", "Endereço: Rua das Palmeiras, 150, Bloco B, Apto 201, São Paulo, SP".
    *   **Justificativa**: Estes dados são cruciais para a identificação do titular e para a validade do documento.

2.  **Definição do Escopo de Uso e Mídia**:
    *   **Ação**: Especificar detalhadamente como o depoimento será utilizado, por quanto tempo e onde.
    *   **Exemplo Concreto**: "Uso em Marketing Digital (Facebook, Instagram, LinkedIn, YouTube, Blog e Site institucional da Empresa X)", "Período de Uso: 5 anos a partir da data de assinatura", "Território de Abrangência: Brasil", "Formato: Texto, Imagem (fotografia), Vídeo (curta duração)".
    *   **Justificativa**: A especificidade do escopo é um pilar do consentimento informado e evita usos indevidos que poderiam gerar litígios.

3.  **Geração do Rascunho do Termo**:
    *   **Ação**: Preencher o template padrão de Testimonial Release com as informações coletadas e o escopo definido.
    *   **Exemplo Concreto**: Inserir "Maria Silva" como "DEPOENTE", "Empresa XYZ Ltda." como "CONTRATANTE", e as descrições de mídia, prazo e território nas cláusulas pertinentes do termo modelo.
    *   **Justificativa**: Padronização garante que todas as cláusulas essenciais estejam presentes e agiliza o processo.

4.  **Revisão de Conformidade com LGPD/GDPR e Direito de Imagem**:
    *   **Ação**: Verificar se o termo contém todas as cláusulas exigidas pelas leis de privacidade e direitos da personalidade.
    *   **Exemplo Concreto**: Assegurar que o termo contenha: (a) menção ao Art. 7º, I da LGPD (base legal do consentimento); (b) finalidade específica ("promoção de [produto/serviço Y] da Empresa X"); (c) direito de revogação do consentimento a qualquer momento; (d) identificação do controlador de dados (Empresa X) e, se aplicável, do Encarregado de Dados (DPO).
    *   **Justificativa**: A não conformidade pode resultar em multas pesadas e danos à reputação.

5.  **Envio para Assinatura e Armazenamento Seguro**:
    *   **Ação**: Enviar o termo finalizado para assinatura eletrônica do depoente e, após assinado, armazená-lo de forma segura e acessível.
    *   **Exemplo Concreto**: Utilizar a plataforma Clicksign para o envio. Após a assinatura, armazenar o PDF assinado em um diretório criptografado no Google Drive com acesso restrito e registrar a data de assinatura e expiração em uma planilha de controle de consentimentos.
    *   **Justificativa**: A assinatura eletrônica confere validade jurídica e o armazenamento seguro é uma exigência da LGPD.

### Workflow 2: Gestão e Revogação de Consentimento de Depoimento

Este workflow aborda a manutenção dos termos de autorização e o procedimento para lidar com solicitações de revogação de consentimento, garantindo a rápida remoção do conteúdo.

1.  **Registro Centralizado dos Termos de Autorização**:
    *   **Ação**: Manter um sistema ou banco de dados atualizado com todos os termos de depoimento ativos.
    *   **Exemplo Concreto**: Criar uma tabela em um CRM ou planilha (Google Sheets/Excel) com as colunas: "ID do Termo", "Nome do Depoente", "CPF do Depoente", "E-mail de Contato", "Data de Assinatura", "Data de Expiração", "Escopo de Uso Detalhado", "Link para Termo Assinado", "Status (Ativo/Revogado)". Ex: `ID: TR-001; Depoente: João Costa; Data Ass: 2023-03-10; Data Exp: 2028-03-09; Escopo: Redes Sociais e Site; Status: Ativo`.
    *   **Justificativa**: Essencial para o monitoramento de prazos e conformidade, evitando uso de consentimentos expirados ou revogados.

2.  **Monitoramento de Prazos e Escopo**:
    *   **Ação**: Implementar alertas para os termos que estão próximos da expiração ou que atingiram o limite do escopo de uso.
    *   **Exemplo Concreto**: Configurar um lembrete automático no Google Calendar ou no sistema de CRM para disparar um aviso 60 dias antes da `Data de Expiração` de cada termo, com a mensagem: "Termo TR-001 (João Costa) expira em 2028-03-09. Avaliar renovação ou remoção de conteúdo".
    *   **Justificativa**: Previne o uso indevido de depoimentos após o vencimento do consentimento, reduzindo riscos jurídicos.

3.  **Processamento de Solicitação de Revogação de Consentimento**:
    *   **Ação**: Estabelecer um protocolo claro para receber, registrar e agir sobre pedidos de revogação.
    *   **Exemplo Concreto**:
        *   **Recebimento**: O depoente "João Costa" envia um e-mail para `privacidade@suaempresa.com.br` solicitando a revogação do consentimento.
        *   **Registro**: O e-mail é registrado no sistema de tickets interno, com a tag "Revogação de Consentimento - Depoimento".
        *   **Ação Imediata (48h)**: A equipe de marketing é notificada para suspender imediatamente qualquer nova veiculação do depoimento de João Costa em todas as plataformas.
        *   **Ação de Conformidade (7 dias)**: Remover todas as instâncias existentes do depoimento (vídeos do YouTube, posts de Instagram, artigos de blog, imagens do site) e instruir parceiros (agências de publicidade) a fazer o mesmo.
    *   **Justificativa**: A LGPD exige que a revogação seja processada de forma rápida e efetiva, garantindo o direito do titular.

4.  **Notificação e Comprovação da Revogação**:
    *   **Ação**: Informar o depoente sobre a conclusão do processo de revogação e manter um registro da ação.
    *   **Exemplo Concreto**: Enviar um e-mail de confirmação a João Costa com o assunto "Sua solicitação de revogação de consentimento foi processada", descrevendo as ações tomadas (ex: "Todos os materiais com seu depoimento foram removidos de nossas plataformas e canais de parceiros"). Anexar, se possível, capturas de tela ou relatórios de remoção como prova.
    *   **Justificativa**: Transparência com o titular dos dados e criação de evidências de conformidade para auditorias futuras.

---

## Templates

### Termo de Autorização de Uso de Depoimento (Completo - LGPD)

```
TERMO DE AUTORIZAÇÃO DE USO DE DEPOIMENTO E IMAGEM

Pelo presente instrumento particular, de um lado:

**AUTORIZANTE/DEPOENTE:** [Nome Completo do Depoente], [Nacionalidade], [Estado Civil], [Profissão], portador(a) do RG nº [Número do RG] e CPF nº [Número do CPF], residente e domiciliado(a) na [Endereço Completo do Depoente, incluindo CEP], doravante denominado(a) simplesmente **DEPOENTE**;

E de outro lado:

**AUTORIZADA/CONTRATANTE:** [Nome Completo ou Razão Social da Empresa Contratante], pessoa jurídica de direito privado, inscrita no CNPJ sob o nº [Número do CNPJ], com sede na [Endereço Completo da Empresa, incluindo CEP], neste ato representada na forma de seu Estatuto/Contrato Social, doravante denominada simplesmente **CONTRATANTE**.

As partes acima qualificadas têm entre si, justo e contratado o presente Termo de Autorização de Uso de Depoimento e Imagem, que se regerá pelas cláusulas e condições seguintes:

**CLÁUSULA PRIMEIRA – DO OBJETO DA AUTORIZAÇÃO**

1.1. O DEPOENTE, de livre e espontânea vontade, pelo presente Termo, AUTORIZA a CONTRATANTE a utilizar seu nome, imagem (fotografia, vídeo, ou qualquer representação visual), voz e depoimento (em formato de texto ou áudio/vídeo), fornecidos em [Data do Depoimento, ex: 15 de janeiro de 2024], para fins de [Finalidade Específica do Uso, ex: promoção e divulgação dos serviços de 'consultoria financeira' da CONTRATANTE].

1.2. A presente autorização abrange a veiculação do material em todas as mídias, eletrônicas ou impressas, incluindo, mas não se limitando a: websites (ex: www.empresaexemplo.com.br), redes sociais (ex: Instagram, Facebook, LinkedIn, YouTube), e-mail marketing, blogs, materiais promocionais (folders, banners) e campanhas publicitárias.

**CLÁUSULA SEGUNDA – DO PRAZO E ABRANGÊNCIA**

2.1. A autorização concedida pelo DEPOENTE vigorará pelo prazo de [Prazo de Uso, ex: 5 (cinco) anos] a contar da data de assinatura do presente Termo.

2.2. A abrangência territorial para a utilização do depoimento e imagem é [Abrangência Territorial, ex: Nacional (território brasileiro)].

**CLÁUSULA TERCEIRA – DA GRATUIDADE OU REMUNERAÇÃO**

3.1. A presente autorização é concedida a título [Escolher: gratuito e não oneroso OU oneroso, mediante pagamento de R$ [Valor] conforme acordado entre as partes, devidamente quitado em [Data do Pagamento]].

3.2. O DEPOENTE declara, para todos os fins de direito, que não possui quaisquer direitos ou compensações a serem reclamados da CONTRATANTE em relação ao uso do seu depoimento, nome, imagem e voz, nos termos e condições aqui estabelecidos.

**CLÁUSULA QUARTA – DA PROTEÇÃO DE DADOS PESSOAIS (LGPD)**

4.1. O DEPOENTE está ciente de que seus dados pessoais (nome, imagem, voz e depoimento), conforme Art. 7º, I da Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD), serão tratados pela CONTRATANTE para a finalidade específica descrita na Cláusula Primeira.

4.2. A CONTRATANTE compromete-se a tratar os dados pessoais do DEPOENTE em conformidade com a LGPD, garantindo a segurança e a confidencialidade das informações.

4.3. O DEPOENTE poderá, a qualquer momento, revogar o presente consentimento, bem como exercer os direitos previstos na LGPD (acesso, correção, eliminação, portabilidade, etc.) mediante solicitação formal através do e-mail [E-mail do Encarregado de Dados/DPO ou Canal de Privacidade, ex: privacidade@empresaexemplo.com.br]. A revogação do consentimento implicará na imediata interrupção do uso do depoimento e remoção dos materiais em até 7 (sete) dias úteis a partir da solicitação.

**CLÁUSULA QUINTA – DAS DECLARAÇÕES**

5.1. O DEPOENTE declara que o depoimento concedido é verdadeiro, espontâneo e reflete sua experiência real com os serviços/produtos da CONTRATANTE, não havendo qualquer tipo de coação ou manipulação.

5.2. O DEPOENTE declara ter plena capacidade civil para assinar o presente Termo e que leu e compreendeu todas as suas cláusulas e condições.

**CLÁUSULA SEXTA – DO FORO**

6.1. Fica eleito o foro da Comarca de [Cidade/Estado da Sede da Contratante, ex: São Paulo, SP] para dirimir quaisquer dúvidas ou litígios oriundos do presente Termo, com renúncia expressa a qualquer outro, por mais privilegiado que seja.

E por estarem assim justos e contratados, as partes assinam o presente Termo em 2 (duas) vias de igual teor e forma, na presença das duas testemunhas abaixo, para que produza seus efeitos legais.

[Cidade da Assinatura], [Dia] de [Mês] de [Ano].

________________________________________
[Nome Completo do Depoente]
DEPOENTE

________________________________________
[Nome do Representante Legal da Empresa]
[Cargo do Representante Legal]
CONTRATANTE: [Nome Completo ou Razão Social da Empresa Contratante]

**TESTEMUNHAS:**
1. Nome: [Nome Testemunha 1]
   CPF: [CPF Testemunha 1]

2. Nome: [Nome Testemunha 2]
   CPF: [CPF Testemunha 2]
```

### E-mail de Notificação de Revogação de Consentimento Processada

```
Assunto: Sua solicitação de revogação de consentimento foi processada - [Nome da Empresa]

Prezado(a) [Nome do Depoente],

Confirmamos o recebimento e o processamento de sua solicitação de revogação de consentimento para o uso de seu depoimento, imagem e voz, datada de [Data da Solicitação de Revogação].

Conforme sua solicitação e em conformidade com a Lei Geral de Proteção de Dados (LGPD), informamos que todas as ações necessárias para remover seu depoimento e quaisquer materiais associados de nossas plataformas foram concluídas.

Isso inclui, mas não se limita a:
*   Remoção de posts e vídeos de nossas redes sociais (Instagram, Facebook, YouTube, LinkedIn).
*   Remoção de imagens e textos de nosso website institucional ([Endereço do Site, ex: www.empresaexemplo.com.br]) e blog.
*   Instrução a nossos parceiros de marketing e agências de publicidade para cessarem qualquer veiculação do material.

Agradecemos sua colaboração e permanecemos à disposição para quaisquer esclarecimentos adicionais.

Atenciosamente,

Equipe de Privacidade de Dados
[Nome da Empresa]
[E-mail de Contato para Privacidade, ex: privacidade@empresaexemplo.com.br]
[Telefone de Contato (Opcional)]
[Endereço do Site da Empresa]
```

---

## Checklist

-   [x] Consentimento explícito e específico obtido para cada tipo de uso (imagem, voz, texto).
-   [x] Finalidade clara e detalhada do uso do depoimento definida no termo (ex: "para promoção do curso X da empresa Y").
-   [x] Prazo de utilização do depoimento especificado e razoável (ex: 3 anos, 5 anos).
-   [x] Abrangência geográfica de uso do depoimento delimitada (ex: Nacional, América Latina, Global).
-   [x] Cláusula de revogação do consentimento presente e clara, informando como o depoente pode exercê-la.
-   [x] Canais para solicitação de revogação informados ao depoente (ex: e-mail específico, formulário no site).
-   [x] Identificação completa do controlador (empresa) e, se houver, do encarregado de dados (DPO) no termo.
-   [x] Menção expressa à Lei Geral de Proteção de Dados (LGPD) e aos direitos do titular dos dados.
-   [x] Termo assinado por ambas as partes (ou eletronicamente com validade jurídica reconhecida).
-   [x] Armazenamento seguro do termo assinado e dos metadados de consentimento (data de assinatura, expiração, IP).
-   [x] Procedimento interno documentado para gestão de revogações e remoção de conteúdo em todas as plataformas.
-   [x] Processo de monitoramento de expiração de prazos dos termos de autorização em vigor.

---

## Métricas de Referência

| Métrica | Benchmark | Meta |
| :-------------------------------- | :-------- | :----- |
| Taxa de conformidade dos termos | 98% | 100% |
| Tempo médio para processar revogação | 48 horas | 24 horas |
| % de termos com escopo detalhado | 95% | 100% |
| % de depoimentos com consentimento ativo | 90% | 95% |
| % de multas por uso indevido de imagem | 0% | 0% |
| Taxa de renovação de consentimento (se aplicável) | 70% | 85% |

---

## Erros Comuns

1.  **Consentimento Genérico**: **Como evitar**: Em vez de "Autorizo o uso para fins de marketing", especificar "Autorizo o uso de minha imagem e depoimento em vídeo para a campanha 'Histórias de Sucesso' da Empresa X, veiculada no YouTube e Instagram, por um período de 3 anos, com o objetivo de promover o curso de 'Gestão Financeira'".
2.  **Falta de Cláusula de Revogação ou Dificuldade de Exercício**: **Como evitar**: Incluir um parágrafo explícito no termo sobre o direito do titular de revogar o consentimento a qualquer momento e indicar um canal claro e fácil para essa solicitação (ex: "Solicitações de revogação devem ser enviadas para privacidade@empresa.com.br").
3.  **Uso Fora do Escopo ou Após o Prazo**: **Como evitar**: Manter um sistema de controle de validade e escopo para cada termo. Ex: Se um termo autoriza uso apenas em redes sociais por 2 anos, não utilizar o depoimento em uma campanha de TV no 3º ano ou após a data de expiração.
4.  **Armazenamento Inadequado dos Termos Assinados**: **Como evitar**: Utilizar plataformas de gestão documental (DMS) com criptografia, controle de acesso baseado em função (RBAC) e trilhas de auditoria, garantindo a integridade e a rastreabilidade dos termos assinados.
5.  **Não Identificação do Controlador/DPO**: **Como evitar**: O termo deve sempre indicar claramente quem é a empresa que está coletando e utilizando o depoimento (o controlador de dados) e, preferencialmente, o contato do Encarregado de Dados (DPO), conforme exigência da LGPD.

---

## Dicas Avançadas

1.  **Implementação de um Gerenciador de Consentimento Dedicado**: Utilize um sistema de Gerenciamento de Consentimento (CMP) focado em depoimentos, que não apenas armazene os termos, mas também automatize o monitoramento de prazos, dispare alertas de expiração e integre-se a plataformas de marketing para facilitar a remoção ou atualização de conteúdo.
2.  **Segmentação de Termos por Nível de Risco/Visibilidade**: Crie diferentes modelos de Termos de Autorização com cláusulas variadas, dependendo do perfil do depoente (ex: influenciador vs. cliente comum) ou da amplitude da campanha (ex: campanha nacional de TV vs. post em blog). Termos para alto risco/visibilidade podem exigir cláusulas mais robustas e compensação financeira.
3.  **Processo Automatizado de "Sunset" de Depoimentos**: Desenvolva um fluxo automatizado que, ao detectar a expiração de um Termo de Autorização ou a revogação do consentimento, inicie um processo de "sunset" (desativação). Este processo deve incluir a despublicação automática de conteúdo em plataformas digitais e a notificação de equipes internas e parceiros externos para a remoção de materiais.
4.  **Auditoria Contínua de Conteúdo Ativo**: Realize auditorias periódicas (mensais/trimestrais) de todo o conteúdo de marketing ativo que utiliza depoimentos para verificar se cada um possui um Termo de Autorização válido, se o uso está estritamente dentro do escopo e prazo definidos e se o depoente não revogou o consentimento.
5.  **Treinamento Regular da Equipe de Marketing e Vendas**: Garanta que todas as equipes que interagem com depoimentos de clientes recebam treinamento contínuo sobre a importância do Termo de Autorização, os requisitos da LGPD/GDPR e os procedimentos corretos para coleta, uso e gestão desses materiais. Isso minimiza erros na fonte e promove uma cultura de conformidade.
---