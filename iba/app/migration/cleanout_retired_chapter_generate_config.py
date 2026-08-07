"""cleanout_retired_chapter_generate_config.py — hard-deletes the dangling `report.passage_debate`/
`passage.debate_sync` config references left behind after their steps (and the `chapter-generate`/
`passage-debate-sync` work packages carrying them) were retired via `configmaint.propose`
(escalations #543/#545/#544/#546, approved and applied 2026-08-07).

Same carve-out class and precedent as `cleanout_retired_verse_span_meaning_config.py`
(2026-08-06, escalation #445): `inactive=1` on the step/work-package rows themselves leaves their
own downstream references (cfg_on_fail, cfg_report, cfg_report_section, cfg_write_grant) still
naming them, and `configmaint.validate` treats "references a step with no active registration
anywhere" as a structural error, not merely advisory. Direct researcher authorization for the
retirement itself (the just-approved #543-546 proposals) is treated as the up-front approval for
this mechanical follow-through, the same way it was for verse_span_meaning's cleanup — this is not
a fresh design decision, it's the dangling-reference half of a change already approved.

Hard-deletes (this app's convention for "genuinely retired, not merely disabled" cfg_* rows):
- cfg_on_fail: 2 rows for step='report.passage_debate', 2 rows for step='passage.debate_sync'
- cfg_report: 1 row for step='report.passage_debate'
- cfg_report_section: 8 rows for step='report.passage_debate'
- cfg_write_grant: 2 rows for writer='report.passage_debate'

Deliberately NOT touched: `cfg_column.filled_by` values on `passage`/`verse_passage` that mention
`report.passage_debate` — checked directly, these already correctly describe it as one of two
historical writers ("report.passage_debate (legacy, passage.rule IS NULL) ... or report.debate
(new-model ...)"), not asserting a live step exists. Left for a follow-up only if
`configmaint.validate`'s advisory `stale_filled_by` check actually flags them post-cleanup — not
assumed here.

Idempotent: safe to re-run (each block checks for live rows first).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"


def run(conn: sqlite3.Connection) -> dict:
    counts = {"on_fail": 0, "report": 0, "report_section": 0, "write_grant": 0}

    n = conn.execute(
        "SELECT COUNT(*) FROM cfg_on_fail WHERE step IN ('report.passage_debate', "
        "'passage.debate_sync')").fetchone()[0]
    if n:
        conn.execute("DELETE FROM cfg_on_fail WHERE step IN ('report.passage_debate', "
                     "'passage.debate_sync')")
        counts["on_fail"] = n

    row = conn.execute("SELECT 1 FROM cfg_report WHERE step='report.passage_debate'").fetchone()
    if row:
        conn.execute("DELETE FROM cfg_report WHERE step='report.passage_debate'")
        counts["report"] = 1

    n = conn.execute(
        "SELECT COUNT(*) FROM cfg_report_section WHERE step='report.passage_debate'").fetchone()[0]
    if n:
        conn.execute("DELETE FROM cfg_report_section WHERE step='report.passage_debate'")
        counts["report_section"] = n

    n = conn.execute(
        "SELECT COUNT(*) FROM cfg_write_grant WHERE writer='report.passage_debate'").fetchone()[0]
    if n:
        conn.execute("DELETE FROM cfg_write_grant WHERE writer='report.passage_debate'")
        counts["write_grant"] = n

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    result = run(conn)
    print("cleanout result:", result)
    conn.close()
