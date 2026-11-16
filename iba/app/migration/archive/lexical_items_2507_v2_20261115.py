"""lexical_items_2507_v2_20261115.py -- escalation #2507: the stage 1 item redefined to the observation rules.

The first run of stage 1 (BUILD 534) wrote one observation for each word that restated the dictionary range of its code and was not tied to what the verse says; the researcher removed it
(BUILD 535). Behaviour rule 131 (an observation interprets what its verse says, is founded in it and is tied to its verses) and RW-04 (never a restatement of the word's dictionary sense)
govern. RG-22 (a function word gets no observation of its own, except a negator and a connective) governs which words are read. The items word-lexical and word-face are replaced by one item:
  word-sense   one ledger row for each content word (surface and lettered Strong's code); answered by one observation for each sense the verses give the word (kind term, or face where an
               occurrence departs from the usual sense), each with the occurrences it holds for, together every occurrence; the text cites its verses and does not restate them.
  layer.reading gains function_classes (the morph classes that are function words, RG-22) and the item flags multi, kinds and tie_to_verse.
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage: python iba/app/migration/lexical_items_2507_v2_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2507-LEXICAL-ITEMS-20261115"
MODULE = "lexical_items_2507_v2_20261115"
MSRC = "strong_meaning_tree; strong_lexicon.lsj; strong_lexicon.mounce"
PROMPTS = ["M0.1.1", "M0.1.2", "M0.1.3", "M0.4.1", "M0.5.1", "M0.5.2", "M0.5.3", "M0.5.4", "M0.5.5", "M0.5.6", "M0.5.7", "M0.5.8", "M0.5.9", "M0.5.11"]
FUNCTION_CLASSES = ["preposition", "particle", "pronoun", "relative pronoun", "demonstrative", "reflexive pronoun", "possessive", "correlative pronoun", "reciprocal pronoun", "article",
                    "suffix", "interrogative", "correlative interrogative", "conditional"]
ITEM = {"kind": "term", "kinds": ["term", "face"], "multi": True, "tie_to_verse": True, "none_allowed": False, "member_role": "lexical", "window": "meaning", "meaning_source": MSRC,
        "prompts": PROMPTS,
        "asks": "In the verses of this collection where this word stands (the surface with its lettered Strong's code), what does it mean in each, as the verse itself shows it? Write one observation "
                "for each sense the verses give it, with the occurrences it holds for (every occurrence is in some sense, none is left out): state the sense in the verse, how the verse shows it "
                "(the words it stands with, the construction, the morph) and name the verses by reference. An occurrence whose sense departs from the usual sense of the word is its own "
                "observation, of kind face. The lexicon entries are evidence to read, never text to restate (RW-04, B:131). A prompt that does not apply is not answered (RG-17)."}
LR02 = ("The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the "
        "recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and "
        "together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or "
        "read, B:131) and tied to its verses (the text names them and does not restate them): the lexical items (S1, 1.2, 2.1) state what the verses, the lexicon and the stored structure show "
        "of a word in its verses and never what a word does for the inner being; only the group definition of step 1.1, the researcher's grouping, states what the group is or does for the "
        "inner being. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.")
LX01 = ("The rules RG-08 (the original word), RG-09 (the face), RG-14 (morph read), RG-16 (homonym and data error), RG-21 (grain), RG-22 (a function word gets no observation of its own, except a "
        "negator and a connective), RW-04 and RW-05 (concise and span-grounded: never a restatement of the word's dictionary sense) apply to the lexical items as they do to the reading and are "
        "not restated here; the recorder refuses an observation that names none of its verses or restates one of them. Adjacency is not scope (#2463 v28): a negator or qualifier beside a word "
        "reaches the word it governs, which the observation states and never assumes.")


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    lay = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading' AND inactive=0")[0])
    new = json.loads(json.dumps(lay))
    new["items"].pop("word-lexical", None)
    new["items"].pop("word-face", None)
    new["items"]["word-sense"] = ITEM
    for st in new["steps"]:
        if st["key"] == "S1":
            st["items"] = ["word-sense"]
    new["function_classes"] = FUNCTION_CLASSES
    if new != lay:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    if one("SELECT rule_text FROM cfg_method_rule WHERE id=238")[0] != LR02:
        ops.append(("cfg_method_rule", "update", {"id": 238}, {"rule_text": LR02}))
    r = one("SELECT id, rule_text FROM cfg_method_rule WHERE step='collection.layer_record' AND rule_key LIKE 'LX-01%'")
    if r and r[1] != LX01:
        ops.append(("cfg_method_rule", "update", {"id": r[0]}, {"rule_text": LX01}))
    for name, text in (("item", "the kind of aspect (layer.reading items): word-sense, group-definition, strong-enrichment, pairing, qualifier, entity, direction, group-relation, double-meaning"),
                       ("subject", "what distinguishes the aspect within a group: the word of a stage 1 aspect (surface|lettered Strong's code), the partner collection of a pairing, the other group of a relation (its id), the surface of a double meaning; empty otherwise")):
        if one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='collection_layer_item' AND name=?", name)[0] != text:
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": "collection_layer_item", "name": name}, {"use": text}))
    r = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=132")[0]
    old = ("each an observation whose nodes are its occurrences, and the occurrences where a word's meaning departs "
           "from its usual sense are face observations;")
    if old in r:
        ops.append(("cfg_behaviour_rule", "update", {"id": 132}, {"rule_text": r.replace(old, "each sense the verses give it an observation tied to its verses whose nodes are the occurrences it holds for, "
                                                                                          "and an occurrence whose sense departs from the usual one a face observation;")}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py",
                                                  "purpose": f"ONE-OFF migration -- escalation #2507: the stage 1 item redefined to the observation rules; run_id {RUN_ID}.", "inactive": 1,
                                                  "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
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
            print(" ", t, op, where)
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-items', named=True)}")
    try:
        conn.execute("SAVEPOINT items_2507")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE items_2507")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO items_2507")
        conn.execute("RELEASE items_2507")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
