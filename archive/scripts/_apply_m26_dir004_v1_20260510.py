"""_apply_m26_dir004_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-004 (M26-A2 straggler cleanup) under the
post-DIR-003 v12 state.

Source directive:
  Sessions/Session_Clusters/M26/wa-cluster-M26-dir-004-A2-straggler-cleanup-v1-20260510.md

12 vc.group_id UPDATEs:
  - 8 I-6 stragglers (DIR-003 omissions)
  - 4 legacy 3246-001 remnants

Plus:
  - 1 analytical note appended to vr_id 96008 (Psa 17:15 H6664G —
    eschatological dimension flagged for future VSG split).

Post-apply check: 3246-001 still has 4 M26-A1 + 1 M26-BOUNDARY verses
so it is NOT soft-deleted (only empty in M26-A2 scope).

Single transaction, foreign_keys=ON, no API calls.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

# All moves expressed as (vr_id, dest_group_code). The vc row must
# currently sit in M26-A2; that's the directive's scope.
MOVES = [
    # I-6 stragglers (DIR-003 omissions)
    (25184, "M26-A2-010"),
    (28314, "M26-A2-003"),
    (28315, "M26-A2-006"),
    (28330, "M26-A2-008"),
    (28333, "950-002"),
    (96008, "M26-A2-014"),
    (96013, "3246-003"),
    (169443, "M26-A2-014"),
    # 3246-001 legacy remnants
    (169461, "M26-A2-006"),
    (169429, "M26-A2-011"),
    (169358, "M26-A2-002"),
    (169374, "M26-A2-017"),
]

# vr_id 96008 also gets an analytical note (eschatological flag).
NOTE_96008 = (
    "DIR-004 (2026-05-10): assigned to M26-A2-014 (relational "
    "orientation toward God) as closest existing group. This verse "
    "has an eschatological dimension — 'behold your face in "
    "righteousness, awake satisfied with your likeness' — that "
    "warrants its own VSG eventually. Flagged for future "
    "eschatological-righteousness split."
)


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


def preflight(conn):
    msgs = []
    ok = True

    sg = {r[0]: r[1] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    )}
    if "M26-A2" not in sg:
        msgs.append("[ERR] M26-A2 sub-group missing")
        return False, msgs, sg, {}

    # Resolve dest group_codes
    codes = sorted({c for _, c in MOVES})
    ph = ",".join("?" * len(codes))
    code_to_id = {r[0]: r[1] for r in conn.execute(
        f"SELECT group_code, id FROM verse_context_group "
        f" WHERE group_code IN ({ph}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        codes,
    )}
    missing = [c for c in codes if c not in code_to_id]
    if missing:
        msgs.append(f"[ERR] destination vcgs missing: {missing}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(codes)} destination vcgs resolved")

    # Each vr_id must have exactly one active vc row in M26-A2
    vr_ids = [v for v, _ in MOVES]
    ph_v = ",".join("?" * len(vr_ids))
    vc_rows = list(conn.execute(
        f"SELECT verse_record_id, COUNT(*) FROM verse_context "
        f" WHERE verse_record_id IN ({ph_v}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0 "
        f" GROUP BY verse_record_id",
        (*vr_ids, sg["M26-A2"]),
    ))
    found = {r[0]: r[1] for r in vc_rows}
    missing_vr = [v for v in vr_ids if v not in found]
    multi_vr = [v for v, n in found.items() if n > 1]
    if missing_vr:
        msgs.append(f"[ERR] vr_ids with no active M26-A2 vc row: "
                    f"{missing_vr}")
        ok = False
    if multi_vr:
        msgs.append(f"[WARN] vr_ids with >1 active M26-A2 vc row "
                    f"(directive assumes exactly 1): {multi_vr}")
    if not missing_vr and not multi_vr:
        msgs.append(f"[ok] all {len(vr_ids)} vr_ids have exactly 1 "
                    f"active M26-A2 vc row")

    return ok, msgs, sg, code_to_id


def run_apply(conn, sg, code_to_id):
    cur = conn.cursor()
    counts = defaultdict(int)
    sg_a2 = sg["M26-A2"]

    print()
    print("EXECUTE")
    print("-" * 72)
    for vr_id, dest_code in MOVES:
        dest_id = code_to_id[dest_code]
        rc = cur.execute(
            "UPDATE verse_context "
            "   SET group_id=? "
            " WHERE verse_record_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (dest_id, vr_id, sg_a2),
        ).rowcount
        counts["vc_moves"] += rc
        print(f"  vr_id {vr_id:>6} → {dest_code:<14} ({rc} row)")

    # Append eschatological note to vr_id 96008
    rc = cur.execute(
        "UPDATE verse_context "
        "   SET notes=COALESCE(notes || ' | ', '') || ? "
        " WHERE verse_record_id=? "
        "   AND cluster_subgroup_id=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (NOTE_96008, 96008, sg_a2),
    ).rowcount
    counts["notes_appended"] = rc
    print(f"  vr_id 96008 — analytical note appended ({rc} row)")

    return counts


def verify(conn, sg, code_to_id):
    invariants = {}
    sg_a2 = sg["M26-A2"]

    # I-1: Each move landed correctly
    placements = {}
    for vr_id, dest_code in MOVES:
        r = conn.execute(
            "SELECT vcg.group_code FROM verse_context vc "
            "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
            " WHERE vc.verse_record_id=? "
            "   AND vc.cluster_subgroup_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0",
            (vr_id, sg_a2),
        ).fetchone()
        actual = r[0] if r else "(missing)"
        placements[vr_id] = (
            f"{actual} {'✓' if actual == dest_code else '✗ expected '+dest_code}"
        )
    invariants["I-1: vc placements"] = placements

    # I-2: 3246-001 should have 0 M26-A2 verses
    r = conn.execute(
        "SELECT id FROM verse_context_group WHERE group_code='3246-001' "
        " AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    if r:
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (r[0], sg_a2),
        ).fetchone()[0]
        invariants["I-2: 3246-001 active vc rows in M26-A2 "
                   "(expect 0)"] = n
        # And what remains in 3246-001 globally?
        n_other = conn.execute(
            "SELECT cs.subgroup_code, COUNT(*) FROM verse_context vc "
            "  JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
            " WHERE vc.group_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0 "
            " GROUP BY cs.subgroup_code",
            (r[0],),
        ).fetchall()
        invariants["I-3: 3246-001 active vc rows by sub-group"] = (
            {row[0]: row[1] for row in n_other}
        )

    # I-4: M26-A2 active vc rows without group_id (pre-existing 3 only)
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE vc.cluster_subgroup_id=? "
        "   AND vc.group_id IS NULL "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND mt.cluster_code='M26'",
        (sg_a2,),
    ).fetchone()[0]
    invariants["I-4: M26-A2 active vc rows without group_id"] = n

    return invariants


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
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print("DIR-M26-20260510-004 apply (M26-A2 straggler cleanup)")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, sg, code_to_id = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting.")
        return 1

    if args.live:
        print("Taking pre-apply backup...")
        b = take_backup("m26_dir004")
        print(f"  Backup saved: {b}")
        print()

    try:
        conn.execute("BEGIN")
        counts = run_apply(conn, sg, code_to_id)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            print(f"  [ERR] {len(fkv)} FK violations")
            raise RuntimeError(f"foreign_key_check failed: {len(fkv)}")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, sg, code_to_id)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {type(e).__name__}: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:30s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
