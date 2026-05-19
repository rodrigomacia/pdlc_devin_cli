---
name: spec-funcional
description: Spec funcional + resumo-head a partir de feature stories — favo 04 SDD
argument-hint: "<id>"
agent: spec-funcional-writer
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
  - grep
  - glob
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**)
---

@colmeia/04-construcao/modelo-sdd.md
@colmeia/04-construcao/artefatos.md

ID: **$ARGUMENTS**

1. Gate 03 — decisão **`scale`** em `decisao-experimentos.md`; abortar se iterate/kill/defer
2. `feature-$1.md` com `validacao_real: confirmada` (EXP-04 se pendente)
3. Ler `historias.yaml` em favo 02
4. Gerar `spec-funcional-$1.md` + `resumo-head.md` (template artefatos)
5. Linguagem de cliente — sem API, sem stack
6. Parar → `/grill-me $1 spec-funcional`
