"""engagement_2406_v1_20261109.py -- escalation #2406: registers the engagement step (what each surface of a collection does for the inner being).

  settings   engagement.stage, .roles, .group_rule, .no_bearing_kind, .tests, .working_dir, .report_path, .group_judged_by (module engagement)
  enum       ib_observation.stage: engagement
  package    engagement (iba/app/ps/Engagement.ps1); steps engagement.pull, .record, .group, .check, each with its on_fail conditions
  grants     engagement.record writes ib_observation, ib_node, ib_observation_change; engagement.group writes surface_term, surface_event
  utilities  lib/engagement.py, handlers/engagement.py, Engagement.ps1, this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/engagement_2406_v1_20261109.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2406-ENGAGEMENT-20261109"
MODULE = "engagement_2406_v1_20261109"
WP = "engagement"
H = "iba.app.handlers.engagement"
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
NOT_ASSESSED = "reported, nothing refused -- a member surface is not assessed in every one of its verses; the report names it"
LEFT = "reported; the handler raised one escalation for the collection (a member surface left the study group; this step never unlinks it, R4)"
SETTINGS = [
    ("engagement.stage", "engagement", "the stage value written on the observations of the engagement step (#2406); kept apart from Analysis_phase_1, whose check forbids the silence kind"),
    ("engagement.roles", {"relevant": ["characteristic", "qualifier"], "bears_on": ["object", "relational_target", "enactment"]},
     "the roles a surface takes in a verse in the engagement assessment: a relevant surface is a characteristic or a qualifier of an inner-being operation, a surface that bears on an act is an object, relational target or enactment; the same words as reading.node_roles (#2406)"),
    ("engagement.group_rule", {"characteristic": "behaviour", "qualifier": "inner_being_state", "none": "other"},
     "the surface-level group of a member surface from its live engagement nodes (#2406, researcher 2026-11-09): behaviour if it is a characteristic in any verse, else inner_being_state if it is a qualifier in any verse, else other (it leaves the study group)"),
    ("engagement.no_bearing_kind", "silence", "the observation kind that records a surface with no inner-being bearing in a verse in the engagement assessment (#2406 Q2); Analysis_phase_1 still does not use it"),
    ("engagement.tests", ["inner_being_vocabulary", "idiom_or_combined_span", "volitional_sense", "other_party", "negation_or_modifier", "sequence_link", "grammar_only"],
     "the relevance tests of specification 4.1 (outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md), by key; an engagement evaluation records the test the surface passed (#2406 Q3), until the researcher sets the line between behaviour and description"),
    ("engagement.working_dir", "_analytics/surfaces/working_files/engagement", "the folder of the engagement working files (the pull of a collection and the filled assessment), part of surfaces.working_files_root (#2406)"),
    ("engagement.report_path", "outputs/reports/engagement", "the folder of the engagement check reports (#2406)"),
    ("engagement.group_judged_by", "rule:engagement", "the value of surface_term.group_judged_by when the engagement step decides a group (#2406)"),
]
STEPS = [
    (1, "engagement.pull", "pull", "write the working file of one collection with -Collection: its member surfaces, their verses with the ESV text and the observations already on those verses (a view of the tables, never overwritten) -- see lib/engagement.py (escalation #2406)"),
    (2, "engagement.record", "record", "check a filled assessment against its pull, whole, and write it in one transaction with -File (-Check previews): the actions on the existing observations, one observation for each surface and role, a node for each verse -- see lib/engagement.py (escalation #2406)"),
    (3, "engagement.group", "group", "set the surface-level group of each member surface of -Collection from its engagement nodes (-Check previews); a surface that leaves the study group is raised as one escalation, never unlinked -- see lib/engagement.py (escalation #2406)"),
    (4, "engagement.check", "check", "report every member surface of -Collection against its verses to engagement.report_path -- see lib/engagement.py (escalation #2406)"),
]
CONDITIONS = {"engagement.pull": [("refused", REFUSED)], "engagement.record": [("refused", REFUSED)],
              "engagement.group": [("refused", REFUSED), ("member_left_study", LEFT)], "engagement.check": [("refused", REFUSED), ("not_assessed", NOT_ASSESSED)]}
GRANTS = [("engagement.record", "ib_observation"), ("engagement.record", "ib_node"), ("engagement.record", "ib_observation_change"),
          ("engagement.group", "surface_term"), ("engagement.group", "surface_event")]
UTILITIES = [
    ("engagement", "iba/app/lib/engagement.py", 0, "engagement.py -- the step before narration: what each surface of a collection does for the inner being: the pull, the check and write of the assessment, the group rule, the report (escalation #2406).", 1,
     "every value is a cfg_setting of module engagement read through settings(); the code holds no tunable value"),
    ("handlers_engagement", "iba/app/handlers/engagement.py", 0, "handlers for work package engagement: pull, record, group, check (escalation #2406).", 1, "handlers hold no rule; the rule is lib/engagement.py and cfg_setting module engagement"),
    ("Engagement.ps1", "iba/app/ps/Engagement.ps1", 0, "PS entry point for the engagement step (escalation #2406): Pull, Record, Group, Check; dispatches through run.py, work package engagement.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2406: registers the engagement step; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": "engagement", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_enum WHERE name='ib_observation.stage' AND value='engagement'"):
        top = conn.execute("SELECT max(ordinal) FROM cfg_enum WHERE name='ib_observation.stage'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.stage", "value": "engagement", "ordinal": top + 1, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Engagement.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for ordinal, step, fn, does in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": ordinal, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": "operations"}))
        for cond, msg in CONDITIONS[step]:
            if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
                ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": "report-continue", "resolver": None, "message": msg,
                                                          "route": "terminal", "inactive": 0}))
    for writer, table in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", writer, table):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": table, "database": "iba", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2406-engagement', named=True)}")
    try:
        conn.execute("SAVEPOINT engagement_cfg")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE engagement_cfg")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO engagement_cfg")
        conn.execute("RELEASE engagement_cfg")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
