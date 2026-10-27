"""analysis_phase_1_2320_v1_20261027.py -- escalation #2320: the build of Analysis_phase_1 to the specification
outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md (approved by the researcher, #2318 v14 and #2319 v10).

What this changes (config and schema; the code is in iba/app/lib/reading.py, observationrecord.py, versecollate.py):
- ib_observation.parts (TEXT, JSON): the structured parts of a finding (spec 4.2), polarity included (the observation, not the node).
- cfg_enum observation_role: object, relational_target, enactment added (spec 4.1, decision D-a). 'standalone' stays an enum
  value because 23,429 existing nodes hold it; cfg_setting reading.node_roles lists the roles a NEW node may take.
- cfg_setting reading.verse_loop (new): the verse loop's settings (verses per sheet, the minimum reason length, the passage
  window, the actions on an existing observation); reading.node_roles (new); reading.observation_parts (parts added);
  reading.focus_words (now a grammar hint only); reading.surface_requirements (restated).
- cfg_step: reading.gather retired (inactive); the descriptions of reading.open, observe, record, check restated.
- cfg_method_rule: RS-01, RG-03, RG-09, RW-02, RO5, RO12 restated; RS-03 to RS-07 added.
- cfg_write_grant: reading.record may write reading_strand_hit (ledger faces linked, spec 2.4).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive) in the same transaction. Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2320_v1_20261027.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2320-ANALYSIS-PHASE-1-20261027"
MODULE = "analysis_phase_1_2320_v1_20261027"
SPEC = "outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md"
SRC = f"#2320, {SPEC}"
FILLED = "iba/app/lib/observationrecord.py (through iba/app/lib/reading.py)"

PARTS_USE = ("the structured parts of a finding, a JSON object (spec 4.2): sense (the meaning here), evidence, polarity "
             "(refusal or pursuit; the observation, not the node), content (what the act is directed at), enactment, party, "
             "circumstance (how it appears here), chain, primary_operation, flags (each typed data-quality or discovery)")
NODE_ROLES_USE = ("the roles a NEW node may take (#2320, spec 4.1), by the evaluation result of its surface: relevant (the characteristic or a qualifier of it) and bears_on (the object, relational target or enactment of a relevant act). The word's role in the finding. 'standalone' is not a role "
                  "of a new node: a standalone word is ignored, or recorded inside the observation for the claims to decide")
LOOP_USE = ("the verse loop of Analysis_phase_1 (#2320): verses_per_sheet = how many verses Observe puts in hand at once; "
            "min_reason_chars = the shortest reason accepted; passage_window = verses either side shown with a verse; "
            "existing_actions = what the reading does with an existing observation; evaluation_results = the results of a surface's evaluation; observation_set = the columns a modify may "
            "change; node_set = the columns a modify may change on a node; polarity = the values of the polarity part")
FOCUS_USE = ("a GRAMMAR HINT only (#2320): the function-word morph prefixes and the kept tags (negators, connectives). It decides "
             "nothing: every surface of a verse is evaluated for an inner-being role by the reading (spec 4.1), and the "
             "hint is shown beside the surface. function_word_morph: OT, the first two letters of the morph code; NT, the part "
             "before the first hyphen.")
REQ_USE = ("what makes a relevant surface covered (#2320, spec 4.4): a live node of a finding, with a role from "
           "reading.node_roles, on the surface's occurrence. A surface with no inner-being role has no observation; its "
           "evaluation is kept in the JSON.")

RS01 = ("Every surface of every verse is evaluated for an inner-being role (the characteristic, or a qualifier of it), by "
        "tests and not by the gloss or the cluster tag, and the result with its reason is kept in the JSON. A relevant surface "
        "is covered by a live finding whose node names its occurrence with a role from reading.node_roles; a surface with no "
        "inner-being role has no observation and no silence finding.")
RG03 = ("Find the main inner-being operation, and give every relevant surface its role in this finding (cfg_setting "
        "reading.node_roles): characteristic, qualifier, object or content, relational target, or enactment. The role comes "
        "from this verse, never from the cluster tag. A standalone word is ignored; where it could be a qualifier it is "
        "recorded inside the observation for the claims to decide.")
RG09 = ("Record each relevant word's face as it appears HERE: the circumstance in this verse and where the sense departs from "
        "the general gloss. How the face differs from the word's other occurrences needs more than one verse and is claims work.")
RW02 = ("A reading records findings of eight kinds (cfg_setting reading.observation_parts; the kind is the tag): face, "
        "qualification, party, statement, link, use, term, silence. A finding holds its text, meaning, implication, basis, "
        "its structured parts (ib_observation.parts: sense, evidence, polarity, content, enactment, party, circumstance, chain, "
        "primary operation, typed flags) and, on a party or link finding, its route; its nodes hold the verse, the word, the "
        "occurrence, the subgroup, the cluster, the word's role in the finding and the reading that applied it. The silence "
        "kind is not used by Analysis_phase_1: a surface with no inner-being role is not recorded.")
RO5 = ("The pull is a query by verse (#2320): when a verse is worked, its existing observations and nodes are read from the "
       "tables, so that what earlier verses wrote is seen. The JSON is the index of the verses and copies no observation.")
RO12 = ("Gap work comes into play at step 4, not in Analysis_phase_1 (researcher, 2026-10-27): the verse loop records no gaps. "
        "Gaps are processed for the scope only.")
NEW_RULES = [
    ("RS-03 surface-evaluated-for-inner-being-role", "reading.observe",
     "Every surface of the verse is enumerated and evaluated by the tests of the lexical work (inner-being vocabulary, idiom or "
     "combined span, volitional sense behind a plain verb, another party named or implied against 'relates', polarity, "
     "sequence, grammar only). The result, relevant or not_relevant, and its reason are kept in the JSON, not in the tables."),
    ("RS-04 existing-checked-accept-modify-delete", "reading.observe",
     "When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse and "
     "accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change) or "
     "soft deleted (the observation withdrawn, or the node's disposition withdrawn, with the reason). Nothing is deleted."),
    ("RS-05 non-relevant-not-recorded", "reading.observe",
     "A surface with no inner-being role is not recorded in the observations. A standalone word is ignored; where it could be "
     "a qualifier it is recorded inside the observation for the claims to decide."),
    ("RS-06 open-items-out-of-phase-1", "reading.observe",
     "Analysis_phase_1 neither pulls nor answers open items, and its gate does not look at them. They stay in the register and "
     "are cleared after the claims, as a secondary validation (researcher, 2026-10-27)."),
    ("RS-07 json-is-the-index", "reading.open",
     "The scope JSON indexes the verses in scope: per verse its reference, the route that brought it in, its progress and "
     "the evaluation of its surfaces. It is the one record of the scope; no table duplicates it for these steps."),
]
STEP_DOES = {
    "reading.open": "0.C: a reading opened on one subgroup or a segment of it (-Subgroup, optional -Surface or -Verse), with its objective: "
                    "the scope JSON that indexes the verses (reference, route, progress), and the reading row. Writes no observation -- see lib/reading.py (#2320)",
    "reading.observe": "the verse loop, first half: for the next verses waiting, query the database for each verse's text and passage, its surfaces, "
                       "its existing observations and nodes and the ledger faces, and put the sheet in the JSON for the reading to fill -- see lib/reading.py (#2320)",
    "reading.record": "the verse loop, second half: the filled sheets checked whole, then the surface evaluations kept in the JSON, the existing "
                      "observations and nodes accepted, modified or soft deleted, and the new findings written, in one transaction -- see lib/reading.py (#2320)",
    "reading.check": "the gate the reading is at, checked from the tables and the JSON: at open, the Observe gate (every verse done; open -> observed; "
                     "the verses then marked analysed); later states as before -- see lib/reading.py (#2320)",
}


class Refused(Exception):
    pass


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    # ib_observation.parts
    if not one("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name='parts'"):
        ops.append(("cfg_column", "insert", {}, {
            "database": "iba", "table_name": "ib_observation", "name": "parts", "ordinal": 27, "type": "TEXT", "is_pk": 0,
            "notnull": 0, "is_unique": 0, "dflt": None, "fk": None, "use": PARTS_USE, "expectation": None, "source": SRC,
            "filled_by": FILLED, "inactive": 0}))
    # node roles
    o = one("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name='observation_role'")[0]
    for v in ("object", "relational_target", "enactment"):
        if not one("SELECT 1 FROM cfg_enum WHERE name='observation_role' AND value=?", v):
            ops.append(("cfg_enum", "insert", {}, {"name": "observation_role", "value": v, "ordinal": o, "inactive": 0}))
            o += 1
    roles = {"relevant": ["characteristic", "qualifier"], "bears_on": ["object", "relational_target", "enactment"]}
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.node_roles'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "reading.node_roles", "module": "reading", "inactive": 0,
                                                  "use": NODE_ROLES_USE, "value": json.dumps(roles)}))
    loop = {"verses_per_sheet": 5, "min_reason_chars": 10, "passage_window": 2,
            "existing_actions": ["accept", "modify", "delete"],
            "observation_set": ["obs_text", "meaning", "implication", "basis", "tag", "route", "parts"],
            "node_set": ["verse_lexical_id", "cluster_subgroup_code", "cluster_code", "role", "surface", "morph_code"],
            "polarity": ["refusal", "pursuit"], "evaluation_results": ["relevant", "bears_on", "not_relevant"]}
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.verse_loop'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "reading.verse_loop", "module": "reading", "inactive": 0,
                                                  "use": LOOP_USE, "value": json.dumps(loop)}))
    # observation_parts: parts added
    op = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0])
    if "parts" not in op:
        op["parts"] = ["sense", "evidence", "polarity", "content", "enactment", "party", "circumstance", "chain",
                       "primary_operation", "flags"]
        op["flag_types"] = ["data-quality", "discovery"]
        op["finding"] = list(op["finding"]) + ["parts"]
        ops.append(("cfg_setting", "update", {"key": "reading.observation_parts"}, {"value": json.dumps(op, ensure_ascii=False)}))
    fw = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.focus_words'")[0])
    ops.append(("cfg_setting", "update", {"key": "reading.focus_words"}, {
        "value": json.dumps({"function_word_morph": fw["function_word_morph"], "keep_tags": fw["keep_tags"],
                             "applies": FOCUS_USE}, ensure_ascii=False), "use": FOCUS_USE}))
    ops.append(("cfg_setting", "update", {"key": "reading.surface_requirements"}, {
        "value": json.dumps({"covered_by": "a live node with a role from reading.node_roles on the surface's occurrence",
                             "not_relevant": "no observation; the evaluation is kept in the JSON"}), "use": REQ_USE}))
    # steps
    for step, text in STEP_DOES.items():
        ops.append(("cfg_step", "update", {"work_package": "reading", "step": step}, {"does": text}))
    ops.append(("cfg_step", "update", {"work_package": "reading", "step": "reading.gather"}, {
        "inactive": 1, "does": "RETIRED (#2320): the pull is a query by verse inside reading.observe; see spec outputs/escalation/"
                               "2318-analysis-phase-1-specification-v4-20261027.md section 3"}))
    # method rules
    for key, text in (("RS-01 ", RS01), ("RG-03 ", RG03), ("RG-09 ", RG09), ("RW-02 ", RW02), ("RO5 ", RO5), ("RO12 ", RO12)):
        row = one("SELECT id, rule_key FROM cfg_method_rule WHERE rule_key LIKE ? AND active=1", key + "%")
        if row:
            new_key = row[1]
            if key == "RS-01 ":
                new_key = "RS-01 surface-evaluated-and-covered"
            elif key == "RO5 ":
                new_key = "RO5 query-by-verse"
            elif key == "RO12 ":
                new_key = "RO12 gaps-at-step-4"
            ops.append(("cfg_method_rule", "update", {"id": row[0]}, {"rule_text": text, "rule_key": new_key,
                                                                      "source_doc": SRC}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    nord = one("SELECT max(ordinal) FROM cfg_method_rule")[0]
    for key, step, text in NEW_RULES:
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            nord += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": step, "rule_key": key, "rule_text": text,
                                                          "source_doc": SRC, "enforced_by": None, "ordinal": nord, "active": 1}))
    # write grant
    g = one("SELECT inactive FROM cfg_write_grant WHERE writer='reading.record' AND table_name='reading_strand_hit' "
            "AND database='iba'")
    if g is None:
        ops.append(("cfg_write_grant", "insert", {}, {"writer": "reading.record", "table_name": "reading_strand_hit",
                                                      "database": "iba", "inactive": 0}))
    elif g[0]:
        ops.append(("cfg_write_grant", "update", {"writer": "reading.record", "table_name": "reading_strand_hit",
                                                  "database": "iba"}, {"inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2320: Analysis_phase_1 to specification v4; run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    try:
        ops = plan(conn)
    except Refused as exc:
        print(f"REFUSED, nothing written: {exc}")
        return 2
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    cols = {r[1] for r in conn.execute("PRAGMA table_info(ib_observation)")}
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if "parts" not in cols:
            conn.execute('ALTER TABLE ib_observation ADD COLUMN "parts" TEXT')
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
