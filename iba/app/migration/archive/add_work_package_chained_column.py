"""add_work_package_chained_column.py — ONE-OFF: add cfg_work_package.chained, fixing the
run.state completion bug found 2026-07-22.

Root cause: run.py's dispatcher marked a run 'done' only when the current step was the LAST step
in its work package's cfg_step sequence. That's correct for a work package that always runs its
whole sequence under one run_id in one PS invocation (new-word, set-candidates, build-passages —
each has a PowerShell `foreach` that chains every step). It's wrong for a work package whose steps
are each invoked INDEPENDENTLY, one per run_id (configuration-maintenance's validate/propose/report,
reports' report.word/validation.word/validation.book) — a standalone step can never BE the last
step in its multi-step registration, so the run stayed 'paused'/'running' forever even after fully
resolving. Confirmed live: 185 run rows stuck this way.

This column lets the dispatcher (run.py) tell the two shapes apart: chained=1 packages keep the
existing "done when last-in-sequence" logic; chained=0 packages are marked done on their own first
'ok'/'report-continue'/'self-heal' outcome, regardless of ordinal position.

NOTE: cfg_work_package's schema lives in cfgload.py's CFG_DDL (a cfg_* table's schema is code, not
config-content, per cfgload.py's own docstring) and is normally rebuilt from config/run.json on
reload — but that JSON seed no longer exists at its live path (only iba/app/config/archive/,
reference-only). A full cfgload.load() cannot currently run. This migration ALTERs the live table
directly; cfgload.py's CFG_DDL is updated to match so a *future* restored JSON seed round-trips
correctly, but populating `chained` via a JSON reload needs run.json to carry a `chained` field per
work package first — a separate, not-yet-done piece, noted honestly rather than silently assumed.

    python -m iba.app.migration.add_work_package_chained_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# the only packages whose PS wrapper chains every step under one run_id (verified by reading
# each Xxx.ps1: New-Word.ps1, Set-Candidates.ps1, Build-Passages.ps1 all `foreach` the full
# sequence; Config-Maintenance.ps1/Candidate-Quality.ps1/Passage-Quality.ps1/Reports.ps1/
# Candidate-Curate.ps1 each invoke exactly one step per run_id, independently selected by -Step)
CHAINED = {"new-word", "set-candidates", "build-passages"}


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_work_package)")}
    if "chained" not in cols:
        conn.execute("ALTER TABLE cfg_work_package ADD COLUMN chained INTEGER DEFAULT 0")
        print("cfg_work_package.chained column added")
    else:
        print("cfg_work_package.chained already present")

    packages = [r[0] for r in conn.execute("SELECT name FROM cfg_work_package")]
    for name in packages:
        val = 1 if name in CHAINED else 0
        conn.execute("UPDATE cfg_work_package SET chained=? WHERE name=?", (val, name))
    conn.commit()

    print("\ncfg_work_package.chained:")
    for r in conn.execute("SELECT name, chained FROM cfg_work_package ORDER BY name"):
        print(f"  {r[0]:26} chained={r[1]}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
