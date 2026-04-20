"""build_label_patterns_extract.py — Label pattern registry extract (M35).

Source of truth: `wa_label_pattern` in the live DB.

Usage:
  python scripts/build_label_patterns_extract.py
  python scripts/build_label_patterns_extract.py --also-markdown
  python scripts/build_label_patterns_extract.py --out=PATH

Default output:
  data/exports/reference/wa-label-patterns-extract-{YYYYMMDD}.json
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

DB_PATH = os.path.join("data", "bible_research.db")
OUT_DIR = os.path.join("data", "exports", "reference")
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


def extract_patterns(conn) -> dict:
    rows = conn.execute(
        """SELECT pattern_code, pattern, entity, description,
                  governing_instruction, deprecated, deprecation_note,
                  created_at, last_modified
             FROM wa_label_pattern
            WHERE deprecated = 0
            ORDER BY pattern_code"""
    ).fetchall()

    by_code = {r["pattern_code"]: dict(r) for r in rows}
    return {
        "by_code": by_code,
        "count": len(rows),
    }


def build_extract(conn) -> dict:
    patterns = extract_patterns(conn)
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "source": "wa_label_pattern (M35 live, 2026-04-20)",
            "canonical_note": "DB is source of truth post-M35 for label patterns (DIM-, PH2-, SD, FLAG, group_code, VCB, Q-COV, directive, patch ID).",
        },
        "label_patterns": patterns,
    }


def render_markdown_view(extract: dict) -> str:
    lines = []
    meta = extract["meta"]
    lp = extract["label_patterns"]
    lines.append(f"# WA Label Pattern Registry — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema {meta['schema_version']} · source: `wa_label_pattern`._\n")
    lines.append("---\n")
    lines.append(f"**Patterns:** {lp['count']}\n")
    lines.append("| Code | Pattern | Entity / Column | Description | Governing |")
    lines.append("|---|---|---|---|---|")
    for code in sorted(lp["by_code"].keys()):
        r = lp["by_code"][code]
        desc = (r["description"] or "").replace("|", "\\|").replace("\n", " ")
        if len(desc) > 90:
            desc = desc[:87] + "..."
        gov = (r["governing_instruction"] or "").replace("|", "\\|")
        ent = (r["entity"] or "").replace("|", "\\|")
        lines.append(f"| `{code}` | `{r['pattern']}` | {ent} | {desc} | {gov} |")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated {meta['generated_at']}.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build label-pattern registry extract from DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--also-markdown", action="store_true")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    out_path = Path(args.out) if args.out else out_dir / f"wa-label-patterns-extract-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(extract), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    print(f"Label patterns: {extract['label_patterns']['count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
