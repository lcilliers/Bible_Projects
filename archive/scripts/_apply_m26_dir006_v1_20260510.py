"""_apply_m26_dir006_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-006 (M26-B/C/D/E/F/G targeted cleanup).

7 small operations in one transaction:

  Phase 1 — 4 vr_ids: status P → SA + set_aside_reason='no_inner_being'
            45950 Job 33:23   (M26-B, H3476)
            145645 Mat 27:3   (M26-E, G2632)
            145640 Mar 14:64  (M26-E, G2632)
            145632 2Pe 2:6    (M26-E, G2632)

  Phase 2 — vr_id 232246 (Ecc 12:10 H3476): vcg 1211-002 → 1211-003

  Phase 3 — 2 vr_ids: SA → G (clear set_aside_reason, set group_id)
            101925 1Pe 5:12 G3049 → 3410-001
            101959 Rom 9:8  G3049 → 3410-001

NO API calls. ~1 sec wall time.
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

PHASE1_PSA = [
    (45950, "Job 33:23 H3476"),
    (145645, "Mat 27:3 G2632"),
    (145640, "Mar 14:64 G2632"),
    (145632, "2Pe 2:6 G2632"),
]
PHASE2_REASSIGN = (232246, "1211-002", "1211-003")
PHASE3_SA_TO_G = [(101925, "3410-001"), (101959, "3410-001")]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def get_vcg_id(conn, code):
    r = conn.execute(
        "SELECT id FROM verse_context_group "
        " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
        (code,),
    ).fetchone()
    return r[0] if r else None


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
    print("DIR-M26-20260510-006 apply (B/C/D/E/F/G cleanup)")
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

    # Phase 1: 4 vr_ids must each have an active vc row that's currently
    # P-status (is_relevant=1, group_id NULL, set_aside_reason NULL/empty)
    for vr, label in PHASE1_PSA:
        r = conn.execute(
            "SELECT id, is_relevant, group_id, set_aside_reason "
            "  FROM verse_context "
            " WHERE verse_record_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vr,),
        ).fetchone()
        if not r:
            print(f"  [ERR] vr_id {vr} ({label}) — no active vc row")
            ok = False
        else:
            is_p = (r["is_relevant"] == 1 and r["group_id"] is None
                    and not r["set_aside_reason"])
            print(f"  [{'ok' if is_p else 'WARN'}] vr_id {vr} ({label}) "
                  f"vc.id={r['id']} is_p={is_p}")

    # Phase 2: vr_id 232246, currently in 1211-002
    src_id = get_vcg_id(conn, "1211-002")
    dst_id = get_vcg_id(conn, "1211-003")
    if not src_id or not dst_id:
        print(f"  [ERR] Phase 2 vcg codes missing: src={src_id} dst={dst_id}")
        ok = False
    else:
        r = conn.execute(
            "SELECT id, group_id FROM verse_context "
            " WHERE verse_record_id=232246 "
            "   AND COALESCE(delete_flagged,0)=0"
        ).fetchone()
        if not r:
            print(f"  [ERR] vr_id 232246 has no active vc row")
            ok = False
        else:
            print(f"  [{'ok' if r['group_id']==src_id else 'WARN'}] "
                  f"vr_id 232246 vc.id={r['id']} currently group_id="
                  f"{r['group_id']} (1211-002={src_id}, 1211-003={dst_id})")

    # Phase 3: 2 vr_ids currently SA, target 3410-001
    p3_dst = get_vcg_id(conn, "3410-001")
    if not p3_dst:
        print(f"  [ERR] Phase 3 destination vcg 3410-001 not found")
        ok = False
    else:
        for vr, _ in PHASE3_SA_TO_G:
            r = conn.execute(
                "SELECT id, set_aside_reason, group_id "
                "  FROM verse_context "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            if not r:
                print(f"  [ERR] vr_id {vr} no active vc row")
                ok = False
            else:
                print(f"  [ok] vr_id {vr} vc.id={r['id']} "
                      f"current SA={bool(r['set_aside_reason'])} "
                      f"group_id={r['group_id']}")

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup("m26_dir006")
        print(f"Backup: {b}\n")

    print("EXECUTE")
    print("-" * 72)
    counts = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # Phase 1
        rc = 0
        for vr, _ in PHASE1_PSA:
            rc += cur.execute(
                "UPDATE verse_context "
                "   SET set_aside_reason='no_inner_being' "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr,),
            ).rowcount
        counts["phase1_p_to_sa"] = rc
        print(f"  Phase 1 (P → SA): {rc} vc rows")

        # Phase 2
        vr, src, dst = PHASE2_REASSIGN
        rc = cur.execute(
            "UPDATE verse_context "
            "   SET group_id=? "
            " WHERE verse_record_id=? "
            "   AND group_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (dst_id, vr, src_id),
        ).rowcount
        counts["phase2_reassign"] = rc
        print(f"  Phase 2 (1211-002 → 1211-003): {rc} vc row")

        # Phase 3
        rc = 0
        for vr, _ in PHASE3_SA_TO_G:
            rc += cur.execute(
                "UPDATE verse_context "
                "   SET set_aside_reason=NULL, "
                "       is_relevant=1, "
                "       group_id=? "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (p3_dst, vr),
            ).rowcount
        counts["phase3_sa_to_g"] = rc
        print(f"  Phase 3 (SA → G in 3410-001): {rc} vc rows")

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}")
        print()
        print("FK check: ok")

        # Verify
        print()
        print("VERIFICATION")
        print("-" * 72)
        # 1. Phase 1 vr_ids now SA
        for vr, label in PHASE1_PSA:
            r = conn.execute(
                "SELECT set_aside_reason FROM verse_context "
                " WHERE verse_record_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            print(f"  vr_id {vr} ({label}) set_aside_reason="
                  f"'{r['set_aside_reason']}'")
        # 2. Phase 2 vr_id now in 1211-003
        r = conn.execute(
            "SELECT vcg.group_code FROM verse_context vc "
            "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
            " WHERE vc.verse_record_id=232246 "
            "   AND COALESCE(vc.delete_flagged,0)=0"
        ).fetchone()
        print(f"  vr_id 232246 → {r['group_code']}")
        # 3. Phase 3 vr_ids now in 3410-001
        for vr, _ in PHASE3_SA_TO_G:
            r = conn.execute(
                "SELECT vcg.group_code, vc.set_aside_reason FROM verse_context vc "
                "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
                " WHERE vc.verse_record_id=? "
                "   AND COALESCE(vc.delete_flagged,0)=0",
                (vr,),
            ).fetchone()
            print(f"  vr_id {vr} → {r['group_code']} "
                  f"(set_aside_reason={r['set_aside_reason']})")

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
        print(f"  {k:30s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
