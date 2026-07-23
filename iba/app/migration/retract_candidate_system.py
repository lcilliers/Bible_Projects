"""retract_candidate_system.py — ONE-OFF: mark the entire candidate-handling system inactive
(escalations #306/#310, 2026-07-23).

The researcher's own words: "the entire working around the candidate rules and handling the
candidates will change[,] the comes from a substantial mess up over the past few days that will
all be retracted in due course." Confirmed via escalation #306 that cfg_candidate_rule (flagged
"makes no sense, assume unused") is in fact load-bearing — read by BOTH the old `candidate.seed`
AND the new `candidate.load`/`candidate.curate` (handlers/candidate.py: seed()'s accept/reject
kinds are seed-only, but _resolve_lemma()'s synonym kind and _ib_referent()'s body-part/
other-being kinds are shared with the new routines). So this is not a delete (would break the
"new" routines too) — it is a full DEACTIVATION of the whole candidate surface, old and new alike,
ahead of the coming replacement, using escalation #310's new `inactive` column (see
bootstrap_inactive_column.py, run first) so configmaint.validate stops raising findings about
config that's about to be thrown away, without losing the rows.

SCOPE — every row genuinely part of the candidate system, enumerated by direct query (not
guessed), covering 4 work packages, 6 steps, 5 write-grants, 7 settings, 3 cfg_report rows + their
10 sections + 5 CSV pairings, 10 on_fail rows, 4 enum groups (15 values total), and all 289
cfg_candidate_rule rows:

    python -m iba.app.migration.retract_candidate_system
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

WORK_PACKAGES = ("set-candidates", "seed-candidate-report", "candidate-quality",
                  "candidate-curation")
STEPS = ("candidate.seed", "candidate.set", "report.seed_candidate", "candidate.validate",
          "candidate.curate", "candidate.load")
REPORT_STEPS = ("candidate.load", "candidate.validate", "report.seed_candidate")
ENUM_GROUPS = ("candidate_decision", "candidate_ib_referent", "candidate_source",
               "candidate_step_status")


def _deactivate(conn: sqlite3.Connection, report: list[str], label: str,
                sql: str, params: tuple = ()) -> None:
    cur = conn.execute(sql, params)
    report.append(f"{label}: {cur.rowcount} row(s) set inactive")


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
               "UPDATE cfg_write_grant SET inactive=1 WHERE writer LIKE 'candidate%'")
    _deactivate(conn, report, "cfg_setting (module=candidate)",
               "UPDATE cfg_setting SET inactive=1 WHERE module='candidate'")
    _deactivate(conn, report, "cfg_report",
               f"UPDATE cfg_report SET inactive=1 WHERE step IN ({ph(len(REPORT_STEPS))})",
               REPORT_STEPS)
    _deactivate(conn, report, "cfg_report_section",
               f"UPDATE cfg_report_section SET inactive=1 WHERE step IN ({ph(len(REPORT_STEPS))})",
               REPORT_STEPS)
    _deactivate(conn, report, "cfg_report_csv_table",
               f"UPDATE cfg_report_csv_table SET inactive=1 WHERE step IN ({ph(len(REPORT_STEPS))})",
               REPORT_STEPS)
    _deactivate(conn, report, "cfg_on_fail",
               f"UPDATE cfg_on_fail SET inactive=1 WHERE step IN ({ph(len(STEPS))})", STEPS)
    _deactivate(conn, report, "cfg_enum (candidate groups)",
               f"UPDATE cfg_enum SET inactive=1 WHERE name IN ({ph(len(ENUM_GROUPS))})",
               ENUM_GROUPS)
    _deactivate(conn, report, "cfg_candidate_rule (all rows)",
               "UPDATE cfg_candidate_rule SET inactive=1")

    conn.commit()
    conn.close()

    print("candidate-system retraction (escalations #306/#310):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
