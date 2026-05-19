---
favo: 01-contexto-estrategico
versao: 1.0
tags: [tools, mcp, plataforma-okr]
---

# Capacidades (tools) — favo 01

## Camada 1 — Devin nativas

| Tool | Uso |
|------|-----|
| `read` / `edit` | Artefatos `colmeia/01/.../_iniciativas/` |
| `grep` / `glob` | Validar schema, gates |
| `web_search` | Scanning (opcional, `scanner-ambiente`) |

## Camada 2 — Plataforma OKR (obrigatória para desdobramento completo)

Produto de acompanhamento multi-nível com **OKR, KR, KPI** e metas **baseline · target · roof · moonshot**.

| Tool lógica | Descrição |
|-------------|-----------|
| **okr.read_tree** | Cascata completa por ciclo |
| **okr.read_node** | Detalhe de Objective/KR/KPI |
| **okr.upsert_*** | Publicar desdobramento |
| **okr.link_parent** | Vínculo pai-filho |
| **okr.progress** | Acompanhamento atual |

Implementação: MCP configurado em `_config/okr-plataforma.md`.

## Camada 3 — Suporte (opcional)

| Tool | Uso |
|------|-----|
| BI / dicionário de métricas | Validar definição de KR/KPI |
| Wiki / diretriz | Fonte L0–L2 |
| Issue tracker | Link iniciativa `{id}` ↔ squad |

## Skills × tools

| Skill | Tools mínimas |
|-------|---------------|
| `/draft-okr` | read, edit; opcional `okr.read_tree` |
| `/desdobrar-okr` | read, edit; **okr.read_tree**, **okr.link_parent** |
| `/sync-okr-plataforma` | **okr.read_***, **okr.upsert_*** |
| `/auditar-okr` | read; opcional `okr.read_node` para diff |

Ver [modelo-okr.md](./modelo-okr.md).
