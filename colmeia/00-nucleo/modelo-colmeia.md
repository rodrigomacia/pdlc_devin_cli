---
favo: 00-nucleo
versao: 1.0
status: estavel
tags: [modelo, colmeia]
---

# Modelo Colmeia

Organização do framework de **execução** do ciclo de produtação digital.

## Camadas

```
┌─────────────────────────────────────────┐
│  .devin/skills + .devin/agents          │  ← Execução (Devin CLI)
├─────────────────────────────────────────┤
│  colmeia/{favo}/                         │  ← Contrato: fluxo, gates, templates
│    fluxo.md | gates.md | artefatos.md   │
│    agentes.md (mapa skill ↔ subagente)  │
├─────────────────────────────────────────┤
│  colmeia/*/_iniciativas/{id}/           │  ← Runtime (gitignored)
└─────────────────────────────────────────┘
```

## Favo = etapa do ciclo

Cada favo documenta **como executar** a etapa, não **o quê** construir:

| Arquivo | Função |
|---------|--------|
| `README.md` | Escopo do favo, skills, entradas/saídas do processo |
| `fluxo.md` | Passos e invocação de skills |
| `gates.md` | Checklist objetivo de transição |
| `artefatos.md` | Templates vazios (placeholders) |
| `agentes.md` | Mapa agent/subagent → skill |

Não manter `skills.md` separado de competências humanas genéricas — o catálogo de skills está em `00-nucleo/catalogo-skills.md`.

## Feromônios (frontmatter)

```yaml
---
favo: "02-discovery"
versao: 1.0
status: rascunho | estavel
upstream: []
downstream: []
skill_primaria: sintetizar-visoes
---
```

## Hierarquia de execução

```
Orquestrador (/orquestrar-producao)
    ├── Skill de favo (ex: /draft-okr)
    │       └── Subagent (ex: auditor-okr) via agent: ou subagent: true
    └── Transversal (/governanca-check, /curar-contexto)
```

**Regra Devin:** um nível de subagente — skill orquestradora chama skills com `subagent: true`; subagentes não spawnam outros subagentes.

## Mel (artefato) vs. favo (definição)

- **Favo** = código-fonte do processo (versionado)
- **Mel** = output de uma skill para `{id}` (runtime, gitignored)
