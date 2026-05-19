---
favo: 02-discovery
versao: 2.0
status: estavel
upstream:
  - ../01-contexto-estrategico/gates.md
downstream:
  - ../03-experimentacao/README.md
skill_primaria: sintetizar-visoes
---

# Favo 02 — Discovery

## Função no ciclo

Construir três visões (**Mercado · Produto · Cliente**) ancoradas no OKR, gerar hipóteses, validar com personas sintéticas (**SVM**), materializar em **protótipo Figma** e entregar **feature com histórias segmentadas por valor**.

Modelo operacional: **Head de Produto = Go-to-Market** é dono ponta-a-ponta. Agentes do favo são *tools*, não pessoas em série.

## Modelo e tools

| Doc | Conteúdo |
|-----|----------|
| [modelo-discovery.md](./modelo-discovery.md) | Três visões, SVM, feature stories, códigos |
| [capacidades-tools.md](./capacidades-tools.md) | VOC, analytics, personas sintéticas, Figma |
| [_config/discovery-tools.md](../_config/discovery-tools.md) | Conexões MCP do operador |

## Skills (ordem típica)

```
/visao-mercado {id}
/visao-produto {id}
/visao-cliente {id}
→ /sintetizar-visoes {id}
→ /gerar-hipoteses {id}
→ /testar-svm {id} [hipotese]
→ /prototipo-figma {id}
→ /feature-stories {id}
```

| Skill | Papel |
|-------|-------|
| `/visao-mercado` | Tendências, concorrência, pesquisa, sintéticos de mercado |
| `/visao-produto` | Funil, dead/rage click, jornada em loop, tempo, cohort |
| `/visao-cliente` | VOC: transcrições, reviews, suporte, social, entrevistas |
| `/sintetizar-visoes` | Cruzamento → oportunidades + OST + mapa de evidências |
| `/gerar-hipoteses` | Hipóteses testáveis ligadas a KR/KPI |
| `/testar-svm` | Validação com personas sintéticas (filtro pré-protótipo) |
| `/prototipo-figma` | Spec de protótipo navegável + anotações de hipótese |
| `/feature-stories` | Feature com histórias por valor (entregável Gate 02) |
| `/prep-entrevista` | Roteiro para entrevista estruturada (entra na VOC) |

Após cada etapa de decisão: **`/grill-me {id} {momento}`** — ver [grill-me.md](../00-nucleo/grill-me.md). Obrigatório: `hipoteses`, `feature`, `gate-02`.

## Saídas (runtime)

`colmeia/02-discovery/_iniciativas/{id}/` — ver [README](./_iniciativas/README.md)

## Documentos

[fluxo.md](./fluxo.md) · [gates.md](./gates.md) · [artefatos.md](./artefatos.md) · [agentes.md](./agentes.md)
