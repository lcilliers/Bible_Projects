"""apply_cluster_alloc_v1_3_20260812.py — ONE-OFF: process the researcher's LLM-assisted cluster
allocation round into the DB.

Two source files (`iba/docs/cluster assignment process/`):
  wa-global-t3-cluster-record-v1_0-20260811.json         -- new cluster 'T3' (Operations) to add
  wa-global-cluster-alloc-final-v1_3-20260811.json       -- 1,612 assignments for the exact set of
                                                             word-origin strongs that had no
                                                             cluster (strong_without_cluster.csv,
                                                             report.cluster, this session)

Validated before writing anything (session record, not re-checked here): every assignment's
strongNumber is exactly the exported gap-list set (0 extra, 0 missing); every cluster_code used is
either an existing live cluster or 'T3'; confidence is a clean 3-value enum; the assignment tally
matches meta.counts_by_cluster exactly; review_flag=true exactly equals the low-confidence count
(574); stepGloss/language/count on every row match the live `strong` table exactly (0 mismatches).

This is ADDITIONS ONLY — every target strong currently has zero cluster_strong rows (confirmed:
the source scope IS the gap list). No existing cluster_strong row is touched. Re-assignment of any
of the prior 2,801 old-system-migration rows is explicitly NOT part of this script (a separate,
not-yet-provided companion file per the source's own meta.prior_output_reference).

    python -m iba.app.migration.apply_cluster_alloc_v1_3_20260812 --dry-run
    python -m iba.app.migration.apply_cluster_alloc_v1_3_20260812 --apply
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

DOCS = pathlib.Path("iba/docs/cluster assignment process")
T3_FILE = DOCS / "wa-global-t3-cluster-record-v1_0-20260811.json"
ALLOC_FILE = DOCS / "wa-global-cluster-alloc-final-v1_3-20260811.json"
SOURCE_TAG = "llm-allocation-v1_3-20260811"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    for t in ("cluster", "cluster_strong"):
        grant = conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name=? AND inactive=0",
            (t,)).fetchone()
        if not grant:
            print(f"write-grant violation: 'migration' may not write {t!r}", file=sys.stderr)
            return 1

    t3 = json.loads(T3_FILE.read_text(encoding="utf-8"))["cluster"]
    alloc = json.loads(ALLOC_FILE.read_text(encoding="utf-8"))
    assignments = alloc["assignments"]

    t3_exists = conn.execute(
        "SELECT 1 FROM cluster WHERE cluster_code=? AND deleted=0", (t3["cluster_code"],)).fetchone()
    already_assigned = conn.execute(
        "SELECT COUNT(*) n FROM cluster_strong cs WHERE cs.deleted=0 AND cs.strong IN "
        f"({','.join('?' * len(assignments))})",
        [x["strongNumber"] for x in assignments]).fetchone()["n"]

    print(f"T3 cluster: {'already present, no-op' if t3_exists else 'will be inserted'} "
          f"({t3['cluster_code']} — {t3['short_name']})")
    print(f"assignments to insert: {len(assignments)}")
    print(f"of those, already carrying a cluster_strong row (would be duplicates, skipped): "
          f"{already_assigned}")
    conf_counts = {}
    for x in assignments:
        conf_counts[x["confidence"]] = conf_counts.get(x["confidence"], 0) + 1
    print(f"by confidence: {conf_counts}")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write.")
        conn.close()
        return 0

    if not t3_exists:
        conn.execute(
            "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
            "VALUES (?,?,?,?,?)",
            (t3["cluster_code"], t3["short_name"], t3["description"], t3["gloss"], t3["deleted"]))
        print(f"inserted cluster {t3['cluster_code']}")

    now = _now()
    n_inserted, n_skipped = 0, 0
    for x in assignments:
        exists = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND deleted=0", (x["strongNumber"],)
        ).fetchone()
        if exists:
            n_skipped += 1
            continue
        conn.execute(
            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
            "confidence, operation, alt_clusters, review_flag, rationale) "
            "VALUES (?,?,?,?,0,?,?,?,?,?)",
            (x["strongNumber"], x["cluster_code"], SOURCE_TAG, now,
             x["confidence"], 1 if x["operation"] else 0, json.dumps(x["alt_clusters"]),
             1 if x["review_flag"] else 0, x["rationale"]))
        n_inserted += 1

    conn.commit()
    conn.close()
    print(f"\napplied: {n_inserted} cluster_strong row(s) inserted, {n_skipped} skipped "
          f"(already had one).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
