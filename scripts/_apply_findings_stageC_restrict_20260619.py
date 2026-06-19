"""_apply_findings_stageC_restrict_20260619.py — Stage C: restrict (mark) the OLD M01/M02 findings.

Soft-delete (delete_flagged=1) + documented reason. Restricts visibility for analysis while RETAINING all data
(reversible by flipping the flag). Scope = the cleanly cluster-coded old findings + their characteristics:
  1. cluster_finding — old consolidated-2026-05-16 set (NOT the DIR-002 C7 row).
  2. finding (CLUSTER level) — session_b_migration + l2_rollup (NOT verse-level l2_meaning — kept as grounding).
  3. characteristic — the legacy 7/6-char model (Pre-v2_6 backfill).
HELD (not touched here — flagged for a separate scoping decision): wa_session_b_findings (registry-keyed, fuzzy
cluster scope) and the old cluster_subgroups (referenced by term-placements/VCGs).

  python scripts/_apply_findings_stageC_restrict_20260619.py --dry-run | --live
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
REASON = "superseded by 2026-06-19 NEW findings (11/7-char model, prose_section capture); retained, excluded from analysis"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sel_cf = """cluster_code IN ('M01','M02') AND COALESCE(delete_flagged,0)=0
                AND source_file LIKE 'WA-M0%-consolidated-findings-v1-20260516%'"""
    sel_fd = """cluster_code IN ('M01','M02') AND COALESCE(delete_flagged,0)=0
                AND level='CLUSTER' AND provenance IN ('session_b_migration','l2_rollup')"""
    sel_ch = """cluster_code IN ('M01','M02') AND COALESCE(delete_flagged,0)=0 AND source LIKE 'Pre-v2_6%'"""

    n_cf = cur.execute(f"SELECT COUNT(*) FROM cluster_finding WHERE {sel_cf}").fetchone()[0]
    n_fd = cur.execute(f"SELECT COUNT(*) FROM finding WHERE {sel_fd}").fetchone()[0]
    n_ch = cur.execute(f"SELECT COUNT(*) FROM characteristic WHERE {sel_ch}").fetchone()[0]
    print(f"to restrict: cluster_finding={n_cf} · finding(CLUSTER)={n_fd} · characteristic(legacy)={n_ch}")
    # KEEP guards (must be untouched)
    keep_l2 = cur.execute("SELECT COUNT(*) FROM finding WHERE cluster_code IN ('M01','M02') AND level='VERSE' AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    keep_dir002 = cur.execute("SELECT COUNT(*) FROM cluster_finding WHERE source_file LIKE 'wa-m02-marah-mar%' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    keep_new = cur.execute("SELECT COUNT(*) FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE t.code LIKE 'cf_%' AND COALESCE(ps.delete_flagged,0)=0").fetchone()[0]
    keep_newchar = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code IN ('M01','M02') AND source LIKE '%2026-06-1%' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"KEEP (must stay): verse l2_meaning={keep_l2} · DIR-002 C7 row={keep_dir002} · new prose_section={keep_new} · new characteristics={keep_newchar}")

    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0

    r1 = cur.execute(f"UPDATE cluster_finding SET delete_flagged=1, notes=COALESCE(notes||' | ','')||? WHERE {sel_cf}", (REASON,)).rowcount
    r2 = cur.execute(f"UPDATE finding SET delete_flagged=1, source_legacy_ref=COALESCE(source_legacy_ref||' | ','')||? WHERE {sel_fd}", (REASON,)).rowcount
    r3 = cur.execute(f"UPDATE characteristic SET delete_flagged=1, notes=COALESCE(notes||' | ','')||? WHERE {sel_ch}", (REASON,)).rowcount
    conn.commit()
    print(f"\nLIVE: restricted cluster_finding={r1} · finding={r2} · characteristic={r3}")
    # verify KEEP untouched
    keep_l2b = cur.execute("SELECT COUNT(*) FROM finding WHERE cluster_code IN ('M01','M02') AND level='VERSE' AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    keep_dir002b = cur.execute("SELECT COUNT(*) FROM cluster_finding WHERE source_file LIKE 'wa-m02-marah-mar%' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    keep_newb = cur.execute("SELECT COUNT(*) FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE t.code LIKE 'cf_%' AND COALESCE(ps.delete_flagged,0)=0").fetchone()[0]
    print(f"KEEP after: verse l2_meaning={keep_l2b} (was {keep_l2}) · DIR-002={keep_dir002b} (was {keep_dir002}) · new prose_section={keep_newb} (was {keep_new})")
    assert (keep_l2b, keep_dir002b, keep_newb) == (keep_l2, keep_dir002, keep_new), "KEEP set changed — investigate!"
    print("KEEP set intact. integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
