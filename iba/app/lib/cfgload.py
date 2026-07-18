"""cfgload.py — load the JSON SEEDS into the config tables in the DATABASE.

The framework (from iba/config's own principle): the JSON files are the human-editable
SEED; a loader validates and writes them into the DB; the DB is authoritative at
runtime. The app reads config from the DB (cfg.py), never from the JSON.

This module:
  1. creates the cfg_* tables (the config's own schema — the ONE bootstrap that is in
     code, because the loader that builds the config store cannot read it from the
     store it is building),
  2. loads config/schema.json, step.json, run.json, rules.json into them.

After this runs, everything else — including the DATA tables — is built by reading the
cfg_* tables, not the JSON.

    python -m iba.app.lib.cfgload            # (re)load the seeds into the DB
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import sqlite3

from . import cfgcheck

APP = pathlib.Path(__file__).resolve().parent.parent
CONFIG = APP / "config"
DB_PATH = APP / "db" / "iba.db"


class ConfigRejected(RuntimeError):
    """The seeds failed validation. Nothing was loaded — bad config never reached the DB."""

# ── the config store's own schema — the one bootstrap in code ────────────────
CFG_DDL = [
    "CREATE TABLE cfg_meta (key TEXT PRIMARY KEY, value TEXT)",

    """CREATE TABLE cfg_table (
        name TEXT PRIMARY KEY, grain TEXT, "use" TEXT)""",

    """CREATE TABLE cfg_column (
        table_name TEXT, name TEXT, ordinal INTEGER,
        "type" TEXT, is_pk INTEGER, "notnull" INTEGER, is_unique INTEGER,
        dflt TEXT, fk TEXT,
        "use" TEXT, expectation TEXT, source TEXT, filled_by TEXT,
        PRIMARY KEY (table_name, name))""",

    """CREATE TABLE cfg_unique (           -- composite unique / dedup key per table
        table_name TEXT, col TEXT, ordinal INTEGER,
        PRIMARY KEY (table_name, col))""",

    "CREATE TABLE cfg_enum (name TEXT, value TEXT, ordinal INTEGER, PRIMARY KEY (name, value))",

    "CREATE TABLE cfg_connection (key TEXT PRIMARY KEY, value TEXT)",

    """CREATE TABLE cfg_api (
        name TEXT PRIMARY KEY, route TEXT, input TEXT, returns TEXT)""",

    """CREATE TABLE cfg_write_grant (      -- who may write what: writer is an api OR a step OR 'run'
        writer TEXT, table_name TEXT, PRIMARY KEY (writer, table_name))""",

    """CREATE TABLE cfg_work_package (
        name TEXT PRIMARY KEY, ps_script TEXT, runs_over TEXT)""",

    """CREATE TABLE cfg_step (
        work_package TEXT, ordinal INTEGER, step TEXT,
        handler TEXT, scope TEXT, does TEXT,
        PRIMARY KEY (work_package, step))""",

    "CREATE TABLE cfg_setting (key TEXT PRIMARY KEY, value TEXT, use TEXT)",

    """CREATE TABLE cfg_on_fail (
        step TEXT, condition TEXT, path TEXT, resolver TEXT, message TEXT,
        PRIMARY KEY (step, condition))""",

    """CREATE TABLE cfg_status_flow (
        entity TEXT, status TEXT, set_by TEXT, ordinal INTEGER,
        PRIMARY KEY (entity, status))""",

    """CREATE TABLE cfg_change_log (        -- audit: every accepted load, with a seed hash
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        config_version TEXT, seed_hash TEXT, loaded_at TEXT, validated INTEGER)""",

    "CREATE TABLE cfg_book_order (book TEXT PRIMARY KEY, ordinal INTEGER)",
]


def _seed_hash(*seeds: dict) -> str:
    h = hashlib.sha256()
    for s in seeds:
        h.update(json.dumps(s, sort_keys=True, ensure_ascii=False).encode("utf-8"))
    return h.hexdigest()[:16]


def _load_json(name: str) -> dict:
    return json.loads((CONFIG / name).read_text(encoding="utf-8"))


def load(db_path: pathlib.Path = DB_PATH) -> pathlib.Path:
    schema = _load_json("schema.json")
    step = _load_json("step.json")
    run = _load_json("run.json")
    rules = _load_json("rules.json")
    report = _load_json("report.json")
    reference = _load_json("reference.json")

    # ── VALIDATE BEFORE WRITE (the config-maintenance discipline) ──
    ok, errors = cfgcheck.check(schema, step, run, rules, report)
    if not ok:
        raise ConfigRejected(
            "config REJECTED — not loaded. Fix the seeds:\n  " + "\n  ".join(errors))

    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    # drop + recreate the cfg_* store (idempotent reload; data tables untouched here)
    for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg_%'").fetchall():
        conn.execute(f'DROP TABLE IF EXISTS "{row[0]}"')
    for ddl in CFG_DDL:
        conn.execute(ddl)

    conn.execute("INSERT INTO cfg_meta VALUES ('database', ?)", (schema["database"],))
    conn.execute("INSERT INTO cfg_meta VALUES ('config_version', ?)", (run["config_version"],))

    # ── schema ──
    for tname, t in schema["tables"].items():
        conn.execute("INSERT INTO cfg_table VALUES (?,?,?)",
                     (tname, t.get("grain"), t.get("use")))
        for i, (cname, c) in enumerate(t["columns"].items()):
            conn.execute("INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                tname, cname, i, c.get("type", "TEXT"),
                1 if c.get("pk") else 0, 1 if c.get("notnull") else 0,
                1 if c.get("unique") else 0, str(c["default"]) if "default" in c else None,
                c.get("fk"), c.get("use"), c.get("expectation"), c.get("source"), c.get("filled_by")))
        for j, col in enumerate(t.get("unique", [])):
            conn.execute("INSERT INTO cfg_unique VALUES (?,?,?)", (tname, col, j))
    for ename, vals in schema.get("enums", {}).items():
        for k, v in enumerate(vals):
            conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", (ename, v, k))

    # ── step / api ──
    for k, v in step["connection"].items():
        if k != "note":
            conn.execute("INSERT INTO cfg_connection VALUES (?,?)", (k, str(v)))
    conn.execute("INSERT INTO cfg_setting VALUES ('step.cap', ?, 'STEP result cap')", (str(step["cap"]),))
    for aname, api in step["apis"].items():
        conn.execute("INSERT INTO cfg_api VALUES (?,?,?,?)",
                     (aname, api["route"], api.get("input"), api.get("returns")))
        for tbl in api.get("may_source", []):        # api writers -> write grants
            conn.execute("INSERT INTO cfg_write_grant VALUES (?,?)", (aname, tbl))

    # ── run / sequence ──
    for wpname, wp in run["work_packages"].items():
        conn.execute("INSERT INTO cfg_work_package VALUES (?,?,?)",
                     (wpname, wp.get("ps_script"), wp.get("runs_over")))
        for i, s in enumerate(wp["sequence"]):
            conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                         (wpname, i, s["step"], s["handler"], s.get("scope"), s.get("does")))

    # ── rules ──
    for k, s in rules["settings"].items():
        conn.execute("INSERT OR REPLACE INTO cfg_setting VALUES (?,?,?)",
                     (k, json.dumps(s["value"]), s.get("use")))
    for r in rules["on_fail"]:
        conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)",
                     (r["step"], r["condition"], r["path"], r.get("resolver"), r.get("message")))
    for writer, tbls in rules["write_grants"].items():   # step / dispatcher writers -> grants
        if writer.startswith("_"):
            continue
        for tbl in tbls:
            conn.execute("INSERT OR IGNORE INTO cfg_write_grant VALUES (?,?)", (writer, tbl))
    for entity, flow in rules["status_flow"].items():
        for i, f in enumerate(flow):
            conn.execute("INSERT INTO cfg_status_flow VALUES (?,?,?,?)",
                         (entity, f["to"], f["by"], i))

    # ── report / output ──
    for k, s in report["settings"].items():
        conn.execute("INSERT OR REPLACE INTO cfg_setting VALUES (?,?,?)",
                     (k, json.dumps(s["value"]), s.get("use")))

    # ── reference: book order + patterns (were hard-coded in the code) ──
    for i, b in enumerate(reference["book_order"]):
        conn.execute("INSERT INTO cfg_book_order VALUES (?,?)", (b, i))
    for k, s in reference["patterns"].items():
        conn.execute("INSERT OR REPLACE INTO cfg_setting VALUES (?,?,?)",
                     (k, json.dumps(s["value"]), s.get("use")))

    # audit the accepted load
    conn.execute("INSERT INTO cfg_change_log (config_version, seed_hash, loaded_at, validated) "
                 "VALUES (?,?,?,1)",
                 (run["config_version"], _seed_hash(schema, step, run, rules, report),
                  datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")))
    conn.commit()
    n = {r[0]: conn.execute(f'SELECT COUNT(*) FROM "{r[0]}"').fetchone()[0]
         for r in conn.execute("SELECT name FROM sqlite_master WHERE name LIKE 'cfg_%'")}
    conn.close()
    return db_path, n


if __name__ == "__main__":
    path, counts = load()
    print(f"config loaded into {path}")
    for t, c in counts.items():
        print(f"  {t:20} {c} rows")
