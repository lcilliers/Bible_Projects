"""B1a meaning-backfill handler (per cluster) — reusable remediation handler.

Wraps the existing Pass A runner (_run_passa_via_api_v1: for each is_relevant verse
lacking analysis_note, AI writes a one-line meaning, +keywords when available) and the
patch applier (apply_session_patch.py applies the VCREVISE patch). Re-reports the B1a gap
(is_relevant verses missing analysis_note) before/after.

This handler only ORCHESTRATES the two proven scripts; it never calls the API or writes
the DB directly. Run before B1b keyword-backfill (keywords derive from meaning).

  python scripts/_apply_meaning_backfill_v1_20260602.py --cluster M20                 # dry: count gap
  python scripts/_apply_meaning_backfill_v1_20260602.py --cluster M20 --dry-run-fetch # plumbing (no API)
  python scripts/_apply_meaning_backfill_v1_20260602.py --cluster M20 --apply         # Pass A (API) + apply patch
"""
import argparse, glob, os, sqlite3, subprocess, sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
PASSA = os.path.join(REPO, "scripts", "_run_passa_via_api_v1_20260515.py")
APPLY = os.path.join(REPO, "scripts", "apply_session_patch.py")
DB = os.path.join(REPO, "database", "bible_research.db")
TSUB = "(SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0)"


def gap(cluster):
    c = sqlite3.connect(DB)
    n = c.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN " + TSUB +
                  " AND is_relevant=1 AND COALESCE(delete_flagged,0)=0 AND (analysis_note IS NULL OR TRIM(analysis_note)='')",
                  (cluster,)).fetchone()[0]
    c.close()
    return n


def run(cmd):
    print(f"   $ {' '.join(os.path.basename(p) if os.path.isabs(p) else p for p in cmd)}")
    r = subprocess.run(cmd, cwd=REPO)
    if r.returncode != 0:
        raise SystemExit(f"ABORT: step exited {r.returncode}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run-fetch", action="store_true")
    a = ap.parse_args()
    before = gap(a.cluster)
    print(f"===== meaning backfill {a.cluster} =====")
    print(f"is_relevant verses missing analysis_note (B1a gap): {before}")
    if before == 0:
        print("Nothing to backfill."); return
    if not (a.apply or a.dry_run_fetch):
        print("\nDRY: --dry-run-fetch (plumbing, no API) or --apply (Pass A API + apply patch).")
        return

    cmd = [PY, PASSA, "--m-cluster", a.cluster]
    if a.dry_run_fetch:
        cmd.append("--dry-run-fetch")
    print("\nPass A " + ("(dry-run-fetch)" if a.dry_run_fetch else "(API)") + " …")
    run(cmd)
    if a.dry_run_fetch:
        return

    pat = os.path.join("Sessions", "Session_Clusters", a.cluster, f"wa-cluster-{a.cluster}-patch-passa-meanings-v*.json")
    hits = sorted(glob.glob(os.path.join(REPO, pat)))
    if not hits:
        print(f"   (no Pass A patch produced for {a.cluster}; nothing to apply)"); return
    patch = hits[-1]
    print(f"\nApply VCREVISE patch {os.path.basename(patch)} …")
    run([PY, APPLY, patch])
    after = gap(a.cluster)
    print(f"\nAFTER: B1a gap {before} -> {after}. Re-audit; then run keyword backfill for any remaining B1b.")


if __name__ == "__main__":
    main()
