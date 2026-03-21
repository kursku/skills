# Public Catalog Strategy

## Objetivo

Tratar este repositório público como catálogo principal, canônico e compartilhável de skills, mantendo qualquer material operacional ou de backup como apoio secundário fora da experiência principal.

## Problema Atual

Hoje o repositório mistura quatro papéis:

- catálogo público para usuários finais
- estrutura técnica das skills-fonte
- material operacional de composição, importação e manutenção
- coleções em `packs/` que ainda aparecem como se fossem estrutura principal

Isso gera confusão no README, na navegação e no histórico de branches, porque a raiz do repositório não representa sozinha o catálogo final publicado.

## Modelo Recomendado

### 1. Repositório público

Deve concentrar:

- catálogo publicado para consumo
- navegação simples e estável
- README orientado ao usuário final
- histórico principal que você compartilha com outras pessoas
- taxonomia pública final das skills

### 2. Repositório privado ou operacional

Deve concentrar:

- scripts de importação e release
- documentação operacional
- experimentos, auditorias e material de manutenção
- automações e backups de trabalho
- qualquer staging temporário de migração que não precise ficar exposto ao público

## Leitura Correta da Estrutura Atual

- `dist/` = saída publicada final e navegação pública real
- raiz técnica (`backend/`, `frontend/`, `tooling/`, etc.) = organização das skills-fonte
- `packs/` = mecanismo legado de composição, útil durante a transição, mas inadequado como estrutura pública principal

## Direção de Migração

### Fase 1

Corrigir a documentação pública:

- README aponta para `dist/`
- README deixa explícito que a raiz técnica não é a navegação final
- README rebaixa `packs/` para papel transitório
- repo passa a se apresentar como catálogo público principal

### Fase 2

Separar a operação e a autoria interna:

- mover scripts, material operacional e backstage para repo privado quando fizer sentido
- manter o público focado no catálogo e no que precisa ser compartilhado
- parar de apresentar `packs/` como centro conceitual do repositório

### Fase 3

Migrar a taxonomia real:

- redistribuir todas as skills hoje mantidas em `packs/` para categorias públicas finais equivalentes
- garantir que skills PT-BR e importadas coexistam dentro da taxonomia pública oficial
- reduzir ou remover `packs/` do repositório público

## Critério de Decisão

Se um arquivo existe para:

- navegar, baixar, entender e consumir skills: ele pertence ao catálogo público principal
- compor, importar, auditar, gerar ou manter skills internamente: ele pertence à operação secundária/privada

## Decisao Estrutural

No repositório público, `packs/` não deve ser tratado como a estrutura oficial do catálogo.

A direção correta é:

- categorias públicas finais como estrutura principal
- `packs/` como etapa de transição
- posterior redistribuição das skills para a taxonomia pública definitiva
