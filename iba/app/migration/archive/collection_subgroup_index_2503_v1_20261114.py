"""collection_subgroup_index_2503_v1_20261114.py -- escalation #2503 (researcher, 2026-11-14, under #2463: "Approve, build it"; design
outputs/escalation/2463-collection-subgroup-index-design-v1-20261114.md).

Builds two tables from their cfg_column rows (lib/db.table_ddl):
  collection_subgroup          a group of surfaces inside one collection (the layer 1 concept), with a status
  collection_subgroup_surface  the index: one live row for each member surface of a confirmed collection, with its subgroup and a state (unplaced, placed, isolated);
                               strong is empty for the whole surface and a Strong's code on a surface split between groups
and registers them: cfg_table, cfg_column, cfg_unique, cfg_index, cfg_write_grant, cfg_enum (the statuses, states, the new surface_event actions and subject kinds), cfg_setting
(collection.index_check_name), the steps collection.index, collection.subgroup and collection.index_check with their routed condition, the library collectionindex and this migration.
All cfg_* writes through configmaint.apply_logged(). The tables are created empty: the first fill is the step collection.index. A named rollback snapshot is taken before a live apply.
Idempotent. One transaction.

Usage:
    python iba/app/migration/collection_subgroup_index_2503_v1_20261114.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2503-COLLECTION-SUBGROUP-INDEX-20261114"
MODULE = "collection_subgroup_index_2503_v1_20261114"
SOURCE = "escalation #2503 (researcher: Approve, build it, 2026-11-14; outputs/escalation/2463-collection-subgroup-index-design-v1-20261114.md)"
FILLED = "Collection-Build.ps1 -Action Index (the fill) and -Action Subgroup (groups and placements), lib/collectionindex.py"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"
G, I = "collection_subgroup", "collection_subgroup_surface"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ, "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


def tail(table, start):
    return [col(table, "run_id", start, "TEXT", "the run that wrote the row"),
            col(table, "created_at", start + 1, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
            col(table, "updated_at", start + 2, "TEXT", "when last changed (ISO-8601 UTC)"),
            col(table, "created_by", start + 3, "TEXT", WHO, nn=1, dflt="'direct edit'"),
            col(table, "deleted", start + 4, "INTEGER", "soft delete: 1 when the row is no longer live", nn=1, dflt="0")]


TABLES = {
    G: ("one row per subgroup of one collection",
        "#2503: a subgroup of the surfaces of one collection, formed in the layer 1 reading (for example starting, weighing, meditation in the collection thought). It is the group of surfaces that do the same "
        "thing for the inner being; its definition and the Strong's enrichment of it are layer 1 observations found through their nodes, not columns here. A subgroup belongs to one collection and is "
        "not a cluster subgroup (cluster_subgroup and surface_subgroup are the retired cluster allocation and are not read or changed by it). A change is a soft delete and a new row, and a surface_event"),
    I: ("one row per (collection, surface) or, for a surface split between groups, per (collection, surface, Strong's code)",
        "#2503: the index of the surfaces of the confirmed collections and the subgroup each is placed in. One live row for each member surface (the surface is a member by the one rule of the evidence report: "
        "its own link in a member tier, else the link of its base; each surface is in exactly one collection, B:129). state: unplaced (in the index, no subgroup yet), placed (in subgroup_id), isolated (no "
        "inner-being role: bound to its partner or excluded). strong is empty for the whole surface; when a surface has senses placed in different subgroups it has one row for each Strong's code it carries in "
        "the verses and none for the whole surface. A node reaches its subgroup by collection_id, surface and strong. The first fill is mechanical (Collection-Build.ps1 -Action Index); a placement is the researcher's instruction with a reason"),
}
COLS = (
    [col(G, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
     col(G, "collection_id", 1, "INTEGER", "the collection this subgroup is in", nn=1, fk="collection.id"),
     col(G, "name", 2, "TEXT", "what the subgroup is (for example starting, weighing, meditation); unique among the live subgroups of the collection", nn=1),
     col(G, "status", 3, "TEXT", "indicative (made, not reviewed), confirmed (the researcher confirmed it), retired", nn=1, dflt="'indicative'", exp="enum.collection_subgroup.status"),
     col(G, "note", 4, "TEXT", "the researcher's instruction or the reading's note that made the subgroup (quoted, with the escalation id)")] + tail(G, 5)
    + [col(I, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
       col(I, "collection_id", 1, "INTEGER", "the collection the surface is a member of", nn=1, fk="collection.id"),
       col(I, "term_id", 2, "INTEGER", "the surface: surface_term.id (the same text key as verse_lexical.surface)", nn=1, fk="surface_term.id"),
       col(I, "strong", 3, "TEXT", "empty: the whole surface; a Strong's code: only that sense of the surface (the surface is split between subgroups). When one row of a surface has a code every live row of it has one", fk="strong.strongNumber"),
       col(I, "subgroup_id", 4, "INTEGER", "the subgroup the surface (or sense) is placed in; empty while unplaced or isolated", fk="collection_subgroup.id"),
       col(I, "state", 5, "TEXT", "unplaced (in the index, no subgroup), placed (in subgroup_id), isolated (no inner-being role: bound to its partner or excluded)", nn=1, dflt="'unplaced'",
           exp="enum.collection_subgroup_surface.state"),
       col(I, "reason", 6, "TEXT", "why: 'index fill' for the mechanical fill, else the researcher's instruction, quoted, with the escalation id")] + tail(I, 7))
UNIQUE = {G: ["collection_id", "name"], I: ["collection_id", "term_id", "strong"]}
INDEXES = {G: [("idx_collection_subgroup_collection", ["collection_id"])],
           I: [("idx_collection_subgroup_surface_subgroup", ["subgroup_id"]), ("idx_collection_subgroup_surface_term", ["term_id"]), ("idx_collection_subgroup_surface_collection", ["collection_id"])]}
ENUMS = {"collection_subgroup.status": ["indicative", "confirmed", "retired"],
         "collection_subgroup_surface.state": ["unplaced", "placed", "isolated"],
         "surface_event.action": ["subgroup_make", "subgroup_place", "subgroup_isolate", "index_retire"],
         "surface_subject_kind": ["collection_subgroup", "collection_subgroup_surface"]}
SETTING = ("collection.index_check_name", "collection-index-check",
           "the file name stem of the report of the collection index check (#2503): <stem>-v<n>-<yyyymmdd>.md under surfaces.exports_root, versioned by the filing rule", "collection")
STEPS = [
    ("collection-build", 11, "collection.index", "iba.app.handlers.collectionbuild:index_fill", "none",
     "fill the index of the surfaces of the confirmed collections (#2503): one live row for each member surface, unplaced; a row whose surface left its collection is retired; mechanical, -Check previews -- see lib/collectionindex.py", "operations"),
    ("collection-build", 12, "collection.subgroup", "iba.app.handlers.collectionbuild:subgroup", "none",
     "make a subgroup of a collection (-Collection, -Name, -Reason), place surfaces in it (-Surface, -Name, -Strong, -Reason) or isolate surfaces with no inner-being role (-Surface, -Isolate, -Reason), on the researcher's instruction, each with a surface_event; -Check previews -- see lib/collectionindex.py (escalation #2503)", "operations"),
    ("collection-build", 13, "collection.index_check", "iba.app.handlers.collectionbuild:index_check", "none",
     "check the index of the collection surfaces (#2503): member surfaces with no row, rows of surfaces that left, a surface in two collections, duplicates, the split rule, placements that do not agree, shared flags without a second link; read-only on the tables, writes a versioned Markdown report under surfaces.exports_root -- see lib/collectionindex.py", "utility"),
]
GRANTS = [("migration", G), ("migration", I), ("collection.index", I), ("collection.index", "surface_event"), ("collection.subgroup", G), ("collection.subgroup", I), ("collection.subgroup", "surface_event")]
ON_FAIL = [(s[2], "refused", "report-continue", None, "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)", "terminal", 0) for s in STEPS]
UTILITIES = [
    ("collectionindex", "iba/app/lib/collectionindex.py", 0,
     "collectionindex.py -- the index of the surfaces of each confirmed collection and their subgroups (escalation #2503): the fill, the subgroups and placements, and the checker.", 1,
     "the member tiers, the report name and the folder are read from cfg_setting; the code holds no tunable value"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2503: the tables {G} and {I} and their registration; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for t, (grain, use) in TABLES.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": grain, "use": use, "inactive": 0, "category": "data"}))
        for i, c in enumerate(UNIQUE[t]):
            if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", t, c):
                ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": t, "col": c, "ordinal": i}))
        for name, cols in INDEXES.get(t, []):
            for i, c in enumerate(cols):
                if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", t, name, c):
                    ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": c, "ordinal": i}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    for c in COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", c["table_name"], c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for name, values in ENUMS.items():
        top = conn.execute("SELECT coalesce(max(ordinal),-1) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        for v in values:
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                top += 1
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": top, "inactive": 0}))
    key, value, use, module = SETTING
    if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
        ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    for wp, ordinal, step, handler, scope, does, kind in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": wp, "ordinal": ordinal, "step": step, "handler": handler, "scope": scope, "does": does, "inactive": 0, "kind": kind}))
    for step, cond, path, resolver, message, route, inactive in ON_FAIL:
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path, "resolver": resolver, "message": message, "route": route, "inactive": inactive}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt, "config_exempt_reason": reason,
                                                      "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); tables to create: {[t for t in TABLES if t not in live]}")
        for t, op, where, set_ in ops:
            print(" ", t, op, set_.get("name") or set_.get("module") or set_.get("step") or set_.get("key") or set_.get("table_name"), set_.get("value", ""))
        return 0
    if not ops and all(t in live for t in TABLES):
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2503-collection-subgroup-index', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_subgroup_index")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for t in TABLES:
            if t not in live:
                create_sql, index_sql = table_ddl(cfg, t)
                conn.execute(create_sql)
                for sql in index_sql:
                    conn.execute(sql)
        conn.execute("RELEASE collection_subgroup_index")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_subgroup_index")
        conn.execute("RELEASE collection_subgroup_index")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); tables created: {[t for t in TABLES if t not in live]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
