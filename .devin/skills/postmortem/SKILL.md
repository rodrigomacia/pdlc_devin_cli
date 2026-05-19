---
name: postmortem
description: Postmortem blameless — favo 05
argument-hint: "<id> <ref-incidente>"
agent: operador-lead
subagent: true
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Write(colmeia/05-operacao/_iniciativas/**)
---

@colmeia/05-operacao/artefatos.md

ID: **$1** | Ref: **$2**

Operador fornece: timeline, impacto, causa. Skill estrutura em `postmortem-$2.md`.

Ligar a KR/OKR se operador indicar — não inventar impacto em métricas.
