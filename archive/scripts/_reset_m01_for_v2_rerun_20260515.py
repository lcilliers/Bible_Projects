"""Reset M01 to a pre-DIR-001 / pre-DIR-002 state for the v2_0 methodology rerun.

Researcher-authorised reset (2026-05-15). After this script, M01 should be back to
the "post-UT-review, pre-constitution-debate" state:

  - 94 active mti_terms with cluster_code='M01' (12 transferred terms returned)
  - 0 active cluster_subgroup rows for M01
  - 0 active mti_term_subgroup rows for M01
  - cluster.status = 'Not started' (so the constitution-report-gen script fires
    the inline transition to 'Data - In Progress')
  - All UT-review vc rows (128 + Act 7:11 set-aside) PRESERVED — Phase 1 in both
    old and new methodology produces the same work; no need to redo

Reverses:
  - DIR-20260515-001 (term transfer): 10 mti_terms M24 → M01; 2 M03 → M01
  - DIR-20260515-002 (sub-group assign): soft-delete 86 mti_term_subgroup rows,
    soft-delete 9 cluster_subgroup rows, revert cluster.status

Preserves:
  - The UT review API patch (archived) and its 128 vc inserts
  - The Act 7:11 set-aside vc row (researcher decision)
  - All existing analysis_note values (none should exist — Phase 2 hasn't run yet)
  - The closed DIR-001 / DIR-002 / closure reports as historical record

Single transaction. Rollback on any failure.

Usage:
  python scripts/_reset_m01_for_v2_rerun_20260515.py [--dry-run]
"""
from __future__ import annotations
import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"

M24_RETURN_MTIS = [21, 51, 156, 240, 2494, 4814, 5157, 5572, 6210, 6385]  # 10 terms
M03_RETURN_MTIS = [198, 1552]  # 2 terms

NOTE_PREFIX = "v2_0 rerun reset (researcher-authorised 2026-05-15): "


def main():
    dry_run = "--dry-run" in sys.argv
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    try:
        conn.execute("BEGIN")

        # Pre-state snapshot
        pre = {}
        pre["m01_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        pre["m24_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M24' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        pre["m03_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M03' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        pre["m01_subgroups"] = conn.execute(
            "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        pre["m01_mti_subgroup_links"] = conn.execute("""
            SELECT COUNT(*) FROM mti_term_subgroup mts
            JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
            WHERE cs.cluster_code='M01' AND COALESCE(mts.delete_flagged,0)=0
        """).fetchone()[0]
        pre["m01_status"] = conn.execute("SELECT status FROM cluster WHERE cluster_code='M01'").fetchone()[0]
        pre["m01_vc_active"] = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code='M01' AND COALESCE(vc.delete_flagged,0)=0
        """).fetchone()[0]
        print("=== Pre-reset state ===")
        for k, v in pre.items():
            print(f"  {k}: {v}")

        # ===== Operation A — Revert term transfers =====
        # 10 mti_terms M24 → M01
        for mti in M24_RETURN_MTIS:
            r = conn.execute(
                "SELECT cluster_code FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (mti,)
            ).fetchone()
            if not r:
                raise RuntimeError(f"mti_id={mti}: row not found or soft-deleted")
            if r["cluster_code"] != "M24":
                raise RuntimeError(f"mti_id={mti}: expected cluster_code='M24', got {r['cluster_code']!r}")
        for mti in M03_RETURN_MTIS:
            r = conn.execute(
                "SELECT cluster_code FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (mti,)
            ).fetchone()
            if not r:
                raise RuntimeError(f"mti_id={mti}: row not found or soft-deleted")
            if r["cluster_code"] != "M03":
                raise RuntimeError(f"mti_id={mti}: expected cluster_code='M03', got {r['cluster_code']!r}")

        rc_m24 = 0
        for mti in M24_RETURN_MTIS:
            rc = conn.execute(
                "UPDATE mti_terms SET cluster_code='M01', last_changed=? WHERE id=? AND cluster_code='M24'",
                (now, mti)
            ).rowcount
            rc_m24 += rc
        if rc_m24 != 10:
            raise RuntimeError(f"Expected 10 M24→M01 reverts, got {rc_m24}")

        rc_m03 = 0
        for mti in M03_RETURN_MTIS:
            rc = conn.execute(
                "UPDATE mti_terms SET cluster_code='M01', last_changed=? WHERE id=? AND cluster_code='M03'",
                (now, mti)
            ).rowcount
            rc_m03 += rc
        if rc_m03 != 2:
            raise RuntimeError(f"Expected 2 M03→M01 reverts, got {rc_m03}")
        print(f"\n[A] Reverted term transfers: 10 M24→M01, 2 M03→M01")

        # ===== Operation B — Soft-delete mti_term_subgroup rows for M01 =====
        rc_mts = conn.execute("""
            UPDATE mti_term_subgroup SET delete_flagged=1, last_updated_date=?,
              placement_note = COALESCE(placement_note,'') || ?
            WHERE cluster_subgroup_id IN (
              SELECT id FROM cluster_subgroup WHERE cluster_code='M01'
            ) AND COALESCE(delete_flagged,0)=0
        """, (now, " | " + NOTE_PREFIX + "soft-deleted on reset of DIR-20260515-002")).rowcount
        print(f"[B] Soft-deleted mti_term_subgroup rows for M01: {rc_mts}")

        # ===== Operation C — Soft-delete cluster_subgroup rows for M01 =====
        rc_cs = conn.execute("""
            UPDATE cluster_subgroup SET delete_flagged=1, last_updated_date=?,
              notes = COALESCE(notes,'') || ?
            WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0
        """, (now, " | " + NOTE_PREFIX + "soft-deleted on reset of DIR-20260515-002")).rowcount
        print(f"[C] Soft-deleted cluster_subgroup rows for M01: {rc_cs}")

        # ===== Operation D — Revert cluster.status =====
        rc_status = conn.execute("""
            UPDATE cluster SET status='Not started', last_updated_date=?
            WHERE cluster_code='M01'
        """, (now,)).rowcount
        if rc_status != 1:
            raise RuntimeError(f"Expected 1 cluster status reset, got {rc_status}")
        print(f"[D] Reset cluster.status M01 → 'Not started'")

        # ===== Post-state =====
        post = {}
        post["m01_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        post["m24_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M24' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        post["m03_term_count"] = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M03' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        post["m01_subgroups"] = conn.execute(
            "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        post["m01_mti_subgroup_links"] = conn.execute("""
            SELECT COUNT(*) FROM mti_term_subgroup mts
            JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
            WHERE cs.cluster_code='M01' AND COALESCE(mts.delete_flagged,0)=0
        """).fetchone()[0]
        post["m01_status"] = conn.execute("SELECT status FROM cluster WHERE cluster_code='M01'").fetchone()[0]
        post["m01_vc_active"] = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code='M01' AND COALESCE(vc.delete_flagged,0)=0
        """).fetchone()[0]

        print("\n=== Post-reset state ===")
        for k in pre:
            print(f"  {k}: {pre[k]} → {post[k]}")

        # Expected: M01 = 94, M24 = 67, M03 = 86, subgroups = 0, links = 0, status = 'Not started'
        expected = {
            "m01_term_count": 94,
            "m24_term_count": 67,
            "m03_term_count": 86,
            "m01_subgroups": 0,
            "m01_mti_subgroup_links": 0,
            "m01_status": "Not started",
        }
        problems = []
        for k, exp in expected.items():
            if post[k] != exp:
                problems.append(f"{k}: expected {exp}, got {post[k]}")
        if problems:
            print("\nProblems:")
            for p in problems:
                print(f"  ✗ {p}")
            raise RuntimeError("Post-reset state did not match expected — rolling back.")

        if dry_run:
            conn.execute("ROLLBACK")
            print("\n[DRY RUN] Rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nCommitted.")
    except Exception as exc:
        conn.execute("ROLLBACK")
        print(f"\nERROR: {exc}\nRolled back.")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
