"""collection_evidence_pairs_2502_v1_20261114.py -- escalation #2502: the collection evidence report carries the layer 2 pairings (the words that live with the member words in
their verses, typed, with side and distance, counted at the Strong's code, the surface and the collection; qualifiers as a type of pairing).

  setting    collection.evidence_pairs (the collection statuses read for the neighbour's collection, the distance bands, the morph classes, what makes a qualifier candidate, the
             length of a top list)
  step       collection.evidence: description brought up to date
  utilities  lib/collectionevidence.py and lib/collectionevidencereport.py: purpose brought up to date; this migration registered
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/collection_evidence_pairs_2502_v1_20261114.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2502-COLLECTION-EVIDENCE-PAIRS-20261114"
MODULE = "collection_evidence_pairs_2502_v1_20261114"
KEY = "collection.evidence_pairs"
VALUE = {
    "collection_status": ["confirmed"],
    "bands": {"adjacent": 1, "near": 3},
    "morph_class": {
        "NT": {"N": "noun", "V": "verb", "CONJ": "conjunction", "P": "pronoun", "PREP": "preposition", "A": "adjective", "PRT": "particle", "ADV": "adverb",
               "R": "relative pronoun", "D": "demonstrative", "COND": "conditional", "I": "interrogative", "X": "other", "INJ": "interjection",
               "F": "reflexive pronoun", "S": "possessive", "K": "correlative pronoun", "C": "reciprocal pronoun", "T": "article", "Q": "correlative interrogative"},
        "OT": {"N": "noun", "V": "verb", "R": "preposition", "T": "particle", "S": "suffix", "C": "conjunction", "A": "adjective", "P": "pronoun", "D": "adverb"},
    },
    "qualifier": {"cluster_codes": ["T5"], "subgroup_kind": "qualifier", "morph_classes": ["adjective", "adverb"]},
    "top_n": 15,
}
USE = ("the layer 2 pairings of the collection evidence report (#2502): collection_status = the statuses of the collections read for the collection of a neighbouring word; "
       "bands = the distance in verse_lexical positions up to which a pairing is adjacent and near (above near is far); morph_class = the grammar hint of a morph code, NT by the part "
       "before the first hyphen, OT by the letter after the language letter; qualifier = what makes a neighbouring word a qualifier candidate: a cluster code (T5 negator), a surface in a "
       "cluster_subgroup of this kind (history data), or a morph class; top_n = the length of the top lists in the Markdown. A hint and a candidate decide nothing: the reading does")
STEP_DOES = ("write the evidence report of one collection or a comma list (-Collection), or of a verse or list of verses (-Verse, items separated by a semicolon): a Markdown report "
             "(the Strong's codes behind the members, the pairings of the member words with the words of their verses, what the study recorded for their occurrences, the claims and the "
             "narrative, the phrases, the faults) and an Excel workbook (every listing in full, one sheet each, among them the verse view, the pairings and the pairing counts) under "
             "surfaces.exports_root, versioned by the filing rule, the previous live versions archived; verses in Scripture order; no evaluation, nothing inferred, nothing written to a "
             "table; -Check writes no file -- see lib/collectionevidence.py and lib/collectionevidencereport.py (escalations #2464, #2467, #2469, #2477, #2502)")
EV_PURPOSE = ("collectionevidence.py -- the data of the evidence report of one collection, a list or a verse list: the stored entries from the base data through observations and claims "
              "into the narrative, and the pairings of the member words with the words of their verses, read-only on the tables (escalations #2464, #2467, #2477, #2502); "
              "lib/collectionevidencereport.py writes the Markdown and the workbook from it.")
REP_PURPOSE = ("collectionevidencereport.py -- the Markdown report and the Excel workbook of the collection evidence data: built up from the Strong's codes behind the members to the "
               "pairings, observations, claims, narrative, phrases and faults; one workbook sheet for each listing (escalations #2477, #2502).")
UTILITIES = [
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2502: the collection evidence report carries the layer 2 pairings; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_setting WHERE key=?", KEY):
        ops.append(("cfg_setting", "insert", {}, {"key": KEY, "value": json.dumps(VALUE), "use": USE, "module": "collection", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step='collection.evidence' AND does=?", STEP_DOES):
        ops.append(("cfg_step", "update", {"step": "collection.evidence"}, {"does": STEP_DOES}))
    if not has("SELECT 1 FROM cfg_utility WHERE module='collectionevidence' AND purpose=?", EV_PURPOSE):
        ops.append(("cfg_utility", "update", {"module": "collectionevidence"}, {"purpose": EV_PURPOSE}))
    if not has("SELECT 1 FROM cfg_utility WHERE module='collectionevidencereport' AND purpose=?", REP_PURPOSE):
        ops.append(("cfg_utility", "update", {"module": "collectionevidencereport"}, {"purpose": REP_PURPOSE}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or set_.get("key") or set_.get("step") or set_.get("module"))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2502-collection-evidence-pairs', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_evidence_pairs")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE collection_evidence_pairs")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_evidence_pairs")
        conn.execute("RELEASE collection_evidence_pairs")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
