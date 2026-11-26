"""readwords_2538_v1_20261125.py -- escalation #2538 (design outputs/escalation/2538-read-commands-design-v1-20261125.md, approved 2026-11-25: "Approve, build ReadWords").

Registers the first read command of the layered reading: ReadWords / RecordWords (step S1, the words of one subgroup; lib/readcommands.py, handlers collection.read_words and
collection.record_words, Collection-Build.ps1 -Action ReadWords / RecordWords).
  cfg_setting layer.read_types   the instruction of each read (what to read, how, what to write, the rules it keeps by key) and the limits of a package (size, seconds)
  cfg_step    collection.read_words, collection.record_words
  cfg_utility readcommands
  cfg_write_grant  the tables each step writes (as collection.layer_open and collection.layer_record)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/readwords_2538_v1_20261125.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-READWORDS-20261125"

READ_TYPES = {
    "limits": {"package_max_chars": 40000, "read_max_seconds": 20},
    "words": {
        "step": "S1", "item": "word-sense", "batch_words": 12,
        "what": "Step S1, the words of one subgroup (stage 1, the lexical analysis): each word -- a surface with its lettered Strong's code -- read in the verse of each of its occurrences, "
                "for what it is and how it is used there. Nothing here says what a word does for the inner being; that begins at step 3.1.",
        "read": [
            "Take one word at a time, and within it one occurrence at a time, in the verse of that occurrence.",
            "Read the evidence in this order: the verse text and the occurrence's stored structure (morph, unit, surface_kind, negator, party_kind, narrative); then the meaning sources "
            "for the code read together (sense_head, meaning_range, lsj, mounce), none picked and the others dropped; then the English rendering against the literal sense: does the English add or hide?",
            "Judge the meaning in context from the Strong's code and the verse, not from the English surface alone. Where occurrences show different stems or voices, say whether the subject does, undergoes or causes the act.",
            "The prompts are areas to explore; a prompt that does not apply is not answered.",
        ],
        "write": [
            "Fill `answer.rows`: for each word, its `readings`. One reading for each distinct way the word is used: the occurrences where it is used the same way are listed together in "
            "that reading's `occurrences` (occurrence ids or verse references); an occurrence used differently is its own reading.",
            "kind: term; face where the use in a verse departs from the word's usual sense.",
            "obs_text: concise; names the verse or verses; states what the word is and how it is used there (its object, setting, construction, what the morph shows); never the dictionary range, never the verse restated.",
            "basis: stated (the verse says it) or read (read from the structure or the context). grounds: what in the verse shows it.",
            "Every occurrence of the word is in exactly one reading; none is left out. A homonym or a name is recorded as such; a data error is named in grounds, not fixed.",
            "`older`: the older observations on the word's occurrences. Read each with the word (they are what was recorded before) and answer each in the row's `older`, once: "
            "keep (with `nature` evidence or inner_being: it stands as it is); restate (with `nature`, `new_text` and `checked`: what in the base data the new text was checked against); "
            "merge (with `into`: a live observation saying the same); consume (with `carriers`, [\"this\"] for this row's readings or observation ids, and `mapping`: what the old one says and "
            "which carrier states each part); delete_neither (with `reason`: it is neither evidence nor inner being); carry (with `to` a later step, 1.1 or 2.1, and `reason`: what that step "
            "is to consider); defer (with `collection`, `nature` and `finding`: another collection owns the rest). An older observation listed under another word is answered there.",
            "Then: Collection-Build.ps1 -Action RecordWords -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.",
        ],
        "rules": ["RG-08", "RG-14", "RG-16", "RG-17", "RG-21", "RG-22", "RW-03", "RW-04", "RW-08", "RW-09", "RW-13", "RS-04", "VA-03", "VA-04"],
    },
}
READ_TYPES_USE = ("the reads of the layered reading, one command each (escalation #2538; lib/readcommands.py; design outputs/escalation/2538-read-commands-design-v1-20261125.md): for each read "
                  "(words, so far) the step and item it answers, the batch size, what the read is, how to read, what to write, the method rules it keeps (keys of cfg_method_rule, whose text "
                  "the package reads live) and what is not in this read; limits: package_max_chars (the largest package; a batch stops before it) and read_max_seconds (a read that takes "
                  "longer is refused and writes nothing)")
STEPS = [
    ("collection.read_words", "iba.app.handlers.collectionbuild:read_words", "utility",
     "write the package of the next words of one subgroup to read (step S1; -Collection -Subgroup): the instruction of this read from cfg_setting layer.read_types with its rules read live "
     "from cfg_method_rule, only these words' occurrences, verses and lexicon, and the answer to fill, to layer.working_dir; opens S1 for the subgroup if it is not open -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_words", "iba.app.handlers.collectionbuild:record_words", "operations",
     "check a filled ReadWords answer whole and write it through the recorder of the layered reading (observations, nodes, ledger) in one transaction; validate the subgroup's rows; "
     "print the next command; -Check previews -- see lib/readcommands.py (escalation #2538)"),
]
GRANTS = {"collection.read_words": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"],
          "collection.record_words": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]}


def plan(conn):
    ops = []
    cur = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    val = json.dumps(READ_TYPES, ensure_ascii=False)
    if cur is None:
        ops.append(("cfg_setting", "insert", {}, {"key": "layer.read_types", "value": val, "use": READ_TYPES_USE, "module": "layer", "inactive": 0}))
    elif cur[0] != val:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": val, "use": READ_TYPES_USE}))
    top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
    for step, handler, kind, does in STEPS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            top += 1
            ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none", "does": does, "inactive": 0, "kind": kind}))
    for writer, tables in GRANTS.items():
        for t in tables:
            if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (writer, t)).fetchone():
                ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": t, "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module='readcommands'").fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": "readcommands", "file_path": "iba/app/lib/readcommands.py",
                                                  "purpose": "readcommands.py -- one command for each read of the layered reading (escalation #2538): a package for the reader (the instruction of the read, only its unit's data, the answer) and the record of the answer through the recorder, naming the next command.",
                                                  "inactive": 0, "config_exempt": 1,
                                                  "config_exempt_reason": "the reads, their instructions, rules, batch sizes and limits are read from cfg_setting layer.read_types and layer.reading; the code holds no tunable value",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module='readwords_2538_v1_20261125'").fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": "readwords_2538_v1_20261125", "file_path": "iba/app/migration/readwords_2538_v1_20261125.py",
                                                  "purpose": "migration of escalation #2538: registers ReadWords / RecordWords (layer.read_types, two cfg_step rows, write grants, the readcommands module)",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-readwords-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rw")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rw")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rw")
        conn.execute("RELEASE rw")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
