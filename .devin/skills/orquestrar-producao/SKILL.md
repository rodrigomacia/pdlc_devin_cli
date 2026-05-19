---
name: orquestrar-producao
description: Orquestra ciclo — favo atual, lacunas, próximas skills
argument-hint: "<id-iniciativa>"
triggers:
  - user
allowed-tools:
  - read
  - grep
  - glob
---

@colmeia/00-nucleo/catalogo-skills.md
@colmeia/00-nucleo/ciclo-completo.md
@colmeia/00-nucleo/modelo-experimentacao-discovery.md
@colmeia/00-nucleo/indice-colmeia.md
@AGENTS.md

Iniciativa: **$ARGUMENTS**

1. Varra `colmeia/*/_iniciativas/$ARGUMENTS/` e `colmeia/_handoffs/*$ARGUMENTS*`
2. Determine favo atual (01–05) pelos artefatos e gates
3. Compare com cada `colmeia/{favo}/gates.md`
4. Liste skills na ordem de `ciclo-completo.md` / matriz do catálogo
5. **Roteamento favo 03:** se `decisao-experimentos.md` tem `scale` → favo 04; `iterate`/`pivot`/`kill` → favo 02 (handoff 03→02)
6. **Roteamento favo 04:** não sugerir `/ci-validar` ou `/cd-promover` sem `/review-pr` aprovado; feature com `validacao_real: confirmada`
7. Liste inputs `[FORNECER]` — **não invente contexto de produto**

Saída: formato em `colmeia/00-nucleo/orquestrador-producao.md`
