---
name: desdobrar-okr
description: Desdobra OKR em cascata L3/L4 com KR, KPI e 4 metas
argument-hint: "<id> [L4]"
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
@colmeia/01-contexto-estrategico/artefatos.md
@colmeia/_config/okr-plataforma.md

Iniciativa: **$1** | Desdobrar L4: **$2** (opcional)

Pré-requisitos:
1. `okr-{ciclo}.md` em `_iniciativas/$1/`
2. Árvore pai: resultado de `/sync-okr-plataforma $1 pull` ou dados do operador

Gerar/atualizar:
- `okr-cascata.yaml` (canônico)
- Seção cascata em `okr-*.md`

Validar pesos e OKR-CAS-*. Recomendar `/auditar-okr $1` e depois `/sync-okr-plataforma $1 push`.
