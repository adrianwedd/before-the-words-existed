# Scripts

## verify_openlibrary.py

Query Open Library for publication metadata (publisher/place/year).

Example:

```
python scripts/verify_openlibrary.py "Neuromancer William Gibson" "Hackers Steven Levy 1984"
```

Notes:
- Requires network access.
- Returns the top three matches with basic fields.

## render_thesis.py

Render the thesis HTML and PDF from `Before-the-Words-Existed.md`.

Example:

```
python scripts/render_thesis.py
```

Notes:
- Requires `markdown` and `weasyprint` to be installed.

## check_paths.py

Verify that `README.md` and `reference/structure.md` reference the expected
`analysis/` paths.

Example:

```
python scripts/check_paths.py
```
