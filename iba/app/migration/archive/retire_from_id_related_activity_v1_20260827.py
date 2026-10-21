"""retire_from_id_related_activity_v1_20260827.py — ONE-OFF, idempotent: implements escalation
#909's full removal of D14 (`from_id`) and D15 (`related_activity`'s pairing/graph role).

Researcher, verbatim (2026-08-26/27), after two live audits this session found the mechanism
unreliable and never actually used (`iba/app/reports/related-activity-summary-mockup-20260826.md`,
`iba/app/reports/from-id-data-quality-audit-20260826.md`), on top of escalation #768's own
10-round closure (`GOVERNANCE.md` §56): *"the related-activity and fromid columns in the table is
unreliable, and does not serve a purpose, and is very confusing and distracting in the history
report. I dont think you can solve the problem, and I dont think it is worth it, because you in
any case are not using it. so scrap it."*

Full removal, not a soft deprecation:
  1. `cfg_escalation_requirement` — 6 rows for field IN ('from_id','related_activity') removed.
  2. `cfg_report_section` — 6 rows removed (`escalation.list`: cycle/dangling/mismatched_pairing/
     missing_link/incoherent_link; `escalation.history`: downward_chain).
  3. `cfg_column` — 4 rows removed (escalation.from_id/.related_activity,
     escalation_history.from_id/.related_activity).
  4. `escalation`/`escalation_history` (both tables, iba.db) — `from_id`/`related_activity`
     columns physically dropped via `ALTER TABLE ... DROP COLUMN` (SQLite 3.35+).

Code side (already done, same escalation): `iba/app/lib/escalation.py`,
`iba/app/ps/Escalation.ps1` — every check/CLI param/report section built on these columns removed.

    python -m iba.app.migration.retire_from_id_related_activity_v1_20260827
"""
from __future__ import annotations

import datetime
import os
import shutil
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _backup(report: list[str]) -> None:
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    project_root = os.path.abspath(os.path.join(os.path.dirname(DB_PATH), "..", "..", ".."))
    backups_dir = os.path.join(project_root, "backups")
    os.makedirs(backups_dir, exist_ok=True)
    dest = os.path.join(backups_dir, f"iba_backup_{stamp}_RETIRE-FROM-ID-RELATED-ACTIVITY.db")
    shutil.copy2(DB_PATH, dest)
    report.append(f"[BACKUP] {os.path.basename(dest)}")


def _drop_requirement_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    cur = conn.execute(
        "DELETE FROM cfg_escalation_requirement WHERE field IN ('from_id','related_activity')")
    report.append(f"iba.db: cfg_escalation_requirement -- {cur.rowcount} row(s) deleted "
                   f"(from_id/related_activity pairing rules)")


def _drop_report_sections(conn: sqlite3.Connection, report: list[str]) -> None:
    cur = conn.execute(
        "DELETE FROM cfg_report_section WHERE (step='escalation.list' AND section_key IN "
        "('cycle','dangling','mismatched_pairing','missing_link','incoherent_link')) "
        "OR (step='escalation.history' AND section_key='downward_chain')")
    report.append(f"iba.db: cfg_report_section -- {cur.rowcount} row(s) deleted (D15 exception "
                   f"sections + downward_chain)")


def _drop_column_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    cur = conn.execute(
        "DELETE FROM cfg_column WHERE table_name IN ('escalation','escalation_history') "
        "AND name IN ('from_id','related_activity')")
    report.append(f"iba.db: cfg_column -- {cur.rowcount} row(s) deleted")


def _drop_physical_columns(conn: sqlite3.Connection, report: list[str]) -> None:
    for table in ("escalation", "escalation_history"):
        cols = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
        for col in ("from_id", "related_activity"):
            if col in cols:
                conn.execute(f"ALTER TABLE {table} DROP COLUMN {col}")
                report.append(f"iba.db: {table}.{col} column dropped")
            else:
                report.append(f"iba.db: {table}.{col} already dropped")


def _register_self(conn: sqlite3.Connection, report: list[str]) -> None:
    module = "retire_from_id_related_activity_v1_20260827"
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        return
    conn.execute(
        "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
        (module, f"iba/app/migration/{module}.py",
         "ONE-OFF migration, escalation #909 -- full removal of D14 (from_id) and D15 "
         "(related_activity's pairing/graph role): 6 cfg_escalation_requirement rows, "
         "6 cfg_report_section rows, 4 cfg_column rows deleted; from_id/related_activity columns "
         "physically dropped from escalation/escalation_history. Researcher decision after two "
         "live audits found the mechanism unreliable and unused. inactive=1 once applied -- a "
         "one-off, not a reusable routine."))
    report.append("iba.db: cfg_utility row for this migration registered")


def main() -> int:
    report: list[str] = []
    _backup(report)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _drop_requirement_rows(conn, report)
    _drop_report_sections(conn, report)
    _drop_column_rows(conn, report)
    _drop_physical_columns(conn, report)
    _register_self(conn, report)
    conn.commit()
    conn.close()
    print("D14/D15 retirement (escalation #909):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
