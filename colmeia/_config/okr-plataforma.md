---
config: okr-plataforma
versao: 1.0
status: template
---

# Configuração — Plataforma OKR

Preencha pelo operador. Skills `/sync-okr-plataforma` e `/desdobrar-okr` leem este arquivo.

## Conexão

| Campo | Valor |
|-------|-------|
| `mcp_server` | `[FORNECER: id do MCP da plataforma]` |
| `ciclo_atual` | `[FORNECER: ex. 2026-Q2]` |
| `tenant` | `[FORNECER]` |

## Níveis habilitados

```yaml
niveis:
  - codigo: L0
    label: Empresa
  - codigo: L1
    label: Diretoria
  - codigo: L2
    label: Comunidade
  - codigo: L3
    label: Squad
  # - codigo: L4
  #   label: Time
```

## Regras de desdobramento

```yaml
desdobramento:
  soma_pesos_max: 1.0          # 100% contribuição linear
  exigir_parent_ref: true
  metricas_obrigatorias:
    - baseline
    - target
    - roof
    - moonshot
  direcao_padrao: higher_is_better   # ou lower_is_better por métrica
```

## Mapeamento de operações MCP

| Capacidade framework | Método MCP |
|---------------------|------------|
| `okr.read_tree` | `[FORNECER]` |
| `okr.upsert_kr` | `[FORNECER]` |
| `okr.progress` | `[FORNECER]` |

## North Star

```yaml
north_star:
  nivel: L3
  # id preenchido após primeiro push
```
