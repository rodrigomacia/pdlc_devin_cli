---
favo: 00-nucleo
versao: 4.0
---

# Devin CLI

## Setup rápido

```bash
./scripts/setup-devin-cli.sh
# Edite .devin/config.local.json e colmeia/_config/*.md
devin
/orquestrar-producao {id}
```

Documentação: [`docs/index.html`](../../docs/index.html) · Setup: [`docs/configuracao.html`](../../docs/configuracao.html)

```
.devin/agents/     # 32 agents
.devin/skills/     # 46 skills
colmeia/           # contratos por favo
```

## Agents (seleção)

| ID | Favo |
|----|------|
| `discovery-lead` | 02 (Head GTM) |
| `builder-lead` | 04 (Head GTM construção) |
| `spec-funcional-writer` · `spec-tech-writer` · `implementador` · `pipeline-guardian` · `rollout-coordinator` | 04 ⊂ |
| `ert-lead` · `ert-logger` · `ert-comm` · `ert-sme-produto` · `ert-sme-tech` | 05 ERT |
| `grill-me` | transversal ⊂ |

Lista completa: pastas em `.devin/agents/`

## Skills (46)

Ver [catalogo-skills.md](./catalogo-skills.md)

Destaques favo 04: SDD · **`review-pr` antes de CI** · `ci-validar` · `cd-promover` · rollout canário · `rollout-rollback`

Destaques favo 05 ERT: `ert-abrir` · `ert-comandar` · `ert-registrar` · `ert-comunicar` · `ert-diagnosticar` · `ert-fechar`

Grill-me: [grill-me.md](./grill-me.md) · Fluxo Head: [fluxo-head-produto-devin.html](../../docs/fluxo-head-produto-devin.html)
