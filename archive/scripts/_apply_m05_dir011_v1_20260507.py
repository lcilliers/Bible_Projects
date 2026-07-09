"""_apply_m05_dir011_v1_20260507.py — DB-modifying.

Applies DIR-20260507-M05-011 — follow-up resolution for the 4 outstanding
items from DIR-004..010 + the 2 residual-verse cleanups:

  Op 1: Anchor for Group 1542 (agape mti=562) -> Rom 5:8 (vr=4943)
  Op 2: Anchor for Group 1271 (an.vah mti=188) -> Psa 18:35 (vr=3741)
  Op 3: Group 3602 (anoche mti=7502) -> no anchor; report non-7502 rows
  Op 4: Group 1583 split -> create 1583-a + 1583-b; route 115 vr_ids
  Op 5: Group 629 residuals (5 verses) -> 629-b (gid=3599)
  Op 6: Group 604 residual (vr=59217) -> 604-a (gid=3600)

Transaction-safe: single transaction, all-or-nothing.
Idempotent: re-run safe (UPDATE-then-INSERT pattern; existing groups + verses
re-checked).
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIR_ID = "DIR-20260507-M05-011"

# Op 1 + Op 2 anchor targets: (group_id, vr_id, mti_id, ref_for_log)
OP12_ANCHORS = [
    (1542, 4943, 562, "Rom 5:8"),
    (1271, 3741, 188, "Psa 18:35"),
]

# Op 4: Group 1583 split routing — (vr_id, target_subkey)
# subkey 'a' -> 1583-a (group_code 536-001-a)
# subkey 'b' -> 1583-b (group_code 536-001-b)
SPLIT_1583 = [
    (3875, "b"), (3878, "b"), (3879, "b"), (3880, "b"), (3882, "b"),
    (3883, "b"), (3886, "b"), (3887, "a"), (3888, "a"), (3889, "a"),
    (3891, "a"), (3892, "b"), (3893, "a"), (3894, "a"), (3895, "b"),
    (3906, "b"), (3908, "b"), (3913, "b"), (3915, "b"), (3917, "b"),
    (3918, "a"), (3920, "a"), (3921, "a"), (3922, "b"), (3924, "b"),
    (3925, "a"), (3926, "a"), (3927, "b"), (3928, "a"), (3929, "a"),
    (3930, "a"), (3934, "a"), (3935, "b"), (3936, "b"), (3937, "a"),
    (3938, "a"), (3939, "a"), (3941, "b"), (3945, "b"), (3946, "a"),
    (3947, "a"), (3948, "b"), (3949, "a"), (3950, "b"), (3951, "b"),
    (3952, "b"), (3953, "a"), (3954, "a"), (3955, "b"), (3956, "a"),
    (3957, "a"), (3958, "b"), (3959, "b"), (3960, "b"), (3961, "a"),
    (3962, "a"), (3963, "a"), (3964, "b"), (3965, "a"), (3966, "a"),
    (3967, "b"), (3968, "b"), (3969, "a"), (3970, "a"), (3971, "b"),
    (3972, "a"), (3973, "b"), (3974, "a"), (3975, "a"), (3976, "b"),
    (3977, "a"), (3978, "b"), (3979, "a"), (3980, "a"), (3981, "b"),
    (3982, "a"), (3983, "a"), (3984, "b"), (3985, "b"), (3986, "b"),
    (3987, "a"), (3988, "b"), (3989, "a"), (3990, "a"), (3991, "b"),
    (3992, "a"), (3993, "a"), (3994, "a"), (3995, "a"), (3996, "a"),
    (3997, "b"), (3998, "b"), (3999, "b"), (4000, "b"), (4001, "b"),
    (4002, "a"), (4003, "b"), (4084, "a"), (4086, "b"), (4087, "a"),
    (4088, "b"), (4090, "b"), (4092, "a"), (4094, "b"), (4095, "a"),
    (4096, "a"), (4097, "a"), (4098, "b"), (4099, "b"), (4100, "a"),
    (4101, "b"), (4107, "a"), (4109, "a"), (4111, "a"), (4112, "b"),
]

# 1583-a / 1583-b group definitions
SPLIT_1583_DEFS = {
    "a": {
        "code": "536-001-a",
        "mti": 536,
        "description": (
            "God's chesed as his eternal declared attribute — the "
            "covenantal faithfulness that never ceases, is proclaimed in "
            "the divine self-disclosure formula (Exo 34:6), and is the "
            "ground of Israel's hope and petition even in desolation "
            "(Lam 3:22)"
        ),
        "anchor_vr": 4097,  # Lam 3:22
    },
    "b": {
        "code": "536-001-b",
        "mti": 536,
        "description": (
            "God's chesed enacted in specific historical acts toward "
            "individuals and toward Israel — the covenantal faithfulness "
            "made concrete in protection, provision, deliverance, and "
            "sustained presence (Exo 15:13, Gen 19:19 type)"
        ),
        "anchor_vr": 3886,  # Exo 15:13
    },
}

# Op 5: Group 629 residuals -> 629-b (gid 3599)
OP5_VRS_TO_629B = [1569, 59047, 59054, 59040, 59055]

# Op 6: Group 604 residual -> 604-a (gid 3600)
OP6_VR_TO_604A = 59217


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m05_dir011.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ---- Pre-flight: confirm 629-b and 604-a group ids
    gid_629b = conn.execute(
        "SELECT id FROM verse_context_group "
        " WHERE group_code='487-001-b' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    gid_604a = conn.execute(
        "SELECT id FROM verse_context_group "
        " WHERE group_code='510-003-a' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    if not gid_629b or not gid_604a:
        print("[err] missing group_codes 487-001-b and/or 510-003-a")
        return 2
    gid_629b = gid_629b["id"]
    gid_604a = gid_604a["id"]
    print(f"Pre-flight: 629-b = gid {gid_629b}; 604-a = gid {gid_604a}")

    # ---- Pre-flight: anchors targets exist
    for gid, vr, mti, ref in OP12_ANCHORS:
        r = conn.execute(
            "SELECT id FROM verse_context "
            " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vr, mti, gid),
        ).fetchone()
        if not r:
            print(f"[warn] no row for vr={vr} mti={mti} group={gid} ({ref}) "
                  f"— will INSERT during apply")
        else:
            print(f"  Op12: vr={vr} mti={mti} group={gid} ({ref}) -> "
                  f"existing vc_id={r['id']}")

    # ---- Pre-flight: 1583 verses present in original group
    placeholders = ",".join("?" * len(SPLIT_1583))
    found_1583 = {
        r["verse_record_id"] for r in conn.execute(
            f"SELECT verse_record_id FROM verse_context "
            f" WHERE group_id=1583 AND verse_record_id IN ({placeholders}) "
            f"   AND COALESCE(delete_flagged,0)=0",
            [vr for vr, _ in SPLIT_1583],
        )
    }
    expected_1583 = {vr for vr, _ in SPLIT_1583}
    missing_1583 = expected_1583 - found_1583
    extra_1583 = found_1583 - expected_1583
    print(f"  Op4: 1583 verses to route: expected {len(expected_1583)}, "
          f"found {len(found_1583)}, missing {len(missing_1583)}")

    # Are there vr_ids in group 1583 NOT in our routing table?
    extra_in_db = list(conn.execute(
        f"SELECT verse_record_id FROM verse_context "
        f" WHERE group_id=1583 AND COALESCE(delete_flagged,0)=0 "
        f"   AND verse_record_id NOT IN ({placeholders})",
        [vr for vr, _ in SPLIT_1583],
    ))
    if extra_in_db:
        print(f"  Op4 WARNING: {len(extra_in_db)} vr_ids in DB group 1583 "
              f"NOT in routing table; will be left in 1583 for AI review")

    n_changes = {
        "op1_anchors": 0, "op2_anchors": 0,
        "op4_groups_created": 0, "op4_routed": 0, "op4_anchor_set": 0,
        "op5_routed": 0, "op6_routed": 0,
    }
    op3_report = []

    try:
        conn.execute("BEGIN")

        # ============ Op 1 + Op 2: anchors for 1542 + 1271 ============
        for gid, vr, mti, ref in OP12_ANCHORS:
            # Clear existing anchor on this group
            conn.execute(
                "UPDATE verse_context SET is_anchor=0 "
                " WHERE group_id=? AND is_anchor=1 "
                "   AND COALESCE(delete_flagged,0)=0",
                (gid,),
            )
            # Set anchor on the target row (UPDATE if exists, INSERT if not)
            row = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr, mti, gid),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE verse_context SET is_anchor=1 WHERE id=?",
                    (row["id"],),
                )
            else:
                conn.execute(
                    "INSERT INTO verse_context "
                    "  (verse_record_id, mti_term_id, group_id, is_anchor, "
                    "   is_relevant, is_related, notes, delete_flagged, "
                    "   set_aside_reason) "
                    "VALUES (?, ?, ?, 1, 1, 0, ?, 0, NULL)",
                    (vr, mti, gid, f"{DIR_ID} anchor ({ref})"),
                )
            if gid == 1542:
                n_changes["op1_anchors"] += 1
            else:
                n_changes["op2_anchors"] += 1

        # ============ Op 3: report non-7502 rows in group 3602 ============
        for r in conn.execute(
            "SELECT id, verse_record_id, mti_term_id "
            "  FROM verse_context "
            " WHERE group_id=3602 AND COALESCE(delete_flagged,0)=0"
        ):
            if r["mti_term_id"] != 7502:
                op3_report.append({
                    "vc_id": r["id"],
                    "vr_id": r["verse_record_id"],
                    "mti_term_id": r["mti_term_id"],
                })

        # ============ Op 4: 1583 split — create groups + route ============
        gid_1583_a = None
        gid_1583_b = None
        for sub in ("a", "b"):
            d = SPLIT_1583_DEFS[sub]
            existing = conn.execute(
                "SELECT id FROM verse_context_group "
                " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
                (d["code"],),
            ).fetchone()
            if existing:
                conn.execute(
                    "UPDATE verse_context_group "
                    "   SET context_description=? "
                    " WHERE id=?",
                    (d["description"], existing["id"]),
                )
                new_gid = existing["id"]
            else:
                cur = conn.execute(
                    "INSERT INTO verse_context_group "
                    "  (mti_term_id, group_code, context_description, "
                    "   notes, delete_flagged, vertical_pass_flag) "
                    "VALUES (?, ?, ?, ?, 0, 0)",
                    (d["mti"], d["code"], d["description"],
                     f"Created by {DIR_ID}"),
                )
                new_gid = cur.lastrowid
                n_changes["op4_groups_created"] += 1
            if sub == "a":
                gid_1583_a = new_gid
            else:
                gid_1583_b = new_gid

        # Route 115 vr_ids from 1583 -> 1583-a or 1583-b
        for vr, sub in SPLIT_1583:
            target_gid = gid_1583_a if sub == "a" else gid_1583_b
            # Find the row in original 1583 for this vr (mti=536 implied)
            row = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=536 "
                "   AND group_id=1583 "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE verse_context SET group_id=? WHERE id=?",
                    (target_gid, row["id"]),
                )
                n_changes["op4_routed"] += 1
            else:
                # Maybe already routed (idempotent re-run); check target
                already = conn.execute(
                    "SELECT id FROM verse_context "
                    " WHERE verse_record_id=? AND mti_term_id=536 "
                    "   AND group_id=? AND COALESCE(delete_flagged,0)=0",
                    (vr, target_gid),
                ).fetchone()
                if not already:
                    # Truly missing — INSERT
                    conn.execute(
                        "INSERT INTO verse_context "
                        "  (verse_record_id, mti_term_id, group_id, "
                        "   is_anchor, is_relevant, is_related, notes, "
                        "   delete_flagged, set_aside_reason) "
                        "VALUES (?, 536, ?, 0, 1, 0, ?, 0, NULL)",
                        (vr, target_gid,
                         f"{DIR_ID} 1583 split route to 1583-{sub}"),
                    )
                    n_changes["op4_routed"] += 1

        # Set anchors on 1583-a and 1583-b
        for sub in ("a", "b"):
            d = SPLIT_1583_DEFS[sub]
            target_gid = gid_1583_a if sub == "a" else gid_1583_b
            # Clear existing
            conn.execute(
                "UPDATE verse_context SET is_anchor=0 "
                " WHERE group_id=? AND is_anchor=1 "
                "   AND COALESCE(delete_flagged,0)=0",
                (target_gid,),
            )
            # Set anchor on the named vr
            row = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=? AND group_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (d["anchor_vr"], d["mti"], target_gid),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE verse_context SET is_anchor=1 WHERE id=?",
                    (row["id"],),
                )
                n_changes["op4_anchor_set"] += 1

        # ============ Op 5: 629 residuals -> 629-b ============
        for vr in OP5_VRS_TO_629B:
            row = conn.execute(
                "SELECT id FROM verse_context "
                " WHERE verse_record_id=? AND mti_term_id=487 "
                "   AND group_id=629 AND COALESCE(delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE verse_context SET group_id=? WHERE id=?",
                    (gid_629b, row["id"]),
                )
                n_changes["op5_routed"] += 1

        # ============ Op 6: 604 residual -> 604-a ============
        row = conn.execute(
            "SELECT id FROM verse_context "
            " WHERE verse_record_id=? AND mti_term_id=510 "
            "   AND group_id=604 AND COALESCE(delete_flagged,0)=0",
            (OP6_VR_TO_604A,),
        ).fetchone()
        if row:
            conn.execute(
                "UPDATE verse_context SET group_id=? WHERE id=?",
                (gid_604a, row["id"]),
            )
            n_changes["op6_routed"] += 1

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print("APPLY SUMMARY")
    print("-" * 60)
    for k, v in n_changes.items():
        print(f"  {k:25s} {v}")

    if op3_report:
        print()
        print(f"Op 3 report: {len(op3_report)} non-7502 rows in group 3602:")
        for r in op3_report:
            print(f"  vc={r['vc_id']:6d} vr={r['vr_id']:6d} "
                  f"mti={r['mti_term_id']}")
    else:
        print()
        print("Op 3 report: 0 non-7502 rows in group 3602 (clean)")

    # ---- Verification queries
    print()
    print("VERIFICATION")
    print("-" * 60)

    # Anchors for 1542, 1271
    for gid, vr, mti, ref in OP12_ANCHORS:
        r = conn.execute(
            "SELECT vr_id, verse_record_id, is_anchor "
            "  FROM verse_context "
            " WHERE group_id=? AND is_anchor=1 "
            "   AND COALESCE(delete_flagged,0)=0",
            (gid,),
        ).fetchone() if False else conn.execute(
            "SELECT verse_record_id, is_anchor "
            "  FROM verse_context "
            " WHERE group_id=? AND is_anchor=1 "
            "   AND COALESCE(delete_flagged,0)=0",
            (gid,),
        ).fetchone()
        if r and r["verse_record_id"] == vr:
            print(f"  group {gid} anchor: vr={vr} ({ref}) OK")
        else:
            print(f"  group {gid} anchor: NOT SET ({ref})")

    # 1583 split
    for code in ("536-001-a", "536-001-b"):
        r = conn.execute(
            "SELECT vcg.id, COUNT(vc.id) AS n, SUM(vc.is_anchor) AS anc "
            "  FROM verse_context_group vcg "
            "  LEFT JOIN verse_context vc ON vc.group_id=vcg.id "
            "       AND COALESCE(vc.delete_flagged,0)=0 "
            " WHERE vcg.group_code=? AND COALESCE(vcg.delete_flagged,0)=0 "
            " GROUP BY vcg.id",
            (code,),
        ).fetchone()
        if r:
            print(f"  {code} (gid={r['id']}): {r['n']} verses, "
                  f"{r['anc']} anchor")

    # Original 1583, 629, 604 row counts (should be ~0)
    for gid, label in ((1583, "1583 (orig)"),
                       (629, "629 (orig)"),
                       (604, "604 (orig)")):
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND COALESCE(delete_flagged,0)=0",
            (gid,),
        ).fetchone()[0]
        print(f"  {label} residual: {n}")

    # M05 anchor coverage check
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
    """))
    print()
    print(f"  M05 groups with non-1 anchor: {len(bad)}")
    for r in bad[:15]:
        print(f"    gid={r['gid']:5d} code={r['group_code']:14s} "
              f"anc={r['anc']} verses={r['verses']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
