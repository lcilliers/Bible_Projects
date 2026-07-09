"""_apply_m15_subgroup_vcg_generic_v1_20260511.py — DB-modifying.

Generic apply script for an M15 sub-group VCG cleanup.

Takes:
  --staging PATH  staging JSON for the sub-group
  --directive-id  e.g. DIR-20260511-M15-014
  --dry-run | --live

Operations (single transaction):
  Phase 0  Backup (live mode)
  Phase 0b If staging.metadata.needs_subgroup_creation == true:
            INSERT a new cluster_subgroup row using
            staging.metadata.subgroup_to_create
  Phase 1  Create N VCGs (verse_context_group) + vcg_term links per VCG
  Phase 2  Assign verses + mark anchors (sets cluster_subgroup_id to SG)
  Phase 3  Apply set-aside (also sets cluster_subgroup_id to SG)

Used for DIR-014..DIR-019.
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
    ap.add_argument("--staging", required=True)
    ap.add_argument("--directive-id", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    with open(args.staging, "r", encoding="utf-8") as f:
        staging = json.load(f)
    sg_code = staging["metadata"]["cluster_subgroup_code"]
    needs_sg_create = staging["metadata"].get("needs_subgroup_creation", False)
    sg_create_info = staging["metadata"].get("subgroup_to_create")
    vcg_blocks = staging["vcg_creations"]
    setaside_block = staging["setasides"]

    print("=" * 72)
    print(f"{args.directive_id} apply ({sg_code} VCG cleanup)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print(f"  Staging: {args.staging}")
    print(f"  Needs sub-group creation: {needs_sg_create}")
    print("=" * 72)
    print()

    print(f"Staging summary:")
    print(f"  VCGs to create: {len(vcg_blocks)}")
    print(f"  Verses to assign: {sum(b['verse_count'] for b in vcg_blocks)}")
    print(f"  Verses to set aside: {setaside_block['verse_count']}")
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Pre-flight
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    SG_ID = None
    r = conn.execute(
        "SELECT id FROM cluster_subgroup "
        " WHERE cluster_code='M15' AND subgroup_code=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (sg_code,),
    ).fetchone()
    if r:
        SG_ID = r["id"]
        print(f"  [ok] {sg_code} sub-group exists, id={SG_ID}")
    elif needs_sg_create:
        print(f"  [info] {sg_code} sub-group does not exist; will create in Phase 0b")
    else:
        print(f"  [ERR] {sg_code} sub-group missing and no creation flag")
        ok = False

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

    all_targets: list[int] = []
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

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup(f"m15_{args.directive_id.lower().replace('-','_')}_{sg_code.lower().replace('-','_')}")
        print(f"Backup: {b}")
        print()

    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 0b — Create sub-group if needed
        if needs_sg_create and SG_ID is None:
            print("Phase 0b — Create cluster_subgroup row")
            print("-" * 72)
            SG_ID = cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, "
                "   status, version, source, delete_flagged, "
                "   created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?)",
                ("M15", sg_create_info["code"], sg_create_info["label"],
                 sg_create_info["description"],
                 "active", "v1",
                 f"{args.directive_id}: new sub-group for logos",
                 ts, ts),
            ).lastrowid
            counts["phase0b_subgroup_created"] = 1
            print(f"  Created {sg_code} sub-group, id={SG_ID}")
            print()

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
                     f"{args.directive_id}: {sg_code} VCG cleanup", ts, ts),
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
        ph2_duplicates_resolved = 0
        for block in vcg_blocks:
            vcg_id = new_vcg_id_by_code[block["code"]]
            verse_vr_ids = {v["vr_id"] for v in block["verses"]}
            anchor_vr = block.get("anchor_proposed", {}).get("vr_id") if block.get("anchor_proposed") else None
            if anchor_vr is not None and anchor_vr not in verse_vr_ids:
                verse_vr_ids.add(anchor_vr)
            for vr_id in verse_vr_ids:
                is_anchor = 1 if vr_id in anchor_vr_ids else 0
                # Detect multiple active vc rows (the known duplicate-vr
                # data-integrity issue). Update the lowest vc_id; soft-
                # delete the rest with an explanatory note.
                vc_rows = cur.execute(
                    "SELECT id, cluster_subgroup_id FROM verse_context "
                    " WHERE verse_record_id=? "
                    "   AND COALESCE(delete_flagged,0)=0 "
                    " ORDER BY id ASC",
                    (vr_id,),
                ).fetchall()
                if not vc_rows:
                    continue
                primary_vc_id = vc_rows[0]["id"]
                pre_sg = vc_rows[0]["cluster_subgroup_id"]
                if pre_sg != SG_ID:
                    ph2_moved += 1
                # Update the primary
                rc = cur.execute(
                    "UPDATE verse_context "
                    "   SET group_id = ?, "
                    "       cluster_subgroup_id = ?, "
                    "       is_relevant = 1, "
                    "       is_anchor = ?, "
                    "       set_aside_reason = NULL "
                    " WHERE id = ?",
                    (vcg_id, SG_ID, is_anchor, primary_vc_id),
                ).rowcount
                ph2 += rc
                # Soft-delete duplicates
                for extra in vc_rows[1:]:
                    cur.execute(
                        "UPDATE verse_context "
                        "   SET delete_flagged = 1, "
                        "       notes = COALESCE(notes || ' | ', '') || ? "
                        " WHERE id = ?",
                        (f"{args.directive_id}: duplicate active vc row "
                         f"for vr_id {vr_id} — soft-deleted (primary kept "
                         f"as vc_id {primary_vc_id})", extra["id"]),
                    )
                    ph2_duplicates_resolved += 1
        counts["phase2_verses_assigned"] = ph2
        counts["phase2_moved_from_other_sg"] = ph2_moved
        counts["phase2_duplicate_vc_rows_soft_deleted"] = ph2_duplicates_resolved
        print(f"  Assigned {ph2} rows, {len(anchor_vr_ids)} anchors"
              + (f", {ph2_moved} moved into {sg_code} from other sg"
                 if ph2_moved else "")
              + (f", {ph2_duplicates_resolved} duplicate vc rows soft-deleted"
                 if ph2_duplicates_resolved else ""))

        # Phase 3 — Set-asides
        print()
        print(f"Phase 3 — Apply set-aside (and move to {sg_code} if elsewhere)")
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
        print(f"  Set aside {ph3} rows"
              + (f" ({ph3_moved} moved into {sg_code} from other sg)"
                 if ph3_moved else ""))

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print()
        print("FK check: ok")

        # Verification (compact)
        print()
        print("VERIFICATION (compact)")
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
            print(f"  {code:18s} vcg_id={vcg_id:>6d} verses={n:>3d} anchors={a}")
        n_sa = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
             WHERE mt.cluster_code='M15'
               AND vc.cluster_subgroup_id=?
               AND vc.set_aside_reason=?
               AND COALESCE(vc.delete_flagged,0)=0
        """, (SG_ID, setaside_block["reason_code"])).fetchone()[0]
        print(f"  {sg_code} set-asides (post): {n_sa}")

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
