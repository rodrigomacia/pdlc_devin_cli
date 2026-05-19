---
favo: 05-operacao
versao: 2.0
status: estavel
skill_primaria: review-metricas
---

# Favo 05 — Operação

## Função no ciclo

Monitorar produção, responder incidentes via **ERT (IA)** com visão 360°, e fechar o loop com Discovery.

## ERT — Emergency Response Team

| Papel | Skill |
|-------|-------|
| Incident Commander | `/ert-comandar` |
| Logger | `/ert-registrar` |
| Communication Focal | `/ert-comunicar` |
| SME Produto + Tech | `/ert-diagnosticar` |

Modelo: [modelo-ert.md](./modelo-ert.md)

## Skills

| Skill | Função |
|-------|--------|
| `/review-metricas` | OKR vs produção (métricas discovery) |
| `/rollout-status` | Status rollout (delega favo 04) |
| `/ert-abrir` · `/ert-comandar` · `/ert-registrar` · `/ert-comunicar` · `/ert-diagnosticar` · `/ert-fechar` | Ciclo incidente |
| `/postmortem` | Aprendizado |
| `/insight-para-discovery` | Retorno favo 02 |

## Loop

```
05 insights → 02 visões → sintetizar → …
```

## Documentos

[fluxo.md](./fluxo.md) · [gates.md](./gates.md) · [artefatos.md](./artefatos.md) · [agentes.md](./agentes.md)
