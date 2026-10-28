"""backup_rollback_method_2301_v1_20261028.py -- escalation #2301: the rollback method.

Researcher, chat 2026-10-28 (verbatim): "the rule regarding database copies is no longer functional. the rule should be modified to a method
that is more in line with the objective of ensuring rollback can be performed, but also no making continuious copies of the entire DB that
is really unproductive." (#2301 v5 and v7, 2026-10-26: "approved to prune the snapshots"; "I approved 2301 for your action".)

The rule (backup.pre_run_snapshot_policy) took a full copy of iba.db, about 870 MB and 7 seconds, before EVERY new run, even a read-only
report, and kept the newest 5 (retention.snapshot_keep_count): four session-close runs in one hour used the window, and the named copies
taken before a migration were pruned with them. It gave no usable rollback and cost a copy for every run. The method now (config, read by
iba/app/lib/dbsnapshot.py): backup.rollback_method
- a run snapshot is taken before a new run only when the newest is older than min_interval_minutes (120);
- run snapshots keep the newest keep_recent (2) and the newest of each of the last keep_daily (3) calendar days, today included;
- a named snapshot (dbsnapshot --named), taken on purpose before a migration or a bulk change, is kept in its own folder (named_dir) and is
  never pruned by the run snapshots; the newest keep_named (4) are kept.
Between two snapshots the changes are in the change records, the reading files and git, and the NAS keeps a daily copy.

This migration: adds backup.rollback_method; restates backup.pre_run_snapshot_policy (one home for the rule: it points at the setting);
retires retention.snapshot_keep_count (inactive); amends cfg_behaviour_rule developer-mode-scope-and-conduct (a rollback point before a
migration is a named snapshot, not an ad-hoc copy).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/backup_rollback_method_2301_v1_20261028.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2301-ROLLBACK-METHOD-20261028"
MODULE = "backup_rollback_method_2301_v1_20261028"
RULE = {"min_interval_minutes": 120, "keep_recent": 2, "keep_daily": 3, "keep_named": 4, "named_dir": "kept"}
RULE_USE = (
    "the rollback method (#2301): a run snapshot of iba.db (SQLite backup API, lib/dbsnapshot.copy_db) is taken before a new run only when the "
    "newest run snapshot is older than min_interval_minutes; run snapshots keep the newest keep_recent plus the newest of each of the last "
    "keep_daily calendar days, today included (older ones are removed); a named snapshot (python -m iba.app.lib.dbsnapshot --reason <id> --named), taken on purpose "
    "before a migration or a bulk change, is kept in named_dir under iba/app/db/snapshots, never pruned by the run snapshots, the newest "
    "keep_named kept. Between snapshots the changes are in the change records (cfg_change_detail, ib_observation_change, "
    "escalation_history), the reading files and git; the NAS keeps a daily copy of iba.db. Read by iba/app/lib/dbsnapshot.py")
POLICY = ("the rollback method is cfg_setting backup.rollback_method: a database snapshot (SQLite backup API, lib/dbsnapshot.copy_db) before a "
          "new run only when the newest is older than min_interval_minutes, kept as the newest few plus one per day for a few days, and a "
          "named snapshot (dbsnapshot --named) before a migration or a bulk change, kept apart; run.py:_ensure_run -> "
          "lib/dbsnapshot.snapshot(). IBA_NO_SNAPSHOT=1 skips it for a tight loop. The NAS copy of iba.db is "
          "backup.nas_db_backup_schedule.")
DEV_OLD = "never a file copy), with the result recorded on its escalation;"
DEV_NEW = ("never a file copy), with the result recorded on its escalation; a rollback point before a migration or a bulk change is a named "
           "snapshot (iba/app/lib/dbsnapshot.py --named, cfg_setting backup.rollback_method), not an ad-hoc copy of the database;")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_setting WHERE key='backup.rollback_method'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "backup.rollback_method", "value": json.dumps(RULE), "use": RULE_USE,
                                                  "module": "backup", "inactive": 0}))
    ops.append(("cfg_setting", "update", {"key": "backup.pre_run_snapshot_policy"}, {"value": json.dumps(POLICY)}))
    ops.append(("cfg_setting", "update", {"key": "retention.snapshot_keep_count"}, {"inactive": 1}))
    row = one("SELECT rule_text, source FROM cfg_behaviour_rule WHERE rule_key='developer-mode-scope-and-conduct'")
    if row and DEV_OLD in row[0]:
        ops.append(("cfg_behaviour_rule", "update", {"rule_key": "developer-mode-scope-and-conduct"},
                    {"rule_text": row[0].replace(DEV_OLD, DEV_NEW, 1),
                     "source": row[1] + " | Amended 2026-10-28 (escalation #2301): a rollback point is a named snapshot."}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2301: the rollback method (backup.rollback_method); run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
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
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
