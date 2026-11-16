"""stage_boundary_and_grouping_2509_v7_20261115.py -- escalation #2509 (design v2, approved 2026-11-15) and the boundary of the stages (researcher, same day: "you did not respect the boundaries between
lexical work and inner being work in stages").

The researcher's ruling: the surface groups are about the meaning of the surface words, judged from the dictionary meaning; nothing in stages 1 to 3 judges what a word does for the inner being.
What this migration corrects and adds:
  layer.reading   every item of steps 1.1, 1.2 and 2.1 had the inner-being roles characteristic, relational_target or qualifier on its nodes, the entity item the kind party with an inner-being route and
                  the qualifier item the kind qualification; they now take the node role lexical, the kinds group, enrichment, pairing, relation and face, no route, and an `asks` about the dictionary meaning, the
                  lexicon, the stored structure; group-definition and strong-enrichment ground a read observation in the lexicon (`grounds_in`)
  rules           B:132, B:134, LR-02 restated; method rules GP-01 to GP-04 for the grouping
  texts           cfg_step collection.subgroup; cfg_table collection_subgroup and collection_subgroup_surface; cfg_column state, reason, name and note of those tables
  settings        group.reading (the file's limits and its asks), group.report_name
  steps           collection.group_pull, collection.group_record, their write grants and routed condition
  utilities       lib/collectiongroup.py and this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage: python iba/app/migration/stage_boundary_and_grouping_2509_v7_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2509-GROUPING-BOUNDARY-20261115"
MODULE = "stage_boundary_and_grouping_2509_v7_20261115"
SOURCE = "escalation #2509 (researcher, 2026-11-15: ruling and approval of v2; outputs/escalation/2509-surface-grouping-method-design-v2-20261115.md)"

ITEMS = {
    "group-definition": {"kind": "group", "none_allowed": False, "member_role": "lexical", "grounds_in": "lexicon",
                         "asks": "What do the surfaces of this group mean, as the dictionary gives their meaning? State the one meaning, or the one kind of meaning, they share, in words the Strong's meaning "
                                 "of their codes supports; the group is named for it."},
    "strong-enrichment": {"kind": "enrichment", "none_allowed": False, "member_role": "lexical", "grounds_in": "lexicon",
                          "asks": "What do the Strong's codes of this group say? Validate the grouping against them, give a short definition from the lexicon entries (for example what meditation means) and name "
                                  "the codes that link the group to its usage. State what the lexicon entries show."},
    "pairing": {"kind": "pairing", "none_allowed": True, "member_role": "lexical", "partner_role": "lexical",
                "asks": "Which words of the partner collection stand with this group in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? "
                        "State the structure the data shows."},
    "qualifier": {"kind": "pairing", "none_allowed": True, "member_role": "lexical", "partner_role": "lexical",
                  "asks": "Which qualifiers (negators and the words they reach, adjectives, adverbs, prepositional qualifiers) stand with this group, and what does each give it by the grammar? Adjacency is not "
                          "scope: state the word the negator or qualifier reaches."},
    "entity": {"kind": "pairing", "none_allowed": True, "member_role": "lexical", "partner_role": "lexical",
               "asks": "Which entities (divine, human, other) are named or referred to, by name or pronoun, in the verses of this group, and do they differ from those of the other groups? State who is named "
                       "and how the text refers to them."},
    "direction": {"kind": "relation", "none_allowed": True, "member_role": "lexical", "partner_role": "lexical",
                  "asks": "Does the direction of travel the text states (from whom to whom, by the grammar) change across the verses of this group?"},
    "group-relation": {"kind": "relation", "none_allowed": True, "member_role": "lexical",
                       "asks": "Do this group and the other group stand together in the verses they share, interchangeably or in sequence, as the text shows?"},
    "double-meaning": {"kind": "face", "none_allowed": True, "member_role": "lexical",
                       "asks": "Does this surface carry a different Strong's code or sense in different verses (the faces of the word)? State the codes and the verses."},
}
GROUP_SETTING = {"min_text_chars": 40, "min_reason_chars": 10, "evidence_chars": 500,
                 "asks": "Judge each surface from the dictionary meaning of its codes: put it in the group of the meaning it shares with the others (name the group for that meaning and define it), or set it aside with "
                         "the reason where its meaning is not the one this collection gathers; a surface whose codes mean different things is answered by code. Mark a placement the dictionary leaves open as uncertain "
                         "and say what is unsettled. Nothing here judges what a word does for the inner being."}
STEPS = [
    ("collection-build", 19, "collection.group_pull", "iba.app.handlers.collectionbuild:group_pull", "none",
     "write the working file for the grouping of the surfaces of a collection by their dictionary meaning (-Collection): one row for each row of the index with the Strong's meaning of its codes; read-only on the tables "
     "-- see lib/collectiongroup.py (escalation #2509)", "utility"),
    ("collection-build", 20, "collection.group_record", "iba.app.handlers.collectionbuild:group_record", "none",
     "check a filled grouping file whole and write the groups and placements in one transaction (-File; -Check previews); a surface whose meaning is not the collection's is set aside with its reason; writes the scrutiny "
     "report -- see lib/collectiongroup.py (escalation #2509)", "utility"),
]
GRANTS = [("migration", "collection_subgroup"), ("collection.group_record", "collection_subgroup"), ("collection.group_record", "collection_subgroup_surface"), ("collection.group_record", "surface_event"),
          ("collection.group_record", "ib_node"), ("collection.group_record", "ib_observation_change")]
METHOD = [
    ("GP-01 meaning-from-the-dictionary",
     "The surfaces of a collection are grouped by their meaning, judged from the dictionary meaning of the words: the Strong's meaning of each of their codes (strong_sense, strong_meaning_tree, the lexicons). "
     "A verse is read only where the dictionary leaves two groups open. Nothing in the grouping judges what a word does for the inner being (researcher, #2509, 2026-11-15)."),
    ("GP-02 whole-file-in-one-transaction",
     "A grouping file is checked whole and written in one transaction, or refused: every row of the index answered once, every group named once with the meaning it holds and holding a surface, a surface set aside "
     "with its reason, a surface answered by code with every one of its codes answered. Each change is a surface_event with its reason."),
    ("GP-03 set-aside-by-meaning",
     "A surface or a code whose dictionary meaning is not the meaning the collection gathers (a preposition, a different sense of the same spelling) is set aside in the index (state isolated) with the reason and is not "
     "grouped; a surface whose codes mean different things is split by code. A word that is a function word in every occurrence needs no placement (RG-22)."),
    ("GP-04 uncertain-and-the-researchers-correction",
     "A placement the dictionary leaves open between two groups is marked uncertain with what is unsettled and listed in the scrutiny report. The researcher's Subgroup instruction corrects a placement and wins over "
     "Claude's."),
]
B132_OLD = ("Stage 2 is the grouping of the surfaces (the four groups, the "
            "collections of groups 1 and 2, and the subgroups within a collection: Collection-Build.ps1 -Action Subgroup); step 1.1 records each group as an observation and isolates a surface with no "
            "inner-being role with its reason.")
B132_NEW = ("Stage 2 is the grouping of the surfaces (the four surface groups, the collections of groups 1 and 2, and the subgroups within a collection): the surfaces of a collection are grouped by their meaning, "
            "judged from the dictionary meaning of the words (the Strong's meaning), a subgroup being the surfaces that mean the same or the same kind of thing, named for that meaning; a surface whose meaning is not "
            "the one the collection gathers is set aside with its reason; nothing in the grouping judges what a word does for the inner being (Collection-Build.ps1 GroupPull and GroupRecord; Subgroup for the "
            "researcher's corrections); step 1.1 records each group as an observation of the meaning its surfaces share.")
B132_END = ("Every observation of stages 1 to 3 states what the dictionary, the verses and the stored structure show; none states what a word does for the inner being and none carries an inner-being role or route.")
B134_OLD = "A surface with no inner-being role is isolated in the index with its reason; it is bound to its partner or excluded, and is never analysed or described on its own."
B134_NEW = "A surface whose meaning is not the one its collection gathers is set aside in the index (state isolated) with its reason and is not grouped."
LR02_OLD = ("the lexical items (S1, 1.2, 2.1) state what the verses, the lexicon and the stored structure show of a word in its verses and never what a word does for the inner being; only the group definition of "
            "step 1.1, the researcher's grouping, states what the group is or does for the inner being.")
LR02_NEW = ("the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role "
            "lexical and no route.")
SUBGROUP_DOES = ("make a subgroup of a collection (-Collection, -Name, -Reason), place surfaces in it (-Surface, -Name, -Strong, -Reason) or set aside surfaces whose meaning is not the collection's (-Surface, -Isolate, "
                 "-Reason), as the researcher's correction of the grouping by meaning (GroupPull and GroupRecord make it), each with a surface_event; -Check previews -- see lib/collectionindex.py (escalation #2503, #2509)")
TABLE_SUBGROUP = ("#2503, #2509: a subgroup of the surfaces of one collection: the surfaces that mean the same or the same kind of thing (for example starting, weighing, meditation in the collection thought), judged from "
                  "the dictionary meaning of the words (lib/collectiongroup.py; the researcher corrects with Subgroup). Its definition, the meaning its surfaces share, is the column note and the observation of step 1.1; "
                  "the Strong's enrichment of it is a layer observation found through its nodes. A subgroup belongs to one collection and is not a cluster subgroup (cluster_subgroup and surface_subgroup are the "
                  "retired cluster allocation and are not read or changed by it). A change is a soft delete and a new row, and a surface_event")
TABLE_INDEX_OLD = "isolated (no inner-being role: bound to its partner or excluded)"
TABLE_INDEX_NEW = "isolated (set aside: its meaning is not the one the collection gathers)"
TABLE_INDEX_PLACE_OLD = "a placement is the researcher's instruction with a reason"
TABLE_INDEX_PLACE_NEW = "a placement is a judgement of the dictionary meaning (GroupRecord) or the researcher's correction (Subgroup), each with a reason"


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    lay = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading' AND inactive=0")[0])
    new = json.loads(json.dumps(lay))
    for k, v in ITEMS.items():
        new["items"][k] = v
    if new != lay:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    for key, value, use in (("group.reading", GROUP_SETTING, "the grouping of the surfaces of a collection by their dictionary meaning (#2509): the limits of a grouping file (min_text_chars of a group's definition, "
                                                               "min_reason_chars of a reason) and the instruction the working file carries (asks), evidence_chars the length of the lexicon text shown for a code. "
                                                               "Read by lib/collectiongroup.py"),
                            ("group.report_name", "collection-groups", "the file name stem of the scrutiny report of a grouping: <stem>-<collection>-v<n>-<yyyymmdd>.md under surfaces.exports_root, versioned by the "
                                                                       "filing rule (Collection-Build.ps1 GroupRecord)")):
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value, ensure_ascii=False), "use": use, "module": "layer", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='alignment.inner_being_kinds'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "alignment.inner_being_kinds", "value": json.dumps(["party", "qualification", "statement", "silence", "use"]),
                                                   "use": "the observation kinds that state what a word does for the inner being (reading.observation_parts): no item of the lexical stages 1 to 3 is written as one (the boundary check of "
                                                          "lib/lexicalalignment.py, #2509)", "module": "lexical", "inactive": 0}))
    for wp, ordinal, step, handler, scope, does, kind in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": wp, "ordinal": ordinal, "step": step, "handler": handler, "scope": scope, "does": does, "inactive": 0, "kind": kind}))
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None,
                                                       "message": "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)", "route": "terminal", "inactive": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    for i, (key, text) in enumerate(METHOD):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step='collection.group_record' AND rule_key=?", key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "collection.group_record", "rule_key": key, "rule_text": text, "source_doc": SOURCE,
                                                           "enforced_by": "iba/app/lib/collectiongroup.py", "ordinal": i, "active": 1}))
    t132 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=132")[0]
    n132 = t132
    if B132_OLD in n132:
        n132 = n132.replace(B132_OLD, B132_NEW)
    if B132_END not in n132:
        n132 = n132.replace("The steps, aspects, kinds, stages and thresholds are cfg_setting layer.reading;", B132_END + " The steps, aspects, kinds, stages and thresholds are cfg_setting layer.reading;", 1)
    if n132 != t132:
        ops.append(("cfg_behaviour_rule", "update", {"id": 132}, {"rule_text": n132}))
    t134 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=134")[0]
    if B134_OLD in t134:
        ops.append(("cfg_behaviour_rule", "update", {"id": 134}, {"rule_text": t134.replace(B134_OLD, B134_NEW)}))
    t238 = one("SELECT rule_text FROM cfg_method_rule WHERE id=238")[0]
    if LR02_OLD in t238:
        ops.append(("cfg_method_rule", "update", {"id": 238}, {"rule_text": t238.replace(LR02_OLD, LR02_NEW)}))
    if one("SELECT does FROM cfg_step WHERE step='collection.subgroup'")[0] != SUBGROUP_DOES:
        ops.append(("cfg_step", "update", {"step": "collection.subgroup"}, {"does": SUBGROUP_DOES}))
    if one("SELECT use FROM cfg_table WHERE database='iba' AND name='collection_subgroup'")[0] != TABLE_SUBGROUP:
        ops.append(("cfg_table", "update", {"database": "iba", "name": "collection_subgroup"}, {"use": TABLE_SUBGROUP}))
    tu = one("SELECT use FROM cfg_table WHERE database='iba' AND name='collection_subgroup_surface'")[0]
    nu = tu.replace(TABLE_INDEX_OLD, TABLE_INDEX_NEW).replace(TABLE_INDEX_PLACE_OLD, TABLE_INDEX_PLACE_NEW)
    if nu != tu:
        ops.append(("cfg_table", "update", {"database": "iba", "name": "collection_subgroup_surface"}, {"use": nu}))
    for table, col, old, new_ in (("collection_subgroup_surface", "state", "isolated (no inner-being role: bound to its partner or excluded)", "isolated (set aside: its meaning is not the one the collection gathers)"),
                                  ("collection_subgroup_surface", "reason", "else the researcher's instruction, quoted, with the escalation id", "else the judgement of the dictionary meaning (GroupRecord, with the file) or the researcher's correction, quoted, with the escalation id"),
                                  ("collection_subgroup", "name", "what the subgroup is (for example starting, weighing, meditation)", "the meaning the subgroup holds (for example starting, weighing, meditation)"),
                                  ("collection_subgroup", "note", None, None)):
        cur = one("SELECT use FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", table, col)
        if cur is None:
            continue
        if old and old in (cur[0] or ""):
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": table, "name": col}, {"use": cur[0].replace(old, new_)}))
        elif col == "note" and "the meaning its surfaces share" not in (cur[0] or ""):
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": table, "name": col},
                        {"use": "the meaning the subgroup's surfaces share, in words the dictionary supports (with the file and run that judged it): its definition (#2509); for a subgroup made by the researcher's instruction, the instruction quoted"}))
    for module, path, inactive, purpose, exempt, reason in (
            ("collectiongroup", "iba/app/lib/collectiongroup.py", 0, "collectiongroup.py -- the grouping of the surfaces of a collection by their dictionary meaning (escalation #2509): the working file with the Strong's meaning of each code and the whole-file recorder.", 1,
             "the file's limits and instruction are cfg_setting group.reading; the code holds no tunable value"),
            (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2509: the grouping by meaning and the boundary of the stages; run_id {RUN_ID}.", 1,
             "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")):
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt, "config_exempt_reason": reason,
                                                       "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", set_.get("step") or set_.get("rule_key") or "")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2509-grouping', named=True)}")
    try:
        conn.execute("SAVEPOINT grouping_2509")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE grouping_2509")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO grouping_2509")
        conn.execute("RELEASE grouping_2509")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
