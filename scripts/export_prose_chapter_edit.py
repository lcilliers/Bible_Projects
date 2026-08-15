"""Export one current prose chapter or section as a temporary editable Markdown file.

The markers are immutable routing metadata. Edit only the body below each
chapter heading; the importer rejects structural marker changes.
"""
from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("database/bible_research.db")
DEFAULT_OUT_DIR = Path("outputs/markdown")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a prose chapter for editing")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--type-id", type=int, help="single prose_section_type.id")
    group.add_argument("--book", help="book_label, for example Programme")
    parser.add_argument("--chapter", type=int, help="chapter number; required with --book")
    parser.add_argument("--db", type=Path, default=DB_PATH)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.type_id is not None:
        sql = """
        SELECT ps.id, ps.heading, ps.body, ps.version, ps.source_file,
               pst.code, pst.book_order, pst.book_label, pst.section_order,
               pst.section_label, pst.chapter_no, pst.label AS chapter_title,
               pst.description, pst.sort_order
        FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE pst.id = ?
          AND COALESCE(pst.delete_flagged, 0) = 0
          AND COALESCE(ps.delete_flagged, 0) = 0
          AND ps.superseded_by_id IS NULL
        ORDER BY pst.sort_order, ps.id
        """
        query_params = (args.type_id,)
    else:
        if args.chapter is None:
            parser.error("--chapter is required with --book")
        sql = """
        SELECT ps.id, ps.heading, ps.body, ps.version, ps.source_file,
               pst.code, pst.book_order, pst.book_label, pst.section_order,
               pst.section_label, pst.chapter_no, pst.label AS chapter_title,
               pst.description, pst.sort_order
        FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE lower(pst.book_label) = lower(?)
          AND pst.chapter_no = ?
          AND COALESCE(pst.delete_flagged, 0) = 0
          AND COALESCE(ps.delete_flagged, 0) = 0
          AND ps.superseded_by_id IS NULL
        ORDER BY pst.sort_order, ps.id
        """
        query_params = (args.book, args.chapter)
    rows = conn.execute(sql, query_params).fetchall()
    conn.close()

    if not rows:
        parser.error(f"no active prose rows found for {args.book!r}, chapter {args.chapter}")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    book_name = rows[0]["book_label"] or "unassigned-book"
    chapter_no = rows[0]["chapter_no"]
    title = f"{book_name} — Chapter {chapter_no}" if chapter_no is not None else book_name
    output = args.out or DEFAULT_OUT_DIR / (
        f"prose-edit-{book_name.lower().replace(' ', '-')}-"
        f"{('chapter-' + str(chapter_no)) if chapter_no is not None else ('type-' + str(rows[0]['code']))}-"
        f"{stamp}.md"
    )
    lines = [
        f"# Prose Edit — {title}",
        "",
        "<!-- Edit only the prose body below each chapter heading. Do not change markers. -->",
        "<!-- This file is temporary and can be discarded after patch application. -->",
        "",
    ]
    for row in rows:
        markers = [
            f"<!-- PROSE_SECTION_ID: {row['id']} -->",
            f"<!-- PROSE_SECTION_TYPE: {row['code']} -->",
            f"<!-- PROSE_BOOK: {row['book_label']} -->",
            f"<!-- PROSE_SECTION: {row['section_label']} -->",
            f"<!-- PROSE_CHAPTER_NO: {row['chapter_no']} -->",
            f"<!-- PROSE_CHAPTER_TITLE: {row['chapter_title']} -->",
            f"<!-- PROSE_SORT_ORDER: {row['sort_order']} -->",
            f"<!-- PROSE_VERSION: {row['version']} -->",
            f"<!-- PROSE_SOURCE_FILE: {row['source_file'] or ''} -->",
            "",
            f"## {row['heading']}",
            "",
            row["body"].rstrip(),
            "",
            "---",
            "",
        ]
        lines.extend(markers)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Exported {len(rows)} prose section(s): {output}")
    print("Edit prose bodies only; preserve all PROSE_* markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
