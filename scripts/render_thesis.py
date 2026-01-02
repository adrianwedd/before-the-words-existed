#!/usr/bin/env python3
"""Render thesis HTML/PDF from Before-the-Words-Existed.md."""

from pathlib import Path

import markdown
from weasyprint import HTML


def render_html(markdown_path: Path, html_path: Path) -> None:
    src = markdown_path.read_text(encoding="utf-8")
    # Convert markdown into a single HTML body we can wrap with layout + metadata.
    html_body = markdown.markdown(src, extensions=["tables", "fenced_code"])
    description = (
        "A literary analysis of William Gibson's Neuromancer arguing that "
        "Case's cognition coheres with interface access, anticipating later "
        "vocabulary for cognitive mismatch."
    )
    # Canonical URL for preview cards and search engines.
    canonical_url = "https://adrianwedd.github.io/before-the-words-existed/thesis.html"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Before the Words Existed: Neuromancer and the Experience of Cognitive Mismatch</title>
  <meta name="description" content="{description}">
  <meta name="author" content="Adrian Wedd">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="Before the Words Existed: Neuromancer and the Experience of Cognitive Mismatch">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Before the Words Existed: Neuromancer and the Experience of Cognitive Mismatch">
  <meta name="twitter:description" content="{description}">
  <style>
:root {{
  --bg: #0a0a0a;
  --text: #e0e0e0;
  --accent: #00ff00;
  --muted: #666;
  --highlight: #141414;
}}
* {{ box-sizing: border-box; }}
html {{ background: var(--bg); }}
body {{
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: 'Courier New', monospace;
  line-height: 1.7;
}}
main {{
  max-width: 900px;
  margin: 0 auto;
  padding: 2.5rem 2rem 4rem;
}}
header {{
  border-bottom: 1px solid var(--accent);
  margin-bottom: 2rem;
  padding-bottom: 1.25rem;
}}
header h2 {{ margin: 0 0 0.5rem 0; color: var(--accent); font-size: 2.2rem; font-weight: 400; }}
header p {{ margin: 0; color: var(--muted); }}
.abstract {{ margin-top: 0.75rem; color: var(--text); }}
nav {{
  margin: 1.5rem 0 2.5rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}}
a {{ color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent; }}
a:hover {{ border-bottom-color: var(--accent); }}

h1, h2, h3, h4 {{ color: var(--accent); font-weight: 400; }}
h1 {{ font-size: 2rem; }}
h2 {{ font-size: 1.5rem; margin-top: 2rem; }}
h3 {{ font-size: 1.2rem; margin-top: 1.5rem; }}

p {{ margin: 0 0 1rem; }}
ul, ol {{ margin: 0 0 1rem 1.5rem; }}
li {{ margin-bottom: 0.4rem; }}
blockquote {{
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  background: var(--highlight);
  border-left: 3px solid var(--accent);
  font-style: italic;
}}
code {{
  background: var(--highlight);
  padding: 0.1rem 0.3rem;
}}
pre {{
  background: var(--highlight);
  padding: 1rem;
}}
hr {{ border: none; border-top: 1px solid var(--muted); margin: 2rem 0; }}

@media print {{
  nav {{ display: none; }}
  html, body {{ background: var(--bg); }}
}}

@page {{
  margin: 0;
}}
  </style>
</head>
<body>
  <main>
    <header>
      <h2>Before the Words Existed</h2>
      <p>Neuromancer and the Experience of Cognitive Mismatch</p>
      <p class="abstract">A close reading of <em>Neuromancer</em> that tracks how attention, time, and agency change with interface access, and why the novel anticipates later language for cognitive mismatch.</p>
    </header>
    <nav>
      <a href="index.html">Home</a>
      <a href="Before-the-Words-Existed.pdf">Download PDF</a>
    </nav>
    {html_body}
  </main>
</body>
</html>
"""
    html_path.write_text(html, encoding="utf-8")


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    # Render with full-bleed settings defined in the HTML @page styles.
    HTML(str(html_path)).write_pdf(str(pdf_path))


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    # Source thesis and rendered outputs.
    markdown_path = repo_root / "Before-the-Words-Existed.md"
    html_path = repo_root / "docs" / "thesis.html"
    pdf_path = repo_root / "docs" / "Before-the-Words-Existed.pdf"

    render_html(markdown_path, html_path)
    render_pdf(html_path, pdf_path)


if __name__ == "__main__":
    main()
