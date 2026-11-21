"""stage4_config_2528_v1_20261121.py -- escalation #2528 (build brief B5; design outputs/escalation/2528-stage-4-design-v1-20261121.md, approved 2026-11-21 with D1 and D2).

The configuration of stage 4 of the study (the inner-being analysis) as steps 3.1 to 3.3 of the layered reading. Every write is an audited apply_logged (rule 75):
  - cfg_enum ib_observation.stage: the value layer-3;
  - cfg_setting layer.reading: stages."3", the steps 3.1, 3.2, 3.3 (with `pairs` on 3.3), the items verse-working, subgroup-working, interworking, pull_max_rows;
  - cfg_setting layer.interventions (new): the prompts every stage 4 row carries;
  - cfg_method_rule IB-01 to IB-06 on the steps collection.layer_open, layer_record and layer_check (pointers to RG, RW and RS, not restated);
  - cfg_column use text of collection_layer_item step, item, subgroup_id and subject, and the cfg_setting use text of layer.reading.
Idempotent: a second run changes nothing.

Usage:
    python iba/app/migration/stage4_config_2528_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-STAGE4-CONFIG-20261121"
SRC = "escalation #2528 (researcher, 2026-11-21: approval of the design with D1 and D2; outputs/escalation/2528-stage-4-design-v1-20261121.md)"
CODE = "iba/app/lib/layerinner.py, iba/app/lib/layerreading.py"

STEPS = [
    {"key": "3.1", "layer": 3, "name": "specific behaviours", "needs": ["1.1", "1.2", "2.1"], "items": ["verse-working"]},
    {"key": "3.2", "layer": 3, "name": "groups of behaviours", "needs": ["3.1"], "items": ["subgroup-working"]},
    {"key": "3.3", "layer": 3, "name": "across subgroups and collections", "needs": ["3.2"], "items": ["interworking"], "pairs": True},
]
ITEMS = {
    "verse-working": {
        "kind": "statement", "kinds": ["qualification", "statement", "party", "link"], "findings": True, "none_allowed": False,
        "uses": ["role", "polarity", "object", "enactment", "party", "circumstance", "operation", "chain", "flag"],
        "asks": ("What does this subgroup's word do, in this verse, for the inner being? Read the verse in its passage. Give every occurrence of the subgroup in the verse a node with the role it has here "
                 "(characteristic, qualifier, object, relational target, enactment, or standalone where it holds nothing for the inner being), and write one finding for each applicable item of its uses: "
                 "the role of the characteristic and what a qualifier gives it, whether the act is a refusal or a pursuit, what it is directed at, the outward act the verse states, the other party with the route, "
                 "the circumstance, the operation (who or what does what, with its mode; the verse always has one) and the chain of operations. An item the verse shows none of is stated absent with its reason. "
                 "A finding is one observation with a node on each word it applies to, never a duplicate; it is founded in the verse and never restates it.")},
    "subgroup-working": {
        "kind": "statement", "kinds": ["statement", "link"], "findings": True, "none_allowed": False,
        "uses": ["operation", "chain", "circumstance", "flag"],
        "asks": ("What do the workings of this subgroup show across its verses (its modes, states and transitions, the operations it takes part in)? Each finding rests on named observations of step 3.1 "
                 "(a traced node on each), carries a node on occurrences of the subgroup, and says what the verses together show that no single verse does.")},
    "interworking": {
        "kind": "statement", "kinds": ["statement", "link", "party"], "findings": True, "none_allowed": True,
        "uses": ["operation", "chain", "party", "circumstance", "flag"],
        "asks": ("How do these two subgroups, or this subgroup and this partner collection, work together in the verses they share? Each finding rests on named observations of step 3.1 or 3.2 "
                 "(a traced node on each) and carries the nodes of both sides. Where the shared verses show no working together, record none with its reason.")},
}
INTERVENTIONS = [
    "Read beyond the verse, in its passage, genre and speaker (RG-02), where the verse alone does not settle what the word does.",
    "Read outward from the verse and not inward from a question (RG-01); record everything the verse carries before an answer is shaped.",
    "Check the original: the word's range in all three meaning sources read together, never one picked and the others dropped (RG-08).",
    "A word whose role here is not its collection's is reclassified by the collection change procedure; the move is processed so that the step reopens (B:129, B:134).",
    "Do not force a meaning and never close on 'not X' (RG-10); a prompt that does not apply is not answered (RG-17).",
    "A discovery outside the verse is recorded separately as a flag finding of type discovery, and is not resolved inline (RW-07).",
]
RULES = [
    ("IB-01 stage-4-opens-on-stage-3-closed", "collection.layer_open",
     "Step 3.1 opens only when stage 3 is closed for the collection, that is steps 1.1, 1.2 and 2.1 each closed (every row answered and validated), the grouping finished, and nothing the grouping changed left open; "
     "step 3.2 needs 3.1 closed and 3.3 needs 3.2 closed. Opening derives the ledger rows: one verse-working row for each subgroup and verse in which the subgroup has an occurrence, one subgroup-working row for each "
     "subgroup, one interworking row for each pair of subgroups that share relation_min_verses verses and for each partner collection that shares pair_min_verses verses with a subgroup. A change to the grouping "
     "retires the rows the data no longer demands and adds the rows it now demands."),
    ("IB-02 every-occurrence-carries-a-node-with-its-role", "collection.layer_record",
     "Every occurrence a verse-working row (step 3.1) demands carries a live node, on a finding of the row or on an earlier observation the row kept, with a role from reading.node_roles other than lexical: "
     "characteristic or qualifier (relevant), object, relational target "
     "or enactment (bears on), or standalone where the word holds nothing for the inner being (RS-05; researcher ruling on #2525 and on #2528, D2). The role is chosen for each node by the reading, not fixed for the row. "
     "No occurrence is left with no node: an occurrence that is not carried is one that was not read. Steps 3.2 and 3.3 rest on the step below and do not demand a node on every occurrence (every occurrence "
     "was read in 3.1, and a partner word is read in its own collection); each of their findings carries a node on an occurrence of the row and a traced node on an observation of the step below."),
    ("IB-03 findings-follow-the-observation-rules", "collection.layer_record",
     "A finding of a stage 4 row is checked by the rules of observationrecord.check and check_item_parts (kind, text, basis, route, parts.item and what the item needs, node roles, collection of each node) "
     "and by RG, RW and RS, which are not restated here: one observation for each finding, never a duplicate, with a node on each word it applies to (RO11, RW-03); founded in the verse and never a restatement of "
     "it (B:131); parts.item is one of the items the row's item uses (cfg_setting layer.reading). An observation whose nodes all bear on an act is refused: those words are nodes of the observation of the act."),
    ("IB-04 each-characteristic-has-each-item", "collection.layer_record",
     "For a verse-working row: the verse always has an observation of the item operation (reading.observation_items verse_always); for every occurrence given the role characteristic, each item of the row's uses is "
     "either observed with a node on that occurrence or stated absent with its reason in items_absent, never both; an item that is not shared is one observation for each characteristic (RS-10)."),
    ("IB-05 earlier-observations-are-checked-first", "collection.layer_record",
     "Every earlier inner-being observation with a node on the verse of a verse-working row (any stage but lexical, layer-1, layer-2 and layer-3) needs an action in `existing`: accepted, modified, deleted, merged or "
     "left, each with its reason, through observationrecord (RS-04, RW-01, RW-09); none is passed over. One accepted or modified is kept on the row and counts for its coverage and items; one left or deleted counts "
     "for nothing. The flags the pull shows come from lib/verseevidence.py. A row answered again withdraws its earlier observations with the reason."),
    ("IB-06 stage-4-check-rederives-from-the-tables", "collection.layer_check",
     "LayerCheck validates a stage 4 row from the tables alone: the demanded occurrences are re-derived; at least one live observation of stage layer-3 with its stable_key on the row; each observation's parts still valid; "
     "each live node has a valid role, a collection and its subgroup; on a verse-working row every demanded occurrence is carried by an observation of the row or one it kept, and the operation observation is present; "
     "no observation restates a run of the verse "
     "longer than reading.observation_items max_verse_words_copied; a step 3.2 or 3.3 finding has a traced node on a live observation of the step below. A row that fails is unvalidated and its step is not closed."),
]
COLUMN_USE = {
    "step": "the step of the layered reading that demands it (layer.reading steps): S1 (stage 1, the words), 1.1, 1.2 or 2.1 (stages 2 and 3 of the study), or 3.1, 3.2 or 3.3 (stage 4, the inner-being analysis)",
    "item": "the kind of aspect (layer.reading items): word-sense, group-definition, strong-enrichment, pairing, qualifier, entity, direction, group-relation, double-meaning; and, for stage 4, verse-working, subgroup-working, interworking",
    "subgroup_id": "the group the aspect is about (for a relation between two groups, the one with the lower id); 0 for an aspect of stage 1 (a word), which belongs to no group yet",
    "subject": ("what distinguishes the aspect within a group: the word of a stage 1 aspect (surface|lettered Strong's code), the partner collection of a pairing, the other group of a relation (its id), the surface of a double meaning; "
                "for stage 4 the verse of a verse-working row (its osis id), and for an interworking row group:<id of the other group> or collection:<name of the partner collection>; empty otherwise"),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='ib_observation.stage' AND value='layer-3'").fetchone():
            apply_logged(conn, RUN_ID, "cfg_enum", "insert", {}, {"name": "ib_observation.stage", "value": "layer-3", "ordinal": 15, "inactive": 0})
            n += 1
        row = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading'").fetchone()
        lay = json.loads(row[0])
        before = json.dumps(lay, sort_keys=True)
        lay["stages"]["3"] = "layer-3"
        have = {s["key"] for s in lay["steps"]}
        lay["steps"] += [s for s in STEPS if s["key"] not in have]
        for k, v in ITEMS.items():
            lay["items"].setdefault(k, v)
        lay.setdefault("pull_max_rows", 5)
        if json.dumps(lay, sort_keys=True) != before:
            use = conn.execute("SELECT use FROM cfg_setting WHERE key='layer.reading'").fetchone()[0]
            new_use = use.replace("the steps (1.1 groups, 1.2 Strong's enrichment, 2.1 pairings) with what each needs", "the steps (1.1 groups, 1.2 Strong's enrichment, 2.1 pairings, and the stage 4 steps 3.1 specific behaviours, 3.2 groups of behaviours, 3.3 across subgroups and collections) with what each needs")
            new_use = new_use.replace("pull_max_nodes (the nodes shown for each row of a working file)", "pull_max_nodes (the nodes shown for each row of a working file), pull_max_rows (the rows of a stage 4 working file); a stage 4 item names the observation items it uses (`uses`, reading.observation_items) and `findings`")
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(lay, ensure_ascii=False), "use": new_use})
            n += 1
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='layer.interventions'").fetchone():
            apply_logged(conn, RUN_ID, "cfg_setting", "insert", {}, {"key": "layer.interventions", "value": json.dumps(INTERVENTIONS, ensure_ascii=False), "module": "layer", "inactive": 0,
                                                                     "use": "the prompts every stage 4 row (steps 3.1 to 3.3) carries in its working file: how to read beyond the verse, outward, the original, a word out of its collection, no forced meaning, a discovery recorded apart (#2528). Read by lib/layerinner.py"})
            n += 1
        nxt = conn.execute("SELECT max(ordinal) FROM cfg_method_rule WHERE step IN ('collection.layer_open','collection.layer_record','collection.layer_check')").fetchone()[0] or 0
        for key, step, text in RULES:
            if not conn.execute("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", (key,)).fetchone():
                nxt += 1
                apply_logged(conn, RUN_ID, "cfg_method_rule", "insert", {}, {"step": step, "rule_key": key, "rule_text": text, "source_doc": SRC, "enforced_by": CODE, "ordinal": nxt, "active": 1})
                n += 1
        for col, use in COLUMN_USE.items():
            cur = conn.execute("SELECT use FROM cfg_column WHERE table_name='collection_layer_item' AND name=?", (col,)).fetchone()[0]
            if cur != use:
                apply_logged(conn, RUN_ID, "cfg_column", "update", {"database": "iba", "table_name": "collection_layer_item", "name": col}, {"use": use})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
