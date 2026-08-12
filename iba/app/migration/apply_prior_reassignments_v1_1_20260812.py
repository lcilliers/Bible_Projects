"""apply_prior_reassignments_v1_1_20260812.py — ONE-OFF: process the researcher's cluster
REASSIGNMENT round (`wa-global-prior-reassignments-v1_1-20260811.json`) into the DB — the
companion to `apply_cluster_alloc_v1_3_20260812.py`, which was additions-only. This one revises
218 of the 2,801 prior old-system-migration `cluster_strong` rows.

Validated before writing (session record, not re-checked here): meta.count (218) matches the
actual `moves` array length; the reason tally matches meta.breakdown exactly; every `from_cluster`
instance genuinely exists as a live `cluster_strong` row (0 missing); every `to_cluster` is a known
cluster including the newly-added T3 (0 unknown); stepGloss/language on every move matches the
live `strong` table (0 mismatches). 15 `(strong, T3)` target pairs are duplicated WITHIN the file
— expected, per the source's own note: a multi-cluster strong (one T2 instance + one FLAG
instance) both move to T3, which must collapse to ONE active `cluster_strong` row, not two.

Mechanism, per the codebase's own "supersede, never overwrite in place" convention (same shape as
`verse_lexical`'s write_readings_for_span): for each move, the (strong, from_cluster) row is
soft-deleted; a new (strong, to_cluster) row is inserted — but only if a live row for that exact
(strong, to_cluster) pair doesn't already exist (handles the 15 within-file duplicates AND the
case where the target already legitimately holds a row for other reasons).

    python -m iba.app.migration.apply_prior_reassignments_v1_1_20260812 --dry-run
    python -m iba.app.migration.apply_prior_reassignments_v1_1_20260812 --apply
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
MOVES_FILE = DOCS / "wa-global-prior-reassignments-v1_1-20260811.json"
SOURCE_TAG = "llm-reassignment-v1_1-20260811"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    grant = conn.execute(
        "SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name='cluster_strong' "
        "AND inactive=0").fetchone()
    if not grant:
        print("write-grant violation: 'migration' may not write 'cluster_strong'", file=sys.stderr)
        return 1

    moves = json.loads(MOVES_FILE.read_text(encoding="utf-8"))["moves"]

    n_source_missing, n_target_created, n_target_deduped = 0, 0, 0
    seen_targets_this_run: set[tuple[str, str]] = set()
    for m in moves:
        src = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (m["strongNumber"], m["from_cluster"])).fetchone()
        if not src:
            n_source_missing += 1
            continue
        key = (m["strongNumber"], m["to_cluster"])
        already_live = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            key).fetchone()
        if already_live or key in seen_targets_this_run:
            n_target_deduped += 1
        else:
            n_target_created += 1
        seen_targets_this_run.add(key)

    print(f"moves: {len(moves)}")
    print(f"source row missing (would skip, none expected): {n_source_missing}")
    print(f"target rows to create: {n_target_created}")
    print(f"target rows deduped (already live or duplicate within this file): {n_target_deduped}")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write (soft-delete source, insert deduped target).")
        conn.close()
        return 0

    now = _now()
    n_deleted, n_inserted, n_skipped_dup, n_skipped_missing = 0, 0, 0, 0
    written_targets: set[tuple[str, str]] = set()
    for m in moves:
        src = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (m["strongNumber"], m["from_cluster"])).fetchone()
        if not src:
            n_skipped_missing += 1
            continue
        conn.execute(
            "UPDATE cluster_strong SET deleted=1 WHERE strong=? AND cluster_code=? AND deleted=0",
            (m["strongNumber"], m["from_cluster"]))
        n_deleted += 1

        key = (m["strongNumber"], m["to_cluster"])
        already_live = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0", key
        ).fetchone()
        if already_live or key in written_targets:
            n_skipped_dup += 1
            continue
        conn.execute(
            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
            "confidence, operation, alt_clusters, review_flag, rationale) "
            "VALUES (?,?,?,?,0,?,?,?,?,?)",
            (m["strongNumber"], m["to_cluster"], SOURCE_TAG, now,
             None, 1, json.dumps([]), 0, m["reason"]))
        n_inserted += 1
        written_targets.add(key)

    conn.commit()
    conn.close()
    print(f"\napplied: {n_deleted} source row(s) soft-deleted, {n_inserted} target row(s) "
          f"inserted, {n_skipped_dup} target(s) deduped, {n_skipped_missing} source(s) missing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
