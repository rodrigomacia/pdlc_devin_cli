---
name: ert-diagnosticar
description: SMEs — visão 360 cliente/produto/negócio/tech
argument-hint: "<id> <ref>"
agent: ert-sme-produto
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**/incidentes/**/visao-360.md)
---

@colmeia/05-operacao/modelo-ert.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/04-construcao/modelo-monorepo.md

ID: **$1** | Ref: **$2**

1. **SME Produto** (`ert-sme-produto`): prod.*, voc.*, rollout, feature stories, decisão favo 03
2. **SME Tech** — invocar explicitamente agente **`ert-sme-tech`** (subagente):
   - pipeline, `ci-status`, `cd-state`, `deploy_ref` / `commit_hash`
   - release recente, BFF/apps/infra AWS
3. Consolidar em `visao-360.md` — 5 seções do modelo ERT
4. `[DADO AUSENTE]` se tool indisponível — não inventar métricas
