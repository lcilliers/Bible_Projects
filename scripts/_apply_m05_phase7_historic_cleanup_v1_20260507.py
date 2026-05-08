"""_apply_m05_phase7_historic_cleanup_v1_20260507.py — DB-modifying.

Lightweight cleanup of two historic items flagged before Phase 8:

  1. Group 3602 (anoche, mti=7502): two vc rows point at wa_verse_records
     233380 and 233381 whose mti_term_id is NULL (orphan vr rows). Soft-
     delete the two vc rows and append a note to the group recording
     that anoche needs a STEP extraction before it can be re-anchored.

  2. Five M05 groups carry two is_anchor=1 rows from before this work:
     1549, 1551, 1566, 1591, 3218. Keep the lower-id anchor and clear
     is_anchor on the higher-id duplicate. (Group 1583 also appears in
     the diagnosis pass but is now anc=0 — the residue of unrouted
     verses, separate issue, leave alone.)

Idempotent. Run inside a single transaction.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

# Soft-delete vc rows in this group (orphan vr rows; mti=NULL on vr).
ORPHAN_GROUP = 3602
ORPHAN_NOTE_APPEND = (
    " | 2026-05-07: 2 vc rows soft-deleted (vr=233380, 233381 are "
    "orphan rows with mti_term_id=NULL on wa_verse_records). "
    "anoche (mti=7502) needs STEP extraction before re-anchoring. "
    "Standing item before Phase 8."
)

# (group_id, vc_id_to_keep_anchor) — anchor stays on the lower vc.id;
# the *other* anchor row in the group is cleared.
ANCHOR_DUPES = [
    (1549, 28014),  # vr=5041 kept; vc.id=28015 (vr=5042) cleared
    (1551, 28017),  # vr=66981 kept; vc.id=28018 (vr=66980) cleared
    (1566, 28070),  # vr=66976 kept; vc.id=28071 (vr=66973) cleared
    (1591, 28368),  # vr=4352  kept; vc.id=28369 (vr=65372) cleared
    (3218, 58056),  # vr=54301 kept; vc.id=58058 (vr=54303) cleared
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    n_orphan_soft_deleted = 0
    n_group_note_updated = 0
    n_anchor_cleared = 0

    try:
        conn.execute("BEGIN")

        # --- 1. Orphan vc rows in group 3602 ---
        orphans = list(conn.execute(
            "SELECT vc.id "
            "  FROM verse_context vc "
            "  LEFT JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
            " WHERE vc.group_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0 "
            "   AND vr.mti_term_id IS NULL",
            (ORPHAN_GROUP,),
        ))
        for r in orphans:
            conn.execute(
                "UPDATE verse_context "
                "   SET delete_flagged=1, "
                "       set_aside_reason=COALESCE(set_aside_reason,'') "
                "         || ' | orphan vr row (vr.mti=NULL); cleanup 2026-05-07' "
                " WHERE id=?",
                (r["id"],),
            )
            n_orphan_soft_deleted += 1

        # Update group notes (verse_context_group has: notes column only —
        # no last_updated_date column on this table).
        cur_note = conn.execute(
            "SELECT notes FROM verse_context_group WHERE id=?",
            (ORPHAN_GROUP,),
        ).fetchone()
        if cur_note is not None:
            new_notes = (cur_note["notes"] or "") + ORPHAN_NOTE_APPEND
            conn.execute(
                "UPDATE verse_context_group SET notes=? WHERE id=?",
                (new_notes, ORPHAN_GROUP),
            )
            n_group_note_updated = 1

        # --- 2. anchor=2 cleanup ---
        for gid, keep_id in ANCHOR_DUPES:
            res = conn.execute(
                "UPDATE verse_context "
                "   SET is_anchor=0 "
                " WHERE group_id=? "
                "   AND is_anchor=1 "
                "   AND id != ? "
                "   AND COALESCE(delete_flagged,0)=0",
                (gid, keep_id),
            )
            n_anchor_cleared += res.rowcount or 0

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print(f"Orphan vc rows soft-deleted (group 3602): {n_orphan_soft_deleted}")
    print(f"Group 3602 notes appended: {n_group_note_updated}")
    print(f"Duplicate anchors cleared:               {n_anchor_cleared}")

    # --- Verification ---
    print()
    print("Verification — M05 groups with anchor count != 1:")
    bad = list(conn.execute("""
        SELECT vcg.id AS gid, vcg.group_code,
               SUM(vc.is_anchor) AS anc, COUNT(vc.id) AS verses
          FROM verse_context_group vcg
          JOIN verse_context vc ON vc.group_id=vcg.id
          JOIN mti_terms mt ON mt.id=vcg.mti_term_id
         WHERE mt.cluster_code='M05'
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY vcg.id HAVING anc != 1
         ORDER BY vcg.id
    """))
    if not bad:
        print("  (none)")
    else:
        for r in bad:
            print(f"  gid={r['gid']:5d} code={r['group_code']:14s} "
                  f"anc={r['anc']} verses={r['verses']}")

    # 3602 follow-up state
    print()
    print("Group 3602 active vc rows after cleanup:")
    for r in conn.execute(
        "SELECT id, verse_record_id, is_anchor, "
        "       COALESCE(delete_flagged,0) AS df "
        "  FROM verse_context WHERE group_id=? "
        " ORDER BY id",
        (ORPHAN_GROUP,),
    ):
        print(f"  vc.id={r['id']} vr={r['verse_record_id']} "
              f"anchor={r['is_anchor']} df={r['df']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
