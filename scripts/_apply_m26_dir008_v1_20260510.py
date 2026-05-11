"""_apply_m26_dir008_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-008 (M26 final cleanup: H8 residuals + H7 closure).

Operations (single transaction, foreign_keys=ON):

  Phase 1 — Within-BOUNDARY vcg reassignments (2 vr_ids → 942-002)
  Phase 2 — BOUNDARY → M26-A2 verse moves (9 vr_ids)
  Phase 2b — Auto-absorb mti_term_subgroup + vcg_term for new
              cross-term/cross-sg placements
  Phase 3 — H8200 she.phat NR confirmation: NO DB change

NO API calls.
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

# Phase 1: stay in BOUNDARY, change vcg from 911-003 → 942-002
PHASE1_VCG_REASSIGN = [
    (169299, "Psa 11:7", "942-002"),
    (25170, "Isa 10:22", "942-002"),
]

# Phase 2: move BOUNDARY → M26-A2, set vcg
# (vr_id, dest_vcg_code)
PHASE2_TO_A2 = [
    (28339, "942-001"),    # Job 31:6
    (96036, "942-001"),    # Psa 94:15
    (96006, "M26-A2-014"), # Psa 15:2
    (96002, "3246-003"),   # Psa 119:62
    (96000, "3246-003"),   # Psa 119:164
    (96001, "3246-003"),   # Psa 119:172
    (28765, "950-002"),    # Rom 6:13
    (28728, "M26-A2-009"), # 2Cor 6:7
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def main():
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
    print("DIR-M26-20260510-008 apply (M26 final cleanup)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Pre-flight
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Resolve sub-group + vcg ids
    sg = {r[0]: r[1] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    )}
    if "M26-A2" not in sg or "M26-BOUNDARY" not in sg:
        print(f"  [ERR] missing sub-groups")
        ok = False

    all_vcg_codes = sorted(
        {c for _, _, c in PHASE1_VCG_REASSIGN} |
        {c for _, c in PHASE2_TO_A2}
    )
    ph = ",".join("?" * len(all_vcg_codes))
    # Look up active AND soft-deleted vcgs — DIR-008 expects 942-002 which
    # was soft-deleted in the H5 fix-up after DIR-007 (it was emptied by
    # DIR-007). The directive's reasoning treats 942-002's description
    # ("God's foundational attribute") as the correct home for these
    # BOUNDARY verses, so we'll reactivate it as part of Phase 1.
    vcg_all = {r[0]: (r[1], r[2]) for r in conn.execute(
        f"SELECT group_code, id, delete_flagged FROM verse_context_group "
        f" WHERE group_code IN ({ph})",
        all_vcg_codes,
    )}
    missing = [c for c in all_vcg_codes if c not in vcg_all]
    if missing:
        print(f"  [ERR] vcg codes missing: {missing}")
        ok = False
    else:
        vcg_ids = {c: vcg_all[c][0] for c in all_vcg_codes}
        soft_deleted = [c for c in all_vcg_codes if vcg_all[c][1]]
        if soft_deleted:
            print(f"  [info] vcg codes soft-deleted (will reactivate): "
                  f"{soft_deleted}")
        print(f"  [ok] all {len(all_vcg_codes)} destination vcg codes present")

    # Each Phase 1 vr_id must currently be in M26-BOUNDARY with group_id pointing
    # at 911-003
    src_911003 = conn.execute(
        "SELECT id FROM verse_context_group WHERE group_code='911-003' "
        "  AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    src_911003 = src_911003[0] if src_911003 else None
    for vr, label, _ in PHASE1_VCG_REASSIGN:
        r = conn.execute(
            "SELECT vc.id, cs.subgroup_code, vc.group_id "
            "  FROM verse_context vc "
            "  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
            " WHERE vc.verse_record_id=? AND COALESCE(vc.delete_flagged,0)=0",
            (vr,),
        ).fetchone()
        if not r:
            print(f"  [ERR] vr_id {vr} ({label}) — no active vc row")
            ok = False
        else:
            in_b = r["subgroup_code"] == "M26-BOUNDARY"
            in_911003 = r["group_id"] == src_911003
            tag = "ok" if in_b and in_911003 else "WARN"
            print(f"  [{tag}] Phase 1 vr_id {vr} ({label}) "
                  f"sg={r['subgroup_code']} group_id={r['group_id']} "
                  f"(911-003={src_911003})")

    # Each Phase 2 vr_id must be in BOUNDARY currently
    for vr, _ in PHASE2_TO_A2:
        r = conn.execute(
            "SELECT vc.id, cs.subgroup_code FROM verse_context vc "
            "  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
            " WHERE vc.verse_record_id=? AND COALESCE(vc.delete_flagged,0)=0",
            (vr,),
        ).fetchone()
        if not r:
            print(f"  [ERR] vr_id {vr} no active vc row")
            ok = False
        else:
            tag = "ok" if r["subgroup_code"] == "M26-BOUNDARY" else "WARN"
            print(f"  [{tag}] Phase 2 vr_id {vr} sg={r['subgroup_code']}")

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup("m26_dir008")
        print(f"Backup: {b}\n")

    counts = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 0 — Reactivate any soft-deleted destination vcgs the
        # directive expects to use
        for code in all_vcg_codes:
            vid, deleted = vcg_all[code]
            if deleted:
                cur.execute(
                    "UPDATE verse_context_group "
                    "   SET delete_flagged=0, "
                    "       notes=COALESCE(notes || ' | ', '') || ? "
                    " WHERE id=?",
                    (f"DIR-008: reactivated — directive routes BOUNDARY "
                     f"verses to this vcg; description retained from "
                     f"DIR-007 update", vid),
                )
                counts["phase0_vcgs_reactivated"] = (
                    counts.get("phase0_vcgs_reactivated", 0) + 1
                )
                print(f"Phase 0: reactivated vcg {code}")

        # Phase 1
        rc = 0
        for vr, _, dest_code in PHASE1_VCG_REASSIGN:
            rc += cur.execute(
                "UPDATE verse_context "
                "   SET group_id=? "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vcg_ids[dest_code], vr),
            ).rowcount
        counts["phase1_within_boundary"] = rc
        print(f"Phase 1: {rc} vc rows reassigned (911-003 → 942-002)")

        # Phase 2
        rc = 0
        for vr, dest_code in PHASE2_TO_A2:
            rc += cur.execute(
                "UPDATE verse_context "
                "   SET cluster_subgroup_id=?, group_id=? "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (sg["M26-A2"], vcg_ids[dest_code], vr),
            ).rowcount
        counts["phase2_to_a2"] = rc
        print(f"Phase 2: {rc} vc rows moved BOUNDARY → M26-A2")

        # Phase 2b — auto-absorb (mti_term_subgroup + vcg_term)
        rc1 = cur.execute(
            "INSERT OR IGNORE INTO mti_term_subgroup "
            "  (mti_term_id, cluster_subgroup_id, placement_note, "
            "   delete_flagged, created_at, last_updated_date) "
            "SELECT DISTINCT vc.mti_term_id, vc.cluster_subgroup_id, "
            "       'DIR-008 absorb', 0, ?, ? "
            "  FROM verse_context vc "
            "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
            " WHERE mt.cluster_code='M26' "
            "   AND vc.cluster_subgroup_id IS NOT NULL "
            "   AND COALESCE(vc.delete_flagged,0)=0 "
            "   AND NOT EXISTS ("
            "       SELECT 1 FROM mti_term_subgroup mts "
            "        WHERE mts.mti_term_id=vc.mti_term_id "
            "          AND mts.cluster_subgroup_id=vc.cluster_subgroup_id "
            "          AND COALESCE(mts.delete_flagged,0)=0"
            "   )",
            (ts, ts),
        ).rowcount
        rc2 = cur.execute(
            "INSERT OR IGNORE INTO vcg_term "
            "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
            "   created_at, last_updated_date) "
            "SELECT DISTINCT vc.group_id, vc.mti_term_id, "
            "       'DIR-008 absorb', 0, ?, ? "
            "  FROM verse_context vc "
            "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
            "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
            " WHERE mt.cluster_code='M26' "
            "   AND COALESCE(vc.delete_flagged,0)=0 "
            "   AND COALESCE(vcg.delete_flagged,0)=0 "
            "   AND NOT EXISTS ("
            "       SELECT 1 FROM vcg_term vt "
            "        WHERE vt.vcg_id=vc.group_id "
            "          AND vt.mti_term_id=vc.mti_term_id "
            "          AND COALESCE(vt.delete_flagged,0)=0"
            "   )",
            (ts, ts),
        ).rowcount
        counts["phase2b_mts_absorbed"] = rc1
        counts["phase2b_vcg_term_absorbed"] = rc2
        print(f"Phase 2b: mti_term_subgroup +{rc1}, vcg_term +{rc2}")

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}")
        print("\nFK check: ok")

        # Verify
        print()
        print("VERIFICATION")
        print("-" * 72)
        for vr, _, dest_code in PHASE1_VCG_REASSIGN:
            r = conn.execute(
                "SELECT cs.subgroup_code, vcg.group_code FROM verse_context vc "
                "  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
                "  LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id "
                " WHERE vc.verse_record_id=? AND COALESCE(vc.delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            print(f"  vr_id {vr}: sg={r['subgroup_code']} vcg={r['group_code']}")
        for vr, dest_code in PHASE2_TO_A2:
            r = conn.execute(
                "SELECT cs.subgroup_code, vcg.group_code FROM verse_context vc "
                "  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
                "  LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id "
                " WHERE vc.verse_record_id=? AND COALESCE(vc.delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            print(f"  vr_id {vr}: sg={r['subgroup_code']} vcg={r['group_code']}")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print("\nDRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nLIVE: COMMIT successful.")
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
