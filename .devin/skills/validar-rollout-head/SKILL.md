---
name: validar-rollout-head
description: Head valida canário em produção com métricas discovery — favo 04
argument-hint: "<id>"
agent: builder-lead
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/validacao-head*.md)
---

@colmeia/04-construcao/modelo-rollout.md
@colmeia/02-discovery/capacidades-tools.md

ID: **$ARGUMENTS**

1. Ler `rollout-state.yaml` — fase canario
2. Head fornece ou MCP coleta: funil, tempo, dead/rage, cohort, VOC — **segmento canário vs controle**
3. Gerar `validacao-head-$1.md` com veredito: APROVAR_EXPANSAO | ITERAR | ROLLBACK
4. Não inventar métricas
5. Parar → `/grill-me $1 rollout-head`
