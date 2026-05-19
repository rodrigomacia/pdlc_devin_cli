---
favo: 02-discovery
versao: 2.0
tags: [templates, visoes, svm, feature-stories]
---

# Templates — favo 02

Path runtime: `colmeia/02-discovery/_iniciativas/{id}/`

## visao-mercado.md

```yaml
---
favo: 02-discovery
iniciativa: {id}
visao: mercado
kr_ref: {kr_id da Plataforma OKR}
periodo: {YYYY-MM}
---
```

```markdown
# Visão de Mercado — {id}

## Outcome alvo
{KR/KPI ref}

## Tendências
| # | Sinal | Implicação | Confiança | Fonte |

## Concorrência
| Player | Movimento | Implicação | Segmento |

## Pesquisa secundária
| Estudo | Insight | Segmento |

## Cenários sintéticos (synth.persona_run)
| Cenário | Hipótese de mercado | Reação sintética | Segmento |
*Marcar [SINTÉTICO]*

## Implicações para OKR
| KR/KPI | Impacto estimado | Onde olhar |
```

## visao-produto.md

```yaml
---
favo: 02-discovery
iniciativa: {id}
visao: produto
kr_ref: {kr_id}
janela: {YYYY-MM-DD..YYYY-MM-DD}
segmentos: [{seg_list}]
---
```

```markdown
# Visão de Produto — {id}

## Funil de conversão
| Etapa | Volume | Taxa | Drop | Segmento |
| ... | ... | ... | ... | ... |

## Tempo em jornada
| Etapa | p50 | p90 | Segmento |

## Jornada em loop (desorientação)
| Etapa | % reentrada | Padrão | Segmento |

## Dead click
| Tela | Área | Volume | Segmento |

## Rage click
| Tela | Elemento | Volume | Segmento |

## Cohort de retenção
| Cohort | D1 | D7 | D30 | Segmento |

## Drop-offs específicos
| Canal/device | Etapa | % | Nota |

## Implicações
{[FORNECER pela síntese]}
```

## visao-cliente.md

```yaml
---
favo: 02-discovery
iniciativa: {id}
visao: cliente
kr_ref: {kr_id}
canais: [central, app_store, social, entrevista, survey]
segmentos: [...]
---
```

```markdown
# Visão de Cliente (VOC) — {id}

## Central de atendimento
| Tópico | Volume | Sentimento | Segmento | Citação representativa |

## Reviews loja
| Estrela | Tema | Citação | Segmento | Plataforma |

## Suporte / chat
| Tópico | Volume | Segmento |

## Social listening
| Tema | Sentimento | Segmento |

## Pesquisas in-app (NPS/CSAT)
| Pergunta | Score | Segmento | Comentários abertos (resumo) |

## Entrevistas estruturadas
| Data | Perfil | Oportunidade explorada | Insight |

## Síntese qualitativa
| Tema | Frequência | Segmento(s) | Job afetado |
```

## sintese-visoes / oportunidades

`oportunidades.md`:

```markdown
# Oportunidades — {id}

| O# | Descrição | Visões de origem | Segmento(s) | Confiança | Impacto KR |
|----|-----------|-------------------|-------------|-----------|------------|
| O1 | | mercado+produto+cliente | | alta | KR? |
```

`mapa-evidencias.md`:

```markdown
# Mapa de evidências — {id}

| O# | Mercado | Produto | Cliente | Notas |
|----|---------|---------|---------|-------|
| O1 | mkt:T2 | prod:funnel-etapa3 | voc:central:tema7 | |
```

`ost-{id}.md`:

```markdown
# OST — {id}
## Outcome
{KR/KPI ref}
## Oportunidades
### O1 — ...
- Evidência: mercado / produto / cliente
- Soluções: S1, S2
- Hipóteses: H1, H2
```

## hipoteses.yaml

```yaml
iniciativa: {id}
hipoteses:
  - hipotese_id: hip-1
    oportunidade_ref: O1
    enunciado: >
      Acreditamos que [intervenção] para [segmento] resultará em
      [mudança em KR/KPI] porque [insight].
      Saberemos quando [sinal].
    segmento: [...]
    kr_ref: {kr_id}
    risco: [valor, usabilidade, viabilidade, factibilidade, regulatorio]
    confianca: alta | media | baixa
    status: nova | em-svm | strong | iterate | kill
    svm_ref: null
```

## personas-sinteticas.yaml

```yaml
iniciativa: {id}
versao: 0
personas:
  - persona_id: p-{seg}-01
    segmento: {seg}
    demografia: {[FORNECER]}
    contexto_uso: {[FORNECER]}
    motivacoes: []
    frictions_observadas: []
    metricas_associadas: []
    fonte_dados: [voc, produto, mercado]
    construido_em: {YYYY-MM-DD}
```

## svm-{hip}.md

```markdown
# SVM — {hipotese_id} — {data}
**[SINTÉTICO — não usar como evidência de cliente real]**

## Hipótese
{enunciado}

## Personas testadas
| persona_id | segmento | reação | objeções | palavras-chave |

## Pontuação por segmento
| Segmento | Strong | Weak | Inconclusive | Recomendação |

## Decisão
{strong | iterate | kill}

## Próximo passo
{prototipo | refinar hipótese | descartar}
```

## prototipo-spec.md

```markdown
# Protótipo — {id}

## Figma
URL: {[FORNECER]}
Frame raiz: {[FORNECER]}

## Fluxo principal
| Tela | hipotese_ref | KPI alvo | Notas |

## Fluxos alternativos
| Caso | Telas | Tratamento |

## Variantes (se aplicável)
| Variante | Diferença | Para favo 03 |

## Anotações de hipótese
| Tela | hipotese_id | Sinal esperado |
```

## feature-{id}.md (ENTREGÁVEL Gate 02)

```yaml
---
favo: 02-discovery
iniciativa: {id}
tipo: feature
outcome_kr_ref: {kr_id}
status: candidata-handoff-03
validacao_real: pendente
---
```

```markdown
# Feature — {nome}

## Outcome
{KR/KPI ref + meta target/roof}

## Hipóteses validadas
| hipotese_id | Status SVM | Visões de origem |

## Jornada (protótipo)
Figma: {url}

## Histórias por valor

### Valor V1 — {frase de valor} — Segmento {S1}
- h-1.1: …
- h-1.2: …

### Valor V2 — {frase} — Segmento {S2}
- h-2.1: …

## Métricas-alvo
| KPI | baseline | target | tela/passo |

## Riscos abertos para favo 03
| Tipo | Descrição | Tratamento sugerido |
```

## historias.yaml

```yaml
iniciativa: {id}
historias:
  - historia_id: h-1.1
    valor: "{frase de valor}"
    segmento: {seg}
    quem: "Como {tipo}..."
    quero: "...quero..."
    para: "...para..."
    hipotese_ref: hip-1
    kr_ref: {kr_id}
    prototipo_ref: "figma:{frame}"
    criterios_aceitacao:
      - "{comportamento observável}"
    sinais_sucesso:
      - "{KPI}"
```

## gate-02-registro.md

```markdown
# Gate 02 — {id}
Status: APROVADO | RESSALVAS | REPROVADO
Aprovador: Head de Produto (Go-to-Market)
Data:
Ressalvas:
```

## roteiros/roteiro-{data}.md

Ver template antigo de entrevista (mantido) — output do `/prep-entrevista`.
