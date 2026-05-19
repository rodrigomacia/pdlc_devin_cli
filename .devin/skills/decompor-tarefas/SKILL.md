---
name: decompor-tarefas
description: Decompõe specs em tarefas (entregável código) — favo 04
argument-hint: "<id>"
agent: task-decomposer
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/tarefas.yaml)
---

@colmeia/04-construcao/modelo-sdd.md
@colmeia/04-construcao/artefatos.md

ID: **$ARGUMENTS**

1. Specs funcional + técnica presentes
2. Gerar `tarefas.yaml` — 100% histórias cobertas
3. Parar → `/grill-me $1 tarefas`
