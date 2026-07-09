"""_apply_m15_dir013_m15c_vcg_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M15-013: M15-C VCG cleanup.

Operations (single transaction, foreign_keys=ON):

  Phase 0 — Backup
  Phase 1 — Create 12 new VCGs (M15-C-VCG01..12) + vcg_term links
  Phase 2 — Assign 572 verses + mark 12 anchors
  Phase 3 — Apply set-aside to 4 verses (also moves them to M15-C
             if they sit elsewhere in DB)

Source: Sessions/Session_Clusters/M15/m15-vcg-db-staging-M15C-v1-20260511.json
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
STAGING_PATH = os.path.join(
    "Sessions", "Session_Clusters", "M15",
    "m15-vcg-db-staging-M15C-v1-20260511.json",
)
DIRECTIVE_ID = "DIR-20260511-M15-013"
SUBGROUP_CODE = "M15-C"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def main() -> int:
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

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply ({SUBGROUP_CODE} VCG cleanup)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    with open(STAGING_PATH, "r", encoding="utf-8") as f:
        staging = json.load(f)

    vcg_blocks = staging["vcg_creations"]
    setaside_block = staging["setasides"]

    print(f"Staging summary:")
    print(f"  VCGs to create: {len(vcg_blocks)}")
    print(f"  Verses to assign to VCGs: {sum(b['verse_count'] for b in vcg_blocks)}")
    print(f"  Verses to set aside: {setaside_block['verse_count']}")
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # ---------- Pre-flight ----------
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True
    sg_ids = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        " WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0"
    )}
    SG_ID = sg_ids.get(SUBGROUP_CODE)
    if not SG_ID:
        print(f"  [ERR] missing {SUBGROUP_CODE} sub-group")
        ok = False
    else:
        print(f"  [ok] {SUBGROUP_CODE} sub-group id={SG_ID}")

    new_codes = [b["code"] for b in vcg_blocks]
    placeholders = ",".join("?" * len(new_codes))
    existing = list(conn.execute(
        f"SELECT group_code FROM verse_context_group "
        f" WHERE group_code IN ({placeholders}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        new_codes,
    ))
    if existing:
        print(f"  [ERR] VCG codes already exist: "
              f"{[r['group_code'] for r in existing]}")
        ok = False
    else:
        print(f"  [ok] none of the {len(new_codes)} new VCG codes already exist")

    all_targets = []
    for b in vcg_blocks:
        for v in b["verses"]:
            all_targets.append(v["vr_id"])
    for v in setaside_block["verses"]:
        all_targets.append(v["vr_id"])
    missing_vc = []
    for vr_id in all_targets:
        r = conn.execute(
            "SELECT id FROM verse_context "
            " WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0",
            (vr_id,),
        ).fetchone()
        if not r:
            missing_vc.append(vr_id)
    if missing_vc:
        print(f"  [ERR] {len(missing_vc)} vr_ids have no active vc row; "
              f"sample: {missing_vc[:10]}")
        ok = False
    else:
        print(f"  [ok] all {len(all_targets)} targets have an active vc row")

    for b in vcg_blocks:
        a = b.get("anchor_proposed")
        if not a:
            print(f"  [ERR] VCG {b['code']} has no anchor_proposed")
            ok = False
    print(f"  [ok] anchor presence checked")

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup(f"m15_dir013_{SUBGROUP_CODE.lower().replace('-','_')}_vcg")
        print(f"Backup: {b}")
        print()

    # ---------- Apply ----------
    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 1
        print("Phase 1 — Create VCGs + vcg_term links")
        print("-" * 72)
        new_vcg_id_by_code: dict[str, int] = {}
        vcg_term_inserts = 0
        for block in vcg_blocks:
            rowid = cur.execute(
                "INSERT INTO verse_context_group "
                "  (group_code, context_description, delete_flagged, "
                "   vertical_pass_flag) "
                "VALUES (?, ?, 0, 0)",
                (block["code"], block["context_description"]),
            ).lastrowid
            new_vcg_id_by_code[block["code"]] = rowid
            for mti_id in block["mti_term_ids"]:
                cur.execute(
                    "INSERT INTO vcg_term "
                    "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
                    "   created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (rowid, mti_id,
                     f"{DIRECTIVE_ID}: {SUBGROUP_CODE} VCG cleanup", ts, ts),
                )
                vcg_term_inserts += 1
        counts["phase1_vcgs_created"] = len(new_vcg_id_by_code)
        counts["phase1_vcg_term_inserts"] = vcg_term_inserts
        print(f"  Created {len(new_vcg_id_by_code)} VCGs, "
              f"{vcg_term_inserts} vcg_term rows")

        # Phase 2
        print()
        print("Phase 2 — Assign verses + mark anchors")
        print("-" * 72)
        anchor_vr_ids = {b["anchor_proposed"]["vr_id"]
                         for b in vcg_blocks if b.get("anchor_proposed")}
        ph2 = 0
        ph2_moved = 0
        for block in vcg_blocks:
            vcg_id = new_vcg_id_by_code[block["code"]]
            verse_vr_ids = {v["vr_id"] for v in block["verses"]}
            anchor_vr = block.get("anchor_proposed", {}).get("vr_id")
            if anchor_vr is not None and anchor_vr not in verse_vr_ids:
                verse_vr_ids.add(anchor_vr)
            for vr_id in verse_vr_ids:
                is_anchor = 1 if vr_id in anchor_vr_ids else 0
                # Track moves (pre-state sg != SG_ID)
                pre = cur.execute(
                    "SELECT cluster_subgroup_id FROM verse_context "
                    " WHERE verse_record_id=? "
                    "   AND COALESCE(delete_flagged,0)=0",
                    (vr_id,),
                ).fetchone()
                if pre and pre[0] != SG_ID:
                    ph2_moved += 1
                rc = cur.execute(
                    "UPDATE verse_context "
                    "   SET group_id = ?, "
                    "       cluster_subgroup_id = ?, "
                    "       is_relevant = 1, "
                    "       is_anchor = ?, "
                    "       set_aside_reason = NULL "
                    " WHERE verse_record_id = ? "
                    "   AND COALESCE(delete_flagged,0)=0",
                    (vcg_id, SG_ID, is_anchor, vr_id),
                ).rowcount
                ph2 += rc
        counts["phase2_verses_assigned"] = ph2
        counts["phase2_moved_from_other_sg"] = ph2_moved
        print(f"  Assigned {ph2} verse_context rows, "
              f"{len(anchor_vr_ids)} anchors marked"
              + (f", {ph2_moved} moved into {SUBGROUP_CODE} from other sg"
                 if ph2_moved else ""))

        # Phase 3 — Set-asides (with sub-group move)
        print()
        print(f"Phase 3 — Apply set-aside (and move to {SUBGROUP_CODE} if elsewhere)")
        print("-" * 72)
        ph3 = 0
        ph3_moved = 0
        for v in setaside_block["verses"]:
            pre = cur.execute(
                "SELECT cluster_subgroup_id FROM verse_context "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (v["vr_id"],),
            ).fetchone()
            if pre and pre[0] != SG_ID:
                ph3_moved += 1
            rc = cur.execute(
                "UPDATE verse_context "
                "   SET group_id = NULL, "
                "       cluster_subgroup_id = ?, "
                "       is_relevant = 0, "
                "       is_anchor = 0, "
                "       set_aside_reason = ? "
                " WHERE verse_record_id = ? "
                "   AND COALESCE(delete_flagged,0)=0",
                (SG_ID, setaside_block["reason_code"], v["vr_id"]),
            ).rowcount
            ph3 += rc
        counts["phase3_setasides"] = ph3
        counts["phase3_moved_from_other_sg"] = ph3_moved
        print(f"  Set aside {ph3} verse_context rows"
              + (f" ({ph3_moved} moved into {SUBGROUP_CODE} from other sg)"
                 if ph3_moved else ""))

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print()
        print("FK check: ok")

        # Verification
        print()
        print("VERIFICATION")
        print("-" * 72)
        for code, vcg_id in sorted(new_vcg_id_by_code.items()):
            n = conn.execute(
                "SELECT COUNT(*) FROM verse_context "
                " WHERE group_id=? AND COALESCE(delete_flagged,0)=0",
                (vcg_id,),
            ).fetchone()[0]
            a = conn.execute(
                "SELECT COUNT(*) FROM verse_context "
                " WHERE group_id=? AND is_anchor=1 "
                "   AND COALESCE(delete_flagged,0)=0",
                (vcg_id,),
            ).fetchone()[0]
            tn = conn.execute(
                "SELECT COUNT(*) FROM vcg_term "
                " WHERE vcg_id=? AND COALESCE(delete_flagged,0)=0",
                (vcg_id,),
            ).fetchone()[0]
            print(f"  {code:14s} vcg_id={vcg_id:>6d} verses={n:>3d} "
                  f"anchors={a} terms={tn}")
        n_sa = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
             WHERE mt.cluster_code='M15'
               AND vc.cluster_subgroup_id=?
               AND vc.set_aside_reason=?
               AND COALESCE(vc.delete_flagged,0)=0
        """, (SG_ID, setaside_block["reason_code"])).fetchone()[0]
        print(f"  {SUBGROUP_CODE} set-asides (post): {n_sa}")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print()
            print("DRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print()
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
