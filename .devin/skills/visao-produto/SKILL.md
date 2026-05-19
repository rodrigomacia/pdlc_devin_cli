---
name: visao-produto
description: Constrói Visão de Produto (funil, dead/rage click, loops, tempo, cohort) — favo 02
argument-hint: "<id>"
agent: product-analytics
subagent: true
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/02-discovery/_iniciativas/**/visao-produto.md)
    - Write(colmeia/02-discovery/_iniciativas/**/sinais-produto/**)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/02-discovery/artefatos.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS**

1. Validar Gate 01 — OKR existe; senão, parar
2. Carregar `kr_ref`, jornada-alvo, segmentos
3. Coletar via tools (`prod.*`) ou aceitar dump do operador:
   - Funil de conversão (etapas, taxa, drop)
   - Tempo em jornada (p50, p90) por etapa
   - Jornada em loop (% reentrada, padrão)
   - Dead click (tela + área + volume)
   - Rage click (tela + elemento + volume)
   - Cohort de retenção (D1/D7/D30/D90)
   - Drop-off por canal/device
4. Toda métrica taggeada por segmento
5. Escrever `colmeia/02-discovery/_iniciativas/$1/visao-produto.md` (template em `artefatos.md`)
6. Dado indisponível → `[DADO AUSENTE]`; nunca inventar números
