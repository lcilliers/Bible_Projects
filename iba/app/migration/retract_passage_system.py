"""retract_passage_system.py — ONE-OFF: retire the `passage`/`verse_passage` system, both its
config registration AND its data (2026-07-26).

The researcher's own words: "the past use, and rules have moved on. The assembly of the passages
is no longer based on the same premise... the current data is no longer relevant and is getting in
the way... there is nothing to migrate from the old to the new. The effort of reconciling the old
data with potential new data is not worth it."

Mirrors `retract_candidate_system.py`'s shape (GOVERNANCE.md §15D) for the CONFIG side — same
`inactive` mechanism (bootstrap_inactive_column.py), same "deactivate, don't delete the config rows"
approach so `configmaint.validate` stops raising findings about config that's retired without
losing the rows. Goes one step further than that precedent on the DATA side: `passage`/
`verse_passage` are also soft-deleted (`deleted=1`) here, because — unlike candidate_seed/
span_candidate, which were left frozen in place pending the "new" candidate routines that still
read them — the researcher explicitly asked for the current passage data to stop being "in the way,"
not just frozen. A full verbatim CSV export was taken FIRST (see
reports/passage-system-retirement-record-20260726.md) so nothing is lost, only cleared from the
live path. No physical DROP TABLE — the schema stays for whatever the future passage design turns
out to be; only the rows are marked deleted, matching this app's own soft-delete convention.

SCOPE — enumerated by direct query before writing this, not guessed: 2 work packages, 2 steps,
5 settings (module=passage), 1 cfg_report row + its 2 sections, 4 on_fail rows, 2 write-grants,
18,504 passage rows, 24,763 verse_passage rows.

    python -m iba.app.migration.retract_passage_system
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

WORK_PACKAGES = ("build-passages", "passage-quality")
STEPS = ("passage.build", "passage.validate")


def _deactivate(conn: sqlite3.Connection, report: list[str], label: str,
                sql: str, params: tuple = ()) -> None:
    cur = conn.execute(sql, params)
    report.append(f"{label}: {cur.rowcount} row(s) set inactive")


def _soft_delete(conn: sqlite3.Connection, report: list[str], table: str) -> None:
    cur = conn.execute(f'UPDATE "{table}" SET deleted=1 WHERE deleted=0')
    report.append(f"{table}: {cur.rowcount} row(s) soft-deleted (deleted=1)")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    ph = lambda n: ",".join("?" * n)

    _deactivate(conn, report, "cfg_work_package",
               f"UPDATE cfg_work_package SET inactive=1 WHERE name IN ({ph(len(WORK_PACKAGES))})",
               WORK_PACKAGES)
    _deactivate(conn, report, "cfg_step",
               f"UPDATE cfg_step SET inactive=1 WHERE step IN ({ph(len(STEPS))})", STEPS)
    _deactivate(conn, report, "cfg_write_grant",
               "UPDATE cfg_write_grant SET inactive=1 WHERE writer='passage.build'")
    _deactivate(conn, report, "cfg_setting (module=passage)",
               "UPDATE cfg_setting SET inactive=1 WHERE module='passage'")
    _deactivate(conn, report, "cfg_report",
               f"UPDATE cfg_report SET inactive=1 WHERE step IN ({ph(len(STEPS))})", STEPS)
    _deactivate(conn, report, "cfg_report_section",
               f"UPDATE cfg_report_section SET inactive=1 WHERE step IN ({ph(len(STEPS))})", STEPS)
    _deactivate(conn, report, "cfg_on_fail",
               f"UPDATE cfg_on_fail SET inactive=1 WHERE step IN ({ph(len(STEPS))})", STEPS)

    _soft_delete(conn, report, "passage")
    _soft_delete(conn, report, "verse_passage")

    conn.commit()
    conn.close()

    print("passage-system retraction (2026-07-26 — record: "
         "reports/passage-system-retirement-record-20260726.md):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
