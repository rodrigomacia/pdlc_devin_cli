---
name: pipeline-validar
description: "Alias de /ci-validar — CI segregado (retrocompat)"
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
    - Write(colmeia/04-construcao/_iniciativas/**)
---

@colmeia/04-construcao/modelo-ci-cd.md
@colmeia/04-construcao/modelo-pipeline.md

**Alias:** comportamento idêntico a `/ci-validar`.

ID: **$ARGUMENTS**

1. Executar fluxo de `ci-validar` (CI apenas — sem CD)
2. Gerar `ci-status-{id}.md` (e opcionalmente `pipeline-status-{id}.md` como cópia)
3. Parar → `/grill-me {id} ci` ou `pipeline`
