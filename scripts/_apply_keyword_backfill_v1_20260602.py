"""B1b keyword-backfill handler (per cluster) — reusable remediation handler.

Wraps the existing per-sub-group keyword discovery (API) + DB loader into one
orchestrated backfill: for each sub-group with is_relevant verses MISSING keywords,
run `_keyword_discovery_subgroup_v1` (API: 3-7 inner-being keywords per verse from
verse text + Pass A meaning) then `_load_keywords_to_db_v1` (-> verse_context.keywords).
Re-reports the B1b gap (verses missing keywords) before/after.

This handler only ORCHESTRATES the two proven scripts; it never calls the API or writes
the DB directly. Verses must already have analysis_note (Pass A meaning) — keywords are
derived from that, so run after B1a passes.

  python scripts/_apply_keyword_backfill_v1_20260602.py --cluster M08                 # dry: list sub-groups + missing counts
  python scripts/_apply_keyword_backfill_v1_20260602.py --cluster M08 --subgroup M08-A2 --dry-run-fetch  # plumbing test (no API)
  python scripts/_apply_keyword_backfill_v1_20260602.py --cluster M08 --subgroup M08-A2 --apply          # one sub-group (API)
  python scripts/_apply_keyword_backfill_v1_20260602.py --cluster M08 --apply                            # whole cluster (API)
"""
import argparse, glob, os, subprocess, sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
DISCOVER = os.path.join(REPO, "scripts", "_keyword_discovery_subgroup_v1_20260523.py")
LOADER = os.path.join(REPO, "scripts", "_load_keywords_to_db_v1_20260523.py")
DB = os.path.join(REPO, "database", "bible_research.db")


def subgroup_gaps(cluster):
    import sqlite3
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = c.execute(
        """SELECT cs.subgroup_code,
             SUM(CASE WHEN vc.is_relevant=1 THEN 1 ELSE 0 END) rel,
             SUM(CASE WHEN vc.is_relevant=1 AND (vc.keywords IS NULL OR TRIM(vc.keywords)='') THEN 1 ELSE 0 END) missing,
             SUM(CASE WHEN vc.is_relevant=1 AND (vc.analysis_note IS NULL OR TRIM(vc.analysis_note)='') THEN 1 ELSE 0 END) no_note
           FROM cluster_subgroup cs
           LEFT JOIN verse_context vc ON vc.cluster_subgroup_id=cs.id AND COALESCE(vc.delete_flagged,0)=0
           WHERE cs.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0
           GROUP BY cs.id HAVING missing>0 ORDER BY cs.subgroup_code""", (cluster,)).fetchall()
    c.close()
    return rows


def run(cmd):
    print(f"   $ {' '.join(os.path.basename(p) if os.path.isabs(p) else p for p in cmd)}")
    r = subprocess.run(cmd, cwd=REPO)
    if r.returncode != 0:
        raise SystemExit(f"ABORT: step exited {r.returncode}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--subgroup", default=None, help="limit to one sub-group (testing)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run-fetch", action="store_true", help="plumbing test: discovery fetch+count, no API")
    a = ap.parse_args()

    gaps = subgroup_gaps(a.cluster)
    if a.subgroup:
        gaps = [g for g in gaps if g["subgroup_code"] == a.subgroup]
    total = sum(g["missing"] for g in gaps)
    print(f"===== keyword backfill {a.cluster} =====")
    print(f"sub-groups with missing keywords: {len(gaps)} | total verses missing: {total}")
    for g in gaps:
        warn = f"  ⚠ {g['no_note']} missing analysis_note (run B1a first)" if g["no_note"] else ""
        print(f"  {g['subgroup_code']}: {g['missing']}/{g['rel']} missing{warn}")
    blocked = [g["subgroup_code"] for g in gaps if g["no_note"]]
    if blocked:
        print(f"\nBLOCKED (no meaning): {blocked} — B1a backfill must run before keyword backfill.")

    if not (a.apply or a.dry_run_fetch):
        print("\nDRY: pass --dry-run-fetch (plumbing, no API) or --apply (runs API discovery + load).")
        return

    for g in gaps:
        sg = g["subgroup_code"]
        if g["no_note"]:
            print(f"\n[{sg}] SKIP — has verses without meaning."); continue
        print(f"\n[{sg}] discovery {'(dry-run-fetch)' if a.dry_run_fetch else '(API)'} …")
        cmd = [PY, DISCOVER, "--cluster", a.cluster, "--subgroup", sg]
        if a.dry_run_fetch:
            cmd.append("--dry-run-fetch")
        run(cmd)
        if a.dry_run_fetch:
            continue
        # discovery names files wa-cluster-{SG}-keywords (SG already carries the cluster prefix)
        pat = os.path.join("Sessions", "Session_Clusters", a.cluster, "files phase 5",
                           f"wa-cluster-{sg}-keywords-v*.json")
        if not glob.glob(os.path.join(REPO, pat)):
            print(f"   (no keywords JSON produced for {sg}; skipping load)"); continue
        run([PY, LOADER, "--glob", pat])

    if a.apply:
        rem = subgroup_gaps(a.cluster)
        if a.subgroup:
            rem = [g for g in rem if g["subgroup_code"] == a.subgroup]
        print(f"\nAFTER: verses still missing keywords = {sum(g['missing'] for g in rem)} "
              f"(was {total}). Re-audit the cluster to confirm B1b.")


if __name__ == "__main__":
    main()
