"""gates_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "Build B4 and B5 first"; specification v5 sections B4 and B5).

Registers the sweep (B4) and the evidence validation (B5) of a subgroup as the gates at the end of step 2.1, before 3.1, each with its read command:
  cfg_setting layer.reading     two ledger-only items, sweep and evidence-validation, added to step 2.1 (one row for each subgroup; 2.1 closes only when both are answered and validated,
                                so 3.1, which needs 2.1 closed, waits for them)
  cfg_setting layer.read_types  the instructions of the two reads (sweep, evidence); and for every read its `command` and the `items` it answers, from which LayerNext names the command
  cfg_step    collection.read_sweep, collection.record_sweep, collection.read_evidence, collection.record_evidence
  cfg_write_grant  the tables each step writes
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/gates_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-GATES-20261126"
MODULE = "gates_2538_v1_20261126"

ITEMS = {
    "sweep": {"kind": "sweep", "ledger_only": True, "none_allowed": False, "member_role": "lexical",
              "asks": "The sweep (B4): are any older observations on the subgroup's occurrences still unmarked after B1 to B3, or carried to the sweep? Judge each by content: evidence or inner being "
                      "(marked), neither (deleted with its nodes here), or another collection's (marked and deferred to it). Answered by ReadSweep and RecordSweep."},
    "evidence-validation": {"kind": "validation", "ledger_only": True, "none_allowed": False, "member_role": "lexical",
                            "asks": "The evidence validation (B5): do the code checks of the subgroup's observations pass, and is every evidence observation true, founded and coherent with the "
                                    "others? Read each and record it; repair what is not. Inner being is not judged here. Answered by ReadEvidence and RecordEvidence."},
}
READS = {
    "sweep": {
        "step": "2.1", "item": "sweep", "command": "ReadSweep", "items": ["sweep"], "actions": ["keep", "merge", "consume", "delete_neither", "defer"],
        "what": "The sweep (B4) of one subgroup, after its 2.1 rows: every observation of the subgroup's scope still unmarked after B1 to B3 -- older observations on its occurrences that B1 "
                "carried forward and B2 and B3 did not take up, any carried to the sweep, and any other unmarked observation of the scope (for example the reading of an earlier grouping). Each is "
                "judged by its content. End state: none of the subgroup's observations is unmarked, except one deferred to a named collection.",
        "read": [
            "Take one older observation at a time (`older`): its text, its stage and kind, its verses, how many of its nodes are on this subgroup's occurrences and how many elsewhere, and the "
            "collections its nodes belong to.",
            "Judge it by what it states, not by its stage or kind: does it state what the data are or show, tied to a verse (evidence)? how something works in the inner being, based on evidence "
            "(inner being)? or neither?",
        ],
        "write": [
            "Fill `answer.older`, one entry for each observation, each answered once, with `reason`: what it states and why it is so judged.",
            "merge, with `into`: a live observation of the subgroup says the same in the same words. consume, with `carriers` (observation ids) and `mapping`: live observations already state "
            "what it says; every word occurrence of it must be on a live node of a carrier (VA-03), then it is deleted. "
            "keep, with `nature` evidence or inner_being: it stands as it is (an inner-being one waits for 3.1). delete_neither: it is neither evidence nor inner being; it is commented, then "
            "deleted with its nodes here (one held by other subgroups or collections loses only the nodes here). defer, with `collection`, `nature` and `finding`: another collection owns it; it is "
            "marked now and the finding is left to that collection.",
            "Then: Collection-Build.ps1 -Action RecordSweep -File <the answer file> (-Check to preview). The record refuses the whole file on any fault; every unmarked observation must be answered.",
        ],
        "rules": ["VA-04", "VA-05", "RW-01", "RS-04"],
    },
    "evidence": {
        "step": "2.1", "item": "evidence-validation", "command": "ReadEvidence", "items": ["evidence-validation"], "batch_observations": 40, "package_max_chars": 60000,
        "what": "The evidence validation (B5) of one subgroup, after its sweep, the gate before 3.1: the code checks of its observations (shown in `code_checks`), and the reading of every evidence "
                "observation of the subgroup (its own of S1 to 2.1, and the older ones on its occurrences kept as evidence) for whether it is true, founded and coherent with the others. Inner "
                "being is not judged here; the two validations are never run together.",
        "read": [
            "Read the code checks first: a failing check names observations to repair (unmarked, no node, a word node missing a column without its reason, a trace to a deleted observation, two "
            "of one text, a B1 observation no sense traces, a sense the 2.1 observations on its occurrences do not trace, an older observation left open).",
            "Take one observation at a time (`observations`, in the order of the steps): its text, basis and grounds against its verses (`verses`) and the observations it traces. Is it true of those "
            "verses? Does it say more than they show? Does it contradict another observation of the subgroup?",
        ],
        "write": [
            "Fill `answer.observations`, one entry for each observation of the package: verdict true, with `why` (what in the verses and the data bears it out); or verdict repair, with `why` (what "
            "is wrong) and `actions`: the actions of the validation that repair it (cfg_setting validate.reading actions, each with its parameters, for example {\"action\": \"restate\", \"oid\": id, "
            "\"new_text\": ..., \"checked\": ..., \"reason\": ...}, or delete_neither, complete_node, add_trace).",
            "A repair is checked as it is written; an observation that cannot be made true is deleted with its reason.",
            "Then: Collection-Build.ps1 -Action RecordEvidence -File <the answer file> (-Check to preview), and ReadEvidence again until every evidence observation is read; the gate passes when "
            "all are read and the code checks pass.",
        ],
        "rules": ["VA-01", "VA-02", "VA-03", "VA-04", "VA-05", "VA-06", "RW-01", "RW-03", "RW-04", "RW-06", "RW-11"],
    },
}
COMMANDS = {"words": ("ReadWords", ["word-sense"]), "senses": ("ReadSenses", ["group-definition"]), "enrichment": ("ReadEnrichment", ["strong-enrichment"]),
            "structure": ("ReadStructure", ["double-meaning", "qualifier", "entity", "direction", "pairing"])}
READ_TYPES_USE = ("the reads of the layered reading, one command each (escalation #2538; lib/readcommands.py; design outputs/escalation/2538-read-commands-design-v2-20261125.md): for each read "
                  "(words: step S1; senses: 1.1; enrichment: 1.2; structure: 2.1; sweep and evidence: the gates at the end of 2.1, B4 and B5) the step and item it answers, its `command` and the "
                  "`items` it answers (LayerNext names the command of the next open item from these), what the read is, how to read, what to write, the method rules it keeps (keys of "
                  "cfg_method_rule, whose text the package reads live), and its sizes (words: batch_words; structure: batch_rows; evidence: batch_observations; senses and enrichment: "
                  "lexicon_chars and full_lexicon; senses, enrichment, structure and evidence: package_max_chars, the largest package); the sweep's `actions`, the answers it takes; limits: "
                  "package_max_chars (the words of one words package) and read_max_seconds (a read that takes longer is refused and writes nothing)")
STEPS = [
    ("collection.read_sweep", "iba.app.handlers.collectionbuild:read_sweep", "utility",
     "the sweep (B4) of one subgroup after its 2.1 rows (-Collection -Subgroup): the package of its older observations still unmarked, with the instruction from cfg_setting layer.read_types; "
     "with none left, the sweep row is answered as such and validated -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_sweep", "iba.app.handlers.collectionbuild:record_sweep", "operations",
     "check a filled ReadSweep answer whole and write it in one transaction (keep, delete_neither, defer); validate the sweep row; print the next command; -Check previews -- see "
     "lib/readcommands.py (escalation #2538)"),
    ("collection.read_evidence", "iba.app.handlers.collectionbuild:read_evidence", "utility",
     "the evidence validation (B5) of one subgroup after its sweep (-Collection -Subgroup): the code checks and the package of the next evidence observations not yet read, with the "
     "instruction from cfg_setting layer.read_types; with all read and the checks passing, the row is answered and validated -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_evidence", "iba.app.handlers.collectionbuild:record_evidence", "operations",
     "check a filled ReadEvidence answer whole: the repairs written through the validation actions, each observation logged as read (evidence_read); validate the gate when all is read and "
     "the checks pass; print the next command; -Check previews -- see lib/readcommands.py (escalation #2538)"),
]
TABLES = ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]


def plan(conn):
    ops = []
    lr_ = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading'").fetchone()
    rt_ = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if lr_ is None or rt_ is None:
        raise SystemExit("cfg_setting layer.reading or layer.read_types is missing: the earlier #2538 migrations come first")
    reading = json.loads(lr_[0])
    new_r = json.loads(lr_[0])
    new_r["items"].update(ITEMS)
    for st in new_r["steps"]:
        if st["key"] == "2.1":
            rest = [i for i in st["items"] if i not in ITEMS]
            at = rest.index("old-observation") if "old-observation" in rest else len(rest)
            st["items"] = rest[:at] + list(ITEMS) + rest[at:]
    if new_r != reading:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new_r, ensure_ascii=False)}))
    types = json.loads(rt_[0])
    new_t = json.loads(rt_[0])
    for k, (cmd, items) in COMMANDS.items():
        if k in new_t:
            new_t[k] = {**new_t[k], "command": cmd, "items": items}
    new_t.update(READS)
    if new_t != types or rt_[1] != READ_TYPES_USE:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(new_t, ensure_ascii=False), "use": READ_TYPES_USE}))
    top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
    for step, handler, kind, does in STEPS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            top += 1
            ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none", "does": does, "inactive": 0, "kind": kind}))
        for t in TABLES:
            if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (step, t)).fetchone():
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": t, "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of escalation #2538: the sweep (B4) and the evidence validation (B5) as gate items of step 2.1 with their read commands (layer.reading, layer.read_types, four cfg_step rows, write grants)",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-gates-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rg")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rg")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rg")
        conn.execute("RELEASE rg")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
