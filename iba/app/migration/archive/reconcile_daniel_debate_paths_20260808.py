"""reconcile_daniel_debate_paths_20260808.py — ONE-OFF: fix 3 `passage.debate_path` rows left
stale by the 2026-08-08 book-report-filing-convention fix (BUILD.md, same day).

Trigger: `build_debate_report.py`/`handlers/operations.py` had been filing debate/reconciliation
reports flat under `governance.oneoff_report_dir` (`iba/app/reports/`) instead of the book-scoped
`report.verse_analysis_output_dir/<book_label>/` convention every sibling book tool uses — a real
filing bug (researcher: "the filing for all Book related operations should be in the
iba/app/verse-analysis/[book] folders where it has been since we started"), not a deliberate
design difference; see `_write_reconciliation_report`'s docstring and `build_debate_report.py`'s
"Filing corrected 2026-08-08" note. Fixed going forward; this script is the retrofit half —
refiling the pre-existing misfiled files (via `git mv`, same session) leaves the DB's tracked
`passage.debate_path` pointing at the old, now-empty location for the 3 rows whose debate report
was actually still live (not yet superseded) at refile time.

Correct current paths confirmed by direct listing before writing this (each file physically present
at the new path, refiled by `git mv` in this same session, not guessed):

    passage 37464 (Dan 8:1-27,  debate_status=complete) -> dan-8-debate-report-20260806.md
    passage 37465 (Dan 8:1-27,  debate_status=complete) -> dan-8-debate-report-20260806-v2.md
    passage 37467 (Dan 1:1-21,  debate_status=complete) -> dan-1-debate-report-20260807-v2.md

Deliberately NOT touched: passage 37463 (Dan 8:1, debate_status=complete, debate_path=
`iba\\app\\reports\\dan-8-1-1-debate-report-20260806-v3.md`) — that file does not exist anywhere on
disk AND has no trace in `git log --all`, so it predates this session's refile entirely; it is a
separate, pre-existing stale pointer, not something this refile caused, and correcting it is a
judgement call (delete the passage row as a stale test artifact, or re-render) left to the
researcher, not decided here.

    python -m iba.app.migration.reconcile_daniel_debate_paths_20260808
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH

FOLDER = "iba\\app\\verse-analysis\\Daniel\\"

FIXES = [
    # (passage_id, correct_filename)
    (37464, "dan-8-debate-report-20260806.md"),
    (37465, "dan-8-debate-report-20260806-v2.md"),
    (37467, "dan-1-debate-report-20260807-v2.md"),
]


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for passage_id, filename in FIXES:
        new_path = FOLDER + filename
        cur = conn.execute(
            "UPDATE passage SET debate_path=?, debate_written_at=? WHERE id=? AND deleted=0",
            (new_path, _now(), passage_id))
        report.append(f"passage {passage_id} -> {filename}: {cur.rowcount} row(s) updated")

    conn.commit()
    conn.close()

    print("Daniel debate_path reconciliation (2026-08-08, post-refile):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
