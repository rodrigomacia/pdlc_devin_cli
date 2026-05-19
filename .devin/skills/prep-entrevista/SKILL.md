---
name: prep-entrevista
description: Roteiro de entrevista de oportunidade — favo 02
argument-hint: "<id> [oportunidade]"
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Write(colmeia/02-discovery/_iniciativas/**)
---

@colmeia/02-discovery/artefatos.md

ID: **$1** | Foco: **$2** (ou primeira oportunidade da OST)

Ler OST em `colmeia/02-discovery/_iniciativas/$1/ost-*.md`

Gerar `colmeia/02-discovery/_iniciativas/$1/roteiros/roteiro-YYYY-MM-DD.md`:
- Objetivo da sessão (oportunidade)
- O que não perguntar (viés de solução)
- Roteiro comportamental past-tense
- Critérios de recrutamento: `[FORNECER pelo operador]`

Sem persona ou produto inventado.
