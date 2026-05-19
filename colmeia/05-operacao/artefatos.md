---
favo: 05-operacao
versao: 2.0
---

# Templates — favo 05

## incidente.yaml

```yaml
incidente_id: inc-{YYYYMMDD}-{nn}
iniciativa: {id}
severidade: sev1 | sev2 | sev3
status: investigando | mitigando | monitorando | resolvido
commander: ert-lead
aberto_em: ISO8601
segmentos_afetados: []
kr_em_risco: []
```

## timeline.md (Logger)

```markdown
# Timeline — {incidente_id}
| UTC | Autor (agent) | Evento | Evidência |
```

## comunicacoes.md

```markdown
# Comunicações — {incidente_id}
| Hora | Audiência | Canal | Mensagem | Status |
```

## visao-360.md

Ver [modelo-ert.md](./modelo-ert.md).

## acoes.md (Commander)

```markdown
# Ações — {incidente_id}
| # | Ação | Owner agent | Status | Resultado |
```

## fechamento.md

```markdown
# Fechamento — {incidente_id}
Causa raiz (provisória/final):
Impacto cliente:
Lições:
Postmortem ref:
```

## metricas-review · postmortem · insights

(Mantidos da v1)
