---
name: decidir-experimento
description: Consolida decisões e roteia scale→04 ou iterate/kill→02
argument-hint: "<id>"
agent: experiment-lead
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/03-experimentacao/_iniciativas/**)
    - Write(colmeia/02-discovery/_iniciativas/**/feature-*.md)
---

@colmeia/03-experimentacao/gates.md
@colmeia/03-experimentacao/artefatos.md
@colmeia/00-nucleo/modelo-experimentacao-discovery.md

ID: **$ARGUMENTS**

1. Ler `experimento-*.md` em favo 03
2. Gerar `decisao-experimentos.md` com coluna **Próximo favo** e **Handoff sugerido**
3. Para cada decisão **`scale`**:
   - Atualizar `02-discovery/_iniciativas/$ARGUMENTS/feature-$ARGUMENTS.md` → `validacao_real: confirmada`
   - Recomendar: `/curar-contexto 03 04 $ARGUMENTS`
4. Para **`iterate`**, **`pivot`**, **`kill`**:
   - Recomendar: `/curar-contexto 03 02 $ARGUMENTS` + skills favo 02 indicadas
   - **Não** handoff 03→04
5. Parecer Gate 03 + `/grill-me $ARGUMENTS decisao-exp` + `/grill-me $ARGUMENTS gate-03`

Decisões: scale, iterate, pivot, kill, defer
