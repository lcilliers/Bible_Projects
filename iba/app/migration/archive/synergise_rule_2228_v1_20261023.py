"""synergise_rule_2228_v1_20261023.py -- escalation #2228: the researcher's rule that synergising is done from
the tables, never from memory, as a cfg_behaviour_rule row (study_method, delivered while the study is active,
a general rule so the session compliance file restates it).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/synergise_rule_2228_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2228-SYNERGISE-RULE-20261023"
MODULE = "synergise_rule_2228_v1_20261023"
KEY = "synergise-from-tables-not-memory"
TEXT = ("Study work runs in order: the scope is resolved (Verse-Scope.ps1), what is already known is collated for it, "
        "the gaps are recorded into the tables, and only then are claims finalised and the narrative written. That "
        "last step, synergising, is done only from the tables (observations, strand faces, claims and their sources, "
        "read through the app for the scope in hand), never from memory or recollection of earlier readings or of the "
        "conversation. The recording is finished first; a session may break between the end of recording and the "
        "start of synergising.")
SOURCE = ("Researcher, chat 2026-10-23 (verbatim, #2228 v23): \"with the tool of scoping and collating the material to "
          "work with, preventing rework of territory already covered,  the recording of the gaps based on the material "
          "at hand can begin, and then after the gaps have been updated, the newly formed database results can be used "
          "to finalise the claims leading into the narrative.  I would not be surprised if a session should break "
          "between the finalisation of the recording phase, and the start of the synergising. synergising should never "
          "be done from memory. it must be based on the tables.\"")


def plan(conn) -> list[tuple]:
    ops = []
    row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (KEY,)).fetchone()
    rid = row[0] if row else conn.execute("SELECT max(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    if not row:
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": rid, "class": "study_method", "rule_key": KEY, "rule_text": TEXT, "source": SOURCE,
            "enforced_by": "Context-delivered at session start while the study is active (rule 81); the tools of #2228 "
                           "give the tables for a scope", "added_at": datetime.datetime.now(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"), "active": 1, "enforcement_status": "context_delivered",
            "deliver_when": "study_active"}))
    if not conn.execute("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='general'", (f"B:{rid}",)).fetchone():
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{rid}", "scope_kind": "general",
                                                     "scope_value": "general", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2228: cfg_behaviour_rule {KEY} (general, study_active); "
                       f"run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
