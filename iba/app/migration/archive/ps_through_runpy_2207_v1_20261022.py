"""ps_through_runpy_2207_v1_20261022.py -- escalation #2207 item 1 (fix-not-count part 2, approved
v7: "2 PS scripts bypassing run.py ... Dispatch them through run.py"; cfg_behaviour_rule 43).
iba/app/ps/Behaviour.ps1 and iba/app/ps/VerseMeta.ps1 called lib/behaviour.py and lib/versemeta.py
directly. They now dispatch through run.py:

- work package `behaviour`, step `behaviour.list` (handlers/reports.py:behaviour_list, utility);
- work package `verse-meta`, step `verse_meta.set_status` (handlers/versemeta.py:set_status,
  operations), its write grant on verse_meta, and two usage outcomes (bad-parameter, not-found)
  routed report-continue, so a typed-in error is not recorded as an escalation.

The cfg_utility purposes of the four files and cfg_column verse_meta.status/status_changed_at
filled_by no longer describe a direct CLI.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/ps_through_runpy_2207_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2207-PS-THROUGH-RUNPY-20261022"
MODULE = "ps_through_runpy_2207_v1_20261022"

INSERTS = [
    ("cfg_work_package", {"name": "behaviour"}, {
        "name": "behaviour", "ps_script": "iba/app/ps/Behaviour.ps1", "runs_over": "none",
        "chained": 0, "inactive": 0}),
    ("cfg_step", {"work_package": "behaviour", "step": "behaviour.list"}, {
        "work_package": "behaviour", "ordinal": 0, "step": "behaviour.list",
        "handler": "iba.app.handlers.reports:behaviour_list", "scope": "none", "kind": "utility",
        "inactive": 0,
        "does": "every active cfg_behaviour_rule, optionally one -Class, to behaviour.list_report_path "
                "-- read-only (#2207: through run.py)"}),
    ("cfg_work_package", {"name": "verse-meta"}, {
        "name": "verse-meta", "ps_script": "iba/app/ps/VerseMeta.ps1", "runs_over": "none",
        "chained": 0, "inactive": 0}),
    ("cfg_step", {"work_package": "verse-meta", "step": "verse_meta.set_status"}, {
        "work_package": "verse-meta", "ordinal": 0, "step": "verse_meta.set_status",
        "handler": "iba.app.handlers.versemeta:set_status", "scope": "none", "kind": "operations",
        "inactive": 0,
        "does": "sets verse_meta.status (cfg_enum verse_meta_status) for a comma-delimited list of "
                "verse references; stamps status_changed_at only on a real change (#1661; #2207: "
                "through run.py)"}),
    ("cfg_write_grant", {"writer": "verse_meta.set_status", "table_name": "verse_meta"}, {
        "writer": "verse_meta.set_status", "table_name": "verse_meta", "database": "iba",
        "inactive": 0}),
    ("cfg_on_fail", {"step": "verse_meta.set_status", "condition": "bad-parameter"}, {
        "step": "verse_meta.set_status", "condition": "bad-parameter", "path": "report-continue",
        "route": "terminal", "inactive": 0,
        "message": "usage error, nothing written, not recorded as an escalation -- -Status must be "
                   "a live value of cfg_enum verse_meta_status"}),
    ("cfg_on_fail", {"step": "verse_meta.set_status", "condition": "not-found"}, {
        "step": "verse_meta.set_status", "condition": "not-found", "path": "report-continue",
        "route": "terminal", "inactive": 0,
        "message": "one or more references not found (the rest were set), not recorded as an "
                   "escalation -- check the references listed"}),
]

UPDATES = [
    ("cfg_utility", {"module": "behaviour"}, {
        "purpose": "Read-only report of cfg_behaviour_class/cfg_behaviour_rule (escalations "
                   "#715/#732/#733): writes the live rule set to behaviour.list_report_path. Run as "
                   "step behaviour.list (handlers/reports.py) behind Behaviour.ps1 (#2207). Rules "
                   "are written through configmaint, never by this module."}),
    ("cfg_utility", {"module": "versemeta"}, {
        "purpose": "Write path for verse_meta.status (cfg_enum verse_meta_status: "
                   "exclude/citated/analysed). Stamps status_changed_at only on an actual value "
                   "change. Run as step verse_meta.set_status (handlers/versemeta.py) behind "
                   "VerseMeta.ps1 (#2207). Escalation #1661."}),
    ("cfg_utility", {"module": "VerseMeta.ps1"}, {
        "purpose": "PS entry point of work package verse-meta: VerseMeta.ps1 -Step SetStatus "
                   "-References \"Gen.1.1,Rom 1:2\" -Status analysed, dispatched through run.py "
                   "(step verse_meta.set_status, #2207). Escalation #1661.",
        "config_exempt_reason": "PS entry point: the step's config is read by the handler and "
                                "lib/versemeta.py"}),
    ("cfg_utility", {"module": "iba_app_ps_behaviour"}, {
        "purpose": "PS entry point of work package behaviour: Behaviour.ps1 -Action List [-Class], "
                   "dispatched through run.py (step behaviour.list, #2207).",
        "config_exempt_reason": "PS entry point: the step's config is read by the handler"}),
    ("cfg_column", {"table_name": "verse_meta", "name": "status"}, {
        "filled_by": "VerseMeta.ps1 -Step SetStatus (step verse_meta.set_status, lib/versemeta.py)"}),
    ("cfg_column", {"table_name": "verse_meta", "name": "status_changed_at"}, {
        "filled_by": "VerseMeta.ps1 -Step SetStatus (step verse_meta.set_status, lib/versemeta.py)"}),
]


def _where_sql(where: dict) -> tuple[str, list]:
    return " AND ".join(f'"{k}"=?' for k in where), list(where.values())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    for table, key, row in INSERTS:
        w, v = _where_sql(key)
        if not conn.execute(f'SELECT 1 FROM "{table}" WHERE {w}', v).fetchone():
            ops.append((table, "insert", {}, row))
    for table, where, set_ in UPDATES:
        w, v = _where_sql(where)
        cur = conn.execute(f'SELECT {", ".join(chr(34) + c + chr(34) for c in set_)} FROM "{table}" '
                           f'WHERE {w}', v).fetchone()
        if cur is None:
            print(f"missing row: {table} {where}")
            return 1
        if list(cur) != list(set_.values()):
            ops.append((table, "update", where, set_))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2207 item 1: Behaviour.ps1 and VerseMeta.ps1 "
                       f"through run.py (work packages, steps, write grant, on_fail rules), through "
                       f"configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied."}))
    for t, op, where, set_ in ops:
        print(f"  {op} {t} {where or ''} {list(set_)}")
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
