#!/usr/bin/env python3
"""Render print-ready PDF from Before-the-Words-Existed-print.md.

Produces a 5.5 x 8.5 inch trade paperback PDF suitable for
print-on-demand via Books.by or similar services.
"""

from pathlib import Path

import markdown
from weasyprint import HTML


def render_print_html(markdown_path: Path, html_path: Path) -> None:
    src = markdown_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        src, extensions=["tables", "fenced_code", "md_in_html"]
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Before the Words Existed</title>
  <style>
/* ==========================================================
   PRINT-READY BOOK STYLES — 5.5 x 8.5 in Trade Paperback
   ========================================================== */

@page {{
  size: 5.5in 8.5in;
  margin-top: 0.75in;
  margin-bottom: 0.75in;
  margin-outside: 0.75in;
  margin-inside: 0.875in;

  @bottom-center {{
    content: counter(page);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 9pt;
    color: #555;
  }}
}}

/* Frontmatter pages: no page numbers, centered content */
@page frontmatter {{
  size: 5.5in 8.5in;
  margin: 0.75in;
  margin-inside: 0.875in;
  @bottom-center {{ content: none; }}
}}

/* First page of body: suppress header */
@page chapter-start {{
  size: 5.5in 8.5in;
  margin-top: 1.5in;
  margin-bottom: 0.75in;
  margin-outside: 0.75in;
  margin-inside: 0.875in;
  @bottom-center {{
    content: counter(page);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 9pt;
    color: #555;
  }}
}}

/* ==========================================================
   BASE TYPOGRAPHY
   ========================================================== */

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

html {{
  font-size: 11pt;
}}

body {{
  font-family: Georgia, 'Times New Roman', serif;
  line-height: 1.6;
  color: #1a1a1a;
  background: #fff;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}}

/* ==========================================================
   FRONTMATTER PAGES
   ========================================================== */

.half-title-page {{
  page: frontmatter;
  page-break-after: always;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  padding-top: 2.5in;
  text-align: center;
}}

.half-title-page h1 {{
  font-size: 20pt;
  font-weight: 400;
  letter-spacing: 0.04em;
  color: #1a1a1a;
  border: none;
  margin: 0;
  padding: 0;
}}

.blank-page {{
  page: frontmatter;
  page-break-after: always;
  visibility: hidden;
  min-height: 1px;
}}

.title-page {{
  page: frontmatter;
  page-break-after: always;
  padding-top: 1.8in;
  text-align: center;
}}

.title-page h1 {{
  font-size: 24pt;
  font-weight: 400;
  letter-spacing: 0.04em;
  margin-bottom: 0.4in;
  color: #1a1a1a;
  border: none;
}}

.title-page h2 {{
  font-size: 13pt;
  font-weight: 400;
  font-style: italic;
  color: #444;
  margin-bottom: 1.2in;
  letter-spacing: 0.02em;
  border: none;
  padding: 0;
  page-break-before: avoid;
  margin-top: 0;
}}

.title-page p {{
  font-size: 12pt;
  color: #333;
  margin: 0;
}}

.copyright-page {{
  page: frontmatter;
  page-break-after: always;
  padding-top: 4in;
  font-size: 8.5pt;
  line-height: 1.5;
  color: #555;
}}

.copyright-page strong {{
  display: block;
  margin-bottom: 0.8em;
  font-size: 9pt;
  color: #333;
}}

.copyright-page p {{
  margin-bottom: 0.6em;
}}

.epigraph-page {{
  page: frontmatter;
  page-break-after: always;
  padding-top: 2.5in;
}}

.epigraph-page blockquote {{
  border-left: none;
  padding: 0;
  margin: 0 0.5in;
  font-style: italic;
  font-size: 11pt;
  line-height: 1.7;
  color: #333;
  background: none;
}}

.toc-page {{
  page: frontmatter;
  page-break-after: always;
}}

.toc-page h2 {{
  font-size: 16pt;
  font-weight: 400;
  letter-spacing: 0.05em;
  margin-bottom: 0.5in;
  text-align: center;
  border: none;
  padding: 0;
  margin-top: 0.8in;
  color: #1a1a1a;
}}

.toc-page ol {{
  list-style: decimal;
  padding: 0;
  margin: 0 0 0 1.5em;
}}

.toc-page ol li {{
  font-size: 10.5pt;
  line-height: 2;
  color: #333;
  padding-left: 0;
  hyphens: none;
  text-align: left;
}}

.toc-page p {{
  font-size: 10.5pt;
  line-height: 2;
  color: #333;
  margin-top: 0.3in;
  padding-left: 0;
  hyphens: none;
  text-align: left;
}}

/* ==========================================================
   BODY TEXT START — reset page counter
   ========================================================== */

.body-start {{
  counter-reset: page 1;
}}

/* ==========================================================
   HEADINGS
   ========================================================== */

h1 {{
  font-size: 22pt;
  font-weight: 400;
  letter-spacing: 0.03em;
  color: #1a1a1a;
  margin-top: 0;
  margin-bottom: 0.3in;
  border-bottom: 0.5pt solid #ccc;
  padding-bottom: 0.15in;
}}

h2 {{
  font-size: 14pt;
  font-weight: 600;
  color: #1a1a1a;
  margin-top: 0.15in;
  margin-bottom: 0.25in;
  page-break-before: always;
  padding-top: 0.6in;
  border-bottom: 0.5pt solid #ddd;
  padding-bottom: 0.1in;
}}

/* Don't break before the very first h2 if it follows body-start */
.body-start + h2 {{
  page-break-before: avoid;
}}

h3 {{
  font-size: 12pt;
  font-weight: 600;
  color: #333;
  margin-top: 0.3in;
  margin-bottom: 0.15in;
}}

/* ==========================================================
   BODY TEXT
   ========================================================== */

p {{
  margin-bottom: 0.8em;
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;
  orphans: 3;
  widows: 3;
}}

/* ==========================================================
   BLOCKQUOTES
   ========================================================== */

blockquote {{
  margin: 1em 0;
  padding: 0.1in 0 0.1in 0.3in;
  border-left: 2pt solid #999;
  font-style: italic;
  color: #333;
  background: none;
}}

blockquote p {{
  margin-bottom: 0.5em;
}}

/* ==========================================================
   LISTS
   ========================================================== */

ul, ol {{
  margin: 0.5em 0 1em 1.5em;
}}

li {{
  margin-bottom: 0.3em;
  line-height: 1.5;
}}

/* ==========================================================
   TABLES (Appendix A timeline)
   ========================================================== */

table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 9pt;
  line-height: 1.4;
  page-break-inside: auto;
}}

thead {{
  display: table-header-group;
}}

tr {{
  page-break-inside: avoid;
}}

th {{
  background: #f5f5f5;
  border-bottom: 1pt solid #999;
  padding: 0.15in 0.1in;
  text-align: left;
  font-weight: 600;
  font-size: 8.5pt;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #333;
}}

td {{
  padding: 0.1in 0.1in;
  border-bottom: 0.5pt solid #ddd;
  vertical-align: top;
  color: #1a1a1a;
}}

/* Bold year in timeline */
td strong {{
  color: #000;
}}

/* ==========================================================
   EMPHASIS & INLINE
   ========================================================== */

em {{
  font-style: italic;
}}

strong {{
  font-weight: 700;
}}

/* ==========================================================
   HORIZONTAL RULES (section dividers)
   ========================================================== */

hr {{
  border: none;
  border-top: 0.5pt solid #ccc;
  margin: 1.5em 0;
}}

/* ==========================================================
   REFERENCES
   ========================================================== */

.references-page ~ h2 {{
  page-break-before: always;
}}

/* Hanging indent for bibliography entries */
.references-page ~ h2 + p,
.references-page ~ p {{
  padding-left: 0.4in;
  text-indent: -0.4in;
  font-size: 10pt;
  line-height: 1.5;
  margin-bottom: 0.6em;
  text-align: left;
}}

/* ==========================================================
   APPENDICES
   ========================================================== */

.appendix-start ~ h2 {{
  page-break-before: always;
  font-size: 13pt;
}}

.appendix-start ~ p {{
  font-size: 10.5pt;
}}

/* ==========================================================
   ABOUT THE AUTHOR
   ========================================================== */

.about-page {{
  page-break-before: always;
}}

.about-page ~ h2 {{
  text-align: center;
  border: none;
  padding-top: 1.5in;
}}

.about-page ~ p {{
  text-align: center;
  font-size: 10.5pt;
  line-height: 1.7;
  max-width: 3.5in;
  margin: 0 auto;
}}

/* ==========================================================
   PRINT SAFEGUARDS
   ========================================================== */

a {{
  color: inherit;
  text-decoration: none;
}}

img {{
  max-width: 100%;
}}

/* Prevent breaks after headings */
h1, h2, h3, h4 {{
  page-break-after: avoid;
}}

/* Keep blockquotes together */
blockquote {{
  page-break-inside: avoid;
}}

  </style>
</head>
<body>
{html_body}
</body>
</html>
"""
    html_path.write_text(html, encoding="utf-8")


def render_print_pdf(html_path: Path, pdf_path: Path) -> None:
    HTML(str(html_path)).write_pdf(str(pdf_path))


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    markdown_path = repo_root / "Before-the-Words-Existed-print.md"
    html_path = repo_root / "docs" / "print-edition.html"
    pdf_path = repo_root / "docs" / "Before-the-Words-Existed-print.pdf"

    print("Rendering print-edition HTML...")
    render_print_html(markdown_path, html_path)
    print(f"  -> {html_path}")

    print("Rendering print-edition PDF (5.5 x 8.5 trade paperback)...")
    render_print_pdf(html_path, pdf_path)
    print(f"  -> {pdf_path}")

    # Report page count
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        print(f"\nPage count: {len(reader.pages)}")
    except ImportError:
        print("\nInstall pypdf to see page count: pip install pypdf")


if __name__ == "__main__":
    main()
