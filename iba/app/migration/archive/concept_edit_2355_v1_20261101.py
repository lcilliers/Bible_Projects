"""concept_edit_2355_v1_20261101.py -- escalation #2355 (researcher, chat 2026-11-01: descriptions are added and
edited in standard mode through a PowerShell script; "the tool must allow for adding new domains, and setting the
delete flag for a domain").

Registers the tool iba/app/ps/Concept-Edit.ps1: work package concept-edit with four steps (list, describe,
add_domain, set_deleted), the 'refused' condition of each, the write grants of the three writing steps
(concept_domain, concept), the cfg_utility rows of the script, its handler module and its library, and this script
(inactive, at its archive path). The filled_by text of the cfg_column rows of concept_domain and concept is brought
to the steps that now write them. cfg_* writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/concept_edit_2355_v1_20261101.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2355-CONCEPT-EDIT-20261101"
MODULE = "concept_edit_2355_v1_20261101"
WP = "concept-edit"
H = "iba.app.handlers.conceptedit"
STEPS = [
    ("concept_edit.list", f"{H}:list_", "the domains and concepts with their descriptions (read-only); "
     "-Level, -DomainId, -IncludeDeleted -- see lib/conceptedit.py (escalation #2355)", ()),
    ("concept_edit.describe", f"{H}:describe", "set the description of a domain or a concept, one or a JSON list "
     "as one unit; the wording replaced is shown -- see lib/conceptedit.py (escalation #2355)",
     ("concept_domain", "concept")),
    ("concept_edit.add_domain", f"{H}:add_domain", "add a domain, last in order unless an ordinal is given "
     "-- see lib/conceptedit.py (escalation #2355)", ("concept_domain",)),
    ("concept_edit.set_deleted", f"{H}:set_deleted", "set or clear the delete flag of a domain; refused while it "
     "holds live concepts -- see lib/conceptedit.py (escalation #2355)", ("concept_domain",)),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("conceptedit", "iba/app/lib/conceptedit.py", 0, "conceptedit.py -- the researcher's edits to the concept "
     "grouping (escalation #2355): the description of a domain or a concept, a new domain, a domain's delete "
     "flag.", 0, None),
    ("handlers_conceptedit", "iba/app/handlers/conceptedit.py", 0, "handlers/conceptedit.py -- the run.py "
     "handlers for work package concept-edit (Concept-Edit.ps1, escalation #2355).", 0, None),
    ("Concept-Edit.ps1", "iba/app/ps/Concept-Edit.ps1", 0, "PS entry point for editing the concept grouping "
     "(escalation #2355): List, Describe, AddDomain, SetDeleted; dispatches through run.py, work package "
     "concept-edit.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2355: registers "
     f"the concept-edit tool; run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows through "
     "configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
OLD_FILLED = "no step writes the table yet"
NEW_FILLED = ("iba/app/ps/Concept-Edit.ps1 writes new domains, descriptions and a domain's delete flag "
              "(steps concept_edit.describe, .add_domain, .set_deleted)")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Concept-Edit.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, handler, does, tables) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": i, "step": step, "handler": handler, "scope": "none",
                "does": does, "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {
                "step": step, "condition": "refused", "path": "report-continue", "resolver": None,
                "message": REFUSED, "route": "terminal", "inactive": 0}))
        for t in tables:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", step, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": t, "database": "iba",
                                                              "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {
                "module": module, "file_path": path, "purpose": purpose, "inactive": inactive,
                "config_exempt": exempt, "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                "crash_escalation_note": None}))
    for t in ("concept_domain", "concept"):
        for name, filled in conn.execute("SELECT name, filled_by FROM cfg_column WHERE database='iba' "
                                         "AND table_name=?", (t,)).fetchall():
            if name == "description":
                new = "iba/app/ps/Concept-Edit.ps1 -Action Describe" + (", AddDomain" if t == "concept_domain"
                                                                        else "")
            elif filled and filled.endswith(OLD_FILLED):
                new = filled[:-len(OLD_FILLED)] + NEW_FILLED
            else:
                continue
            if new != filled:
                ops.append(("cfg_column", "update", {"database": "iba", "table_name": t, "name": name},
                            {"filled_by": new}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('step') or set_.get('module') or set_.get('name') or where.get('name')}"
                  f" {set_.get('table_name', '') if t == 'cfg_write_grant' else ''}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT concept_edit_reg")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE concept_edit_reg")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO concept_edit_reg")
        conn.execute("RELEASE concept_edit_reg")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
