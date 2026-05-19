---
favo: 04-construcao
versao: 2.0
tags: [sdd, templates]
---

# Templates — favo 04 (SDD)

Path runtime: `colmeia/04-construcao/_iniciativas/{id}/`

## resumo-head.md (atualizado a cada spec)

```markdown
# Resumo para o Head — {id}

## O que vamos entregar ao cliente
{linguagem de valor — sem tech}

## Histórias incluídas
| historia_id | valor | segmento |

## Métricas que vamos observar em produção
| KPI | baseline | target |

## Riscos em linguagem de negócio
| Risco | Mitigação |

## Próxima decisão que o Head toma
{ex: aprovar spec funcional / validar canário}
```

## spec-funcional-{id}.md

```yaml
---
tipo: spec-funcional
iniciativa: {id}
versao: 1.0
---
```

```markdown
# Especificação funcional — {id}

## Escopo
Outcome KR: {kr_ref}

## Por história

### {historia_id} — {valor}
- **Segmento:** {seg}
- **Comportamento esperado:** ...
- **Critérios de aceitação:** (copiados de historias.yaml, expandidos)
- **Fluxos alternativos:** erro, vazio, offline
- **Fora de escopo:** ...

## Regras de negócio transversais
| ID | Regra | Histórias |

## Dependências de outros times/sistemas (linguagem negócio)
| Sistema | O que precisamos |

## Rastreabilidade
| Spec § | historia_id | hipotese_ref |
```

## spec-nfr-{id}.yaml

```yaml
iniciativa: {id}
nfr:
  performance:
    p95_latency_ms: [FORNECER]
    rps_min: [FORNECER]
  disponibilidade:
    slo: 99.9
    multi_region: true
  seguranca:
    autenticacao: [FORNECER]
    dados_sensiveis: [FORNECER]
    regulacao: [FORNECER]
  acessibilidade:
    wcag: 2.1 AA
  observabilidade:
    metricas_discovery: [funnel, journey_time, dead_click, rage_click, cohort]
resumo_head: |
  {parágrafo em linguagem de negócio}
```

## spec-tecnica-{id}.md

```markdown
# Especificação técnica — {id}
**Audiência: agents de implementação — não enviar ao Head como doc principal**

## Mapeamento monorepo
| historia_id | apps/mobile-native | apps/web-ssg | apps/bff | integrations |

## Contratos
| API/evento | Contrato path | Versão |

## Modelo de dados (lógico)
...

## Integrações Sistema produto
| int_id | operação | contrato |

## Infra / multi-região
| Recurso | Regiões | Notas |

## Rastreabilidade
| Componente | spec-funcional § | historia_id |
```

## tarefas.yaml

```yaml
iniciativa: {id}
tarefas:
  - tarefa_id: t-001
    titulo: "{entregável em uma linha}"
    historia_id: h-1.1
    spec_funcional_ref: "§..."
    spec_tecnica_ref: "§..."
    camadas: [web-ssg, bff]
    entregavel: codigo   # sempre código + testes
    testes_obrigatorios: [unit, functional]
    status: pendente | em-progresso | pronto | bloqueada
    pr_ref: null
```

## ci-status-{id}.md

Ver [modelo-pipeline.md](./modelo-pipeline.md) (CI segregado).

```markdown
# CI — {id}
commit_hash: {hash}
semáforo: VERDE | VERMELHO
artifact_id: art-{hash}
pronto_para_cd: sim | nao
```

## deploy-manifest-{hash}.yaml

```yaml
commit_hash: "{hash}"
artifact_id: art-{hash}
built_at: ISO8601
components:
  - name: bff
    image: "{registry}/bff:{hash}"
  - name: web-ssg
    image: "{registry}/web-ssg:{hash}"
  - name: mobile-native
    build: "{hash}"
checksum: "{sha256}"
```

## cd-state.yaml

```yaml
iniciativa: {id}
commit_hash: "{hash}"
ci_status: verde
cd:
  sandbox:
    status: pending | deployed | failed | tests_ok
    deploy_ref: "{hash}"
    deployed_at: null
  homolog:
    status: pending | deployed | failed | tests_ok
    deploy_ref: "{hash}"
    service_virtualization: true
    mock_profile: "mock-profile-{id}"
    tests:
      functional: null
      nfr_perf: null
      nfr_security: null
  producao:
    status: pending | deployed | canario | expanding | complete
    deploy_ref: "{hash}"
    deploy_anterior_ref: null
    rollout: {}
```

## cd-status-head-{id}.md

Ver [modelo-ci-cd.md](./modelo-ci-cd.md).

## mock-profile-{id}.yaml (Homolog)

```yaml
iniciativa: {id}
profile: mock-profile-{id}
service_virtualization: true
stubs:
  - operation: sistema_produto.{operacao}
    method: GET | POST
    response_fixture: "fixtures/{nome}.json"
    latency_ms: 50
```

## pipeline-status-{id}.md

**Legado** — preferir `ci-status-{id}.md`. Alias de saída CI.

## rollout-plan-{id}.md

```markdown
# Plano de rollout — {id}

## Para o Head
- **Primeiro grupo de clientes (canário):** {segmento — linguagem negócio}
- **O que observar:** {KPIs}
- **Por quanto tempo:** {dias}
- **Critério para expandir:** {definido com Head}

## Fases
| Fase | Segmento | % clientes | Status |

## Rollback (linguagem Head)
Se {condição negócio}, voltamos versão anterior em {tempo}.
```

## rollout-state.yaml

```yaml
iniciativa: {id}
fase_atual: canario | validacao_head | expansao | completo
segmento_canario: {}
segmentos_ativos: []
percentual_global: 0
regioes: []
```

## validacao-head-{id}.md

```markdown
# Validação do Head — rollout canário — {id}

## Segmento observado
## Período
## Métricas (mesmas do discovery)
| Métrica | Canário | Controle | Δ |

## VOC resumido
## Veredito Head
APROVAR_EXPANSAO | ITERAR | ROLLBACK

## Próximo segmento (se expansão)
```

## release-plan.md · review-pr · changelog · gate-04

(Mantidos — ver versão anterior; adicionar seção rollout e pipeline)
