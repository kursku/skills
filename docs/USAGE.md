# Guia de Uso: Como Usar as Skills na Pratica

> **Perdido apos a instalacao?** Este guia te mostra exatamente o que fazer, passo a passo.

---

## "Instalei as skills. E agora?"

Otima pergunta! Veja o que aconteceu e o que fazer a seguir:

### O Que Voce Acabou de Fazer

Quando voce baixou e configurou as Skills para Claude, voce:

- **Baixou os arquivos de skills** para o seu computador
- **Deixou tudo disponivel** para o seu assistente de IA
- **NAO ativou todas automaticamente** (elas estao la, esperando voce usar)

Pense nisso como instalar uma caixa de ferramentas. Voce tem todas as ferramentas agora, mas precisa **escolher quais usar** para cada tarefa.

---

## Passo 1: Entendendo os "Bundles" (Isso NAO e Outra Instalacao!)

**Confusao comum:** "Preciso baixar cada skill separadamente?"

**Resposta: NAO!** Veja o que bundles realmente sao:

### O Que Sao Bundles

Bundles sao **listas recomendadas** de skills agrupadas por funcao. Eles ajudam voce a decidir por onde comecar.

**Analogia:**

- Voce instalou uma caixa de ferramentas com centenas de ferramentas (ja feito)
- Bundles sao como **bandejas organizadoras com etiquetas** dizendo: "Se voce e desenvolvedor web, comece com essas 10 ferramentas"
- Voce nao instala bundles — voce **escolhe skills a partir deles**

### O Que Bundles NAO Sao

- Instalacoes separadas
- Comandos de download diferentes
- Algo que precisa ser "ativado"

### Exemplo: O Bundle "Web Wizard"

Quando voce ve o [bundle Web Wizard](BUNDLES.md#-the-web-wizard-pack), ele lista:

- `frontend-design`
- `react-best-practices`
- `tailwind-patterns`
- etc.

Essas sao **recomendacoes** de quais skills um desenvolvedor web deveria experimentar primeiro. Elas ja estao instaladas — voce so precisa **usa-las nos seus prompts**.

---

## Passo 2: Como Usar uma Skill de Verdade

Essa e a parte que merece mais atencao! Veja como usar as skills:

### A Resposta Simples

**Basta mencionar o nome da skill na sua conversa com o assistente de IA.**

### Como Adicionar uma Skill ao Claude

O fluxo para habilitar uma skill no Claude e:

**Personalizar → Habilidades → Upload do SKILL.md**

Depois de fazer o upload, a skill fica disponivel para uso nas suas conversas.

### Diferentes Ferramentas, Diferentes Sintaxes

A sintaxe exata varia por ferramenta, mas sempre e simples:

#### Claude Code (CLI)

```bash
# No seu terminal/chat com o Claude Code:
>> Use @brainstorming to help me design a todo app
```

#### Cursor (IDE)

```bash
# No painel de chat do Cursor:
@brainstorming help me design a todo app
```

#### Gemini CLI

```bash
# Na sua conversa com o Gemini:
Use the brainstorming skill to help me plan my app
```

#### Codex CLI

```bash
# Na sua conversa com o Codex:
Apply @brainstorming to design a new feature
```

> **Dica:** A maioria das ferramentas modernas usa a sintaxe `@nome-da-skill`. Na duvida, tente isso primeiro!

---

## Passo 3: Como Devem Ser Meus Prompts?

Aqui estao **exemplos reais** de bons prompts:

### Exemplo 1: Comecando um Novo Projeto

**Prompt Ruim:**

> "Me ajude a fazer um app de tarefas"

**Prompt Bom:**

> "Use @brainstorming para me ajudar a projetar um app de tarefas com autenticacao de usuario e sincronizacao na nuvem"

**Por que e melhor:** Voce invoca a skill explicitamente e fornece contexto.

---

### Exemplo 2: Revisando Codigo

**Prompt Ruim:**

> "Verifica meu codigo"

**Prompt Bom:**

> "Use @lint-and-validate para verificar `src/components/Button.tsx` em busca de problemas"

**Por que e melhor:** Skill especifica + arquivo especifico = resultados precisos.

---

### Exemplo 3: Auditoria de Seguranca

**Prompt Ruim:**

> "Deixa minha API segura"

**Prompt Bom:**

> "Use @api-security-best-practices para revisar meus endpoints REST em `routes/api/users.js`"

**Por que e melhor:** A IA sabe exatamente quais padroes da skill aplicar.

---

### Exemplo 4: Combinando Multiplas Skills

**Prompt Bom:**

> "Use @brainstorming para projetar um fluxo de pagamento, depois aplique @stripe-integration para implementar"

**Por que e bom:** Voce pode encadear skills em um unico prompt!

---

## Passo 4: Sua Primeira Skill (Tutorial Pratico)

Vamos usar uma skill agora mesmo. Siga estes passos:

### Cenario: Voce quer planejar uma nova funcionalidade

1. **Escolha uma skill:** Vamos usar `brainstorming` (do bundle "Essentials")

2. **Abra seu assistente de IA** (Claude Code, Cursor, etc.)

3. **Digite este prompt:**

   ```
   Use @brainstorming para me ajudar a projetar uma pagina de perfil de usuario para meu app
   ```

4. **Aperte Enter**

5. **O que acontece em seguida:**
   - A IA carrega a skill de brainstorming
   - Ela vai comecar a fazer perguntas estruturadas (uma de cada vez)
   - Ela vai te guiar pelas etapas de entendimento, requisitos e design
   - Voce responde cada pergunta, e ela constroi uma especificacao completa

6. **Resultado:** Voce termina com um documento de design detalhado — sem escrever uma unica linha de codigo!

---

## Passo 5: Escolhendo Suas Primeiras Skills (Conselho Pratico)

Nao tente usar todas as skills de uma vez! Aqui vai uma abordagem sensata:

### Comece com "O Essencial" (5 skills que todo mundo precisa)

1. **`@brainstorming`** - Planeje antes de construir
2. **`@lint-and-validate`** - Mantenha o codigo limpo
3. **`@git-pushing`** - Salve seu trabalho com seguranca
4. **`@systematic-debugging`** - Corrija bugs mais rapido
5. **`@concise-planning`** - Organize tarefas

**Como usar:**

- Antes de escrever codigo novo → `@brainstorming`
- Depois de escrever codigo → `@lint-and-validate`
- Antes de commitar → `@git-pushing`
- Quando travar → `@systematic-debugging`

### Depois Adicione Skills do Seu Perfil (mais 5-10)

Encontre seu perfil em [BUNDLES.md](BUNDLES.md) e escolha 5-10 skills daquele bundle.

**Exemplo para Desenvolvedor Web:**

- `@frontend-design`
- `@react-best-practices`
- `@tailwind-patterns`
- `@seo-audit`

**Exemplo para Engenheiro de Seguranca:**

- `@api-security-best-practices`
- `@vulnerability-scanner`
- `@ethical-hacking-methodology`

### Por Fim, Adicione Skills Sob Demanda (conforme necessidade)

Mantenha o [CATALOG.md](../CATALOG.md) aberto como referencia. Quando precisar de algo especifico:

> "Preciso integrar pagamentos com Stripe"
> → Busque no catalogo → Encontre `@stripe-integration` → Use!

---

## Exemplo Completo: Construindo uma Feature de Ponta a Ponta

Vamos acompanhar um cenario realista:

### Tarefa: "Adicionar um blog ao meu site Next.js"

#### Etapa 1: Planejar (use @brainstorming)

```
Voce: Use @brainstorming para projetar um sistema de blog para meu site Next.js

IA: [Faz perguntas estruturadas sobre requisitos]
Voce: [Responde as perguntas]
IA: [Produz uma especificacao de design detalhada]
```

#### Etapa 2: Implementar (use @nextjs-best-practices)

```
Voce: Use @nextjs-best-practices para criar a estrutura do blog com App Router

IA: [Cria estrutura de arquivos, configura rotas, adiciona componentes]
```

#### Etapa 3: Estilizar (use @tailwind-patterns)

```
Voce: Use @tailwind-patterns para deixar os posts do blog com visual moderno

IA: [Aplica estilizacao com Tailwind e design responsivo]
```

#### Etapa 4: SEO (use @seo-audit)

```
Voce: Use @seo-audit para otimizar o blog para mecanismos de busca

IA: [Adiciona meta tags, sitemaps, dados estruturados]
```

#### Etapa 5: Testar e Deploy

```
Voce: Use @test-driven-development para adicionar testes, depois @vercel-deployment para fazer o deploy

IA: [Cria testes, configura CI/CD, faz deploy na Vercel]
```

**Resultado:** Blog profissional construido com boas praticas, sem precisar pesquisar cada etapa manualmente!

---

## Perguntas Frequentes

### "Qual ferramenta devo usar? Claude Code, Cursor, Gemini?"

**Qualquer uma!** As skills funcionam universalmente. Escolha a ferramenta que voce ja usa ou prefere:

- **Claude Code** - Melhor para workflows no terminal/CLI
- **Cursor** - Melhor para integracao com IDE
- **Gemini CLI** - Melhor para o ecossistema Google
- **Codex CLI** - Melhor para o ecossistema OpenAI

### "Posso ver todas as skills disponiveis?"

Sim! De tres formas:

1. Navegue pelo [CATALOG.md](../CATALOG.md) (lista pesquisavel)
2. Rode `ls ~/.agent/skills/` (se instalou la)
3. Pergunte a sua IA: "Quais skills voce tem para [topico]?"

### "Preciso reiniciar minha IDE depois de instalar?"

Geralmente nao, mas se sua IA nao reconhecer uma skill:

1. Tente reiniciar sua IDE/CLI
2. Verifique se o caminho de instalacao corresponde a sua ferramenta
3. Para o Claude, siga o fluxo: Personalizar → Habilidades → Upload do SKILL.md

### "Posso criar minhas proprias skills?"

Sim! Use a skill `@skill-creator`:

```
Use @skill-creator para me ajudar a criar uma skill personalizada para [sua tarefa]
```

### "E se uma skill nao funcionar como esperado?"

1. Verifique o arquivo SKILL.md da skill diretamente: `~/.agent/skills/[nome-da-skill]/SKILL.md`
2. Leia a descricao para garantir que esta usando corretamente
3. [Abra uma issue](https://github.com/sickn33/antigravity-awesome-skills/issues) com detalhes

---

## Cartao de Referencia Rapida

**Salve isso para consulta rapida:**

| Tarefa                  | Skill para Usar                | Exemplo de Prompt                                                |
| ----------------------- | ------------------------------ | ---------------------------------------------------------------- |
| Planejar nova feature   | `@brainstorming`               | `Use @brainstorming para projetar um sistema de login`           |
| Revisar codigo          | `@lint-and-validate`           | `Use @lint-and-validate em src/app.js`                           |
| Debugar problema        | `@systematic-debugging`        | `Use @systematic-debugging para corrigir erro de login`          |
| Auditoria de seguranca  | `@api-security-best-practices` | `Use @api-security-best-practices nas minhas rotas de API`       |
| Verificar SEO           | `@seo-audit`                   | `Use @seo-audit na minha landing page`                           |
| Componente React        | `@react-patterns`              | `Use @react-patterns para construir um componente de formulario` |
| Deploy do app           | `@vercel-deployment`           | `Use @vercel-deployment para colocar isso em producao`           |

---

## Proximos Passos

Agora que voce entende como usar as skills:

1. **Experimente uma skill agora** - Comece com `@brainstorming` em qualquer ideia que voce tenha
2. **Escolha 3-5 skills** do bundle do seu perfil em [BUNDLES.md](BUNDLES.md)
3. **Salve nos favoritos** o [CATALOG.md](../CATALOG.md) para quando precisar de algo especifico
4. **Experimente um workflow** de [WORKFLOWS.md](WORKFLOWS.md) para um processo completo de ponta a ponta

---

## Dicas para Maximo Aproveitamento

### Dica 1: Comece Toda Feature com @brainstorming

> Antes de escrever codigo, use `@brainstorming` para planejar. Voce vai economizar horas de refatoracao.

### Dica 2: Encadeie Skills na Ordem Certa

> Nao tente fazer tudo de uma vez. Use skills sequencialmente: Planejar → Construir → Testar → Deploy

### Dica 3: Seja Especifico nos Prompts

> Ruim: "Use @react-patterns"
> Bom: "Use @react-patterns para construir um componente de modal com animacoes"

### Dica 4: Referencie Caminhos de Arquivos

> Ajude a IA a focar: "Use @security-auditor em routes/api/auth.js"

### Dica 5: Combine Skills para Tarefas Complexas

> "Use @brainstorming para projetar, depois @test-driven-development para implementar com testes"

---

## Ainda Com Duvidas?

Se algo ainda nao faz sentido:

1. Veja o [FAQ](FAQ.md)
2. Veja os [Exemplos Reais](EXAMPLES.md)
3. [Abra uma Discussao](https://github.com/sickn33/antigravity-awesome-skills/discussions)
4. [Abra uma Issue](https://github.com/sickn33/antigravity-awesome-skills/issues) para nos ajudar a melhorar este guia!

Lembre-se: voce nao esta sozinho! O objetivo deste projeto e tornar os assistentes de IA mais faceis de usar. Se este guia nao ajudou, nos avise para que possamos melhorar.
