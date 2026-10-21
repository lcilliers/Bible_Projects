"""build_reference_snapshot.py — Reference-as-Database snapshot extractor.

Produces a single JSON file (and optional MD view) containing the canonical
reference content sourced from the live DB. Intended for AI session-start
consumption — replaces the document-based `wa-reference` going forward.

Design: research/investigations/reference-as-database-design-20260420.md §10
Framework: research/investigations/reference-as-database-framework-execution-20260420.md

Current coverage (M32 POC):
  - vocabularies (wa_vocab_set + wa_vocab_member)
  - schema index (tables + per-table columns via PRAGMA table_info)

Will grow with each migration:
  - M33 rules                     (wa_rule_registry)
  - M34 programme-prose index     (prose_section_type where source_stage='programme')
  - M35 patch types + file patterns + label patterns

Usage:
  python scripts/build_reference_snapshot.py                  # writes default JSON
  python scripts/build_reference_snapshot.py --also-markdown  # also writes MD view
  python scripts/build_reference_snapshot.py --out=PATH       # custom output path

Author: Claude Code — reference-as-DB M32.
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


def get_schema_version(conn: sqlite3.Connection) -> str:
    row = conn.execute(
        "SELECT version_code FROM schema_version "
        "WHERE id = (SELECT MAX(id) FROM schema_version)"
    ).fetchone()
    return row[0] if row else "unknown"


def extract_vocabularies(conn: sqlite3.Connection) -> dict:
    """Extract all active controlled vocabularies (M32+)."""
    # Check table exists (graceful behaviour on pre-M32 DBs)
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_vocab_set'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available", "_reason": "wa_vocab_set table not in DB — M32 not applied"}

    out = {}
    sets = conn.execute("""
        SELECT id, set_code, name, description, governing_doc, applies_to,
               created_at, last_modified
          FROM wa_vocab_set WHERE deprecated = 0 ORDER BY set_code
    """).fetchall()
    for s in sets:
        members = conn.execute("""
            SELECT value, label, description, sort_order, introduced_at
              FROM wa_vocab_member
             WHERE set_id = ? AND deprecated = 0
             ORDER BY sort_order, value
        """, (s["id"],)).fetchall()
        out[s["set_code"]] = {
            "set_code": s["set_code"],
            "name": s["name"],
            "description": s["description"],
            "governing_doc": s["governing_doc"],
            "applies_to": s["applies_to"],
            "members": [
                {
                    "value": m["value"],
                    "label": m["label"],
                    "description": m["description"],
                    "sort_order": m["sort_order"],
                }
                for m in members
            ],
            "member_count": len(members),
        }
    return out


def extract_schema(conn: sqlite3.Connection) -> dict:
    """Live schema index — tables + per-table columns."""
    tables = [
        r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%' "
            "ORDER BY name"
        )
    ]
    per_table = {}
    for t in tables:
        cols = [r[1] for r in conn.execute(f"PRAGMA table_info({t})")]
        per_table[t] = cols
    return {
        "table_count": len(tables),
        "tables": tables,
        "per_table_columns": per_table,
    }


def extract_rules(conn: sqlite3.Connection) -> dict:
    """Extract global rules + addenda (M33+). Not-available until M33 applied."""
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_rule_registry'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available", "_reason": "wa_rule_registry table not in DB — M33 not applied"}

    # Active rules
    rows = conn.execute("""
        SELECT rule_id, category, subject, rule_text, example, applies_to,
               version, added_date, last_modified, superseded_by, addendum_ref,
               source_document
          FROM wa_rule_registry
         WHERE obsolete = 0
         ORDER BY category, rule_id
    """).fetchall()
    rules = {r["rule_id"]: dict(r) for r in rows}

    # Addenda — schema v3.14.0+ has obsolete column (M36); default excludes obsolete
    addenda = {}
    a_exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_addendum_registry'"
    ).fetchone()
    if a_exists:
        cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_addendum_registry)")}
        has_obs = "obsolete" in cols
        where = " WHERE obsolete = 0" if has_obs else ""
        a_rows = conn.execute(f"""
            SELECT item_id, addendum_group, rule_id, audit_source, subject,
                   observation, migration_target, migration_status,
                   researcher_comment, source_document
              FROM wa_addendum_registry{where}
             ORDER BY addendum_group, item_id
        """).fetchall()
        for a in a_rows:
            addenda.setdefault(a["addendum_group"], []).append(dict(a))

    return {
        "rules": rules,
        "rule_count": len(rules),
        "addenda": addenda,
    }


def extract_programme_prose_index(conn: sqlite3.Connection) -> dict:
    """Extract programme-stage prose section index (M34+)."""
    rows = conn.execute("""
        SELECT st.code, st.label, st.description, st.sort_order,
               COUNT(s.id) AS section_count
          FROM prose_section_type st
          LEFT JOIN prose_section s ON s.section_type_id = st.id AND s.delete_flagged = 0
         WHERE st.source_stage = 'programme' AND st.delete_flagged = 0
         GROUP BY st.id
         ORDER BY st.sort_order, st.code
    """).fetchall()
    if not rows:
        return {"_status": "not-available", "_reason": "no programme-stage prose section types seeded — M34 not applied"}
    return {
        "types": [dict(r) for r in rows],
        "type_count": len(rows),
    }


def extract_patch_types(conn: sqlite3.Connection) -> dict:
    """Extract patch type registry (M35+)."""
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_patch_type_registry'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available", "_reason": "wa_patch_type_registry not in DB — M35 not applied"}
    rows = conn.execute("""
        SELECT type_code, description, session_b_status_exempt,
               governing_instruction, schema_affected
          FROM wa_patch_type_registry WHERE deprecated = 0 ORDER BY type_code
    """).fetchall()
    return {r["type_code"]: dict(r) for r in rows}


def extract_file_name_patterns(conn: sqlite3.Connection) -> dict:
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_file_name_pattern'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available", "_reason": "wa_file_name_pattern not in DB — M35 not applied"}
    rows = conn.execute("""
        SELECT pattern_code, pattern, scope, description, governing_instruction
          FROM wa_file_name_pattern WHERE deprecated = 0 ORDER BY pattern_code
    """).fetchall()
    return {r["pattern_code"]: dict(r) for r in rows}


def extract_label_patterns(conn: sqlite3.Connection) -> dict:
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_label_pattern'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available", "_reason": "wa_label_pattern not in DB — M35 not applied"}
    rows = conn.execute("""
        SELECT pattern_code, pattern, entity, description, governing_instruction
          FROM wa_label_pattern WHERE deprecated = 0 ORDER BY pattern_code
    """).fetchall()
    return {r["pattern_code"]: dict(r) for r in rows}


def build_snapshot(conn: sqlite3.Connection) -> dict:
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "description": "Reference-as-Database snapshot. Source of truth for controlled vocabularies, schema, global rules, patch types, file/label patterns. Generated at session start for AI consumption.",
            "design_doc": "research/investigations/reference-as-database-design-20260420.md",
        },
        "vocabularies": extract_vocabularies(conn),
        "schema": extract_schema(conn),
        "rules": extract_rules(conn),
        "patch_types": extract_patch_types(conn),
        "file_name_patterns": extract_file_name_patterns(conn),
        "label_patterns": extract_label_patterns(conn),
        "programme_prose_index": extract_programme_prose_index(conn),
    }


def render_markdown_view(snapshot: dict) -> str:
    """Human-readable markdown rendering of the snapshot."""
    lines = []
    meta = snapshot["meta"]
    lines.append(f"# WA Reference Snapshot — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema version: **{meta['schema_version']}** · "
                 f"extractor: v{meta['extractor_version']}_\n")
    lines.append(f"_Source: live DB (single source of truth). Regenerate at session start._\n")
    lines.append("---\n")

    # Vocabularies
    lines.append("## Controlled Vocabularies\n")
    vocab = snapshot["vocabularies"]
    if isinstance(vocab, dict) and "_status" in vocab:
        lines.append(f"_{vocab.get('_reason', 'not available')}_\n")
    else:
        for set_code in sorted(vocab.keys()):
            v = vocab[set_code]
            lines.append(f"### {v['set_code']} — {v['name']}\n")
            lines.append(f"**Governing:** {v['governing_doc']}  ")
            lines.append(f"**Applies to:** `{v['applies_to']}`  ")
            lines.append(f"**Members:** {v['member_count']}\n")
            if v['description']:
                lines.append(f"_{v['description']}_\n")
            lines.append("| Value | Description |")
            lines.append("|---|---|")
            for m in v['members']:
                desc = (m['description'] or '').replace('|', '\\|').replace('\n', ' ')
                if len(desc) > 120:
                    desc = desc[:117] + '...'
                lines.append(f"| `{m['value']}` | {desc or '—'} |")
            lines.append("")

    # Schema
    lines.append("## Schema — live DB\n")
    sch = snapshot["schema"]
    lines.append(f"**Tables:** {sch['table_count']}\n")
    lines.append("Full per-table column listing in JSON snapshot.\n")

    # Rules / patch types / patterns / programme prose — placeholders until M33-M35
    for k, title in [
        ("rules", "Global Rules"),
        ("patch_types", "Patch Type Registry"),
        ("file_name_patterns", "File-Naming Patterns"),
        ("label_patterns", "Label Patterns"),
        ("programme_prose_index", "Programme-Wide Prose (L2)"),
    ]:
        lines.append(f"## {title}\n")
        blob = snapshot.get(k)
        if isinstance(blob, dict) and "_status" in blob:
            lines.append(f"_{blob.get('_reason', 'not available')}_\n")
        else:
            lines.append(f"_(populated — see JSON snapshot for detail)_\n")
            if isinstance(blob, dict):
                lines.append(f"**Entries:** {len(blob)}\n")

    lines.append("---\n")
    lines.append(f"*Snapshot generated {meta['generated_at']} — regenerate at next session start.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build reference snapshot from live DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None,
                    help="JSON output path (default: Workflow/reference/wa-reference-snapshot-{YYYYMMDD}.json)")
    ap.add_argument("--also-markdown", action="store_true",
                    help="also emit a human-readable .md view alongside the JSON")
    args = ap.parse_args()

    conn = open_db(args.db)
    snapshot = build_snapshot(conn)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    out_path = Path(args.out) if args.out else out_dir / f"wa-reference-snapshot-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(snapshot), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    vocab = snapshot.get("vocabularies", {})
    if isinstance(vocab, dict) and "_status" not in vocab:
        vocab_count = len(vocab)
        member_total = sum(v.get("member_count", 0) for v in vocab.values())
        print(f"Vocabularies: {vocab_count} sets, {member_total} members")
    sch = snapshot.get("schema", {})
    print(f"Schema: {sch.get('table_count', '?')} tables")
    return 0


if __name__ == "__main__":
    sys.exit(main())
