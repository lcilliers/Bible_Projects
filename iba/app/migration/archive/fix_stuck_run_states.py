"""fix_stuck_run_states.py — ONE-OFF: retroactively correct run.state for runs stuck by the
run.py completion bug fixed 2026-07-22 (see migration/add_work_package_chained_column.py).

Scope, deliberately narrow: only touches a run row where
  - its work package is NON-chained (cfg_work_package.chained=0 — configuration-maintenance,
    reports, candidate-quality, passage-quality, candidate-curation), AND
  - state is 'running' or 'paused', AND
  - no escalation for that run_id is still 'raised' (nothing is actually pending).

For a non-chained package, resolving its one step IS finishing the whole run — there is no
ambiguity. Does NOT touch chained packages (new-word, set-candidates, build-passages): a chained
run stuck mid-sequence may genuinely be an abandoned/incomplete run (e.g. a standalone
candidate.seed test that was never meant to continue to candidate.set), and relabelling it 'done'
would misrepresent what actually happened. Those are surfaced instead in the retention/status
report (lib/retention.py) as archival candidates, for a real decision, not silently reclassified.

    python -m iba.app.migration.fix_stuck_run_states --dry-run
    python -m iba.app.migration.fix_stuck_run_states
"""

from __future__ import annotations

import argparse
import datetime
import sys

from ..lib.cfg import DB_PATH
import sqlite3


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _eligible(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    return conn.execute("""
        SELECT r.id, r.run_id, r.work_package, r.state, r.resume_point, r.outcome FROM run r
        JOIN cfg_work_package wp ON wp.name = r.work_package
        WHERE wp.chained = 0 AND r.state IN ('running','paused')
        AND NOT EXISTS (SELECT 1 FROM escalation e WHERE e.run_id = r.run_id AND e.state='raised')
    """).fetchall()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    rows = _eligible(conn)
    print(f"{len(rows)} run(s) eligible for retroactive 'done' correction:")
    for r in rows:
        print(f"  {r['run_id']:44} {r['work_package']:26} was {r['state']}")

    if a.dry_run:
        print("\n--dry-run: no changes made.")
        conn.close()
        return 0

    now = _now()
    for r in rows:
        outcome = r["outcome"] or "retroactively corrected 2026-07-22: run.state was stuck at " \
                                   f"{r['state']!r} due to the completion-detection bug (fixed in " \
                                   "run.py) — every escalation on this run was already answered."
        conn.execute("UPDATE run SET state='done', ended_at=?, outcome=? WHERE id=?",
                     (now, outcome, r["id"]))
    conn.commit()
    print(f"\ncorrected {len(rows)} run(s) to state='done'.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
