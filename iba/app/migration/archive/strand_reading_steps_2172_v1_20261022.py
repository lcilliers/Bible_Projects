"""strand_reading_steps_2172_v1_20261022.py -- escalation #2172, build plan v1 section 5 steps 2 to 5
(outputs/escalation/2172-process-build-plan-v1-20261022.md): the reading process as config.

- work package strand-reading (iba/app/ps/Strand-Reading.ps1) and its eight steps (Define, then the
  seven of the design: Context, Record, Gather, Map, Derive, Rewrite, Account), each with its write
  grants and its 'refused' route; cfg_report rows for the three report steps; the output folder
  setting strand_reading.output_dir; the three new files registered in cfg_utility.
- the close gate (build decision 5): cfg_escalation_requirement check kind strand_account_clean on
  Update and ResolveSelfCorrectable -- the escalation that records a strand reaches completed or
  closed only when every hit has a face or a reason and every observation a disposition.
- the narrative rules that govern Narrative-Register.ps1 (B:76, B:77, B:78) also govern
  Strand-Reading.ps1 (cfg_rule_scope); B:76 names the new tool; cfg_utility for narrativeregister
  no longer lists Record.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/strand_reading_steps_2172_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2172-STRAND-STEPS-20261022"
MODULE = "strand_reading_steps_2172_v1_20261022"
WP = "strand-reading"
SEE = "see lib/strandreading.py (escalation #2172)"
NARR = ["narrative_claim", "narrative_claim_source", "narrative_claim_telling", "narrative_claim_change"]

STEPS = [  # step, handler function, does, write grants
    ("define", "define", "a strand: its code, title, cluster, escalation and word family (-Strongs); adds words to "
     "an open strand", ["reading_strand", "reading_strand_strong"]),
    ("context", "context", "step 1: every hit with its text and lexical data, the observations already on those "
     "words and verses, the open thread items that match, each verse's coverage -> the context file",
     ["reading_strand_hit"]),
    ("record", "record", "step 2: the reading recorded -- observations (grounded, quote-checked), a face or a reason "
     "per hit read; read verses marked analysed", ["ib_observation", "ib_node", "reading_strand_hit", "verse_meta"]),
    ("gather", "gather", "step 3: every narrative block related to the strand, with its text and tellings "
     "(read-only)", []),
    ("map", "map_blocks", "step 4: each related block's statements mapped to the claims register; an unclaimed "
     "statement becomes a new claim or an item on the strand's escalation", NARR),
    ("derive", "derive", "step 5: new, adjusted and withdrawn claims, each resting on observations or verses; each "
     "observation's disposition", NARR + ["ib_observation"]),
    ("rewrite", "rewrite", "step 6: blocks written anew, whole (every claim a block told accounted for); the "
     "chapters published from the database; cited verses marked citated",
     ["narrative_update", "narrative_update_ref", "narrative_section", "narrative_claim_telling",
      "narrative_claim_change", "narrative_citation", "narrative_chapter", "verse_meta"]),
    ("account", "account", "step 7: the strand from the tables, gaps as text (read-only); the same facts are the "
     "close gate", []),
]
REPORTS = {"context": "Strand context", "gather": "Strand gather", "account": "Strand account"}
UTILITIES = [
    ("strandreading", "iba/app/lib/strandreading.py", "strandreading.py -- the reading process (escalation #2172): "
     "define a strand, then context, record, gather, map, derive, rewrite and account; account_gaps() is the close "
     "gate. Observations through recordingpass, the narrative through narrativeregister.", 0, None),
    ("handlers_strandreading", "iba/app/handlers/strandreading.py", "handlers/strandreading.py -- the run.py "
     "handlers for work package strand-reading (one per Strand-Reading.ps1 step); the logic is in "
     "lib/strandreading.py (escalation #2172).", 0, None),
    ("Strand-Reading.ps1", "iba/app/ps/Strand-Reading.ps1", "PS entry point for the reading process (escalation "
     "#2172); every step dispatches through run.py, work package strand-reading.", 1,
     "thin wrapper; config is read by the handlers through run.py"),
]
GATE_MSG = ("the escalation that records a strand reaches completed or closed only when every hit has a face or a "
            "reason and every observation a disposition -- #2172 safeguard 5 (Strand-Reading.ps1 -Step Account "
            "lists the gaps)")
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
B76_OLD = "through `Narrative-Register.ps1` or directly"
B76_NEW = "through `Narrative-Register.ps1` and `Strand-Reading.ps1` (the narrative itself: -Step Rewrite) or directly"


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Strand-Reading.ps1",
                                                       "runs_over": "none", "chained": 0, "inactive": 0}))
    for i, (step, fn, does, grants) in enumerate(STEPS):
        sid = f"strand_reading.{step}"
        if not has("SELECT 1 FROM cfg_step WHERE step=?", sid):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": sid,
                                                   "handler": f"iba.app.handlers.strandreading:{fn}", "scope": "none",
                                                   "does": f"{does} -- {SEE}", "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", sid):
            ops.append(("cfg_on_fail", "insert", {}, {"step": sid, "condition": "refused", "path": "report-continue",
                                                      "resolver": None, "message": REFUSED, "route": "terminal",
                                                      "inactive": 0}))
        for t in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", sid, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": sid, "table_name": t, "database": "iba",
                                                              "inactive": 0}))
        if step in REPORTS and not has("SELECT 1 FROM cfg_report WHERE step=?", sid):
            ops.append(("cfg_report", "insert", {}, {"step": sid, "title": REPORTS[step], "show_toc": 0,
                                                     "footer_text": None, "output_kind": "md", "naming_scheme": "dated",
                                                     "archive_dir": "archive", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='strand_reading.output_dir'"):
        ops.append(("cfg_setting", "insert", {}, {
            "key": "strand_reading.output_dir", "value": '"outputs/strand-reading"', "module": "strand_reading",
            "inactive": 0, "use": "where Strand-Reading.ps1 writes each strand's context, gather and account files, "
                                  "one folder per strand (escalation #2172)"}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    for action in ("update", "resolve_self_correctable"):
        if not has("SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND check_kind='strand_account_clean'",
                   action):
            ops.append(("cfg_escalation_requirement", "insert", {}, {
                "action": action, "field": "state", "condition_key": "always", "message": GATE_MSG, "active": 1,
                "check_kind": "strand_account_clean"}))
    for ref in ("B:76", "B:77", "B:78"):
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value=?", ref,
                   "Strand-Reading.ps1"):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": ref, "scope_kind": "ps",
                                                         "scope_value": "Strand-Reading.ps1", "inactive": 0}))
    r = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=76").fetchone()
    if r and B76_OLD in r[0]:
        ops.append(("cfg_behaviour_rule", "update", {"id": 76}, {"rule_text": r[0].replace(B76_OLD, B76_NEW)}))
    r = conn.execute("SELECT purpose FROM cfg_utility WHERE module='narrativeregister'").fetchone()
    if r and "Record" in r[0]:
        ops.append(("cfg_utility", "update", {"module": "narrativeregister"}, {
            "purpose": "narrativeregister.py -- the narrative claim register in iba.db (escalation #2110): the reference "
                       "parser and book-alias map, the register actions (AddClaim, Edit, Tell, Untell, Withdraw, "
                       "EditNote, AddChapter, EditChapter, EditSection, Find, History, Check), Export of the three "
                       "published files, and the narrative held as blocks: rewrite() and publish_chapter() (#2172). "
                       "See USER-GUIDE.md and GOVERNANCE.md."}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2172: work package strand-reading, its steps, grants, "
                       f"reports and setting; the strand close gate; rule links; run_id {RUN_ID}. inactive=1 once "
                       f"applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
