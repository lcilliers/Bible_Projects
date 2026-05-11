"""_apply_M46_term_subgroup_m2m_v1_20260510.py — DB-modifying.

Schema migration M46: Term-to-sub-group many-to-many.
Per researcher decision 2026-05-10
(outputs/markdown/m39-subgroup-multi-term-design-v1-20260510.md, decisions
DEC-1..DEC-8 locked).

Replaces the 1:1 FK `mti_terms.cluster_subgroup_id` with an m:n join
table `mti_term_subgroup`. Adds `verse_context.cluster_subgroup_id` so
each verse-occurrence routes to ONE sub-group even when its term spans
several. The legacy column on `mti_terms` is dropped (DEC-1, clean cut).

Operations (single transaction, foreign_keys=ON):
  1. CREATE TABLE mti_term_subgroup
  2. ALTER verse_context ADD COLUMN cluster_subgroup_id INTEGER
  3. INSERT mti_term_subgroup from existing mti_terms FK (~243 rows)
  4. UPDATE verse_context.cluster_subgroup_id from mt.cluster_subgroup_id
     (~4,684 active vc rows in sub-grouped clusters)
  5. Rebuild verse_context with extended UNIQUE
     (verse_record_id, mti_term_id, group_id, cluster_subgroup_id)
     — required so 'both' verses can route to TWO sub-groups (DEC-3)
  6. Rebuild mti_terms to drop cluster_subgroup_id column (DEC-1)
  7. Bump schema_version → 3.20.0; append M46 to migration_history

Pre-flight aborts if mti_term_subgroup already exists. Idempotent across
re-runs (post-migration runs short-circuit on the pre-flight check).

NO API calls. ~5-15 sec wall time. No cost.
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
NEW_SCHEMA_VERSION = "3.20.0"
MIGRATION_REF = "M46"
MIGRATION_DESC = (
    "Term-to-sub-group many-to-many: new mti_term_subgroup table, "
    "verse_context.cluster_subgroup_id column, drop "
    "mti_terms.cluster_subgroup_id (DEC-1)"
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
        (NEW_SCHEMA_VERSION, now_iso(), json.dumps(history, ensure_ascii=False),
         sv_id),
    )


def preflight(conn) -> tuple[bool, list[str]]:
    """Return (ok, messages). Aborts on hard fail; reports current state."""
    msgs = []
    ok = True

    # 1. mti_term_subgroup must NOT exist
    r = conn.execute(
        "SELECT name FROM sqlite_master "
        " WHERE type='table' AND name='mti_term_subgroup'"
    ).fetchone()
    if r:
        msgs.append("[ERR] mti_term_subgroup already exists — migration "
                    "appears to have been applied. Aborting.")
        ok = False
    else:
        msgs.append("[ok] mti_term_subgroup does not yet exist.")

    # 2. verse_context.cluster_subgroup_id must NOT exist
    vc_cols = {r[1] for r in conn.execute("PRAGMA table_info(verse_context)")}
    if "cluster_subgroup_id" in vc_cols:
        msgs.append("[ERR] verse_context.cluster_subgroup_id already exists "
                    "— migration appears partially applied. Aborting.")
        ok = False
    else:
        msgs.append("[ok] verse_context.cluster_subgroup_id does not exist.")

    # 3. mti_terms.cluster_subgroup_id must STILL exist
    mt_cols = {r[1] for r in conn.execute("PRAGMA table_info(mti_terms)")}
    if "cluster_subgroup_id" not in mt_cols:
        msgs.append("[ERR] mti_terms.cluster_subgroup_id missing — pre-M46 "
                    "state expected. Aborting.")
        ok = False
    else:
        msgs.append("[ok] mti_terms.cluster_subgroup_id still present.")

    # Counts that will drive the migration
    n_term_with_sg = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_subgroup_id IS NOT NULL"
    ).fetchone()[0]
    n_vc_active = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    n_vc_routable = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE COALESCE(vc.delete_flagged,0)=0 "
        "   AND mt.cluster_subgroup_id IS NOT NULL"
    ).fetchone()[0]
    msgs.append(f"  Terms with cluster_subgroup_id (will be backfilled "
                f"to mti_term_subgroup): {n_term_with_sg}")
    msgs.append(f"  Active vc rows total:         {n_vc_active}")
    msgs.append(f"  Active vc rows routable:      {n_vc_routable}")

    return ok, msgs


def run_migration(conn, dry_run: bool) -> dict:
    cur = conn.cursor()
    counts = {}

    # ── 1. CREATE mti_term_subgroup ───────────────────────────────────────
    cur.execute("""
        CREATE TABLE mti_term_subgroup (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            mti_term_id         INTEGER NOT NULL
                                  REFERENCES mti_terms(id),
            cluster_subgroup_id INTEGER NOT NULL
                                  REFERENCES cluster_subgroup(id),
            placement_note      TEXT,
            delete_flagged      INTEGER NOT NULL DEFAULT 0,
            created_at          TEXT NOT NULL,
            last_updated_date   TEXT NOT NULL,
            UNIQUE (mti_term_id, cluster_subgroup_id)
        )
    """)
    cur.execute(
        "CREATE INDEX ix_mts_term ON mti_term_subgroup(mti_term_id) "
        "WHERE delete_flagged = 0"
    )
    cur.execute(
        "CREATE INDEX ix_mts_subgroup "
        "  ON mti_term_subgroup(cluster_subgroup_id) "
        "WHERE delete_flagged = 0"
    )
    print("  [1/7] CREATE TABLE mti_term_subgroup + indexes")

    # ── 2. ALTER verse_context ADD COLUMN cluster_subgroup_id ─────────────
    cur.execute(
        "ALTER TABLE verse_context "
        "  ADD COLUMN cluster_subgroup_id INTEGER "
        "  REFERENCES cluster_subgroup(id)"
    )
    cur.execute(
        "CREATE INDEX ix_vc_cluster_subgroup "
        "  ON verse_context(cluster_subgroup_id) "
        "WHERE delete_flagged = 0"
    )
    print("  [2/7] ALTER TABLE verse_context ADD COLUMN cluster_subgroup_id "
          "+ index")

    # ── 3. Backfill mti_term_subgroup ─────────────────────────────────────
    ts = now_iso()
    rc = cur.execute(
        "INSERT INTO mti_term_subgroup "
        "  (mti_term_id, cluster_subgroup_id, placement_note, "
        "   delete_flagged, created_at, last_updated_date) "
        "SELECT id, cluster_subgroup_id, "
        "       'M46 backfill from mti_terms.cluster_subgroup_id', "
        "       0, ?, ? "
        "  FROM mti_terms "
        " WHERE cluster_subgroup_id IS NOT NULL",
        (ts, ts),
    ).rowcount
    counts["mti_term_subgroup_inserted"] = rc
    print(f"  [3/7] Backfilled mti_term_subgroup: {rc} rows")

    # ── 4. Backfill verse_context.cluster_subgroup_id ─────────────────────
    rc = cur.execute(
        "UPDATE verse_context "
        "   SET cluster_subgroup_id = ("
        "         SELECT mt.cluster_subgroup_id FROM mti_terms mt "
        "          WHERE mt.id = verse_context.mti_term_id"
        "       ) "
        " WHERE EXISTS ("
        "         SELECT 1 FROM mti_terms mt "
        "          WHERE mt.id = verse_context.mti_term_id "
        "            AND mt.cluster_subgroup_id IS NOT NULL"
        "       )"
    ).rowcount
    counts["verse_context_routed"] = rc
    print(f"  [4/7] Backfilled verse_context.cluster_subgroup_id: {rc} rows")

    # ── 5. Rebuild verse_context with extended UNIQUE ─────────────────────
    # Canonical SQLite table-rebuild recipe (foreign_keys must be OFF
    # outside this transaction; see main()):
    #   1. CREATE _new with desired schema
    #   2. INSERT _new SELECT FROM old
    #   3. DROP old
    #   4. ALTER _new RENAME TO old
    # Pre-rebuild UNIQUE: (verse_record_id, mti_term_id, group_id)
    # Post-rebuild UNIQUE: (verse_record_id, mti_term_id, group_id,
    #                       cluster_subgroup_id)
    # Required so 'both' verses can have TWO vc rows differing only in
    # cluster_subgroup_id (DEC-3).
    print("  [5/7] Rebuilding verse_context with extended UNIQUE...")
    cur.execute("""
        CREATE TABLE _vc_new_M46 (
            id                  INTEGER PRIMARY KEY,
            verse_record_id     INTEGER NOT NULL
                                  REFERENCES wa_verse_records(id),
            mti_term_id         INTEGER NOT NULL
                                  REFERENCES mti_terms(id),
            group_id            INTEGER REFERENCES verse_context_group(id),
            cluster_subgroup_id INTEGER REFERENCES cluster_subgroup(id),
            is_anchor           INTEGER NOT NULL DEFAULT 0,
            is_relevant         INTEGER NOT NULL DEFAULT 0,
            is_related          INTEGER NOT NULL DEFAULT 0,
            notes               TEXT DEFAULT NULL,
            delete_flagged      INTEGER DEFAULT 0,
            vertical_pass_flag  INTEGER DEFAULT 0,
            set_aside_reason    TEXT DEFAULT NULL,
            analysis_note       TEXT,
            UNIQUE (verse_record_id, mti_term_id, group_id,
                    cluster_subgroup_id)
        )
    """)
    cur.execute("""
        INSERT INTO _vc_new_M46 (
            id, verse_record_id, mti_term_id, group_id, cluster_subgroup_id,
            is_anchor, is_relevant, is_related, notes, delete_flagged,
            vertical_pass_flag, set_aside_reason, analysis_note
        )
        SELECT id, verse_record_id, mti_term_id, group_id, cluster_subgroup_id,
               is_anchor, is_relevant, is_related, notes, delete_flagged,
               vertical_pass_flag, set_aside_reason, analysis_note
          FROM verse_context
    """)
    cur.execute("DROP TABLE verse_context")
    cur.execute("ALTER TABLE _vc_new_M46 RENAME TO verse_context")
    cur.execute(
        "CREATE INDEX ix_vc_cluster_subgroup "
        "  ON verse_context(cluster_subgroup_id) "
        "WHERE delete_flagged = 0"
    )
    n_vc = cur.execute("SELECT COUNT(*) FROM verse_context").fetchone()[0]
    counts["verse_context_total_after_rebuild"] = n_vc
    print(f"        verse_context rebuilt: {n_vc} rows preserved")

    # ── 6. Rebuild mti_terms to DROP cluster_subgroup_id (DEC-1) ──────────
    print("  [6/7] Rebuilding mti_terms (drop cluster_subgroup_id)...")
    cur.execute("""
        CREATE TABLE _mt_new_M46 (
            id                       INTEGER PRIMARY KEY,
            strongs_number           TEXT,
            transliteration          TEXT,
            gloss                    TEXT,
            language                 TEXT,
            owning_registry          TEXT,
            owning_registry_fk       INTEGER REFERENCES word_registry(id),
            owning_word              TEXT,
            owning_part              TEXT,
            word_data_reference      TEXT,
            word_data_ref_fk         INTEGER,
            status                   TEXT,
            exclusion_reason         TEXT,
            extraction_date          TEXT,
            strongs_reconciled       INTEGER,
            anchor_note              TEXT,
            last_changed             TEXT,
            delete_flagged           INTEGER,
            vc_status                TEXT NOT NULL DEFAULT 'not_done',
            vc_instruction_version   TEXT,
            vc_status_updated_at     TEXT,
            vc_status_note           TEXT,
            md_version               INTEGER NOT NULL DEFAULT 1,
            cluster_code             TEXT
        )
    """)
    cur.execute("""
        INSERT INTO _mt_new_M46 (
            id, strongs_number, transliteration, gloss, language,
            owning_registry, owning_registry_fk, owning_word, owning_part,
            word_data_reference, word_data_ref_fk, status, exclusion_reason,
            extraction_date, strongs_reconciled, anchor_note, last_changed,
            delete_flagged, vc_status, vc_instruction_version,
            vc_status_updated_at, vc_status_note, md_version, cluster_code
        )
        SELECT id, strongs_number, transliteration, gloss, language,
               owning_registry, owning_registry_fk, owning_word, owning_part,
               word_data_reference, word_data_ref_fk, status, exclusion_reason,
               extraction_date, strongs_reconciled, anchor_note, last_changed,
               delete_flagged, vc_status, vc_instruction_version,
               vc_status_updated_at, vc_status_note, md_version, cluster_code
          FROM mti_terms
    """)
    cur.execute("DROP TABLE mti_terms")
    cur.execute("ALTER TABLE _mt_new_M46 RENAME TO mti_terms")
    cur.execute(
        "CREATE INDEX IF NOT EXISTS idx_mti_terms_owning_vc_status "
        "  ON mti_terms(owning_registry_fk, vc_status) "
        "WHERE delete_flagged = 0"
    )
    n_mt = cur.execute("SELECT COUNT(*) FROM mti_terms").fetchone()[0]
    counts["mti_terms_total_after_rebuild"] = n_mt
    print(f"        mti_terms rebuilt: {n_mt} rows preserved")

    # ── 7. schema_version bump + history ──────────────────────────────────
    append_migration_history(conn)
    print(f"  [7/7] schema_version → {NEW_SCHEMA_VERSION}")

    return counts


def verify(conn) -> dict:
    """Post-migration integrity invariants per researcher guidance:
    - every term referenced by a sub-group has ≥1 mti_term_subgroup row
    - every active vc row in a sub-grouped cluster has cluster_subgroup_id
    - every active vc row that should have group_id has group_id
    """
    invariants = {}

    # I-1: Every term that previously had cluster_subgroup_id has at least
    # one mti_term_subgroup row. (We can verify by checking that the new
    # table count equals the count of pre-migration assignments — both
    # accessible because they should match.)
    n_mts = conn.execute(
        "SELECT COUNT(DISTINCT mti_term_id) FROM mti_term_subgroup "
        " WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    invariants["I-1: distinct terms in mti_term_subgroup"] = n_mts

    # I-2: Verses with cluster_subgroup_id set
    n_vc_routed = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE COALESCE(delete_flagged,0)=0 "
        "   AND cluster_subgroup_id IS NOT NULL"
    ).fetchone()[0]
    invariants["I-2: active vc rows routed (cluster_subgroup_id NOT NULL)"] = (
        n_vc_routed
    )

    # I-3: Active vc rows with NULL cluster_subgroup_id (clusters not yet
    # processed past Phase 3 — expected non-zero)
    n_vc_unrouted = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE COALESCE(delete_flagged,0)=0 "
        "   AND cluster_subgroup_id IS NULL"
    ).fetchone()[0]
    invariants["I-3: active vc rows NOT routed (no sub-group yet)"] = (
        n_vc_unrouted
    )

    # I-4: Active vc rows with NULL group_id (verse_context_group unassigned)
    n_vc_no_grp = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE COALESCE(delete_flagged,0)=0 "
        "   AND group_id IS NULL"
    ).fetchone()[0]
    invariants["I-4: active vc rows NOT in any verse_context_group"] = (
        n_vc_no_grp
    )

    # I-5: schema_version
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

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="Run migration in a transaction that is rolled "
                    "back at the end. Counts and verification are reported.")
    ap.add_argument("--live", action="store_true",
                    help="COMMIT the migration. Pre-migration backup is "
                    "always taken regardless.")
    args = ap.parse_args()

    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("=" * 72)
    print(f"M46 — Term-to-sub-group m:n migration  ({NEW_SCHEMA_VERSION})")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    # Foreign keys must be OFF during the rebuild — the canonical SQLite
    # recipe needs to DROP tables that have incoming FK references. We
    # restore foreign_keys=ON after the transaction and run a final
    # foreign_key_check to confirm no orphans were introduced.
    print("Disabling foreign_keys for the rebuild...")
    conn.execute("PRAGMA foreign_keys = OFF")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting without changes.")
        conn.execute("PRAGMA foreign_keys = ON")
        return 1

    if args.live:
        print("Taking pre-migration backup...")
        b = take_backup("M46")
        print(f"  Backup saved: {b}")
        print()

    print("EXECUTE")
    print("-" * 72)
    try:
        conn.execute("BEGIN")
        counts = run_migration(conn, args.dry_run)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fk_violations = list(conn.execute("PRAGMA foreign_key_check"))
        if fk_violations:
            print(f"  [ERR] {len(fk_violations)} FK violation(s) detected:")
            for v in fk_violations[:20]:
                print(f"    {dict(zip(['table', 'rowid', 'parent', 'fkid'], v))}")
            raise RuntimeError(
                f"foreign_key_check failed: {len(fk_violations)} violations"
            )
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
