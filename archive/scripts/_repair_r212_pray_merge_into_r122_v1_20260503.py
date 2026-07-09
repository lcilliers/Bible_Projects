"""_repair_r212_pray_merge_into_r122_v1_20260503.py

Merges R212 (pray) into R122 (prayer) and marks R212 as excluded with reason
'duplicate of R122 prayer'.

Operations performed in a single transaction:

  1. Move 2 active OWNER terms (H0577, H6739) from R212 to R122:
     - mti_terms: owning_registry/owning_registry_fk/owning_word -> R122/'prayer'
     - wa_term_inventory: file_id -> R122's file (156)

  2. Delete-flag 31 XREF ti rows in R212's file (redundant; R122 already
     covers prayer's lexical territory).

  3. Delete-flag 3 inactive OWNER ti rows (H7593, H6760, H6761 — status=delete).

  4. Delete-flag R212's wa_file_index entry (file 236) — now empty.

  5. Resolve R212's 2 open research flags with reason 'registry_merged'.

  6. Mark R212:
     - phase1_status = 'Excluded'
     - description += merge audit trail
     - inference_note += merge note

Usage:
  python scripts/_repair_r212_pray_merge_into_r122_v1_20260503.py            # dry-run
  python scripts/_repair_r212_pray_merge_into_r122_v1_20260503.py --live     # apply
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

R212_ID = 212
R122_ID = 122
R212_FILE_ID = 236
R122_FILE_ID = 156
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Strong's to move (active OWNER terms in R212)
TERMS_TO_MOVE = ["H0577", "H6739"]

MERGE_NOTE = (
    f"Merged 2026-05-03: R212 'pray' identified as duplicate of R122 'prayer'. "
    f"OWNER terms H0577 (a.n.na 'Please!') and H6739 (tse.la 'to pray') "
    f"re-homed to R122. R212 XREF terms delete-flagged as redundant."
)


def fetch_state(conn) -> dict:
    """Snapshot current state for verification before/after."""
    cur = conn.cursor()
    state = {}

    # R212 OWNER ti count
    state["r212_owner_ti_active"] = cur.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
    """, (R212_ID,)).fetchone()[0]

    state["r212_xref_ti_active"] = cur.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND ti.term_owner_type='XREF' AND ti.delete_flagged=0
    """, (R212_ID,)).fetchone()[0]

    # R122 OWNER ti count
    state["r122_owner_ti_active"] = cur.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
    """, (R122_ID,)).fetchone()[0]

    # mti_terms ownership of moved Strong's
    state["moved_terms_ownership"] = {}
    for s in TERMS_TO_MOVE:
        r = cur.execute("""
            SELECT owning_registry, owning_registry_fk, owning_word
              FROM mti_terms WHERE strongs_number = ? AND delete_flagged=0
        """, (s,)).fetchone()
        state["moved_terms_ownership"][s] = dict(zip(
            ("owning_registry", "owning_registry_fk", "owning_word"), r
        )) if r else None

    # R212 phase1_status
    state["r212_phase1_status"] = cur.execute(
        "SELECT phase1_status FROM word_registry WHERE id = ?", (R212_ID,)
    ).fetchone()[0]

    # R212 file_index revision_note (proxy for state; table has no delete_flagged)
    r = cur.execute(
        "SELECT revision_note FROM wa_file_index WHERE id = ?", (R212_FILE_ID,)
    ).fetchone()
    state["r212_file_revision_note"] = (r[0] if r else None)

    # R212 open flags
    state["r212_open_flags"] = cur.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags
         WHERE registry_id = ? AND (resolved=0 OR resolved IS NULL)
    """, (R212_ID,)).fetchone()[0]

    return state


def show_state(label: str, state: dict) -> None:
    print(f"--- {label} ---")
    print(f"  R212 OWNER ti active: {state['r212_owner_ti_active']}")
    print(f"  R212 XREF ti active:  {state['r212_xref_ti_active']}")
    print(f"  R122 OWNER ti active: {state['r122_owner_ti_active']}")
    print(f"  R212 phase1_status:   {state['r212_phase1_status']!r}")
    print(f"  R212 file_index revision_note: {state['r212_file_revision_note']!r}")
    print(f"  R212 open research flags: {state['r212_open_flags']}")
    for s, info in state["moved_terms_ownership"].items():
        if info is None:
            print(f"  {s}: not found")
            continue
        print(f"  {s}: owning_registry={info['owning_registry']!r} "
              f"owning_registry_fk={info['owning_registry_fk']} "
              f"owning_word={info['owning_word']!r}")
    print()


def execute_merge(conn: sqlite3.Connection, dry: bool) -> dict:
    """Run all 6 steps in a single transaction. Returns counts dict."""
    cur = conn.cursor()
    counts = {}

    # Step 1a — mti_terms updates
    res = cur.executemany(
        """UPDATE mti_terms
              SET owning_registry='122', owning_registry_fk=?, owning_word='prayer',
                  last_changed=?
            WHERE strongs_number=? AND delete_flagged=0
               AND owning_registry_fk=?""",
        [(R122_ID, NOW_ISO, s, R212_ID) for s in TERMS_TO_MOVE]
    )
    counts["mti_terms_updated"] = res.rowcount

    # Step 1b — wa_term_inventory file_id move (only OWNER rows)
    placeholders = ",".join(["?"] * len(TERMS_TO_MOVE))
    cur.execute(f"""
        UPDATE wa_term_inventory
           SET file_id=?, last_changed=?
         WHERE strongs_number IN ({placeholders})
           AND term_owner_type='OWNER'
           AND delete_flagged=0
           AND file_id=?
    """, [R122_FILE_ID, NOW_ISO] + TERMS_TO_MOVE + [R212_FILE_ID])
    counts["ti_owner_moved"] = cur.rowcount

    # Step 2 — delete-flag R212's XREF ti rows
    cur.execute("""
        UPDATE wa_term_inventory
           SET delete_flagged=1, last_changed=?
         WHERE file_id=? AND term_owner_type='XREF' AND delete_flagged=0
    """, (NOW_ISO, R212_FILE_ID))
    counts["xref_ti_delete_flagged"] = cur.rowcount

    # Step 3 — delete-flag R212's inactive OWNER ti rows (status=delete)
    cur.execute("""
        UPDATE wa_term_inventory
           SET delete_flagged=1, last_changed=?
         WHERE file_id=? AND term_owner_type='OWNER' AND delete_flagged=0
           AND strongs_number IN (
             SELECT strongs_number FROM mti_terms WHERE status='delete'
           )
    """, (NOW_ISO, R212_FILE_ID))
    counts["inactive_owner_ti_delete_flagged"] = cur.rowcount

    # Step 4 — annotate R212's file_index (no delete_flagged column on this table)
    cur.execute("""
        UPDATE wa_file_index
           SET revision_note=COALESCE(revision_note,'') ||
                             CASE WHEN COALESCE(revision_note,'')='' THEN '' ELSE ' | ' END ||
                             ?,
               last_changed=?
         WHERE id=?
    """, (f"R212 merged into R122 on 2026-05-03; file orphaned (all ti rows delete-flagged)",
          NOW_ISO, R212_FILE_ID))
    counts["file_index_annotated"] = cur.rowcount

    # Step 5 — resolve R212's open research flags
    cur.execute("""
        UPDATE wa_session_research_flags
           SET resolved=1,
               resolved_note=?,
               resolved_date=?
         WHERE registry_id=? AND (resolved=0 OR resolved IS NULL)
    """, ("Registry merged into R122 prayer 2026-05-03 — duplicate", NOW_ISO, R212_ID))
    counts["research_flags_resolved"] = cur.rowcount

    # Step 6 — mark R212 excluded
    new_inference_note = (
        f"R212 EXCLUDED 2026-05-03 — duplicate of R122 prayer. "
        f"H0577 (Please!) and H6739 (to pray) merged into R122. "
        f"31 XREF terms delete-flagged as redundant. "
        f"phase1_status set to 'Excluded' per existing controlled vocab."
    )
    cur.execute("""
        UPDATE word_registry
           SET phase1_status='Excluded',
               session_b_status=NULL,
               verse_context_status=NULL,
               dim_review_status=NULL,
               inference_note=?,
               description=COALESCE(description,'') ||
                           CASE WHEN COALESCE(description,'')='' THEN '' ELSE ' | ' END ||
                           ?
         WHERE id=?
    """, (new_inference_note, MERGE_NOTE, R212_ID))
    counts["registry_marked_excluded"] = cur.rowcount

    if dry:
        conn.rollback()
        print("[DRY-RUN] All operations rolled back. No changes persisted.")
    else:
        conn.commit()
        print("[LIVE] All operations committed.")

    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply changes (default: dry-run)")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_r212_merge_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    state_before = fetch_state(conn)
    show_state("BEFORE", state_before)

    print("--- Executing merge operations ---")
    conn.execute("BEGIN")
    counts = execute_merge(conn, dry=not args.live)
    print()
    print("--- Counts ---")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print()

    state_after = fetch_state(conn)
    show_state("AFTER (post-rollback)" if not args.live else "AFTER (committed)",
               state_after)

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
