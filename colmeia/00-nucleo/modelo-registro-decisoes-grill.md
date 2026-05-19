---
favo: 00-nucleo
versao: 1.0
status: estavel
tags: [grill-me, decisao, rastreabilidade, hipoteses]
relacionado: [grill-me.md](./grill-me.md)
---

# Registro de decisões pós grill-me

## Princípio

Todo item **candidato a decisão** (hipótese, oportunidade, experimento, história, KR auxiliar) deve constar no registro com:

1. **Decisão explícita** — continuar, desconsiderar, adiar, iterar, scale, kill, etc.
2. **Motivadores** — evidências, grill, Head, SVM, dados reais (com fonte rastreável).
3. **Motivos de não continuar** — quando desconsiderado ou adiado, **obrigatório** documentar por que não segue.

**Cobertura:** 100% dos itens do artefato interrogado naquele momento — nenhum item pode “sumir” sem linha no registro.

## Artefato canônico (runtime)

`colmeia/_grill/{id}/registro-decisoes-grill.yaml`

- **Um arquivo por iniciativa**, atualizado a cada `/grill-me`.
- Cada execução de grill acrescenta uma **entrada** (`entradas[]`) — histórico imutável (correções = nova entrada com `corrige_entrada_ref`).

## Valores de decisão (por tipo)

| Tipo item | Decisões permitidas |
|-----------|---------------------|
| `hipotese` | `continuar` · `desconsiderar` · `adiar` · `iterar` |
| `oportunidade` | `priorizar` · `desconsiderar` · `adiar` |
| `svm` | `continuar_prototipo` · `iterar` · `desconsiderar` |
| `experimento` | `scale` · `iterate` · `pivot` · `kill` · `defer` |
| `historia` | `incluir_feature` · `desconsiderar` · `adiar` |
| `okr_aux` | `manter` · `refinar` · `remover` |

## Motivadores (estrutura)

Cada motivador:

```yaml
- tipo: evidencia | grill | head | svm | experimento_real | risco | compliance
  fonte: visao-mercado | visao-produto | visao-cliente | grill-{momento} | entrevista | analytics | ...
  referencia: "caminho ou ID do artefato"
  descricao: "texto objetivo — o que sustenta a decisão"
```

| Campo na decisão | Quando preencher |
|------------------|------------------|
| `motivadores_continuar` | decisão implica seguir (continuar, scale, priorizar, incluir_feature, …) |
| `motivadores_nao_continuar` | decisão implica parar (desconsiderar, kill, remover, …) |
| Ambos | **adiar** / **iterar** — documentar por que não agora **e** o que falta para continuar |

## Regra 100%

Após grill do momento `M`, a entrada deve listar **todos** os IDs do conjunto:

| Momento grill | Conjunto obrigatório (100%) |
|---------------|----------------------------|
| `hipoteses` | todos `hipotese_id` em `hipoteses.yaml` |
| `oportunidades` | todas `O#` em `oportunidades.md` |
| `svm` | todas hipóteses com `status` ≠ `nova` ou com linha `desconsiderar` + motivo |
| `prototipo` | todas hipóteses referenciadas em `prototipo-spec.md` + hipóteses do yaml não no protótipo |
| `feature` | todas hipóteses em `feature-*.md` + histórias em `historias.yaml` |
| `decisao-exp` | todos experimentos em `experiments-backlog.md` + hipóteses ligadas |
| `gate-02` / `gate-03` | validação de que entradas anteriores estão completas |

Se faltar item → veredito grill `REFINAR` ou `BLOQUEAR` · código **GRILL-REG-01**.

## Integração com `hipoteses.yaml`

Cada hipótese ganha campos (atualizados pelo grill ou pela skill seguinte):

```yaml
decisao_pos_grill: continuar | desconsiderar | adiar | iterar | pendente
registro_grill_ref: "entradas[2].itens[hip-1]"  # rastreio
```

Hipótese `desconsiderar` **permanece** no yaml — não apagar; status `kill` ou `descartada` + motivadores no registro.

## Quem preenche

| Papel | Responsabilidade |
|-------|------------------|
| `/grill-me` | Gera perguntas; propõe rascunho de decisão por item; **não** decide sozinho |
| **Head de Produto** | Confirma ou corrige decisão e motivadores na sessão |
| Skill `/grill-me` | Persiste entrada em `registro-decisoes-grill.yaml` após respostas do Head |

## Gates

| Gate | Checklist |
|------|-----------|
| 02 | **G2.REG** — registro cobre 100% hipóteses após `grill hipoteses` + `grill svm` |
| 03 | **G3.REG** — registro cobre 100% experimentos/hipóteses após `grill decisao-exp` |

## Códigos

| Código | Condição |
|--------|----------|
| GRILL-REG-01 | Item do artefato sem linha no registro |
| GRILL-REG-02 | `desconsiderar` / `kill` sem `motivadores_nao_continuar` |
| GRILL-REG-03 | `continuar` / `scale` sem `motivadores_continuar` |
| GRILL-REG-04 | Registro contradiz `hipoteses.yaml` ou `decisao-experimentos.md` |

Template YAML: [../02-discovery/artefatos.md](../02-discovery/artefatos.md#registro-decisoes-grillyaml)
