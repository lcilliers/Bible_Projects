"""layers_2505_v1_20261115.py -- escalation #2505 (researcher, 2026-11-15, under #2463: "comply with governance ... get it done"; design
outputs/escalation/2505-layers-1-2-build-design-v1-20261115.md).

Registers the layered reading of a collection (layer 1 steps 1.1 and 1.2, layer 2 step 2.1) in config and creates what it needs:
  tables / columns   collection_layer_item (the ledger: one row for each aspect a step demands) and ib_node.subgroup_id (the group on the node)
  enums              ib_observation.stage layer-1 and layer-2; ib_observation.tag group, enrichment, pairing, relation; collection_layer_item.state
  settings           layer.reading (steps, items, kinds, stages, thresholds), layer.working_dir, layer.check_name
  steps              collection.layer_open, layer_pull, layer_record, layer_check, node_groups (work package collection-build), their routed condition, write grants
  rules              three behaviour rules (the layers; lexical and claims readings separate; the ledger), B:119 and B:120 reworded for collections, B:127 and B:130 restated,
                     method rules LR-01 to LR-05, RW-02 and RG-09 restated, RO13 retired
  utilities          the library layerreading and this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/layers_2505_v1_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2505-LAYERS-20261115"
MODULE = "layers_2505_v1_20261115"
SOURCE = "escalation #2505 (researcher, 2026-11-15; outputs/escalation/2505-layers-1-2-build-design-v1-20261115.md; the layer definition on #2463 v16, answers v18 to v22)"
FILLED = "Collection-Build.ps1 -Action LayerOpen, LayerRecord, LayerCheck, lib/layerreading.py"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"
T = "collection_layer_item"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None, filled=FILLED):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ, "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": filled, "inactive": 0}


TABLE = ("one row for each aspect a step of the layered reading demands of a collection",
         "#2505: the ledger of the layered reading. When a step is opened (Collection-Build.ps1 -Action LayerOpen) one row is made for each aspect the data demands of it (a group definition, a group's "
         "Strong's enrichment, a pairing of a group with a partner collection, a qualifier, entity, direction or double-meaning aspect, a relation between two groups). A row is answered by an observation "
         "(state observed, observation_id) or, where cfg_setting layer.reading allows it, by none with its reason; it is validated only by LayerCheck, which re-derives what the row demands from the tables. "
         "A step is closed when every row is answered and validated; the next step does not open before. A row whose aspect the data no longer demands is retired, never deleted. The groups are the "
         "researcher's (collection_subgroup); the rows are derived, never typed")
COLS = ([col(T, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
         col(T, "collection_id", 1, "INTEGER", "the collection the aspect belongs to", nn=1, fk="collection.id"),
         col(T, "step", 2, "TEXT", "the step of the layered reading that demands it (layer.reading steps): 1.1, 1.2 or 2.1", nn=1),
         col(T, "item", 3, "TEXT", "the kind of aspect (layer.reading items): group-definition, strong-enrichment, pairing, qualifier, entity, direction, group-relation, double-meaning", nn=1),
         col(T, "subgroup_id", 4, "INTEGER", "the group the aspect is about (for a relation between two groups, the one with the lower id)", nn=1, fk="collection_subgroup.id"),
         col(T, "subject", 5, "TEXT", "what distinguishes the aspect within a group: the partner collection of a pairing, the other group of a relation (its id), the surface of a double meaning; empty otherwise", nn=1, dflt="''"),
         col(T, "state", 6, "TEXT", "open (to be answered), observed (answered by observation_id), none (answered: nothing to observe, with the reason), retired (the data no longer demands it)", nn=1, dflt="'open'",
             exp="enum.collection_layer_item.state"),
         col(T, "observation_id", 7, "INTEGER", "the ib_observation that answers the aspect (state observed)", fk="ib_observation.id"),
         col(T, "reason", 8, "TEXT", "why none (state none): the reading's reason, in words; why retired"),
         col(T, "validated", 9, "INTEGER", "1 when LayerCheck found the answer to agree with what the tables demand; set only by LayerCheck, cleared when the row is answered again", nn=1, dflt="0"),
         col(T, "run_id", 10, "TEXT", "the run that wrote the row"),
         col(T, "created_at", 11, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
         col(T, "updated_at", 12, "TEXT", "when last changed (ISO-8601 UTC)"),
         col(T, "created_by", 13, "TEXT", WHO, nn=1, dflt="'direct edit'"),
         col(T, "deleted", 14, "INTEGER", "soft delete: 1 when the row is no longer live", nn=1, dflt="0")])
NODE_COL = col("ib_node", "subgroup_id", 20, "INTEGER",
               "the subgroup of the node's surface in its collection (collection_subgroup, #2503): set when the node is written and when the surface is placed (collection.subgroup), refreshed by Collection-Build.ps1 "
               "-Action NodeGroups; NULL while the surface is unplaced or isolated, or on a node with no collection. It is the collection's subgroup, never a cluster subgroup. It is how the claims process finds "
               "the observations of a group (#2505, researcher 2026-11-15: 'if the claim need to references a group it should be able to discover it')",
               fk="collection_subgroup.id", filled="the node writers (observationrecord, draftapply, engagement, layerreading), collectionindex.refresh_nodes")
UNIQUE = ["collection_id", "item", "subgroup_id", "subject"]
INDEXES = [("idx_collection_layer_item_collection_step", ["collection_id", "step"]), ("idx_collection_layer_item_observation", ["observation_id"])]
NODE_INDEX = ("idx_ib_node_subgroup", ["subgroup_id"])
ENUMS = {"ib_observation.stage": ["layer-1", "layer-2"],
         "ib_observation.tag": ["group", "enrichment", "pairing", "relation"],
         "collection_layer_item.state": ["open", "observed", "none", "retired"]}

LAYER = {
    "stages": {"1": "layer-1", "2": "layer-2"},
    "steps": [
        {"key": "1.1", "layer": 1, "name": "groups", "needs": ["lexical-gate"], "items": ["group-definition"]},
        {"key": "1.2", "layer": 1, "name": "strong-enrichment", "needs": ["1.1"], "items": ["strong-enrichment"]},
        {"key": "2.1", "layer": 2, "name": "pairings", "needs": ["1.2"], "items": ["pairing", "qualifier", "entity", "direction", "group-relation", "double-meaning"]},
    ],
    "items": {
        "group-definition": {"kind": "group", "none_allowed": False, "member_role": "characteristic",
                             "asks": "What do the surfaces of this group do for the inner being? Define the group by what it is or does; the observation says definitively that these words are part of the inner being's working."},
        "strong-enrichment": {"kind": "enrichment", "none_allowed": False, "member_role": "characteristic",
                              "asks": "What do the Strong's codes of this group say? Validate the grouping, give a short definition from them (for example what meditation means) and name the codes that link the group to its usage."},
        "pairing": {"kind": "pairing", "none_allowed": True, "member_role": "characteristic", "partner_role": "relational_target",
                    "asks": "Which words of the partner collection travel with this group, what do they do for or with it, and which of them stand out?"},
        "qualifier": {"kind": "qualification", "none_allowed": True, "member_role": "characteristic", "partner_role": "qualifier",
                      "asks": "What do the qualifiers of this group (negators, adjectives, adverbs) give it? Capture the significance of each qualifier."},
        "entity": {"kind": "party", "none_allowed": True, "route": True, "member_role": "characteristic", "partner_role": "relational_target",
                   "asks": "How many entities (divine, human) does this group meet, and do they differ from those of the other groups?"},
        "direction": {"kind": "relation", "none_allowed": True, "member_role": "characteristic", "partner_role": "relational_target",
                      "asks": "Does the direction of travel (from whom to whom) change across the verses of this group?"},
        "group-relation": {"kind": "relation", "none_allowed": True, "member_role": "characteristic",
                           "asks": "Is this group related to the other group, or are the two used interchangeably, in the verses they share?"},
        "double-meaning": {"kind": "face", "none_allowed": True, "member_role": "characteristic",
                           "asks": "Does this surface carry a double meaning in different scenarios (one Strong's code or sense here, another there)?"},
    },
    "thresholds": {"pair_min_verses": 3, "relation_min_verses": 3},
    "min_reason_chars": 10, "min_text_chars": 40, "pull_max_nodes": 80,
}
SETTINGS = [
    ("layer.reading", LAYER, "the layered reading of a collection (#2505): the stages of the two layers, the steps (1.1 groups, 1.2 Strong's enrichment, 2.1 pairings) with what each needs, the items each step "
     "demands with the kind of observation that answers it, whether none is allowed, the default node roles and, for a party item, that it carries a route; thresholds: pair_min_verses (a group and a partner "
     "collection that share at least this many verses demand a pairing observation) and relation_min_verses (two groups that share this many verses demand a relation); min_reason_chars, min_text_chars, "
     "pull_max_nodes (the nodes shown for each row of a working file). Read by lib/layerreading.py", "layer"),
    ("layer.working_dir", "_analytics/surfaces/working_files/layers", "the folder of the working files of the layered reading (LayerPull writes, LayerRecord reads), registered in folder_purpose (B:128)", "layer"),
    ("layer.check_name", "layer-check", "the file name stem of the report of LayerCheck: <stem>-v<n>-<yyyymmdd>.md under surfaces.exports_root, versioned by the filing rule", "layer"),
]
STEPS = [
    ("collection-build", 14, "collection.layer_open", "iba.app.handlers.collectionbuild:layer_open", "none",
     "open a step of the layered reading of a collection (-Collection, -Step 1.1|1.2|2.1): the lexical gate, the grouping finished, the previous step closed; then one ledger row for each aspect the data demands; -Check previews -- see lib/layerreading.py (escalation #2505)", "operations"),
    ("collection-build", 15, "collection.layer_pull", "iba.app.handlers.collectionbuild:layer_pull", "none",
     "write the working file of the open ledger rows of a step with the evidence to read (the occurrences, the codes, the partners) to layer.working_dir; read-only on the tables -- see lib/layerreading.py", "utility"),
    ("collection-build", 16, "collection.layer_record", "iba.app.handlers.collectionbuild:layer_record", "none",
     "check a filled working file whole and write its observations, their nodes (built from the data) and the ledger answers in one transaction; -Check previews; any problem refuses the file -- see lib/layerreading.py", "operations"),
    ("collection-build", 17, "collection.layer_check", "iba.app.handlers.collectionbuild:layer_check", "none",
     "validate every answered ledger row of a collection against the tables (stage, kind, nodes, roles, codes), set validated, and write the report (layer.check_name) naming what is open, failed or missing -- see lib/layerreading.py", "operations"),
    ("collection-build", 18, "collection.node_groups", "iba.app.handlers.collectionbuild:node_groups", "none",
     "set ib_node.subgroup_id of the live nodes from the collection index; -Check previews; every change kept with its reason in ib_observation_change -- see lib/collectionindex.py refresh_nodes", "operations"),
]
GRANTS = [("migration", T), ("collection.layer_open", T), ("collection.layer_record", T), ("collection.layer_record", "ib_observation"), ("collection.layer_record", "ib_node"),
          ("collection.layer_record", "ib_observation_change"), ("collection.layer_check", T), ("collection.node_groups", "ib_node"), ("collection.node_groups", "ib_observation_change"),
          ("collection.subgroup", "ib_node"), ("collection.subgroup", "ib_observation_change")]
ON_FAIL = [(s[2], "refused", "report-continue", None, "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)", "terminal", 0) for s in STEPS]
UTILITIES = [
    ("layerreading", "iba/app/lib/layerreading.py", 0,
     "layerreading.py -- the layered reading of a collection (escalation #2505): the gates, the ledger, the working file, the recorder, the checker and the group on the node.", 1,
     "the steps, items, kinds, stages and thresholds are read from cfg_setting layer.reading; the code holds no tunable value"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2505: the layered reading registered; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
METHOD = [
    ("collection.layer_open", "LR-01 a-step-opens-on-gates-and-derives-its-ledger",
     "A step of the layered reading opens only when the lexical gate passes (every member occurrence of the collection carries a lexical node with a role), the grouping is finished (every surface placed in a "
     "subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an "
     "aspect the data no longer demands is retired, a new one is added, and a second open changes nothing."),
    ("collection.layer_record", "LR-02 nodes-are-built-from-the-data",
     "The nodes of a layer observation are the occurrences the aspect demands (the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and "
     "the subgroup of each surface; they are never typed. The interpretation is the observation text, founded in what the evidence shows and stating what the words do for the inner being (basis stated or read, "
     "B:131). The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observation with the reason."),
    ("collection.layer_record", "LR-03 none-needs-a-permitted-reason",
     "An aspect is recorded as none only where its item allows it (cfg_setting layer.reading none_allowed) and with its reason in words. A group definition and a group's Strong's enrichment are always observed."),
    ("collection.layer_check", "LR-04 validated-is-set-only-by-the-check",
     "A ledger row is validated only by LayerCheck, which re-derives what the row demands from the tables: a live observation of the item's kind and the layer's stage, nodes equal to the demanded occurrences, "
     "each with a node role and a collection, and for an enrichment a node for every Strong's code of the group. A step is closed when every row is answered and validated and the data demands nothing more."),
    ("collection.node_groups", "LR-05 the-group-is-on-the-node",
     "A live node carries the subgroup its surface is placed in within the node's collection (ib_node.subgroup_id), so that the observations of a group are found through its nodes; it is set when the node is "
     "written and when the surface is placed, and the refresh and the index check name any node that disagrees with the index."),
]

RULES = [
    ("collection-reading-runs-in-layers",
     "A collection is read in layers, in order. A step is closed before the next opens: every aspect it demands is answered by an observation with its nodes (or, where the setting allows it, by a recorded "
     "none with its reason) and validated by the check. Layer 1 step 1: the surfaces of the collection are grouped by what each does for the inner being, a surface with no inner-being role is isolated with "
     "its reason, and each group is an observation whose nodes are the occurrences of its surfaces. Layer 1 step 2: each group's Strong's codes are studied, the grouping validated and a short definition "
     "given, and each enrichment is an observation whose nodes carry the group's codes. Layer 2 step 1: what the other words of the verse do for or with each group (the words that pair with it and those "
     "that stand out, whether groups are related or used interchangeably, what qualifiers give, how many entities and whether they differ between groups, whether the direction of travel changes, a double "
     "meaning in different scenarios), each an observation with its nodes. Layers 1 and 2 are inner-being work and it shows in every observation. Claude reads the evidence and decides; what reaches the "
     "researcher is a case the evidence could not settle, with that evidence, and the researcher scrutinises Claude's judgement. The last layer formulates the claims from these observations; layers 1 and 2 "
     "only prepare the base data. The steps, aspects, kinds, stages and thresholds are cfg_setting layer.reading; the routine is Collection-Build.ps1 LayerOpen, LayerPull, LayerRecord and LayerCheck.",
     "iba/app/lib/layerreading.py: a step does not open before its gates and the previous step are closed (open_step), the nodes are built from the data (record), validated is set only by check; the groups "
     "are placed with Collection-Build.ps1 -Action Subgroup (iba/app/lib/collectionindex.py)", "mechanically_enforced"),
    ("lexical-and-claims-readings-are-separate",
     "The lexical reading of a verse (what it says: its observations) and the layered reading of a collection (what the words do for the inner being) are separate processes and never run at the same "
     "time: a verse cannot be analysed lexically and have its inner-being implications determined in the same process, each needs its own observations. A collection's layer reading opens only when every "
     "occurrence of its member surfaces already carries a lexical node with a role; where not, the lexical observations are completed first. A lexical observation may let the border between a word's meaning "
     "in the verse and its meaning for the inner being blur: that is an enrichment, not a conflict.",
     "iba/app/lib/layerreading.py lexical_gate: LayerOpen refuses while a member occurrence has no lexical node with a role, and LayerCheck reports the gate", "mechanically_enforced"),
    ("layer-aspects-are-ledgered-and-never-left-open",
     "Every aspect a layer step demands is a row of the ledger collection_layer_item and is closed by an observation or a permitted none: nothing is dropped and nothing is left standing. A word found wrongly "
     "placed in a collection is moved by the collection change procedure of collections-are-built-on-surfaces-one-each and the move is processed, so that the step reopens and the completeness tests hold. "
     "A surface with no inner-being role is isolated in the index with its reason; it is bound to its partner or excluded, and is never analysed or described on its own.",
     "iba/app/lib/layerreading.py (the ledger, check) and iba/app/lib/collectionindex.py (isolation needs a reason: the grouping gate)", "mechanically_enforced"),
]
B119 = ("A word enters a scope through its surface (verse_lexical.surface) and the collection of that surface (its own link, else its base), never through word_strong and never through a cluster or "
        "subgroup of the cluster allocation.")
B119_ENF = "iba/app/lib/versescope.py Resolver.word (#2295) matches a word to verse_lexical.surface and its occurrences; word_strong is not read by the resolver. The layered reading takes its scope from the collection (iba/app/lib/layerreading.py)."
B120 = ("A work unit is a collection's verses (the verses holding an occurrence of one of its member surfaces) or a subset of them, and that collection is the home until all its verses have been read. The other "
        "collections a verse holds are read in that verse and never add verses to the scope. A word that only qualifies, or that has no inner-being role of its own, is not analysed or described by itself: it is "
        "bound to the characteristic it qualifies, or excluded; a word found wrongly placed in a collection is moved by the collection change procedure of collections-are-built-on-surfaces-one-each, and the "
        "move is processed.")
B120_ENF = "iba/app/lib/layerreading.py: every step is opened and checked for one collection; the other collections of a verse are partners and add no verses (expected_nodes)."


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", T):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": T, "grain": TABLE[0], "use": TABLE[1], "inactive": 0, "category": "data"}))
    for i, c in enumerate(UNIQUE):
        if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", T, c):
            ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": T, "col": c, "ordinal": i}))
    for name, cols in INDEXES:
        for i, c in enumerate(cols):
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", T, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": T, "name": name, "col": c, "ordinal": i}))
    if not has("SELECT 1 FROM cfg_index WHERE table_name='ib_node' AND name=? AND col=?", NODE_INDEX[0], NODE_INDEX[1][0]):
        ops.append(("cfg_index", "insert", {}, {"table_name": "ib_node", "name": NODE_INDEX[0], "col": NODE_INDEX[1][0], "ordinal": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    for c in COLS + [NODE_COL]:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", c["table_name"], c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for name, values in ENUMS.items():
        top = one("SELECT coalesce(max(ordinal),-1) FROM cfg_enum WHERE name=?", name)[0]
        for v in values:
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                top += 1
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": top, "inactive": 0}))
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value, ensure_ascii=False), "use": use, "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='layer'"):
        top = one("SELECT coalesce(max(ordinal),-1) FROM cfg_enum WHERE name='config_module'")[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "layer", "ordinal": top + 1, "inactive": 0}))
    for wp, ordinal, step, handler, scope, does, kind in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": wp, "ordinal": ordinal, "step": step, "handler": handler, "scope": scope, "does": does, "inactive": 0, "kind": kind}))
    for step, cond, path, resolver, message, route, inactive in ON_FAIL:
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path, "resolver": resolver, "message": message, "route": route, "inactive": inactive}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt, "config_exempt_reason": reason,
                                                      "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    for i, (step, key, text) in enumerate(METHOD):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", step, key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": step, "rule_key": key, "rule_text": text, "source_doc": SOURCE, "enforced_by": "iba/app/lib/layerreading.py", "ordinal": i, "active": 1}))
    # method rules restated, one retired
    m163 = one("SELECT rule_text FROM cfg_method_rule WHERE id=163")[0]
    old = "the occurrence, the subgroup, the cluster, the word's role"
    if old in m163:
        ops.append(("cfg_method_rule", "update", {"id": 163}, {"rule_text": m163.replace(old, "the occurrence, the collection and its subgroup, the word's role")}))
    m151 = one("SELECT rule_text FROM cfg_method_rule WHERE id=151")[0]
    old = "How the face differs from the word's other occurrences needs more than one verse and is claims work."
    if old in m151:
        ops.append(("cfg_method_rule", "update", {"id": 151}, {"rule_text": m151.replace(
            old, "Identifying and clarifying the face is lexical work; what the faces do for the inner being, and a double meaning in different scenarios, are layer 2 of the collection reading (layer-aspects-are-ledgered-and-never-left-open).")}))
    if one("SELECT active FROM cfg_method_rule WHERE id=201")[0]:
        ops.append(("cfg_method_rule", "update", {"id": 201}, {"active": 0}))
    # behaviour rules
    top = one("SELECT max(id) FROM cfg_behaviour_rule")[0]
    for key, text, enf, status in RULES:
        if not has("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", key):
            top += 1
            ops.append(("cfg_behaviour_rule", "insert", {}, {"id": top, "class": "study_method", "rule_key": key, "rule_text": text, "source": SOURCE, "enforced_by": enf, "added_at": _now(),
                                                              "active": 1, "enforcement_status": status, "deliver_when": "study_active"}))
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{top}", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    ops.append(("cfg_behaviour_rule", "update", {"id": 119}, {"rule_text": B119, "enforced_by": B119_ENF, "enforcement_status": "partially_enforced"})) if one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=119")[0] != B119 else None
    ops.append(("cfg_behaviour_rule", "update", {"id": 120}, {"rule_text": B120, "enforced_by": B120_ENF, "enforcement_status": "partially_enforced"})) if one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=120")[0] != B120 else None
    t127 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=127")[0]
    old = "The researcher does the interpretation and evaluation with Claude; Claude prepares and presents the aspects of the synergy and analysis in a form the researcher can digest"
    if old in t127:
        ops.append(("cfg_behaviour_rule", "update", {"id": 127}, {"rule_text": t127.replace(
            old, "Claude reads the evidence and decides in the majority of cases, the researcher scrutinises Claude's judgement and decides what the evidence cannot settle (collection-reading-runs-in-layers); "
                 "Claude prepares and presents the aspects of the synergy and analysis in a form the researcher can digest")}))
    t130 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=130")[0]
    new130 = t130.replace("collection_id, role, source_stage", "collection_id, subgroup_id, role, source_stage").replace(
        "Clusters and sub groups served to establish the collections and play no part in nodes and observations; cluster_code and cluster_subgroup_code are history.",
        "Clusters and cluster sub groups served to establish the collections and play no part in nodes and observations; cluster_code and cluster_subgroup_code are history. The subgroup_id of a node is the "
        "collection's own subgroup of its surface (collection_subgroup), set when the surface is placed, so that the observations of a group are found through the nodes.")
    if new130 != t130:
        ops.append(("cfg_behaviour_rule", "update", {"id": 130}, {"rule_text": new130}))
    return ops


def _now():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    node_cols = {r[1] for r in conn.execute("PRAGMA table_info(ib_node)")}
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); table to create: {T not in live}; ib_node.subgroup_id to add: {'subgroup_id' not in node_cols}")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", set_.get("name") or set_.get("module") or set_.get("step") or set_.get("key") or set_.get("rule_key") or set_.get("table_name") or "")
        return 0
    if not ops and T in live and "subgroup_id" in node_cols:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2505-layers', named=True)}")
    try:
        conn.execute("SAVEPOINT layers_2505")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if T not in live:
            create_sql, index_sql = table_ddl(cfg, T)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        if "subgroup_id" not in node_cols:
            conn.execute("ALTER TABLE ib_node ADD COLUMN subgroup_id INTEGER REFERENCES collection_subgroup(id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ib_node_subgroup ON ib_node(subgroup_id)")
        conn.execute("RELEASE layers_2505")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO layers_2505")
        conn.execute("RELEASE layers_2505")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); table created: {T not in live}; ib_node.subgroup_id added: {'subgroup_id' not in node_cols}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
