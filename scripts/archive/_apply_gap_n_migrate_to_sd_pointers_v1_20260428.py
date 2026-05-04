"""_apply_gap_n_migrate_to_sd_pointers_v1_20260428.py

Migrate GAP-N-001/002/003 from `wa_obs_question_catalogue` to
`wa_session_research_flags` as SD pointers.

These 3 rows were added on 2026-04-27 as a result of R067 goodness obslog v3
work. Researcher feedback (2026-04-28) corrected the categorisation:

  > "GAP-N-002 and GAP-N-003 is a word specific SD Pointer, not a catalogue
  > question. So it should be removed from the catalogue and be added to
  > the SD pointer table."

The same applies to GAP-N-001 (it's the same triplet — programme-level
methodology questions about dimension vocabulary, not per-word analytical
questions). They belong as SD_POINTER rows in `wa_session_research_flags`
sourced to R067 (where they were raised), with session_target='D'.

Operations (transactional):
  1. Insert 3 SD_POINTER rows in wa_session_research_flags
     (registry_id = R067 id, flag_label = 'SP-067-009/010/011', priority,
      session_target='Session D', description = original question text + context)
  2. Soft-delete the 3 catalogue rows (wa_obs_question_catalogue.deleted=1)
     with a deleted_reason captured in review_note
  3. Soft-delete any wa_finding_catalogue_links rows pointing at these
     question_ids (delete_flagged=1) — they're orphan citations now

Pre-write backup taken automatically.

Usage:
  python scripts/archive/_apply_gap_n_migrate_to_sd_pointers_v1_20260428.py
  python scripts/archive/_apply_gap_n_migrate_to_sd_pointers_v1_20260428.py --live
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

# Map: catalogue obs_id → new SD pointer flag_label, priority
# SP-067-001..008 already in DB from R067 goodness work; new SD pointers
# continue the sequence at 009..011.
TARGETS = [
    {"obs_id": 221, "qcode": "GAP-N-001", "new_label": "SP-067-009", "priority": "MEDIUM"},
    {"obs_id": 222, "qcode": "GAP-N-002", "new_label": "SP-067-010", "priority": "MEDIUM"},
    {"obs_id": 223, "qcode": "GAP-N-003", "new_label": "SP-067-011", "priority": "MEDIUM"},
]


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
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_gap_n_migrate_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.live:
        conn.execute("BEGIN")

    try:
        # Find R067 registry id
        r = conn.execute("SELECT id FROM word_registry WHERE no = 67").fetchone()
        if not r:
            print("ERROR: R067 not found")
            return 1
        r067_id = r["id"]

        # Pre-state report
        print("=== Pre-state ===\n")
        for t in TARGETS:
            r = conn.execute(
                "SELECT obs_id, question_code, deleted, SUBSTR(question_text,1,80) AS qt "
                "FROM wa_obs_question_catalogue WHERE obs_id = ?", (t["obs_id"],),
            ).fetchone()
            if r:
                print(f"  catalogue obs_id={r['obs_id']} {r['question_code']:12s} deleted={r['deleted']!s} text: {r['qt']}...")
            existing_sp = conn.execute(
                "SELECT id FROM wa_session_research_flags WHERE flag_label = ?",
                (t["new_label"],),
            ).fetchone()
            if existing_sp:
                print(f"  flag_label {t['new_label']} already exists at id {existing_sp['id']}")

        # Idempotency: check both legs (SD pointer present AND catalogue row deleted).
        # Each target may need either or both halves done.
        sd_present = []
        cat_deleted = []
        for t in TARGETS:
            sd = conn.execute(
                "SELECT 1 FROM wa_session_research_flags WHERE flag_label = ?",
                (t["new_label"],),
            ).fetchone()
            cat = conn.execute(
                "SELECT deleted FROM wa_obs_question_catalogue WHERE obs_id = ?",
                (t["obs_id"],),
            ).fetchone()
            sd_present.append(bool(sd))
            cat_deleted.append(bool(cat and cat["deleted"]))
        if all(sd_present) and all(cat_deleted):
            print(f"\n[idempotent] All 3 migrations complete (SD pointers present + catalogue rows deleted); nothing to do.")
            return 0
        if any(sd_present) and not all(cat_deleted):
            print(f"\n[partial] SD pointer side: {sum(sd_present)}/3 present.  Catalogue cleanup side: {sum(cat_deleted)}/3 deleted.  Will complete remaining work.")

        if not args.live:
            print("\n[DRY-RUN] would:")
            for t in TARGETS:
                print(f"  · INSERT SD pointer {t['new_label']} (priority={t['priority']}) for R067")
                print(f"    soft-delete catalogue obs_id={t['obs_id']} ({t['qcode']})")
                print(f"    soft-delete any wa_finding_catalogue_links rows where question_id={t['obs_id']}")
            return 0

        # Live writes
        for t in TARGETS:
            # Get the original question text for the SD description
            row = conn.execute(
                "SELECT question_text FROM wa_obs_question_catalogue WHERE obs_id = ?",
                (t["obs_id"],),
            ).fetchone()
            if not row:
                print(f"  WARN: catalogue obs_id={t['obs_id']} not found; skipping SD insert")
                continue
            description = (
                f"[Migrated from catalogue {t['qcode']} 2026-04-28] " + row["question_text"]
            )

            # Insert SD pointer (idempotent on flag_label)
            existing = conn.execute(
                "SELECT id FROM wa_session_research_flags WHERE flag_label = ?",
                (t["new_label"],),
            ).fetchone()
            if not existing:
                conn.execute("""
                    INSERT INTO wa_session_research_flags
                        (registry_id, flag_code, flag_label, priority, description,
                         session_target, raised_date, resolved, session_raised)
                    VALUES (?, 'SD_POINTER', ?, ?, ?, 'Session D', ?, 0, ?)
                """, (r067_id, t["new_label"], t["priority"], description, now_iso(),
                      "Session B Stage 2 (R067 goodness obslog v3); migrated from catalogue 2026-04-28"))
                print(f"  inserted SD pointer {t['new_label']}")

            # Soft-delete the catalogue row
            conn.execute("""
                UPDATE wa_obs_question_catalogue
                   SET deleted = 1,
                       review_note = COALESCE(review_note, '') ||
                                     ' [2026-04-28: migrated to ' || ? || ' as SD pointer per researcher direction; this row was mis-categorised as a catalogue question — it is a programme-level methodology Q for Session D synthesis]'
                 WHERE obs_id = ?
            """, (t["new_label"], t["obs_id"]))
            print(f"  soft-deleted catalogue obs_id={t['obs_id']} ({t['qcode']})")

            # Soft-delete any orphan link rows
            n = conn.execute("""
                UPDATE wa_finding_catalogue_links
                   SET delete_flagged = 1
                 WHERE question_id = ? AND (delete_flagged = 0 OR delete_flagged IS NULL)
            """, (t["obs_id"],)).rowcount
            if n:
                print(f"    soft-deleted {n} link row(s) referencing question_id={t['obs_id']}")

        conn.commit()
        print("\n[LIVE] committed.")

    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
