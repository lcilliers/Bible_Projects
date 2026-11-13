"""draft_apply_config_2498_v1_20261113.py -- escalation #2498: the processing of prepared re-read drafts, registered.

1. Work package draft-apply (iba/app/ps/Draft-Apply.ps1) with steps draft_apply.check (utility, read-only) and draft_apply.apply (operations;
   write grants ib_observation, ib_node, ib_observation_change) -- handlers/draftapply.py, lib/draftapply.py.
2. Enums: config_module draft_apply; ib_observation.stage prior-reread. Setting draft_apply.output_dir (_analytics/reading-tools/prior-reread,
   behaviour rule B:128). The routed condition 'refused' (report-continue).
3. Method rules DA-01 to DA-04 on draft_apply.apply.
4. cfg_utility for lib/draftapply.py, handlers/draftapply.py, Draft-Apply.ps1 and this script.
The folder is registered in folder_purpose with FolderPurpose.ps1 -Action Set (type results) in the same unit of work, after this run.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice. One transaction.
Usage: python -m iba.app.migration.draft_apply_config_2498_v1_20261113 [--db PATH] [--dry-run]"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2498-DRAFT-APPLY-CONFIG-20261113"
MODULE = "draft_apply_config_2498_v1_20261113"
WP = "draft-apply"
SEE = "see lib/draftapply.py (escalation #2498)"
STEPS = [
    ("draft_apply.check", 0, "utility", "a re-read load file applied inside a savepoint and rolled back: what a run would do and every problem (writes nothing to any table)", []),
    ("draft_apply.apply", 1, "operations", "a re-read load file written in one transaction: existing observations restated in place, nodes and roles added, new observations in stage prior-reread; the whole file refused on any problem",
     ["ib_observation", "ib_node", "ib_observation_change"]),
]
RULES = [
    ("DA-01 enrich-restates-the-text-only", "An existing observation that a re-read improves is changed in place: its text is restated, founded in its verse and never repeating more than "
     "reading.observation_items max_verse_words_copied consecutive verse words. Its kind and basis were chosen with the finding and stay. Every change is kept with its reason in ib_observation_change."),
    ("DA-02 a-node-per-occurrence-with-its-surfaces-collection", "A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the "
     "surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope "
     "(B:130), is not written and is listed."),
    ("DA-03 whole-load-or-none", "A load file is checked first (nothing written); a problem anywhere refuses the whole file. A second run changes nothing."),
    ("DA-04 new-observation-stage-and-trace", "An observation added by a re-read has stage prior-reread, status draft, stable_key <reading_file id>:L<first line>:reread-<draft> and a revisit_note "
     "naming the document and its lines (#2498)."),
]
UTILITIES = [
    ("draftapply", "iba/app/lib/draftapply.py", "draftapply.py -- the processing of prepared re-read drafts into the observation record: check and apply (#2498, rules DA-01 to DA-04)", 0, None),
    ("handlers_draftapply", "iba/app/handlers/draftapply.py", "draftapply handler -- work package draft-apply: steps draft_apply.check, draft_apply.apply (#2498)", 0, None),
    ("Draft-Apply.ps1", "iba/app/ps/Draft-Apply.ps1", "PS entry point of work package draft-apply (#2498): -Step Check|Apply -File <load file>", 1,
     "PS entry point: dispatches through run.py; its settings are the steps' own"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for name, value in (("config_module", "draft_apply"), ("ib_observation.stage", "prior-reread")):
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            base = conn.execute("SELECT COALESCE(MAX(ordinal)+1, 0) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": base, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Draft-Apply.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for step, o, kind, does, grants in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": o, "step": step, "handler": f"iba.app.handlers.draftapply:{step.split('.', 1)[1]}",
                                                   "scope": "none", "does": f"{does} -- {SEE}", "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, "refused"):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None,
                                                      "message": "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)",
                                                      "route": "terminal", "inactive": 0}))
        for table in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", step, table):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": table, "database": "iba", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='draft_apply.output_dir'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "draft_apply.output_dir", "value": json.dumps("_analytics/reading-tools/prior-reread"),
                                                  "use": "#2498: where the reports of the draft check and apply steps are written (versioned per day by lib/filingkit; rule B:128)",
                                                  "module": "draft_apply", "inactive": 0}))
    for i, (key, text) in enumerate(RULES):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step='draft_apply.apply' AND rule_key=?", key):
            ops.append(("cfg_method_rule", "insert", {}, {"step": "draft_apply.apply", "rule_key": key, "rule_text": text,
                                                          "source_doc": "#2498 design v3 section 5 and the researcher's decisions 2026-11-13",
                                                          "enforced_by": "iba/app/lib/draftapply.py", "ordinal": i, "active": 1}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1, "config_exempt": 1,
                                                  "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "purpose": f"ONE-OFF migration -- escalation #2498: work package draft-apply, its steps, grants, setting, stage and method rules DA-01 to DA-04; run_id {RUN_ID}."}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
