"""surface_subgroup_schema_2292_v1_20261025.py -- escalation #2292 (#2286 build plan U2, approved #2286 v38 and v41;
outputs/escalation/2286-build-plan-v4-20261025.md sections 2, 3 and 6).

1. surface_subgroup: one row per (cluster, Strong's code, surface) pair, with its subgroup, the two-sense flag (C2),
   provisional status (C3), who allocated it (B1, B5) and the reason (behaviour rules B:117, B:118). Unique among live
   rows on (cluster_code, strong, surface).
2. cluster_subgroup.kind (cfg_enum cluster_subgroup.kind: group, qualifier, not_this_sense, anomaly; B2, B3, E4). The
   existing 13 subgroups of M49, M67 and M83 take 'group' (B5).
3. ib_node.verse_lexical_id: the occurrence a node reads (S3, B:121), with its index. Filled by #2296 (U6).
4. The enums surface_subgroup.status and surface_subgroup.allocated_by.

Write grants come with the steps that write the table (#2293 cluster.surface_map, #2296 reading.apply).
Tables and columns are built from their cfg_column rows (lib/db.table_ddl; ALTER for the added columns).
cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.
One transaction.

Usage:
    python iba/app/migration/surface_subgroup_schema_2292_v1_20261025.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2292-SURFACE-SUBGROUP-SCHEMA-20261025"
MODULE = "surface_subgroup_schema_2292_v1_20261025"
SOURCE = "escalation #2292 (#2286 U2; outputs/escalation/2286-build-plan-v4-20261025.md)"
FILLED = "iba/app/lib/surfacemap.py (#2293, cluster.surface_map); reading.apply (#2296) for a move"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None, filled=FILLED):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": filled, "inactive": 0}


T = "surface_subgroup"
GRAIN = "one row per (cluster, Strong's code, surface) pair"
USE = ("#2286 E2 (#2292): the subgroup each (code, surface) pair of an M cluster belongs to, made in bulk at the "
       "clustering stage (behaviour rules B:117, B:118). Provisional, never a finding; a two-sense pair is flagged and "
       "settled per occurrence in the claims step (B:122). Surface to verse stays in verse_lexical")
COLS = [
    col(T, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
    col(T, "cluster_code", 1, "TEXT", "the M cluster the code is in (cluster_strong); checked against it so a code "
        "that leaves the cluster leaves stale pairs (C5, #2294)", nn=1, fk="cluster.cluster_code"),
    col(T, "strong", 2, "TEXT", "the lettered Strong's code as it occurs in verse_lexical (B:113)", nn=1,
        fk="strong.strongNumber"),
    col(T, "surface", 3, "TEXT", "verse_lexical.surface, lower-cased and trimmed: the key a verse_lexical row is "
        "matched on with its strong", nn=1),
    col(T, "cluster_subgroup_id", 4, "INTEGER", "the subgroup the pair belongs to, of any kind: group, qualifier, "
        "not_this_sense or the cluster's anomaly group (C4)", nn=1, fk="cluster_subgroup.id"),
    col(T, "two_sense", 5, "INTEGER", "1 when the pair carries two senses: settled per occurrence in the claims step "
        "(C2, B:122)", nn=1, dflt="0"),
    col(T, "status", 6, "TEXT", "provisional (C3), or moved once the claims step has moved the pair", nn=1,
        dflt="'provisional'", exp="enum.surface_subgroup.status"),
    col(T, "allocated_by", 7, "TEXT", "who placed the pair: inherited (an existing subgroup, B5), session (Claude, the "
        "head), api (the tail), reading (a claims-step move) or manual (an anomaly cleared by hand)", nn=1,
        exp="enum.surface_subgroup.allocated_by"),
    col(T, "reason", 8, "TEXT", "why the pair is in this subgroup (C1); on a move, the settlement observation it "
        "cites", nn=1),
    col(T, "run_id", 9, "TEXT", "the run that wrote the row"),
    col(T, "created_at", 10, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
    col(T, "updated_at", 11, "TEXT", "when last changed (ISO-8601 UTC)"),
    col(T, "created_by", 12, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    col(T, "deleted", 13, "INTEGER", "soft delete: 1 when the pair is no longer live", nn=1, dflt="0"),
]
UNIQUE = ["cluster_code", "strong", "surface"]
INDEXES = [("idx_surface_subgroup_subgroup", ["cluster_subgroup_id"]),
           ("idx_surface_subgroup_strong_surface", ["strong", "surface"])]

SG_KIND = col("cluster_subgroup", "kind", 14, "TEXT", "#2286 B3 (#2292): group (a surface group), qualifier (its "
              "uses mainly qualify: never a home scope, E4), not_this_sense (pairs whose sense is not the "
              "cluster's), or anomaly (the cluster's bucket of pairs and nodes cleared by hand, B2, B6)", nn=1,
              dflt="'group'", exp="enum.cluster_subgroup.kind", filled=FILLED)
SG_USE = ("A cluster's subgroups (#2286): groups of (code, surface) pairs held in surface_subgroup, each with its kind. "
          "The 13 made by the retired cluster.subgroup pipeline for M49, M67 and M83 are kept as kind group (B5)")
NODE_COL = col("ib_node", "verse_lexical_id", 17, "INTEGER", "#2286 S3 (#2292): the occurrence the node reads, one "
               "verse_lexical row; NULL until #2296 fills it. A node that matches more than one occurrence goes to its "
               "cluster's anomaly group (B6)", fk="verse_lexical.id", filled="reading.record (#2296)")
NODE_INDEX = ("idx_ib_node_verse_lexical_id", "verse_lexical_id")
ENUMS = {"cluster_subgroup.kind": ["group", "qualifier", "not_this_sense", "anomaly"],
         "surface_subgroup.status": ["provisional", "moved"],
         "surface_subgroup.allocated_by": ["inherited", "session", "api", "reading", "manual"]}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", T):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": T, "grain": GRAIN, "use": USE,
                                                "inactive": 0, "category": "data"}))
    for c in COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", T, c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for i, c in enumerate(UNIQUE):
        if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", T, c):
            ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": T, "col": c, "ordinal": i}))
    for name, cols in INDEXES:
        for i, c in enumerate(cols):
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", T, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": T, "name": name, "col": c, "ordinal": i}))
    for c in (SG_KIND, NODE_COL):
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", c["table_name"],
                   c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    if one("SELECT use FROM cfg_table WHERE database='iba' AND name='cluster_subgroup'")[0] != SG_USE:
        ops.append(("cfg_table", "update", {"database": "iba", "name": "cluster_subgroup"}, {"use": SG_USE}))
    if not has("SELECT 1 FROM cfg_index WHERE table_name='ib_node' AND name=?", NODE_INDEX[0]):
        ops.append(("cfg_index", "insert", {}, {"table_name": "ib_node", "name": NODE_INDEX[0], "col": NODE_INDEX[1],
                                                "ordinal": 0}))
    for name, values in ENUMS.items():
        for i, v in enumerate(values):
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": i, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2292 (#2286 U2): table surface_subgroup, "
                       f"cluster_subgroup.kind, ib_node.verse_lexical_id, their enums; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    cols = {t: {r[1] for r in conn.execute(f"PRAGMA table_info({t})")} for t in ("cluster_subgroup", "ib_node")}
    print(f"{len(ops)} cfg write(s); {T} live: {T in live}")
    if a.dry_run:
        for t, op, where, set_ in ops:
            what = (set_.get("name") or set_.get("value") or set_.get("module") or set_.get("col")
                    or json.dumps(where))
            print(f"  {op:6} {t:18} {set_.get('table_name', '')} {what}")
        return 0
    try:
        conn.execute("SAVEPOINT surface_subgroup_schema")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if T not in live:
            create_sql, index_sql = table_ddl(cfg, T)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        if "kind" not in cols["cluster_subgroup"]:
            conn.execute("ALTER TABLE cluster_subgroup ADD COLUMN kind TEXT NOT NULL DEFAULT 'group'")
        if "verse_lexical_id" not in cols["ib_node"]:
            conn.execute('ALTER TABLE ib_node ADD COLUMN verse_lexical_id INTEGER REFERENCES "verse_lexical"("id")')
        conn.execute(f'CREATE INDEX IF NOT EXISTS "{NODE_INDEX[0]}" ON ib_node("{NODE_INDEX[1]}")')
        conn.execute("RELEASE surface_subgroup_schema")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_subgroup_schema")
        conn.execute("RELEASE surface_subgroup_schema")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
