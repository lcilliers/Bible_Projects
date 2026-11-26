"""traceindex_2538_v1_20261126.py -- escalation #2538: an index on ib_node(traced_observation_id).

Researcher 2026-11-26: "are you doing full scans with the validation actions." Yes: every lookup of the observations that trace a given one
(`ib_node WHERE traced_observation_id=?`) scanned all of ib_node (102,718 rows), because the column had no index. It runs on every delete
(observationrecord.release_traces, #2618), in validationactions.consume and delete_neither, and in layerinner's trace lookups.
  cfg_index    idx_ib_node_traced_observation_id on ib_node (traced_observation_id), registered so the schema build makes it
  the index    created on the database
  cfg_utility  this migration's own row
Config through configmaint.apply_logged; named snapshot before a live apply; archives itself after. Idempotent.
Usage: python iba/app/migration/traceindex_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-TRACEINDEX-20261126"
MODULE = "traceindex_2538_v1_20261126"
INDEX = ("ib_node", "idx_ib_node_traced_observation_id", "traced_observation_id")


def plan(conn):
    ops = []
    t, name, col = INDEX
    if not conn.execute("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", (t, name)).fetchone():
        ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": col, "ordinal": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: the index on ib_node(traced_observation_id), so no trace lookup scans ib_node",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    t, name, col = INDEX
    has = conn.execute("SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (name,)).fetchone()
    if a.dry_run or (not ops and has):
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s), index {'present' if has else 'to create'}")
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-traceindex-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t_, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t_, op, where, set_)
        conn.execute(f"CREATE INDEX IF NOT EXISTS {name} ON {t} ({col})")
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s), index {name} created")
    if live:
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
