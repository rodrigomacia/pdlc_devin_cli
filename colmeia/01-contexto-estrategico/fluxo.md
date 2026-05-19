---
favo: 01-contexto-estrategico
versao: 1.1
status: estavel
skill_primaria: desdobrar-okr
---

# Fluxo — Invocação de skills (favo 01)

Modelo de domínio: [modelo-okr.md](./modelo-okr.md) · Tools: [capacidades-tools.md](./capacidades-tools.md)

## Diagrama

```mermaid
flowchart LR
  O[/orquestrar-producao/] --> PULL[/sync-okr pull/]
  PULL --> D[/draft-okr/]
  D --> G1[/grill-me okr-draft/]
  G1 --> DES[/desdobrar-okr/]
  DES --> G2[/grill-me okr-cascata/]
  G2 --> A[/auditar-okr/]
  A --> G3[/grill-me gate-01/]
  G3 --> PUSH[/sync-okr push/]
  PUSH --> GOV[/governanca-check/]
  GOV --> C[/curar-contexto 01 02/]
```

## Passos

| Step | Skill | Pré-condição | Output |
|------|-------|--------------|--------|
| 1 | `/orquestrar-producao {id}` | ID definido | Plano |
| 2 | Config `colmeia/_config/okr-plataforma.md` | MCP da plataforma | — |
| 3 | `/sync-okr-plataforma {id} pull` | Config OK | Árvore pai L0–L2 em contexto |
| 4 | Operador: diretriz, baselines (ou pull da plataforma) | — | — |
| 5 | `/draft-okr {id} {tipo}` | Pull ou diretriz | `okr-{ciclo}.md`, `tese-produto.md` |
| 5b | `/grill-me {id} okr-draft` | Draft OKR | Grill estratégico |
| 6 | `/desdobrar-okr {id}` | Grill okr-draft ≠ BLOQUEAR | `okr-cascata.yaml` |
| 6b | `/grill-me {id} okr-cascata` | Cascata | Pesos e 4 metas |
| 7 | `/auditar-okr {id}` | Grill okr-cascata ≠ BLOQUEAR | Parecer |
| 7b | `/grill-me {id} gate-01` | Parecer auditor | Pronto para discovery? |
| 8 | `/sync-okr-plataforma {id} push` | Grill gate-01 ≠ BLOQUEAR | `sync-okr-log.md`, IDs plataforma |
| 9 | `/governanca-check {id} 01` | Condicional | Checklist |
| 10 | Gate 01 + `/curar-contexto 01 02 {id}` | Push OK | handoff |

## Skills do pilar

| Skill | Função |
|-------|--------|
| `/sync-okr-plataforma` | **Tool** — leitura/escrita na Plataforma OKR |
| `/desdobrar-okr` | **Desdobramento** — cascata L3 (e L4) com pesos e vínculos |
| `/draft-okr` | Narrativa + tese + rascunho markdown |
| `/auditar-okr` | Coerência cascata + baseline/target/roof/moonshot |

## Subagentes

| Agent | Quando |
|-------|--------|
| `scanner-ambiente` | Scanning externo (opcional) |
| `auditor-okr` | `/auditar-okr` |
| `mapeador-metricas` | Validação OKR-MET-* (via auditor ou desdobrar) |

## Falhas

| Situação | Ação |
|----------|------|
| Plataforma indisponível | `desdobrar-okr` só em markdown; marcar `OKR-SYNC-01` pendente |
| KR sem 4 metas | Auditor reprova `OKR-MET-01` |
| Ordem metas inválida | `OKR-MET-02` |
