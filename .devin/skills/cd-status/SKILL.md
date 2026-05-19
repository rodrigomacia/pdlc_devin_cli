---
name: cd-status
description: Status CI/CD por ambiente em linguagem Head — favo 04
argument-hint: "<id>"
agent: builder-lead
model: sonnet
allowed-tools:
  - read
permissions:
  allow:
    - Read(colmeia/**)
---

@colmeia/04-construcao/modelo-ci-cd.md

ID: **$ARGUMENTS**

1. Ler `ci-status-$1.md`, `cd-state.yaml`, `rollout-state.yaml`
2. Responder na sessão ou atualizar `cd-status-head-$1.md`:
   - Versão (`commit_hash`) única em todos ambientes
   - Sandbox / Homolog / Produção — status em linguagem negócio
   - Próxima decisão do Head
3. Sem jargão: pod, helm, pipeline YAML
