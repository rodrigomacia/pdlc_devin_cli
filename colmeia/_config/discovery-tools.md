---
config: discovery-tools
versao: 1.0
status: template
---

# Configuração — Tools de Discovery (favo 02)

Preencha pelo operador. Skills do favo 02 leem este arquivo.

## Voz do Cliente (VOC)

```yaml
voc:
  central_atendimento:
    mcp: "[FORNECER]"
    janela_dias: 30
  app_store:
    mcp: "[FORNECER]"
    apps: ["[FORNECER]"]
  suporte:
    mcp: "[FORNECER]"
  social:
    mcp: "[FORNECER]"
  surveys:
    mcp: "[FORNECER]"
  pii_masking: true
```

## Analytics de Produto

```yaml
produto:
  mcp: "[FORNECER]"
  metricas_padrao:
    - funnel
    - journey_time
    - journey_loops
    - dead_click
    - rage_click
    - cohort_retention
  janela_padrao_dias: 28
```

## Segmentação (transversal)

```yaml
segmentacao:
  fonte: "[FORNECER — CDP / DW]"
  segmentos:
    - "[FORNECER]"
  default: "todos"
```

## Pesquisa de Mercado

```yaml
mercado:
  fontes_secundarias: []
  benchmark_setor: "[FORNECER]"
  web_search_habilitado: true
```

## Personas sintéticas

```yaml
personas:
  modelo: "[FORNECER — provedor LLM]"
  pool_size_default: 8
  segmentos_obrigatorios: []
  marca_sintetico: "[SINTÉTICO]"
```

## Prototipagem Figma

```yaml
figma:
  mcp: "[FORNECER]"
  workspace: "[FORNECER]"
  template_jornada: "[FORNECER]"
```

## Issue tracker (opcional)

```yaml
tracker:
  mcp: "[FORNECER]"
  projeto_default: "[FORNECER]"
```
