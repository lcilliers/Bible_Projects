"""behaviours_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "readmatches and the validation after stage 4 cannot be planned as yet, it is
gated by a state that have all collections completed.  however, step 3.2 is a fundamental part of the collection process and must be codified. it is not a process that is
left open for interactive chat, although it is reading based and the method must be called from within a chat.").

Registers step 3.2 as a read command of the package (design v2 command 10):
  cfg_setting      layer.read_types `behaviours`: the instruction of ReadBehaviours (what to read, how, what to write, the rules it keeps) and its limits
  cfg_setting      layer.reading step 3.3 `read_command_deferred`: the researcher's ruling, so that the check that every step has its read command
                   (cfgquality.find_analytic_guide_gaps) names 3.3 as deferred, not missing
  cfg_step         collection.read_behaviours, collection.record_behaviours, collection.sweep_superseded (the close of 3.1: researcher 2026-11-26, "step 3.1 is
                   incomplete. it did not sweep the observations that are not valid, and removed them.")
  cfg_method_rule  IB-08 what-a-behaviour-is (the approach of the 3.2 draft, approved by the researcher 2026-11-26: "the approach and observation results for 3.2
                   looks good.")
  cfg_setting      layer.read_types guide.also gains SweepSuperseded
  cfg_write_grant  the tables each writes (as ReadElements and RecordElements)
  cfg_utility      this migration's own row
Written through configmaint.apply_logged. Named snapshot before a live apply; after the live apply the file archives itself. Idempotent.
Usage: python iba/app/migration/behaviours_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-BEHAVIOURS-20261126"
MODULE = "behaviours_2538_v1_20261126"
RULING = ('researcher 2026-11-26 (#2538): "readmatches and the validation after stage 4 cannot be planned as yet, it is  gated by a state that have all '
          'collections completed."')
BEHAVIOURS = {
    "step": "3.2", "item": "collection-gathering", "command": "ReadBehaviours", "items": ["collection-gathering"],
    "package_max_chars": 400000, "read_max_seconds": 60,
    "what": ("Step 3.2, the behaviours of the collection (stage 4, C2), read once every subgroup is through 3.1 and the sweep has closed 3.1: which behaviours of the inner "
             "being the collection shows, DISCOVERED from the element observations of its subgroups. The input is the 3.1 findings of the current subgroups (`to_take_up`), "
             "each whole with its subgroups and occurrences, not the verses. A behaviour gathers elements; it is "
             "never a claim about what the behaviour is (that is stage 5)."),
    "read": ["Apply IB-08 (what a behaviour is). Read every operation finding first, across all the subgroups (`subgroups` lists the findings on each), and write down its core "
             "operation in a few words, ignoring the word used for it: who or what does what.",
             "Put together the operation findings whose core operation is the same, even where they sit in different subgroups: the subgroups were made from the dictionary meaning "
             "of the words (stage 2), the behaviours from what the elements show the person doing.",
             "Attach to each group the other findings (object, polarity, enactment, role, circumstance, chain) that describe the same verses and the same act: each goes with the "
             "operation it describes, not with its subgroup.",
             "Test each group against IB-08: one operation? A group that holds two operations is split; two groups that hold one operation are joined.",
             "Name each behaviour by what is done, never by what it means for the inner being (stage 5).",
             "Read across the behaviours for what relates them: a chain from one into another, a party that acts on several (with its route, B:72), a dimension that runs through "
             "several (pursuit or refusal), a circumstance named in several.",
             "Every finding is in exactly one behaviour, or declared not gathered with its reason: the not gathered are those that show no working of a human inner being (another "
             "being in its own right, route A; a word that is not an act of the mind). Go back to a verse only where the findings do not settle a question, and say why (read_back)."],
    "write": ["Fill `answer.findings`. Each behaviour is a finding of the item flag (`parts.item` flag, `parts.flag_type` discovery, `kind` statement) that names the behaviour, says "
              "which elements belong together and why, and gathers its element observations by a `traced` node on each. At least one behaviour, or `disposition` none with its reason.",
              "What relates elements across subgroups is a finding of operation (with its mode), chain (kind link), party (with the route, B:72), circumstance or role, each "
              "resting on the observations it relates by traced nodes.",
              "Every finding also has `occurrence` nodes, with their `role`, on occurrences the observations it rests on cover (each observation's `occurrences`); an occurrence "
              "outside them needs a `read_back` entry {verse: the osis id, why}.",
              "`not_gathered`: {observation id: reason} for every observation to take up that no finding rests on. Every one is rested on or declared, never both.",
              "`older`: answer each older unsettled observation on an occurrence your findings name (keep, restate, merge, consume, delete_neither, defer, carry).",
              "The text says what the observations show; it names its verses; it never restates a verse and never formulates the claim.",
              "Then: Collection-Build.ps1 -Action RecordBehaviours -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault."],
    "rules": ["IB-02", "IB-03", "IB-04", "IB-06", "IB-07", "IB-08", "RG-03", "RG-04", "RG-06", "RG-10", "RG-11", "RG-13", "RO11", "RW-03", "RW-04", "RW-12", "VA-05", "B:72"],
}
STEPS = [("collection.read_behaviours", "iba.app.handlers.collectionbuild:read_behaviours", "utility",
          "the package of step 3.2 of a collection (-Collection): every inner-being observation of the collection to take up, each whole with its subgroups and occurrences, the "
          "subgroups with their definitions, the older unsettled observations, with the instruction from cfg_setting layer.read_types; opens 3.2 if needed -- see "
          "lib/readcommands.py (escalation #2538)"),
         ("collection.record_behaviours", "iba.app.handlers.collectionbuild:record_behaviours", "operations",
          "check a filled ReadBehaviours answer whole and write it through the recorder of stage 4 (layerinner.record); validate the 3.2 row; print the next command; -Check "
          "previews -- see lib/readcommands.py (escalation #2538)")]
GRANTS = ["collection_layer_item", "ib_node", "ib_observation", "ib_observation_change"]
SWEEP = ("collection.sweep_superseded", "iba.app.handlers.collectionbuild:sweep_superseded", "operations",
         "the close of 3.1 for a collection (-Collection): every live ledger row of a deleted subgroup retired and the observations written under it removed (nodes deleted, traces "
         "released, each change kept with its reason); refused while a current subgroup is not through 3.1; named snapshot first; -Check counts -- see lib/layerreading.py "
         "sweep_superseded (escalation #2538)")
IB08 = {"step": "collection.record_behaviours", "rule_key": "IB-08 what-a-behaviour-is", "ordinal": 12, "active": 1,
        "rule_text": ("A behaviour (step 3.2) is one working of the inner being: one core operation, who or what does what, shown by several element observations of 3.1. Elements "
                      "that show the same operation belong to one behaviour, whatever their mode, polarity, object, party or circumstance, and in whatever subgroup they sit; "
                      "those differences are written as relating findings (operation, chain, party, circumstance, role). Different operations linked in sequence are a chain "
                      "between behaviours, not one behaviour. A group that holds two operations is split; two groups that hold one operation are joined. An element that shows "
                      "no working of a human inner being (another being in its own right, route A of B:72; a word that is not an act of the mind) is declared not gathered "
                      "with its reason. A behaviour is named by what is done, never by what it means for the inner being (stage 5)."),
        "source_doc": ('escalation #2538: outputs/escalation/2538-step-3-2-draft-behaviours-thought-v1-20261126.md, section 2; researcher 2026-11-26: "the approach and '
                       'observation results for 3.2 looks good."'),
        "enforced_by": "the 3.2 read instruction (cfg_setting layer.read_types behaviours) and the reading; the recorder checks the form (layerinner.record, IB-04)"}


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", (IB08["rule_key"],)).fetchone():
        ops.append(("cfg_method_rule", "insert", {}, dict(IB08)))
    types = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    also = types.get("guide", {}).get("also", [])
    if types.get("behaviours") != BEHAVIOURS or "SweepSuperseded" not in also:
        types["behaviours"] = BEHAVIOURS
        if "guide" in types and "SweepSuperseded" not in also:
            types["guide"] = {**types["guide"], "also": also + ["SweepSuperseded"]}
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(types, ensure_ascii=False)}))
    lay = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading'").fetchone()[0])
    s33 = next(s for s in lay["steps"] if s["key"] == "3.3")
    if s33.get("read_command_deferred") != RULING:
        s33["read_command_deferred"] = RULING
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(lay, ensure_ascii=False)}))
    top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
    for step, handler, kind, does in STEPS + [SWEEP]:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            top += 1
            ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none",
                                                  "does": does, "inactive": 0, "kind": kind}))
        for t in GRANTS:
            if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (step, t)).fetchone():
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": t, "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: ReadBehaviours/RecordBehaviours (step 3.2) registered; 3.3 read command deferred by the researcher's ruling",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-behaviours-apply', named=True)}")
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
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
