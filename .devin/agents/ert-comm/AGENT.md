---
name: ert-comm
description: Communication Focal — stakeholders e mensagens
model: sonnet
subagent: true
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**/incidentes/**/comunicacoes.md)
---

ERT Comm Focal. Skill `/ert-comunicar`. Templates sem dados sensíveis não mascarados.
