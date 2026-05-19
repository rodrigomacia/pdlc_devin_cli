---
name: feature-stories
description: Escreve feature com histórias segmentadas por valor — entregável Gate 02
argument-hint: "<id>"
agent: feature-writer
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
    - Write(colmeia/02-discovery/_iniciativas/**/feature-*.md)
    - Write(colmeia/02-discovery/_iniciativas/**/historias.yaml)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/artefatos.md
@colmeia/02-discovery/gates.md

ID: **$ARGUMENTS**

1. Pré-condição: `prototipo-spec.md` + `hipoteses.yaml` (com SVM concluído) + três visões presentes
2. Ler outcome (KR/KPI) do OKR (favo 01)
3. Gerar `feature-$1.md` com frontmatter:
   - `validacao_real: pendente` (favo 03 confirma com clientes reais)
   - `status: candidata-handoff-03`
   - Outcome (KR/KPI ref + target/roof)
   - Hipóteses validadas (lista com `status` SVM)
   - Jornada — link para `prototipo-spec.md` (e URL Figma)
   - **Histórias agrupadas por valor + segmento** (não por componente técnico)
   - Métricas-alvo (KPI baseline → target por tela/passo)
   - Riscos abertos para favo 03
4. Gerar `historias.yaml` — uma entrada por história com:
   - `historia_id`, `valor`, `segmento`, `quem/quero/para`
   - `hipotese_ref`, `kr_ref`, `prototipo_ref`
   - `criterios_aceitacao` (comportamental, linguagem de cliente)
   - `sinais_sucesso` (KPI específico)
5. Proibido:
   - História sem `valor` ou `segmento` → `DIS-STORY-01`
   - História com decisão técnica → `DIS-STORY-02`
6. Este é o **entregável do Gate 02** — pacote pronto para handoff 02→03
