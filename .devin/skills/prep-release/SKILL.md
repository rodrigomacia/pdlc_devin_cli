---
name: prep-release
description: Plano de release + rollout — após CI verde, antes do canário
argument-hint: "<id> [versao]"
agent: builder-lead
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**)
---

@colmeia/04-construcao/artefatos.md
@colmeia/04-construcao/modelo-rollout.md
@colmeia/04-construcao/modelo-ci-cd.md

ID: **$1** | Versão: **$2**

Pré: Gate 03 scale · CI verde · review-pr aprovado

1. Ler `ci-status`, `deploy-manifest-{hash}`, `decisao-experimentos.md`
2. `release-plan.md`, `rollout-plan-$1.md`, `changelog-*.md`
3. Documentar `commit_hash` e segmento canário proposto (Head confirma no rollout)
4. `/grill-me $1 release`

Ordem: **depois** de `/ci-validar` + grill `ci` · **antes** de `/cd-promover` e do canário.
