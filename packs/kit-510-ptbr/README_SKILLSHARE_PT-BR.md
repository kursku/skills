# Guia para Iniciantes: Kit 510+ com Skillshare

**Language / Idioma:** [English (Main README)](../../README.md) · Português (PT-BR)

Este guia foi escrito para quem esta comecando agora.
Objetivo: em poucos passos, voce instala o kit, testa um skill e entende como manter tudo funcionando.

Mapa geral de explicacoes do repositorio: `docs/SKILL_EXPLANATIONS_PT-BR.md`.

---

## Usando no Claude.ai sem instalar nada

Se voce usa o Claude.ai no navegador, nao precisa do `skillshare`. Baixe o arquivo `.skill` direto e envie para o seu Projeto.

**Passo a passo:**

1. Acesse a lista de skills por categoria:
   - [Frontend](../../frontend/) — design, animacoes, acessibilidade
   - [Backend](../../backend/) — banco de dados, APIs
   - [Data & AI](../../data-ai/) — LLMs, avaliacao de modelos, agentes
   - [Tooling](../../tooling/) — ferramentas, CLIs, produtividade
   - [Workflow (GSD)](../../workflow/) — gerenciamento de projetos e fases
   - [Core](../../core/) — comunicacao interna e uso geral

2. Clique em **Download** na skill que quiser.

3. No Claude.ai, abra seu Projeto e va em **Configuracoes**.

4. Clique em **Add content** e faca o upload do arquivo `.skill`.

5. Pronto. A skill esta ativa no seu Projeto.

**Dica:** suba de 10 a 40 skills por projeto, agrupadas por contexto (ex.: Marketing, Operacoes, Vendas).

---

## O que e este kit?

Pacote de skills em portugues para marketing, operacoes e automacao.

Estrutura principal:
- `00-utilitarios-tecnicos`: integracao, automacao, seguranca e engenharia.
- `00-utilitarios-negocio`: suporte, pesquisa e contexto de negocio.
- `01` a `16`: trilhas por tema (copy, email, funis, ads, SEO, financeiro etc).

## Qual caminho escolher? (guia rapido)

Use esta tabela para decidir por onde comecar:

| Se seu objetivo principal e... | Comece com... | Comando base |
|---|---|---|
| Crescer redes sociais e conteudo | `01-conteudo-copy` + `09-redes-sociais` | Ver caminho `Social Media` |
| Rodar anuncios e melhorar ROI | `04-anuncios-trafego` + `15-analytics-dados` | Ver caminho `Trafego Pago` |
| Estruturar atendimento e consultoria | `10-clientes-consultoria` + `11-operacoes-sistemas` + `00-utilitarios-negocio` | Ver caminho `Consultoria e Atendimento` |

Se estiver em duvida, comece por `Social Media` (mais facil para primeiros resultados).

## Antes de comecar

Voce precisa de:
1. `skillshare` instalado.
2. Um projeto onde quer usar os skills.
3. Este repositorio clonado localmente.

## Inicio rapido (10 minutos)

No terminal, dentro do seu projeto:

```bash
skillshare init -p --targets "claude"
skillshare install ~/Downloads/skills/packs/kit-510-ptbr -p --all --force
skillshare sync -p
```

Pronto. Agora os skills do kit estao disponiveis no projeto.

## Primeiro teste (recomendado)

Escolha um skill simples e faca um pedido direto no chat do seu agente.

Exemplo de prompt:

```text
Use o skill "social-media-calendar" para montar um calendario de 30 dias para Instagram.
```

## Instalacao por partes (mais leve)

Se nao quiser tudo de uma vez, instale so algumas trilhas:

```bash
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/01-conteudo-copy -p --all --force
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/00-utilitarios-tecnicos -p --all --force
skillshare sync -p
```

## Caminhos iniciais (por perfil)

Se voce for iniciante, escolha um caminho e comece por ele.

### 1) Social Media (conteudo + redes)

Indicado para quem cria calendario, posts e estrategia social.

```bash
skillshare init -p --targets "claude"
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/01-conteudo-copy -p --all --force
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/09-redes-sociais -p --all --force
skillshare sync -p
```

Prompt inicial sugerido:

```text
Use os skills de conteudo e redes para criar um plano de 30 dias com 4 posts por semana para Instagram e LinkedIn.
```

### 2) Trafego Pago (anuncios + metricas)

Indicado para quem roda Meta Ads, Google Ads e quer melhorar performance.

```bash
skillshare init -p --targets "claude"
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/04-anuncios-trafego -p --all --force
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/15-analytics-dados -p --all --force
skillshare sync -p
```

Prompt inicial sugerido:

```text
Use os skills de anuncios e analytics para montar um plano de campanha com objetivo de leads e estrutura de monitoramento semanal.
```

### 3) Consultoria e Atendimento (clientes + operacao)

Indicado para freelancers, agencias e consultores com foco em relacionamento e entrega.

```bash
skillshare init -p --targets "claude"
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/10-clientes-consultoria -p --all --force
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/11-operacoes-sistemas -p --all --force
skillshare install ~/Downloads/skills/packs/kit-510-ptbr/00-utilitarios-negocio -p --all --force
skillshare sync -p
```

Prompt inicial sugerido:

```text
Use os skills de consultoria e operacoes para criar um fluxo de onboarding de cliente com checklist, cronograma de 30 dias e modelo de follow-up.
```

## Comandos do dia a dia

Verificar atualizacoes:

```bash
skillshare check -p
```

Atualizar tudo e sincronizar:

```bash
skillshare update --all -p
skillshare sync -p
```

## Problemas comuns

### 1. Skill nao aparece no agente

Rode novamente:

```bash
skillshare sync -p --force
```

### 2. Erro de symlink no Windows

Use modo copia:

```bash
skillshare target claude --mode copy -p
skillshare sync -p --force
```

### 3. Instalacao muito pesada

Nao instale o kit inteiro. Comece por 1 ou 2 trilhas (ex.: `01-conteudo-copy`, `09-redes-sociais`).

## Glossario rapido

- `-p`: modo projeto (recomendado para times e repositorios).
- `sync`: envia os skills da origem para os alvos configurados.
- `target`: ferramenta destino (ex.: claude).
- `--force`: ignora confirmacoes e sobrescreve quando necessario.

## Usando no Claude.ai (web)

No Claude.ai do navegador, o fluxo e diferente:
- `skillshare` nao sincroniza direto no Claude.ai.
- Voce pode enviar arquivos `.skill` (download direto) ou `SKILL.md` manualmente.

**Opcao 1 — Download direto (recomendado):**
1. Baixe os arquivos `.skill` pelas listas de categoria acima.
2. Crie um Projeto no Claude.ai (ex.: "Marketing").
3. Em Configuracoes do Projeto, clique em **Add content** e envie os `.skill` baixados.
4. Adicione uma instrucao fixa do projeto (modelo abaixo).

**Opcao 2 — Upload manual de SKILL.md:**
1. Crie um Projeto no Claude.ai (ex.: "Marketing").
2. Envie os `SKILL.md` das trilhas que voce quer usar.
3. Envie tambem arquivos de apoio importantes (templates/referencias).
4. Adicione uma instrucao fixa do projeto (modelo abaixo).
5. Nos prompts, diga explicitamente qual skill usar.

### Instrucao sugerida para o Projeto no Claude.ai

Copie este texto em "Project instructions":

```text
Voce deve priorizar os skills enviados neste projeto.
Quando eu pedir uma tarefa, primeiro identifique qual skill e mais adequado.
Explique rapidamente qual skill foi escolhido e execute usando o estilo e as regras do SKILL.md correspondente.
Se faltar contexto, faca no maximo 3 perguntas curtas antes de executar.
```

### Checklist de upload (Claude.ai)

Para cada trilha que voce subir:
1. Envie o `SKILL.md`.
2. Envie arquivos de apoio citados no skill (ex.: templates, referencias).
3. Evite enviar material que nao sera usado no curto prazo.

Exemplo minimo para comecar (Marketing):
- `01-conteudo-copy/.../SKILL.md`
- `09-redes-sociais/.../SKILL.md`
- `00-utilitarios-negocio/customer-support/SKILL.md`

Exemplo:

```text
Use o skill "email-subject-lines" dos arquivos do projeto para criar 20 assuntos de email para campanha de reativacao.
```

Boas praticas no Claude.ai:
- Suba poucos skills por projeto (10 a 40).
- Organize por contexto (Marketing, Operacoes, Vendas).
- Atualize uploads quando o repositorio mudar.

Rotina recomendada de manutencao:
1. Semanal: revisar quais skills estao sendo usados de verdade.
2. Quinzenal: remover uploads sem uso e adicionar os necessarios.
3. Mensal: atualizar os skills enviados com base no repositorio git.

## Observacao sobre nomes

A pasta foi renomeada para `composição`, mas o nome interno do skill pode continuar como `composio` no frontmatter por compatibilidade.
