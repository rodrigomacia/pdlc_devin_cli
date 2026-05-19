# PDLC — Ciclo de Produtação Digital

**Do OKR ao cliente em produção — com decisões claras, evidência real e o Head de Produto no centro.**

O PDLC é um sistema open source que combina **processo de Go-to-Market**, **portões de decisão** e **assistentes de IA** (via [Devin CLI](https://cli.devin.ai)) para conduzir iniciativas de produto digital sem improviso e sem construir cedo demais.

[![Documentação](https://img.shields.io/badge/docs-site-00e5b8)](https://rodrigomacia.github.io/pdlc_devin_cli/)
[![Guia Head](https://img.shields.io/badge/guia-Head%20de%20Produto-8b7cff)](GUIA-HEAD.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## O problema que resolve

| Hoje (sem ciclo) | Com PDLC |
|------------------|----------|
| Ideia vira projeto antes de prova com cliente | Só escala após **evidência real** |
| Simulação confundida com validação | Três momentos de validação **explícitos** |
| Ninguém sabe quem aprova o quê | **Head de Produto** decide; IA executa e questiona |
| Aprendizado da operação não volta ao discovery | Loop contínuo: operação → nova oportunidade |

---

## Para quem é

**Head de Produto (Go-to-Market)** — dono da iniciativa ponta a ponta: estratégia, discovery, experimento com clientes, aprovação do que vai ao ar e leitura de resultados.

A IA não substitui sua decisão. Ela **pesquisa, redige, organiza e desafia** — você fornece contexto, números e o “sim” ou “não” em cada portão.

Times de **TI e Engenharia** entram na preparação do ambiente (uma vez) e na construção em escala (etapa 4).

---

## Como funciona (visão de produto)

```text
Estratégia → Descoberta → Teste com clientes → Construção → Operação
     ①            ②              ③                 ④           ⑤
                                                      ↓
                                              (volta para ②)
```

| Etapa | O que acontece | Entregável de negócio |
|-------|----------------|------------------------|
| **1. Contexto** | Metas alinhadas à estratégia (OKR) | Prioridade clara do trimestre |
| **2. Descoberta** | Mercado + produto + cliente → hipóteses e protótipo | Pacote **candidato** (ainda não vai para engenharia) |
| **3. Experimentação** | **Você** testa com pessoas reais | Decisão: escalar, ajustar ou encerrar |
| **4. Construção** | Spec do que o cliente vê + lançamento gradual | Produto em produção com validação no canário |
| **5. Operação** | Métricas, incidentes, aprendizados | Insights para o próximo ciclo |

Em cada transição há um **portão**: critérios objetivos + revisor crítico (“grill-me”) antes do Head aprovar.

---

## Três validações (não confundir)

| Momento | Custo | O que prova |
|---------|-------|-------------|
| **Descoberta** — personas sintéticas + protótipo | Baixo | Se a ideia merece teste real |
| **Experimentação** — clientes reais | Médio | Se vale investir em construção |
| **Canário em produção** — grupo pequeno de clientes | Controlado | Se o KPI move no mundo real |

Pular a etapa 3 é a principal fonte de desperdício que o PDLC evita.

---

## Começar em 2 minutos (Head)

**Precisa clonar o repositório todo dia? Não.**

1. Abra o **Devin** na pasta que a TI configurou.
2. Digite (troque o nome da sua iniciativa):

   ```
   /orquestrar-producao conta-digital-q3-2026
   ```

3. Siga o que o assistente sugerir — responda com dados de negócio quando pedir.

**Guia completo (sem jargão técnico):** [GUIA-HEAD.md](GUIA-HEAD.md) · [versão web](https://rodrigomacia.github.io/pdlc_devin_cli/guia-inicio.html)

---

## Preparação única (TI — primeira vez)

Antes do Head usar o ciclo, alguém de **TI ou plataforma** prepara o ambiente (~30–60 min):

1. Instalar [Devin CLI](https://cli.devin.ai)
2. Baixar este repositório
3. Rodar `./scripts/setup-devin-cli.sh`
4. Conectar Plataforma OKR, VOC, analytics e pipeline (templates em `colmeia/_config/`)

Roteiro técnico: [configuração](docs/configuracao.html)

---

## Documentação

| Público | Onde |
|---------|------|
| **Head de Produto** | [Como começar](GUIA-HEAD.md) · [Fluxo Head × Devin](docs/fluxo-head-produto-devin.html) |
| **Comitê / liderança** | [Apresentação executiva](docs/apresentacao-executiva.html) |
| **Portal completo** | [rodrigomacia.github.io/pdlc_devin_cli](https://rodrigomacia.github.io/pdlc_devin_cli/) |
| **Times técnicos** | [Mapa de skills](colmeia/00-nucleo/catalogo-skills.md) · [Arquitetura do fluxo](docs/fluxo-producao.html) |

---

## Princípios do produto

1. **Head decide** — IA propõe, você aprova portões.
2. **Evidência antes de escala** — construção em grande volume só após cliente real.
3. **Revisor crítico sempre** — grill-me em hipóteses, features e decisões caras.
4. **Rastreabilidade** — da meta estratégica à métrica em produção.
5. **Sem produto fictício no git** — artefatos das suas iniciativas ficam na sua máquina, não no repositório público.

---

## Repositório

**GitHub:** [github.com/rodrigomacia/pdlc_devin_cli](https://github.com/rodrigomacia/pdlc_devin_cli)

```bash
git clone https://github.com/rodrigomacia/pdlc_devin_cli.git
```

Licença [MIT](LICENSE) · Contribuições bem-vindas.

<details>
<summary><strong>Referência técnica</strong> (times de engenharia)</summary>

- **46 skills** e **32 agentes** em `.devin/`
- Contratos de fluxo, gates e templates em `colmeia/`
- Ordem favo 04: spec → implementar → **review-pr** → CI/CD → rollout canário
- Catálogo: [`colmeia/00-nucleo/catalogo-skills.md`](colmeia/00-nucleo/catalogo-skills.md)

</details>
