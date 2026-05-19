---
favo: 01-contexto-estrategico
versao: 1.1
skill_primaria: desdobrar-okr
---

# Mapa Agentes ↔ Skills (favo 01)

| Skill | Agent | Subagent? |
|-------|-------|-----------|
| `/draft-okr` | `estrategista-okr` | — |
| `/desdobrar-okr` | `desdobrador-okr` | — |
| `/sync-okr-plataforma` | `sync-okr` | — |
| `/auditar-okr` | `auditor-okr` | ⊂ |
| scanning (opcional) | `scanner-ambiente` (inline em `draft-okr` / `auditar-okr` — sem skill dedicada) | ⊂ |

## desdobrador-okr

- Lê `modelo-okr.md` + árvore pai (pull ou operador)
- Produz `okr-cascata.yaml` com pesos e 4 metas por KR/KPI
- Invoca validação `mapeador-metricas` se ordem de metas ambígua

## sync-okr

- Implementa contrato MCP em `_config/okr-plataforma.md`
- `pull` antes do draft; `push` após auditor
- Não push se `OKR-MET-*` ou `OKR-CAS-*` abertos

## mapeador-metricas (subagente — invocado por `desdobrar-okr` / `auditar-okr`, sem skill `/mapeador-metricas`)

- Valida baseline ≤ target ≤ roof ≤ moonshot (ou inverso)
- Saída: tabela por KR com status OKR-MET-02

Paths: `.devin/agents/`
