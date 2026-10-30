"""analysis_phase_1_2329_v3_20261030.py -- escalation #2329: the observation structure of the worked example v3.

Approved by the researcher, chat 2026-10-30: 'proceed with redoing all 39 verses to this new level ... ensure that the configs include
pointers for the different nuances', and 'build 2329' (the decisions of the build plan section 1 are Claude's to judge). The structure:
outputs/escalation/2329-observation-structure-worked-example-v3-20261030.md; the plan: outputs/escalation/2329-build-and-redo-plan-v1-20261030.md.
Config first (governance.rules_must_be_config_driven), then the code that reads it (iba/app/lib/observationrecord.py, reading.py).

Decisions of plan section 1 (judged against the objective, recorded here and in the rule rows):
- kinds: the existing kinds are kept (no schema change); each of the nine items names the kinds it may be written as. The item an
  observation is, is held in ib_observation.parts as {"item": key}, so the claims process queries by item with json_extract.
- `parts` column: kept, and now small: item, mode, polarity, flag_type, grounds. Before, after, enactment-as-text, the typed party and the
  twelve-part form go. The 132 existing observations carry the old form; each is accepted, modified or soft deleted when its verse is redone (RS-04).
- the mode of an operation (done, foreseen, commanded, negated, reported) is `mode` on the operation item's observation, from the list in
  reading.observation_items.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2329_v3_20261030.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2329-OBSERVATION-ITEMS-20261030"
MODULE = "analysis_phase_1_2329_v3_20261030"
SRC = "#2329 (researcher, chat 2026-10-30)"
SPEC = "outputs/escalation/2329-observation-structure-worked-example-v3-20261030.md"

S, R = "stated", "read"
ITEMS = {
    "items": [
        {"no": 1, "key": "meaning", "name": "the surface and its meaning here, with the evidence", "kinds": ["face"], "bases": [S], "shared": False},
        {"no": 2, "key": "role", "name": "its role: the qualifier and what it gives the characteristic", "kinds": ["qualification", "statement"],
         "bases": [S, R], "shared": True},
        {"no": 3, "key": "polarity", "name": "whether the act is a refusal or a pursuit", "kinds": ["statement"], "bases": [S, R],
         "shared": False, "polarity_required": True},
        {"no": 4, "key": "object", "name": "what the act is directed at or against", "kinds": ["statement"], "bases": [S, R], "shared": False},
        {"no": 5, "key": "enactment", "name": "the outward act the inner act produces, where the verse states one", "kinds": ["statement"],
         "bases": [S, R], "shared": False},
        {"no": 6, "key": "party", "name": "the other party and the sequence, with the route", "kinds": ["party"], "bases": [S, R], "shared": True},
        {"no": 7, "key": "circumstance", "name": "how it appears here: the circumstance of the verse", "kinds": ["statement"], "bases": [S],
         "shared": True},
        {"no": 8, "key": "operation", "name": "the operation as an action description (who or what does what), its mode, the primary one",
         "kinds": ["statement"], "bases": [S, R], "shared": False, "mode_required": True},
        {"no": 8, "key": "chain", "name": "the chain of operations the verse links in sequence", "kinds": ["link"], "bases": [S, R], "shared": True},
        {"no": 9, "key": "flag", "name": "a typed flag: data-quality, or discovery for the claims process", "kinds": ["statement"],
         "bases": [S, R], "shared": True, "flag_type_required": True},
    ],
    "parts_keys": ["item", "mode", "polarity", "flag_type", "grounds"],
    "modes": ["done", "foreseen", "commanded", "negated", "reported"],
    "flag_types": ["data-quality", "discovery"],
    "item_roles": ["characteristic"],
    "surface_always": ["meaning"],
    "verse_always": ["operation"],
    "grounds_required_for_basis": ["read"],
    "max_verse_words_copied": 7,
}
ITEMS_USE = (
    "the nine items of an observation of Analysis_phase_1 (spec 4.2; #2329, worked example v3): for each its key, the kinds it may be written "
    "as, the bases allowed (stated, read), whether one observation may be shared across characteristics by its nodes, and what it must carry "
    "in ib_observation.parts (polarity, mode, flag_type). Item 8 has two forms (operation, chain). parts_keys = the only keys of `parts`; "
    "modes = the mode of an operation; item_roles = the node roles whose surface is a characteristic: every such surface has, for each item, "
    "an observation of that item or the item stated absent with the reason (surface items_absent on the sheet); surface_always = items never "
    "absent for such a surface; verse_always = items the verse always has; grounds_required_for_basis = a read observation names its "
    "grounds; max_verse_words_copied = an observation restates no run of the verse text longer than this. Read by iba/app/lib/observationrecord.py "
    "check_item_parts and iba/app/lib/reading.py _validate_sheet")

NUANCES = [
    {"nuance": "a negated act is a refusal; the negator is a qualifier", "item": "polarity", "form": "statement; qualifier node on the negator",
     "basis": "stated", "rule": "RG-07", "verse": "Judg 13:6, Jos 9:14"},
    {"nuance": "a qualifier shared across characteristics", "item": "role", "form": "qualification; one observation, nodes on each characteristic",
     "basis": "stated", "rule": "RG-04", "verse": "Judg 13:6 (very, not)"},
    {"nuance": "a T-coded word takes the role characteristic because the verse makes it carry the track", "item": "role",
     "form": "role by the verse, never by the cluster", "basis": "stated", "rule": "RG-03", "verse": "Judg 13:6 (appearance)"},
    {"nuance": "a refrained act with something hidden behind it", "item": "operation", "form": "statement, basis read, grounds named",
     "basis": "read", "rule": "RG-11", "verse": "Judg 13:6"},
    {"nuance": "a relation between characteristics in one verse (one conditions another)", "item": "chain",
     "form": "link, basis read, nodes on each characteristic, with a discovery flag", "basis": "read", "rule": "RW-08, RG-15", "verse": "Judg 13:6"},
    {"nuance": "a source of a state against an enablement to act", "item": "operation", "form": "separate observations", "basis": "stated",
     "rule": "RG-13", "verse": "to find"},
    {"nuance": "a figure or simile: the tenor, not the vehicle", "item": "operation", "form": "operation of the tenor", "basis": "stated",
     "rule": "RG-25, RG-02", "verse": "to find"},
    {"nuance": "a tagged word working adverbially", "item": "role", "form": "qualification in that occurrence", "basis": "stated",
     "rule": "RG-24", "verse": "to find"},
    {"nuance": "an idiom or multi-word span whose surface hides the word", "item": "meaning", "form": "face, surface rule", "basis": "stated",
     "rule": "RG-08, lexical.span_surface", "verse": "Jos 9:14 ('counsel' as 'ask at the mouth')"},
    {"nuance": "a reading that is open in more than one way", "item": "operation", "form": "one observation per reading, basis read",
     "basis": "read", "rule": "RW-08, RG-08", "verse": "to find"},
    {"nuance": "the speaker and the audience of reported speech", "item": "party", "form": "party with its route", "basis": "stated",
     "rule": "RG-02", "verse": "Gen 43:7, Judg 13:6"},
    {"nuance": "the mode of an operation: done, foreseen, commanded, negated, reported", "item": "operation", "form": "parts.mode on the operation",
     "basis": "stated", "rule": "RS-10", "verse": "Gen 32:17, Deu 4:32, Gen 43:7, Jos 9:14"},
    {"nuance": "a homonym or data error", "item": "flag", "form": "flag_type data-quality, not fixed in the reading", "basis": "stated",
     "rule": "RG-16", "verse": "to find"},
    {"nuance": "a literary pattern with no inner-being content", "item": "flag", "form": "open question as a discovery flag, not an observation",
     "basis": "read", "rule": "RG-12", "verse": "to find"},
    {"nuance": "a structural fact the verse does not explain", "item": "circumstance", "form": "kept, not dropped", "basis": "stated",
     "rule": "spec 4.2", "verse": "to find"},
    {"nuance": "the state before and the outcome after an operation, as the verse itself states them", "item": "operation",
     "form": "inside the operation description; where the verse states none, a discovery flag says the passage must be read",
     "basis": "stated", "rule": "RS-10", "verse": "Judg 13:6"},
]
NUANCE_USE = (
    "the nuance pointers (#2329): one row per nuance met in the reading: the nuance, the item it falls under, the form and basis it is written "
    "in, the rule it comes from, and a verse that shows it. The Observe sheet carries the rows so that the reading and the check know where "
    "each nuance is recorded. A nuance met in the redo that has no row gets a row in the same session, with the verse that showed it. "
    "Read by iba/app/lib/reading.py _sheets")

RULE_NEW = {"step": "reading.record", "rule_key": "RS-10 one-observation-per-item", "ordinal": 79, "active": 1, "source_doc": SRC + "; " + SPEC,
            "enforced_by": "iba/app/lib/reading.py _validate_sheet; iba/app/lib/observationrecord.py check_item_parts",
            "rule_text": "For every surface with the role characteristic, the nine items of spec 4.2 (reading.observation_items) are each explored, "
                         "and each applicable item is its own observation (parts.item), written once and applied to every characteristic it "
                         "is true of by its nodes; a qualifier or shared observation carries nodes on every characteristic it covers. An "
                         "item the verse does not show gets no observation and is stated absent on the surface (items_absent) with the "
                         "reason; the meaning item is never absent. The operation item carries a mode (done, foreseen, commanded, negated, "
                         "reported) and an action description of who or what does what, read from before and after as the verse itself "
                         "states them (passage-level before and after are the claims process's); the verse always has an operation "
                         "observation. A read observation (basis read) names its grounds in the words of the verse (parts.grounds). No "
                         "observation restates the verse text (no run of more than reading.observation_items max_verse_words_copied words). "
                         "The same text for all items is not an exploration of them. Which word is the characteristic is the verse's decision, "
                         "never the cluster's (RG-03). The nuance pointers (reading.nuance_pointers) say where each nuance is recorded (#2329)."}
RS08_TEXT = (
    "The observations of a verse state what the verse shows, and Record enforces it from cfg_setting reading.observation_rules and "
    "reading.observation_items: an observation of a relevant surface carries parts.item (one of the nine items), is written as one of the "
    "kinds that item allows, on a basis the item allows (a read observation names its grounds), and carries what its item needs "
    "(polarity, mode, flag type; a party carries its route). The words that bear on an act are nodes of the observation of the act, never an "
    "observation of their own (bears_on_only_refused). Every surface with the role characteristic has each applicable item observed or stated "
    "absent with the reason; the verse always has an operation observation. A verse whose observations do not comply is not recorded (#2329).")
RW02_TEXT = (
    "A reading records findings of eight kinds (cfg_setting reading.observation_parts; the kind is the tag): face, qualification, party, "
    "statement, link, use, term, silence. A finding holds its text, meaning, implication, basis, its structured parts (ib_observation.parts: "
    "item, and mode, polarity, flag_type or grounds where its item needs them; reading.observation_items) and, on a party or link finding, "
    "its route; its nodes hold the verse, the word, the occurrence, the subgroup, the cluster, the word's role in the finding and the reading "
    "that applied it. The silence kind is not used by Analysis_phase_1: a surface with no inner-being role is not recorded.")
ENFORCED = "iba/app/lib/reading.py _validate_sheet; iba/app/lib/observationrecord.py check_item_parts"


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.observation_items'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "reading.observation_items", "value": json.dumps(ITEMS), "use": ITEMS_USE,
                                                  "module": "reading", "inactive": 0}))
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.nuance_pointers'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "reading.nuance_pointers", "value": json.dumps(NUANCES), "use": NUANCE_USE,
                                                  "module": "reading", "inactive": 0}))
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0])
    if any(k in cur for k in ("parts", "flag_types", "party_form")):
        for k in ("parts", "flag_types", "party_form"):
            cur.pop(k, None)
        cur["rule"] = ("one finding per description, applied by its nodes (#2273); the item it is (parts.item, reading.observation_items), "
                       "the face, the qualification, the party and the operation (statement) are findings, not columns")
        ops.append(("cfg_setting", "update", {"key": "reading.observation_parts"}, {"value": json.dumps(cur)}))
    rules = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.observation_rules'")[0])
    if any(k in rules for k in ("parts_never_absent", "primary_operation", "chain", "party")):
        for k in ("parts_never_absent", "primary_operation", "chain", "party"):
            rules.pop(k, None)
        ops.append(("cfg_setting", "update", {"key": "reading.observation_rules"}, {"value": json.dumps(rules)}))
    for like, text, enf in (("RS-08 %", RS08_TEXT, ENFORCED), ("RW-02 %", RW02_TEXT, None)):
        row = one("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE ? AND active=1", like)
        if row and row[1] != text:
            sets = {"rule_text": text, "source_doc": SRC + "; " + SPEC}
            if enf:
                sets["enforced_by"] = enf
            ops.append(("cfg_method_rule", "update", {"id": row[0]}, sets))
    if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", RULE_NEW["rule_key"]):
        ops.append(("cfg_method_rule", "insert", {}, RULE_NEW))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2329: the nine observation items, the nuance pointers, RS-08 and RW-02 restated, "
                       f"RS-10; run_id {RUN_ID}. inactive=1 once applied."}))
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
    ops = plan(conn)
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
