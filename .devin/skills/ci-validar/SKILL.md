---
name: ci-validar
description: CI segregado — build artefato por commit_hash, sem deploy — favo 04
argument-hint: "<id> [commit_hash]"
agent: pipeline-guardian
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/ci-status*.md)
    - Write(colmeia/04-construcao/_iniciativas/**/deploy-manifest*.yaml)
    - Write(colmeia/04-construcao/_iniciativas/**/cd-state.yaml)
---

@colmeia/04-construcao/modelo-ci-cd.md
@colmeia/04-construcao/modelo-pipeline.md
@colmeia/_config/construcao-monorepo.md

ID: **$1** | Hash: **$2** ou obter do CI/PR

1. Consultar workflow **CI** (não CD) via config MCP ou operador
2. Validar artefato taggeado com **commit_hash** (CI-01 se ausente)
3. Gerar `ci-status-$1.md` + `deploy-manifest-{hash}.yaml`
4. Inicializar/atualizar `cd-state.yaml` com `commit_hash` e `ci_status: verde`
5. **Não** deployar em nenhum ambiente nesta skill
6. Parar → `/grill-me $1 ci` (alias: `pipeline`)
