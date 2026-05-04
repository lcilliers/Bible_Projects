"""_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py

Migrate GAP-S1-001..GAP-S5-001 (8 questions, obs_ids 207-214) from
`wa_obs_question_catalogue` to `wa_session_research_flags` as SD pointers.

Background
----------
These 8 GAP-S* rows were added to the catalogue during R067 goodness obslog v3
work (2026-04-27). Researcher feedback (2026-04-28) identified the same
mis-categorisation pattern previously seen with GAP-N-001..003:

    > "GAP-S2-002 is word specific. This should be answered in goodness, if
    > not, it should be surfaced as to be researched further... I don't think
    > the QA method has achieved its objectives."

All 8 GAP-S* questions are programme-level methodology questions about how
the analytical framework treats specific structural patterns (multiple
semantic modes, negative/absence forms, multiple anchors, comparative modes,
distributed root families, multi-dimensional words). They are not per-word
analytical questions and do not belong in the generic obs catalogue.

Per the GAP-N precedent (see _apply_gap_n_migrate_to_sd_pointers_v1_20260428.py),
they belong as SD_POINTER rows in `wa_session_research_flags` sourced to R67
(where they were raised) with session_target='Session D'.

Sequence note: SP-067-009..018 are already populated with substantive R067
goodness SD pointers from the obslog. The previous GAP-N migration script
attempted SP-067-009..011 and silently skipped the inserts (idempotency check
saw the labels already populated) — that is a separate, known issue. This
script picks up the next free sequence at SP-067-019.

Three of the 8 questions already have answers captured against them
(GAP-S1-001 / GAP-S1-002 from R064 forgiveness, GAP-S2-001 from R030
contrition). Those answers are preserved in `wa_session_b_findings` and
remain reachable via the original `finding_id` foreign keys; the SD pointer
description references them so the Session D synthesist can find them.

Operations (transactional)
--------------------------
  1. Insert 8 SD_POINTER rows in wa_session_research_flags (SP-067-019..026)
  2. Soft-delete the 8 catalogue rows (wa_obs_question_catalogue.deleted=1)
     with a deleted_reason captured in review_note
  3. Soft-delete any wa_finding_catalogue_links rows pointing at these
     question_ids (delete_flagged=1) — the answers themselves remain in
     wa_session_b_findings, only the catalogue link is dropped

Pre-write backup taken automatically.

Usage
-----
  python scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py
  python scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py --live
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

# Map: catalogue obs_id -> new SD pointer flag_label, priority
# SP-067-019..026 continue the SP-067 sequence (max currently 018 from
# goodness obslog v2/v3 substantive pointers).
TARGETS = [
    {"obs_id": 207, "qcode": "GAP-S1-001", "new_label": "SP-067-019", "priority": "MEDIUM"},
    {"obs_id": 208, "qcode": "GAP-S1-002", "new_label": "SP-067-020", "priority": "MEDIUM"},
    {"obs_id": 209, "qcode": "GAP-S2-001", "new_label": "SP-067-021", "priority": "MEDIUM"},
    {"obs_id": 210, "qcode": "GAP-S2-002", "new_label": "SP-067-022", "priority": "MEDIUM"},
    {"obs_id": 211, "qcode": "GAP-S3-001", "new_label": "SP-067-023", "priority": "MEDIUM"},
    {"obs_id": 212, "qcode": "GAP-S3-002", "new_label": "SP-067-024", "priority": "MEDIUM"},
    {"obs_id": 213, "qcode": "GAP-S4-001", "new_label": "SP-067-025", "priority": "MEDIUM"},
    {"obs_id": 214, "qcode": "GAP-S5-001", "new_label": "SP-067-026", "priority": "MEDIUM"},
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def existing_answers(conn: sqlite3.Connection, obs_id: int) -> list[dict]:
    """Return non-stub catalogue links for this question, with finding registry/finding_id."""
    rows = conn.execute(
        """
        SELECT l.coverage, f.registry_id, f.finding_id
        FROM wa_finding_catalogue_links l
        LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE l.question_id = ?
          AND l.coverage IN ('full','partial')
          AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        ORDER BY f.registry_id, f.finding_id
        """,
        (obs_id,),
    ).fetchall()
    return [{"coverage": r[0], "registry_id": r[1], "finding_id": r[2]} for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_gap_s_migrate_{today_compact()}.db")
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
            row = conn.execute(
                "SELECT obs_id, question_code, deleted, SUBSTR(question_text,1,90) AS qt "
                "FROM wa_obs_question_catalogue WHERE obs_id = ?",
                (t["obs_id"],),
            ).fetchone()
            if row:
                print(f"  obs_id={row['obs_id']} {row['question_code']:12s} deleted={row['deleted']!s} qt: {row['qt']}...")
            existing_sp = conn.execute(
                "SELECT id FROM wa_session_research_flags WHERE flag_label = ?",
                (t["new_label"],),
            ).fetchone()
            if existing_sp:
                print(f"    NOTE: flag_label {t['new_label']} already exists at id {existing_sp['id']}")
            answers = existing_answers(conn, t["obs_id"])
            if answers:
                ans_str = ", ".join(
                    f"R{a['registry_id']:03d}/{a['finding_id']}" for a in answers
                )
                print(f"    existing answers: {ans_str}")

        # Idempotency: both legs need to be done
        sd_present, cat_deleted = [], []
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
            print("\n[idempotent] All 8 migrations complete; nothing to do.")
            return 0
        if any(sd_present) and not all(cat_deleted):
            print(
                f"\n[partial] SD pointer side: {sum(sd_present)}/8 present.  "
                f"Catalogue cleanup side: {sum(cat_deleted)}/8 deleted.  Will complete remaining work."
            )

        if not args.live:
            print("\n[DRY-RUN] would:")
            for t in TARGETS:
                answers = existing_answers(conn, t["obs_id"])
                ans_summary = (
                    f"  ({len(answers)} answer(s) on file: "
                    + ", ".join(f"R{a['registry_id']:03d}/{a['finding_id']}" for a in answers)
                    + ")"
                ) if answers else "  (no answers on file)"
                print(f"  - INSERT SD pointer {t['new_label']} (priority={t['priority']}) for R067{ans_summary}")
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

            # Check existing answers and append a pointer
            answers = existing_answers(conn, t["obs_id"])
            answer_pointer = ""
            if answers:
                refs = []
                for a in answers:
                    refs.append(f"R{a['registry_id']:03d} {a['finding_id']} ({a['coverage']})")
                answer_pointer = (
                    " [Partial answers already captured pre-migration in wa_session_b_findings: "
                    + "; ".join(refs)
                    + ". These remain accessible via finding_id; the catalogue link is being dropped only because the question is being re-classified.]"
                )

            description = (
                f"[Migrated from catalogue {t['qcode']} 2026-04-28 — programme-level "
                f"methodology question, not a per-word analytical question] "
                + row["question_text"]
                + answer_pointer
            )

            # Insert SD pointer (idempotent on flag_label)
            existing = conn.execute(
                "SELECT id FROM wa_session_research_flags WHERE flag_label = ?",
                (t["new_label"],),
            ).fetchone()
            if not existing:
                conn.execute(
                    """
                    INSERT INTO wa_session_research_flags
                        (registry_id, flag_code, flag_label, priority, description,
                         session_target, raised_date, resolved, session_raised)
                    VALUES (?, 'SD_POINTER', ?, ?, ?, 'Session D', ?, 0, ?)
                    """,
                    (
                        r067_id,
                        t["new_label"],
                        t["priority"],
                        description,
                        now_iso(),
                        "Session B Stage 2 (R067 goodness obslog v3); migrated from catalogue 2026-04-28",
                    ),
                )
                print(f"  inserted SD pointer {t['new_label']} ({t['qcode']})")
            else:
                print(f"  SD pointer {t['new_label']} already present; not re-inserted")

            # Soft-delete the catalogue row
            conn.execute(
                """
                UPDATE wa_obs_question_catalogue
                   SET deleted = 1,
                       review_note = COALESCE(review_note, '') ||
                                     ' [2026-04-28: migrated to ' || ? || ' as SD pointer per researcher direction; this row was mis-categorised as a catalogue question — it is a programme-level methodology Q for Session D synthesis]'
                 WHERE obs_id = ?
                """,
                (t["new_label"], t["obs_id"]),
            )
            print(f"    soft-deleted catalogue obs_id={t['obs_id']} ({t['qcode']})")

            # Soft-delete any orphan link rows
            n = conn.execute(
                """
                UPDATE wa_finding_catalogue_links
                   SET delete_flagged = 1
                 WHERE question_id = ? AND (delete_flagged = 0 OR delete_flagged IS NULL)
                """,
                (t["obs_id"],),
            ).rowcount
            if n:
                print(f"    soft-deleted {n} link row(s) referencing question_id={t['obs_id']}")

        conn.commit()
        print("\n[LIVE] committed.")

    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
