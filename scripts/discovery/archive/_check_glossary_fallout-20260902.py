#!/usr/bin/env python
"""Read-only discovery script (design-support for escalation #1377): for each candidate glossary
term/sense, find every live config citation across both databases -- cfg_column.name (column-
identity matches), cfg_column.use / cfg_setting.value+use / cfg_prose.value+use (textual
mentions). Not a registered utility yet -- ad hoc analysis feeding the glossary design's fallout
list and informing the wording of the draft glossary entries, per researcher instruction
2026-09-02 (7.4 must be developed before 7.3's wording is finalised).

Usage: python glossary_fallout_scan.py
Reads both DBs read-only. Writes nothing.
"""
import json
import re
import sqlite3

IBA_DB = "iba/app/db/iba.db"  # relative to project root; run from c:/Bible_study_projects

# Candidate terms drawn from 1377-vocabulary-glossary-seed-v2-20260901.md Parts 1-4.
# Each entry: (query_term, search_variants) -- variants used for the textual/word-boundary scan;
# query_term alone is used for the column-name exact/substring scan.
TERMS = [
    "inner-being characteristic", "HIB", "phenomenon", "operation", "cluster", "cluster_code",
    "characteristic", "family", "cluster_subgroup", "characteristic_subgroup", "T2", "T3", "FLAG",
    "descriptor", "scope", "source", "tier", "span", "surface", "term", "word", "content",
    "function", "resolved", "unregistered", "content_resolved", "inner-being-related",
    "Layer A", "Layer B", "Phase 1", "Phase 2", "verse-context", "model", "dimension",
    "inner being", "anchor", "registry", "passage", "flag", "status", "resolution",
    "delete_flagged", "deleted", "delete_flag", "deprecated",
]


def word_pattern(term: str) -> re.Pattern:
    # Word-boundary-ish match; terms with spaces/underscores treated literally.
    escaped = re.escape(term)
    return re.compile(rf"(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])", re.IGNORECASE)


def main() -> None:
    conn = sqlite3.connect(IBA_DB)
    conn.row_factory = sqlite3.Row

    cfg_columns = conn.execute(
        "SELECT database, table_name, name, use FROM cfg_column WHERE inactive=0"
    ).fetchall()
    cfg_settings = conn.execute(
        "SELECT key, value, use FROM cfg_setting"
    ).fetchall()
    cfg_prose = conn.execute(
        "SELECT key, value, use FROM cfg_prose"
    ).fetchall()

    results = {}
    for term in TERMS:
        pat = word_pattern(term)
        entry = {"column_name_matches": [], "cfg_column_use_matches": [],
                 "cfg_setting_matches": [], "cfg_prose_matches": []}

        for row in cfg_columns:
            if row["name"] and pat.search(row["name"]):
                entry["column_name_matches"].append(
                    f"{row['database']}.{row['table_name']}.{row['name']}"
                )
            use = row["use"] or ""
            if pat.search(use):
                entry["cfg_column_use_matches"].append(
                    f"{row['database']}.{row['table_name']}.{row['name']}: "
                    f"{use[:160]}{'...' if len(use) > 160 else ''}"
                )

        for row in cfg_settings:
            haystack = f"{row['value'] or ''} {row['use'] or ''}"
            if pat.search(haystack) or pat.search(row["key"] or ""):
                entry["cfg_setting_matches"].append(
                    f"{row['key']}: {haystack[:160]}{'...' if len(haystack) > 160 else ''}"
                )

        for row in cfg_prose:
            haystack = f"{row['value'] or ''} {row['use'] or ''}"
            if pat.search(haystack) or pat.search(row["key"] or ""):
                entry["cfg_prose_matches"].append(
                    f"{row['key']}: {haystack[:160]}{'...' if len(haystack) > 160 else ''}"
                )

        total = sum(len(v) for v in entry.values())
        if total:
            results[term] = entry

    out_path = "Workflow/Catalogue/glossary-fallout-raw-20260902.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)
    print(f"wrote {out_path}")
    conn.close()


if __name__ == "__main__":
    main()
