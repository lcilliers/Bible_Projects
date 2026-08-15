"""Search prose_section across all prose books.

Examples:
  python scripts/search_prose.py grace
  python scripts/search_prose.py "inner being" --book Programme
    python scripts/search_prose.py grace --out outputs/markdown/grace-prose-search.md
    python scripts/search_prose.py 'grace OR mercy' --fts

The query uses SQLite FTS5 syntax. Results are limited to active,
non-superseded prose sections and include their hierarchy and provenance.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("database/bible_research.db")
DEFAULT_OUT_DIR = Path("outputs/markdown")
DEFAULT_LIMIT = 100


def open_db(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def search_prose(
    conn: sqlite3.Connection,
    query: str,
    book: str | None = None,
    limit: int = DEFAULT_LIMIT,
    raw_fts: bool = False,
) -> tuple[list[sqlite3.Row], int]:
    book_clause = ""
    # Plain input is treated as literal text. Use --fts for MATCH expressions.
    fts_query = query if raw_fts else f'"{query.replace(chr(34), chr(34) + chr(34))}"'
    params: list[object] = [fts_query]
    if book is not None:
        book_clause = "AND lower(pst.book_label) = lower(?)"
        params.append(book.strip())
    params.append(limit)

    where_sql = f"""
        FROM prose_section_fts
        JOIN prose_section ps ON ps.id = prose_section_fts.rowid
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE prose_section_fts MATCH ?
          AND COALESCE(ps.delete_flagged, 0) = 0
          AND ps.superseded_by_id IS NULL
          AND COALESCE(pst.delete_flagged, 0) = 0
          {book_clause}
    """
    total_params = params[:-1]
    total_matches = conn.execute(
        f"SELECT COUNT(*) {where_sql}", total_params
    ).fetchone()[0]

    rows = conn.execute(
        f"""
        SELECT
            ps.id,
            ps.heading,
            ps.status,
            ps.version,
            ps.author,
            ps.source_file,
            pst.source_stage,
            pst.book_order,
            pst.book_label,
            pst.section_order,
            pst.section_label,
            pst.chapter_no,
            pst.label AS chapter_title,
            pst.sort_order,
            snippet(prose_section_fts, 0, '**', '**', ' ... ', 36) AS context,
            bm25(prose_section_fts) AS relevance
        {where_sql}
        ORDER BY relevance, pst.book_order, pst.section_order,
                 pst.chapter_no, pst.sort_order, ps.id
        LIMIT ?
        """,
        params,
    ).fetchall()
    return rows, total_matches


def render_markdown(query: str, rows: list[sqlite3.Row], total_matches: int, book: str | None) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    scope = book or "All books"
    lines = [
        f"# Prose Search — {query}",
        "",
        f"_Generated {generated} · scope: {scope} · showing {len(rows)} of {total_matches} matches_",
        "",
        "---",
        "",
    ]

    if not rows:
        lines.append("No active prose sections matched the query.")
        return "\n".join(lines) + "\n"

    for index, row in enumerate(rows, start=1):
        location = [
            row["book_label"] or "Unassigned book",
            row["section_label"] or row["source_stage"] or "Unassigned section",
        ]
        if row["chapter_no"] is not None:
            location.append(f"Chapter {row['chapter_no']}: {row['chapter_title']}")
        lines.extend(
            [
                f"## {index}. {row['heading']}",
                "",
                f"**Reference:** {' / '.join(location)}",
                f"**Prose section ID:** `{row['id']}` · **status:** `{row['status']}` · **version:** `{row['version']}`",
                f"**Source file:** `{row['source_file'] or 'not recorded'}`",
                "",
                f"> {row['context']}",
                "",
            ]
        )

    return "\n".join(lines)


def default_output_path(query: str, book: str | None) -> Path:
    slug = re.sub(r"[^a-z0-9]+", "-", query.lower()).strip("-") or "query"
    if book:
        book_slug = re.sub(r"[^a-z0-9]+", "-", book.lower()).strip("-")
        slug = f"{slug}-{book_slug}"
    date = datetime.now(timezone.utc).strftime("%Y%m%d")
    return DEFAULT_OUT_DIR / f"prose-search-{slug}-{date}.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Search active prose sections with SQLite FTS5")
    parser.add_argument("query", help="text to search, for example grace or \"inner being\"")
    parser.add_argument("--db", type=Path, default=DB_PATH)
    parser.add_argument("--book", help="limit results to a book_label")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--fts", action="store_true",
                        help="interpret query as a raw SQLite FTS5 MATCH expression")
    parser.add_argument("--out", type=Path,
                        help="Markdown report path; defaults to outputs/markdown/prose-search-*.md")
    args = parser.parse_args()

    if args.limit < 1:
        parser.error("--limit must be at least 1")

    conn = open_db(args.db)
    try:
        rows, total_matches = search_prose(
            conn, args.query, book=args.book, limit=args.limit, raw_fts=args.fts
        )
    finally:
        conn.close()

    report = render_markdown(args.query, rows, total_matches, args.book)
    output_path = args.out or default_output_path(args.query, args.book)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Report: {output_path}")
    print(f"Matches: showing {len(rows)} of {total_matches}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
