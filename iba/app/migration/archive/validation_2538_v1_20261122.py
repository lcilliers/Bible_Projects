"""validation_2538_v1_20261122.py -- escalation #2538 (researcher, 2026-11-22: "Yes, promote it"; plan outputs/escalation/2538-validation-step-plan-v9-20261122.md).

Registers the validation after stage 4 of a collection in config and creates what it needs:
  columns / tables   ib_observation.nature (the marker: evidence or inner_being), registered in cfg_column
  enums              ib_observation.nature: evidence, inner_being
  settings           validate.reading (the required word columns, the actions a sheet may hold), validate.pull_name, validate.check_name
  steps              collection.validate_pull, validate_record, validate_check (work package collection-build), their routed condition, write grants
  rules              method rules VA-01 to VA-06 and IB-07; the behaviour rule collection-validation-follows-stage-4; B:132 and B:133 each gain the sentence that
                     separates the marker from the stage and the two validations
  utilities          the libraries collectionvalidate and validationactions, and this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/validation_2538_v1_20261122.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import datetime
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2538-VALIDATION-20261122"
MODULE = "validation_2538_v1_20261122"
SOURCE = "escalation #2538 (researcher, 2026-11-22; outputs/escalation/2538-validation-step-plan-v9-20261122.md and the pilot reports of the same day)"
FILLED = "Collection-Build.ps1 -Action ValidateRecord (lib/validationactions.py set_nature, create_observation)"

NATURE_COL = {"database": "iba", "table_name": "ib_observation", "name": "nature", "type": "TEXT", "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None,
              "use": "the marker (#2538): evidence (an observation about the data, tied to a verse) or inner_being (an observation about the working of the inner being, based on evidence; a building block of "
                     "the stage 5 claims, never a claim). It follows the content and purpose of the observation, never its stage; empty means not yet judged by the validation. An observation that is neither "
                     "is deleted. Set only by the validation (lib/validationactions.py set_nature), each setting kept in ib_observation_change with its reason",
              "expectation": "enum.ib_observation.nature", "source": SOURCE, "filled_by": FILLED, "inactive": 0}
ENUMS = {"ib_observation.nature": ["evidence", "inner_being"]}

ACTIONS = ["set_nature", "defer", "close_deferral", "annotate", "complete_node", "note_node", "restate", "add_trace", "create_observation", "add_word_node", "move_node",
           "drop_node", "drop_unrelated_node", "consume", "delete_neither", "mark_self_evidencing"]
SETTINGS = [
    ("validate.reading", {"word_columns": ["verse_reference", "verse_lexical_id", "surface", "strong", "morph_code", "role", "collection_id"], "actions": ACTIONS},
     "the validation after stage 4 of a collection (#2538): the columns a word node must carry (a traced node names another observation and carries none) and the actions a sheet of ValidateRecord "
     "may hold (functions of lib/validationactions.py). Read by lib/collectionvalidate.py", "layer"),
    ("validate.pull_name", "validate-pull", "the file name stem of the report of ValidatePull: <stem>-<collection>-v<n>-<yyyymmdd>.md under surfaces.exports_root, versioned by the filing rule", "layer"),
    ("validate.check_name", "validate-check", "the file name stem of the report of ValidateCheck: <stem>-<collection>-v<n>-<yyyymmdd>.md under surfaces.exports_root, versioned by the filing rule", "layer"),
]
STEPS = [
    ("collection-build", 21, "collection.validate_pull", "iba.app.handlers.collectionbuild:validate_pull", "none",
     "the scope of a collection (every live observation related to it) with the structural tests: a Markdown report and the working file of the observations to read; writes no table -- see lib/collectionvalidate.py (escalation #2538)", "utility"),
    ("collection-build", 22, "collection.validate_record", "iba.app.handlers.collectionbuild:validate_record", "none",
     "check a sheet of validation actions whole and write them in one transaction (marker, deferral, restate, trace, create, consume, delete as neither, node completion, annotation); -Check runs and rolls back; any problem refuses the sheet -- see lib/collectionvalidate.py, lib/validationactions.py", "operations"),
    ("collection-build", 23, "collection.validate_check", "iba.app.handlers.collectionbuild:validate_check", "none",
     "the completeness check of a collection's validation in two layers, evidence first; names what is open, deferred to a named collection or pending; writes a report; writes no table -- see lib/collectionvalidate.py", "operations"),
]
GRANTS = [("migration", "ib_observation"), ("collection.validate_record", "ib_observation"), ("collection.validate_record", "ib_node"), ("collection.validate_record", "ib_observation_change")]
ON_FAIL = [(s[2], "refused", "report-continue", None, "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)", "terminal", 0) for s in STEPS]
UTILITIES = [
    ("collectionvalidate", "iba/app/lib/collectionvalidate.py", 0,
     "collectionvalidate.py -- the validation after stage 4 of a collection (escalation #2538): the scope, the structural tests, the two-layer completeness check and the sheet of actions.", 1,
     "the required word columns and the actions a sheet may hold are read from cfg_setting validate.reading; the code holds no tunable value"),
    ("validationactions", "iba/app/lib/validationactions.py", 0,
     "validationactions.py -- the actions of the validation (escalation #2538): marker, deferral, node completion, restatement, trace, creation, consumption, deletion as neither, annotation of a deleted observation.", 1,
     "the marker values are cfg_enum ib_observation.nature; the roles are cfg_setting reading.node_roles; the minimum length of a stated reason is a floor of wording, not a tunable"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2538: the validation registered; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
VA = "iba/app/lib/collectionvalidate.py and lib/validationactions.py"
METHOD = [
    ("collection.validate_record", "VA-01 a-sheet-is-one-checked-transaction",
     "A sheet of validation actions is checked whole (every action named, its parameters complete) and written in one transaction: any action the tables refuse refuses the whole sheet and nothing is kept. -Check runs every "
     "action and rolls back. Every change is kept in ib_observation_change with its reason (RW-01); nothing is physically deleted."),
    ("collection.validate_record", "VA-02 repair-first-and-every-finding-acted-on",
     "A finding of the validation is repaired first: a wording that is untrue or stronger than its verse is restated and the restatement checked against the base data; a node missing a column is completed, or the reason the data "
     "cannot give it is recorded; a duplicate is consolidated; a node is deleted only when another live node carries its occurrence or it supports no finding of its observation. A finding is left open only when a named "
     "collection's validation will touch the observation: the deferral to that collection and the finding are recorded, and the check accepts it as deferred. A finding with no named owner is closed in the validation."),
    ("collection.validate_record", "VA-03 consumption-is-verified-before-deletion",
     "An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in "
     "words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first."),
    ("collection.validate_record", "VA-04 neither-evidence-nor-inner-being-is-deleted",
     "An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation "
     "holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way."),
    ("collection.validate_record", "VA-05 the-marker-follows-content-not-stage",
     "Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows "
     "the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split."),
    ("collection.validate_check", "IB-07 inner-being-observations-trace-to-evidence",
     "Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every "
     "word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the "
     "quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed."),
    ("collection.validate_check", "VA-06 evidence-validation-gates-inner-being-validation",
     "The validation runs in two layers, never concurrently: evidence first, then inner being. The inner-being layer is judged only when the evidence layer passes (every in-scope observation marked, none without a live "
     "node, no word node missing a required column without its reason, no live trace to a deleted observation, no two of one meaning). A later evidence change reopens only the inner-being rows it touches."),
]
RULE = ("collection-validation-follows-stage-4",
        "After stage 4 a collection is validated (ValidatePull, ValidateRecord, ValidateCheck): every live observation related to it, through the collection, a verse of it, a member surface with its lettered "
        "Strong's code, or its meaning, and excluding deleted observations and nodes, is evaluated and marked evidence or inner being by its content. The validation repairs first (restate, complete, consolidate), "
        "deletes last, deletes an observation that is neither, never discards an older observation without a verified consumption, and acts on every finding or defers it to a named collection that will touch the "
        "observation. Evidence is validated before inner being, never concurrently. Claude reads and decides; the researcher scrutinises. The marker, the actions and the check are the routines of Collection-Build.ps1.",
        "iba/app/lib/collectionvalidate.py (the scope, the check, the sheet) and iba/app/lib/validationactions.py (each action keeps its change and reason)", "partially_enforced")
B132_ADD = (" The marker of an observation (ib_observation.nature: evidence or inner_being) follows its content, not its stage; the stored stage is a record of origin and an observation of any stage may be inner being "
            "when it traces to evidence (collection-validation-follows-stage-4).")
B133_ADD = (" After stage 4 the validation of a collection runs in two layers, evidence and then inner being, never concurrently; the inner-being layer opens only when the evidence layer passes "
            "(collection-validation-follows-stage-4).")


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name='nature'"):
        top = one("SELECT coalesce(max(ordinal), -1) FROM cfg_column WHERE database='iba' AND table_name='ib_observation'")[0]
        ops.append(("cfg_column", "insert", {}, dict(NATURE_COL, ordinal=top + 1)))
    for name, values in ENUMS.items():
        top = one("SELECT coalesce(max(ordinal),-1) FROM cfg_enum WHERE name=?", name)[0]
        for v in values:
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                top += 1
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": top, "inactive": 0}))
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value, ensure_ascii=False), "use": use, "module": module, "inactive": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    for wp, ordinal, step, handler, scope, does, kind in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": wp, "ordinal": ordinal, "step": step, "handler": handler, "scope": scope, "does": does, "inactive": 0, "kind": kind}))
    for step, cond, path, resolver, message, route, inactive in ON_FAIL:
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path, "resolver": resolver, "message": message, "route": route, "inactive": inactive}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt, "config_exempt_reason": reason,
                                                      "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    for i, (step, key, text) in enumerate(METHOD):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", step, key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": step, "rule_key": key, "rule_text": text, "source_doc": SOURCE, "enforced_by": VA, "ordinal": i, "active": 1}))
    key, text, enf, status = RULE
    if not has("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", key):
        top = one("SELECT max(id) FROM cfg_behaviour_rule")[0] + 1
        ops.append(("cfg_behaviour_rule", "insert", {}, {"id": top, "class": "study_method", "rule_key": key, "rule_text": text, "source": SOURCE, "enforced_by": enf, "added_at": _now(),
                                                          "active": 1, "enforcement_status": status, "deliver_when": "study_active"}))
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{top}", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    for rid, add in ((132, B132_ADD), (133, B133_ADD)):
        t = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=?", rid)[0]
        if add.strip() not in t:
            ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"rule_text": t.rstrip() + add}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    cols = {r[1] for r in conn.execute("PRAGMA table_info(ib_observation)")}
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); ib_observation.nature to add: {'nature' not in cols}")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", set_.get("name") or set_.get("module") or set_.get("step") or set_.get("key") or set_.get("rule_key") or set_.get("table_name") or "")
        return 0
    if not ops and "nature" in cols:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-validation', named=True)}")
    try:
        conn.execute("SAVEPOINT validation_2538")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if "nature" not in cols:
            conn.execute("ALTER TABLE ib_observation ADD COLUMN nature TEXT")
        conn.execute("RELEASE validation_2538")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO validation_2538")
        conn.execute("RELEASE validation_2538")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); ib_observation.nature added: {'nature' not in cols}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
