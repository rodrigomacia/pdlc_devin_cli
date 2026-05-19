---
name: curar-contexto
description: Handoff entre favos (máx. 7 docs listados)
argument-hint: "<de> <para> <id>"
model: swe
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Write(colmeia/_handoffs/**)
---

@colmeia/_agentes-transversais/curador-contexto.md

Favo origem: **$1** | Destino: **$2** | ID: **$3**

1. Listar artefatos existentes em `_iniciativas/$3/` dos favos envolvidos
2. Máximo 7 paths no pacote
3. Decisões fechadas (não reabrir)
4. Lacunas `[FORNECER]`
5. Skills recomendadas para favo destino (de `catalogo-skills.md`)

Salvar: `colmeia/_handoffs/handoff-$1-$2-$3.md`

Não copiar conteúdo de produto — só índice e metadados.
