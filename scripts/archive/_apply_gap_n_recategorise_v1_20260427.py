"""_apply_gap_n_recategorise_v1_20260427.py

Re-categorise the 3 GAP-N-* generic catalogue rows (added 2026-04-27 from R067
goodness obslog v3) so they're picked up by the readiness sweep's
`section LIKE 'Section %'` filter.

All three are dimension-classification questions — they fit Section 1
(Word Characteristic Summary) since they concern the word's structural
relation to the dimension vocabulary.

Updates:
  obs_id=221 GAP-N-001  section: 'Generic — Gap (R067 obslog v3)'
                              → 'Section 1 — Generic (gap addition R067 obslog v3)'
  obs_id=222 GAP-N-002  section: same → same
  obs_id=223 GAP-N-003  section: same → same

Idempotent: re-running on a DB where the section is already updated produces
no further changes.

Usage:
  python scripts/archive/_apply_gap_n_recategorise_v1_20260427.py
  python scripts/archive/_apply_gap_n_recategorise_v1_20260427.py --live
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

OLD_SECTION = "Generic — Gap (R067 obslog v3)"
NEW_SECTION = "Section 1 — Generic (gap addition R067 obslog v3)"
TARGET_OBS_IDS = (221, 222, 223)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_gap_n_recategorise_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    try:
        if args.live:
            conn.execute("BEGIN")

        # Pre-state
        rows = conn.execute("""
            SELECT obs_id, question_code, section
              FROM wa_obs_question_catalogue
             WHERE obs_id IN (?,?,?)
        """, TARGET_OBS_IDS).fetchall()
        print("=== Pre-state ===")
        for r in rows:
            print(f"  obs_id={r[0]:4d} {r[1]:12s} section={r[2]!r}")

        if not rows:
            print("ERROR: no rows found for target obs_ids.")
            return 1

        # Are any already updated?
        already = sum(1 for r in rows if r[2] == NEW_SECTION)
        if already == len(rows):
            print(f"\n[idempotent] All {len(rows)} rows already at NEW_SECTION; nothing to do.")
            return 0
        if already > 0:
            print(f"\n[partial] {already} of {len(rows)} already at NEW_SECTION; only the {len(rows)-already} not-yet-updated row(s) will change.")

        if not args.live:
            print(f"\n[DRY-RUN] would UPDATE {len(rows)-already} row(s) section field "
                  f"from {OLD_SECTION!r} to {NEW_SECTION!r}")
            return 0

        # wa_obs_question_catalogue has no last_modified column; section + the
        # appended ' obslog v3' marker carry the change-trail.
        cur = conn.execute("""
            UPDATE wa_obs_question_catalogue
               SET section = ?
             WHERE obs_id IN (?,?,?)
               AND section = ?
        """, (NEW_SECTION, *TARGET_OBS_IDS, OLD_SECTION))
        n = cur.rowcount
        conn.commit()
        print(f"\n[LIVE] {n} row(s) updated; committed.")

        # Post-state
        print("\n=== Post-state ===")
        for r in conn.execute("""
            SELECT obs_id, question_code, section
              FROM wa_obs_question_catalogue
             WHERE obs_id IN (?,?,?)
        """, TARGET_OBS_IDS):
            print(f"  obs_id={r[0]:4d} {r[1]:12s} section={r[2]!r}")

    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
