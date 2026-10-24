"""method_file_2271_v1_20261024.py -- escalation #2271 (#2268 W-1): the live parts of the July verse-analysis method
file (Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md) as method rules on reading.record, and one
setting; the file is then archived (#2268 R11: "Take from the file what is relevant, and place it in config, then
archive the file. I know for instance that genre is no longer written to any table, and we no longer do any book
reading so a lot of stuff from this document is no longer relevant").

Carried: the read-back loop (sec 1, 4, 13a), the grain (sec 11), content words carry the impact and T2 never stands
alone (sec 12), the stop-list, the adverbial qualifier and the simile (sec 14). Not carried, retired with the file:
ve_lexical, process markers, genre, passage-by-consecutive-run, term-driven batching, book/chapter/segmentation
reading, the story filed to prose tables, and the Phase-1 derivation residuals (sec 2, 3, 5 to 10, 12 storage, 14
scripts, 15). Worked examples it holds (Psa 1:1 and 1:5; the perek driver/restraint learning) go to build B10.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Refuses to
run twice.

Usage:
    python iba/app/migration/method_file_2271_v1_20261024.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2271-METHOD-FILE-20261024"
MODULE = "method_file_2271_v1_20261024"
SRC = "Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md (archived); #2271, #2268 R11"

RULES = [
    ("RG-20 read-back", "After recording, every observation is read back against the verse for sense. An uncertain one "
     "is recorded as uncertain (tag could-not-resolve, or basis read: 'I read'), never asserted. A rule found to be "
     "systematically wrong is raised as a config change with the learning, never worked round in the reading.",
     "sec 1, 4, 13a"),
    ("RG-21 grain", "A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The "
     "occurrences of a word with several senses are related per grain and never aggregated across grains: related "
     "verses are same-grain occurrences.", "sec 11"),
    ("RG-22 content-words-carry-impact", "Content words carry the inner-being impact and are read even when no "
     "cluster tags them. Function words (particles, prepositions, conjunctions, suffixes, pronouns) get no observation "
     "of their own, except negators and connectives, which are read for what they do (RG-07). A T2 word never stands "
     "alone: it is read as the qualifier of what it binds to.", "sec 12"),
    ("RG-23 never-characteristic", "The words in cfg_setting reading.non_characteristic_strongs are never a verse's "
     "characteristic: superscription metadata and named external adversaries. They are read as standalone or as "
     "qualifiers. The list is per word, not per cluster, because a cluster can hold both kinds.", "sec 14 stop-list"),
    ("RG-24 adverbial-qualifier", "A tagged word that works adverbially in an occurrence (a noun with a preposition "
     "qualifying the predicate, as 'in the counsel of the wicked') is a qualifier there, not the verse's "
     "characteristic. The role is per occurrence: the same word may be the characteristic elsewhere.", "sec 14"),
    ("RG-25 simile-tenor", "In a simile, the predicates of the vehicle (the tree that yields, does not wither) are "
     "read for what they say of the one compared (the tenor), not as the vehicle's own acts.", "sec 14"),
]
NON_CHAR = {"H4210": "superscription: 'Psalm' (mizmor)", "H7892": "superscription: 'Song' (shir)",
            "H5329": "superscription: 'to the choirmaster' (menatseach)", "H0341": "external adversary: 'enemy'",
            "H6862": "external adversary: 'foe, adversary'"}


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    base = one("SELECT coalesce(max(ordinal),0) FROM cfg_method_rule WHERE step='reading.record'")[0]
    for i, (key, text, sec) in enumerate(RULES, 1):
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "reading.record", "rule_key": key,
                                                          "rule_text": text, "source_doc": f"{sec}; {SRC}",
                                                          "enforced_by": None, "ordinal": base + i, "active": 1}))
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.non_characteristic_strongs'"):
        ops.append(("cfg_setting", "insert", {}, {
            "key": "reading.non_characteristic_strongs", "value": json.dumps(NON_CHAR, ensure_ascii=False),
            "use": "#2271 (method file sec 14 stop-list): words that are never a verse's characteristic (method rule "
                   "RG-23); per word, extended as verified words appear", "module": "reading", "inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2271 (#2268 W-1): the July method file's live rules as "
                       f"method rules RG-20 to RG-25 and reading.non_characteristic_strongs; run_id {RUN_ID}."}))
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
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
