# Skills para claude.ai

Skills são módulos de instrução especializada que ensinam o Claude a lidar com tarefas específicas. Pense nelas como conhecimento de especialista que você pode carregar no seu Projeto do claude.ai.

---

## Como instalar no claude.ai

<!-- demo GIF — gerado por scripts/record_install_demo.py -->
![Instalando uma skill no claude.ai](docs/assets/install-demo.gif)

**1. Escolha uma skill nas categorias abaixo e clique em ⬇ Download**

**2. Acesse [claude.ai/customize/skills](https://claude.ai/customize/skills)**

**3. Clique em "Add skill" e faça upload do arquivo `.skill` baixado**

**4. Pronto! A skill está disponível em todos os seus chats e Projetos**

> **Alternativa (Projetos):** Se preferir usar a skill apenas em um Projeto específico, abra o Projeto → Configurações → Add content → faça upload do `.skill`.

---

## claude.ai vs Claude Desktop

| | claude.ai (web) | Claude Desktop / CLI |
|---|---|---|
| **Como instalar** | Upload do `.skill` em [claude.ai/customize/skills](https://claude.ai/customize/skills) | `skillshare install` via terminal |
| **Formato** | Arquivo `.skill` (ZIP renomeado com `SKILL.md`) | Pasta com `SKILL.md` diretamente |
| **Escopo** | Global — disponível em todos os chats e Projetos | Por projeto ou global, conforme config |
| **Atualização** | Re-upload manual | `skillshare update --all` |

Se você usa o **claude.ai no navegador**, siga o passo a passo acima.
Se você usa o **Claude Desktop ou Claude Code**, veja [docs/SKILLSHARE.md](docs/SKILLSHARE.md) para instalar via `skillshare`.

---

## Categorias

### Frontend
Skills para design de interface, animações, acessibilidade e desenvolvimento web.

[Ver skills de Frontend →](./frontend/)

---

### Backend
Skills para banco de dados, APIs e plataformas de servidor.

[Ver skills de Backend →](./backend/)

---

### Data & AI
Skills para projetos com LLMs, avaliação de modelos e arquiteturas de agentes.

[Ver skills de Data & AI →](./data-ai/)

---

### Tooling
Skills para ferramentas de produtividade, CLIs e extensão de capacidades do AI.

[Ver skills de Tooling →](./tooling/)

---

### Workflow (GSD)
Sistema completo de gerenciamento de projetos com milestones, fases e execução paralela.

[Ver skills de Workflow →](./workflow/)

---

### Core
Skills essenciais para comunicação interna e uso geral.

[Ver skills de Core →](./core/)

---

## Contribuindo

Quer criar uma skill ou melhorar uma existente? Abra uma issue ou Pull Request.
