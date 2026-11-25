"""findings_2538_v1_20261125.py -- escalation #2538 (researcher, 2026-11-24 and 2026-11-25; specification outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md).

Step 2.1 is answered by findings. The researcher, 2026-11-25: "the same surface for multiple verses = multiple nodes, not multiple observations. the same applies to B3". And 2026-11-24: "each subgroup surface will have
its own observation, when it gets to 3.2 then these observations are pulled together". So, in cfg_setting layer.reading:
  - the items pairing, qualifier, entity, direction and double-meaning are answered by a list of findings (multi): each finding is one observation holding the occurrences (verses) it holds in as nodes;
  - those items name the verses they are tied to (tie_to_verse);
  - the item group-relation (one observation that joins two subgroups) is removed from step 2.1 and from the items, and thresholds.relation_min_verses with it (a minimum number of shared verses was never the researcher's);
  - the LEDGER is a record of processing kept current at every event (researcher 2026-11-25): three stamps on collection_layer_item (pulled_at, answered_at, checked_at; each registered in cfg_column) and the
    ledger item old-observation, one row for each old observation in scope from the first step of the loop to its fate (answered, carried to a later step, deleted, marked);
  - thresholds.pair_min_verses is removed (step 3.3 asks for a row for any shared verse), pull_verse_texts is removed (3.1 is given every verse), and partner_complete [] is added (the partners the researcher declares complete).
Config only; the code is lib/layerreading.py (derive, expected_nodes, pull, record). All writes through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/archive/findings_2538_v1_20261125.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-FINDINGS-20261125"
MODULE = "findings_2538_v1_20261125"

ASKS = {
    "pairing": "Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? "
               "The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.",
    "qualifier": "Which qualifiers (negators and the words they reach, adjectives, adverbs, prepositional qualifiers) stand with the subgroup's surfaces, and what does each give by the grammar? "
                 "Adjacency is not scope: state the word the negator or qualifier reaches. One finding for each distinct thing shown; it holds the verses it holds in as its nodes.",
    "entity": "Which entities (divine, human, other) are named or referred to, by name or pronoun, in the verses of the subgroup, and how does the text refer to them? One finding for each distinct thing shown; "
              "it holds the verses it holds in as its nodes.",
    "direction": "Does the direction of travel the text states (from whom to whom, by the grammar) change across the verses of the subgroup? One finding for each distinct direction; it holds the verses it holds in as its nodes.",
}
MULTI_ITEMS = ("pairing", "qualifier", "entity", "direction", "double-meaning")
SOURCE = "escalation #2538 (researcher, 2026-11-25; outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md section 1A)"
STAMPS = {
    "pulled_at": "the time the row was last taken into a working file (LayerPull): the ledger is stamped as the work happens, not at the end",
    "answered_at": "the time the row was last answered by an observation or a recorded none (LayerRecord), or an old observation's fate was recorded; empty when the row is open or was reopened",
    "checked_at": "the time the check (LayerCheck) last judged the row, the time `validated` was set or cleared",
}
OLD_ITEM = {"kind": "old", "ledger_only": True, "none_allowed": False, "member_role": "lexical",
            "asks": "What is the fate of this old observation in scope? Answer it once: keep or restate (with its marker), merge, consume, delete_neither, defer, or carry it to a later step. "
                    "The ledger records the fate as it is answered."}


def new_value(cur: dict) -> dict:
    new = json.loads(json.dumps(cur))
    for st in new["steps"]:
        if st["key"] == "2.1":
            st["items"] = [i for i in st["items"] if i != "group-relation"]
    new["items"].pop("group-relation", None)
    for k, v in ASKS.items():
        new["items"][k]["asks"] = v
    for k in MULTI_ITEMS:
        new["items"][k]["multi"] = True
        new["items"][k]["tie_to_verse"] = True
        new["items"][k]["traces_to"] = [{"stage": "layer-1", "tag": "group"}]       # B3 builds on the B2 sense observations that hold its occurrences (researcher 2026-11-25)
    # B2: one observation for each SENSE (concept) of the subgroup, found by meaning in context, traced to the B1 observations it covers (researcher 2026-11-25)
    gd, se = new["items"]["group-definition"], new["items"]["strong-enrichment"]
    for it in (gd, se):
        it["multi"] = True
        it["exactly_once"] = True
        it["tie_to_verse"] = True
    gd["traces_to"] = [{"stage": "lexical"}]
    gd["carries_all_of"] = {"stage": "lexical"}
    se["traces_to"] = [{"stage": "layer-1", "tag": "group"}]
    se["carries_all_of"] = {"stage": "layer-1", "tag": "group"}
    gd["asks"] = ("What are the senses of this subgroup, found by meaning in context? Read the word observations (step S1) and gather the occurrences, of any surface and any Strong's code of the subgroup, whose meaning in "
                  "context is the same into one sense; the same surface may carry different senses and different surfaces one. The meaning rests on what the base data say (the Strong's code, the lexicon, the verse), not on "
                  "the English surface alone. Write one finding for each sense, naming the occurrences it covers (each occurrence in exactly one sense). Say only what the base data show.")
    se["asks"] = ("What do the Strong's codes of each sense say? Validate the sense against them, give a short definition from the lexicon entries and name the codes that link the sense to its usage. Write one finding "
                  "for each sense of step 1.1, naming the same occurrences. State what the lexicon entries show.")
    new["items"]["old-observation"] = json.loads(json.dumps(OLD_ITEM))
    for st in new["steps"]:
        if st["key"] in ("S1", "1.1", "1.2", "2.1") and "old-observation" not in st["items"]:
            st["items"] = list(st["items"]) + ["old-observation"]
    x33 = new["items"]["interworking"]      # 3.3 (researcher 2026-11-25): one observation for each unique match across the observations that reference more than one collection
    x33["asks"] = ("What does this match show? The match is one pairing of a word of this collection with a word of another collection that the nodes of the observations place together in the shared verses. "
                   "Record ONE observation for the match, with a traced node on EVERY observation the match comes from and the occurrences of both sides in the shared verses as nodes. "
                   "The pairing can span many verses (all of them are nodes of the one observation): read the verses and observe whether they show a variety of implications or a single behaviour, and say which. It is the basis for a deeper analysis of what the pairing means; many matches will have no inner-being significance, and that is for later: record what the observations show, or none with the reason.")
    for st in new["steps"]:
        if st["key"] == "3.3":
            st["pairs"] = False
    new["thresholds"].pop("relation_min_verses", None)
    new["thresholds"].pop("pair_min_verses", None)        # step 3.3 asks for a row for any shared verse: a minimum was never the researcher's
    new.pop("pull_verse_texts", None)                     # step 3.1 is given the text of ALL the verses of the subgroup (researcher 2026-11-24)
    new.setdefault("partner_complete", [])                # the partner collections the researcher has declared complete when asked (step 3.3 gate)
    return new


def ddl(conn):
    """The columns of the ledger stamps (idempotent). A schema change: the cfg_column rows are written by plan()."""
    have = {r[1] for r in conn.execute("PRAGMA table_info(collection_layer_item)")}
    for col in STAMPS:
        if col not in have:
            conn.execute(f"ALTER TABLE collection_layer_item ADD COLUMN {col} TEXT")


def apply_to_copy(conn):
    """For a test copy: the config of the specification (cfg_setting only) and the columns, with no cfg_column logging and no snapshot. Never used on the live database."""
    for _t, _op, _w, _s in plan(conn):
        if _t == "cfg_setting":
            conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (_s["value"], _w["key"]))
    ddl(conn)
    conn.commit()


def plan(conn):
    one = lambda q, *a: conn.execute(q, a).fetchone()  # noqa: E731
    ops = []
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading'")[0])
    new = new_value(cur)
    if new != cur:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    top = one("SELECT coalesce(max(ordinal), -1) FROM cfg_column WHERE database='iba' AND table_name='collection_layer_item'")[0]
    for i, (col, use) in enumerate(STAMPS.items(), 1):
        if not one("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='collection_layer_item' AND name=?", col):
            ops.append(("cfg_column", "insert", {}, {"database": "iba", "table_name": "collection_layer_item", "name": col, "type": "TEXT", "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None,
                                                     "use": use, "expectation": "an ISO UTC time or empty", "source": SOURCE, "filled_by": "lib/layerreading.py (pull, record, check) and lib/buildvalidate.py ledger_answer",
                                                     "inactive": 0, "ordinal": top + i}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2538: step 2.1 answered by findings, group-relation removed; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where)
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-findings-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT fi")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        ddl(conn)
        conn.execute("RELEASE fi")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO fi")
        conn.execute("RELEASE fi")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
