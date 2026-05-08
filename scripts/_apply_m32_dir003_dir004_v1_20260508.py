"""_apply_m32_dir003_dir004_v1_20260508.py — DB-modifying.

Applies two M32 Phase-7 directives in sequence (one transaction each):

  DIR-20260508-002 (dir-003) — M32-A mapping:
    - UPDATE verse_context_group.context_description on group 1643
    - Clear is_anchor=1 on vr=1178 and vr=1179 in group 1643
      (pre-existing anchor pollution; only vr=1177 should remain anchor)
    - vr=82337 in group 364 already anchor=1, vr=1177 already anchor=1
      — no further action needed for those

  DIR-20260508-003 (dir-004) — M32-B mapping:
    - INSERT 2 new verse_context_group rows: 3578-A, 3578-B
    - REASSIGN 7 vc rows from group 1776 to 3578-A (4) / 3578-B (3)
    - SET is_anchor=1 on vr=132801 (Jer 31:21) in 3578-A
    - vr=132800 (Exo 7:23) already anchor=1; remains the 3578-B anchor
    - Clear all OTHER vc rows to is_anchor=0 in 3578-A / 3578-B
    - SOFT-RETIRE group 1776 (set delete_flagged=1) since it'll be empty

Each directive runs in its own transaction; if either fails, only that
one rolls back. Both report state at end.

Pre-flight verifies:
  - All target vr_ids exist for the right mti_ids
  - Group 1776 currently has exactly 7 verse_context rows for mti=3578
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

DIR_003_GROUP_1643_DESC = (
    "Term names a conscious inner awareness — moral complicity or "
    "cognitive recognition — that informs volitional response. The "
    "moral-complicity pole (shared inner co-knowing of one's "
    "participation in a morally charged act) is the primary conscience "
    "characteristic; the cognitive-recognition pole (becoming aware of "
    "a situation) represents the term's broader semantic range within "
    "the same faculty."
)

# (vr_id, mti_id, group_id, target_anchor)
DIR_003_VC_TARGETS = [
    (1177, 454, 1643, 1),   # Act 5:2 — anchor stays
    (1178, 454, 1643, 0),   # Act 12:12 — clear anchor
    (1179, 454, 1643, 0),   # Act 14:6 — clear anchor
    (82337, 2739, 364, 1),  # 1Cor 4:4 — anchor stays
]

# DIR-004 new groups
DIR_004_NEW_GROUPS = [
    ("3578-A", 3578,
     "The active exercise of the inner-attending faculty — deliberate "
     "inner attention directed at a matter, person, or one's own past, "
     "sustained with purpose, and productive of learning, repentance, "
     "or accurate testimony",
     "Split from group 1776 / 3578-001 (Phase 6 conglomerate review, "
     "2026-05-08)"),
    ("3578-B", 3578,
     "The failure, refusal, or social suppression of the inner-attending "
     "faculty — the characteristic named by its non-engagement: the "
     "person who does not take something to heart, whose attention has "
     "collapsed, or who is counselled not to attend",
     "Split from group 1776 / 3578-001 (Phase 6 conglomerate review, "
     "2026-05-08)"),
]

# (vr_id, target_group_code, target_anchor)
DIR_004_VC_TARGETS = [
    (132803, "3578-A", 0),  # Psa 13:2
    (132804, "3578-A", 0),  # Psa 48:13
    (132802, "3578-A", 0),  # Pro 24:32
    (132801, "3578-A", 1),  # Jer 31:21 — anchor
    (132800, "3578-B", 1),  # Exo 7:23 — anchor (already 1)
    (132798, "3578-B", 0),  # 1Sa 4:20
    (132799, "3578-B", 0),  # 2Sa 13:20
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_dir_003(conn) -> dict:
    """DIR-20260508-002 — M32-A mapping."""
    cur = conn.cursor()
    ts = now_iso()
    counts = {"group_desc_updated": 0, "anchors_cleared": 0,
              "anchors_kept": 0}

    # Pre-flight
    for vr_id, mti_id, group_id, _ in DIR_003_VC_TARGETS:
        r = cur.execute(
            "SELECT id, is_anchor FROM verse_context "
            " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vr_id, mti_id, group_id),
        ).fetchone()
        if r is None:
            raise RuntimeError(
                f"DIR-003 pre-flight: vc not found vr={vr_id} mti={mti_id} "
                f"grp={group_id}"
            )

    cur.execute("BEGIN")
    try:
        # Update group 1643 description
        rc = cur.execute(
            "UPDATE verse_context_group "
            "   SET context_description=? "
            " WHERE id=1643 AND COALESCE(delete_flagged,0)=0",
            (DIR_003_GROUP_1643_DESC,),
        ).rowcount
        if rc != 1:
            raise RuntimeError(f"DIR-003 group 1643 update rc={rc}")
        counts["group_desc_updated"] = 1

        # Set is_anchor for the 4 target vc rows
        for vr_id, mti_id, group_id, target_anchor in DIR_003_VC_TARGETS:
            cur.execute(
                "UPDATE verse_context "
                "   SET is_anchor=? "
                " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (target_anchor, vr_id, mti_id, group_id),
            )
            if target_anchor == 1:
                counts["anchors_kept"] += 1
            else:
                # If it was 1 and now 0, that's a clear
                counts["anchors_cleared"] += 1

        cur.execute("COMMIT")
        print("DIR-20260508-002 (dir-003 M32-A) COMMITTED")
        for k, v in counts.items():
            print(f"  {k}: {v}")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"DIR-003 rolled back: {e}")
        raise

    return counts


def run_dir_004(conn) -> dict:
    """DIR-20260508-003 — M32-B mapping (split + retire)."""
    cur = conn.cursor()
    ts = now_iso()
    counts = {"groups_inserted": 0, "vc_reassigned": 0,
              "anchors_set": 0, "old_group_retired": 0}

    # Pre-flight: group 1776 has exactly 7 active vc rows for mti=3578
    n = cur.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE group_id=1776 AND mti_term_id=3578 "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    if n != 7:
        raise RuntimeError(
            f"DIR-004 pre-flight: group 1776 mti=3578 has {n} active vc "
            f"rows, expected 7"
        )
    # Pre-flight: all 7 target vr_ids exist with mti=3578 in group 1776
    for vr_id, _, _ in DIR_004_VC_TARGETS:
        r = cur.execute(
            "SELECT id FROM verse_context "
            " WHERE verse_record_id=? AND mti_term_id=3578 "
            "   AND group_id=1776 AND COALESCE(delete_flagged,0)=0",
            (vr_id,),
        ).fetchone()
        if r is None:
            raise RuntimeError(
                f"DIR-004 pre-flight: vc vr={vr_id} mti=3578 grp=1776 "
                f"not found"
            )

    cur.execute("BEGIN")
    try:
        # 1. Insert 2 new groups
        new_group_ids: dict[str, int] = {}
        for code, mti_id, desc, notes in DIR_004_NEW_GROUPS:
            cur.execute(
                "INSERT INTO verse_context_group "
                "  (mti_term_id, group_code, context_description, notes, "
                "   delete_flagged) "
                "VALUES (?, ?, ?, ?, 0)",
                (mti_id, code, desc, notes),
            )
            new_group_ids[code] = cur.lastrowid
            counts["groups_inserted"] += 1
            print(f"  + verse_context_group INSERT {code} -> "
                  f"id={cur.lastrowid}")

        # 2. Reassign vc rows to new groups + set anchors
        for vr_id, target_code, target_anchor in DIR_004_VC_TARGETS:
            new_gid = new_group_ids[target_code]
            rc = cur.execute(
                "UPDATE verse_context "
                "   SET group_id=?, is_anchor=? "
                " WHERE verse_record_id=? AND mti_term_id=3578 "
                "   AND group_id=1776 AND COALESCE(delete_flagged,0)=0",
                (new_gid, target_anchor, vr_id),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"DIR-004 vc reassign vr={vr_id} expected 1, got {rc}"
                )
            counts["vc_reassigned"] += 1
            if target_anchor == 1:
                counts["anchors_set"] += 1

        # 3. Verify group 1776 is empty, then soft-retire it
        n = cur.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=1776 AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        if n != 0:
            raise RuntimeError(
                f"DIR-004 post-reassign: group 1776 still has {n} vc rows "
                f"(expected 0)"
            )
        rc = cur.execute(
            "UPDATE verse_context_group "
            "   SET delete_flagged=1, "
            "       notes=COALESCE(notes,'') || "
            "         ' | RETIRED 2026-05-08 (DIR-20260508-003): split into "
            "3578-A and 3578-B per Phase 6 conglomerate review.' "
            " WHERE id=1776",
        ).rowcount
        if rc != 1:
            raise RuntimeError(f"DIR-004 group 1776 retire rc={rc}")
        counts["old_group_retired"] = 1

        cur.execute("COMMIT")
        print("DIR-20260508-003 (dir-004 M32-B) COMMITTED")
        for k, v in counts.items():
            print(f"  {k}: {v}")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"DIR-004 rolled back: {e}")
        raise

    return counts


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Baselines
    cur = conn.cursor()
    n_sb_a = cur.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings "
        " WHERE term_id IN (454, 2739)"
    ).fetchone()[0]
    n_sb_b = cur.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings WHERE term_id=3578"
    ).fetchone()[0]
    print(f"BASELINE wa_session_b_findings (M32-A terms): {n_sb_a}")
    print(f"BASELINE wa_session_b_findings (M32-B term):  {n_sb_b}")
    print()

    run_dir_003(conn)
    print()
    run_dir_004(conn)

    # Post-state confirmations (read-only)
    print()
    print("=" * 60)
    print("  Post-state confirmations")
    print("=" * 60)

    print()
    print("--- DIR-003 Q1: M32-A anchor check ---")
    for r in conn.execute(
        "SELECT vc.verse_record_id AS vr, vc.mti_term_id AS mti, "
        "       vc.group_id, vc.is_anchor, vcg.group_code "
        "  FROM verse_context vc "
        "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        " WHERE vc.mti_term_id IN (454, 2739) "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        " ORDER BY vc.group_id, vc.is_anchor DESC, vc.verse_record_id"
    ):
        print(f"  vr={r['vr']:6d} mti={r['mti']} grp={r['group_id']} "
              f"({r['group_code']}) anchor={r['is_anchor']}")

    print()
    print("--- DIR-003 Q2: group 1643 description excerpt ---")
    r = conn.execute(
        "SELECT id, group_code, SUBSTR(context_description, 1, 120) AS d "
        "  FROM verse_context_group WHERE id IN (1643, 364)"
    ).fetchall()
    for row in r:
        print(f"  id={row['id']} ({row['group_code']}): {row['d']}...")

    print()
    print("--- DIR-004 Q1: new groups exist ---")
    for r in conn.execute(
        "SELECT id, group_code, mti_term_id, "
        "       SUBSTR(context_description, 1, 80) AS d "
        "  FROM verse_context_group "
        " WHERE group_code IN ('3578-A','3578-B') "
        "   AND COALESCE(delete_flagged,0)=0 "
        " ORDER BY group_code"
    ):
        print(f"  id={r['id']} {r['group_code']} mti={r['mti_term_id']}")
        print(f"    {r['d']}...")

    print()
    print("--- DIR-004 Q2: M32-B verse assignments + anchors ---")
    for r in conn.execute(
        "SELECT vc.verse_record_id AS vr, vc.group_id, vcg.group_code, "
        "       vc.is_anchor, b.short_code AS book, vr.chapter, vr.verse_num "
        "  FROM verse_context vc "
        "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        "  JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
        "  JOIN books b ON b.id=vr.book_id "
        " WHERE vc.mti_term_id=3578 "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        " ORDER BY vcg.group_code, vc.is_anchor DESC, vc.verse_record_id"
    ):
        print(f"  vr={r['vr']:6d} {r['book']} {r['chapter']:>3}:{r['verse_num']:<3} "
              f"grp={r['group_id']} ({r['group_code']}) anchor={r['is_anchor']}")

    print()
    print("--- DIR-004 Q3: old group 1776 active rowcount ---")
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE group_id=1776 AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  active vc rows in group 1776: {n} (expected 0)")
    r = conn.execute(
        "SELECT id, group_code, COALESCE(delete_flagged,0) AS df, "
        "       SUBSTR(notes, 1, 120) AS notes "
        "  FROM verse_context_group WHERE id=1776"
    ).fetchone()
    print(f"  group 1776 status: df={r['df']} (1=retired)")
    print(f"  notes: {r['notes']}")

    print()
    print("--- Q3/Q4: wa_session_b_findings unchanged ---")
    n_sb_a_post = conn.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings "
        " WHERE term_id IN (454, 2739)"
    ).fetchone()[0]
    n_sb_b_post = conn.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings WHERE term_id=3578"
    ).fetchone()[0]
    print(f"  M32-A terms: pre={n_sb_a} post={n_sb_a_post} "
          f"({'unchanged' if n_sb_a==n_sb_a_post else 'CHANGED!'})")
    print(f"  M32-B term:  pre={n_sb_b} post={n_sb_b_post} "
          f"({'unchanged' if n_sb_b==n_sb_b_post else 'CHANGED!'})")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
