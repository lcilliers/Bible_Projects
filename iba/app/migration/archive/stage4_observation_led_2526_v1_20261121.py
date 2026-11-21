"""stage4_observation_led_2526_v1_20261121.py -- escalation #2528 / #2526 (design outputs/escalation/2528-stage-4-design-v2-20261121.md; the researcher's answer to Q7 of #2526, 2026-11-21).

Stage 4 is redesigned: the input is the subgroups and their stage 3 observations; the behaviours are discovered from analysing those observations, with only occasional reading back into the base
data; stage 4 sets the observations for the elements of behaviour and formulates no claim. The rows are no longer a subgroup and a verse. Written to:
  - cfg_setting layer.reading: the items subgroup-analysis, collection-gathering, interworking replace verse-working, subgroup-working, interworking; the names of steps 3.1 to 3.3;
    pull_verse_texts; the use text;
  - cfg_setting layer.interventions: the prompts of the observation-led reading;
  - cfg_method_rule IB-01 to IB-06: reworded to the new rows and checks;
  - cfg_behaviour_rule 132: the stage 2 and stage 4 sentences;
  - cfg_column collection_layer_item.item and .subject: the use text.
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/stage4_observation_led_2526_v1_20261121.py [--db PATH]
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
RUN_ID = "DEVMODE-2526-STAGE4-OBSERVATION-LED-20261121"

STEPS = {"3.1": ("elements of the subgroups", ["subgroup-analysis"]), "3.2": ("behaviours of the collection", ["collection-gathering"]), "3.3": ("across collections", ["interworking"])}
ITEMS = {
    "subgroup-analysis": {
        "kind": "statement", "kinds": ["qualification", "statement", "party", "link"], "findings": True, "none_allowed": False,
        "uses": ["role", "polarity", "object", "enactment", "party", "circumstance", "operation", "chain", "flag"],
        "asks": ("What do the stage 3 observations of this subgroup (its definition, its Strong's enrichment, its pairings, qualifiers, entities, direction, relations and double meanings, with the stage 1 senses) "
                 "show of the elements of a behaviour of the inner being: what is done and its mode, whether a refusal or a pursuit, what it is directed at, the outward act, the other party with the "
                 "route, the circumstance, the chain of operations, and the dimensions of the working (what a qualifier or a variation of the word gives it, from the lexical variation the stage 3 "
                 "observations record)? Each finding is one observation that rests on named observations (a traced node on each) and carries nodes on the occurrences those observations cover, with the "
                 "role each has; an occurrence outside them is allowed only with a read-back (the verse and why). Every stage 3 observation of the subgroup is rested on by a finding or declared not used, "
                 "with the reason. A finding is a building block and never a claim about the behaviour as a whole (stage 5).")},
    "collection-gathering": {
        "kind": "statement", "kinds": ["statement", "link", "party", "qualification"], "findings": True, "none_allowed": True,
        "uses": ["flag", "operation", "chain", "party", "circumstance", "role"],
        "asks": ("Which behaviours does this collection show, discovered from the element observations of its subgroups? A behaviour may be one subgroup, part of one, or gather elements from several; a "
                 "subgroup may form none. Record each behaviour as a finding of the item flag with flag_type discovery that names it and gathers its element observations by a traced node on each, saying "
                 "which elements belong together and why; it states no claim about what the behaviour is (stage 5). Record also, as findings of operation, chain, party, circumstance or role, what "
                 "relates elements across subgroups. Every 3.1 observation of the collection is gathered into a behaviour or declared not gathered, with the reason. Where the collection shows no "
                 "behaviour, record none with its reason.")},
    "interworking": {
        "kind": "statement", "kinds": ["statement", "link", "party"], "findings": True, "none_allowed": True,
        "uses": ["operation", "chain", "party", "circumstance", "flag"],
        "asks": ("How do this subgroup and this partner collection work together in the verses they share? Each finding rests on named observations of step 3.1 or 3.2 of this collection (a traced node on "
                 "each) and carries nodes on the occurrences of both sides in the shared verses. Where the shared verses show no working together, record none with its reason.")},
}
INTERVENTIONS = [
    "Work from the observations: the stage 3 observations of the subgroup are the input, and the verses are base data read back only where an observation does not settle the point; a read-back is recorded (the verse and why).",
    "Read the lexical variation (the different Strong's codes of a surface, the forms of a word, the double meanings) as the dimensions of how the working happens, not as a difference to be smoothed away.",
    "A behaviour is discovered from the elements, not assumed from the subgroup: a subgroup may form one behaviour, part of one, join others, or form none.",
    "Record building blocks only. A statement of what a behaviour is, is a claim and belongs to stage 5; stage 5 receives the observations and not the subgroups, so everything it will need from them is recorded here.",
    "Check the original where an observation depends on the word's range (RG-08); do not force a meaning and never close on 'not X' (RG-10).",
    "A word whose role is not its collection's is reclassified by the collection change procedure and the step reopens (B:129, B:134); a discovery outside the observations is recorded as a flag finding of type discovery and is not resolved inline (RW-07).",
]
RULES = {
    "IB-01": ("Step 3.1 opens only when stage 3 is closed for the collection, that is steps 1.1, 1.2 and 2.1 each closed (every row answered and validated), the grouping finished, and nothing the grouping "
              "changed left open; step 3.2 needs 3.1 closed and 3.3 needs 3.2 closed. Opening derives the ledger rows: one subgroup-analysis row for each subgroup that has stage 3 observations, one "
              "collection-gathering row for the collection, one interworking row for each subgroup and partner collection that share pair_min_verses verses. A change to the grouping retires the rows the "
              "data no longer demands and adds the rows it now demands."),
    "IB-02": ("Stage 4 starts from the observations, not the verses (researcher, #2526 Q7, 2026-11-21): the subgroups and the stage 3 observations on them are the input, the behaviours are discovered from "
              "analysing them, and the base data is read back into only occasionally. Every finding of step 3.1 or 3.2 rests on named observations (a traced node on each, with an occurrence node as well) and "
              "its occurrence nodes lie within the occurrences those observations cover; an occurrence outside them is allowed only where the finding records a read-back (the verse and why). Each node has a role "
              "from reading.node_roles other than lexical, chosen by the reading. A 3.3 finding carries nodes on the occurrences of both sides in the shared verses."),
    "IB-03": ("A finding of a stage 4 row is checked by the rules of observationrecord.check and check_item_parts (kind, text, basis, route, parts.item and what the item needs, node roles, collection of each node) "
              "and by RG, RW and RS, which are not restated here: one observation for each finding, never a duplicate, with a node on each word it applies to (RO11, RW-03); founded in the observations and never a "
              "restatement of the verse (B:131); parts.item is one of the items the row's item uses (cfg_setting layer.reading). An observation whose nodes all bear on an act is refused: those words are nodes of "
              "the observation of the act. A finding is a building block of a behaviour and never a claim (stage 5)."),
    "IB-04": ("Nothing the step reads is lost on the way to stage 5. Step 3.1: every stage 3 observation of the subgroup is rested on by a finding or declared in not_used with its reason in words. Step 3.2: "
              "every 3.1 observation of the collection is gathered into a behaviour (a traced node on it from a flag finding of type discovery) or declared in not_gathered with its reason, and the row has at "
              "least one behaviour unless it is recorded as none with its reason. A behaviour names and gathers; it makes no claim about what the behaviour is."),
    "IB-05": ("An earlier inner-being observation with a node on the occurrences of a 3.1 row (any stage but lexical, layer-1, layer-2 and layer-3) is shown in the pull for information and may be actioned in "
              "`existing`: accepted, modified, deleted, merged or left, each with its reason, through observationrecord (RW-01, RW-09); nothing is demanded of it, and it counts for nothing in the check. A row "
              "answered again withdraws its earlier observations with the reason."),
    "IB-06": ("LayerCheck validates a stage 4 row from the tables alone: the demanded occurrences and the observations the row may rest on are re-derived; at least one live observation of stage layer-3 with its "
              "stable_key on the row; each observation's parts still valid and its item one the row uses; each live node has a valid role, a collection and its subgroup; each observation has a traced node on an "
              "observation the row may rest on; in 3.1 and 3.2 each occurrence node lies in the occurrences of the observations it rests on or its verse is in the recorded read-back; the completeness of IB-04 "
              "(not_used, not_gathered, the behaviour of 3.2); no observation restates a run of the verse longer than reading.observation_items max_verse_words_copied. A row that fails is unvalidated and its "
              "step is not closed."),
}
R132 = [("the surfaces of a collection are grouped by their meaning, judged from the dictionary meaning of the words (the Strong's meaning), a subgroup being the surfaces that mean the same or the same kind of thing, named for that meaning; a surface whose meaning is not the one the collection gathers is set aside with its reason;",
         "the surfaces of a collection are grouped by their meaning in context, each surface placed whole in one subgroup, a subgroup being the surfaces that mean the same or the same kind of thing, named for that meaning (the dictionary meaning is a pointer, and a surface may carry a hidden meaning in the different Strong's codes used for it); a surface plainly not a member in meaning is set aside with its reason for the change procedure;"),
        ("is the steps 3.1 (specific behaviours), 3.2 (groups of behaviours) and 3.3 (across subgroups and collections),",
         "is the steps 3.1 (the elements the stage 3 observations of each subgroup show), 3.2 (the behaviours discovered in the collection) and 3.3 (the working across collections); its input is the subgroups and their stage 3 observations, the behaviours are discovered from analysing those observations with only occasional reading back into the base data, and it records building-block observations and no claims (stage 5),")]
COL_ITEM_OLD = "and, for stage 4, verse-working, subgroup-working, interworking"
COL_ITEM_NEW = "and, for stage 4, subgroup-analysis, collection-gathering, interworking"
COL_SUBJ_OLD = "for stage 4 the verse of a verse-working row (its osis id), and for an interworking row group:<id of the other group> or collection:<name of the partner collection>; empty otherwise"
COL_SUBJ_NEW = "for stage 4 empty for a subgroup-analysis row (its group is the subgroup) and for the collection-gathering row, and collection:<name of the partner collection> for an interworking row"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        row = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.reading'").fetchone()
        lay = json.loads(row[0])
        new = json.loads(row[0])
        for st in new["steps"]:
            if st["key"] in STEPS:
                st["name"], st["items"] = STEPS[st["key"]][0], STEPS[st["key"]][1]
        for k in ("verse-working", "subgroup-working"):
            new["items"].pop(k, None)
        new["items"].update(ITEMS)
        new["pull_verse_texts"] = 12
        if new != lay:
            use = (row[1] or "").replace("a stage 4 item names the observation items it uses", "a stage 4 item names the observation items it uses").replace(
                "pull_max_rows (the rows of a stage 4 working file);", "pull_max_rows (the rows of a stage 4 working file), pull_verse_texts (the verses of a subgroup whose text a 3.1 file carries for a read-back);")
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False), "use": use})
            n += 1
        cur = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.interventions'").fetchone()[0]
        if json.loads(cur) != INTERVENTIONS:
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "layer.interventions"}, {"value": json.dumps(INTERVENTIONS, ensure_ascii=False)})
            n += 1
        for key, text in RULES.items():
            r = conn.execute("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE ?", (key + " %",)).fetchone()
            if r is None:
                raise SystemExit(f"rule {key} not found")
            if r[1] != text:
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": r[0]}, {"rule_text": text})
                n += 1
        t = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=132").fetchone()[0]
        t2 = t
        for old, new_ in R132:
            if old not in t2 and new_ not in t2:
                raise SystemExit("rule 132: expected text not found: " + old[:60])
            t2 = t2.replace(old, new_)
        if t2 != t:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 132}, {"rule_text": t2})
            n += 1
        for col, o, nw in (("item", COL_ITEM_OLD, COL_ITEM_NEW), ("subject", COL_SUBJ_OLD, COL_SUBJ_NEW)):
            u = conn.execute("SELECT use FROM cfg_column WHERE table_name='collection_layer_item' AND name=?", (col,)).fetchone()[0]
            if o in u:
                apply_logged(conn, RUN_ID, "cfg_column", "update", {"database": "iba", "table_name": "collection_layer_item", "name": col}, {"use": u.replace(o, nw)})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
