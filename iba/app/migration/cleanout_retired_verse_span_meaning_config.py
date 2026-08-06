"""cleanout_retired_verse_span_meaning_config.py — hard-deletes the dangling `report.verse_span_meaning`
config references configmaint.validate keeps flagging (escalation #445, 2026-08-05), and corrects the
3 cfg_column.filled_by values CONFIG-REPORT-v34 names as stale (2026-08-06).

`report.verse_span_meaning` itself (cfg_step, both work packages) was already made `inactive=1` when
the T1-T3/span_reading rebuild superseded it with `report.verse_lexical`/`lexical.build` (BUILD.md
§56-59) — but `inactive=1` alone left its own downstream references (cfg_on_fail, cfg_report,
cfg_report_section, cfg_write_grant) still naming it, and validate treats "references an inactive
step" as a structural error, not merely advisory. Same carve-out class and precedent as
`cleanout_retired_passage_config.py` (2026-08-06): direct researcher authorization is the up-front
approval ("previously I retired these configs - they should all be marked softdelete. take this as
approval for the deletion" — escalation #445 + the CONFIG-REPORT-v34 "Stale filled_by (3)" finding,
both 2026-08-06).

Hard-deletes (this app's convention for "genuinely retired, not merely disabled" cfg_* rows —
`inactive=1` is for "exists but not currently callable"; a row with no live meaning left at all is
removed, matching cleanout_retired_passage_config.py):
- cfg_on_fail: the one row for step='report.verse_span_meaning'
- cfg_report: the one row for step='report.verse_span_meaning'
- cfg_report_section: the 2 rows for step='report.verse_span_meaning'
- cfg_write_grant: the 2 rows for writer='report.verse_span_meaning'

Updates (not deleted -- the columns themselves are live, only their filled_by provenance was stale):
- cfg_column.filled_by for passage.book_label / passage.verse_span_meaning_path /
  passage.verse_span_meaning_written_at -> a DORMANT marker, since nothing in the current
  input-scope passage model (BUILD.md §67) writes these 3 columns at all (confirmed by reading
  handlers/passage.py:build directly, not assumed).

Idempotent: safe to re-run (each block checks for live rows first).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

DORMANT = ("DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / "
           "lexical.build, BUILD.md §56-59); not carried into the input-scope passage model "
           "(BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against "
           "handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34)")


def run(conn: sqlite3.Connection) -> dict:
    counts = {"on_fail": 0, "report": 0, "report_section": 0, "write_grant": 0, "column_updated": 0}

    row = conn.execute(
        "SELECT 1 FROM cfg_on_fail WHERE step='report.verse_span_meaning'").fetchone()
    if row:
        conn.execute("DELETE FROM cfg_on_fail WHERE step='report.verse_span_meaning'")
        counts["on_fail"] = 1

    row = conn.execute(
        "SELECT 1 FROM cfg_report WHERE step='report.verse_span_meaning'").fetchone()
    if row:
        conn.execute("DELETE FROM cfg_report WHERE step='report.verse_span_meaning'")
        counts["report"] = 1

    n = conn.execute(
        "SELECT COUNT(*) FROM cfg_report_section WHERE step='report.verse_span_meaning'").fetchone()[0]
    if n:
        conn.execute("DELETE FROM cfg_report_section WHERE step='report.verse_span_meaning'")
        counts["report_section"] = n

    n = conn.execute(
        "SELECT COUNT(*) FROM cfg_write_grant WHERE writer='report.verse_span_meaning'").fetchone()[0]
    if n:
        conn.execute("DELETE FROM cfg_write_grant WHERE writer='report.verse_span_meaning'")
        counts["write_grant"] = n

    for col in ("book_label", "verse_span_meaning_path", "verse_span_meaning_written_at"):
        row = conn.execute(
            "SELECT filled_by FROM cfg_column WHERE table_name='passage' AND name=?", (col,)).fetchone()
        if row and row[0] != DORMANT:
            conn.execute(
                "UPDATE cfg_column SET filled_by=? WHERE table_name='passage' AND name=?",
                (DORMANT, col))
            counts["column_updated"] += 1

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    result = run(conn)
    print("cleanout result:", result)
    conn.close()
