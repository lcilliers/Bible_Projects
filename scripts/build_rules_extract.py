"""build_rules_extract.py — Global rules + addenda JSON extract.

Dedicated rules-only snapshot from the DB (post-M33). Separate from the full
reference snapshot when only rules are needed at session start.

Source of truth: `wa_rule_registry` + `wa_addendum_registry` in the live DB.
The JSON seed file `wa-global-general-rules-v2_11-20260418.json` remains as
audit-trail but is no longer authoritative (DB is).

Usage:
  python scripts/build_rules_extract.py                  # writes default JSON
  python scripts/build_rules_extract.py --also-markdown  # also writes MD view
  python scripts/build_rules_extract.py --out=PATH       # custom output path
  python scripts/build_rules_extract.py --include-obsolete   # include retired rules in output

Default output:
  data/exports/reference/wa-global-rules-extract-{YYYYMMDD}.json
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


def get_schema_version(conn: sqlite3.Connection) -> str:
    row = conn.execute(
        "SELECT version_code FROM schema_version "
        "WHERE id = (SELECT MAX(id) FROM schema_version)"
    ).fetchone()
    return row[0] if row else "unknown"


def extract_rules(conn: sqlite3.Connection, include_obsolete: bool = False) -> dict:
    where = "" if include_obsolete else " WHERE obsolete = 0"
    rows = conn.execute(
        f"""SELECT rule_id, category, subject, rule_text, example, applies_to,
                   version, added_date, last_modified, obsolete, obsolete_reason,
                   superseded_by, addendum_ref, source_document
              FROM wa_rule_registry{where}
             ORDER BY category, rule_id"""
    ).fetchall()

    all_rules = [dict(r) for r in rows]
    by_category: dict[str, list[dict]] = defaultdict(list)
    for r in all_rules:
        by_category[r["category"]].append(r)

    # Active / obsolete breakdown
    active = [r for r in all_rules if not r["obsolete"]]
    obsolete = [r for r in all_rules if r["obsolete"]]

    # Category summary
    category_summary = {
        cat: {
            "total": len(rules),
            "active": len([r for r in rules if not r["obsolete"]]),
            "obsolete": len([r for r in rules if r["obsolete"]]),
        }
        for cat, rules in by_category.items()
    }

    return {
        "total": len(all_rules),
        "active_count": len(active),
        "obsolete_count": len(obsolete),
        "category_summary": category_summary,
        "by_category": dict(by_category),
        "all_rules": all_rules,
    }


def extract_addenda(conn: sqlite3.Connection, include_obsolete: bool = False) -> dict:
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_addendum_registry'"
    ).fetchone()
    if not exists:
        return {"_status": "not-available"}

    # Schema v3.14.0+: wa_addendum_registry has obsolete column (M36).
    # Default: exclude obsolete (researcher direction 2026-04-20).
    cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_addendum_registry)")}
    has_obsolete = "obsolete" in cols
    select_extra = ", obsolete, obsolete_reason" if has_obsolete else ", 0 AS obsolete, NULL AS obsolete_reason"
    where = ""
    if has_obsolete and not include_obsolete:
        where = " WHERE obsolete = 0"
    rows = conn.execute(
        f"""SELECT item_id, addendum_group, rule_id, audit_source, subject,
                   observation, migration_target, migration_status,
                   researcher_comment, source_document{select_extra}
              FROM wa_addendum_registry{where}
             ORDER BY addendum_group, item_id"""
    ).fetchall()

    by_group: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_group[r["addendum_group"]].append(dict(r))

    return {
        "total": len(rows),
        "by_group": dict(by_group),
        "group_summary": {g: len(items) for g, items in by_group.items()},
    }


def build_extract(conn: sqlite3.Connection, include_obsolete: bool = False) -> dict:
    rules = extract_rules(conn, include_obsolete=include_obsolete)
    addenda = extract_addenda(conn, include_obsolete=include_obsolete)
    return {
        "meta": {
            "generated_at": now_iso(),
            "schema_version": get_schema_version(conn),
            "extractor_version": EXTRACTOR_VERSION,
            "source": "wa_rule_registry + wa_addendum_registry (M33 live, 2026-04-20)",
            "canonical_note": "DB is source of truth post-M33. The seed JSON "
                              "wa-global-general-rules-v2_11-20260418.json is "
                              "retained for audit; divergence resolves to DB.",
            "include_obsolete": include_obsolete,
            "description": "Global rules + addenda extract for AI session-start "
                           "loading. Per GR-LOAD-001, Claude AI must read this "
                           "at session start.",
        },
        "rules": rules,
        "addenda": addenda,
    }


def render_markdown_view(extract: dict) -> str:
    lines = []
    meta = extract["meta"]
    rules = extract["rules"]
    addenda = extract["addenda"]

    lines.append(f"# WA Global Rules Extract — {meta['generated_at'][:10]}\n")
    lines.append(f"_Schema {meta['schema_version']} · extractor v{meta['extractor_version']}_\n")
    lines.append(f"_Source: DB `wa_rule_registry` + `wa_addendum_registry`. Regenerate at session start._\n")
    lines.append("---\n")

    # Summary
    lines.append("## Summary\n")
    lines.append(f"| Aspect | Count |")
    lines.append(f"|---|---:|")
    lines.append(f"| Active rules | {rules['active_count']} |")
    lines.append(f"| Obsolete / superseded | {rules['obsolete_count']} |")
    lines.append(f"| Total rules | {rules['total']} |")
    if isinstance(addenda, dict) and "total" in addenda:
        lines.append(f"| Addenda | {addenda['total']} |")
    lines.append("")

    # Category breakdown
    lines.append("## Rules by category\n")
    lines.append("| Category | Active | Obsolete | Total |")
    lines.append("|---|---:|---:|---:|")
    for cat in sorted(rules["category_summary"].keys()):
        s = rules["category_summary"][cat]
        lines.append(f"| `{cat}` | {s['active']} | {s['obsolete']} | {s['total']} |")
    lines.append("")

    # Active rules per category
    lines.append("---\n")
    lines.append("## Active rules (full text)\n")
    for cat in sorted(rules["by_category"].keys()):
        cat_rules = [r for r in rules["by_category"][cat] if not r["obsolete"]]
        if not cat_rules:
            continue
        lines.append(f"### Category: `{cat}` ({len(cat_rules)} active)\n")
        for r in cat_rules:
            lines.append(f"#### {r['rule_id']} — {r['subject'] or ''}\n")
            if r.get("applies_to"):
                lines.append(f"_Applies to: {r['applies_to']}_\n")
            if r.get("version"):
                lines.append(f"_Version: {r['version']}_\n")
            lines.append(r["rule_text"])
            if r.get("example"):
                lines.append(f"\n**Example:** `{r['example']}`")
            lines.append("")

    # Obsolete (condensed)
    if rules["obsolete_count"] > 0 and meta.get("include_obsolete"):
        lines.append("---\n")
        lines.append("## Obsolete / superseded rules\n")
        for r in [r for r in rules["all_rules"] if r["obsolete"]]:
            lines.append(f"- **{r['rule_id']}** — {r.get('subject', '')}")
            if r.get("obsolete_reason"):
                lines.append(f"  _{r['obsolete_reason']}_")
            if r.get("superseded_by"):
                lines.append(f"  _Superseded by: {r['superseded_by']}_")
            lines.append("")

    # Addenda
    if isinstance(addenda, dict) and "by_group" in addenda:
        lines.append("---\n")
        lines.append("## Addenda (rules migration / absorption record)\n")
        for group_name in sorted(addenda["by_group"].keys()):
            items = addenda["by_group"][group_name]
            lines.append(f"### {group_name} ({len(items)} items)\n")
            for a in items:
                lines.append(f"**{a['item_id']}** — {a.get('subject', '')}")
                if a.get("rule_id"):
                    lines.append(f"  Rule: `{a['rule_id']}`")
                if a.get("observation"):
                    lines.append(f"  Observation: {a['observation']}")
                if a.get("migration_target"):
                    lines.append(f"  Migration target: {a['migration_target']}")
                if a.get("migration_status"):
                    lines.append(f"  Status: `{a['migration_status']}`")
                lines.append("")

    lines.append("---")
    lines.append(f"*Generated {meta['generated_at']}.*")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build global rules + addenda extract from DB")
    ap.add_argument("--db", type=str, default=DB_PATH)
    ap.add_argument("--out", type=str, default=None,
                    help="JSON output path (default: data/exports/reference/wa-global-rules-extract-{YYYYMMDD}.json)")
    ap.add_argument("--also-markdown", action="store_true",
                    help="also emit human-readable .md view alongside JSON")
    ap.add_argument("--include-obsolete", action="store_true",
                    help="include retired/superseded rules in output (default: active only)")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn, include_obsolete=args.include_obsolete)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = today_compact()
    out_path = Path(args.out) if args.out else out_dir / f"wa-global-rules-extract-{stamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(extract, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote JSON: {out_path}")

    if args.also_markdown:
        md_path = out_path.with_suffix(".md")
        md_path.write_text(render_markdown_view(extract), encoding="utf-8")
        print(f"Wrote MD:   {md_path}")

    rules = extract["rules"]
    print(f"Rules: {rules['active_count']} active / {rules['obsolete_count']} obsolete / {rules['total']} total")
    print(f"Categories: {len(rules['category_summary'])}")
    if isinstance(extract["addenda"], dict) and "total" in extract["addenda"]:
        print(f"Addenda: {extract['addenda']['total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
