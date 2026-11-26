"""enrichment_2538_v1_20261126.py -- escalation #2538 (design outputs/escalation/2538-read-commands-design-v2-20261125.md, command 5; researcher 2026-11-26: "Approve, apply live"
for ReadSenses, with the next command, ReadEnrichment, built in the same form).

Registers the third read command of the layered reading: ReadEnrichment / RecordEnrichment (step 1.2, what the codes of each sense say; lib/readcommands.py, handlers
collection.read_enrichment and collection.record_enrichment, Collection-Build.ps1 -Action ReadEnrichment / RecordEnrichment).
  cfg_setting layer.read_types   adds the instruction of the enrichment read (`enrichment`); the other reads and the limits are kept as they are
  cfg_step    collection.read_enrichment, collection.record_enrichment
  cfg_write_grant  the tables each step writes (as the other read commands)
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/enrichment_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-ENRICHMENT-20261126"

ENRICHMENT = {
    "step": "1.2", "item": "strong-enrichment", "full_lexicon": True, "lexicon_chars": 700, "package_max_chars": 110000,
    "what": "Step 1.2, the enrichment of one subgroup (stage 1, B2): for each sense of step 1.1, what the Strong's codes of its occurrences say. The lexicon is the point of this read. "
            "Nothing here says what a sense does for the inner being; that begins at step 3.1.",
    "read": [
        "Take one sense at a time (`senses`: its text from step 1.1, its codes, words and occurrences).",
        "Read the lexicon of each of its codes (`codes`: sense_head, meaning_range, lsj, mounce, related), the three meaning sources read together, none picked and the others dropped.",
        "Validate the sense against its codes: do the lexicon entries bear out the meaning the sense names? Where they do not, say so in the enrichment; the sense is not changed here.",
        "Where one surface carries several codes in the sense, read what each code adds.",
    ],
    "write": [
        "Fill `answer.enrichments`: one entry for each sense, named by `sense` (the id of its 1.1 observation); every sense has exactly one. The enrichment takes the sense's occurrences.",
        "kind: enrichment. obs_text: a short definition from the lexicon entries; names the codes that link the sense to its usage and what different codes of one surface add; names "
        "verses the sense holds in, as the package writes the references (for example Psa 77:6); concise; never the lexicon copied whole, never a verse restated, never what the sense "
        "does for the inner being.",
        "basis: read, with `grounds`: words copied exactly from the lexicon of a code of the sense (sense_head, meaning_range, lsj or mounce; the record checks them); or stated, where a verse says it.",
        "Where the lexicon does not bear out the sense, the enrichment says so with its grounds; a missing lexicon entry is named, never filled from memory (RW-11).",
        "`older`: answer each older observation shown, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` [\"this\"] "
        "for this answer's enrichments or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` 2.1 and `reason`), defer (with `collection`, `nature`, `finding`).",
        "Then: Collection-Build.ps1 -Action RecordEnrichment -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.",
    ],
    "rules": ["RG-08", "RG-21", "RO11", "RW-03", "RW-04", "RW-09", "RW-11", "RW-13", "RS-04", "LR-02", "VA-03", "VA-04"],
}
READ_TYPES_USE = ("the reads of the layered reading, one command each (escalation #2538; lib/readcommands.py; design outputs/escalation/2538-read-commands-design-v2-20261125.md): for each read "
                  "(words: step S1; senses: step 1.1; enrichment: step 1.2) the step and item it answers, what the read is, how to read, what to write, the method rules it keeps (keys of "
                  "cfg_method_rule, whose text the package reads live), and its sizes (words: batch_words; senses and enrichment: lexicon_chars, the lexicon shown for each code, full_lexicon, "
                  "whether the three sources are shown (enrichment) or only the head and range (senses), and package_max_chars, the largest package, a subgroup being read whole); limits: "
                  "package_max_chars (the words of one words package) and read_max_seconds (a read that takes longer is refused and writes nothing)")
STEPS = [
    ("collection.read_enrichment", "iba.app.handlers.collectionbuild:read_enrichment", "utility",
     "write the package of the enrichment of one subgroup (step 1.2; -Collection -Subgroup): the instruction of this read from cfg_setting layer.read_types with its rules read live "
     "from cfg_method_rule, every 1.1 sense of the subgroup with its codes and occurrences, the lexicon of every code, the older observations, and the answer to fill, to "
     "layer.working_dir; opens 1.2 for the subgroup if it is not open -- see lib/readcommands.py (escalation #2538)"),
    ("collection.record_enrichment", "iba.app.handlers.collectionbuild:record_enrichment", "operations",
     "check a filled ReadEnrichment answer whole (one enrichment for each 1.1 sense, taking its occurrences) and write it through the recorder of the layered reading in one "
     "transaction; validate the subgroup's 1.2 row; print the next command; -Check previews -- see lib/readcommands.py (escalation #2538)"),
]
GRANTS = {"collection.read_enrichment": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"],
          "collection.record_enrichment": ["collection_layer_item", "ib_observation", "ib_node", "ib_observation_change"]}
MODULE = "enrichment_2538_v1_20261126"


def plan(conn):
    ops = []
    cur = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if cur is None:
        raise SystemExit("cfg_setting layer.read_types is missing: readwords_2538_v1_20261125.py and senses_2538_v1_20261125.py come first")
    val = json.loads(cur[0])
    if val.get("enrichment") != ENRICHMENT or cur[1] != READ_TYPES_USE:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps({**val, "enrichment": ENRICHMENT}, ensure_ascii=False), "use": READ_TYPES_USE}))
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
                                                  "purpose": "migration of escalation #2538: registers ReadEnrichment / RecordEnrichment (layer.read_types enrichment, two cfg_step rows, write grants)",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-enrichment-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT re")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE re")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO re")
        conn.execute("RELEASE re")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
