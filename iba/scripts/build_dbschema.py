"""build_dbschema.py -- capture a database's schema into its DBSchema register.

Reads a database READ-ONLY and writes iba/config/DBSchema/<file>.json: every table,
column, primary key, foreign key, check constraint, index (with its columns),
trigger and view -- plus a per-column PROFILE of the live data, which is what the
descriptions are derived from.

The database list is config, not code: iba/config/utility/DBSchema_maintenance.json
-> ent.dbschema.database.spec.databases.  Pointing this at the new IBA database is
an entry there, not an edit here.

Rules it implements (all from DBSchema_maintenance.json):
    dbschema.from-the-live-db      -- read the DB, never a prior document
    dbschema.description-from-data -- profile the values; the profile stays beside
                                      the description so it is checkable
    dbschema.preserve-descriptions -- a rebuild carries descriptions across, matched
                                      on (table, column) BY NAME, never by position
    dbschema.retire-never-delete   -- a dropped object moves to `retired`
    dbschema.read-only-source      -- file:...?mode=ro, always

Usage:
    python iba/scripts/build_dbschema.py --db bible_research
    python iba/scripts/build_dbschema.py --db bible_research --dry-run
    python iba/scripts/build_dbschema.py --db bible_research --verify
    python iba/scripts/build_dbschema.py --list
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent   # project root
CONFIG = ROOT / "iba" / "config"
MAINT = CONFIG / "utility" / "DBSchema_maintenance.json"

# from dbschema.description-from-data spec
CATEGORICAL_CUTOFF = 200
EXACT_BELOW_ROWS = 50_000
TOP_N = 8


# ── the database list (config, not code) ─────────────────────────────────────
def databases() -> dict[str, dict]:
    doc = json.loads(MAINT.read_text(encoding="utf-8"))
    for item in doc["entities"]:
        if item["id"] == "ent.dbschema.database":
            return {d["code"]: d for d in item["spec"]["databases"]}
    raise SystemExit("ent.dbschema.database not found in DBSchema_maintenance.json")


def connect(path: pathlib.Path) -> sqlite3.Connection:
    """dbschema.read-only-source -- reading a schema must never change one."""
    conn = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def schema_version(conn: sqlite3.Connection, entry: dict) -> str:
    src = entry.get("schema_version_source", {})
    if src.get("method") != "table":
        return "unknown"
    try:
        row = conn.execute(src["sql"]).fetchone()
        return row[0] if row else "unknown"
    except sqlite3.Error:
        return "unknown"


# ── structure ────────────────────────────────────────────────────────────────
def q(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def parse_checks(ddl: str) -> list[str]:
    """CHECK clauses, balanced-paren extracted from the DDL.

    They exist nowhere else: SQLite has no PRAGMA for check constraints, which is
    why the previous exporter never captured them -- they survived only as text
    inside the CREATE TABLE string, where nothing can query them.
    """
    out = []
    for m in re.finditer(r"\bCHECK\s*\(", ddl, re.IGNORECASE):
        i, depth = m.end(), 1
        while i < len(ddl) and depth:
            depth += (ddl[i] == "(") - (ddl[i] == ")")
            i += 1
        out.append(ddl[m.end():i - 1].strip())
    return out


def table_structure(conn: sqlite3.Connection, table: str) -> dict:
    info = conn.execute(f"PRAGMA table_info({q(table)})").fetchall()
    ddl = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone()[0] or ""

    columns = [{
        "name": c["name"],
        "type": c["type"],
        "notnull": bool(c["notnull"]),
        "default": c["dflt_value"],
        "pk": bool(c["pk"]),           # PRAGMA field 5 -- the old exporter read only 1..4
        "description": None,
        "description_source": None,
        "profile": None,
    } for c in info]

    fks = [{
        "column": f["from"],
        "references": f"{f['table']}.{f['to']}" if f["to"] else f["table"],
        "on_delete": f["on_delete"],
        "on_update": f["on_update"],
    } for f in conn.execute(f"PRAGMA foreign_key_list({q(table)})").fetchall()]

    indexes = []
    for idx in conn.execute(f"PRAGMA index_list({q(table)})").fetchall():
        cols = [r["name"] for r in
                conn.execute(f"PRAGMA index_info({q(idx['name'])})").fetchall()]
        indexes.append({
            "name": idx["name"],
            "unique": bool(idx["unique"]),
            "columns": cols,                       # never captured before
            "origin": idx["origin"],               # c=CREATE INDEX, u=UNIQUE, pk=PK
        })

    return {
        "description": None,
        "description_source": None,
        "row_count": conn.execute(f"SELECT COUNT(*) FROM {q(table)}").fetchone()[0],
        "sql": ddl,
        "primary_key": [c["name"] for c in sorted(
            (c for c in info if c["pk"]), key=lambda c: c["pk"])],
        "columns": columns,
        "foreign_keys": fks,
        "checks": parse_checks(ddl),
        "indexes": indexes,
    }


# ── profiling (dbschema.description-from-data) ───────────────────────────────
def bucket_null(rate: float) -> str:
    if rate == 0:
        return "none"
    if rate == 1:
        return "all"
    return "under-50pct" if rate < 0.5 else "over-50pct"


def clip(v, n: int = 120):
    """A profile is evidence, not a data dump.

    Some TEXT columns hold whole paragraphs (word_registry.description) or big JSON
    blobs (strongs_list); their min/max and top values would otherwise bloat the
    register past the point anyone reads it. Enough to recognise the shape, no more.
    """
    if not isinstance(v, str) or len(v) <= n:
        return v
    return v[:n] + f"… (+{len(v) - n} chars)"


def bucket_distinct(n: int) -> str:
    if n <= 1:
        return "constant"
    if n == 2:
        return "binary"
    if n <= 10:
        return "2-10"
    if n <= CATEGORICAL_CUTOFF:
        return f"11-{CATEGORICAL_CUTOFF}"
    return "high-cardinality"


def profile_table(conn: sqlite3.Connection, table: str, t: dict) -> None:
    """Pass A: one scan for all columns.  Pass B: top values, categorical only."""
    rows = t["row_count"]
    exact = rows <= EXACT_BELOW_ROWS
    stride = 1 if exact else -(-rows // EXACT_BELOW_ROWS)   # ceil
    sample = None if exact else f"rowid % {stride} = 0"
    where = f" WHERE {sample}" if sample else ""
    names = [c["name"] for c in t["columns"]]

    if rows == 0:
        for c in t["columns"]:
            c["profile"] = {"scope": "exact", "rows_scanned": 0, "empty_table": True}
        return

    # Pass A -- ONE table scan covering every column, not one scan per column.
    sel = ["COUNT(*)"]
    for n in names:
        sel += [f"COUNT({q(n)})", f"COUNT(DISTINCT {q(n)})",
                f"MIN({q(n)})", f"MAX({q(n)})"]
    row = conn.execute(f"SELECT {', '.join(sel)} FROM {q(table)}{where}").fetchone()

    scanned = row[0]
    for i, c in enumerate(t["columns"]):
        non_null, distinct, mn, mx = row[1 + i * 4: 5 + i * 4]
        nulls = scanned - non_null
        rate = round(nulls / scanned, 4) if scanned else 0.0
        c["profile"] = {
            "scope": "exact" if exact else "sampled",
            "rows_scanned": scanned,
            "null_count": nulls,
            "null_rate": rate,
            "null_bucket": bucket_null(rate),
            "distinct_count": distinct,
            "distinct_bucket": bucket_distinct(distinct),
            "min": clip(mn if isinstance(mn, (int, float, str, type(None))) else str(mn)),
            "max": clip(mx if isinstance(mx, (int, float, str, type(None))) else str(mx)),
            "looks_categorical": 0 < distinct <= CATEGORICAL_CUTOFF,
        }
        if not exact:
            c["profile"]["sample_method"] = f"rowid % {stride} = 0 (deterministic stride)"

    # Pass B -- top values only where they can pay.  A near-unique column's top-8
    # is noise; its min/max and distinct ratio already say everything.
    for c in t["columns"]:
        p = c["profile"]
        if not p["looks_categorical"] or p["distinct_count"] == 0:
            continue
        preds = [f"{q(c['name'])} IS NOT NULL"] + ([sample] if sample else [])
        top = conn.execute(
            f"SELECT {q(c['name'])} v, COUNT(*) n FROM {q(table)} "
            f"WHERE {' AND '.join(preds)} GROUP BY 1 ORDER BY n DESC, 1 LIMIT {TOP_N}"
        ).fetchall()
        p["top_values"] = [
            {"v": clip(r["v"] if isinstance(r["v"], (int, float, str)) else str(r["v"])),
             "n": r["n"]} for r in top]
        covered = sum(r["n"] for r in top)
        non_null_scanned = p["rows_scanned"] - p["null_count"]
        p["top_values_cover"] = (round(covered / non_null_scanned, 4)
                                 if non_null_scanned else 0.0)

    # A vocabulary with no CHECK and no FK behind it is convention, not control --
    # worth flagging, because it is exactly what a description should point out.
    #
    # But a VOCABULARY means values that REPEAT.  A column with one distinct value
    # per row (books.name, books.abbreviation) is an identifier, not a vocabulary,
    # and flagging it says nothing.  Require: few distinct values, each used several
    # times over, and no unique index -- a uniquely-indexed column cannot be one.
    constrained = {f["column"] for f in t["foreign_keys"]}
    checks = " ".join(t["checks"])
    unique_cols = {i["columns"][0] for i in t["indexes"]
                   if i["unique"] and len(i["columns"]) == 1}
    for c in t["columns"]:
        p = c["profile"]
        distinct = p.get("distinct_count") or 0
        non_null = p.get("rows_scanned", 0) - p.get("null_count", 0)
        if (p.get("looks_categorical") and distinct > 1 and not c["pk"]
                and c["name"] not in constrained and c["name"] not in checks
                and c["name"] not in unique_cols
                and distinct <= 50 and non_null >= distinct * 3):
            p["uncontrolled_vocabulary"] = True


# ── merge (dbschema.preserve-descriptions / retire-never-delete) ─────────────
def carry_descriptions(old: dict, new: dict) -> dict:
    """Match on (table, column) BY NAME -- never by position.

    A column added mid-table shifts every ordinal after it; a positional merge
    would silently reattach every description to the wrong column, and the file
    would look fine.
    """
    stats = {"kept": 0, "retired_tables": 0, "retired_columns": 0}
    old_tables = old.get("tables", {})

    for name, t in new["tables"].items():
        ot = old_tables.get(name)
        if not ot:
            continue
        if ot.get("description"):
            t["description"] = ot["description"]
            t["description_source"] = ot.get("description_source") or "profiler"
        old_cols = {c["name"]: c for c in ot.get("columns", [])}
        for c in t["columns"]:
            oc = old_cols.get(c["name"])
            if oc and oc.get("description"):
                c["description"] = oc["description"]
                c["description_source"] = oc.get("description_source") or "profiler"
                stats["kept"] += 1
        # columns that have gone from the DB
        gone = [c for n, c in old_cols.items()
                if n not in {x["name"] for x in t["columns"]} and c.get("description")]
        if gone:
            t["retired_columns"] = {
                **(ot.get("retired_columns") or {}),
                **{c["name"]: {**c, "retired_at": new["exported_date"]} for c in gone},
            }
            stats["retired_columns"] += len(gone)

    # tables that have gone from the DB
    gone_tables = {n: t for n, t in old_tables.items() if n not in new["tables"]}
    retired = dict(old.get("retired_tables") or {})
    for n, t in gone_tables.items():
        retired[n] = {**t, "retired_at": new["exported_date"]}
        stats["retired_tables"] += 1
    if retired:
        new["retired_tables"] = retired

    return stats


# ── build ────────────────────────────────────────────────────────────────────
def build(code: str, entry: dict, out_path: pathlib.Path, dry_run: bool) -> dict:
    db_path = ROOT / entry["path"]
    if not db_path.exists():
        raise SystemExit(f"database not found: {db_path}")

    conn = connect(db_path)
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "AND name NOT LIKE 'sqlite_%' ORDER BY name")]

    reg = {
        "database": code,
        "database_path": entry["path"],
        "database_bytes": db_path.stat().st_size,
        "schema_version": schema_version(conn, entry),
        "exported_date": datetime.date.today().isoformat(),
        "captured_by": "iba/scripts/build_dbschema.py",
        "★ what_this_is": (
            "CAPTURED DATA -- the live schema of this database, read from the DB itself. "
            "Not a rulebook: it records what the schema IS, never what it should be. "
            "Rules governing it: iba/config/utility/DBSchema_maintenance.json (util.dbschema). "
            "Every description is derived from the `profile` beside it (dbschema.description-from-data)."
        ),
        "table_count": len(tables),
        "tables": {},
    }

    for i, name in enumerate(tables, 1):
        t = table_structure(conn, name)
        profile_table(conn, name, t)
        reg["tables"][name] = t
        print(f"  [{i:3}/{len(tables)}] {name:42} {t['row_count']:>8,} rows  "
              f"{len(t['columns']):>3} cols", flush=True)

    reg["views"] = {
        r["name"]: {"sql": r["sql"], "description": None, "description_source": None}
        for r in conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='view' ORDER BY name")
    }
    reg["triggers"] = {
        r["name"]: {"table": r["tbl_name"], "sql": r["sql"],
                    "description": None, "description_source": None}
        for r in conn.execute(
            "SELECT name, tbl_name, sql FROM sqlite_master WHERE type='trigger' ORDER BY name")
    }

    counts = {
        "tables": len(tables),
        "columns": sum(len(t["columns"]) for t in reg["tables"].values()),
        "pk_columns": sum(1 for t in reg["tables"].values() for c in t["columns"] if c["pk"]),
        "foreign_keys": sum(len(t["foreign_keys"]) for t in reg["tables"].values()),
        "checks": sum(len(t["checks"]) for t in reg["tables"].values()),
        "indexes": sum(len(t["indexes"]) for t in reg["tables"].values()),
        "triggers": len(reg["triggers"]),
        "views": len(reg["views"]),
    }
    reg["counts"] = counts
    conn.close()

    if out_path.exists():
        old = json.loads(out_path.read_text(encoding="utf-8"))
        stats = carry_descriptions(old, reg)
        print(f"\n[merge]    kept {stats['kept']} description(s); "
              f"retired {stats['retired_tables']} table(s), "
              f"{stats['retired_columns']} column(s)")

    described = sum(1 for t in reg["tables"].values() for c in t["columns"] if c["description"])
    print(f"\n[counts]   {counts}")
    print(f"[describe] {described}/{counts['columns']} columns described "
          f"({described / counts['columns']:.0%})")

    if dry_run:
        print("[dry-run]  nothing written")
        return reg

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[write]    {out_path.relative_to(ROOT)}  "
          f"({out_path.stat().st_size / 1_048_576:.1f} MB)")
    # The register lives under config/, so cfg_apply hashes it -- and this script is
    # not cfg_apply.  The stale hash is the seed-hash gate doing its job (it is what
    # catches a hand-edit); it is not weakened for our convenience.  Reconcile it:
    print("\n[next]     the config hash for this file is now stale -- reconcile it:\n"
          f'           python iba/scripts/cfg_apply.py --sync --why "recaptured {code} '
          f'@ {reg["schema_version"]}"')
    return reg


def verify(code: str, entry: dict, out_path: pathlib.Path) -> int:
    """gate.dbschema.counts-match + gate.dbschema.description-complete."""
    if not out_path.exists():
        print(f"MISSING: {out_path.relative_to(ROOT)}")
        return 1
    reg = json.loads(out_path.read_text(encoding="utf-8"))
    conn = connect(ROOT / entry["path"])
    live_v = schema_version(conn, entry)
    live_t = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' "
                          "AND name NOT LIKE 'sqlite_%'").fetchone()[0]
    conn.close()

    errs = []
    if reg["schema_version"] != live_v:
        errs.append(f"STALE: register says {reg['schema_version']}, live DB is {live_v}")
    if reg["table_count"] != live_t:
        errs.append(f"STALE: register has {reg['table_count']} tables, live DB has {live_t}")

    cols = reg["counts"]["columns"]
    desc = sum(1 for t in reg["tables"].values() for c in t["columns"] if c["description"])
    tdesc = sum(1 for t in reg["tables"].values() if t["description"])

    print(f"schema_version : {reg['schema_version']}  (live {live_v})")
    print(f"tables         : {reg['table_count']}  (live {live_t})")
    print(f"counts         : {reg['counts']}")
    print(f"descriptions   : {tdesc}/{reg['table_count']} tables, {desc}/{cols} columns")
    for e in errs:
        print(f"  ERROR  {e}")
    print("\n" + ("FAIL" if errs else "PASS -- register matches the live DB"))
    return 1 if errs else 0


# ── describing (the [I] half of dbschema.description-from-data) ──────────────
def digest(reg: dict, tables: list[str]) -> str:
    """A compact, readable profile digest -- the evidence a description is written from.

    The register is ~1.6MB; nobody reads that to describe a column.  This prints
    only what the description must be grounded in.
    """
    out = []
    for name in tables:
        t = reg["tables"][name]
        out.append(f"\n### {name}  ({t['row_count']:,} rows, {len(t['columns'])} cols)")
        if t["primary_key"]:
            out.append(f"PK: {', '.join(t['primary_key'])}")
        for f in t["foreign_keys"]:
            out.append(f"FK: {f['column']} -> {f['references']}"
                       + (f"  ON DELETE {f['on_delete']}" if f["on_delete"] != "NO ACTION" else ""))
        for c in t["checks"]:
            out.append(f"CHECK: {c}")
        for i in t["indexes"]:
            if i["origin"] == "c" or i["unique"]:
                out.append(f"INDEX{' UNIQUE' if i['unique'] else ''}: ({', '.join(i['columns'])})")
        for c in t["columns"]:
            p = c["profile"] or {}
            bits = [c["type"] or "?"]
            if c["pk"]:
                bits.append("PK")
            if c["notnull"]:
                bits.append("NOT NULL")
            if c["default"] is not None:
                bits.append(f"DEFAULT {c['default']}")
            if p.get("empty_table"):
                bits.append("(table empty)")
            else:
                bits.append(f"null {p.get('null_count', 0)}/{p.get('rows_scanned', 0)}")
                bits.append(f"distinct {p.get('distinct_count')}")
                if p.get("scope") == "sampled":
                    bits.append("SAMPLED")
                if p.get("uncontrolled_vocabulary"):
                    bits.append("UNCONTROLLED-VOCAB")
                if p.get("top_values"):
                    vals = ", ".join(f"{v['v']!r}×{v['n']}" for v in p["top_values"][:6])
                    bits.append(f"top[{vals}]")
                elif p.get("min") is not None:
                    bits.append(f"range {p['min']!r}..{p['max']!r}")
            mark = "" if c["description"] else "  <-- NEEDS DESCRIPTION"
            out.append(f"  {c['name']:34} {' · '.join(str(b) for b in bits)}{mark}")
    return "\n".join(out)


def apply_descriptions(reg: dict, path: pathlib.Path, source: str) -> tuple[int, list[str]]:
    """Merge {table: {description, columns:{col: desc}}} in.  Match BY NAME."""
    data = json.loads(path.read_text(encoding="utf-8"))
    n, errs = 0, []
    for tname, td in data.items():
        t = reg["tables"].get(tname)
        if not t:
            errs.append(f"unknown table {tname!r}")
            continue
        if td.get("description"):
            t["description"] = td["description"]
            t["description_source"] = source
            n += 1
        cols = {c["name"]: c for c in t["columns"]}
        for cname, desc in (td.get("columns") or {}).items():
            c = cols.get(cname)
            if not c:
                errs.append(f"unknown column {tname}.{cname!r}")
                continue
            if c.get("description_source") == "researcher" and source != "researcher":
                errs.append(f"refused to overwrite researcher description on {tname}.{cname}")
                continue
            c["description"] = desc
            c["description_source"] = source
            n += 1
    return n, errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", help="database code (see --list)")
    ap.add_argument("--list", action="store_true", help="list the declared databases")
    ap.add_argument("--verify", action="store_true", help="check the register against the live DB")
    ap.add_argument("--dry-run", action="store_true", help="build but write nothing")
    ap.add_argument("--digest", nargs="*", metavar="TABLE",
                    help="print the profile digest for TABLE(s); no args = all undescribed")
    ap.add_argument("--limit", type=int, default=0, help="with --digest: cap the tables shown")
    ap.add_argument("--apply-descriptions", metavar="FILE",
                    help="merge a {table: {description, columns:{}}} json into the register")
    ap.add_argument("--source", default="profiler", choices=["profiler", "researcher"],
                    help="who wrote them (researcher descriptions are never overwritten)")
    a = ap.parse_args()

    dbs = databases()
    if a.list:
        for code, e in dbs.items():
            print(f"  {code:16} {e['db_role']:8} {e['status']:9} "
                  f"{e['path'] or '(does not exist yet)':32} -> {e['schema_file']}")
        return 0
    if not a.db:
        ap.error("--db is required (or --list)")
    if a.db not in dbs:
        ap.error(f"unknown database {a.db!r} -- declared: {', '.join(dbs)}")

    entry = dbs[a.db]
    if not entry.get("capture") and not a.verify:
        print(f"{a.db}: capture is false in DBSchema_maintenance.json "
              f"(status={entry['status']}) -- nothing to do")
        return 0
    out = CONFIG / entry["schema_file"]

    if a.verify:
        return verify(a.db, entry, out)

    if a.digest is not None:
        reg = json.loads(out.read_text(encoding="utf-8"))
        names = a.digest or [n for n, t in reg["tables"].items()
                             if not t["description"]
                             or any(not c["description"] for c in t["columns"])]
        unknown = [n for n in names if n not in reg["tables"]]
        if unknown:
            ap.error(f"unknown table(s): {', '.join(unknown)}")
        if a.limit:
            names = names[:a.limit]
        print(digest(reg, names))
        return 0

    if a.apply_descriptions:
        reg = json.loads(out.read_text(encoding="utf-8"))
        n, errs = apply_descriptions(reg, pathlib.Path(a.apply_descriptions), a.source)
        for e in errs:
            print(f"  ERROR  {e}")
        if errs:
            print("[REJECT]   nothing written")
            return 1
        out.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
        cols = reg["counts"]["columns"]
        done = sum(1 for t in reg["tables"].values() for c in t["columns"] if c["description"])
        print(f"[applied]  {n} description(s) from {a.apply_descriptions} (source={a.source})")
        print(f"[coverage] {done}/{cols} columns ({done / cols:.0%})")
        return 0

    build(a.db, entry, out, a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
