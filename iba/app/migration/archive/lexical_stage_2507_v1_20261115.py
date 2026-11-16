"""lexical_stage_2507_v1_20261115.py -- escalation #2507 (researcher, 2026-11-15: "I will approve for the build"; design
outputs/escalation/2507-lexical-observations-by-collection-alignment-and-design-v4-20261115.md; stages as the researcher defined them on #2507 v7).

Stage 1 of the collection reading, the lexical analysis of the words, is registered in the ledger machinery of #2505 and the wording of stage 3 is corrected:
  tables / columns   collection_layer_item.subgroup_id: 0 for a stage 1 aspect (it belongs to no group yet), no foreign key; the table is rebuilt from config (rows kept)
  enums              ib_observation.stage lexical; observation_role lexical
  settings           layer.reading (step S1 with items word-lexical and word-face; step 1.1 needs S1; the items of steps 1.2 and 2.1 worded as verse-lexical only);
                     reading.node_roles (group lexical); governance.programme_stages
  steps              collection.layer_open text
  rules              behaviour rules 130, 132, 133 restated; B:113 and B:121 also delivered at Collection-Build.ps1; method rules LR-01, LR-02, LR-04 restated, LX-01 added
  column texts       wa_obs_question_catalogue.scope and dimension corrected; ib_observation.stage, ib_node.role, collection_layer_item columns
  utilities          this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/lexical_stage_2507_v1_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2507-LEXICAL-STAGE-20261115"
MODULE = "lexical_stage_2507_v1_20261115"
SOURCE = "escalation #2507 (researcher, 2026-11-15; outputs/escalation/2507-lexical-observations-by-collection-alignment-and-design-v4-20261115.md; the stages on #2507 v7)"
T = "collection_layer_item"
MSRC = "strong_meaning_tree; strong_lexicon.lsj; strong_lexicon.mounce"
WORD_PROMPTS = ["M0.1.1", "M0.1.2", "M0.1.3", "M0.4.1", "M0.5.1", "M0.5.2", "M0.5.3", "M0.5.4", "M0.5.5", "M0.5.6", "M0.5.7", "M0.5.8", "M0.5.9"]

NEW_ITEMS = {
    "word-lexical": {"kind": "term", "none_allowed": False, "member_role": "lexical", "window": "meaning", "meaning_source": MSRC, "prompts": WORD_PROMPTS,
                     "asks": "What is this word, by its lettered Strong's code, in the verses of this collection? Read the three lexicon sources together and the occurrences: its root meaning and "
                             "range, grammatical form and aspect, related terms, Testament context and coinage, and an idiom or combined span where the unit shows one. State what the lexicon and the "
                             "verses show; never what the word does for the inner being (stage 4). A prompt that does not apply is not answered."},
    "word-face": {"kind": "face", "none_allowed": True, "subset": True, "member_role": "lexical", "window": "meaning", "meaning_source": MSRC, "prompts": ["M0.5.11", "M0.1.1"],
                  "asks": "Where does the meaning of this word in an occurrence depart from its usual sense in the others? Name those occurrences (fill.occurrences: occurrence ids or verse "
                          "references) and the nuance, from the verse and the lexicon. None, with the reason, where no occurrence departs."},
}
REWORD_ASKS = {
    "strong-enrichment": "What do the Strong's codes of this group say? Validate the grouping against them, give a short definition from the lexicon entries (for example what meditation means) and "
                         "name the codes that link the group to its usage. State what the lexicon entries show.",
    "pairing": "Which words of the partner collection travel with this group in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? "
               "State the structure the data shows; what the pairing does for the inner being is stage 4.",
    "qualifier": "Which qualifiers (negators and the words they reach, adjectives, adverbs, prepositional qualifiers) stand with this group, and what does each give it by the grammar? "
                 "Adjacency is not scope: state the word the negator or qualifier reaches. Capture the significance of each qualifier as the text shows it.",
    "entity": "Which entities (divine, human, other) are named or referred to, by name or pronoun, in the verses of this group, and do they differ from those of the other groups? State who is "
              "named and how the text refers to them; what they do for the inner being is stage 4.",
    "direction": "Does the direction of travel the text states (from whom to whom, by the grammar) change across the verses of this group?",
    "group-relation": "Do this group and the other group stand together in the verses they share, interchangeably or in sequence, as the text shows?",
    "double-meaning": "Does this surface carry a different Strong's code or sense in different verses (the faces of the word)? State the codes and the verses; what each does for the inner being is stage 4.",
}

B130_OLD = "standalone records that the word was recognised and has no inner-being role on any other surface of the verse."
B130_NEW = ("standalone records that the word was recognised and has no inner-being role on any other surface of the verse; lexical (a node of a stage 1 observation) records that the word was read "
            "lexically and that its inner-being role has not been assessed.")
B132 = ("A collection is read in stages and steps, in order, as the researcher defined them (2026-11-15, #2507 v7). Stage 1, the lexical analysis (step S1): every word of the collection, by surface "
        "and lettered Strong's code, is read lexically from the lexicon and its occurrences, each an observation whose nodes are its occurrences, and the occurrences where a word's meaning departs "
        "from its usual sense are face observations; the relations between the words are base data and are not analysed here. Stage 2 is the grouping of the surfaces (the four groups, the "
        "collections of groups 1 and 2, and the subgroups within a collection: Collection-Build.ps1 -Action Subgroup); step 1.1 records each group as an observation and isolates a surface with no "
        "inner-being role with its reason. Stage 3, verse-lexical only (steps 1.2 and 2.1): each group's Strong's codes are studied and the grouping validated; then what the other words of the verse "
        "show with each group (pairings, qualifiers and the words they reach, entities, direction, the relation between groups, a double meaning), each an observation with its nodes. Stage 4, the "
        "inner-being analysis made from the stage 3 observations, is not yet built; stage 5, the claim formulation, is not yet decided. A step is closed before the next opens: every aspect it "
        "demands is answered by an observation with its nodes (or, where the setting allows it, by a recorded none with its reason) and validated by the check. Claude reads the evidence and decides; "
        "what reaches the researcher is a case the evidence could not settle, with that evidence, and the researcher scrutinises Claude's judgement. The steps, aspects, kinds, stages and thresholds "
        "are cfg_setting layer.reading; the routine is Collection-Build.ps1 LayerOpen, LayerPull, LayerRecord and LayerCheck. The layers 1 and 2 named in the steps are the collection reading's; "
        "they are not the Layer 1 and Layer 2 of the verse_lexical build (Window 1).")
B132_ENF = ("iba/app/lib/layerreading.py: a step does not open before the previous step is closed and, after S1, the grouping is finished (open_step); step 1.1 needs S1; the nodes are built from "
            "the data (record); validated is set only by check; the groups are placed with Collection-Build.ps1 -Action Subgroup (iba/app/lib/collectionindex.py)")
B133 = ("The lexical analysis of a verse (what its words and their structure show) and the inner-being analysis (what the words do for the inner being) are separate processes and never run at the "
        "same time: a verse cannot be analysed lexically and have its inner-being implications determined in the same process, each needs its own observations (researcher, #2463 v20). Step 1.1 of "
        "a collection opens only when stage 1 is closed for it (step S1: every word answered and validated); where not, the lexical analysis is completed first. A lexical observation may let the "
        "border between a word's meaning in the verse and its meaning for the inner being blur: that is an enrichment, not a conflict.")
B133_ENF = "iba/app/lib/layerreading.py open_step: step 1.1 needs S1 closed (a ledger step closed only by LayerCheck); LayerCheck reports stage 1"
PROGRAMME = ("The research programme has three main stages: Base_data (STEP, the spine and verse_lexical, Window 1 Layer 1); Analysis (deriving understanding of the inner being: the lexical analysis of "
             "the words by collection, Window 1 Layer 2 and stage 1 of the collection reading; the grouping of the surfaces, stage 2; the verse-lexical observations, stage 3; the inner-being analysis, "
             "stage 4; the claim formulation, stage 5, not yet decided); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), "
             "Session C (publishing) -- methodologies and processes have changed materially over time across all three.")
LR01 = ("A step of the layered reading opens only when the previous step is closed and, for the steps after S1, the grouping is finished (every surface placed in a subgroup or isolated with its "
        "reason, every subgroup holding a surface). Step 1.1 needs step S1 closed: every word of the collection (surface and lettered Strong's code) answered and validated. Opening derives one ledger "
        "row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.")
LR02 = ("The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the "
        "recorder with the collection and the subgroup of each surface; they are never typed (an item that names a subset, word-face, names its occurrences and the recorder checks them against the "
        "data). The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131): the lexical items (S1, 1.2, 2.1) state what the lexicon, the verses and "
        "the stored structure show and never what a word does for the inner being; only the group definition of step 1.1, the researcher's grouping, states what the group is or does for the inner "
        "being. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observation with the reason.")
LR04 = ("A ledger row is validated only by LayerCheck, which re-derives what the row demands from the tables: a live observation of the item's kind and the step's stage, nodes equal to the demanded "
        "occurrences (for a subset item, some of them and at least one), each with a node role and a collection, and for an enrichment a node for every Strong's code of the group. A step is "
        "closed when every row is answered and validated and the data demands nothing more.")
LX01 = ("The rules RG-08 (the original word), RG-09 (the face), RG-14 (morph read), RG-16 (homonym and data error), RG-21 (grain), RW-04 and RW-05 (concise, span-grounded) apply to the lexical items "
        "as they do to the reading and are not restated here. Adjacency is not scope (#2463 v28): a negator or qualifier beside a word reaches the word it governs, which the observation states and "
        "never assumes.")
CLEAR = {
    "scope": (" CORRECTED 2026-11-15 (#2507): this bucket does not mark lexical work in the researcher's sense: of the 26 questions of Word/term (lexical) only the 14 questions M0.1, M0.4 and "
              "M0.5 are lexical; the 12 questions D5, D7 and X0 ask about the inner being. The questions that guide the lexical items are listed by item in cfg_setting layer.reading (items prompts)."),
    "dimension": (" CORRECTED 2026-11-15 (#2507): M0 is not only lexical evidence: it holds lexical questions (M0.1, M0.4, M0.5), structural ones (M0.6.1, M0.6.5, M0.6.6), inner-being ones (M0.7, "
                  "M0.8.1) and characteristic ones (M0.2, M0.3)."),
}


def _now():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731

    def update_col(table, name, **sets):
        cur = one("SELECT * FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", table, name)
        if cur is None:
            raise SystemExit(f"cfg_column {table}.{name} is missing")
        return [("cfg_column", "update", {"database": "iba", "table_name": table, "name": name}, sets)]

    # enums
    for name, value in (("ib_observation.stage", "lexical"), ("observation_role", "lexical")):
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            top = one("SELECT coalesce(max(ordinal),-1) FROM cfg_enum WHERE name=?", name)[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": top + 1, "inactive": 0}))
    # reading.node_roles: group lexical
    nr = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.node_roles' AND inactive=0")[0])
    if "lexical" not in nr:
        nr["lexical"] = ["lexical"]
        ops.append(("cfg_setting", "update", {"key": "reading.node_roles"}, {"value": json.dumps(nr, ensure_ascii=False)}))
    # layer.reading
    lay = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading' AND inactive=0")[0])
    new = json.loads(json.dumps(lay))
    new["stages"]["0"] = "lexical"
    if not any(s["key"] == "S1" for s in new["steps"]):
        new["steps"].insert(0, {"key": "S1", "layer": 0, "name": "words", "needs": [], "items": ["word-lexical", "word-face"]})
    for s in new["steps"]:
        if s["key"] == "1.1":
            s["needs"] = ["S1"]
    new["items"].update(NEW_ITEMS)
    for k, v in REWORD_ASKS.items():
        new["items"][k]["asks"] = v
    if new != lay:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    # programme stages
    if one("SELECT value FROM cfg_setting WHERE key='governance.programme_stages' AND inactive=0")[0] != json.dumps(PROGRAMME, ensure_ascii=False):
        ops.append(("cfg_setting", "update", {"key": "governance.programme_stages"}, {"value": json.dumps(PROGRAMME, ensure_ascii=False)}))
    # step text
    r = one("SELECT does FROM cfg_step WHERE step='collection.layer_open'")[0]
    old = "(-Collection, -Step 1.1|1.2|2.1): the lexical gate, the grouping finished, the previous step closed;"
    if old in r:
        ops.append(("cfg_step", "update", {"step": "collection.layer_open"}, {"does": r.replace(old, "(-Collection, -Step S1|1.1|1.2|2.1): the previous step closed (1.1 needs the lexical analysis S1) and, after S1, the grouping finished;")}))
    # behaviour rules
    t130 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=130")[0]
    if B130_OLD in t130 and "lexical (a node of a stage 1" not in t130:
        ops.append(("cfg_behaviour_rule", "update", {"id": 130}, {"rule_text": t130.replace(B130_OLD, B130_NEW)}))
    for rid, text, enf in ((132, B132, B132_ENF), (133, B133, B133_ENF)):
        if one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=?", rid)[0] != text:
            ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"rule_text": text, "enforced_by": enf}))
    for ref in ("B:113", "B:121"):
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value='Collection-Build.ps1' AND inactive=0", ref):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": ref, "scope_kind": "ps", "scope_value": "Collection-Build.ps1", "inactive": 0}))
    # method rules
    for rid, text in ((237, LR01), (238, LR02), (240, LR04)):
        if one("SELECT rule_text FROM cfg_method_rule WHERE id=?", rid)[0] != text:
            ops.append(("cfg_method_rule", "update", {"id": rid}, {"rule_text": text}))
    if not has("SELECT 1 FROM cfg_method_rule WHERE step='collection.layer_record' AND rule_key LIKE 'LX-01%'"):
        nid = one("SELECT max(id) FROM cfg_method_rule")[0] + 1
        ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "collection.layer_record", "rule_key": "LX-01 the-lexical-items-follow-the-word-rules", "rule_text": LX01,
                                                       "source_doc": SOURCE, "enforced_by": "iba/app/lib/layerreading.py (the items in cfg_setting layer.reading)", "ordinal": 5, "active": 1}))
    # column texts
    for name, add in CLEAR.items():
        cur = one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='wa_obs_question_catalogue' AND name=?", name)[0]
        if "CORRECTED 2026-11-15 (#2507)" not in cur:
            ops += update_col("wa_obs_question_catalogue", name, use=cur + add)
    cur = one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name='stage'")[0]
    if "lexical (the lexical analysis" not in cur:
        ops += update_col("ib_observation", "stage", use=cur.replace("engagement (what a surface does", "lexical (the lexical analysis of the words by collection, stage 1 of the collection reading, "
                          "written by Collection-Build.ps1 LayerRecord, #2507); layer-1 and layer-2 (the steps of stages 2 and 3, #2505); engagement (what a surface does"))
    cur = one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='ib_node' AND name='role'")[0]
    if "lexical records" not in cur and "lexical (" not in cur:
        ops += update_col("ib_node", "role", use=cur.replace("on any other surface of the verse.", "on any other surface of the verse; lexical (a node of a stage 1 observation) records that the word was read lexically and its inner-being "
                          "role has not been assessed."))
    sub = one("SELECT fk, use FROM cfg_column WHERE database='iba' AND table_name=? AND name='subgroup_id'", T)
    if sub[0]:
        ops += update_col(T, "subgroup_id", fk=None, use="the group the aspect is about (for a relation between two groups, the one with the lower id); 0 for an aspect of stage 1 (a word), which belongs to no group yet")
    for name, text in (("step", "the step of the layered reading that demands it (layer.reading steps): S1 (stage 1, the words), 1.1, 1.2 or 2.1"),
                       ("item", "the kind of aspect (layer.reading items): word-lexical, word-face, group-definition, strong-enrichment, pairing, qualifier, entity, direction, group-relation, double-meaning"),
                       ("subject", "what distinguishes the aspect within a group: the word of a stage 1 aspect (surface|lettered Strong's code), the partner collection of a pairing, the other group of a relation (its id), the surface of a double meaning; empty otherwise")):
        if one("SELECT use FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", T, name)[0] != text:
            ops += update_col(T, name, use=text)
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2507: the lexical analysis (stage 1) registered; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def rebuild(cfg, conn):
    """Rebuild collection_layer_item from config (no foreign key on subgroup_id), keeping its rows."""
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({T})")]
    create_sql, _ = table_ddl(cfg, T, name=f"{T}__new")
    conn.execute(create_sql)
    conn.execute(f"INSERT INTO {T}__new ({', '.join(cols)}) SELECT {', '.join(cols)} FROM {T}")
    conn.execute(f"DROP TABLE {T}")
    conn.execute(f'ALTER TABLE "{T}__new" RENAME TO "{T}"')
    _, index_sql = table_ddl(cfg, T)
    for sql in index_sql:
        conn.execute(sql)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    has_fk = bool(conn.execute(f"PRAGMA foreign_key_list({T})").fetchall() and any(r[3] == "subgroup_id" for r in conn.execute(f"PRAGMA foreign_key_list({T})")))
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); table rebuild (foreign key on subgroup_id present): {has_fk}")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", list(set_)[:3])
        return 0
    if not ops and not has_fk:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-lexical', named=True)}")
    try:
        conn.execute("SAVEPOINT lexical_2507")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if has_fk:
            rebuild(cfg, conn)
        conn.execute("RELEASE lexical_2507")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO lexical_2507")
        conn.execute("RELEASE lexical_2507")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); table rebuilt: {has_fk}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
