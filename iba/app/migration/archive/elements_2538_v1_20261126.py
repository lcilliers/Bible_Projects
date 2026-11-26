"""elements_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "Build ReadElements"; design outputs/escalation/2538-read-commands-design-v2-20261125.md, command 9;
specification v5 section C1).

Registers the read command of step 3.1, the elements of one subgroup: ReadElements / RecordElements (lib/readcommands.py, handlers collection.read_elements and
collection.record_elements, Collection-Build.ps1 -Action ReadElements / RecordElements).
  cfg_setting layer.read_types   adds the instruction of the elements read (`elements`, command ReadElements, item subgroup-analysis); the other reads are kept as they are
  cfg_step    collection.read_elements, collection.record_elements
  cfg_write_grant  the tables each step writes
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/elements_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-ELEMENTS-20261126"
MODULE = "elements_2538_v1_20261126"

ELEMENTS = {
    "step": "3.1", "item": "subgroup-analysis", "command": "ReadElements", "items": ["subgroup-analysis"], "lexicon_chars": 500, "package_max_chars": 160000,
    "what": "Step 3.1, the elements of one subgroup (stage 4, C1; the end of the loop for the subgroup): what the evidence of the subgroup shows of the elements of a behaviour of the inner "
            "being. The input is the evidence observations of the subgroup by marker (`to_take_up`, the senses first, then the 2.1 findings and the older evidence), not the verses; the "
            "verses are kept for an occasional read-back. A finding is a building block, never a claim about the behaviour as a whole (that is stage 5).",
    "read": [
        "Read the observations to take up, in order: the senses (1.1) and their enrichments (1.2) first, then the 2.1 findings (pairings, qualifiers, entities, direction, double meanings), "
        "then the older evidence. The inner-being workings work more with the senses than with the surfaces, so findings rest on the senses first.",
        "For each item a finding may use (`uses`): what is done and its mode (operation, with its chain), whether a refusal or a pursuit (polarity), what it is directed at (object), the "
        "outward act (enactment), the other party with the route (party), the circumstance, and what a qualifier or a variation of the word gives the working (role, the dimension). "
        "Never the meaning of the word (stage 1).",
        "Read the older inner-being observations (`older_inner_being`) with them: each is considered first, accepted with a trace to evidence, restated where it says more than the "
        "evidence, consumed where a finding says the same, merged, or deleted where it cannot be made true.",
        "Go back to a verse (`verses`) only where the evidence does not settle the question, and say why.",
    ],
    "write": [
        "Fill `answer.findings`: each one observation, with a `key` unique in the answer, `kind` (of the item's kinds), `text`, `basis` (stated or read), `parts` with `item` (one of "
        "`uses`) and what the item needs (with `grounds`), and `nodes`: a `traced` node on each observation it rests on (from `to_take_up` or `may_rest_on_besides`) and an `occurrence` "
        "node, with its `role` chosen from the verse (characteristic, qualifier, object, relational target, enactment or standalone), on the occurrences those observations cover.",
        "An occurrence outside the observations a finding rests on is allowed only with a `read_back` entry on the finding: {verse: the osis id, why}.",
        "`not_used`: {observation id: reason} for every observation to take up that no finding rests on. Every one is rested on or declared, never both.",
        "`older`: answer, once, each older inner-being observation (`older_inner_being`) that has a node on an occurrence your findings name (RW-13; the record lists any it misses, and "
        "refuses an answer to one on no named occurrence: those are shown, not demanded, IB-05): keep (with nature inner_being: it stands, traced to evidence), restate, merge, consume "
        "(carriers [\"this\"] or ids, mapping), delete_neither, or defer (collection, nature, finding).",
        "`existing`: answer every earlier reading (`earlier_readings`: inner being of an earlier grouping on these occurrences) with accept, modify, delete, merge or leave, and its reason.",
        "The text says what the evidence shows of the element; it names its verses; it never restates a verse and never states the behaviour as a whole.",
        "Then: Collection-Build.ps1 -Action RecordElements -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.",
    ],
    "rules": ["IB-02", "IB-03", "IB-04", "IB-05", "IB-07", "RG-03", "RG-04", "RG-06", "RG-10", "RG-11", "RG-13", "RG-24", "RG-25", "RO11", "RW-03", "RW-04", "RW-12", "VA-05"],
}
READ_TYPES_USE_ADD = " The elements read (step 3.1) is one package for the subgroup, since a 3.1 row is recorded whole: package_max_chars is its largest size, lexicon_chars the meaning range shown for each code (the full lexicon is read at 1.2)."
STEPS = [
    ("collection.read_elements", "iba.app.handlers.collectionbuild:read_elements", "utility",
     "the package of step 3.1 of one subgroup (-Collection -Subgroup): its evidence observations to take up and those it may rest on, the older inner-being observations to answer, its "
     "definition, meaning by code and verses, with the instruction from cfg_setting layer.read_types; opens 3.1 for the subgroup if needed -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_elements", "iba.app.handlers.collectionbuild:record_elements", "operations",
     "check a filled ReadElements answer whole and write it through the recorder of stage 4 (layerinner.record); validate the 3.1 row; print the next command; -Check previews -- see "
     "lib/readcommands.py (escalation #2538)"),
]
TABLES = ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]


def plan(conn):
    ops = []
    rt_ = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if rt_ is None:
        raise SystemExit("cfg_setting layer.read_types is missing: the earlier #2538 migrations come first")
    types = json.loads(rt_[0])
    use = rt_[1] if READ_TYPES_USE_ADD in (rt_[1] or "") else (rt_[1] or "") + READ_TYPES_USE_ADD
    if types.get("elements") != ELEMENTS or use != rt_[1]:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps({**types, "elements": ELEMENTS}, ensure_ascii=False), "use": use}))
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
                                                  "purpose": "migration of escalation #2538: registers ReadElements / RecordElements (layer.read_types elements, two cfg_step rows, write grants)",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-elements-apply', named=True)}")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
