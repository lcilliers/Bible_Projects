"""Bundle backfill of finding_citation rows for all closed clusters.

Per researcher direction 2026-05-27: the finding_citation table was built (M52)
but only populated for M10. Backfill structured citation extraction across all
remaining closed clusters (and M05, currently 'Ready for re-analysis' — to
test whether its findings carry the citation network we expected).

The two extractors are idempotent per (source_table, source_id, cluster scope):
on each run they delete existing rows in scope and re-insert. Safe to re-run.

Pipeline per cluster:
  1. _extract_finding_citations_v1 --cluster {code} [--live]
     - Parses cluster_finding.finding_text + cluster_observation.description
     - Extracts: verse refs, Strong's, CHAR-N cross-references
  2. _enrich_finding_citations_with_vcg_v1 --cluster {code} [--live]
     - Derives VCG citations from the verse citations via verse→VCG join
     - Independent of citation format in finding text

This script orchestrates both per cluster, sequentially.
"""
from __future__ import annotations
import argparse, io, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent

# Closed clusters needing backfill. M10 excluded (already done).
# M05 included per researcher direction — its 'Ready for re-analysis' status
# doesn't prevent citation extraction of its existing cluster_finding rows.
CLUSTERS = [
    "M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09",
    "M10b", "M10c", "M15", "M20", "M26", "M39", "M46",
]

EXTRACTOR = REPO / "scripts" / "_extract_finding_citations_v1_20260525.py"
ENRICHER = REPO / "scripts" / "_enrich_finding_citations_with_vcg_v1_20260525.py"


def run_step(script: Path, cluster: str, live: bool) -> int:
    """Run a sub-script; return exit code. Stream stdout/stderr to console."""
    args = [sys.executable, str(script), "--cluster", cluster]
    if live:
        args.append("--live")
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    # Print short summary; full output preserved if non-zero
    if result.returncode != 0:
        print(f"  STDOUT:\n{result.stdout}")
        print(f"  STDERR:\n{result.stderr}")
    else:
        # Print last 5 lines of stdout for visibility
        lines = result.stdout.strip().split("\n")
        for ln in lines[-5:]:
            print(f"    {ln}")
    return result.returncode


def main(live: bool) -> int:
    mode = "LIVE" if live else "DRY-RUN"
    print(f"=== Bundle backfill finding_citation — mode={mode} ===")
    print(f"Clusters in scope ({len(CLUSTERS)}): {CLUSTERS}")
    print()

    failures = []
    started = datetime.now(timezone.utc)
    for i, cluster in enumerate(CLUSTERS, start=1):
        print(f"[{i}/{len(CLUSTERS)}] {cluster} — step 1: extract verse/strongs/cross_char citations")
        rc = run_step(EXTRACTOR, cluster, live)
        if rc != 0:
            failures.append((cluster, "extract", rc))
            print(f"  FAILED: extract for {cluster} (rc={rc})")
            continue
        print(f"[{i}/{len(CLUSTERS)}] {cluster} — step 2: enrich VCG citations from verses")
        rc = run_step(ENRICHER, cluster, live)
        if rc != 0:
            failures.append((cluster, "enrich", rc))
            print(f"  FAILED: enrich for {cluster} (rc={rc})")
            continue
        print()

    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print()
    print(f"=== Bundle complete — elapsed {elapsed:.1f}s ===")
    if failures:
        print(f"FAILURES ({len(failures)}):")
        for cluster, step, rc in failures:
            print(f"  {cluster}: {step} failed with rc={rc}")
        return 1
    print(f"All {len(CLUSTERS)} clusters processed successfully.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
