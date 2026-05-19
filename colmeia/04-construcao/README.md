---
favo: 04-construcao
versao: 2.1
status: estavel
upstream:
  - ../03-experimentacao/gates.md
downstream:
  - ../05-operacao/README.md
skill_primaria: spec-funcional
---

# Favo 04 — Construção (SDD)

## Função no ciclo

**Specification-Driven Development:** da feature story à entrega em produção, com o Head de Produto no controle de **o quê** e **para quem** — sem conhecimento técnico.

| Fase | O Head faz | O Devin faz |
|------|------------|-------------|
| Especificar | Aprova `resumo-head.md` | Spec funcional, NFR, técnica, tarefas |
| Construir | — | Implementa código no monorepo |
| Qualidade | — | **`/review-pr`** antes de CI/CD |
| CI | Lê semáforo CI (`ci-status`) | Build artefato por `commit_hash` — **sem deploy** |
| CD | Lê `cd-status-head` por ambiente | Sandbox → Homolog (SV/mock) → Produção (**hash**) |
| Produção | Valida canário com KPIs discovery | Rollout segmentado + expansão ou rollback |

**Pré-requisito:** Gate 03 `scale` + `validacao_real: confirmada` na feature.

## Modelos

| Doc | Conteúdo |
|-----|----------|
| [modelo-sdd.md](./modelo-sdd.md) | Camadas de spec e sequência |
| [modelo-monorepo.md](./modelo-monorepo.md) | Nativo + React SSG + BFF Go + AWS multi-região |
| [modelo-ci-cd.md](./modelo-ci-cd.md) | **CI × CD segregados** · Sandbox · Homolog (SV/mock) · Produção (hash) |
| [modelo-pipeline.md](./modelo-pipeline.md) | CI (detalhe estágios) |
| [modelo-rollout.md](./modelo-rollout.md) | Cliente a cliente |

Config: [`colmeia/_config/construcao-monorepo.md`](../_config/construcao-monorepo.md)

## Skills (ordem de referência)

| # | Skill | Função |
|---|-------|--------|
| 1 | `/spec-funcional` | Spec em linguagem de negócio |
| 2 | `/spec-nao-funcional` | SLO, segurança, regulação |
| 3 | `/spec-tecnica` | Mapeamento monorepo (agents) |
| 4 | `/decompor-tarefas` | Tarefas → entregável código |
| 5 | `/implementar-tarefa` | Implementação + testes |
| 6 | **`/review-pr`** | Parecer PR — **antes de CI/CD** |
| 7 | `/ci-validar` | CI — artefato `commit_hash` |
| 8 | `/prep-release` | Plano release + rollout |
| 9 | `/cd-promover` | CD — `sandbox` \| `homolog` \| `producao` |
| 10 | `/cd-status` | Status ambientes para o Head |
| 11 | `/rollout-canario` | 1º segmento |
| 12 | `/validar-rollout-head` | Decisão Head com métricas produção |
| 13 | `/rollout-expandir` \| `/rollout-rollback` | Expansão ou rollback |
| — | `/pipeline-validar` | Alias de `/ci-validar` |
| — | `/rollout-status` | Consulta status (negócio) |

Grill-me: `spec-funcional`, `tarefas`, `gate-04-pre`, `ci`, `cd-homolog`, `rollout-head`, `release`, `gate-04`.

## Documentos

[fluxo.md](./fluxo.md) · [gates.md](./gates.md) · [artefatos.md](./artefatos.md) · [agentes.md](./agentes.md)
