---
name: sintetizar-visoes
description: Cruza as três visões em oportunidades + OST + mapa de evidências — favo 02
argument-hint: "<id>"
agent: discovery-lead
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/02-discovery/_iniciativas/**)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/artefatos.md
@colmeia/02-discovery/gates.md

ID: **$ARGUMENTS**

1. Validar presença das 3 visões em `colmeia/02-discovery/_iniciativas/$1/`:
   - `visao-mercado.md`, `visao-produto.md`, `visao-cliente.md`
   - Faltando alguma → parar com `DIS-VIS-01`
2. Cruzar sinais — agrupar por **tema + segmento**
3. Gerar `oportunidades.md`:
   - Oportunidade = dor/lacuna observada em ≥ 2 visões com mesmo segmento
   - Marcar confiança (alta se 3 visões; média se 2)
   - Vincular ao KR/KPI alvo
4. Gerar `mapa-evidencias.md` — tabela `O# × Mercado × Produto × Cliente`
5. Gerar/atualizar `ost-$1.md`:
   - Outcome = KR/KPI do OKR (favo 01)
   - Ramos = oportunidades priorizadas
6. Sem cruzamento mínimo → marcar `[SEM EVIDÊNCIA]`; não inventar
