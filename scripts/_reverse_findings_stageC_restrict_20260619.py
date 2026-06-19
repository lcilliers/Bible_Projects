"""_reverse_findings_stageC_restrict_20260619.py — REVERSE Stage C (un-restrict the OLD findings).

Restores delete_flagged=0 and strips the appended "superseded…" marker from the rows Stage C restricted,
returning the old structure to fully visible. (Researcher: too early to disassemble the old structure.)
Stages A (new characteristics) and B (prose_section capture) are additive and left in place.

  python scripts/_reverse_findings_stageC_restrict_20260619.py --dry-run | --live
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
REASON = "superseded by 2026-06-19 NEW findings (11/7-char model, prose_section capture); retained, excluded from analysis"
SUFFIX = " | " + REASON


def strip(val):
    if val is None:
        return None
    if val == REASON:
        return None
    if val.endswith(SUFFIX):
        return val[: -len(SUFFIX)]
    return val  # marker absent — leave unchanged


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    targets = [
        ("cluster_finding", "notes",
         "delete_flagged=1 AND notes LIKE '%superseded by 2026-06-19 NEW findings%'"),
        ("finding", "source_legacy_ref",
         "delete_flagged=1 AND level='CLUSTER' AND source_legacy_ref LIKE '%superseded by 2026-06-19 NEW findings%'"),
        ("characteristic", "notes",
         "delete_flagged=1 AND source LIKE 'Pre-v2_6%' AND notes LIKE '%superseded by 2026-06-19 NEW findings%'"),
    ]
    total = 0
    for tbl, col, where in targets:
        rows = cur.execute(f"SELECT id, {col} AS v FROM {tbl} WHERE {where}").fetchall()
        print(f"{tbl}: {len(rows)} rows to un-restrict")
        total += len(rows)
        if a.live:
            for r in rows:
                cur.execute(f"UPDATE {tbl} SET delete_flagged=0, {col}=? WHERE id=?", (strip(r["v"]), r["id"]))
    if a.dry_run:
        print(f"\n[DRY-RUN] would un-restrict {total} rows. No changes written."); return 0
    conn.commit()
    print(f"\nLIVE: un-restricted {total} rows.")
    # verify: old findings active again, none left carrying the marker
    for tbl, _c, where in targets:
        left = cur.execute(f"SELECT COUNT(*) FROM {tbl} WHERE {where}").fetchone()[0]
        print(f"   {tbl}: still-restricted-with-marker = {left} (expect 0)")
    print("active old cluster_finding (M01/M02 consolidated):",
          cur.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code IN ('M01','M02') AND source_file LIKE 'WA-M0%-consolidated-findings-v1-20260516%' AND COALESCE(delete_flagged,0)=0").fetchone()[0], "(expect 1118)")
    print("active legacy characteristics (M01/M02):",
          cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code IN ('M01','M02') AND source LIKE 'Pre-v2_6%' AND COALESCE(delete_flagged,0)=0").fetchone()[0], "(expect 13)")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
