---
name: spec-nao-funcional
description: Spec não funcional (SLO, segurança, regulação) — favo 04
argument-hint: "<id>"
agent: spec-nfr-writer
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/spec-nfr*.yaml)
---

@colmeia/04-construcao/artefatos.md
@colmeia/_config/construcao-monorepo.md

ID: **$ARGUMENTS**

1. Ler spec-funcional + OKR + `_config/construcao-monorepo.md`
2. Gerar `spec-nfr-$1.yaml` com `resumo_head` em linguagem negócio
3. Incluir metricas_discovery para rollout
