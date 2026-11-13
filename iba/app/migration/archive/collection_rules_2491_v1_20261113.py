"""collection_rules_2491_v1_20261113.py -- escalation #2491: the researcher's rulings of 2026-11-12 and 2026-11-13 on how collections are built,
as one study_method behaviour rule (general scope, study_active). Plan v3 step 0 asked for this (B:31: a rule lives in the authoritative record).

The rulings are recorded verbatim on #2491 (v9, v11, v12 and v13); the rule text below states them without adding to them. Researcher 2026-11-12 in
the essentials: 'Each surface in scope must be a member of one collection. A collection is compiled by putting like words together (synonyms, opposites,
gathered etc). Each member carries verses. A surface should only in very rare circumstances be in more than one collection.'

cfg_* writes through configmaint.apply_logged(). Refuses to run twice.
Usage: python -m iba.app.migration.collection_rules_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2491-COLLECTION-RULES-20261113"
MODULE = "collection_rules_2491_v1_20261113"
KEY = "collections-are-built-on-surfaces-one-each"
TEXT = ("A collection is built on surfaces. Every surface in scope (a word or phrase of the groups behaviour and inner_being_state that has a verse) "
        "is a member of exactly one collection; a surface is in more than one only in very rare circumstances and by the researcher's ruling. A collection "
        "is made by putting like words together (synonyms, opposites, gathered); its members carry the verses. The Strong's code is not the unit and the "
        "base is only an instrument for gathering like words, never the member: a derived form is a surface with a link of its own. A phrase is one "
        "concept and the concept is placed in one collection, not each word of it (the phrase rule of #2437, attach_phrases, is retired). An opposite sits "
        "once: where it stands alone it goes where it is the opposite; where it has its own collection with other members it sits there. Collections whose "
        "members coincide or are close are combined; a small collection is grouped with like-minded ones unless it is truly unique. The name of a collection "
        "is formed from all its members as a concept covering them; the base is the name where suitable. Each collection becomes a chapter of the "
        "narration, so it must make sense, not overlap another and tell a coherent story: a light evaluation only, no chapter number or title is "
        "designed. A word that is neither a behaviour nor an inner-being state (a generic evaluative, motion, quantity, speech or copula word) is not "
        "a surface of a collection and is regrouped to other; the never-grouped surface texts are deliberately outside the collections. Claude "
        "decides combinations, placements and names by what the words mean and brings to the researcher only what it cannot decide from meaning, with "
        "the evidence for that case alone; where it can decide only by word matching it says so. A change to the collections is made class by class, "
        "tried on a copy, under a named snapshot, with the counts predicted and checked, links set deleted and never removed, every change kept in "
        "surface_event, and recorded in BUILD. A node carries the one collection of its surface by the own-row rule (a surface with a link of its own is "
        "read by it; one without, through its base). Coverage is reported as lists under one stated definition, never as a percentage on a changing definition.")
SRC = ("Researcher rulings, escalation #2491 (2026-11-12 and 2026-11-13 sessions, developer mode), verbatim on #2491 v9, v11, v12 and v13 and in "
       "outputs/escalation/2491-collection-rebuild-plan-v3-20261112.md section 1; applied in BUILD 498 to 505.")
ENFORCED = ("The phrase rule is refused by the collection.attach_phrases handler (iba/app/handlers/collectionbuild.py, BUILD 502); the rest is "
            "context-delivered at the start of a session while the study is active (cfg_rule_scope general); working practice.")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn):
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_behaviour_rule WHERE class='study_method' AND rule_key=?", KEY):
        nid = one("SELECT max(id) FROM cfg_behaviour_rule")[0] + 1
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": nid, "class": "study_method", "rule_key": KEY, "rule_text": TEXT, "source": SRC, "enforced_by": ENFORCED,
            "added_at": now(), "active": 1, "enforcement_status": "partially_enforced", "deliver_when": "study_active"}))
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{nid}", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other "
                                    "Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2491: the researcher's rulings on how collections are built as one study_method "
                       f"behaviour rule; run_id {RUN_ID}."}))
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
            print(f"  {op:6} {t:20} {s.get('rule_key') or s.get('module') or s.get('rule_ref')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
