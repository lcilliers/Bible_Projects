"""_apply_M47_vcg_term_m2m_v1_20260510.py — DB-modifying.

Schema migration M47: vcg-to-term many-to-many.
Per researcher decision 2026-05-10 — under DIR-M26-20260510-003 the
NEW-01/02/03/06 vcgs need to span multiple Strong's terms (Proverbs
outcomes, Ezekiel precarious standing, counterfeit righteousness,
hunger/pursuit). The current schema's `verse_context_group.mti_term_id
NOT NULL` ties each vcg to one term, forcing per-term forks of every
shared meaning. M47 relaxes this to m:n via a `vcg_term` join table
(mirroring M46 for term ↔ sub-group).

Decisions locked:
  DEC-1 (per M46 precedent) — drop legacy `vcg.mti_term_id` column
  DEC-2 (per M46 precedent) — no `is_primary` flag in vcg_term
  DEC-3 — keep existing per-term group_codes (e.g. 911-001) as-is;
          new cluster-prefixed codes (e.g. M26-A2-001) only for
          NEW vcgs created post-M47
  DEC-4 — backfill: one row per existing active vcg
  DEC-5 — global migration (all clusters)

Operations (single transaction, foreign_keys=OFF for table rebuild):
  1. CREATE TABLE vcg_term
  2. INSERT INTO vcg_term SELECT id, mti_term_id FROM verse_context_group
  3. Rebuild verse_context_group dropping mti_term_id column
  4. PRAGMA foreign_key_check; bump schema_version → 3.21.0

Pre-flight aborts if vcg_term already exists, or if vcg.mti_term_id
is already gone (re-running on a migrated DB).

NO API calls. ~5 sec wall time. No cost.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
NEW_SCHEMA_VERSION = "3.21.0"
MIGRATION_REF = "M47"
MIGRATION_DESC = (
    "vcg-to-term many-to-many: new vcg_term join table; drop "
    "verse_context_group.mti_term_id (DEC-1 precedent from M46)"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR,
                        f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, path)
    return path


def append_migration_history(conn) -> None:
    row = conn.execute(
        "SELECT id, migration_history FROM schema_version "
        "ORDER BY id DESC LIMIT 1"
    ).fetchone()
    if not row:
        return
    sv_id, hist_json = row[0], row[1]
    history = json.loads(hist_json or "[]")
    if any(e.get("version") == MIGRATION_REF for e in history):
        return
    history.append({
        "version": MIGRATION_REF,
        "description": MIGRATION_DESC,
        "applied_at": now_iso(),
    })
    conn.execute(
        "UPDATE schema_version SET version_code=?, applied_at=?, "
        "       migration_history=? "
        " WHERE id=?",
        (NEW_SCHEMA_VERSION, now_iso(),
         json.dumps(history, ensure_ascii=False), sv_id),
    )


def preflight(conn) -> tuple[bool, list[str]]:
    msgs = []
    ok = True

    r = conn.execute(
        "SELECT name FROM sqlite_master "
        " WHERE type='table' AND name='vcg_term'"
    ).fetchone()
    if r:
        msgs.append("[ERR] vcg_term already exists — migration "
                    "appears applied. Aborting.")
        ok = False
    else:
        msgs.append("[ok] vcg_term does not yet exist.")

    cols = {r[1] for r in conn.execute(
        "PRAGMA table_info(verse_context_group)")}
    if "mti_term_id" not in cols:
        msgs.append("[ERR] verse_context_group.mti_term_id is missing "
                    "— pre-M47 state expected. Aborting.")
        ok = False
    else:
        msgs.append("[ok] verse_context_group.mti_term_id still present.")

    n_active = conn.execute(
        "SELECT COUNT(*) FROM verse_context_group "
        " WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    n_total = conn.execute(
        "SELECT COUNT(*) FROM verse_context_group"
    ).fetchone()[0]
    msgs.append(f"  Active vcg rows (will get vcg_term entry): {n_active}")
    msgs.append(f"  All vcg rows (will be preserved through rebuild): "
                f"{n_total}")

    n_term_null = conn.execute(
        "SELECT COUNT(*) FROM verse_context_group "
        " WHERE mti_term_id IS NULL"
    ).fetchone()[0]
    if n_term_null:
        msgs.append(f"[WARN] {n_term_null} vcg rows have NULL mti_term_id "
                    f"and will not be backfilled into vcg_term")
    return ok, msgs


def run_migration(conn) -> dict:
    cur = conn.cursor()
    counts = {}

    # 1. CREATE vcg_term
    cur.execute("""
        CREATE TABLE vcg_term (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            vcg_id          INTEGER NOT NULL
                              REFERENCES verse_context_group(id),
            mti_term_id     INTEGER NOT NULL
                              REFERENCES mti_terms(id),
            placement_note  TEXT,
            delete_flagged  INTEGER NOT NULL DEFAULT 0,
            created_at      TEXT NOT NULL,
            last_updated_date TEXT NOT NULL,
            UNIQUE (vcg_id, mti_term_id)
        )
    """)
    cur.execute(
        "CREATE INDEX ix_vcgt_vcg ON vcg_term(vcg_id) "
        "WHERE delete_flagged = 0"
    )
    cur.execute(
        "CREATE INDEX ix_vcgt_term ON vcg_term(mti_term_id) "
        "WHERE delete_flagged = 0"
    )
    print("  [1/4] CREATE TABLE vcg_term + indexes")

    # 2a. Backfill from current vcg.mti_term_id
    ts = now_iso()
    rc = cur.execute(
        "INSERT INTO vcg_term "
        "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
        "   created_at, last_updated_date) "
        "SELECT id, mti_term_id, "
        "       'M47 backfill from vcg.mti_term_id', "
        "       COALESCE(delete_flagged, 0), ?, ? "
        "  FROM verse_context_group "
        " WHERE mti_term_id IS NOT NULL",
        (ts, ts),
    ).rowcount
    counts["vcg_term_backfill_primary"] = rc
    print(f"  [2a] Backfilled vcg_term from existing 1:1: {rc} rows")

    # 2b. Absorb pre-existing cross-term placements. Some analysts had
    # already placed vc rows of one term under a vcg owned by another
    # term (e.g. M06 H8135 ↔ H8130, M15 H0995 ↔ G4907) — analytically
    # intentional but not expressible under the old schema. Under m:n
    # we add the missing vcg_term row so the placement becomes
    # legitimate. Only absorb when the vcg is ACTIVE; vc rows pointing
    # at soft-deleted vcgs are a separate data quality issue surfaced
    # by H3 in the comprehensive report.
    rc = cur.execute(
        "INSERT OR IGNORE INTO vcg_term "
        "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
        "   created_at, last_updated_date) "
        "SELECT DISTINCT vc.group_id, vc.mti_term_id, "
        "       'M47 absorb pre-existing cross-term vc placement', "
        "       0, ?, ? "
        "  FROM verse_context vc "
        "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        " WHERE vc.group_id IS NOT NULL "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND COALESCE(vcg.delete_flagged,0)=0 "
        "   AND vc.mti_term_id != vcg.mti_term_id",
        (ts, ts),
    ).rowcount
    counts["vcg_term_absorb_cross_term"] = rc
    print(f"  [2b] Absorbed cross-term placements: {rc} rows")

    # 3. Rebuild verse_context_group to drop mti_term_id (canonical
    #    SQLite recipe — foreign_keys must be OFF outside this txn)
    print("  [3] Rebuilding verse_context_group "
          "(drop mti_term_id)...")
    cur.execute("""
        CREATE TABLE _vcg_new_M47 (
            id                  INTEGER PRIMARY KEY,
            group_code          TEXT NOT NULL UNIQUE,
            context_description TEXT NOT NULL,
            notes               TEXT DEFAULT NULL,
            delete_flagged      INTEGER DEFAULT 0,
            vertical_pass_flag  INTEGER DEFAULT 0
        )
    """)
    cur.execute("""
        INSERT INTO _vcg_new_M47 (
            id, group_code, context_description, notes,
            delete_flagged, vertical_pass_flag
        )
        SELECT id, group_code, context_description, notes,
               delete_flagged, vertical_pass_flag
          FROM verse_context_group
    """)
    cur.execute("DROP TABLE verse_context_group")
    cur.execute("ALTER TABLE _vcg_new_M47 RENAME TO verse_context_group")
    n_vcg = cur.execute(
        "SELECT COUNT(*) FROM verse_context_group"
    ).fetchone()[0]
    counts["vcg_total_after_rebuild"] = n_vcg
    print(f"        verse_context_group rebuilt: {n_vcg} rows preserved")

    # 4. Schema version bump
    append_migration_history(conn)
    print(f"  [4] schema_version → {NEW_SCHEMA_VERSION}")

    return counts


def verify(conn) -> dict:
    invariants = {}

    n_vcgt = conn.execute(
        "SELECT COUNT(*) FROM vcg_term WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    invariants["I-1: active vcg_term rows"] = n_vcgt

    n_vcg_active = conn.execute(
        "SELECT COUNT(*) FROM verse_context_group "
        " WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    invariants["I-2: active vcg rows"] = n_vcg_active

    # Every active vcg should have at least one vcg_term row (the backfill)
    n_vcg_no_term = conn.execute("""
        SELECT COUNT(*) FROM verse_context_group vcg
         WHERE COALESCE(vcg.delete_flagged,0)=0
           AND NOT EXISTS (
               SELECT 1 FROM vcg_term vt
                WHERE vt.vcg_id = vcg.id
                  AND COALESCE(vt.delete_flagged,0)=0
           )
    """).fetchone()[0]
    invariants["I-3: active vcgs WITHOUT a vcg_term row "
               "(expected 0)"] = n_vcg_no_term

    # Cross-term integrity: every active vc.group_id must point at a vcg
    # whose vcg_term set includes vc.mti_term_id (= the new H3 definition)
    n_h3 = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
         WHERE vc.group_id IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
           AND NOT EXISTS (
               SELECT 1 FROM vcg_term vt
                WHERE vt.vcg_id = vc.group_id
                  AND vt.mti_term_id = vc.mti_term_id
                  AND COALESCE(vt.delete_flagged,0)=0
           )
    """).fetchone()[0]
    invariants["I-4: H3 violations under new check (expected 0)"] = n_h3

    sv = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()[0]
    invariants["I-5: schema_version"] = sv

    return invariants


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"M47 — vcg-to-term m:n migration  ({NEW_SCHEMA_VERSION})")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Disabling foreign_keys for the rebuild...")
    conn.execute("PRAGMA foreign_keys = OFF")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        conn.execute("PRAGMA foreign_keys = ON")
        print("Pre-flight failed — exiting without changes.")
        return 1

    if args.live:
        print("Taking pre-migration backup...")
        b = take_backup("M47")
        print(f"  Backup saved: {b}")
        print()

    print("EXECUTE")
    print("-" * 72)
    try:
        conn.execute("BEGIN")
        counts = run_migration(conn)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            print(f"  [ERR] {len(fkv)} FK violations")
            for v in fkv[:20]:
                print(f"    {dict(zip(['table','rowid','parent','fkid'], v))}")
            raise RuntimeError(f"foreign_key_check failed: {len(fkv)}")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: changes rolled back.")
        else:
            conn.execute("COMMIT")
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {type(e).__name__}: {e}")
        conn.execute("PRAGMA foreign_keys = ON")
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:45s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
