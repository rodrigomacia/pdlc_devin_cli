---
name: insight-para-discovery
description: Fecha loop operação → discovery — favo 05
argument-hint: "<id>"
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**)
---

@colmeia/05-operacao/artefatos.md
@colmeia/05-operacao/fluxo.md

ID: **$ARGUMENTS**

1. Ler `metricas-review-*.md` e `postmortem-*.md` em favo 05 `_iniciativas/$ARGUMENTS/`
2. Gerar `insights-discovery.md` — oportunidades com tag evidência ops
3. Sem evidência: `[SEM EVIDÊNCIA OPS]`
4. Recomendar: `/curar-contexto 05 02 $ARGUMENTS` e atualizar visões em 02 — `/visao-produto $ARGUMENTS` e/ou `/visao-cliente $ARGUMENTS` seguidos de `/sintetizar-visoes $ARGUMENTS`

Não inventar oportunidades de produto.
