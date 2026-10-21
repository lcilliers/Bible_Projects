"""bootstrap_raw_backfill.py — ONE-OFF: register the `raw-backfill` work package / `raw.backfill_
meaning` step (handlers/raw.py:backfill_meaning). Brand-new mechanism (new work package + step),
so bootstrap-direct like every other addition of this shape this session — configmaint.propose
only writes rows on already-existing tables/columns.

No new write grants needed: backfill_meaning reuses raw.detail_one() as-is, writing under the
EXISTING 'call2_getInfo' writer identity, which already holds grants on strong/strong_sense/
strong_meaning_tree/strong_lexicon (raw.detail's own grants). No new cfg_table/cfg_column either
— nothing new is stored, this just runs the existing per-strong meaning pull for codes outside
their usual per-word onboarding context. No cfg_report — this is an ACTION step (like raw.detail/
raw.verses), not an advisory quality-check step; governance.reports_must_persist only applies to
the latter.

    python -m iba.app.migration.bootstrap_raw_backfill
"""
from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

REPORT: list[str] = []


def _work_package(conn, name, ps_script):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, complete_message, "
            "next_step_hint, paused_message, inactive) VALUES (?,?,'book',0,NULL,NULL,NULL,0)",
            (name, ps_script))
        REPORT.append(f"cfg_work_package {name!r} added")
    else:
        REPORT.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does):
    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (wp, step)).fetchone():
        conn.execute(
            "INSERT INTO cfg_step (work_package,ordinal,step,handler,scope,does,inactive) "
            "VALUES (?,?,?,?,'book',?,0)", (wp, ordinal, step, handler, does))
        REPORT.append(f"cfg_step {step!r} added")
    else:
        REPORT.append(f"cfg_step {step!r} already present")


def _on_fail(conn, step, condition, path, message, route):
    if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                        (step, condition)).fetchone():
        conn.execute(
            "INSERT INTO cfg_on_fail (step,condition,path,resolver,message,route,inactive) "
            "VALUES (?,?,?,NULL,?,?,0)", (step, condition, path, message, route))
        REPORT.append(f"cfg_on_fail ({step}, {condition}) added")
    else:
        REPORT.append(f"cfg_on_fail ({step}, {condition}) already present")


def register(conn: sqlite3.Connection) -> None:
    _work_package(conn, "raw-backfill", "iba/app/ps/Raw-Backfill.ps1")
    _step(conn, "raw-backfill", 0, "raw.backfill_meaning", "iba.app.handlers.raw:backfill_meaning",
         "for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find "
         "every distinct strong its spans reference that has no `strong` row yet, and pull ONLY "
         "the meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) — "
         "not verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage "
         "growth, not a full-Bible bulk pull.")
    _on_fail(conn, "raw.backfill_meaning", "unreachable", "report-stop",
            "STEP is not reachable — cannot pull any meaning", "terminal")
    _on_fail(conn, "raw.backfill_meaning", "invalid-range", "report-stop",
            "the -Range value could not be parsed", "terminal")
    conn.commit()


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    register(conn)
    conn.close()
    print("raw-backfill bootstrap:")
    for line in REPORT:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
