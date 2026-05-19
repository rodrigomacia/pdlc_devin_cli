---
name: governanca-check
description: Checklist de governança configurável (subagente)
argument-hint: "<id> <favo-01-05>"
agent: guardiao-governanca
subagent: true
allowed-tools:
  - read
  - grep
  - glob
---

@colmeia/_agentes-transversais/guardiao-governanca.md

Iniciativa: **$1** | Favo: **$2**

Ler `colmeia/_config/governanca.md` se existir.
Ler artefatos em `colmeia/*/_iniciativas/$1/` relevantes ao favo.

Tabela requisito × aplicável × status. Sem contexto de produto embutido no repo.
