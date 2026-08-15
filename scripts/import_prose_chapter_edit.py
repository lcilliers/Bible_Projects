"""Turn an edited prose chapter Markdown file into a PROSE supersede patch.

This script validates routing metadata and generates a patch. It does not
modify the database. Apply the reviewed patch with scripts/apply_session_patch.py.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("database/bible_research.db")
DEFAULT_PATCH_DIR = Path("Sessions/Patches")
MARKER_RE = re.compile(r"<!-- PROSE_([A-Z_]+): ?(.*?) -->")
ID_RE = re.compile(r"<!-- PROSE_SECTION_ID: (\d+) -->")


def parse_blocks(text: str) -> list[dict[str, str]]:
    starts = list(ID_RE.finditer(text))
    if not starts:
        raise ValueError("no PROSE_SECTION_ID markers found")
    blocks = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        chunk = text[match.start():end]
        markers = {key: value.strip() for key, value in MARKER_RE.findall(chunk)}
        heading_match = re.search(r"^##\s+(.+?)\s*$", chunk, re.MULTILINE)
        if not heading_match:
            raise ValueError(f"section {markers.get('SECTION_ID')} has no ## heading")
        body = chunk[heading_match.end():].strip()
        body = re.sub(r"\n---\s*$", "", body).strip()
        markers["BODY"] = body
        blocks.append(markers)
    return blocks


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a prose supersede patch from an edited chapter")
    parser.add_argument("input", type=Path)
    parser.add_argument("--db", type=Path, default=DB_PATH)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--author", default="researcher")
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    operations = []
    try:
        for block in blocks:
            required = [
                "SECTION_ID", "SECTION_TYPE", "BOOK", "SECTION", "CHAPTER_NO",
                "CHAPTER_TITLE", "SORT_ORDER", "VERSION", "SOURCE_FILE", "BODY",
            ]
            missing = [key for key in required if key not in block]
            if missing:
                raise ValueError(f"section {block.get('SECTION_ID')} missing markers: {missing}")
            row = conn.execute(
                """
                SELECT ps.id, ps.version, ps.heading, ps.source_file,
                       pst.code, pst.book_label, pst.section_label,
                       pst.chapter_no, pst.label AS chapter_title, pst.sort_order
                FROM prose_section ps
                JOIN prose_section_type pst ON pst.id = ps.section_type_id
                WHERE ps.id = ? AND COALESCE(ps.delete_flagged, 0) = 0
                  AND ps.superseded_by_id IS NULL
                """,
                (int(block["SECTION_ID"]),),
            ).fetchone()
            if not row:
                raise ValueError(f"section {block['SECTION_ID']} is not an active current prose row")
            checks = {
                "SECTION_TYPE": row["code"],
                "BOOK": row["book_label"],
                "SECTION": row["section_label"],
                "CHAPTER_NO": str(row["chapter_no"]),
                "CHAPTER_TITLE": row["chapter_title"],
                "SORT_ORDER": str(row["sort_order"]),
                "VERSION": str(row["version"]),
                "SOURCE_FILE": row["source_file"] or "",
            }
            for key, expected in checks.items():
                if block[key] != (expected or ""):
                    raise ValueError(
                        f"section {row['id']} marker {key} changed: "
                        f"file={block[key]!r}, database={expected!r}"
                    )
            if not block["BODY"]:
                raise ValueError(f"section {row['id']} has an empty body")
            operations.append({
                "op_id": f"PROSE-{row['id']}-SUPERSEDE",
                "table": "prose_section",
                "operation": "supersede",
                "supersedes_id": row["id"],
                "record": {
                    "body": block["BODY"],
                    "heading": row["heading"],
                    "author": args.author,
                    "status": "draft",
                    "source_file": str(args.input).replace("\\", "/"),
                    "metadata_json": json.dumps({
                        "roundtrip_import": "import_prose_chapter_edit.py",
                        "source_version": row["version"],
                    }),
                },
            })
    finally:
        conn.close()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    patch_id = f"PATCH-{stamp}-PROSE-CHAPTER-SUPERSEDE"
    patch = {
        "_patch_meta": {
            "patch_id": patch_id,
            "patch_type": "PROSE",
            "produced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "session_b_status": None,
            "researcher_approval": "PENDING",
            "description": f"Supersede {len(operations)} prose section(s) from an edited chapter Markdown file.",
        },
        "operations": operations,
        "_patch_summary": {
            "total_operations": len(operations),
            "prose_section_supersedes": len(operations),
            "source_edit_file": str(args.input).replace("\\", "/"),
        },
    }
    output = args.out or DEFAULT_PATCH_DIR / f"wa-prose-chapter-supersede-{stamp}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Patch: {output}")
    print(f"Validated sections: {len(operations)}")
    print("No database changes made; review and apply with scripts/apply_session_patch.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
