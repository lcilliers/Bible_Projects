"""ib_node_cluster_nullable_2495_v1_20261113.py -- escalation #2495: cluster and subgroup play no part in nodes and observations (researcher, 2026-11-13:
'notes and observations should not have any part to play with clusters and sub groups').

ib_node.cluster_code was NOT NULL, so every writer had to give a node a cluster. It becomes nullable: a new node carries none, and the live nodes keep the cluster
they hold as history. Rebuilt by the SQLite table-rebuild procedure (new table, copy, drop, rename, indexes), inside one transaction with foreign keys off; the row count,
a checksum of every column and the foreign-key check must agree before and after, or the whole run is rolled back. cfg_column text restated (cluster_code and
cluster_subgroup_code are history, written by no process); cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage: python -m iba.app.migration.ib_node_cluster_nullable_2495_v1_20261113 [--db PATH] [--dry-run]"""
import argparse
import hashlib
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2495-NODE-CLUSTER-NULLABLE-20261113"
MODULE = "ib_node_cluster_nullable_2495_v1_20261113"
USE_CLUSTER = ("History: the word's cluster at the time the node was written. Written by no process since 2026-11-13 (researcher, #2484 ruling 4.4: clusters and subgroups "
               "served to establish the collections and play no part in nodes and observations); a new node holds none. Reports read the collection (collection_id).")
USE_SUBGROUP = ("History: the word's subgroup at the time the node was written. Written by no process since 2026-11-13 (#2495); reports read the collection (collection_id).")


def checksum(conn, table):
    h = hashlib.sha256()
    n = 0
    for row in conn.execute(f"SELECT * FROM {table} ORDER BY id"):
        h.update(repr(tuple(row)).encode("utf-8"))
        n += 1
    return n, h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db, isolation_level=None)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    old_sql = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='ib_node'").fetchone()[0]
    if "cluster_code            TEXT NOT NULL" not in old_sql:
        print("ib_node.cluster_code is not NOT NULL: nothing to rebuild")
        return 1
    new_sql = old_sql.replace("cluster_code            TEXT NOT NULL", "cluster_code            TEXT NULL", 1).replace("CREATE TABLE ib_node (", "CREATE TABLE ib_node_new (", 1)
    indexes = [r[0] for r in conn.execute("SELECT sql FROM sqlite_master WHERE type='index' AND tbl_name='ib_node' AND sql IS NOT NULL")]
    before = checksum(conn, "ib_node")
    print(f"ib_node: {before[0]} rows; {len(indexes)} index(es) to recreate")
    if a.dry_run:
        print("DRY RUN: nothing written")
        return 0
    conn.execute("PRAGMA foreign_keys=OFF")
    conn.execute("BEGIN")
    try:
        conn.execute(new_sql)
        conn.execute("INSERT INTO ib_node_new SELECT * FROM ib_node")
        conn.execute("DROP TABLE ib_node")
        conn.execute("ALTER TABLE ib_node_new RENAME TO ib_node")
        for sql in indexes:
            conn.execute(sql)
        after = checksum(conn, "ib_node")
        if after != before:
            raise RuntimeError(f"ib_node changed in the rebuild: before {before}, after {after}")
        bad = conn.execute("PRAGMA foreign_key_check(ib_node)").fetchall()
        if bad:
            raise RuntimeError(f"foreign key check: {len(bad)} problem(s), e.g. {bad[:3]}")
        apply_logged(conn, RUN_ID, "cfg_column", "update", {"database": "iba", "table_name": "ib_node", "name": "cluster_code"}, {"notnull": 0, "use": USE_CLUSTER})
        apply_logged(conn, RUN_ID, "cfg_column", "update", {"database": "iba", "table_name": "ib_node", "name": "cluster_subgroup_code"}, {"use": USE_SUBGROUP})
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
                "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                "purpose": f"ONE-OFF migration -- escalation #2495: ib_node.cluster_code made nullable (table rebuild, checksum verified); run_id {RUN_ID}."})
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        conn.execute("PRAGMA foreign_keys=ON")
        raise
    conn.execute("PRAGMA foreign_keys=ON")
    print(f"rebuilt: {after[0]} rows, checksum {after[1][:16]} unchanged; cluster_code is nullable (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
