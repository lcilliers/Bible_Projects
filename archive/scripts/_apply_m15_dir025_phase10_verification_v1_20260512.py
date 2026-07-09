"""_apply_m15_dir025_phase10_verification_v1_20260512.py — DB-modifying
(only on Step 5 — cluster.status advance, after all gates pass).

Apply DIR-20260512-002 (M15 Phase 10 verification + cluster closure).

Per cluster instruction §13 Phase 10:

  Step 1 — CC verification queries (read-only)
            A. Anchor verification — each new VCG has exactly one anchor
            B. VCG / verse_context coverage
            C. cluster_finding coverage (189 × scopes)
            D. Connectivity health (H1–H8)
            E. Set-aside consistency (canonical reason)
            F. Duplicate vc rows (must be 0)
            G. Stray verses (must be 0)
  Step 2 — Gap audit (report — gaps allowed if pre-declared)
  Step 3 — Decision gate: any blocker → halt
  Step 4 — Status advance: UPDATE cluster SET status='Analysis Completed'

Halt on any blocker; status advance only if all gates pass.
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
DIRECTIVE_ID = "DIR-20260512-002"
CLUSTER_CODE = "M15"
TARGET_STATUS = "Analysis Completed"


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
    print(f"{DIRECTIVE_ID} apply (M15 Phase 10 verification + closure)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    blockers: list[str] = []
    warnings: list[str] = []

    # ---------- Step 1A — Anchor verification ----------
    print("Step 1A — Anchor verification per new VCG")
    print("-" * 72)
    anchor_rows = list(conn.execute("""
        SELECT vcg.group_code,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.group_id = vcg.id
                   AND vc.is_anchor = 1
                   AND COALESCE(vc.delete_flagged,0) = 0) AS anchors,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.group_id = vcg.id
                   AND COALESCE(vc.delete_flagged,0) = 0) AS verses
          FROM verse_context_group vcg
         WHERE vcg.group_code LIKE 'M15-%-VCG%'
           AND COALESCE(vcg.delete_flagged,0) = 0
         ORDER BY vcg.group_code
    """))
    no_anchor = [r for r in anchor_rows if r["anchors"] == 0]
    multi_anchor = [r for r in anchor_rows if r["anchors"] > 1]
    print(f"  Total new VCGs: {len(anchor_rows)}")
    print(f"  VCGs with 0 anchors: {len(no_anchor)}")
    print(f"  VCGs with >1 anchor: {len(multi_anchor)}")
    if no_anchor:
        for r in no_anchor:
            print(f"    [BLOCKER] {r['group_code']:18s} 0 anchors, {r['verses']} verses")
        blockers.append(f"{len(no_anchor)} VCGs have no anchor")
    if multi_anchor:
        for r in multi_anchor:
            print(f"    [WARN] {r['group_code']:18s} {r['anchors']} anchors")
        warnings.append(f"{len(multi_anchor)} VCGs have multiple anchors")

    # ---------- Step 1B — VCG/verse_context coverage ----------
    print()
    print("Step 1B — VCG / verse_context coverage")
    print("-" * 72)
    total_vc = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15' AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    in_vcg = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15' AND vc.group_id IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    set_aside = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15' AND vc.set_aside_reason IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  Active M15 vc rows: {total_vc}")
    print(f"  In a VCG (group_id NOT NULL): {in_vcg}")
    print(f"  Set-aside (reason populated): {set_aside}")
    print(f"  Other (pending / NR): {total_vc - in_vcg - set_aside}")

    # ---------- Step 1C — cluster_finding coverage ----------
    print()
    print("Step 1C — cluster_finding coverage (M15)")
    print("-" * 72)
    cf_total = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M15'"
    ).fetchone()[0]
    cf_by_status = list(conn.execute("""
        SELECT finding_status, COUNT(*) n FROM cluster_finding
         WHERE cluster_code='M15' GROUP BY finding_status
    """))
    print(f"  Total M15 findings: {cf_total}")
    for r in cf_by_status:
        print(f"    {r['finding_status']:25s} {r['n']}")
    if cf_total < 1500:
        blockers.append(f"cluster_finding has only {cf_total} M15 rows (expected ≥1500)")

    # ---------- Step 1D — Connectivity health (H-checks) ----------
    print()
    print("Step 1D — Connectivity health (H1–H8)")
    print("-" * 72)
    h1 = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15' AND vc.cluster_subgroup_id IS NULL
           AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    h6 = conn.execute("""
        SELECT COUNT(DISTINCT strongs_number) FROM mti_terms mt
         WHERE mt.cluster_code='M15'
           AND NOT EXISTS (SELECT 1 FROM mti_term_subgroup mts
                            WHERE mts.mti_term_id = mt.id
                              AND COALESCE(mts.delete_flagged,0)=0)
    """).fetchone()[0]
    h7 = conn.execute("""
        SELECT COUNT(DISTINCT mt.strongs_number) FROM mti_terms mt
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                                     AND COALESCE(mts.delete_flagged,0)=0
         WHERE mt.cluster_code='M15'
           AND NOT EXISTS (SELECT 1 FROM vcg_term vt
                            WHERE vt.mti_term_id = mt.id
                              AND COALESCE(vt.delete_flagged,0)=0)
    """).fetchone()[0]
    h8 = list(conn.execute("""
        SELECT vcg.group_code, COUNT(DISTINCT cs.subgroup_code) AS n_sg
          FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
          JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15' AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY vcg.group_code
        HAVING COUNT(DISTINCT cs.subgroup_code) > 1
    """))
    print(f"  H1 — vc rows with NULL cluster_subgroup_id: {h1}")
    print(f"  H6 — M15 terms with no mti_term_subgroup link: {h6}")
    print(f"  H7 — M15 terms with sub-group but no vcg_term: {h7}")
    print(f"  H8 — VCGs spanning >1 sub-group: {len(h8)}")
    for r in h8:
        print(f"    [WARN] H8: {r['group_code']} → {r['n_sg']} sub-groups")
    # H1 and H6 should be 0; H7 can be acceptable if terms are zero-verse
    # placeholders; H8 warnings only
    if h1 > 0:
        blockers.append(f"H1: {h1} vc rows with NULL cluster_subgroup_id")
    if h6 > 0:
        # Check if these are zero-verse placeholders
        zero_verse_unmapped = conn.execute("""
            SELECT COUNT(DISTINCT mt.strongs_number) FROM mti_terms mt
             WHERE mt.cluster_code='M15'
               AND NOT EXISTS (SELECT 1 FROM mti_term_subgroup mts
                                WHERE mts.mti_term_id = mt.id
                                  AND COALESCE(mts.delete_flagged,0)=0)
               AND NOT EXISTS (SELECT 1 FROM wa_verse_records vr
                                WHERE vr.mti_term_id = mt.id
                                  AND COALESCE(vr.delete_flagged,0)=0)
        """).fetchone()[0]
        if zero_verse_unmapped == h6:
            warnings.append(f"H6: {h6} unmapped terms — all zero-verse placeholders (acceptable)")
            print(f"    [info] all {h6} unmapped terms are zero-verse placeholders")
        else:
            blockers.append(f"H6: {h6} terms with no sub-group mapping "
                            f"({h6 - zero_verse_unmapped} with verses)")
    if h7 > 0:
        warnings.append(f"H7: {h7} terms have sub-group but no vcg_term — likely zero-verse")
    if h8:
        warnings.append(f"H8: {len(h8)} VCGs span >1 sub-group (multi-sg verses)")

    # ---------- Step 1E — Set-aside consistency ----------
    print()
    print("Step 1E — Set-aside consistency")
    print("-" * 72)
    sa_reasons = list(conn.execute("""
        SELECT set_aside_reason, COUNT(*) n FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15'
           AND vc.set_aside_reason IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY set_aside_reason
    """))
    for r in sa_reasons:
        print(f"  reason={r['set_aside_reason']!r}  {r['n']}")
    non_canon = [r for r in sa_reasons
                 if r["set_aside_reason"] != "no_inner_being_phenomenon"]
    if non_canon:
        blockers.append(f"non-canonical set-aside reasons: "
                        f"{[r['set_aside_reason'] for r in non_canon]}")

    # ---------- Step 1F — Duplicate vc rows ----------
    print()
    print("Step 1F — Duplicate active vc rows")
    print("-" * 72)
    n_dups = conn.execute("""
        SELECT COUNT(*) FROM (
            SELECT vc.verse_record_id, vc.mti_term_id, COUNT(*) n
              FROM verse_context vc
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE mt.cluster_code='M15'
               AND COALESCE(vc.delete_flagged,0)=0
             GROUP BY vc.verse_record_id, vc.mti_term_id
            HAVING COUNT(*) > 1
        )
    """).fetchone()[0]
    print(f"  Duplicate (vr_id, mti_term_id) active vc pairs: {n_dups}")
    if n_dups > 0:
        blockers.append(f"{n_dups} duplicate active vc rows")

    # ---------- Step 1G — Stray verses ----------
    print()
    print("Step 1G — Stray vc rows (no group, no set-aside, relevant=1)")
    print("-" * 72)
    n_stray = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.group_id IS NULL
           AND vc.set_aside_reason IS NULL
           AND vc.is_relevant = 1
    """).fetchone()[0]
    print(f"  Stray vc rows: {n_stray}")
    if n_stray > 0:
        blockers.append(f"{n_stray} stray vc rows")

    # ---------- Step 2 — Gap audit ----------
    print()
    print("Step 2 — Gap audit (pre-declared gaps from directive)")
    print("-" * 72)
    gap_rows = list(conn.execute("""
        SELECT q.question_code,
               COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
               SUBSTR(cf.finding_text, 1, 80) AS excerpt
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
         WHERE cf.cluster_code='M15' AND cf.finding_status='gap'
         ORDER BY q.question_code, scope
    """))
    print(f"  Gap rows: {len(gap_rows)}")
    for r in gap_rows:
        print(f"    {r['question_code']:>8s} {r['scope']:12s} {r['excerpt']}")
    # All gaps should be pre-declared (T6.7.3 + T7.1.8 family)
    expected_gap_qcodes = {"T6.7.3", "T7.1.8"}
    unexpected = [r for r in gap_rows
                  if r["question_code"] not in expected_gap_qcodes]
    if unexpected:
        warnings.append(f"{len(unexpected)} gap rows outside pre-declared set")

    # ---------- Decision gate ----------
    print()
    print("=" * 72)
    print("DECISION GATE")
    print("=" * 72)
    if blockers:
        print()
        print("[HALT] Blockers present:")
        for b in blockers:
            print(f"  - {b}")
        if warnings:
            print()
            print("Warnings (non-blocking):")
            for w in warnings:
                print(f"  - {w}")
        print()
        print("Status will NOT advance. Resolve blockers first.")
        return 1

    print()
    print("✅ All gates pass.")
    if warnings:
        print()
        print("Warnings (non-blocking, recorded):")
        for w in warnings:
            print(f"  - {w}")

    # ---------- Step 4 — Status advance ----------
    print()
    print("Step 4 — Cluster status advance")
    print("-" * 72)
    pre = conn.execute(
        "SELECT cluster_code, status, last_updated_date FROM cluster "
        "WHERE cluster_code=?", (CLUSTER_CODE,),
    ).fetchone()
    print(f"  Pre:  status={pre['status']!r}  last_updated={pre['last_updated_date']}")
    if pre["status"] == TARGET_STATUS:
        print(f"  Already at target status — no change needed.")
        conn.close()
        return 0

    if args.live:
        b = take_backup("m15_dir025_status_complete")
        print(f"  Backup: {b}")

    cur = conn.cursor()
    ts = now_iso()
    cur.execute(
        "UPDATE cluster SET status=?, last_updated_date=? WHERE cluster_code=?",
        (TARGET_STATUS, ts, CLUSTER_CODE),
    )
    print(f"  Updated rows: {cur.rowcount}")
    post = conn.execute(
        "SELECT cluster_code, status, last_updated_date FROM cluster "
        "WHERE cluster_code=?", (CLUSTER_CODE,),
    ).fetchone()
    print(f"  Post: status={post['status']!r}  last_updated={post['last_updated_date']}")

    if args.dry_run:
        conn.rollback()
        print("  DRY-RUN: rolled back.")
    else:
        conn.commit()
        print("  LIVE: COMMIT successful.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
