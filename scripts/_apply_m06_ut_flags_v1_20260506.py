"""_apply_m06_ut_flags_v1_20260506.py — DB-modifying.

Apply researcher's directives on the §Flags + Borderlines from
WA-M06-UT-verse-review-v1-2026-05-05.md.

Researcher's directives (reading the IDE response 2026-05-06):

  1. H8130 sa.ne (Exo 1:10, Deu 30:7, Psa 69:14, Psa 106:10) — KEEP. New
     group: "those that hate me — my enemies — hate coming from others".
     Reverse the set-asides applied yesterday.

  2. H2778A cha.raph (Judg 5:18) — KEEP. Use existing group 2156
     ("taunting as expression of contempt, defiance, or hostility"). The
     reviewer's "act of defiance" framing fits group 2156.

  3. H8263 she.qets (Lev 11:11, Lev 11:13) — KEEP both borderlines. New
     group: "reaction or response to hate / commanded revulsion".

  4. H0887 ba.ash (Gen 34:30, 1Sa 13:4, Psa 38:5) — KEEP all borderlines.
     Use existing group 49 ("stench-metaphor expressing how wickedness and
     folly produce odium / disposition").

  5. H7850 sho.tet (Jos 23:13) — KEEP. New group: "illustrating impact of
     enemy — whip / scourge metaphor for hostile domination; also used for
     oar (something that stirs)". Reverse the set-aside.

The 5 borderlines covered above are the ones the reviewer flagged
("borderlines you highlighted above — keep all").

Idempotent: each verse_context row update is keyed by
(verse_record_id, mti_term_id) and skipped if already in the target state.
Backed up first.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_flags.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main() -> int:
    print(f"DB: {DB_PATH}")
    print(f"Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ---- Verse → vr_id map (resolved earlier; hard-coded here for clarity)
    # Each entry: (vr_id, mti_term_id, reference, label)
    # Decisions:
    #   action = ("revise" if previously set-aside row exists, else "insert")
    #   group_id = target group (existing or new)

    flag1_h8130 = [  # mti=550
        (4383, 550, "Exo 1:10"),
        (4405, 550, "Deu 30:7"),
        (4446, 550, "Psa 69:14"),
        (4454, 550, "Psa 106:10"),
    ]
    flag2_h2778a = (6728, 339, "Judg 5:18")
    flag3_h8263 = [  # mti=247 (new group for these)
        (57902, 247, "Lev 11:11"),
        (57903, 247, "Lev 11:13"),
    ]
    flag4_h0887 = [  # mti=90, use existing group 49
        (184, 90, "Gen 34:30"),
        (191, 90, "1Sa 13:4"),
        (196, 90, "Psa 38:5"),
    ]
    flag5_h7850 = (168602, 5519, "Jos 23:13")

    try:
        conn.execute("BEGIN")

        # ---- Step 1: Create new verse_context_groups
        new_groups = []

        # New group for H8130 (mti=550): hatred received from others
        cur = conn.execute("""
            INSERT INTO verse_context_group
              (mti_term_id, group_code, context_description, notes,
               delete_flagged, vertical_pass_flag)
            VALUES (?, ?, ?, ?, 0, 0)
        """, (
            550,
            "550-002",
            "Term names hatred received from others — those who hate me, "
            "my enemies — hate as an inner-being disposition coming from "
            "another person, directed at the speaker / object",
            "Created from M06 UT review v1 flag 1 (2026-05-06)",
        ))
        gid_h8130 = cur.lastrowid
        new_groups.append(("H8130", "550-002", gid_h8130))

        # New group for H8263 (mti=247): commanded inner reaction
        cur = conn.execute("""
            INSERT INTO verse_context_group
              (mti_term_id, group_code, context_description, notes,
               delete_flagged, vertical_pass_flag)
            VALUES (?, ?, ?, ?, 0, 0)
        """, (
            247,
            "247-002",
            "Term names the commanded inner reaction or response of "
            "detestation — the worshipper's required inner-being orientation "
            "of revulsion toward objects deemed unclean / hateful",
            "Created from M06 UT review v1 flag 3 (2026-05-06)",
        ))
        gid_h8263 = cur.lastrowid
        new_groups.append(("H8263", "247-002", gid_h8263))

        # New group for H7850 (mti=5519): scourge metaphor
        cur = conn.execute("""
            INSERT INTO verse_context_group
              (mti_term_id, group_code, context_description, notes,
               delete_flagged, vertical_pass_flag)
            VALUES (?, ?, ?, ?, 0, 0)
        """, (
            5519,
            "5519-001",
            "Term names the illustrating impact of an enemy — the whip / "
            "scourge metaphor for hostile domination; the term is also used "
            "for an oar — something that stirs",
            "Created from M06 UT review v1 flag 5 (2026-05-06)",
        ))
        gid_h7850 = cur.lastrowid
        new_groups.append(("H7850", "5519-001", gid_h7850))

        print(f"Created {len(new_groups)} new verse_context_group rows:")
        for nm, code, gid in new_groups:
            print(f"  {nm} group_code={code}, group_id={gid}")
        print()

        # ---- Step 2: Apply per-verse decisions
        results = []

        def apply_decision(vr_id, mti_id, ref, group_id, note):
            """Insert OR update the verse_context row."""
            existing = conn.execute("""
                SELECT id, group_id, is_relevant, set_aside_reason
                  FROM verse_context
                 WHERE verse_record_id = ? AND mti_term_id = ?
            """, (vr_id, mti_id)).fetchone()
            if existing:
                conn.execute("""
                    UPDATE verse_context
                       SET group_id = ?,
                           is_relevant = 1,
                           is_anchor = 0,
                           is_related = 0,
                           set_aside_reason = NULL,
                           notes = ?,
                           analysis_note = ?,
                           delete_flagged = 0
                     WHERE id = ?
                """, (
                    group_id,
                    "M06 UT flags v1 (2026-05-06): " + note,
                    "Source: WA-M06-UT-verse-review-v1-2026-05-05 §Flags response",
                    existing["id"],
                ))
                return ("UPDATED", existing["id"])
            else:
                cur = conn.execute("""
                    INSERT INTO verse_context
                      (verse_record_id, mti_term_id, group_id,
                       is_anchor, is_relevant, is_related, notes,
                       delete_flagged, set_aside_reason, analysis_note)
                    VALUES (?, ?, ?, 0, 1, 0, ?, 0, NULL, ?)
                """, (
                    vr_id, mti_id, group_id,
                    "M06 UT flags v1 (2026-05-06): " + note,
                    "Source: WA-M06-UT-verse-review-v1-2026-05-05 §Flags response",
                ))
                return ("INSERTED", cur.lastrowid)

        # Flag 1: H8130 — 4 verses → new group
        for vr_id, mti_id, ref in flag1_h8130:
            outcome, vc_id = apply_decision(
                vr_id, mti_id, ref, gid_h8130,
                "flag 1 — hatred received from others / my enemies"
            )
            results.append((ref, "H8130", outcome, vc_id, gid_h8130))

        # Flag 2: H2778A Judg 5:18 → existing group 2156
        outcome, vc_id = apply_decision(
            *flag2_h2778a, 2156,
            "flag 2 — taunting as act of defiance"
        )
        results.append((flag2_h2778a[2], "H2778A", outcome, vc_id, 2156))

        # Flag 3: H8263 — 2 borderlines → new group
        for vr_id, mti_id, ref in flag3_h8263:
            outcome, vc_id = apply_decision(
                vr_id, mti_id, ref, gid_h8263,
                "flag 3 — commanded inner reaction / response of detestation"
            )
            results.append((ref, "H8263", outcome, vc_id, gid_h8263))

        # Flag 4: H0887 — 3 borderlines → existing group 49
        for vr_id, mti_id, ref in flag4_h0887:
            outcome, vc_id = apply_decision(
                vr_id, mti_id, ref, 49,
                "flag 4 — metaphor for the disposition (group 49)"
            )
            results.append((ref, "H0887", outcome, vc_id, 49))

        # Flag 5: H7850 Jos 23:13 → new group
        outcome, vc_id = apply_decision(
            *flag5_h7850, gid_h7850,
            "flag 5 — illustrating impact of enemy / whip / oar metaphor"
        )
        results.append((flag5_h7850[2], "H7850", outcome, vc_id, gid_h7850))

        conn.execute("COMMIT")
        print("Verse-context updates applied:")
        for ref, sn, outcome, vc_id, gid in results:
            print(f"  {sn:8s}  {ref:10s}  {outcome}  vc_id={vc_id}  group_id={gid}")
        print(f"\nTotal: {len(results)} rows")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n✗ ERROR — rolled back: {e}")
        raise

    # ---- Verification
    print("\nVerification — current state of all 11 flag/borderline verses:")
    all_rows = (
        flag1_h8130
        + [flag2_h2778a]
        + flag3_h8263
        + flag4_h0887
        + [flag5_h7850]
    )
    for vr_id, mti_id, ref in all_rows:
        rec = conn.execute("""
            SELECT group_id, is_relevant, set_aside_reason
              FROM verse_context
             WHERE verse_record_id = ? AND mti_term_id = ?
               AND COALESCE(delete_flagged,0) = 0
        """, (vr_id, mti_id)).fetchone()
        if not rec:
            status = "UT (no row!)"
        elif (rec["group_id"] and rec["group_id"] > 0
              and rec["is_relevant"] == 1):
            status = f"G group_id={rec['group_id']}"
        elif rec["set_aside_reason"]:
            status = f"SA — {rec['set_aside_reason'][:40]}"
        else:
            status = "other"
        print(f"  {ref:12s}  {status}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
