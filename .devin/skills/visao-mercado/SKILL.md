---
name: visao-mercado
description: Constrói Visão de Mercado segmentada — favo 02
argument-hint: "<id>"
agent: market-researcher
subagent: true
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
  - web_search
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/02-discovery/_iniciativas/**/visao-mercado.md)
    - Write(colmeia/02-discovery/_iniciativas/**/sinais-mercado/**)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/02-discovery/artefatos.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS**

1. Validar Gate 01: existe OKR em `colmeia/01-contexto-estrategico/_iniciativas/$1/`; senão, parar
2. Ler `kr_ref` alvo do discovery (do handoff 01→02 ou input do operador)
3. Carregar segmentos de `colmeia/_config/discovery-tools.md`
4. Preencher `colmeia/02-discovery/_iniciativas/$1/visao-mercado.md` (template em `artefatos.md`):
   - Tendências, concorrência, pesquisa secundária
   - Cenários sintéticos (marcar `[SINTÉTICO]`)
   - Implicações para KR/KPI
5. Toda linha taggeada por segmento
6. Dado indisponível → `[DADO AUSENTE]`; nunca inventar
