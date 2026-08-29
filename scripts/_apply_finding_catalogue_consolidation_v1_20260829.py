"""_apply_finding_catalogue_consolidation_v1_20260829.py

One-time consolidation migration, researcher-directed 2026-08-29 (following the finding-tables
landscape review, outputs/finding-tables-landscape-review-20260829.md, and its migration plan
outputs/cluster-finding-to-finding-migration-plan-20260829.md):

1. Folds `cluster_finding` (19,997 rows, real content, frozen since 2026-06-19, never previously
   migrated) into the live `finding` table. Structural links (characteristic_id, cluster_subgroup_id,
   vcg_scope) are RETAINED as new columns on `finding`, not dropped. Each migrated row also gets a
   finding_question_link row for its catalogue link (obs_id).
2. Folds `wa_finding_catalogue_links` (6,199 rows) into the live `finding_question_link` table.
   finding_id is remapped from wa_session_b_findings.id to the live finding.id via the SB: tag
   already written into finding.source_legacy_ref by the prior session_b migration. A row whose
   source finding_id is NULL (743 of 6,199, confirmed live -- not a matching failure, the source
   value itself is absent) cannot be inserted into finding_question_link at all (finding_id is
   NOT NULL there, by design, for every other consumer of the table) -- it is left exactly where
   it already lives, in the retained (inactive-flagged, not dropped) wa_finding_catalogue_links
   table, rather than migrated with a fabricated or misleading finding_id. Per instruction: "do not
   try to reconcile the contents of the questions at this stage" -- rows that DO migrate move
   verbatim; this script does not judge or clean up which finding/question pairings are meaningful.

Neither source table is dropped -- both are left in place on disk; cfg_table.inactive=1 is applied
separately (config change, via Config-Maintenance.ps1 Propose, not by this script).

Usage:
    python scripts/_apply_finding_catalogue_consolidation_v1_20260829.py --dry-run
    python scripts/_apply_finding_catalogue_consolidation_v1_20260829.py --live
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = "database/bible_research.db"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ensure_columns(conn: sqlite3.Connection, table: str, columns: list[tuple[str, str]]) -> list[str]:
    """Adds any column in `columns` ([(name, sql_type), ...]) not already present. Returns the
    list actually added (idempotent -- safe to re-run)."""
    existing = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
    added = []
    for name, sql_type in columns:
        if name in existing:
            continue
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {sql_type}")
        added.append(name)
    return added


def migrate(conn: sqlite3.Connection, live: bool) -> dict:
    report: dict = {}

    # ── 1. schema additions ──────────────────────────────────────────────────
    finding_cols_added = _ensure_columns(conn, "finding", [
        ("characteristic_id", "INTEGER"),
        ("cluster_subgroup_id", "INTEGER"),
        ("vcg_scope", "TEXT"),
        ("notes", "TEXT"),
    ])
    fql_cols_added = _ensure_columns(conn, "finding_question_link", [
        ("status", "TEXT"),
        ("pattern_type", "TEXT"),
        ("mapped_date", "TEXT"),
        ("validated_date", "TEXT"),
        ("validated_by", "TEXT"),
        ("session_b_note", "TEXT"),
        ("source_legacy_ref", "TEXT"),
    ])
    report["finding_columns_added"] = finding_cols_added
    report["finding_question_link_columns_added"] = fql_cols_added

    # ── 2. cluster_finding -> finding ────────────────────────────────────────
    cf_rows = conn.execute("SELECT * FROM cluster_finding").fetchall()
    cf_cols = [d[0] for d in conn.execute("SELECT * FROM cluster_finding LIMIT 0").description]

    new_finding_ids: dict[int, int] = {}   # cluster_finding.id -> new finding.id
    now = _now()
    for row in cf_rows:
        r = dict(zip(cf_cols, row))
        source_legacy_ref = f"CF:{r['id']}|source_file:{r['source_file']}|version:{r['version']}"
        if live:
            cur = conn.execute(
                "INSERT INTO finding (level, cluster_code, finding_value, finding_status, "
                "provenance, source_legacy_ref, characteristic_id, cluster_subgroup_id, "
                "vcg_scope, notes, created_at, last_updated_date, delete_flagged) "
                "VALUES ('CLUSTER', ?, ?, ?, 'cluster_finding_migration', ?, ?, ?, ?, ?, ?, ?, ?)",
                (r["cluster_code"], r["finding_text"], r["finding_status"], source_legacy_ref,
                 r["characteristic_id"], r["cluster_subgroup_id"], r["vcg_scope"], r["notes"],
                 r["created_at"] or now, r["last_updated_date"] or now, r["delete_flagged"] or 0))
            new_finding_ids[r["id"]] = cur.lastrowid
    report["cluster_finding_rows_migrated"] = len(cf_rows)

    # ── 3. cluster_finding.obs_id -> new finding_question_link rows ─────────
    fql_from_cf = 0
    for row in cf_rows:
        r = dict(zip(cf_cols, row))
        if r["obs_id"] is None:
            continue
        fql_from_cf += 1
        if live:
            new_fid = new_finding_ids[r["id"]]
            conn.execute(
                "INSERT INTO finding_question_link (finding_id, question_id, created_at, "
                "source_legacy_ref) VALUES (?, ?, ?, ?)",
                (new_fid, r["obs_id"], now, f"CF:{r['id']}"))
    report["finding_question_link_rows_from_cluster_finding"] = fql_from_cf

    # ── 4. wa_finding_catalogue_links -> finding_question_link (finding_id remapped) ─
    wfcl_rows = conn.execute("SELECT * FROM wa_finding_catalogue_links").fetchall()
    wfcl_cols = [d[0] for d in conn.execute(
        "SELECT * FROM wa_finding_catalogue_links LIMIT 0").description]

    # Build the SB-tag lookup: wa_session_b_findings.id -> finding.id, via the tag the earlier
    # session_b migration already wrote into finding.source_legacy_ref ("SB:{registry}-{finding_id}|...").
    # ONE pass over the ~2,883 session_b_migration rows (indexed by their own tag prefix), not a
    # per-row LIKE scan against all ~1M finding rows -- the original per-row-query version timed
    # out (2,883 x full-table LIKE scans, no index on source_legacy_ref).
    tag_to_finding_id: dict[str, int] = {}
    for fid, ref in conn.execute(
            "SELECT id, source_legacy_ref FROM finding WHERE provenance='session_b_migration'"):
        # ref format: "SB:{registry}-{finding_id}|type:...|..." -- key on the part before the
        # first '|', verbatim, so it matches the tag_prefix built below exactly.
        tag_to_finding_id[ref.split("|", 1)[0]] = fid

    # wa_session_b_findings.finding_id is ALREADY the registry-prefixed form (e.g. "112-F001") --
    # confirmed live; the tag is "SB:" + that value verbatim, not "SB:{registry}-{finding_id}"
    # (that would double the registry prefix, the bug this comment replaces).
    sb_lookup: dict[int, int] = {}
    for sb_id, sb_finding_id in conn.execute("SELECT id, finding_id FROM wa_session_b_findings"):
        tag = f"SB:{sb_finding_id}"
        if tag in tag_to_finding_id:
            sb_lookup[sb_id] = tag_to_finding_id[tag]

    # finding_question_link.finding_id is NOT NULL by schema (every row must reference a real
    # finding) -- a row whose finding_id doesn't remap cleanly CANNOT be faithfully inserted there
    # without either relaxing that constraint (wrong -- it protects every other consumer of this
    # table) or writing a fabricated/misleading finding_id (worse -- silent corruption). Per
    # instruction ("the tables migrated is not dropped, just marked inactive"), the source row
    # isn't lost either way -- wa_finding_catalogue_links stays on disk, inactive-flagged, not
    # deleted. So: skip the insert for an unresolved row, count it, and leave it exactly where it
    # already lives.
    resolved, unresolved = 0, 0
    for row in wfcl_rows:
        r = dict(zip(wfcl_cols, row))
        remapped_finding_id = sb_lookup.get(r["finding_id"]) if r["finding_id"] is not None else None
        if remapped_finding_id is None:
            unresolved += 1
            continue
        resolved += 1
        if live:
            conn.execute(
                "INSERT INTO finding_question_link (finding_id, question_id, coverage, status, "
                "pattern_type, mapped_date, validated_date, validated_by, session_b_note, "
                "created_at, delete_flagged, source_legacy_ref) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (remapped_finding_id, r["question_id"], r["coverage"], r["status"],
                 r["pattern_type"], r["mapped_date"], r["validated_date"], r["validated_by"],
                 r["session_b_note"], now, r["delete_flagged"] or 0, f"WFCL:{r['id']}"))
    report["wa_finding_catalogue_links_rows_migrated"] = resolved
    report["wa_finding_catalogue_links_finding_id_resolved"] = resolved
    report["wa_finding_catalogue_links_rows_left_unmigrated_in_source"] = unresolved

    return report


def verify(conn: sqlite3.Connection) -> dict:
    v = {}
    v["cluster_finding_migrated_count"] = conn.execute(
        "SELECT COUNT(*) FROM finding WHERE provenance='cluster_finding_migration'").fetchone()[0]
    v["cluster_finding_source_count"] = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding").fetchone()[0]
    v["fql_from_cf_count"] = conn.execute(
        "SELECT COUNT(*) FROM finding_question_link WHERE source_legacy_ref LIKE 'CF:%'").fetchone()[0]
    v["wfcl_migrated_count"] = conn.execute(
        "SELECT COUNT(*) FROM finding_question_link WHERE source_legacy_ref LIKE 'WFCL:%'").fetchone()[0]
    v["wfcl_source_count"] = conn.execute(
        "SELECT COUNT(*) FROM wa_finding_catalogue_links").fetchone()[0]
    # spot-check: a migrated finding_value matches its cluster_finding source verbatim
    row = conn.execute(
        "SELECT f.finding_value, c.finding_text FROM finding f "
        "JOIN cluster_finding c ON f.source_legacy_ref LIKE 'CF:' || c.id || '|%' "
        "LIMIT 1").fetchone()
    v["spot_check_value_matches"] = (row is not None and row[0] == row[1])
    return v


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    a = ap.parse_args()
    if a.dry_run == a.live:
        print("pass exactly one of --dry-run or --live")
        return 1

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = None
    try:
        report = migrate(conn, live=a.live)
        for k, v in report.items():
            print(f"{k}: {v}")
        if a.live:
            conn.commit()
            print()
            print("--- verification ---")
            for k, v in verify(conn).items():
                print(f"{k}: {v}")
        else:
            conn.rollback()
            print()
            print("(dry run -- rolled back, nothing written)")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
