# Guia do Head de Produto — Como começar (sem jargão técnico)

Este guia é para **você**, Head de Produto. Não precisa saber programar.

---

## Preciso clonar o repositório?

**Na rotina do dia a dia: não.**

| Situação | O que fazer |
|----------|-------------|
| A TI já abriu a pasta do PDLC no seu Devin | Só abrir o Devin e começar (vá para [Seu passo a passo](#seu-passo-a-passo-head)) |
| É a primeira vez na empresa / no seu computador | Alguém da **TI ou Engenharia** faz o [setup único](#setup-único-uma-vez) — ou siga o roteiro com apoio deles |
| Você quer instalar sozinho | Peça acesso ao [repositório](https://github.com/rodrigomacia/pdlc_devin_cli) e siga o setup único abaixo |

**Clonar** = baixar o pacote de regras do ciclo para o seu computador **uma vez**. Depois disso, você só **abre o Devin** nessa pasta.

---

## Setup único (uma vez)

Quem costuma fazer: **TI, plataforma ou um analista de ferramentas** — leva cerca de 30–60 minutos.

1. Instalar o **Devin CLI** → [cli.devin.ai](https://cli.devin.ai)
2. **Baixar o projeto** (comando que a TI roda no terminal):
   ```
   git clone https://github.com/rodrigomacia/pdlc_devin_cli.git
   ```
3. Rodar o script de preparação (na pasta do projeto):
   ```
   ./scripts/setup-devin-cli.sh
   ```
4. Preencher conexões com **Plataforma OKR**, **dados de cliente** e **analytics** (arquivos em `colmeia/_config/` — a TI ajuda)
5. Pronto. Avise o Head: *“pode abrir o Devin na pasta pdlc_devin_cli”*.

Detalhes técnicos: [docs/configuracao.html](docs/configuracao.html)

---

## Seu passo a passo (Head)

### Antes de começar

Tenha em mãos (pode ser em texto simples na conversa):

- Nome da **iniciativa** (ex.: `conta-digital-q3-2026`)
- **Diretriz** ou prioridade do trimestre
- Acesso aos **OKRs** e, quando pedido, números de **métricas** e **feedback de clientes**

### Passo 1 — Abrir o Devin

Abra o **Devin** (aplicativo de terminal com IA) na pasta do projeto que a TI configurou.

Se não souber qual pasta: pergunte à TI *“onde está o PDLC / pdlc_devin_cli?”*.

### Passo 2 — Iniciar sua iniciativa

Na conversa com o Devin, digite (troque o nome):

```
/orquestrar-producao conta-digital-q3-2026
```

O assistente diz:

- em qual **etapa** do ciclo você está;
- qual **comando** usar em seguida;
- o que está **faltando** — marcado como `[FORNECER]`.

**Sua função:** responder com informações de negócio (metas, dados de cliente, decisões). Não precisa escrever código.

### Passo 3 — Seguir as etapas do ciclo

O assistente vai sugerir comandos nesta ordem geral:

| Etapa | O que você faz (em linguagem simples) |
|-------|--------------------------------------|
| **1. Contexto** | Alinha OKRs e metas com a estratégia |
| **2. Descoberta** | Entende mercado, produto e cliente; monta hipóteses e protótipo |
| **3. Experimentação** | **Você** testa com clientes reais; informa os resultados |
| **4. Construção** | Aprova o que o cliente vai ver; valida o lançamento gradual |
| **5. Operação** | Acompanha se as metas moveram; decide novos ciclos |

Em cada **portão de decisão**, o assistente pode fazer perguntas difíceis (`/grill-me`). Responda com honestidade — é para evitar decisão fraca.

### Passo 4 — Quando o assistente pedir dados

Exemplos do que colar na conversa:

- *“O KR de conversão está em 12%, meta 18%”*
- *“Fizemos 8 entrevistas; 6 confirmaram a dor X”*
- *“Aprovo seguir para construção — evidência suficiente”*

Se aparecer `[FORNECER]` ou `[RESULTADO: fornecer]`, é sinal de que **falta um dado seu** — o assistente não inventa números.

### Passo 5 — Aprovar e avançar

Quando uma etapa terminar, o assistente sugere passar para a próxima. Você **aprova** (ou pede ajuste).

Comandos que o Head usa com frequência:

| Você digita | Para quê |
|-------------|----------|
| `/orquestrar-producao {nome}` | Ver onde está e o que fazer agora |
| `/grill-me {nome} {momento}` | Revisão crítica antes de decidir |
| `/decidir-experimento {nome}` | Depois dos testes com clientes |
| `/validar-rollout-head {nome}` | Validar métricas após canário em produção |

Lista completa: [documentação online](https://rodrigomacia.github.io/pdlc_devin_cli/catalogo-skills.html)

---

## O que você **não** precisa fazer

- Escrever ou ler código
- Rodar `git`, pipeline ou deploy (etapa 4 é com Engenharia + assistente)
- Clonar o repositório todo dia
- Decorar os 46 comandos — use `/orquestrar-producao` e siga as sugestões

---

## Ajuda rápida

| Dúvida | Resposta curta |
|--------|----------------|
| Clono todo dia? | **Não.** Só na primeira vez (setup). |
| O que abro toda manhã? | **Devin** na pasta do PDLC. |
| Primeiro comando? | `/orquestrar-producao {sua-iniciativa}` |
| Quem configura OKR e analytics? | **TI** no setup único. |
| Onde está a visão executiva? | [Apresentação para comitê](docs/apresentacao-executiva.html) |

**Documentação visual:** [rodrigomacia.github.io/pdlc_devin_cli](https://rodrigomacia.github.io/pdlc_devin_cli)
