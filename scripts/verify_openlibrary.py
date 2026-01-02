#!/usr/bin/env python3
"""Lookup publication details via Open Library search.

Usage:
  python scripts/verify_openlibrary.py "query string" "another query"

Notes:
- Intended to verify publisher/place/year for references.
- Network access required.
"""

import json
import sys
import urllib.parse
import urllib.request


def search(query: str, limit: int = 3) -> dict:
    # Open Library search endpoint; limit is applied on output for clarity.
    url = "https://openlibrary.org/search.json?q=" + urllib.parse.quote(query)
    with urllib.request.urlopen(url, timeout=20) as resp:
        return json.load(resp)


def main() -> int:
    queries = sys.argv[1:]
    if not queries:
        print("Usage: python scripts/verify_openlibrary.py \"query\" [...]")
        return 1

    for q in queries:
        try:
            data = search(q)
        except Exception as exc:
            print(f"ERROR: {q}: {exc}")
            continue

        docs = data.get("docs", [])
        print(f"\nQUERY: {q}")
        if not docs:
            print("  No results")
            continue

        # Report the top matches with core bibliographic fields.
        for doc in docs[:3]:
            title = doc.get("title")
            author = ", ".join(doc.get("author_name", [])[:2])
            year = doc.get("first_publish_year")
            publisher = ", ".join(doc.get("publisher", [])[:2])
            place = ", ".join(doc.get("publish_place", [])[:2])
            isbn = ", ".join(doc.get("isbn", [])[:2])
            print(f"  - {title} | {author} | {year} | {publisher} | {place} | {isbn}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
