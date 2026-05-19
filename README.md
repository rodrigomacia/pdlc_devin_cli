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

## Instalação (primeira vez)

**Clonar o repositório é uma vez só** — não precisa repetir no dia a dia. Depois disso, você só abre o **Devin** na pasta do projeto.

| Situação | O que fazer |
|----------|-------------|
| **Você vai instalar** (ou é a primeira vez no Mac) | Siga os passos abaixo (~30–60 min) |
| **A TI já configurou** | Pule para [Uso diário](#uso-diário-head) |
| **Prefere guia passo a passo** | [GUIA-HEAD.md](GUIA-HEAD.md) · [versão web](https://rodrigomacia.github.io/pdlc_devin_cli/guia-inicio.html) |

### 1. Instalar o Devin CLI

O PDLC roda dentro do [Devin CLI](https://cli.devin.ai) — é o “terminal com IA” onde você digita os comandos do ciclo.

**macOS / Linux** (cole no Terminal):

```bash
curl -fsSL https://cli.devin.ai/install.sh | bash
```

Confirme que instalou:

```bash
devin --version
```

Mais opções e troubleshooting: [cli.devin.ai](https://cli.devin.ai)

### 2. Baixar o PDLC

Escolha uma pasta no seu Mac (ex.: `Documentos`) e rode:

```bash
cd ~/Documentos
git clone https://github.com/rodrigomacia/pdlc_devin_cli.git
cd pdlc_devin_cli
```

> Sem `git`? Instale com [git-scm.com](https://git-scm.com/) ou peça à TI para copiar a pasta do repositório para o seu computador.

### 3. Preparar o ambiente (script automático)

Na pasta do projeto:

```bash
chmod +x scripts/setup-devin-cli.sh
./scripts/setup-devin-cli.sh
```

O script:

- valida skills e agentes do ciclo;
- cria pastas para **suas iniciativas** (`_iniciativas/`, handoffs, grill);
- gera `.devin/config.local.json` a partir do exemplo.

### 4. Conectar ferramentas da empresa

Edite (com apoio de TI, se precisar) os templates em `colmeia/_config/`:

| Arquivo | Para quê |
|---------|----------|
| `okr-plataforma.md` | Metas e OKRs da Plataforma |
| `discovery-tools.md` | VOC, analytics, personas sintéticas, Figma |
| `construcao-monorepo.md` | Repositório de código, CI/CD, ambientes |

Opcional: MCP e integrações em `.devin/config.local.json`.

Roteiro técnico completo: [configuração](https://rodrigomacia.github.io/pdlc_devin_cli/configuracao.html)

### 5. Abrir o Devin e iniciar uma iniciativa

Ainda na pasta `pdlc_devin_cli`:

```bash
devin
```

Na conversa, digite (troque o nome da sua iniciativa):

```
/orquestrar-producao conta-digital-q3-2026
```

O assistente mostra a etapa atual, o próximo passo e o que falta — marcado como `[FORNECER]` quando precisar de um dado seu.

---

## Uso diário (Head)

**Precisa clonar de novo? Não.**

1. Abra o **Devin** na pasta `pdlc_devin_cli` (a mesma do setup).
2. Digite `/orquestrar-producao {sua-iniciativa}`.
3. Responda com dados de negócio quando o assistente pedir — metas, entrevistas, aprovações.

Comandos que o Head usa com frequência:

| Comando | Quando |
|---------|--------|
| `/orquestrar-producao {id}` | Ver onde está e o que fazer agora |
| `/grill-me {id} {momento}` | Revisão crítica antes de decidir |
| `/decidir-experimento {id}` | Depois dos testes com clientes reais |
| `/validar-rollout-head {id}` | Validar métricas após canário em produção |

Lista completa: [catálogo de skills](https://rodrigomacia.github.io/pdlc_devin_cli/catalogo-skills.html)

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

**GitHub:** [github.com/rodrigomacia/pdlc_devin_cli](https://github.com/rodrigomacia/pdlc_devin_cli) · Instalação: [passos acima](#instalação-primeira-vez)

Licença [MIT](LICENSE) · Contribuições bem-vindas.

<details>
<summary><strong>Referência técnica</strong> (times de engenharia)</summary>

- **46 skills** e **32 agentes** em `.devin/`
- Contratos de fluxo, gates e templates em `colmeia/`
- Ordem favo 04: spec → implementar → **review-pr** → CI/CD → rollout canário
- Catálogo: [`colmeia/00-nucleo/catalogo-skills.md`](colmeia/00-nucleo/catalogo-skills.md)

</details>
