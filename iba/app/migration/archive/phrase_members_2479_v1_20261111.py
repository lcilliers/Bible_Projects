"""phrase_members_2479_v1_20261111.py -- escalation #2479: the phrases attached to a collection are members of it.

  settings   collection.member_tiers (new: core, synonym, opposite, gathered, phrase -- read by the exports, the evidence report and engagement);
             collection.export_tiers (use text only: the word tiers a phrase is matched against by attach_phrases)
  step       engagement.pull: description brought up to date (-Missing)
  utilities  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/phrase_members_2479_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2479-PHRASE-MEMBERS-20261111"
MODULE = "phrase_members_2479_v1_20261111"
MEMBER_TIERS = ("collection.member_tiers", ["core", "synonym", "opposite", "gathered", "phrase"],
                "the tiers of a collection that count as its members in the exports, the evidence report and the engagement of the surface work (#2479, researcher 2026-11-11: the "
                "phrases attached to a collection are members of it); possible_opposite, associated and set_aside are listed apart and are not members", "collection")
EXPORT_USE = ("the tiers of a collection that are words: the tiers attach_phrases matches a phrase against (#2437); the members of a collection are the tiers of "
              "collection.member_tiers, which adds phrase (#2479)")
STEP_DOES = ("write the working file of one collection with -Collection: its member surfaces, their verses with the ESV text and the observations already on those verses (a view of the "
             "tables, never overwritten); -Batch n gives one batch of the items; -Missing gives only the items with no engagement observation yet -- see lib/engagement.py "
             "(escalations #2406, #2388, #2479)")
UTILITIES = [(MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2479: phrases are members of their collections; run_id {RUN_ID}.", 1,
              "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    key, value, use, module = MEMBER_TIERS
    if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
        ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='collection.export_tiers' AND use=?", EXPORT_USE):
        ops.append(("cfg_setting", "update", {"key": "collection.export_tiers"}, {"use": EXPORT_USE}))
    if not has("SELECT 1 FROM cfg_step WHERE step='engagement.pull' AND does=?", STEP_DOES):
        ops.append(("cfg_step", "update", {"step": "engagement.pull"}, {"does": STEP_DOES}))
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2479-phrase-members', named=True)}")
    try:
        conn.execute("SAVEPOINT phrase_members")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE phrase_members")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO phrase_members")
        conn.execute("RELEASE phrase_members")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
