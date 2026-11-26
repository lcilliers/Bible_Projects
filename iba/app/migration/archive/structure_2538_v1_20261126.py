"""structure_2538_v1_20261126.py -- escalation #2538 (design outputs/escalation/2538-read-commands-design-v2-20261125.md, command 6; researcher 2026-11-26: "Approve, apply live"
for ReadEnrichment, with the next command, ReadStructure, built in the same form).

Registers the fourth read command of the layered reading: ReadStructure / RecordStructure (step 2.1, what stands with the subgroup in each verse; lib/readcommands.py, handlers
collection.read_structure and collection.record_structure, Collection-Build.ps1 -Action ReadStructure / RecordStructure [-Item]).
  cfg_setting layer.read_types   adds the instruction of the structure read (`structure`); the other reads and the limits are kept as they are
  cfg_step    collection.read_structure, collection.record_structure
  cfg_write_grant  the tables each step writes (as the other read commands)
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/structure_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-STRUCTURE-20261126"
MODULE = "structure_2538_v1_20261126"

STRUCTURE = {
    "step": "2.1", "batch_rows": 15, "package_max_chars": 60000,
    "what": "Step 2.1, the structure of one subgroup (stage 1, B3): what stands with the subgroup's words in each verse, read from the stored structure. One item at a time: "
            "double-meaning (a surface with more than one code), qualifier (negators and the word each reaches, adjectives, adverbs, prepositional qualifiers), entity (who is named or "
            "referred to), direction (from whom to whom, by the grammar), pairing (one row for each partner collection: its words in the verses shared with the subgroup). "
            "Nothing here says what anything does for the inner being; that begins at step 3.1.",
    "read": [
        "Take one row at a time (`rows`): what it asks, its occurrences (`as`: member, the subgroup's word; partner, the other word), and its verses.",
        "Read each verse (`verses`) from its stored structure, one line for each word: * marks an occurrence of the subgroup; then the position, surface, Strong's code and morph, and what "
        "the pairing makes of the word (its type, the qualifier it carries, a negator, a party, the collections of a word of another collection). Nothing is evaluated that is not stored.",
        "Where each word stands: its side and distance from the subgroup's word, from the positions. Adjacency is not scope: a negator or qualifier is read for the word it reaches by the grammar.",
        "A pairing row shows the WordNet control for its partner collection: a pairing WordNet gives and the verses do not show is one to look for; a pairing only the verses show has no control.",
        "Differences in meaning are read from the base data (the Strong's code, the morph, the construction), not from the English alone. The subgroup's 1.1 senses (`senses`) are what the findings build on.",
    ],
    "write": [
        "Fill `answer.rows`: for each row, disposition observed with its `findings`, or none with its `reason` (where the row allows none: nothing of the item stands with the subgroup in its verses).",
        "One finding for each distinct thing the structure shows; the same finding in several verses is ONE finding naming all its occurrences; a verse that shows something different is its own finding. "
        "Together the findings name every occurrence of the row (occurrence ids or verse references), each in one finding.",
        "kind: as the template gives it (pairing; relation for direction; face for double-meaning). obs_text: concise; names the verses it holds in, as the package writes the references "
        "(for example Act 18:4); states what the structure shows (which word, where it stands, what it reaches or gives by the grammar); never a verse restated, never what it does for the inner being.",
        "basis: stated (the verse says it) or read (read from the structure), with `grounds`: words copied exactly from the verses it is tied to (the record checks them).",
        "Each subgroup's surface has its own finding; none joins two subgroups. A data error is named in grounds, not fixed.",
        "`older`: answer each older observation shown under the row, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` "
        "[\"this\"] or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` and `reason`), defer (with `collection`, `nature`, `finding`). One listed under another row is answered there.",
        "Then: Collection-Build.ps1 -Action RecordStructure -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.",
    ],
    "rules": ["RG-14", "RG-16", "RG-21", "RO11", "RW-03", "RW-04", "RW-08", "RW-09", "RW-11", "RW-13", "RS-04", "LR-02", "LR-03", "DA-02", "VA-03", "VA-04"],
}
READ_TYPES_USE = ("the reads of the layered reading, one command each (escalation #2538; lib/readcommands.py; design outputs/escalation/2538-read-commands-design-v2-20261125.md): for each read "
                  "(words: step S1; senses: step 1.1; enrichment: step 1.2; structure: step 2.1) the step and item it answers, what the read is, how to read, what to write, the method rules it "
                  "keeps (keys of cfg_method_rule, whose text the package reads live), and its sizes (words: batch_words; structure: batch_rows; senses and enrichment: lexicon_chars, the lexicon "
                  "shown for each code, full_lexicon, whether the three sources are shown (enrichment) or only the head and range (senses); senses, enrichment and structure: package_max_chars, "
                  "the largest package); limits: package_max_chars (the words of one words package) and read_max_seconds (a read that takes longer is refused and writes nothing)")
STEPS = [
    ("collection.read_structure", "iba.app.handlers.collectionbuild:read_structure", "utility",
     "write the package of the next rows of step 2.1 of one subgroup, one item at a time (-Collection -Subgroup [-Item]): the instruction of this read from cfg_setting layer.read_types "
     "with its rules read live from cfg_method_rule, what each row asks, its occurrences, the WordNet control of a pairing, the older observations, the verses with their stored "
     "structure and the 1.1 senses, and the answer to fill, to layer.working_dir; opens 2.1 for the subgroup if it is not open -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_structure", "iba.app.handlers.collectionbuild:record_structure", "operations",
     "check a filled ReadStructure answer whole and write it through the recorder of the layered reading in one transaction; validate the subgroup's rows; print the next command; "
     "-Check previews -- see lib/readcommands.py (escalation #2538)"),
]
GRANTS = {"collection.read_structure": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"],
          "collection.record_structure": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]}


def plan(conn):
    ops = []
    cur = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if cur is None:
        raise SystemExit("cfg_setting layer.read_types is missing: the earlier #2538 read-command migrations come first")
    val = json.loads(cur[0])
    if val.get("structure") != STRUCTURE or cur[1] != READ_TYPES_USE:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps({**val, "structure": STRUCTURE}, ensure_ascii=False), "use": READ_TYPES_USE}))
    top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
    for step, handler, kind, does in STEPS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            top += 1
            ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none", "does": does, "inactive": 0, "kind": kind}))
    for writer, tables in GRANTS.items():
        for t in tables:
            if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (writer, t)).fetchone():
                ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": t, "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of escalation #2538: registers ReadStructure / RecordStructure (layer.read_types structure, two cfg_step rows, write grants)",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-structure-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rst")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rst")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rst")
        conn.execute("RELEASE rst")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
