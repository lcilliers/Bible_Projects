"""reading_phases_2273_v1_20261024.py -- escalations #2273 (B1) and #2274 (B2), one change set (#2268 builds;
design outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md, approved by the
researcher 2026-10-24: "D3 (a) confirmed: route on the party and link finding. Build B1 and B2 as one change set and
test on a copy.").

B2, the observation record (design sec 1 to 3):
1. A reading records findings of eight kinds, the kind being the observation's tag (D2): face, qualification,
   party, statement, link, use, term, silence. Each with its tag guidance.
2. ib_observation.route (cfg_enum observation_route), held on a party or link finding (D3).
3. ib_node.role (cfg_enum observation_role, per finding, D7), ib_node.reading_id (the reading that applied it: the
   home, RO10), ib_node.disposition and disposition_note (cfg_enum observation_disposition: where this verse ends up
   for this finding). ib_node.cluster_code restated as the word's own classification.
4. ib_observation_change: every change to an observation or a node, with its reason (RW-01).

B1, the reading on the phases (design sec 4):
5. reading.objective (0.C) and the times and files of the new gates; reading_state gains gathered, observed and
   narrated ('recorded' is retired: no reading holds it).
6. Steps: Open, Gather, Observe, Record, Check, Synergy, Apply, Narrate (D5), Publish, Account, with their grants.
7. The gap types by phase (pre, observe, post, narrate); cfg_setting reading.focus_words (the words in focus at the
   Observe gate, D8, qualifiers included); reading.observation_parts restated.
8. The method rules: the reading-a-verse rules move to reading.observe, the narrative rules to reading.narrate;
   RG-04 (qualifiers), RW-02, RW-03, RW-10 and RO11 restated on the model (one finding, many nodes).
9. cfg_status_flow ib_observation.reading restated; cfg_utility for the new library and this migration.

Tables and columns are built from their cfg_column rows (lib/db.table_ddl; ALTER for the added columns).
cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.
One transaction.

Usage:
    python iba/app/migration/reading_phases_2273_v1_20261024.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2273-READING-PHASES-20261024"
MODULE = "reading_phases_2273_v1_20261024"
SOURCE = ("escalations #2273, #2274, design v6 "
          "(outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md)")
FILLED = "iba/app/lib/observationrecord.py (through lib/reading.py)"
SEE = "see lib/reading.py (escalations #2228, #2273)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None, filled=FILLED):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": filled, "inactive": 0}


# ── B2 ──────────────────────────────────────────────────────────────────────────────────────────
KINDS = {   # tag: guidance (ib_observation.tag_guidance), the eight kinds of finding (design sec 1)
    "face": "a reading's finding (#2273): the sense a word carries in this occurrence, by what differs from its other "
            "occurrences (the object, the party, the direction of the word, the setting); applied by its nodes to every "
            "occurrence that shows the same face",
    "qualification": "a reading's finding (#2273): what a qualifier gives the characteristic it binds to, evaluated for "
                     "its value (grade, nature, impact, size and relation are examples, not a list); applied by its "
                     "nodes to the qualifier (role qualifier) and the characteristic (role characteristic)",
    "party": "a reading's finding (#2273): who bears, causes or receives the act, who else acts, where it comes from, "
             "toward or from God, with its setting and its route (A, B, C); applied by its nodes to every verse and "
             "word it covers",
    "statement": "a reading's finding (#2273): what the verse shows the inner being doing or undergoing, including what "
                 "sets it off, what follows and where it sits",
    "link": "a reading's finding (#2273): a link the verse states between words or characteristics (one leading to "
            "another, set against, named together, the same root as another), with its setting and, where it has one, "
            "its route",
    "use": "a reading's finding (#2273): how the words are used: the speaker's purpose, one phrase to different ends, "
           "one word in two senses",
    "term": "a reading's finding (#2273): the term's meaning in context against its lexicon entries, its surface "
            "variants and related words; a node with a strong and no verse applies it to the word in general",
    "silence": "a reading's finding (#2273): a word with no inner-being bearing in this occurrence (a name, a homonym, "
               "a superscription), with the reason (RG-10, RG-16)",
}
OBS_COLS = [("route", 26, "the route of a party or link finding (cfg_enum observation_route: A other beings in their "
             "own right, B another being with the inner being, C no bearing); held on the finding because it follows "
             "from what the finding describes (#2273 D3); NULL on every other kind", "enum.observation_route")]
NODE_COLS = [
    ("role", 13, "TEXT", None, "the word's role in this finding (cfg_enum observation_role: characteristic, qualifier, "
     "standalone), per finding: the same word can be the characteristic in one finding and a qualifier in another "
     "(#2273 D7). Required on a reading's node that names a word", "enum.observation_role"),
    ("reading_id", 14, "INTEGER", "reading.id", "the reading that applied the finding here: its home (RO10). NULL on "
     "nodes written before #2273", None),
    ("disposition", 15, "TEXT", None, "where this verse ends up for this finding (cfg_enum observation_disposition: "
     "told, claim, held, data, context, withdrawn); set at the reading's claim step, 'told' at Narrate; a soft delete "
     "is disposition withdrawn with its reason in ib_observation_change", "enum.observation_disposition"),
    ("disposition_note", 16, "TEXT", None, "the reason for the disposition, or the claim or item that carries it", None),
]
CHANGE = ("ib_observation_change", "one row per change to an observation or a node",
          "#2273 (RW-01): every change to a reading's observation or node, with its reason; nothing is overwritten. A "
          "soft delete is a change of the node's disposition, or of the observation's status, to withdrawn", [
    col("ib_observation_change", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
    col("ib_observation_change", "observation_id", 1, "INTEGER", "the observation changed, or whose node changed",
        nn=1, fk="ib_observation.id"),
    col("ib_observation_change", "node_id", 2, "INTEGER", "the node changed; NULL for a change to the observation",
        fk="ib_node.id"),
    col("ib_observation_change", "column_name", 3, "TEXT", "the column changed", nn=1),
    col("ib_observation_change", "old_value", 4, "TEXT", "the value before"),
    col("ib_observation_change", "new_value", 5, "TEXT", "the value after"),
    col("ib_observation_change", "reason", 6, "TEXT", "why, in words (required)", nn=1),
    col("ib_observation_change", "reading_id", 7, "INTEGER", "the reading that made the change", fk="reading.id"),
    col("ib_observation_change", "run_id", 8, "TEXT", "the run that made the change"),
    col("ib_observation_change", "created_at", 9, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
    col("ib_observation_change", "created_by", 10, "TEXT", WHO, nn=1, dflt="'direct edit'"),
])
TABLE_USE = {
    "ib_node": "The application of a finding: one row per verse, word, cluster, subgroup, question or other observation "
               "the finding applies to, with the word's role in it, the reading that applied it and where the verse "
               "ends up (#2273). A finding applying to several verses or words carries several nodes (#2268 R16).",
    "ib_observation": "One finding: a distinct description (its text, meaning, implication, basis, kind as tag and, on a "
                      "party or link finding, its route), applied through ib_node to every verse and word it covers "
                      "(#2273). Written by reading.record and reading.gather. It also holds gathered rows of the older "
                      "stages: the September catalogue work (verse-reading, char-*) and the October ledger work "
                      "(strand-reading). Status meanings are by stage (cfg_status_flow).",
}
CHANGE_INDEX = [("idx_ib_observation_change_observation_id", "observation_id")]
NODE_INDEX = [("idx_ib_node_reading_id", "reading_id")]

# ── B1 ──────────────────────────────────────────────────────────────────────────────────────────
READING_COLS = [
    ("objective", 17, "the scope's objective (0.C): it defines the home of what the reading records (RO10); NULL on "
     "readings opened before #2273"),
    ("gathered_at", 18, "when the pre gate passed (0.GAP pre written into the tables)"),
    ("observe_file", 19, "the observe JSON written at Observe (the verses, the words in focus, the findings to record)"),
    ("observe_built_at", 20, "when the observe JSON was built from the tables; Record refuses a file that does not carry "
     "it"),
    ("observed_at", 21, "when the Observe gate passed"),
    ("narrate_file", 22, "the narrate JSON, built from the tables when the claims gate passes"),
    ("narrated_at", 23, "when the Narrate gate passed"),
]
STATES = ["open", "gathered", "observed", "synergised", "narrated", "published", "withdrawn"]
ITEMS = ["escalation_thread_item", "escalation_thread_item_verse"]
FINDINGS = ["ib_observation", "ib_node", "ib_observation_change"]
NARR = ["narrative_claim", "narrative_claim_source", "narrative_claim_telling", "narrative_claim_change"]
REWRITE = ["narrative_update", "narrative_update_ref", "narrative_section", "narrative_claim_telling",
           "narrative_claim_change", "narrative_citation", "narrative_chapter", "verse_meta"]
STEPS = [  # step, ordinal, does, write grants
    ("open", 0, "0.C and the pre-gaps: a reading opened on a scope with its objective (the selectors of "
     "Verse-Scope.ps1; the 2,500 review applies): its verses kept, the scope collated, and the pre-gap JSON written, one "
     "section per gap type of phase pre", ["reading", "reading_verse"]),
    ("gather", 1, "0.GAP pre written into the tables: each pre-gap item's record (a finding, a named row, a face on a "
     "strand hit, a response on an open item, or a reason) and new open items; the ids written back into the file",
     sorted(set(FINDINGS + ["reading_strand_hit", "reading"] + ITEMS))),
    ("observe", 2, "D3 and D4 input: the observe JSON built from the tables once the reading is gathered -- per verse, "
     "its passage, every finding applied to it with its nodes, the words in focus (qualifiers included, "
     "reading.focus_words), and the current claims on the scope", ["reading"]),
    ("record", 3, "D4 observe written: the observe JSON's findings (one observation each, applied by its nodes; a "
     "duplicate description becomes new nodes), soft deletes with their reasons, each word's open item or reason; ids "
     "written back into the file", sorted(set(FINDINGS + ["reading"] + ITEMS))),
    ("check", 4, "the gate the reading is at, checked from the tables: pre (open -> gathered), observe (gathered -> "
     "observed; the verses then marked analysed), claims (observed -> synergised; the narrate JSON then built) or "
     "narrate (synergised -> narrated)", ["reading", "verse_meta"]),
    ("synergy", 5, "D4 claims input: the synergy JSON built from the tables for the scope -- the reading's findings with "
     "their nodes, the claims, the matched open items -- never memory", ["reading"]),
    ("apply", 6, "D4 claims written: claims new, edited, withdrawn, each source naming its finding; each node's "
     "disposition; open items settled or carried forward",
     sorted(set(NARR + FINDINGS + ["reading"] + ITEMS))),
    ("narrate", 7, "D4 narrate written: tellings, holds and blocks rewritten to the style rows; the nodes whose claim is "
     "told marked told", sorted(set(REWRITE + ["ib_node", "ib_observation_change", "narrative_claim", "reading"]))),
    ("publish", 8, "the chapters the reading touched published from the database, copied to the learning4comfort inbox "
     "and checked byte-identical", ["narrative_chapter", "reading"]),
    ("account", 9, "the reading from the tables: its state, each gate's gaps (read-only)", []),
]
PHASES = {"term_cluster": "pre", "meaning_missing": "pre", "base_missing": "pre", "term_reading_missing": "pre",
          "read_in_files_only": "pre", "face_not_gathered": "pre", "open_item": "pre",
          "not_read": "observe", "observation_part_missing": "observe", "observation_unsupported": "observe",
          "observed_no_claim": "post", "claim_without_observation": "post",
          "claim_not_told": "narrate", "citation_without_record": "narrate"}
GUIDES = {
    "not_read": "A word in focus (reading.focus_words: every M-code word, every qualifier, every negator) with no "
                "finding of this reading applied to it. Read the verse in its passage with every finding already "
                "applied to it in focus; apply a finding (an existing one, or a new one) to the word, raise an open "
                "item, or give the reason.",
    "observation_part_missing": "A finding without what its kind needs: a node without the word's role; a party "
                                "finding without its route; a qualification finding without both its qualifier and its "
                                "characteristic. Presence of something that is not the right thing is not a resolved gap.",
    "observation_unsupported": "A finding the verse no longer supports. Withdraw its node for this verse, or the "
                               "finding everywhere, with the reason (ib_observation_change).",
    "face_not_gathered": "A face recorded for a word occurrence (the ledger faces, a strand hit) that no face finding "
                         "holds. Gather it as a face finding, or give the strand hit its face, or the reason.",
    "read_in_files_only": "A verse an earlier study file reads (its lines are given) with no finding in the tables. "
                          "Gather the reading into a finding, or give the reason the file's reading holds nothing.",
    "observed_no_claim": "A node of this reading with no disposition: carry its finding by a claim, hold it on an "
                         "item, or dispose of it (data, context, withdrawn) with a reason. Checked against the claims "
                         "(0.GAP post).",
}
FOCUS = {"tags": ["T2", "T5"],
         "function_word_morph": {"OT": ["HR", "HS", "HT", "HP", "HC", "AR", "AS", "AT", "AP", "AC"],
                                 "NT": ["P", "PREP", "R", "D", "I", "COND", "X", "F", "S", "PRT", "K", "C", "T", "CONJ"]},
         "applies": "the words in focus at the Observe gate (#2273 D8): every M-coded word; every word in "
                    "reading.non_characteristic_strongs; and every word tagged with one of `tags` (T2 qualifiers, T5 "
                    "negators), except a T2 word whose morph marks a function word (RG-22): OT, the first two letters "
                    "of the morph; NT, the part before the first '-'"}
PARTS = {"kinds": list(KINDS),
         "finding": ["obs_text", "meaning", "implication", "basis", "tag", "route"],
         "node": ["verse_reference", "strong", "surface", "morph_code", "cluster_code", "role", "reading_id",
                  "disposition", "disposition_note", "traced_observation_id", "question_code"],
         "rule": "one finding per description, applied by its nodes (#2273); the face, the qualification, the "
                 "parties and the operation (statement) are findings, not columns"}
PROMPTS = {  # the catalogue's 53 questions of one verse, by the kind of finding they prompt (RG-17; synthesis sec 5)
    "face": ["M0.1.1", "M0.1.3", "M0.4.1", "M0.5.1", "M0.5.2", "M0.5.3", "M0.5.4", "M0.5.11"],
    "qualification": ["M0.8.1"],
    "party": ["D5.2.1", "D7.1.1", "D7.2.1", "D7.3.1", "D7.4.1", "D7.5.1", "D7.6.1", "D7.7.1", "M0.7.9", "M0.7.11",
              "M0.7.12", "M0.7.13", "M0.7.14", "M0.7.15", "M0.7.16"],
    "statement": ["D1.1.1", "D2.1.1", "D3.1.1", "D6.1.1", "D10.1.1", "D10.2.1", "D10.3.1", "D10.4.1", "D10.6.1",
                  "F0.1.1", "M0.7.1", "M0.7.2", "M0.7.3", "M0.7.4", "M0.7.6", "M0.7.7", "M0.7.8", "M0.7.10"],
    "link": ["D10.5.1", "M0.6.5", "M0.6.6", "M0.7.5"],
    "use": ["M0.6.1"],
    "term": ["M0.1.2", "M0.5.5", "M0.5.6", "M0.5.7", "M0.5.8", "M0.5.9"],
    "silence": [],
}
SETTINGS_NEW = [("reading.focus_words", FOCUS, "the words in focus at the Observe gate, qualifiers included (#2273 D8; "
                 "RG-22, RG-23)"),
                ("reading.observe_prompts", PROMPTS, "the catalogue questions of one verse given in the observe JSON as "
                 "prompts, under the kind of finding each serves; a prompt that does not apply is not answered (RG-17; "
                 "#2273, outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md sec 5)")]
RULE_MOVES = {"reading.record": "reading.observe", "reading.apply": "reading.narrate"}
RESTATE = {
    "RG-04": "A qualifier gets no separate account of itself, but what it gives the characteristic it binds to is "
             "evaluated for its value and recorded as a qualification finding, applied by its nodes to the qualifier "
             "(role qualifier) and the characteristic (role characteristic). What it gives can vary widely: grade, "
             "nature, impact, size, relation, a measure, strengthening, ground, cause, object, setting or bait are "
             "examples, not a list (#2273 D9). A qualifier whose usage varies across contexts may earn its own reading "
             "later.",
    "RW-02": "A reading records findings of eight kinds (cfg_setting reading.observation_parts; the kind is the tag): "
             "face, qualification, party, statement, link, use, term, silence. A finding holds its text, meaning, "
             "implication, basis and, on a party or link finding, its route; its nodes hold the verse, the word, the "
             "word's own classification, its role in the finding, the reading that applied it and where the verse "
             "ends up. The term reading results (meaning in context, surface variants, related terms) are term "
             "findings.",
    "RW-03": "One observation per finding: the same description is never written twice. Applied to another verse, "
             "word or scope it gains a node on the existing observation.",
    "RO11": "One observation per finding, never a duplicate description; a finding applying to several verses or "
            "words carries several nodes, each with the word's role in it.",
    "RW-10": "Where a verse ends up for a finding is recorded on the node (ib_node.disposition, cfg_enum "
             "observation_disposition: told, claim, held, data, context, withdrawn), with its reason or carrier.",
}
FLOW = {  # status: set_by, inactive
    "draft": ("recorded by a reading (reading.record or reading.gather); dispositions are on the nodes (#2273)", 0),
    "resolved": ("not set from #2273: a finding's dispositions are on its nodes", 1),
    "open": ("not set from #2273: a finding's dispositions are on its nodes", 1),
    "silent": ("not set from #2273: a finding's dispositions are on its nodes", 1),
    "withdrawn": ("a reading: the finding is wrong everywhere, with the reason in ib_observation_change (RW-01)", 0),
}
REPOINT = [  # table, key, column, old text, new text: the narrative is written at Narrate now (D5)
    ("cfg_behaviour_rule", 76, "rule_text", "(the narrative itself: -Step Apply)", "(the narrative itself: -Step Narrate)"),
    ("cfg_setting", "governance.narrative_home", "value", "written through Reading.ps1 -Step Apply",
     "written through Reading.ps1 -Step Narrate"),
]
RN15 = ("It is named in the observation's parties", "It is named in a party finding")
CONTROL_HOME = ("cfg_method_rule (steps reading.open, reading.observe, reading.check, reading.narrate; word.read and "
                "cluster.read when built), cfg_quality_check (reading.check), cfg_setting reading.*, with "
                "cfg_prose_concept pointers to the glossary")
UTILITIES = [
    ("observationrecord", "iba/app/lib/observationrecord.py", "observationrecord.py -- the observation record (#2274): "
     "a reading's findings, one ib_observation each, applied by ib_node rows with the word's role, the reading and the "
     "verse's disposition; duplicates become nodes; every change kept with its reason (ib_observation_change).", 0,
     None),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    # B2: columns, table, enums, tag guidance
    for name, o, use, exp in OBS_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name=?", name):
            ops.append(("cfg_column", "insert", {}, col("ib_observation", name, o, "TEXT", use, exp=exp)))
    for name, o, typ, fk, use, exp in NODE_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='ib_node' AND name=?", name):
            ops.append(("cfg_column", "insert", {}, col("ib_node", name, o, typ, use, fk=fk, exp=exp)))
    node_cc = ("the word's own classification: its M-code, or the T-code found relevant, checked against cluster_strong "
               "when a reading writes it (#2273). Nodes written before #2273 may hold the cluster of the pass that "
               "cited the word; they are corrected only where a re-read finds them wrong (#2273 D6)")
    if one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='ib_node' AND name='cluster_code'")[0] != node_cc:
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "ib_node", "name": "cluster_code"},
                    {"use": node_cc}))
    t, grain, use, cols = CHANGE
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": grain, "use": use, "inactive": 0,
                                                "category": "data"}))
    for c in cols:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", t, c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for table, idx in ((t, CHANGE_INDEX), ("ib_node", NODE_INDEX)):
        for name, c in idx:
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", table, name):
                ops.append(("cfg_index", "insert", {}, {"table_name": table, "name": name, "col": c, "ordinal": 0}))
    for kind in KINDS:
        if not has("SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=?", kind):
            o = one("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name='ib_observation.tag'")[0]
            ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.tag", "value": kind, "ordinal": o,
                                                   "inactive": 0}))
    guide = json.loads(one("SELECT value FROM cfg_setting WHERE key='ib_observation.tag_guidance'")[0])
    guide = json.loads(guide) if isinstance(guide, str) else guide
    if any(k not in guide for k in KINDS):
        ops.append(("cfg_setting", "update", {"key": "ib_observation.tag_guidance"},
                    {"value": json.dumps({**guide, **KINDS}, ensure_ascii=False)}))
    for name, use in TABLE_USE.items():
        if one("SELECT use FROM cfg_table WHERE database='iba' AND name=?", name)[0] != use:
            ops.append(("cfg_table", "update", {"database": "iba", "name": name}, {"use": use}))
    # B1: reading columns and states
    for name, o, use in READING_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='reading' AND name=?", name):
            ops.append(("cfg_column", "insert", {}, col("reading", name, o, "TEXT", use, filled="iba/app/lib/reading.py")))
    for i, state in enumerate(STATES):
        r = one("SELECT ordinal, inactive FROM cfg_enum WHERE name='reading_state' AND value=?", state)
        if r is None:
            ops.append(("cfg_enum", "insert", {}, {"name": "reading_state", "value": state, "ordinal": i, "inactive": 0}))
        elif r[0] != i:
            ops.append(("cfg_enum", "update", {"name": "reading_state", "value": state}, {"ordinal": i}))
    if has("SELECT 1 FROM cfg_enum WHERE name='reading_state' AND value='recorded' AND inactive=0") and \
            not has("SELECT 1 FROM reading WHERE state='recorded'"):
        ops.append(("cfg_enum", "update", {"name": "reading_state", "value": "recorded"}, {"inactive": 1}))
    # steps, grants, refused routes
    for step, o, does, grants in STEPS:
        sid = f"reading.{step}"
        row = one("SELECT ordinal, does FROM cfg_step WHERE step=?", sid)
        text = f"{does} -- {SEE}"
        if row is None:
            ops.append(("cfg_step", "insert", {}, {"work_package": "reading", "ordinal": o, "step": sid,
                                                   "handler": f"iba.app.handlers.reading:{step}", "scope": "none",
                                                   "does": text, "inactive": 0, "kind": "utility"}))
        elif tuple(row) != (o, text):
            ops.append(("cfg_step", "update", {"step": sid}, {"ordinal": o, "does": text}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", sid):
            ops.append(("cfg_on_fail", "insert", {}, {
                "step": sid, "condition": "refused", "path": "report-continue", "resolver": None, "route": "terminal",
                "message": "refused, nothing written -- the reason follows (a usage outcome, not recorded as an "
                           "escalation)", "inactive": 0}))
        live = {r[0]: r[1] for r in conn.execute("SELECT table_name, inactive FROM cfg_write_grant WHERE writer=?",
                                                 (sid,))}
        for table in grants:
            if table not in live:
                ops.append(("cfg_write_grant", "insert", {}, {"writer": sid, "table_name": table, "database": "iba",
                                                              "inactive": 0}))
            elif live[table]:
                ops.append(("cfg_write_grant", "update", {"writer": sid, "table_name": table, "database": "iba"},
                            {"inactive": 0}))
        for table, inactive in live.items():
            if table not in grants and not inactive:
                ops.append(("cfg_write_grant", "update", {"writer": sid, "table_name": table, "database": "iba"},
                            {"inactive": 1}))
    # gap types by phase; focus words; parts
    gt = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.gap_types'")[0])
    gt = json.loads(gt) if isinstance(gt, str) else gt
    new_gt = {k: {**v, "phase": PHASES[k], "guide": GUIDES.get(k, v["guide"])} for k, v in gt.items()}
    if new_gt != gt:
        ops.append(("cfg_setting", "update", {"key": "reading.gap_types"}, {
            "value": json.dumps(new_gt, ensure_ascii=False),
            "use": "the reading's gap types (cfg_enum reading_gap_type): each one's phase (pre: the pre-gap JSON, the "
                   "pre gate; observe: the Observe gate; post: the claims gate; narrate: the Narrate gate), the table(s) "
                   "it records into and its guide text; adding a gap type is an enum value and an entry here (#2228, "
                   "#2273)"}))
    for key, value, use in SETTINGS_NEW:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value, ensure_ascii=False),
                                                      "module": "reading", "inactive": 0, "use": use}))
    parts = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0])
    if parts != PARTS:
        ops.append(("cfg_setting", "update", {"key": "reading.observation_parts"}, {
            "value": json.dumps(PARTS, ensure_ascii=False),
            "use": "the eight kinds of finding a reading records (the tag), what a finding holds and what its nodes "
                   "hold (#2273 design v6)"}))
    # method rules: moved and restated
    for (rid, step, key) in conn.execute("SELECT id, step, rule_key FROM cfg_method_rule WHERE active=1 AND step IN "
                                         "('reading.record', 'reading.apply')").fetchall():
        sets = {"step": RULE_MOVES[step]}
        short = key.split(" ", 1)[0]
        if short in RESTATE:
            sets["rule_text"] = RESTATE[short]
        ops.append(("cfg_method_rule", "update", {"id": rid}, sets))
    for (rid, key, text) in conn.execute("SELECT id, rule_key, rule_text FROM cfg_method_rule WHERE active=1 AND step="
                                         "'reading.observe'").fetchall():
        short = key.split(" ", 1)[0]
        if short in RESTATE and text != RESTATE[short]:
            ops.append(("cfg_method_rule", "update", {"id": rid}, {"rule_text": RESTATE[short]}))
    # status flow
    for status, (set_by, inactive) in FLOW.items():
        r = one("SELECT set_by, inactive FROM cfg_status_flow WHERE entity='ib_observation.reading' AND status=?", status)
        if r is not None and tuple(r) != (set_by, inactive):
            ops.append(("cfg_status_flow", "update", {"entity": "ib_observation.reading", "status": status},
                        {"set_by": set_by, "inactive": inactive}))
    # rows that still name the old step or shape
    for table, key, col_, old, new in REPOINT:
        kcol = "id" if table == "cfg_behaviour_rule" else "key"
        r = one(f"SELECT {col_} FROM {table} WHERE {kcol}=?", key)
        if r and old in r[0]:
            ops.append((table, "update", {kcol: key}, {col_: r[0].replace(old, new)}))
    r = one("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE 'RN-15 %' AND active=1")
    if r and RN15[0] in r[1]:
        ops.append(("cfg_method_rule", "update", {"id": r[0]}, {"rule_text": r[1].replace(*RN15)}))
    # the control map's home of the study method
    if one("SELECT home FROM cfg_control_home WHERE kind='study_method'")[0] != CONTROL_HOME:
        ops.append(("cfg_control_home", "update", {"kind": "study_method"}, {"home": CONTROL_HOME}))
    # utilities
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    r = one("SELECT purpose FROM cfg_utility WHERE module='reading'")
    if r and "#2273" not in r[0]:
        ops.append(("cfg_utility", "update", {"module": "reading"}, {
            "purpose": "reading.py -- the reading process (#2228, phases #2273): Open (0.C and the pre-gaps), Gather "
                       "and Check (pre gate), Observe, Record and Check (Observe gate), Synergy, Apply and Check (claims "
                       "gate), Narrate and Check (Narrate gate), Publish, and Account; findings through "
                       "observationrecord; reuses strandreading, narrativeregister, openitem and versecollate."}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalations #2273 and #2274: the observation record (findings and their "
                       f"nodes, ib_observation_change) and the reading on its phases (Gather, Observe, Narrate; gates "
                       f"pre, observe, claims, narrate); run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    cols = {t: {r[1] for r in conn.execute(f"PRAGMA table_info({t})")} for t in ("ib_observation", "ib_node", "reading")}
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    print(f"{len(ops)} cfg write(s); {CHANGE[0]} live: {CHANGE[0] in live}")
    if a.dry_run:
        for t, op, where, set_ in ops:
            print(f"  {op:6} {t} {json.dumps(where)[:80]} {', '.join(set_)[:100]}")
        return 0
    try:
        conn.execute("SAVEPOINT reading_phases")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for name, *_ in OBS_COLS:
            if name not in cols["ib_observation"]:
                conn.execute(f'ALTER TABLE ib_observation ADD COLUMN "{name}" TEXT')
        for name, _o, typ, fk, *_ in NODE_COLS:
            if name not in cols["ib_node"]:
                ref = f' REFERENCES "{fk.split(".")[0]}"("{fk.split(".")[1]}")' if fk else ""
                conn.execute(f'ALTER TABLE ib_node ADD COLUMN "{name}" {typ}{ref}')
        for name, *_ in READING_COLS:
            if name not in cols["reading"]:
                conn.execute(f'ALTER TABLE reading ADD COLUMN "{name}" TEXT')
        if CHANGE[0] not in live:
            create_sql, index_sql = table_ddl(cfg, CHANGE[0])
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        for name, c in NODE_INDEX:
            conn.execute(f'CREATE INDEX IF NOT EXISTS "{name}" ON ib_node("{c}")')
        conn.execute("RELEASE reading_phases")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO reading_phases")
        conn.execute("RELEASE reading_phases")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
