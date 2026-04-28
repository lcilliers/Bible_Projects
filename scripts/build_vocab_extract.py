"""build_vocab_extract.py — Controlled vocabulary extract (M32 scope).

Dedicated vocabularies-only snapshot from the DB (post-M32). Separate from the
full reference snapshot when only vocabularies are needed.

Source of truth: `wa_vocab_set` + `wa_vocab_member` in the live DB.

Usage:
  python scripts/build_vocab_extract.py
  python scripts/build_vocab_extract.py --also-markdown
  python scripts/build_vocab_extract.py --set=DIMENSION_LABEL   # single set
  python scripts/build_vocab_extract.py --out=PATH

Default output:
  Workflow/reference/wa-vocab-extract-{YYYYMMDD}.json
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "reference")
EXTRACTOR_VERSION = "1.0"


def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def get_schema_version(conn) -> str:
    row = conn.execute(
        "SELECT version_code FROM schema_version WHERE id = (SELECT MAX(id) FROM schema_version)"
    ).fetchone()
    return row[0] if row else "unknown"


def extract_vocabularies(conn, set_code_filter: str | None = None) -> dict:
    sets_sql = """
        SELECT id, set_code, name, description, governing_doc, applies_to,
               deprecated, deprecation_note, created_at, last_modified
          FROM wa_vocab_set
         WHERE deprecated = 0
    """
    params: list = []
    if set_code_filter:
        sets_sql += " AND set_code = ?"
        params.append(set_code_filter)
    sets_sql += " ORDER BY set_code"
    sets = conn.execute(sets_sql, tuple(params)).fetchall()

    out = {}
    total_members = 0
    for s in sets:
        members = conn.execute(
            """SELECT value, label, description, sort_order, deprecated,
                      deprecation_note, superseded_by_member_id, introduced_at,
                      created_at, last_modified
                 FROM wa_vocab_member
                WHERE set_id = ? AND deprecated = 0
                ORDER BY sort_order, value""",
            (s["id"],),
        ).fetchall()
        out[s["set_code"]] = {
            "set_code": s["set_code"],
            "name": s["name"],
            "description": s["description"],
            "governing_doc": s["governing_doc"],
            "applies_to": s["applies_to"],
            "members": [dict(m) for m in members],
            "member_count": len(members),
        }
        total_members += len(members)
    return {"sets": out, "set_count": len(sets), "total_members": total_members}


def build_extract(conn, set_code_filter: str | None = None) -> dict:
    vocab = extract_vocabularies(conn, set_code_filter)
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "source": "wa_vocab_set + wa_vocab_member (M32 live, 2026-04-20)",
            "canonical_note": "DB is source of truth post-M32 for all listed vocabularies.",
            "filter": f"set_code={set_code_filter}" if set_code_filter else "all active sets",
            "description": "Controlled-vocabulary extract for session-start consumption. Validators query wa_vocab_set/member directly; this snapshot enables AI or researcher to load the same reference.",
        },
        **vocab,
    }


def render_markdown_view(extract: dict) -> str:
    lines = []
    meta = extract["meta"]
    lines.append(f"# WA Controlled Vocabularies — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema {meta['schema_version']} · extractor v{meta['extractor_version']}_\n")
    lines.append(f"_Source: DB `wa_vocab_set` + `wa_vocab_member`._\n")
    lines.append("---\n")
    lines.append(f"## Summary\n")
    lines.append(f"**Sets:** {extract['set_count']}  ·  **Total members:** {extract['total_members']}\n")
    for code in sorted(extract["sets"].keys()):
        v = extract["sets"][code]
        lines.append(f"### {code} — {v['name']}\n")
        lines.append(f"**Governing:** {v['governing_doc']}  ")
        lines.append(f"**Applies to:** `{v['applies_to']}`  ")
        lines.append(f"**Members:** {v['member_count']}\n")
        if v["description"]:
            lines.append(f"_{v['description']}_\n")
        lines.append("| Value | Description |")
        lines.append("|---|---|")
        for m in v["members"]:
            desc = (m["description"] or "").replace("|", "\\|").replace("\n", " ")
            if len(desc) > 130:
                desc = desc[:127] + "..."
            lines.append(f"| `{m['value']}` | {desc or '—'} |")
        lines.append("")
    lines.append("---")
    lines.append(f"*Generated {meta['generated_at']}.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build controlled-vocabulary extract from DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None,
                    help="JSON output path (default: Workflow/reference/wa-vocab-extract-{YYYYMMDD}.json)")
    ap.add_argument("--also-markdown", action="store_true")
    ap.add_argument("--set", type=str, default=None, dest="set_code",
                    help="Restrict to a single set_code (e.g. DIMENSION_LABEL)")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn, set_code_filter=args.set_code)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    if args.out:
        out_path = Path(args.out)
    elif args.set_code:
        out_path = out_dir / f"wa-vocab-{args.set_code.lower()}-extract-{stamp}.json"
    else:
        out_path = out_dir / f"wa-vocab-extract-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(extract), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    print(f"Sets: {extract['set_count']}  Members: {extract['total_members']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
