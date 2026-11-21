"""clear_thought_grouping_2528_v1_20261121.py -- escalation #2528 (build brief B2; researcher ruling on #2515 Q3: nothing previously done stands).

The grouping of the collection thought was withdrawn. This migration returns the collection to the state before stage 2:
  - the live subgroups of thought are retired (collection_subgroup deleted=1, status retired), each with a surface_event;
  - every live index row of thought (collection_subgroup_surface: placed, isolated, and the rows split by Strong's code) is soft deleted with an event, and the
    index fill (lib/collectionindex.fill) then makes one whole-surface unplaced row for each member surface, as it does for any collection;
  - the group on every live node of thought is cleared (lib/collectionindex.refresh_nodes), each change kept with its reason in ib_observation_change.
No step S1 ledger row, no observation and no node is deleted. Idempotent: a second run finds nothing to change.

Usage:
    python iba/app/migration/clear_thought_grouping_2528_v1_20261121.py [--db PATH] [--dry]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-CLEAR-THOUGHT-GROUPING-20261121"
COLLECTION = "thought"
REASON = "researcher ruling on #2515 Q3 (nothing previously done stands): the grouping of thought is withdrawn and the collection returns to its state before stage 2 (#2528 B2)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    cid = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (COLLECTION,)).fetchone()[0]
    groups = conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0", (cid,)).fetchall()
    rows = conn.execute("SELECT id, state, subgroup_id, strong FROM collection_subgroup_surface WHERE collection_id=? AND deleted=0", (cid,)).fetchall()
    nodes = conn.execute("SELECT count(*) FROM ib_node WHERE deleted=0 AND collection_id=? AND subgroup_id IS NOT NULL", (cid,)).fetchone()[0]
    print(f"before: {len(groups)} live subgroups, {len(rows)} live index rows, {nodes} nodes carrying a group")
    if a.dry:
        print("dry run: nothing written")
        return 0
    needs = bool(groups) or any(r[1] != "unplaced" or r[3] is not None for r in rows) or nodes
    if not needs:
        print("nothing to change")
        return 0
    with conn:
        for gid, name in groups:
            conn.execute("UPDATE collection_subgroup SET deleted=1, status='retired', updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (RUN_ID, gid))
            ci._event(conn, RUN_ID, "collection_subgroup", gid, "subgroup_retire", "deleted", "0", "1", f"{name}: {REASON}")
        for rid, state, gid, strong in rows:
            conn.execute("UPDATE collection_subgroup_surface SET deleted=1, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=?, reason=? WHERE id=?", (RUN_ID, REASON, rid))
            ci._event(conn, RUN_ID, "collection_subgroup_surface", rid, "index_reset", "state", state, "retired", REASON)
        fill = ci.fill(conn, cfg, RUN_ID)
        ref = ci.refresh_nodes(conn, RUN_ID, collection_id=cid)
    after = conn.execute("SELECT state, count(*), sum(strong IS NOT NULL), sum(subgroup_id IS NOT NULL) FROM collection_subgroup_surface WHERE collection_id=? AND deleted=0 GROUP BY 1", (cid,)).fetchall()
    print(f"fill: {fill}; nodes: {ref}; index after: {[tuple(r) for r in after]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
