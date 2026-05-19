---
name: sync-okr-plataforma
description: Pull ou push na Plataforma OKR (OKR, KR, KPI, 4 metas)
argument-hint: "<id> <pull|push>"
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

@colmeia/01-contexto-estrategico/modelo-okr.md
@colmeia/01-contexto-estrategico/capacidades-tools.md
@colmeia/_config/okr-plataforma.md

Iniciativa: **$1** | Modo: **$2** (`pull` ou `push`)

### pull
- Invocar MCP conforme config (`okr.read_tree`, `okr.read_node`)
- Salvar snapshot em `_iniciativas/$1/plataforma-snapshot.yaml` (estrutura mínima: ids, níveis, 4 metas)
- Não inventar nós ausentes na API

### push
- Ler `okr-cascata.yaml` aprovado pelo auditor
- `okr.upsert_objective`, `okr.upsert_kr`, `okr.upsert_kpi`, `okr.link_parent`
- Atualizar `sync-okr-log.md` e `plataforma_ref` nos nós

Se MCP indisponível: dry-run em `sync-okr-log.md` + flag `OKR-SYNC-01`.
