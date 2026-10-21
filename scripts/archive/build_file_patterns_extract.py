"""build_file_patterns_extract.py — File-name pattern registry extract (M35).

Source of truth: `wa_file_name_pattern` in the live DB.

Usage:
  python scripts/build_file_patterns_extract.py
  python scripts/build_file_patterns_extract.py --also-markdown
  python scripts/build_file_patterns_extract.py --scope=per-registry

Default output:
  Workflow/reference/wa-file-patterns-extract-{YYYYMMDD}.json
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import defaultdict
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


def extract_patterns(conn, scope_filter: str | None = None) -> dict:
    sql = """SELECT pattern_code, pattern, scope, description,
                    governing_instruction, deprecated, deprecation_note,
                    created_at, last_modified
               FROM wa_file_name_pattern
              WHERE deprecated = 0"""
    params: list = []
    if scope_filter:
        sql += " AND scope = ?"
        params.append(scope_filter)
    sql += " ORDER BY scope, pattern_code"
    rows = conn.execute(sql, tuple(params)).fetchall()

    by_code = {r["pattern_code"]: dict(r) for r in rows}
    by_scope: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_scope[r["scope"] or "(unscoped)"].append(dict(r))
    return {
        "by_code": by_code,
        "by_scope": dict(by_scope),
        "scope_summary": {s: len(items) for s, items in by_scope.items()},
        "count": len(rows),
    }


def build_extract(conn, scope_filter: str | None = None) -> dict:
    patterns = extract_patterns(conn, scope_filter)
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "source": "wa_file_name_pattern (M35 live, 2026-04-20)",
            "canonical_note": "DB is source of truth post-M35 for file-naming pattern catalogue.",
            "filter": f"scope={scope_filter}" if scope_filter else "all active",
        },
        "file_patterns": patterns,
    }


def render_markdown_view(extract: dict) -> str:
    lines = []
    meta = extract["meta"]
    fp = extract["file_patterns"]
    lines.append(f"# WA File-Name Pattern Registry — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema {meta['schema_version']} · source: `wa_file_name_pattern`._\n")
    lines.append("---\n")
    lines.append(f"## Summary\n")
    lines.append(f"**Patterns:** {fp['count']}\n")
    lines.append("By scope:\n")
    for s in sorted(fp["scope_summary"].keys()):
        lines.append(f"- `{s}`: {fp['scope_summary'][s]}")
    lines.append("")
    for scope in sorted(fp["by_scope"].keys()):
        lines.append(f"## Scope: `{scope}`\n")
        lines.append("| Code | Pattern | Description | Governing |")
        lines.append("|---|---|---|---|")
        for r in fp["by_scope"][scope]:
            desc = (r["description"] or "").replace("|", "\\|").replace("\n", " ")
            if len(desc) > 90:
                desc = desc[:87] + "..."
            gov = (r["governing_instruction"] or "").replace("|", "\\|")
            lines.append(f"| `{r['pattern_code']}` | `{r['pattern']}` | {desc} | {gov} |")
        lines.append("")
    lines.append("---")
    lines.append(f"*Generated {meta['generated_at']}.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build file-pattern registry extract from DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--also-markdown", action="store_true")
    ap.add_argument("--scope", type=str, default=None,
                    help="Restrict to a single scope (per-registry, per-cluster, programme, etc.)")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn, scope_filter=args.scope)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    if args.out:
        out_path = Path(args.out)
    elif args.scope:
        out_path = out_dir / f"wa-file-patterns-{args.scope}-extract-{stamp}.json"
    else:
        out_path = out_dir / f"wa-file-patterns-extract-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(extract), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    print(f"File patterns: {extract['file_patterns']['count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
