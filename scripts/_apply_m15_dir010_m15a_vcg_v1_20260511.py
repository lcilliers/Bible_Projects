"""_apply_m15_dir010_m15a_vcg_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M15-010: M15-A VCG cleanup.

Operations (single transaction, foreign_keys=ON):

  Phase 0 — Backup
  Phase 1 — Create 10 new VCGs in verse_context_group (M15-A-VCG01..10)
             plus vcg_term link rows per distinct mti_term_id per VCG
  Phase 2 — Assign 263 verses to their new VCGs (verse_context.group_id,
             cluster_subgroup_id=M15-A, is_relevant=1, set_aside_reason=NULL).
             Mark the 10 designated anchors with is_anchor=1; clear is_anchor
             on every other affected row.
  Phase 3 — Apply set-aside to 39 verses (group_id=NULL, is_relevant=0,
             set_aside_reason='no_inner_being_phenomenon', is_anchor=0).
             cluster_subgroup_id stays M15-A (the verse is still in the
             cluster, just not grouped).
  Phase 4 — Re-route 5 verses to M15-E (cluster_subgroup_id=M15-E.id,
             group_id=NULL, is_anchor=0, set_aside_reason=NULL).

Source: Sessions/Session_Clusters/M15/m15-vcg-db-staging-M15A-v2-20260511.json
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
    "m15-vcg-db-staging-M15A-v2-20260511.json",
)
DIRECTIVE_ID = "DIR-20260511-M15-010"


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
    print(f"{DIRECTIVE_ID} apply (M15-A VCG cleanup)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    with open(STAGING_PATH, "r", encoding="utf-8") as f:
        staging = json.load(f)

    vcg_blocks = staging["vcg_creations"]
    setaside_block = staging["setasides"]
    reroute_block = staging["reroutes"]

    print(f"Staging summary:")
    print(f"  VCGs to create: {len(vcg_blocks)}")
    print(f"  Verses to assign to VCGs: {sum(b['verse_count'] for b in vcg_blocks)}")
    print(f"  Verses to set aside: {setaside_block['verse_count']}")
    print(f"  Verses to reroute to M15-E: {reroute_block['verse_count']}")
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # ---------- Pre-flight ----------
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Sub-group ids
    sg_ids = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        " WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0"
    )}
    M15A_ID = sg_ids.get("M15-A")
    M15E_ID = sg_ids.get("M15-E")
    if not M15A_ID or not M15E_ID:
        print(f"  [ERR] missing sub-groups; have={list(sg_ids.keys())}")
        ok = False
    else:
        print(f"  [ok] M15-A sub-group id={M15A_ID}; M15-E sub-group id={M15E_ID}")

    # VCG codes must not already exist
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
        print(f"  [ok] none of the 10 new VCG codes already exist")

    # Collect all vr_ids and check each has exactly one active verse_context
    # row matching (verse_record_id, mti_term_id). For ones where mti_term_id
    # is given but the existing row uses a different mti_term_id (duplicate
    # mti_terms phenomenon), the UPDATE will not match — fall back to update
    # by verse_record_id alone for that row (the unique key on verse_context
    # is (verse_record_id, mti_term_id, group_id), but typically each verse
    # has one OWNER row).
    all_targets: list[tuple[int, int]] = []  # (vr_id, mti_term_id)
    for b in vcg_blocks:
        for v in b["verses"]:
            all_targets.append((v["vr_id"], v["mti_term_id"]))
    for v in setaside_block["verses"]:
        all_targets.append((v["vr_id"], v["mti_term_id"]))
    for v in reroute_block["verses"]:
        all_targets.append((v["vr_id"], v["mti_term_id"]))
    print(f"  [info] total (vr_id, mti_term_id) targets: {len(all_targets)} "
          f"(unique vr_ids: {len({t[0] for t in all_targets})})")

    # Spot-check the first 20 targets exist in verse_context as an active row
    missing_vc = []
    for vr_id, mti_id in all_targets:
        r = conn.execute(
            "SELECT id, mti_term_id, cluster_subgroup_id "
            "  FROM verse_context "
            " WHERE verse_record_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
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

    # Confirm all anchor vr_ids are present in their VCG's verse list
    for b in vcg_blocks:
        a = b.get("anchor_proposed")
        if not a:
            print(f"  [ERR] VCG {b['code']} has no anchor_proposed")
            ok = False
            continue
        if not any(v["vr_id"] == a["vr_id"] for v in b["verses"]):
            print(f"  [ERR] VCG {b['code']} anchor vr_id {a['vr_id']} "
                  f"is not in its verses list")
            ok = False
    print(f"  [ok] all 10 anchors are present in their VCG verses lists"
          if ok else "  [WARN] anchor presence check failed for at least one VCG")

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup("m15_dir010_m15a_vcg")
        print(f"Backup: {b}")
        print()

    # ---------- Apply ----------
    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 1 — Create VCGs and vcg_term rows
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
            # vcg_term links per mti_term_id
            for mti_id in block["mti_term_ids"]:
                cur.execute(
                    "INSERT INTO vcg_term "
                    "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
                    "   created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (rowid, mti_id,
                     f"{DIRECTIVE_ID}: M15-A VCG cleanup", ts, ts),
                )
                vcg_term_inserts += 1
        counts["phase1_vcgs_created"] = len(new_vcg_id_by_code)
        counts["phase1_vcg_term_inserts"] = vcg_term_inserts
        print(f"  Created {len(new_vcg_id_by_code)} VCGs")

        # Phase 2 — Assign verses + anchors
        print()
        print("Phase 2 — Assign 263 verses to new VCGs + mark 10 anchors")
        print("-" * 72)
        ph2_updates = 0
        anchor_vr_ids = {b["anchor_proposed"]["vr_id"] for b in vcg_blocks}
        for block in vcg_blocks:
            vcg_id = new_vcg_id_by_code[block["code"]]
            for v in block["verses"]:
                is_anchor = 1 if v["vr_id"] in anchor_vr_ids else 0
                rc = cur.execute(
                    "UPDATE verse_context "
                    "   SET group_id = ?, "
                    "       cluster_subgroup_id = ?, "
                    "       is_relevant = 1, "
                    "       is_anchor = ?, "
                    "       set_aside_reason = NULL "
                    " WHERE verse_record_id = ? "
                    "   AND COALESCE(delete_flagged,0) = 0",
                    (vcg_id, M15A_ID, is_anchor, v["vr_id"]),
                ).rowcount
                ph2_updates += rc
        counts["phase2_verses_assigned"] = ph2_updates
        print(f"  Assigned {ph2_updates} verse_context rows")
        print(f"  Anchors marked: {len(anchor_vr_ids)}")

        # Phase 3 — Set-asides
        print()
        print("Phase 3 — Apply set-aside to 39 verses")
        print("-" * 72)
        ph3_updates = 0
        for v in setaside_block["verses"]:
            rc = cur.execute(
                "UPDATE verse_context "
                "   SET group_id = NULL, "
                "       is_relevant = 0, "
                "       is_anchor = 0, "
                "       set_aside_reason = ? "
                " WHERE verse_record_id = ? "
                "   AND COALESCE(delete_flagged,0) = 0",
                (setaside_block["reason_code"], v["vr_id"]),
            ).rowcount
            ph3_updates += rc
        counts["phase3_setasides"] = ph3_updates
        print(f"  Set aside {ph3_updates} verse_context rows")

        # Phase 4 — Reroute to M15-E
        print()
        print("Phase 4 — Re-route 5 verses to M15-E")
        print("-" * 72)
        ph4_updates = 0
        for v in reroute_block["verses"]:
            rc = cur.execute(
                "UPDATE verse_context "
                "   SET cluster_subgroup_id = ?, "
                "       group_id = NULL, "
                "       is_anchor = 0, "
                "       set_aside_reason = NULL, "
                "       is_relevant = 1 "
                " WHERE verse_record_id = ? "
                "   AND COALESCE(delete_flagged,0) = 0",
                (M15E_ID, v["vr_id"]),
            ).rowcount
            ph4_updates += rc
        counts["phase4_reroutes"] = ph4_updates
        print(f"  Rerouted {ph4_updates} verse_context rows to M15-E")

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

        # set-aside count
        n_sa = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
             WHERE mt.cluster_code='M15'
               AND vc.cluster_subgroup_id=?
               AND vc.set_aside_reason=?
               AND COALESCE(vc.delete_flagged,0)=0
        """, (M15A_ID, setaside_block["reason_code"])).fetchone()[0]
        print(f"  M15-A set-asides (post): {n_sa}")

        # M15-E reroute count for cha.shav verses
        n_rr = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
             WHERE mt.strongs_number='H2803G'
               AND vc.cluster_subgroup_id=?
               AND COALESCE(vc.delete_flagged,0)=0
        """, (M15E_ID,)).fetchone()[0]
        print(f"  H2803G cha.shav verses now in M15-E: {n_rr}")

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
