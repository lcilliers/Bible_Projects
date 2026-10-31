"""concept_tables_2339_v1_20261031.py -- escalation #2339 (researcher, chat 2026-10-31: "Build v1 tables").

Builds three tables for the v1 concept grouping and loads it from iba/docs/concept-mapping-spec-v1-20261031.json:
  concept_domain    one row per domain (a chapter of the narrative); narrative_chapter_id stays NULL until the
                    narrative is rebuilt on the domains
  concept           one row per concept (a sub-chapter), in a domain; narrative_section_id stays NULL likewise
  concept_subgroup  one row per (concept, cluster_subgroup): the live group or qualifier subgroups, each in exactly
                    one live concept (partial unique index on cluster_subgroup_id)
Tables and columns are built from their cfg_column rows (lib/db.table_ddl). cfg_* writes through
configmaint.apply_logged(); the data rows are written by this migration (writer 'migration'). The load is refused,
before any write, unless the spec names every live group and qualifier subgroup of cluster_subgroup exactly once,
with the id and code agreeing. Registers itself (inactive, at its own archive path). Idempotent. One transaction.

Usage:
    python iba/app/migration/concept_tables_2339_v1_20261031.py [--db PATH] [--spec PATH] [--dry-run]
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
DEFAULT_SPEC = ROOT / "iba" / "docs" / "concept-mapping-spec-v1-20261031.json"
RUN_ID = "DEVMODE-2339-CONCEPT-TABLES-20261031"
MODULE = "concept_tables_2339_v1_20261031"
SOURCE = "escalation #2339 (researcher: Build v1 tables, chat 2026-10-31; iba/docs/concept-mapping-spec-v1-20261031.json)"
FILLED = f"iba/app/migration/archive/{MODULE}.py (the v1 load); no step writes the table yet"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": None, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


def tail(table, start):
    return [col(table, "run_id", start, "TEXT", "the run that wrote the row"),
            col(table, "created_at", start + 1, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
            col(table, "updated_at", start + 2, "TEXT", "when last changed (ISO-8601 UTC)"),
            col(table, "created_by", start + 3, "TEXT", WHO, nn=1, dflt="'direct edit'"),
            col(table, "deleted", start + 4, "INTEGER", "soft delete: 1 when the row is no longer live", nn=1,
                dflt="0")]


D, C, S = "concept_domain", "concept", "concept_subgroup"
TABLES = {
    D: ("one row per domain of the concept grouping",
        "#2339: a domain of the concept grouping, which the researcher ruled is the new basis for the narrative, "
        "domains as chapters and concepts as sub-chapters (chat 2026-10-31). Loaded from the v1 spec "
        "iba/docs/concept-mapping-spec-v1-20261031.json, made by grouping the existing subgroups; a first grouping, "
        "not a finding. narrative_chapter_id links the domain to the narrative chapter built on it and is NULL until "
        "the narrative is rebuilt on the domains"),
    C: ("one row per concept, in one domain",
        "#2339: a concept of the grouping, a sub-chapter of its domain, named for what its subgroups share; the "
        "concept_subgroup rows say which subgroups it holds. narrative_section_id links it to the narrative section "
        "built on it and is NULL until the narrative is rebuilt on the domains"),
    S: ("one row per (concept, cluster_subgroup) membership",
        "#2339: which concept holds a subgroup of cluster_subgroup (kind group or qualifier). A live subgroup is in "
        "exactly one live concept. This is the link from the base data (cluster_subgroup, then surface_subgroup and "
        "verse_lexical) to the narrative"),
}
COLS = (
    [col(D, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
     col(D, "name", 1, "TEXT", "the domain's name, as in the spec (for example Feeling: anger and grief)", nn=1),
     col(D, "ordinal", 2, "INTEGER", "the domain's order, from 1, as in the spec", nn=1),
     col(D, "narrative_chapter_id", 3, "INTEGER", "the narrative chapter built on this domain; NULL until then",
         fk="narrative_chapter.id")] + tail(D, 4)
    + [col(C, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
       col(C, "domain_id", 1, "INTEGER", "the domain the concept is in", nn=1, fk="concept_domain.id"),
       col(C, "name", 2, "TEXT", "the concept's name, as in the spec (for example Fear, dread, dismay, appalment)",
           nn=1),
       col(C, "ordinal", 3, "INTEGER", "the concept's order within its domain, from 1, as in the spec", nn=1),
       col(C, "narrative_section_id", 4, "INTEGER", "the narrative section built on this concept; NULL until then",
           fk="narrative_section.id")] + tail(C, 5)
    + [col(S, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
       col(S, "concept_id", 1, "INTEGER", "the concept that holds the subgroup", nn=1, fk="concept.id"),
       col(S, "cluster_subgroup_id", 2, "INTEGER", "the subgroup held (cluster_subgroup of kind group or qualifier); "
           "unique among live rows, so a subgroup is in one concept", nn=1, fk="cluster_subgroup.id")] + tail(S, 3))
UNIQUE = {D: ["name"], C: ["domain_id", "name"], S: ["cluster_subgroup_id"]}
INDEXES = {C: [("idx_concept_domain_id", ["domain_id"])], S: [("idx_concept_subgroup_concept_id", ["concept_id"])]}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for t, (grain, use) in TABLES.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": grain, "use": use,
                                                    "inactive": 0, "category": "data"}))
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name=? AND database='iba'", t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": "migration", "table_name": t, "database": "iba",
                                                          "inactive": 0}))
        for i, c in enumerate(UNIQUE[t]):
            if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", t, c):
                ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": t, "col": c, "ordinal": i}))
        for name, cols in INDEXES.get(t, []):
            for i, c in enumerate(cols):
                if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", t, name, c):
                    ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": c, "ordinal": i}))
    for c in COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", c["table_name"],
                   c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2339: tables {D}, {C}, {S} and the load of the v1 concept "
                       f"grouping; run_id {RUN_ID}."}))
    return ops


def check_spec(conn, spec) -> list[str]:
    """Refusals, before any write: the spec must name every live group and qualifier subgroup exactly once."""
    bad = []
    live = {r[0]: r[1] for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup WHERE kind IN ('group','qualifier') AND delete_flagged=0")}
    seen = {}
    for d in spec["domains"]:
        for k in d["concepts"]:
            if len(k["subgroup_ids"]) != len(k["subgroup_codes"]):
                bad.append(f"concept {k['concept']!r}: ids and codes differ in length")
            for i, cd in zip(k["subgroup_ids"], k["subgroup_codes"]):
                if i not in live:
                    bad.append(f"subgroup id {i} ({cd}) is not a live group or qualifier subgroup")
                elif live[i] != cd:
                    bad.append(f"subgroup id {i}: spec code {cd} but cluster_subgroup has {live[i]}")
                if i in seen:
                    bad.append(f"subgroup id {i} is in two concepts: {seen[i]!r} and {k['concept']!r}")
                seen[i] = k["concept"]
    for i in sorted(set(live) - set(seen)):
        bad.append(f"live subgroup id {i} ({live[i]}) is in no concept")
    return bad


def load(conn, spec) -> tuple[int, int, int]:
    nd = nc = ns = 0
    for d in spec["domains"]:
        cur = conn.execute("INSERT INTO concept_domain (name, ordinal, run_id, created_by) VALUES (?,?,?,'migration')",
                           (d["domain"], d["ordinal"], RUN_ID))
        nd += 1
        for k in d["concepts"]:
            cc = conn.execute("INSERT INTO concept (domain_id, name, ordinal, run_id, created_by) "
                              "VALUES (?,?,?,?,'migration')", (cur.lastrowid, k["concept"], k["ordinal"], RUN_ID))
            nc += 1
            for sid in k["subgroup_ids"]:
                conn.execute("INSERT INTO concept_subgroup (concept_id, cluster_subgroup_id, run_id, created_by) "
                             "VALUES (?,?,?,'migration')", (cc.lastrowid, sid, RUN_ID))
                ns += 1
    return nd, nc, ns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--spec", default=str(DEFAULT_SPEC))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    spec = json.load(open(a.spec, encoding="utf-8"))
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if D in live and conn.execute(f"SELECT count(*) FROM {D} WHERE deleted=0").fetchone()[0]:
        print("already applied: concept_domain holds live rows; nothing changed")
        return 0
    refusals = check_spec(conn, spec)
    if refusals:
        print("REFUSED, nothing written:")
        for r in refusals[:40]:
            print("  " + r)
        return 2
    ops = plan(conn)
    n = (len(spec["domains"]), sum(len(d["concepts"]) for d in spec["domains"]),
         sum(len(k["subgroup_ids"]) for d in spec["domains"] for k in d["concepts"]))
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); tables to create: {[t for t in TABLES if t not in live]}; "
              f"rows to load: {n[0]} domains, {n[1]} concepts, {n[2]} concept_subgroup")
        for t, op, where, set_ in ops:
            what = set_.get("name") or set_.get("module") or set_.get("col") or json.dumps(where)
            print(f"  {t} {op} {set_.get('table_name', '')} {what}")
        return 0
    try:
        conn.execute("SAVEPOINT concept_tables")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for t in TABLES:
            if t not in live:
                create_sql, index_sql = table_ddl(cfg, t)
                conn.execute(create_sql)
                for sql in index_sql:
                    conn.execute(sql)
        got = load(conn, spec)
        if got != n:
            raise RuntimeError(f"loaded {got}, expected {n}")
        conn.execute("RELEASE concept_tables")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO concept_tables")
        conn.execute("RELEASE concept_tables")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); loaded {got[0]} domains, {got[1]} concepts, "
          f"{got[2]} concept_subgroup")
    return 0


if __name__ == "__main__":
    sys.exit(main())
