---
name: ert-registrar
description: Logger — registra evento na timeline do incidente
argument-hint: "<id> <ref> <evento>"
agent: ert-logger
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**/incidentes/**/timeline.md)
---

@colmeia/05-operacao/modelo-ert.md

ID: **$1** | Ref: **$2** | Evento: **$3** (ou corpo na sessão)

Append linha em `timeline.md` — UTC, agent, evento, evidência.
