"""reconcile_daniel_debate_paths.py — ONE-OFF: fix five `passage.debate_path` rows for Daniel that
point to files no longer on disk (2026-07-28).

Found running `report.whole_book_read` (§32) against Daniel for the first time: five of the
sixteen tracked `debate_path` values (`Dan 1:1-7`, `1:7-21`, `2:1-16`, `2:17-30`, `2:31-49` — the
four originally hand-authored debates from before `report.passage_debate` was registered, per
§28's note, plus `2:31-49`) point at filenames that no longer exist. Those files were revised
(v1.1 -> v1.2 for the first four; `2:31-49`'s tracked path carried no version suffix at all) after
whatever pass first populated `debate_path` for them, and the column was never updated to follow.
Not a bug in `report.passage_debate`/`passagetrack.py` (both keep `debate_path` current on every
run that goes through them) — these five simply predate that mechanism.

Correct current filenames confirmed by direct `Glob` against the live folder before writing this
(exactly one non-archived match each, not guessed):

    Dan 1:1-7   -> WA-dan-1-1-7-debate-v1.2-2026-07-27.md
    Dan 1:7-21  -> WA-dan-1-7-21-debate-v1.2-2026-07-27.md
    Dan 2:1-16  -> WA-dan-2-1-16-debate-v1.2-2026-07-27.md
    Dan 2:17-30 -> WA-dan-2-17-30-debate-v1.2-2026-07-27.md
    Dan 2:31-49 -> WA-dan-2-31-49-debate-v1.1-2026-07-27.md

Updates ONLY `debate_path` (and stamps `debate_written_at` to record when the pointer was
corrected) for these five exact rows, matched by book/start/end, not a blanket rename/replace —
`debate_status` (already `filled`, correctly) is untouched.

    python -m iba.app.migration.reconcile_daniel_debate_paths
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH

FOLDER = "iba\\app\\verse-analysis\\Daniel\\"

FIXES = [
    # (start_chapter, start_verse, end_chapter, end_verse, correct_filename)
    (1, 1, 1, 7, "WA-dan-1-1-7-debate-v1.2-2026-07-27.md"),
    (1, 7, 1, 21, "WA-dan-1-7-21-debate-v1.2-2026-07-27.md"),
    (2, 1, 2, 16, "WA-dan-2-1-16-debate-v1.2-2026-07-27.md"),
    (2, 17, 2, 30, "WA-dan-2-17-30-debate-v1.2-2026-07-27.md"),
    (2, 31, 2, 49, "WA-dan-2-31-49-debate-v1.1-2026-07-27.md"),
]


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for sc, sv, ec, ev, filename in FIXES:
        new_path = FOLDER + filename
        cur = conn.execute(
            "UPDATE passage SET debate_path=?, debate_written_at=? WHERE book='Dan' AND "
            "start_chapter=? AND start_verse=? AND end_chapter=? AND end_verse=? AND deleted=0 "
            "AND debate_status='filled'",
            (new_path, _now(), sc, sv, ec, ev))
        report.append(f"Dan {sc}:{sv}-{ec}:{ev} -> {filename}: {cur.rowcount} row(s) updated")

    conn.commit()
    conn.close()

    print("Daniel debate_path reconciliation (2026-07-28):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
