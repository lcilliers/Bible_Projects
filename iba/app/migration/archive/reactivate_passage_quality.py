"""reactivate_passage_quality.py — ONE-OFF: bring `passage-quality`/`passage.validate` back as a
book-scoped debate-range size check, narrowly, without resurrecting `build-passages`/`passage.build`
(2026-07-28).

`retract_passage_system.py` (2026-07-26) deactivated the whole passage system in one pass — both
`build-passages`/`passage.build` (raw char-continuity span generation) and `passage-quality`/
`passage.validate` (verse-count distribution check over whatever `passage` rows exist) — because
the raw-generation premise itself had changed and its data was "in the way." That reasoning does
NOT apply to `passage.validate` on its own: it doesn't generate or depend on raw spans, it just
reports on whatever live `passage` rows exist, and today those rows ARE the debate-range units
(`report.passage_debate` upserts one per debated range — see `passagetrack.py`; Daniel's 189 old
raw rows stayed `deleted=1` from the 2026-07-26 retraction, its 16 live rows are exactly its 16
debate ranges, verse_count 7-45).

This closes gap 2 of the plan approved 2026-07-28 (~/.claude/plans/twinkly-orbiting-dawn.md):
reactivating `passage.validate` gives
a real, already-built, already-escalating check on whether a chosen debate range's size looks like
an outlier — something `report.passage_debate` itself never checked before writing a scaffold.

SCOPE — enumerated by direct query before writing this, not guessed (mirrors the discipline
`retract_passage_system.py` itself used): 1 work package (`passage-quality`), 1 step
(`passage.validate`), 1 setting (`passage.quality_report_path` — module=passage's OTHER 4 settings
belong to `passage.build`/`build-passages` and stay `inactive=1`, since `review_over=10` is
calibrated for 1-3-verse raw spans, not chapter-length debate ranges, and reactivating it as-is
would flag every Daniel-scale debate), 1 `cfg_report` row, 2 `cfg_report_section` rows (`dist`,
`by_book`), 3 `cfg_on_fail` rows (`findings-rejected`, `needs-review`, `needs-revision`). No
`cfg_write_grant` row exists for `passage.validate` (it's read-only, per its own docstring) — none
to reactivate. `build-passages`/`passage.build`/`passage.cross_chapter`/`passage.default_rule`/
`passage.min_shared_strongs`/`passage.review_over` are deliberately left untouched.

    python -m iba.app.migration.reactivate_passage_quality
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

WORK_PACKAGE = "passage-quality"
STEP = "passage.validate"
SETTING = "passage.quality_report_path"


def _activate(conn: sqlite3.Connection, report: list[str], label: str,
             sql: str, params: tuple = ()) -> None:
    cur = conn.execute(sql, params)
    report.append(f"{label}: {cur.rowcount} row(s) set active (inactive=0)")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _activate(conn, report, "cfg_work_package",
             "UPDATE cfg_work_package SET inactive=0 WHERE name=?", (WORK_PACKAGE,))
    _activate(conn, report, "cfg_step",
             "UPDATE cfg_step SET inactive=0 WHERE step=?", (STEP,))
    _activate(conn, report, "cfg_setting (passage.quality_report_path only)",
             "UPDATE cfg_setting SET inactive=0 WHERE key=?", (SETTING,))
    _activate(conn, report, "cfg_report",
             "UPDATE cfg_report SET inactive=0 WHERE step=?", (STEP,))
    _activate(conn, report, "cfg_report_section",
             "UPDATE cfg_report_section SET inactive=0 WHERE step=?", (STEP,))
    _activate(conn, report, "cfg_on_fail",
             "UPDATE cfg_on_fail SET inactive=0 WHERE step=?", (STEP,))

    conn.commit()
    conn.close()

    print("passage-quality reactivation (2026-07-28, scoped — build-passages/passage.build "
         "and its 4 other settings stay inactive):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
