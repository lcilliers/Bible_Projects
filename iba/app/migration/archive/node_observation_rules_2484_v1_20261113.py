"""node_observation_rules_2484_v1_20261113.py -- escalation #2484: the node and observation rules, registered in config (B:31, governance.rules_must_be_config_driven).

The researcher's rulings of 2026-11-12 and 2026-11-13 (verbatim on #2484, #2487; the last of them: 'if the same observation wording applies to multiple
collections then their will be a node for each collection ... if two nodes refer to the same observation, and indexing columns of the node is exactly the
same, then the node is either incomplete ... or a duplicate ... standalone may be relevant ... clusters and sub groups have served their purpose in the
creation and establishment of the collections. notes and observations should not have any part to play with clusters and sub groups. all rules associated to
the maintenance of clusters and sub groups in the observations process must be retired ... reset the stale columns ... if the observation cannot be revived
to fit the rules, then it must be retired with its nodes. This applies to all observations') are stated in two behaviour rules without adding to them.

Writes (all through configmaint.apply_logged, one run):
  1. two behaviour rules (class study_method, general scope, study_active): the node rules and the observation rules;
  2. behaviour rule 121 restated without the cluster anomaly group and the subgroup sentence;
  3. behaviour rules 70 and 122 and method rule RA-01 retired (cluster and subgroup maintenance in the observation process), their scope rows inactive;
  4. cfg_setting reading.node_roles gains the group `recognised` (standalone) and reading.surface_requirements.covered_by says so;
  5. cfg_column text restated for ib_node (collection_id, verse_lexical_id, surface, strong, morph_code, role, cluster_code, cluster_subgroup_code).
Not done here (code enforces them; raised as its own escalation): CP-07, CP-09, CP-10, NR-01, NR-04, behaviour rules 117 to 120, RO13, the NOT NULL on ib_node.cluster_code.

Refuses to run twice.   python -m iba.app.migration.archive.node_observation_rules_2484_v1_20261113 [--db PATH] [--dry-run]   (from the project root)"""
import argparse
import datetime
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2484-NODE-OBSERVATION-RULES-20261113"
MODULE = "node_observation_rules_2484_v1_20261113"
SRC = ("Researcher rulings, escalations #2484 and #2487 (2026-11-12 and 2026-11-13 developer-mode sessions), verbatim on #2484 and #2487; "
       "outputs/escalation/2487-node-salvage-plan-v3-20261112.md (R1 to R13) and #2273 design v6 (2026-10-24) as the earlier rulings they restate.")

NODE_KEY = "nodes-index-the-collection-and-comply-with-the-node-rules"
NODE_TEXT = (
    "A node is the cross-reference that links a verse to the element an observation evaluates, and it is how the study finds things: the observations and nodes of "
    "a collection are found through the collection on the node, with no other index. A node cannot exist without a live observation, and a live observation has at "
    "least one live node; a node has one surface; where an observation refers to several variants (verses, surfaces, Strong's codes, collections or the other "
    "mapping columns) it has a node for each variant. The scope is the live collections: a verse is in scope when it holds an occurrence of a member surface; "
    "entity and other surfaces of an in-scope verse are in scope as nodes of the observation that covers them; a verse with only entity or other surfaces is out "
    "of scope and is not touched. Every collection surface has at least one finding (an observation with a node), read on the nodes. The collection is on the "
    "node: a node on a collection surface carries its surface's collection (its own row, else its base); a node on an entity or other surface carries the "
    "collection of the surface it supports; an in-scope node without a collection is an error. Two live nodes of one observation whose indexing columns are all "
    "the same are either incomplete or a duplicate: an incomplete node is completed, a duplicate is withdrawn with its reason, and a duplicate is not written. "
    "A node carries verse_reference, verse_lexical_id, surface, strong, morph_code, collection_id, role, source_stage, seq, created_at and deleted: the "
    "verse_lexical row of the occurrence fixes the verse_lexical_id, surface, strong and morph_code (the surface is the lens, per Strong's); the role is the "
    "word's role in this finding, from this verse and never from a cluster tag. Characteristic and qualifier are relevant; object, relational_target and "
    "enactment bear on (cfg_setting reading.node_roles); standalone records that the word was recognised and has no inner-being role on any other surface of the "
    "verse. A node withdrawn, or a finding the verse no longer supports, is a soft delete with its reason in ib_observation_change, never a physical delete. "
    "Clusters and sub groups served to establish the collections and play no part in nodes and observations; cluster_code and cluster_subgroup_code are history. "
    "Salvaging a node: a missing column that can be derived from the item's context is derived; where a re-read is needed it is done; the work is by hand, "
    "verified, in small steps, with each node's validation flag set only by the validation process, and a class is changed in bulk only after a pilot of the same "
    "class with the counts predicted and checked; no sweeping update without checking that it has the right effect.")
NODE_ENF = ("Partly: the writer refuses a node on an occurrence the observation already has (iba/app/lib/engagement.py) and a role outside cfg_setting "
            "reading.node_roles (iba/app/lib/observationrecord.py); the rest is context-delivered while the study is active, and is checked by the node validation "
            "process still to be built (#2484).")
OBS_KEY = "observations-are-founded-unique-and-fit-the-node-rules"
OBS_TEXT = (
    "An observation is an application or analytic statement that interprets what its verse says and is founded in the verse. It is never a repeat of the verse "
    "text (not more than the number of consecutive verse words in reading.observation_items max_verse_words_copied) and never a statement the verse does not "
    "found. It is tied to verses or surfaces; one that is not is malformed and is restated specific to its verses and surfaces, with a node for each, the restatement "
    "drafted by Claude and approved by the researcher. The same wording and meaning is never two observations: it is one observation with a node for each variant it "
    "refers to; a second live observation with the same text is a duplicate and is withdrawn with its nodes moved to the first. Different stages produced "
    "different kinds of observation, and the kinds, tags and parts of an older observation need not be consistent or a full read, provided it complies with "
    "these rules and the node rules: the collections are read again to enhance the observations. An observation of any stage that cannot be revived to comply is "
    "retired with its nodes, as a soft delete with its reason in ib_observation_change.")
OBS_ENF = ("Partly: the writer refuses a second live observation with the same text and adds nodes to the existing one (reading.observation_rules "
           "merge_same_text_only, iba/app/lib/observationrecord.py); the rest is context-delivered while the study is active and checked by the node validation "
           "process still to be built (#2484).")
R121 = ("The record of reading is kept per occurrence: each word in each verse, one verse_lexical row. A node that cannot be placed on a single occurrence is cleared by "
        "hand. Observations that say the same thing over several verses stay one observation and give one claim, with an anchor verse, traceable to every related verse.")
RET = ("INACTIVATED 2026-11-13, researcher decision on #2484 (verbatim): 'clusters and sub groups have served their purpose in the creation and establishment of the "
       "collections. notes and observations should not have any part to play with clusters and sub groups. all rules associated to the maintenance of clusters and sub "
       "groups in the observations process must be retired.'")
COLS = {
    "collection_id": ("the collection of the node, through which its observation and the node are found (#2484, #2487; researcher 2026-11-12 and 2026-11-13): on a "
                      "collection surface the one collection of the node's surface (its own row, else its base; each surface is in exactly one collection); on an entity or "
                      "other surface of an in-scope verse the collection of the surface it supports. Required on every in-scope node; NULL only on a node not yet validated."),
    "verse_lexical_id": ("the verse_lexical row of the occurrence the node reads; required in scope. Found from the verse and the surface (narrowed by the observation's "
                         "Strong's code); where it cannot be found it is settled by hand and the node is held, never guessed"),
    "surface": "the surface of the verse_lexical row of the node (verse_lexical.surface), the lens per Strong's; required",
    "strong": "the Strong's code of the verse_lexical row of the node; required",
    "morph_code": "the morphology code of the verse_lexical row of the node; required",
    "role": ("the word's role in this finding, from this verse and never from a cluster tag (cfg_enum observation_role): characteristic and qualifier are relevant; "
             "object, relational_target and enactment bear on; standalone records that the word was recognised and has no inner-being role on any other surface of the "
             "verse. Required on a node that names a word; judged per finding by reading the observation"),
    "cluster_code": ("history, not analytic (#2484, 2026-11-13: clusters served to establish the collections and play no part in nodes and observations). The column is "
                     "still NOT NULL in the schema and is written as the word's code from cluster_strong; nothing reads it for analysis"),
    "cluster_subgroup_code": "history, not analytic (#2484, 2026-11-13); nothing reads it for analysis",
}


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn):
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    nid = one("SELECT max(id) FROM cfg_behaviour_rule")[0] + 1
    for key, text, enf in ((NODE_KEY, NODE_TEXT, NODE_ENF), (OBS_KEY, OBS_TEXT, OBS_ENF)):
        if not one("SELECT 1 FROM cfg_behaviour_rule WHERE class='study_method' AND rule_key=?", key):
            ops.append(("cfg_behaviour_rule", "insert", {}, {
                "id": nid, "class": "study_method", "rule_key": key, "rule_text": text, "source": SRC, "enforced_by": enf, "added_at": now(),
                "active": 1, "enforcement_status": "partially_enforced", "deliver_when": "study_active"}))
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{nid}", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
            nid += 1
    ops.append(("cfg_behaviour_rule", "update", {"id": 121}, {"rule_text": R121}))
    for rid in (70, 122):
        ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"active": 0, "enforcement_status": "deliberately_deferred", "enforced_by": RET}))
        for (sid,) in conn.execute("SELECT id FROM cfg_rule_scope WHERE rule_ref=? AND inactive=0", (f"B:{rid}",)).fetchall():
            ops.append(("cfg_rule_scope", "update", {"id": sid}, {"inactive": 1}))
    ops.append(("cfg_method_rule", "update", {"id": 202}, {"active": 0}))
    roles = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.node_roles'")[0])
    if "recognised" not in roles:
        roles["recognised"] = ["standalone"]
        ops.append(("cfg_setting", "update", {"key": "reading.node_roles"}, {"value": json.dumps(roles)}))
    req = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.surface_requirements'")[0])
    if "recognised" not in req["covered_by"]:
        req["covered_by"] = ("a live node with a role from reading.node_roles on the surface's occurrence (relevant, bears_on, or recognised: a surface with no "
                             "inner-being role, whose node records that it was recognised)")
        ops.append(("cfg_setting", "update", {"key": "reading.surface_requirements"}, {"value": json.dumps(req)}))
    for name, use in COLS.items():
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "ib_node", "name": name}, {"use": use}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2484: the node and observation rules registered; run_id {RUN_ID}."}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, s in ops:
            print(f"  {op:6} {t:20} {where or s.get('rule_key') or s.get('module') or s.get('rule_ref')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
