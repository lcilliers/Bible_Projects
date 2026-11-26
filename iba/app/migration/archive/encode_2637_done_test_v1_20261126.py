"""encode_2637_done_test_v1_20261126.py -- escalation #2637 (researcher 2026-11-26, Developer Mode: "Put that test in the governance of IBA app.
Then comply to it.").

Registers in config the test by which a routine of the analytic reading package is called complete:
  cfg_behaviour_rule 138 read-routine-done-only-by-unaided-run, with its general scope row (delivered at every session start)
  cfg_utility        this migration's own row
Written through configmaint.apply_logged. Named snapshot before a live apply; after the live apply the file archives itself
(configmaint.archive_migration). Idempotent.
Usage: python iba/app/migration/encode_2637_done_test_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-DONETEST-20261126"
MODULE = "encode_2637_done_test_v1_20261126"
RULE = {
    "id": 138, "class": "development", "rule_key": "read-routine-done-only-by-unaided-run",
    "rule_text": (
        "A routine of the analytic reading package (grouping, S1, 1.1, 1.2, 2.1, the sweep, the evidence validation, 3.1, 3.2) is called "
        "complete -- in code, a commit, BUILD.md, an escalation or chat -- only after an unaided run of it has passed. The run takes a unit not "
        "read before (a subgroup; for 3.2 a collection) from its first command to its gate, on a database copy made with dbsnapshot.copy_db, in "
        "the session that built the change. In the run Claude reads only the input packet the read command writes, writes only the output "
        "packet in the form that input packet prescribes, and runs only the package commands (Collection-Build.ps1, and Escalation.ps1 for its "
        "records); every database write is made by the record command. The run passes when Claude has created no other file (no script, view, "
        "spec or query file: the session scratchpad holds none) and no refusal names a rule the input packet did not state beforehand; a refusal "
        "of a wrong judgement does not fail it. The run, its files and its refusals are recorded on the routine's escalation. A failed run is "
        "reported as failed, naming each extra file and each unstated rule, and the routine stays open. The rules of every input and output "
        "packet are config rows (cfg_setting layer.read_types, cfg_method_rule, cfg_behaviour_rule) read live into the packet, never held only in "
        "code. A test that feeds the recorder a hand-built answer proves the recorder, not the routine, and is never reported as the routine "
        "tested."),
    "source": (
        'researcher, 2026-11-26, #2637, verbatim: "you have assured me is completed and you even tested it.  Why are you continuing to mislead '
        "me. ... Help me so I can understand what is your concept of 'pre-code a method that will complete the process without manual "
        "interventions'\"; then: \"Put that test in the governance of IBA app.  Then comply to it.  Apply my instruction to complete the coding "
        "for the analytics package of methods to ALL the routines up to and including 3.2 ... I expect the input packet (which are prepare by "
        "the pre-set code of the application) and the output packet in the prescribed format (which again is determined by the pre-set code. "
        'The processing of the output packet into the DB must all be pre-coded. the rules of the input and output packet must all be in the '
        'configs."'),
    "enforced_by": ("Claude's own conduct, the unaided run recorded on the routine's escalation; a mechanical audit of the run (extra files, "
                    "refusals against the rules the packet stated) is to be built under #2637"),
    "active": 1, "enforcement_status": "buildable_not_built", "deliver_when": "always",
}


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", (RULE["rule_key"],)).fetchone():
        if conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE id=?", (RULE["id"],)).fetchone():
            raise SystemExit(f"cfg_behaviour_rule id {RULE['id']} is taken by another rule: re-number before applying")
        ops.append(("cfg_behaviour_rule", "insert", {}, {**RULE, "added_at": "2026-11-26T12:00:00Z"}))
    if not conn.execute("SELECT 1 FROM cfg_rule_scope WHERE rule_ref='B:138'").fetchone():
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": "B:138", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2637: rule 138, a read routine is complete only after an unaided run passes",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2637-donetest-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
