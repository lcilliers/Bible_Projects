"""traceindex_2538_v2_20261126.py -- escalation #2538: the trace index made partial.

v1 (traceindex_2538_v1_20261126.py) indexed ib_node(traced_observation_id) whole. 93,591 of 102,718 nodes hold NULL there (word nodes), and SQLite then
used the index for `traced_observation_id IS NULL` as for an equality: the lookups of word nodes (ReadBehaviours, layerinner._on, the 3.3 match
read) walked 93,591 index entries, and the scan guard refused ReadBehaviours. A partial index over the rows that hold a trace serves
`traced_observation_id=?` (which implies IS NOT NULL) and is never chosen for IS NULL.
  cfg_index      gains the column partial_where (registered in cfg_column); the trace index carries 'traced_observation_id IS NOT NULL'
                 (lib/cfg.py indexes and lib/db.py table_ddl build it)
  the index      dropped and built again as partial
  cfg_utility    this migration's own row
Named snapshot before a live apply; archives itself after. Idempotent.
Usage: python iba/app/migration/traceindex_2538_v2_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-TRACEINDEX2-20261126"
MODULE = "traceindex_2538_v2_20261126"
NAME, TABLE, COL, WHERE = "idx_ib_node_traced_observation_id", "ib_node", "traced_observation_id", "traced_observation_id IS NOT NULL"
CFG_COLUMN = {"database": "iba", "table_name": "cfg_index", "name": "partial_where", "ordinal": 4, "type": "TEXT", "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None,
              "fk": None, "use": "the WHERE of a partial index (NULL: a whole index); for a column that is mostly NULL, so the planner never walks the index for IS NULL (#2538)",
              "expectation": None, "source": None, "filled_by": None, "inactive": 0}


def has_col(conn):
    return any(r[1] == "partial_where" for r in conn.execute("PRAGMA table_info(cfg_index)"))


def index_sql(conn):
    r = conn.execute("SELECT sql FROM sqlite_master WHERE type='index' AND name=?", (NAME,)).fetchone()
    return r[0] if r else None


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name='cfg_index' AND name='partial_where'").fetchone():
        ops.append(("cfg_column", "insert", {}, dict(CFG_COLUMN)))
    if not has_col(conn) or conn.execute("SELECT partial_where FROM cfg_index WHERE table_name=? AND name=?", (TABLE, NAME)).fetchone()[0] != WHERE:
        ops.append(("cfg_index", "update", {"table_name": TABLE, "name": NAME, "col": COL}, {"partial_where": WHERE}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: cfg_index.partial_where and the trace index made partial",
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
    partial = "WHERE" in (index_sql(conn) or "").upper()
    if a.dry_run or (not ops and partial):
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s), index {'partial' if partial else 'to rebuild as partial'}")
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-traceindex2-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        if not has_col(conn):
            conn.execute("ALTER TABLE cfg_index ADD COLUMN partial_where TEXT")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute(f"DROP INDEX IF EXISTS {NAME}")
        conn.execute(f"CREATE INDEX {NAME} ON {TABLE} ({COL}) WHERE {WHERE}")
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s), {NAME} rebuilt as partial")
    if live:
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
