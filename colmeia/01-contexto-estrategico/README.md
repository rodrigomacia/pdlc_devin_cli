---
favo: 01-contexto-estrategico
versao: 1.1
status: estavel
downstream:
  - ../02-discovery/README.md
skill_primaria: desdobrar-okr
---

# Favo 01 — Contexto Estratégico

## Função no ciclo

Traduzir direção em **OKRs desdobrados em todos os níveis**, com acompanhamento na **Plataforma OKR** (KR, KPI, baseline, target, roof, moonshot).

## Modelo e tools

| Doc | Conteúdo |
|-----|----------|
| [modelo-okr.md](./modelo-okr.md) | Domínio: cascata, entidades, 4 metas, desdobramento |
| [capacidades-tools.md](./capacidades-tools.md) | Tools Devin + MCP Plataforma OKR |
| [_config/okr-plataforma.md](../_config/okr-plataforma.md) | Conexão MCP (operador) |

## Skills (ordem)

```
/sync-okr-plataforma {id} pull
→ /draft-okr {id}
→ /desdobrar-okr {id}
→ /auditar-okr {id}
→ /sync-okr-plataforma {id} push
```

| Skill | Papel |
|-------|-------|
| `/sync-okr-plataforma` | **Tool** — sistema de registro multi-nível |
| `/desdobrar-okr` | **Desdobramento** — cascata e pesos |
| `/draft-okr` | Rascunho narrativo + OKR markdown |
| `/auditar-okr` | Gate 01 + coerência de metas |

## Saídas (runtime)

`colmeia/01-contexto-estrategico/_iniciativas/{id}/` — inclui `okr-cascata.yaml`, `plataforma-snapshot.yaml`, `sync-okr-log.md`

## Documentos

[fluxo.md](./fluxo.md) · [gates.md](./gates.md) · [artefatos.md](./artefatos.md) · [agentes.md](./agentes.md)
