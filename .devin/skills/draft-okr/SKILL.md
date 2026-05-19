---
name: draft-okr
description: Rascunha artefatos favo 01 a partir de inputs do operador
argument-hint: "<id> [core|exploratorio|hibrido]"
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/01-contexto-estrategico/_iniciativas/**)
---

@colmeia/01-contexto-estrategico/artefatos.md
@colmeia/01-contexto-estrategico/fluxo.md
@colmeia/01-contexto-estrategico/gates.md

ID: **$1** | Tipo: **$2** (default: perguntar)

**Antes de escrever**, confirmar com operador ou usar só o que ele colou na sessão:
- Diretriz upstream
- Baselines e definições de métrica
- Ciclo (ex: 2026-Q2)

Criar `colmeia/01-contexto-estrategico/_iniciativas/$1/` e arquivos do template.

**Proibido:** números de métrica inventados; exemplos de domínio; texto de produto genérico filler.

Use `[FORNECER]` e `[BASELINE: fornecer]` onde faltar dado.

Recomendar sequência:
1. `/desdobrar-okr $1`
2. `/auditar-okr $1`
3. `/sync-okr-plataforma $1 push`

Se plataforma configurada, sugerir `/sync-okr-plataforma $1 pull` **antes** do draft.
