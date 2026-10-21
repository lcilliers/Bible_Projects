"""build_patch_types_extract.py — Patch type registry extract (M35 scope).

Source of truth: `wa_patch_type_registry` in the live DB.

Usage:
  python scripts/build_patch_types_extract.py
  python scripts/build_patch_types_extract.py --also-markdown
  python scripts/build_patch_types_extract.py --out=PATH

Default output:
  Workflow/reference/wa-patch-types-extract-{YYYYMMDD}.json
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


def extract_patch_types(conn) -> dict:
    rows = conn.execute(
        """SELECT type_code, description, session_b_status_exempt,
                  governing_instruction, schema_affected, deprecated,
                  deprecation_note, created_at, last_modified
             FROM wa_patch_type_registry
            WHERE deprecated = 0
            ORDER BY type_code"""
    ).fetchall()

    by_code = {r["type_code"]: dict(r) for r in rows}
    exempt = [r["type_code"] for r in rows if r["session_b_status_exempt"]]
    required = [r["type_code"] for r in rows if not r["session_b_status_exempt"]]

    return {
        "by_code": by_code,
        "count": len(rows),
        "session_b_status_exempt": exempt,
        "session_b_status_required": required,
    }


def build_extract(conn) -> dict:
    patch_types = extract_patch_types(conn)
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "source": "wa_patch_type_registry (M35 live, 2026-04-20)",
            "canonical_note": "DB is source of truth post-M35 for patch type catalogue.",
            "description": "Patch type registry — single navigation point for patch types. Applicator uses this to validate _patch_meta.patch_type and decide session_b_status requirements.",
        },
        "patch_types": patch_types,
    }


def render_markdown_view(extract: dict) -> str:
    lines = []
    meta = extract["meta"]
    pt = extract["patch_types"]
    lines.append(f"# WA Patch Type Registry — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema {meta['schema_version']} · source: `wa_patch_type_registry`._\n")
    lines.append("---\n")
    lines.append(f"## Summary\n")
    lines.append(f"**Patch types:** {pt['count']}  ·  "
                 f"**session_b_status required:** {len(pt['session_b_status_required'])}  ·  "
                 f"**exempt:** {len(pt['session_b_status_exempt'])}\n")
    lines.append("## Patch types\n")
    lines.append("| Type | Req sb_status | Governing | Schema affected | Description |")
    lines.append("|---|:---:|---|---|---|")
    for code in sorted(pt["by_code"].keys()):
        r = pt["by_code"][code]
        req = "—" if r["session_b_status_exempt"] else "required"
        desc = (r["description"] or "").replace("|", "\\|").replace("\n", " ")
        if len(desc) > 140:
            desc = desc[:137] + "..."
        gov = (r["governing_instruction"] or "").replace("|", "\\|")
        sch = (r["schema_affected"] or "").replace("|", "\\|")
        if len(sch) > 90:
            sch = sch[:87] + "..."
        lines.append(f"| `{code}` | {req} | {gov} | {sch} | {desc} |")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated {meta['generated_at']}.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build patch-type registry extract from DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--also-markdown", action="store_true")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    out_path = Path(args.out) if args.out else out_dir / f"wa-patch-types-extract-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(extract), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    print(f"Patch types: {extract['patch_types']['count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
