# Perguntas Frequentes (FAQ)

**Tem duvidas?** Voce nao esta sozinho! Aqui estao as respostas para as perguntas mais comuns sobre Skills para Claude.

---

## Perguntas Gerais

### O que sao "skills" exatamente?

Skills sao arquivos de instrucao especializados que ensinam assistentes de IA a lidar com tarefas especificas. Pense nelas como modulos de conhecimento especializado que sua IA pode carregar sob demanda.
**Analogia simples:** Assim como voce consultaria diferentes especialistas (um advogado, um medico, um mecanico), essas skills permitem que sua IA se torne especialista em diferentes areas quando voce precisar.

### Preciso instalar todas as 700+ skills?

**Nao!** Quando voce clona o repositorio, todas as skills ficam disponiveis, mas sua IA so carrega quando voce invoca explicitamente com `@nome-da-skill`.
E como ter uma biblioteca — todos os livros estao la, mas voce so le os que precisa.
**Dica:** Use os [Starter Packs](BUNDLES.md) para instalar apenas o que combina com sua funcao.

### Qual a diferenca entre Bundles e Workflows?

- **Bundles** sao recomendacoes curadas agrupadas por funcao ou dominio.
- **Workflows** sao playbooks de execucao ordenados para resultados concretos.

Use bundles quando estiver decidindo *quais skills* incluir. Use workflows quando precisar de *execucao passo a passo*.

Comece por:
- [BUNDLES.md](BUNDLES.md)
- [WORKFLOWS.md](WORKFLOWS.md)

### Quais ferramentas de IA funcionam com essas skills?

- **Claude Code** (CLI da Anthropic)
- **Gemini CLI** (Google)
- **Codex CLI** (OpenAI)
- **Cursor** (AI IDE)
- **Antigravity IDE**
- **OpenCode**
- **GitHub Copilot** (suporte parcial via copiar e colar)

### Essas skills sao gratuitas?

**Sim!** Este repositorio esta licenciado sob a Licenca MIT.

- Gratuito para uso pessoal
- Gratuito para uso comercial
- Voce pode modificar como quiser

### As skills funcionam offline?

Os arquivos das skills ficam armazenados localmente no seu computador, mas seu assistente de IA precisa de conexao com a internet para funcionar.

---

## Seguranca e Confianca (Atualizacao V4)

### O que significam os rotulos de risco?

Classificamos as skills para voce saber o que esta rodando:

- **Safe (Branco/Azul)**: Somente leitura, planejamento ou skills inofensivas.
- **Risk (Vermelho)**: Skills que modificam arquivos (deletam), usam scanners de rede ou executam acoes destrutivas. **Use com cautela.**
- **Official (Roxo)**: Mantidas por vendors confiaveis (Anthropic, DeepMind, etc.).

### Essas skills podem hackear meu computador?

**Nao.** Skills sao arquivos de texto. Porem, elas _instruem_ a IA a executar comandos. Se uma skill disser "delete todos os arquivos", uma IA obediente pode tentar fazer isso.
_Sempre verifique o rotulo de risco e revise o codigo._

---

## Instalacao e Configuracao

### Onde devo instalar as skills?

O caminho universal que funciona com a maioria das ferramentas e `.agent/skills/`.

**Usando npx:** `npx antigravity-awesome-skills` (ou `npx github:sickn33/antigravity-awesome-skills` se aparecer erro 404).

**Usando git clone:**

```bash
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

**Caminhos por ferramenta:**

- Claude Code: `.claude/skills/`
- Gemini CLI: `.gemini/skills/`
- Codex CLI: `.codex/skills/`
- Cursor: `.cursor/skills/` ou raiz do projeto

**Para Claude Code (fluxo recomendado):** Personalizar > Habilidades > Upload do SKILL.md

### Funciona no Windows?

**Sim**, mas algumas skills "Official" usam **symlinks** que o Windows lida mal por padrao.
Clone o git com:

```bash
git clone -c core.symlinks=true https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

Ou habilite o "Modo de Desenvolvedor" nas Configuracoes do Windows.

### Como atualizo as skills?

Navegue ate o diretorio de skills e puxe as ultimas alteracoes:

```bash
cd .agent/skills
git pull origin main
```

---

## Usando Skills

> **Para um guia completo com exemplos, veja [USAGE.md](USAGE.md)**

### Como invoco uma skill?

Use o simbolo `@` seguido do nome da skill:

```bash
@brainstorming me ajude a desenhar um app de tarefas
```

### Posso usar varias skills de uma vez?

**Sim!** Voce pode invocar multiplas skills:

```bash
@brainstorming me ajude a desenhar isso, depois use @writing-plans para criar uma lista de tarefas.
```

### Como sei qual skill usar?

1. **Navegue pelo catalogo**: Confira o [Catalogo de Skills](../CATALOG.md).
2. **Busque**: `ls skills/ | grep "palavra-chave"`
3. **Pergunte para sua IA**: "Quais skills voce tem para testes?"

---

## Solucao de Problemas

### Meu assistente de IA nao reconhece as skills

**Possiveis causas:**

1. **Caminho de instalacao errado**: Verifique a documentacao da sua ferramenta. Tente `.agent/skills/`.
2. **Precisa reiniciar**: Reinicie sua IA/IDE depois de instalar.
3. **Erro de digitacao**: Voce digitou `@brain-storming` em vez de `@brainstorming`?

### Uma skill da conselho incorreto ou desatualizado

Por favor [abra uma issue](https://github.com/sickn33/antigravity-awesome-skills/issues)!
Inclua:

- Qual skill
- O que deu errado
- O que deveria acontecer

---

## Contribuicao

### Sou novo em open source. Posso contribuir?

**Com certeza!** Recebemos iniciantes de bracos abertos.

- Corrija erros de digitacao
- Adicione exemplos
- Melhore a documentacao
  Confira [CONTRIBUTING.md](../CONTRIBUTING.md) para instrucoes.

### Meu PR falhou na verificacao "Quality Bar". Por que?

A V4 introduziu controle de qualidade automatizado. Sua skill pode estar sem:

1. Uma `description` valida.
2. Exemplos de uso.
   Rode `python3 scripts/validate_skills.py` localmente para verificar antes de fazer push.

### Posso atualizar uma skill "Official"?

**Nao.** Skills oficiais (em `skills/official/`) sao espelhadas dos vendors. Abra uma issue em vez disso.

---

## Dicas Pro

- Comece com `@brainstorming` antes de construir qualquer coisa nova
- Use `@systematic-debugging` quando travar num bug
- Experimente `@test-driven-development` para melhor qualidade de codigo
- Explore `@skill-creator` para criar suas proprias skills

**Ainda com duvidas?** [Abra uma discussao](https://github.com/sickn33/antigravity-awesome-skills/discussions) e vamos te ajudar!
