"""senses_2538_v1_20261125.py -- escalation #2538 (design outputs/escalation/2538-read-commands-design-v2-20261125.md, command 4; researcher 2026-11-25: "Approve, apply live",
with the next command, ReadSenses, built in the same form).

Registers the second read command of the layered reading: ReadSenses / RecordSenses (step 1.1, the senses of one subgroup; lib/readcommands.py, handlers collection.read_senses and
collection.record_senses, Collection-Build.ps1 -Action ReadSenses / RecordSenses).
  cfg_setting layer.read_types   adds the instruction of the senses read (`senses`); the words read and the limits are kept as they are
  cfg_step    collection.read_senses, collection.record_senses
  cfg_write_grant  the tables each step writes (as collection.read_words and collection.record_words)
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/senses_2538_v1_20261125.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-SENSES-20261125"

SENSES = {
    "step": "1.1", "item": "group-definition", "lexicon_chars": 500, "package_max_chars": 100000,
    "what": "Step 1.1, the senses of one subgroup (stage 1, B2): the word readings of step S1 gathered into senses by meaning in context. A sense is one meaning, of one or several "
            "surfaces and codes. Nothing here says what a sense does for the inner being; that begins at step 3.1.",
    "read": [
        "Read every B1 observation of the subgroup (`readings`: what each word is and how it is used in its verses, with the occurrences it holds), with the sense head and meaning "
        "range of each code (`codes`).",
        "Gather by meaning in context: the readings, of any surface and any Strong's code of the subgroup, whose meaning in context is the same are one sense. The same surface may carry "
        "different senses; different surfaces may carry one. The grouping rests on the Strong's code, the lexicon and the verse, not on the English surface alone.",
        "The subgroup shows words that may relate to each other and differentiate or accentuate senses. Each sense is named for its meaning.",
        "Read the older observations (`older`) with the readings: one carried here from S1, or one that states what a sense is, is considered first, for correction rather than a new observation.",
    ],
    "write": [
        "Fill `answer.senses`, one entry for each sense. `carries`: the ids of the B1 observations it gathers; each B1 observation is carried by one sense. Where one B1 observation "
        "holds occurrences of two senses, leave it out of `carries` and name its occurrences (occurrence ids) in each sense's `occurrences`. Together every occurrence of the subgroup "
        "is in exactly one sense; an occurrence no reading holds (`occurrences_in_no_reading`) is named in a sense's `occurrences`.",
        "kind: group. obs_text: names the sense and its meaning and names verses it holds in, as the package writes the references (for example Psa 77:6); concise; never the "
        "dictionary range copied, never a verse restated, never what the sense does for the inner being.",
        "basis: read, with `grounds`: words copied exactly from the sense_head or the meaning_range of a code of the sense (the record checks them against the lexicon); or stated, "
        "where a verse says it.",
        "A surface that fits no sense is not forced into one: stop and raise it; it goes back to the grouping (Step 2) with its reason.",
        "`older`: answer each older observation shown, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` [\"this\"] "
        "for this answer's senses or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` 2.1 and `reason`), defer (with `collection`, `nature`, `finding`).",
        "Then: Collection-Build.ps1 -Action RecordSenses -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.",
    ],
    "rules": ["RG-08", "RG-15", "RG-21", "RO11", "RW-03", "RW-04", "RW-08", "RW-09", "RW-13", "RS-04", "LR-02", "VA-03", "VA-04"],
}
READ_TYPES_USE = ("the reads of the layered reading, one command each (escalation #2538; lib/readcommands.py; design outputs/escalation/2538-read-commands-design-v2-20261125.md): for each read "
                  "(words: step S1; senses: step 1.1) the step and item it answers, what the read is, how to read, what to write, the method rules it keeps (keys of cfg_method_rule, whose text "
                  "the package reads live), and its sizes (words: batch_words; senses: lexicon_chars, the meaning range shown for each code, and package_max_chars, the largest senses package, "
                  "a subgroup being read whole); limits: package_max_chars (the words of one words package) and read_max_seconds (a read that takes longer is refused and writes nothing)")
STEPS = [
    ("collection.read_senses", "iba.app.handlers.collectionbuild:read_senses", "utility",
     "write the package of the senses of one subgroup (step 1.1; -Collection -Subgroup): the instruction of this read from cfg_setting layer.read_types with its rules read live from "
     "cfg_method_rule, every B1 observation of the subgroup with the occurrences it holds, the sense head and meaning range of each code, the older observations, and the answer to "
     "fill, to layer.working_dir; opens 1.1 for the subgroup if it is not open -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_senses", "iba.app.handlers.collectionbuild:record_senses", "operations",
     "check a filled ReadSenses answer whole (each B1 observation carried by one sense, its occurrences taken from the observation) and write it through the recorder of the layered "
     "reading in one transaction; validate the subgroup's 1.1 row; print the next command; -Check previews -- see lib/readcommands.py (escalation #2538)"),
]
GRANTS = {"collection.read_senses": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"],
          "collection.record_senses": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]}


def plan(conn):
    ops = []
    cur = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if cur is None:
        raise SystemExit("cfg_setting layer.read_types is missing: readwords_2538_v1_20261125.py comes first")
    val = json.loads(cur[0])
    if val.get("senses") != SENSES or cur[1] != READ_TYPES_USE:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps({**val, "senses": SENSES}, ensure_ascii=False), "use": READ_TYPES_USE}))
    top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
    for step, handler, kind, does in STEPS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            top += 1
            ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none", "does": does, "inactive": 0, "kind": kind}))
    for writer, tables in GRANTS.items():
        for t in tables:
            if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (writer, t)).fetchone():
                ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": t, "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module='senses_2538_v1_20261125'").fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": "senses_2538_v1_20261125", "file_path": "iba/app/migration/senses_2538_v1_20261125.py",
                                                  "purpose": "migration of escalation #2538: registers ReadSenses / RecordSenses (layer.read_types senses, two cfg_step rows, write grants)",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-senses-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rs")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rs")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rs")
        conn.execute("RELEASE rs")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
