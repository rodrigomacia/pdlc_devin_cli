---
favo: 02-discovery
versao: 2.0
tags: [tools, mcp, voc, analytics, personas, figma]
---

# Capacidades (tools) — favo 02

Modelo: [modelo-discovery.md](./modelo-discovery.md)

## Camada 1 — Devin nativas

| Tool | Uso |
|------|-----|
| `read` / `edit` | Artefatos em `_iniciativas/{id}/` |
| `grep` / `glob` | Cross-leitura entre visões |
| `web_search` | Visão de Mercado (tendências, concorrência) |

## Camada 2 — Plataforma OKR (favo 01)

Reutilizada para ancorar outcome: `okr.read_tree`, `okr.read_node`, `okr.progress`.

## Camada 3 — Voz do Cliente (Visão Cliente)

| Capacidade lógica | Função | Implementação típica |
|-------------------|--------|----------------------|
| `voc.transcription` | Transcrição de ligações da central | Serviço de speech-to-text + classificador |
| `voc.topics` | Topic modeling sobre transcrições | NLP / LLM |
| `voc.app_reviews` | Coleta + análise reviews iOS/Android | App store scraper |
| `voc.tickets` | Leitura de tickets de suporte | CRM/helpdesk MCP |
| `voc.social` | Menções e sentimento | Social listening |
| `voc.surveys` | NPS/CSAT/in-app | Survey MCP |
| `voc.segment_tag` | Marcar cada sinal por segmento | CDP / data warehouse |

## Camada 4 — Analytics de Produto (Visão Produto)

| Capacidade lógica | Função | Implementação típica |
|-------------------|--------|----------------------|
| `prod.funnel` | Funil de conversão por etapa | Amplitude / Mixpanel / GA |
| `prod.journey_time` | Tempo p50/p90 por etapa | Mesmos |
| `prod.journey_loops` | Reentradas / desorientação | Behavioral analytics |
| `prod.dead_click` | Cliques mortos | ContentSquare / FullStory / Hotjar |
| `prod.rage_click` | Cliques de raiva | Idem |
| `prod.session_replay` | Replay de sessão (consentido) | FullStory / LogRocket |
| `prod.cohort_retention` | Retenção D1/D7/D30 | Amplitude / Mixpanel |
| `prod.segment_explorer` | Cortes por segmento | CDP + analytics |

## Camada 5 — Mercado e Pesquisa (Visão Mercado)

| Capacidade lógica | Função |
|-------------------|--------|
| `mkt.research_db` | Estudos secundários, relatórios |
| `mkt.competitor_scan` | Movimentos de concorrentes |
| `mkt.benchmark` | Benchmarks setoriais |

## Camada 6 — Personas sintéticas / SVM

| Capacidade lógica | Função | Implementação |
|-------------------|--------|---------------|
| `synth.persona_build` | Compor personas a partir VOC + produto + segmento | LLM + base de dados de sinais |
| `synth.persona_run` | Simular reação de persona a hipótese/prototipo | LLM com prompt estruturado |
| `synth.svm_score` | Pontuação Strong/Weak/Inconclusive | Critério configurável |
| `synth.persona_store` | Versionar pool de personas | YAML em `_iniciativas/` |

## Camada 7 — Prototipagem

| Capacidade lógica | Função |
|-------------------|--------|
| `figma.read_frame` | Ler frames/arquivos Figma | Figma MCP |
| `figma.export_spec` | Exportar spec (URLs, anotações) | Figma MCP |
| `figma.comment` | Anotar telas com `hipotese_id` | Figma MCP |

## Camada 8 — Gestão de iniciativa (opcional)

| Capacidade | Função |
|------------|--------|
| Issue tracker (Linear, Jira) | Histórias rastreáveis para favo 04 |
| Wiki / Notion | Publicação narrativa do discovery |

## Skills × tools

| Skill | Tools mínimas | Tools recomendadas |
|-------|---------------|--------------------|
| `/visao-mercado` | read, edit, web_search | `mkt.*`, `synth.persona_run` |
| `/visao-produto` | read, edit | `prod.*`, `okr.read_node` |
| `/visao-cliente` | read, edit | `voc.*`, `voc.segment_tag` |
| `/sintetizar-visoes` | read, edit | — |
| `/gerar-hipoteses` | read, edit | `okr.read_node` |
| `/testar-svm` | read, edit | `synth.persona_build`, `synth.persona_run`, `synth.svm_score` |
| `/prototipo-figma` | read, edit | `figma.*` |
| `/feature-stories` | read, edit | issue tracker MCP (opcional) |
| `/prep-entrevista` | read, edit | survey/recruiting MCP |

## Permissões por agente (recomendação)

| Agente | Read | Write | MCP |
|--------|------|-------|-----|
| `discovery-lead` (Head de Produto) | colmeia/** | 02-discovery/_iniciativas/** | todos |
| `voc-analyst` ⊂ | colmeia/** | sinais-voc/** | voc.* |
| `product-analytics` ⊂ | colmeia/** | sinais-produto/** | prod.* |
| `market-researcher` ⊂ | colmeia/** | sinais-mercado/** | mkt.*, web_search |
| `personas-sinteticas` ⊂ | colmeia/** | personas/** + svm/** | synth.* |
| `prototipador` ⊂ | colmeia/** | prototipo/** | figma.* |
| `feature-writer` ⊂ | colmeia/** | feature/** | tracker opcional |
