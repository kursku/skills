# Primeiros Passos com Skills para Claude (V6.5.0)

**Chegou agora? Este guia vai turbinar seu AI Agent em 5 minutos.**

> **Confuso sobre o que fazer depois da instalacao?** Confira o [**Guia Completo de Uso**](USAGE.md) para explicacoes detalhadas e exemplos!

---

## O Que Sao "Skills"?

AI Agents (como **Claude Code**, **Gemini**, **Cursor**) sao inteligentes, mas nao tem conhecimento especifico sobre suas ferramentas.
**Skills** sao manuais de instrucao especializados (arquivos markdown) que ensinam sua IA a executar tarefas especificas com perfeicao, sempre.

**Analogia:** Sua IA e um estagiario brilhante. **Skills** sao os POPs (Procedimentos Operacionais Padrao) que transformam ele num Engenheiro Senior.

---

## Inicio Rapido: Os "Starter Packs"

Nao entre em panico com as 954+ skills. Voce nao precisa de todas de uma vez.
Temos **Starter Packs** curados para voce comecar imediatamente.

Voce **instala o repositorio completo uma vez** (npx ou clone); Starter Packs sao listas curadas para ajudar voce a **escolher quais skills usar** por funcao (ex: Web Wizard, Hacker Pack) — nao sao uma forma diferente de instalar.

### 1. Instale o Repositorio

**Opcao A — npx (mais facil):**

```bash
npx antigravity-awesome-skills
```

Isso clona para `~/.gemini/antigravity/skills` por padrao. Use `--cursor`, `--claude`, `--gemini`, `--codex`, ou `--kiro` para instalar para uma ferramenta especifica, ou `--path <dir>` para um local customizado. Execute `npx antigravity-awesome-skills --help` para detalhes.

Se aparecer erro 404, use: `npx github:sickn33/antigravity-awesome-skills`

**Opcao B — git clone:**

```bash
# Universal (funciona com a maioria dos agents)
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

### 2. Escolha Seu Perfil

Encontre o bundle que combina com sua funcao (veja [BUNDLES.md](BUNDLES.md)):

| Perfil                  | Nome do Bundle | O Que Tem Dentro?                                  |
| :---------------------- | :------------- | :------------------------------------------------- |
| **Desenvolvedor Web**   | `Web Wizard`   | React Patterns, dominio de Tailwind, Frontend Design |
| **Engenheiro de Seguranca** | `Hacker Pack`  | OWASP, Metasploit, Metodologia de Pentest        |
| **Gerente / PM**        | `Product Pack` | Brainstorming, Planejamento, SEO, Estrategia       |
| **Tudo**                | `Essentials`   | Clean Code, Planejamento, Validacao (O Basico)     |

---

## Bundles vs Workflows

Bundles e workflows resolvem problemas diferentes:

- **Bundles** = conjuntos curados por funcao (o que escolher).
- **Workflows** = playbooks passo a passo (como executar).

Comece com bundles em [BUNDLES.md](BUNDLES.md), depois rode um workflow de [WORKFLOWS.md](WORKFLOWS.md) quando precisar de execucao guiada.

Exemplo:

> "Use **@antigravity-workflows** e rode `ship-saas-mvp` para minha ideia de projeto."

---

## Como Usar uma Skill

Depois de instalado, basta conversar com sua IA naturalmente.

### Exemplo 1: Planejando uma Feature (**Essentials**)

> "Use **@brainstorming** para me ajudar a desenhar um novo fluxo de login."

**O que acontece:** A IA carrega a skill de brainstorming, faz perguntas estruturadas e produz uma especificacao profissional.

### Exemplo 2: Verificando Seu Codigo (**Web Wizard**)

> "Rode **@lint-and-validate** neste arquivo e corrija os erros."

**O que acontece:** A IA segue regras rigorosas de linting definidas na skill para limpar seu codigo.

### Exemplo 3: Auditoria de Seguranca (**Hacker Pack**)

> "Use **@api-security-best-practices** para revisar meus endpoints de API."

**O que acontece:** A IA audita seu codigo contra os padroes OWASP.

---

## Ferramentas Suportadas

| Ferramenta      | Status          | Caminho                                                               |
| :-------------- | :-------------- | :-------------------------------------------------------------------- |
| **Claude Code** | Suporte Total   | `.claude/skills/`                                                     |
| **Gemini CLI**  | Suporte Total   | `.gemini/skills/`                                                     |
| **Codex CLI**   | Suporte Total   | `.codex/skills/`                                                      |
| **Kiro CLI**    | Suporte Total   | Global: `~/.kiro/skills/` - Workspace: `.kiro/skills/`                |
| **Kiro IDE**    | Suporte Total   | Global: `~/.kiro/skills/` - Workspace: `.kiro/skills/`                |
| **Antigravity** | Nativo          | Global: `~/.gemini/antigravity/skills/` - Workspace: `.agent/skills/` |
| **Cursor**      | Nativo          | `.cursor/skills/`                                                     |
| **OpenCode**    | Suporte Total   | `.agents/skills/`                                                     |
| **AdaL CLI**    | Suporte Total   | `.adal/skills/`                                                       |
| **Copilot**     | Somente Texto   | Copiar e colar manualmente                                            |

---

## Confianca e Seguranca (Novidade na V4)

Classificamos as skills para voce saber o que esta rodando:

- **Official**: Mantidas pela Anthropic/Google/Vendors (Alta Confianca).
- **Safe**: Skills da comunidade que nao sao destrutivas (Somente leitura/Planejamento).
- **Risk**: Skills que modificam sistemas ou executam testes de seguranca (Somente Uso Autorizado).

_Confira o [Catalogo de Skills](../CATALOG.md) para a lista completa._

---

## FAQ

**P: Preciso instalar todas as 954+ skills?**
R: Voce clona o repositorio inteiro uma vez; sua IA so _le_ as skills que voce invoca (ou que sao relevantes), entao fica leve. **Starter Packs** em [BUNDLES.md](BUNDLES.md) sao listas curadas para ajudar voce a descobrir as skills certas para sua funcao — nao mudam a forma de instalar.

**P: Posso criar minhas proprias skills?**
R: Sim! Use a skill **@skill-creator** para criar as suas.

**P: E de graca?**
R: Sim, Licenca MIT. Open Source para sempre.

---

## Proximos Passos

1. [Explore os Bundles](BUNDLES.md)
2. [Veja Exemplos Reais](EXAMPLES.md)
3. [Contribua com uma Skill](../CONTRIBUTING.md)
