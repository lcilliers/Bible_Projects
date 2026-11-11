"""collection_evidence_verse_2467_v1_20261111.py -- escalation #2467: the evidence report takes a verse or list of verses (-Verse) and two layouts (-ByType).

  settings   collection.evidence_verse_name (the file name stem of a verse report)
  step       collection.evidence: its text brought up to date
  utilities  this migration; the purpose of lib/collectionevidence.py brought up to date
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/archive/collection_evidence_verse_2467_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2467-EVIDENCE-VERSE-20261111"
MODULE = "collection_evidence_verse_2467_v1_20261111"
SETTING = ("collection.evidence_verse_name", "verse-evidence",
           "the stem of the verse evidence report's file names (#2467); the references, the version and the date follow it by the filing rule", "collection")
STEP = "collection.evidence"
STEP_DOES = ("write the evidence report of one collection or a comma list (-Collection), or of a verse or list of verses (-Verse, items separated by a semicolon): the table "
             "entries stored for every aspect of the members or words, from the base data through the observations and claims into the narrative, as a Markdown file and a CSV "
             "under collection.evidence_path, versioned by the filing rule, the previous live versions archived; verses in Scripture order; laid out by word (or verse) then by "
             "type, or by type with -ByType; no evaluation, nothing inferred, nothing written to a table; -Check writes no file -- see lib/collectionevidence.py (escalations #2464, #2467)")
UTILITY = "collectionevidence"
UTILITY_PURPOSE = ("collectionevidence.py -- the evidence report of one collection, a list of collections or a verse list: the stored entries from the base data through "
                   "observations and claims into the narrative, in Scripture order, by word or verse then by type or by type; read-only on the tables (escalations #2464, #2467).")
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2467: the evidence report takes a verse list and two layouts; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    key, value, use, module = SETTING
    if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
        ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step=? AND does=?", STEP, STEP_DOES):
        ops.append(("cfg_step", "update", {"step": STEP}, {"does": STEP_DOES}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=? AND purpose=?", UTILITY, UTILITY_PURPOSE):
        ops.append(("cfg_utility", "update", {"module": UTILITY}, {"purpose": UTILITY_PURPOSE}))
    module, path, inactive, purpose, exempt, reason = MIGRATION_ROW
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
            print(" ", t, op, where or set_.get("key") or set_.get("module"))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2467-evidence-verse', named=True)}")
    try:
        conn.execute("SAVEPOINT evidence_verse")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE evidence_verse")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO evidence_verse")
        conn.execute("RELEASE evidence_verse")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
