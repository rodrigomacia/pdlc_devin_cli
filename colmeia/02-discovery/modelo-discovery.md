---
favo: 02-discovery
versao: 2.0
status: estavel
tags: [discovery, visoes, svm, personas-sinteticas, figma, feature-stories]
---

# Modelo de Discovery — três visões → hipóteses → validação → feature

Contrato de domínio do favo 02. Skills e tools devem falar este vocabulário.

## Princípio operacional — Go-to-Market

O **Head de Produto = Go-to-Market** é dono ponta-a-ponta da iniciativa.
Não há handoff de trio: o mesmo dono atravessa contexto → discovery → experimentação → construção → operação.

Os agentes/subagentes do favo 02 são **tools** desse Head de Produto, não pessoas em série.

## As três visões (sempre ancoradas no OKR)

Toda iniciativa começa o discovery construindo as **três visões**, cada uma com referência explícita a um KR ou KPI da Plataforma OKR.

```
                       ┌──────────────────┐
                       │   OKR / KR / KPI │  (favo 01)
                       └────────┬─────────┘
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
       ┌────────────┐    ┌────────────┐    ┌────────────┐
       │  MERCADO   │    │   PRODUTO  │    │   CLIENTE  │
       │  (fora)    │    │  (uso)     │    │   (voz)    │
       └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
             └─────────────────┼─────────────────┘
                               ▼
                         SÍNTESE / OST
                               ▼
                         HIPÓTESES
```

### 1. Visão de Mercado

| Dimensão | Conteúdo |
|----------|----------|
| Tendências | Sinais externos relevantes ao KR |
| Concorrência | Movimentos de players e benchmarks |
| Pesquisa | Estudos quantitativos/qualitativos secundários |
| Personas sintéticas (tool) | Cenários simulados para validar hipóteses de mercado |
| Regulação / ecossistema | Restrições e oportunidades externas |

### 2. Visão de Produto

Métricas de uso do produto em escala — todas segmentáveis por cohort.

| Métrica | O que mede |
|---------|------------|
| **Funil de conversão** | Etapas → taxa de avanço/abandono |
| **Tempo em jornada** | Distribuição (p50, p90) por etapa e total |
| **Jornada em loop** | Reentradas na mesma etapa (sinal de desorientação) |
| **Dead click** | Cliques em áreas não-interativas |
| **Rage click** | Cliques repetidos por frustração |
| **Drop-off por device/canal** | Onde a experiência quebra |
| **Coorte de retenção** | D1 / D7 / D30 / D90 |
| **Heatmap / scroll depth** | Atenção e conteúdo consumido |

### 3. Visão de Cliente (Voz do Cliente — VOC)

Sinais qualitativos vindos do próprio cliente em múltiplos canais.

| Canal | Fonte | Tool |
|-------|-------|------|
| **Central de atendimento** | Transcrição de ligações + classificação | Transcription + NLP/topic modeling |
| **Loja de app** | Reviews iOS/Android | App store scraper |
| **Suporte / chat** | Tickets, conversas | CRM, helpdesk |
| **Redes sociais** | Menções e sentimento | Social listening |
| **Entrevistas estruturadas** | Sessões 1:1 | `/prep-entrevista` |
| **Pesquisas in-app** | NPS, CSAT, micro-surveys | Survey tool |
| **Comportamento observado** | Session replay com consentimento | Analytics behavioral |

### Segmentação como dimensão transversal

Toda visão é segmentada por dimensões — definidas pelo operador em `_config/discovery-tools.md`:

- Segmento de cliente (definido pelo negócio)
- Cohort de aquisição / tempo de relacionamento
- Canal de entrada
- Device / plataforma
- Estado de jornada (novo, ativo, em risco, churn)

Cada insight é taggeado por segmento — sem segmentação, o insight é considerado fraco (`DIS-EVID-01`).

## Síntese das visões

A skill `/sintetizar-visoes` cruza as três visões e produz:

1. **Oportunidades** = dores/lacunas observadas em ≥ 2 visões com mesmo segmento
2. **OST** (Opportunity Solution Tree) — outcome = KR/KPI do OKR
3. **Mapa de evidências** — cada oportunidade com link para visão de origem

> Critério forte: oportunidade que aparece em **mercado + produto + cliente** = prioridade alta automática.

## Hipóteses

Após síntese, gerar **hipóteses testáveis** com a estrutura padrão:

```
Acreditamos que [intervenção]
para [segmento]
resultará em [mudança no KR/KPI]
porque [insight das visões].

Saberemos que estamos certos quando [sinal mensurável].
```

Cada hipótese carrega:
- `hipotese_id`
- `oportunidade_ref`
- `segmento[]`
- `kr_ref` (Plataforma OKR)
- `risco` (valor, usabilidade, viabilidade, factibilidade, regulatório)
- `confianca` (alta/média/baixa baseado em evidências)

## SVM — Synthetic Validation Method

**O que é:** validação rápida de hipóteses com **personas sintéticas** (clientes virtuais gerados por LLM com perfil + contexto + frictions + motivações).

**O que não é:** substituto para teste com cliente real. É filtro barato pré-protótipo.

### Estrutura de uma persona sintética

```yaml
persona_id: p-{seg}-{nn}
segmento: {seg}
demografia: {...}
contexto_uso: {...}
motivacoes: [...]
frictions_observadas: [...]   # vindas da visão Cliente
metricas_associadas: [...]    # vindas da visão Produto
fonte_dados: [voc|produto|pesquisa|sinteses]
```

### Protocolo SVM

| Step | Ação |
|------|------|
| 1 | Construir/atualizar pool de personas sintéticas a partir das 3 visões |
| 2 | Para cada hipótese: simular reação de N personas (default 5–10) |
| 3 | Coletar: aceitação, objeções, perguntas, palavras usadas |
| 4 | Pontuar (Strong / Weak / Inconclusive) por segmento |
| 5 | Toda saída marcada `[SINTÉTICO]` — não confundir com cliente real |

### Saídas SVM

- `svm-{hipotese}.md` — resultado simulado por persona/segmento
- `personas-sinteticas.yaml` — pool versionado

## Protótipo de jornada (Figma)

Hipóteses validadas no SVM viram **protótipo navegável** — visão tangível da experiência.

| Elemento | Conteúdo |
|----------|----------|
| Fluxo principal | Telas + transições da jornada feliz |
| Fluxos alternativos | Erro, sem dados, sem conexão |
| Anotações de hipótese | Cada tela referencia `hipotese_id` |
| Métricas-alvo | Quais KPIs cada tela move |
| Variantes | Versões A/B para favo 03 (se aplicável) |

A skill `/prototipo-figma` produz **especificação** do protótipo (descrição estruturada + URL Figma quando o operador conectar a tool); o trabalho gráfico em si é humano + Figma MCP.

## Feature com histórias segmentadas por valor

**Entregável final do favo 02** — pacote completo para favos 03 (deploy/teste) e 04 (construção).

### Estrutura

```
Feature: {nome}
├── Outcome (KR/KPI do OKR)
├── Hipóteses validadas (SVM + visões)
├── Jornada (protótipo Figma)
└── Histórias por valor
    ├── Valor V1 — segmento S1
    │   ├── História H1.1
    │   ├── História H1.2
    ├── Valor V2 — segmento S2
    └── ...
```

### Anatomia da história segmentada por valor

```yaml
historia_id: h-{n}
valor: "{frase de valor entregue ao cliente}"
segmento: {seg}
quem: "Como {tipo de cliente}..."
quero: "...quero {ação/capacidade}..."
para: "...para {benefício/job}."
hipotese_ref: hip-{n}
kr_ref: kr-L3-{n}
prototipo_ref: figma:{frame}
criterios_aceitacao:
  - {comportamental, não-técnico}
sinais_sucesso:
  - {KPI específico afetado}
```

### Princípios

1. **Histórias agrupadas por valor**, não por componente técnico
2. Cada história rastreável até **hipótese + visão de origem**
3. Critérios de aceitação em **linguagem de cliente**, não de implementação
4. Sem decisão técnica embutida (isso é favo 04)

## Loop com favo 05 (operação)

Quando insights vêm da operação (`/insight-para-discovery`), eles entram como nova evidência na **Visão de Produto** ou **Visão de Cliente** — não como nova etapa.

## Códigos de auditoria (favo 02)

| Código | Condição |
|--------|----------|
| DIS-01 | Outcome não ligado ao OKR/KR |
| DIS-VIS-01 | Menos de 3 visões construídas |
| DIS-VIS-02 | Visão sem segmentação |
| DIS-EVID-01 | Oportunidade sem evidência rastreável (visão de origem) |
| DIS-SVM-01 | Hipótese sem teste SVM antes de prototipagem |
| DIS-SVM-02 | Resultado SVM apresentado como real (sem marca `[SINTÉTICO]`) |
| DIS-FIG-01 | Protótipo sem referência de hipótese |
| DIS-STORY-01 | História sem `valor` ou `segmento` |
| DIS-STORY-02 | História com decisão técnica embutida |
