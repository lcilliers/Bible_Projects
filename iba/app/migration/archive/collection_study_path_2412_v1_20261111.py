"""collection_study_path_2412_v1_20261111.py -- escalation #2412: the researcher's ruling of 2026-11-10 on how each collection is studied,
as one study_method behaviour rule (general scope, study_active).

The ruling (verbatim, 2026-11-10): "we now have units of study (the collection) and have a path into articulating the findings (observations -
claims - narration), the narrative has a structure that supports the units of study (chapter 10 by collection). Going forward each collection
picked up in the study will be taken through the entire path. your role will be do prepare and present the different aspects of the synergy and
analysis to me in a digestable format, recording it faithfully and complete in the database so ensure the fundamental trackability of everything.
there is no path for one shot bulk analysis that will produce the result. the nuances in the base data are too varied, too wide, too interwoven
the merely systemise it into a narrow band."

cfg_* writes through configmaint.apply_logged(). Refuses to run twice.
Usage: python iba/app/migration/collection_study_path_2412_v1_20261111.py [--db PATH] [--dry-run]"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2412-COLLECTION-STUDY-PATH-20261111"
MODULE = "collection_study_path_2412_v1_20261111"
KEY = "collection-taken-through-whole-path-with-researcher"
TEXT = ("The unit of study is the collection. Each collection taken up in the study goes through the whole path: observations, claims, narration "
        "(the narrative's chapter 10 is built by collection). The researcher does the interpretation and evaluation with Claude; Claude prepares and "
        "presents the aspects of the synergy and analysis in a form the researcher can digest, and records everything faithfully and completely in "
        "the database so that every step is traceable. No bulk or one-shot analysis, by Claude or by a model on the Ollama server, is used to produce "
        "the study result: the nuances of the base data are too varied and interwoven to be reduced to a narrow band. Item-by-item roles written in "
        "one pass, templated observation text and sense groups assigned by pattern are not a substitute for reading and articulating each discovery "
        "(for example what is sought, what is found or not found, why and when). Engagement of a collection (Engagement.ps1) is a preparatory "
        "step inside this path, not the result.")
SRC = ("Researcher ruling, escalation #2412 (2026-11-10 session, developer mode), verbatim in the migration docstring "
       "iba/app/migration/archive/collection_study_path_2412_v1_20261111.py and on #2412; recorded with #2460 (what engagement stores) open.")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn):
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_behaviour_rule WHERE class='study_method' AND rule_key=?", KEY):
        nid = one("SELECT max(id) FROM cfg_behaviour_rule")[0] + 1
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": nid, "class": "study_method", "rule_key": KEY, "rule_text": TEXT, "source": SRC,
            "enforced_by": "Context-delivered at the start of a session while the study is active (cfg_rule_scope general); a working practice, "
                           "not mechanically enforced",
            "added_at": now(), "active": 1, "enforcement_status": "context_delivered", "deliver_when": "study_active"}))
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{nid}", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other "
                                    "Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2412: the researcher's ruling on studying each collection through the whole path as one "
                       f"study_method behaviour rule; run_id {RUN_ID}."}))
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
