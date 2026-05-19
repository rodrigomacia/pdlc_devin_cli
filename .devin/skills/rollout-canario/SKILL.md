---
name: rollout-canario
description: Rollout canário — primeiro segmento de clientes — favo 04
argument-hint: "<id> [segmento]"
agent: rollout-coordinator
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/rollout*)
---

@colmeia/04-construcao/modelo-rollout.md
@colmeia/_config/construcao-monorepo.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS** | Segmento: **$2** ou Head define na sessão

1. Pré: CI verde + CD homolog `tests_ok` + `/cd-promover $1 producao {hash}` executado
2. `cd-state.yaml` → `producao.deploy_ref` = commit_hash (ROL-04, CD-03)
3. Head define segmento canário (linguagem negócio)
4. Atualizar `rollout-plan-$1.md`, `rollout-state.yaml` fase=canario
5. Executar via rollout provider (config) ou documentar passos `[FORNECER]`
6. Informar Head: observar KPIs listados no plano
