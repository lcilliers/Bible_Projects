"""cfg_sc4a_own_log_2462_v1_20261111.py -- escalation #2462: SC4a checks a session log only when it names this session's id.

  rule  behaviour rule B:80 (open-items-lines-carry-a-handle): the text and the enforced_by say a log of another session is not checked again
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_sc4a_own_log_2462_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2462-SC4A-OWN-LOG-20261111"
MODULE = "cfg_sc4a_own_log_2462_v1_20261111"
RULE_ID = 80
ADD_TEXT = " A session log is checked only when it names this session's id; a log of another session was checked at that session's own close."
OLD_ENF = "session-close SC4(a) (handlers/session_close.py _sc4a) on every .md file changed in the session."
NEW_ENF = ("session-close SC4(a) (handlers/session_close.py _sc4a) on every .md file changed in the session, except a session log "
           "(governance.session_log_dir, SESSION-LOG-*.md) that does not name this session's id (#2462).")
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2462: SC4a checks a session log only when it names this session's id (B:80 text); run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    r = conn.execute("SELECT rule_text, enforced_by FROM cfg_behaviour_rule WHERE id=?", (RULE_ID,)).fetchone()
    new = {}
    if ADD_TEXT.strip() not in r[0]:
        new["rule_text"] = r[0].rstrip() + ADD_TEXT
    if r[1] == OLD_ENF:
        new["enforced_by"] = NEW_ENF
    if new:
        ops.append(("cfg_behaviour_rule", "update", {"id": RULE_ID}, new))
    module, path, inactive, purpose, exempt, reason = MIGRATION_ROW
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone() is None:
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
            print(" ", t, op, where or set_.get("module"), sorted(set_))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2462-sc4a-own-log', named=True)}")
    try:
        conn.execute("SAVEPOINT sc4a_own_log")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sc4a_own_log")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sc4a_own_log")
        conn.execute("RELEASE sc4a_own_log")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
