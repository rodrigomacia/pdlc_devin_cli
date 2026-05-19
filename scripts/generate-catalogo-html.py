#!/usr/bin/env python3
"""Gera docs/catalogo-skills.html a partir de .devin/skills/*/SKILL.md"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".devin" / "skills"
OUT = ROOT / "docs" / "catalogo-skills.html"

GROUPS = [
    ("00 — Orquestração", lambda n: n == "orquestrar-producao"),
    ("01 — Contexto", lambda n: any(x in n for x in ("okr", "draft", "desdobrar", "auditar", "sync"))),
    ("02 — Discovery", lambda n: any(x in n for x in ("visao", "sintetizar", "hipoteses", "svm", "prototipo", "feature", "prep-entrevista"))),
    ("03 — Experimentação", lambda n: any(x in n for x in ("experiment", "registrar", "decidir", "design"))),
    ("04 — Construção", lambda n: any(x in n for x in ("spec", "implementar", "tarefa", "ci-", "cd-", "rollout", "prep-release", "review-pr", "pipeline", "decompor"))),
    ("05 — Operação", lambda n: any(x in n for x in ("ert-", "review-metricas", "postmortem", "insight"))),
    ("Transversal", lambda n: any(x in n for x in ("grill", "governanca", "curar"))),
]


def favo_for(name: str) -> str:
    for label, pred in GROUPS:
        if pred(name):
            return label
    return "Outros"


def main() -> None:
    skills = []
    for p in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        name = p.parent.name
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^description:\s*(.+)$", text, re.M)
        desc = m.group(1).strip() if m else ""
        skills.append((name, desc))

    rows_by_favo: dict[str, list[tuple[str, str]]] = {}
    for n, d in skills:
        rows_by_favo.setdefault(favo_for(n), []).append((n, d))

    order = [g[0] for g in GROUPS] + ["Outros"]
    parts = []
    for f in order:
        if f not in rows_by_favo:
            continue
        parts.append(f'    <h2 class="section-title">{f}</h2>')
        parts.append("    <table><thead><tr><th>Comando</th><th>Descrição</th></tr></thead><tbody>")
        for n, d in sorted(rows_by_favo[f]):
            esc = d.replace("&", "&amp;").replace("<", "&lt;")
            parts.append(f"      <tr><td><code>/{n}</code></td><td>{esc or '—'}</td></tr>")
        parts.append("    </tbody></table>")

    body = "\n".join(parts)
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Catálogo de Skills — Ciclo de Produtação Digital</title>
  <link rel="stylesheet" href="assets/site.css" />
</head>
<body>
  <header class="site-header">
    <a href="index.html" class="site-logo">🍯 Ciclo de Produtação Digital</a>
    <nav class="site-nav">
      <a href="guia-inicio.html">Começar</a>
      <a href="configuracao.html">Configurar</a>
      <a href="catalogo-skills.html">Skills</a>
      <a href="apresentacao-executiva.html">Executivo</a>
    </nav>
  </header>
  <main>
    <p class="breadcrumb"><a href="index.html">Início</a> / Catálogo de skills</p>
    <h1 style="font-size:1.85rem;margin-bottom:0.5rem">Catálogo de skills ({len(skills)})</h1>
    <p style="color:var(--muted);margin-bottom:2rem">
      Gerado de <code>.devin/skills/</code>.
      Matriz gates: <a href="colmeia/00-nucleo/catalogo-skills.md">catalogo-skills.md</a>.
    </p>
{body}
  </main>
  <footer><a href="index.html">← Voltar ao início</a></footer>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"✓ {OUT} ({len(skills)} skills)")


if __name__ == "__main__":
    main()
