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
  <meta name="theme-color" content="#06070d" />
  <title>Catálogo de Skills — PDLC</title>
  <link rel="stylesheet" href="assets/site.css" />
</head>
<body>
  <div class="hex-bg" aria-hidden="true"></div>
  <header class="site-header">
    <a href="index.html" class="site-logo"><span class="logo-mark">⬡</span> PDLC</a>
    <button class="nav-toggle" type="button" aria-label="Menu">☰</button>
    <nav class="site-nav">
      <a href="guia-inicio.html">Começar</a>
      <a href="configuracao.html">Configurar</a>
      <a href="catalogo-skills.html">Skills</a>
      <a href="apresentacao-executiva.html">Executivo</a>
      <a href="https://github.com/rodrigomacia/pdlc_devin_cli" target="_blank" rel="noopener">GitHub</a>
    </nav>
  </header>
  <main>
    <p class="breadcrumb"><a href="index.html">Início</a> / Skills</p>
    <div class="page-hero">
      <h1>Catálogo de skills ({len(skills)})</h1>
      <p>Gerado de <code>.devin/skills/</code> · Matriz gates em <a href="colmeia/00-nucleo/catalogo-skills.md">catalogo-skills.md</a></p>
    </div>
{body}
  </main>
  <footer class="site-footer"><div class="footer-inner"><a href="index.html" class="footer-brand">← Início</a></div></footer>
  <script src="assets/site.js"></script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"✓ {OUT} ({len(skills)} skills)")


if __name__ == "__main__":
    main()
