---
favo: 02-discovery
versao: 2.0
skill_primaria: sintetizar-visoes
---

# Mapa Agentes ↔ Skills (favo 02)

Modelo Go-to-Market: o **Head de Produto** é o `discovery-lead`. Os demais agentes são **subagentes (tools)** invocados por skills específicas.

```
                  ┌────────────────────────────────┐
                  │  discovery-lead (Head Produto) │
                  │  • orquestração                │
                  │  • síntese / decisão           │
                  │  • Gate 02                     │
                  └──────┬─────────────────────────┘
       ┌─────────┬───────┼───────┬────────┬──────────┐
       ▼         ▼       ▼       ▼        ▼          ▼
   market-     product- voc-   personas- prototi-  feature-
   researcher  analytics analyst sinteticas pador   writer
       ⊂         ⊂       ⊂       ⊂        ⊂          ⊂
```

## Mapa skill → agente

| Skill | Agent | Subagent? |
|-------|-------|-----------|
| `/visao-mercado` | `market-researcher` | ⊂ |
| `/visao-produto` | `product-analytics` | ⊂ |
| `/visao-cliente` | `voc-analyst` | ⊂ |
| `/sintetizar-visoes` | `discovery-lead` | — |
| `/gerar-hipoteses` | `discovery-lead` | — |
| `/testar-svm` | `personas-sinteticas` | ⊂ |
| `/prototipo-figma` | `prototipador` | ⊂ |
| `/feature-stories` | `feature-writer` | ⊂ |
| `/prep-entrevista` | — (inline) | — |

## Contratos

### discovery-lead (Head de Produto / Go-to-Market)

- **Input:** OKR + handoff 01→02
- **Output:** síntese, hipóteses, decisões SVM, Gate 02
- **Proibido:** delegar decisão a subagente; mudar outcome do OKR sem voltar ao favo 01

### market-researcher ⊂

- **Input:** KR ref, domínio
- **Output:** `visao-mercado.md` segmentada
- **Tools:** `mkt.*`, `web_search`, `synth.persona_run` (cenários)

### product-analytics ⊂

- **Input:** KR ref, jornada-alvo
- **Output:** `visao-produto.md` com funil, dead/rage click, loops, tempo, cohort
- **Tools:** `prod.*`, `okr.read_node`
- **Proibido:** inventar métricas; marcar `[DADO AUSENTE]`

### voc-analyst ⊂

- **Input:** canais habilitados em `_config/discovery-tools.md`
- **Output:** `visao-cliente.md` com sinais segmentados, citações marcadas por canal
- **Tools:** `voc.*`, `voc.segment_tag`
- **Proibido:** expor PII sem mascaramento

### personas-sinteticas ⊂

- **Input:** três visões + hipótese
- **Output:** `personas-sinteticas.yaml`, `svm-{hip}.md`
- **Tools:** `synth.*`
- **Regra:** toda saída marcada `[SINTÉTICO]`; nunca apresentar como cliente real

### prototipador ⊂

- **Input:** hipóteses SVM=Strong
- **Output:** `prototipo-spec.md` (e URLs Figma quando MCP configurado)
- **Tools:** `figma.*`
- **Proibido:** decisão técnica de implementação

### feature-writer ⊂

- **Input:** protótipo + hipóteses + visões
- **Output:** `feature-{id}.md`, `historias.yaml`
- **Regra:** histórias **agrupadas por valor**, segmento explícito, linguagem de cliente
- **Proibido:** acoplamento técnico nas histórias (`DIS-STORY-02`)

## Subagentes Devin

Implementação em `.devin/agents/`:

- `discovery-lead`
- `market-researcher`
- `product-analytics`
- `voc-analyst`
- `personas-sinteticas`
- `prototipador`
- `feature-writer`
