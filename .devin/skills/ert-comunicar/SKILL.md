---
name: ert-comunicar
description: Communication Focal — mensagens stakeholders
argument-hint: "<id> <ref>"
agent: ert-comm
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**/incidentes/**/comunicacoes.md)
---

@colmeia/05-operacao/modelo-ert.md

ID: **$1** | Ref: **$2**

1. Ler visao-360 e status do commander
2. Atualizar `comunicacoes.md` — audiência, canal, mensagem, status
3. Linguagem institucional; PII mascarada
