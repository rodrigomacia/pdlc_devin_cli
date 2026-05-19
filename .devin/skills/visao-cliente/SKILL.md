---
name: visao-cliente
description: Constrói Visão de Cliente / VOC (transcrições, reviews, suporte, social) — favo 02
argument-hint: "<id>"
agent: voc-analyst
subagent: true
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/02-discovery/_iniciativas/**/visao-cliente.md)
    - Write(colmeia/02-discovery/_iniciativas/**/sinais-voc/**)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/02-discovery/artefatos.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS**

1. Validar Gate 01 — OKR existe; senão, parar
2. Ler canais habilitados em `colmeia/_config/discovery-tools.md`
3. Coletar via tools `voc.*` (ou dump do operador):
   - Central de atendimento — tópicos via transcrição + NLP
   - Reviews iOS/Android — tema, estrela, citação
   - Suporte / chat — tópicos
   - Social listening — sentimento
   - NPS/CSAT/in-app — score + comentários abertos
   - Entrevistas estruturadas — output do `/prep-entrevista`
4. **PII masking obrigatório** — anonimizar citações
5. Toda citação marca canal + segmento
6. Síntese qualitativa: temas × frequência × segmentos × job afetado
7. Escrever `colmeia/02-discovery/_iniciativas/$1/visao-cliente.md` (template em `artefatos.md`)
8. Sem dado da tool → `[DADO AUSENTE]`; nunca inventar voz do cliente
