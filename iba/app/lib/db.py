"""db.py — the DATA layer. Built FROM the config in the database.

The schema is not in this file and no longer in a JSON file the app reads. It is in
the cfg_* tables (cfgload.py seeded them). build_data_tables() reads cfg_column and
creates the data tables from it. Db.write validates against cfg_column; upsert takes
its key from cfg.unique_key. So the data tables, the allowed columns, and the dedup
keys are all governed by config — the code enforces, it does not decide.
"""

from __future__ import annotations

import pathlib
import sqlite3

from .cfg import Cfg, DB_PATH

# tables the config store itself owns — not data, not built here
_CFG_PREFIX = ("cfg_",)


def _col_ddl(c: sqlite3.Row) -> str:
    parts = [f'"{c["name"]}"', c["type"] or "TEXT"]
    if c["is_pk"]:
        parts.append("PRIMARY KEY")
        if (c["type"] or "") == "INTEGER":
            parts.append("AUTOINCREMENT")
    if c["notnull"]:
        parts.append("NOT NULL")
    if c["is_unique"]:
        parts.append("UNIQUE")
    if c["dflt"] is not None:
        parts.append(f"DEFAULT {c['dflt']}")
    return " ".join(parts)


def build_data_tables(cfg: Cfg, conn: sqlite3.Connection) -> list[str]:
    """Create every DATA table from cfg_column. Config-governed, from line one."""
    built = []
    for table in cfg.tables():
        cols = cfg.columns(table)
        ddl = [_col_ddl(c) for c in cols]
        key = cfg.unique_key(table)
        # composite unique when the key is more than the PK
        pk = [c["name"] for c in cols if c["is_pk"]]
        if len(key) > 1 or (key and key != pk):
            ddl.append(f'UNIQUE ({", ".join(key)})')
        for c in cols:
            if c["fk"]:
                rt, rc = c["fk"].split(".")
                ddl.append(f'FOREIGN KEY ("{c["name"]}") REFERENCES "{rt}"("{rc}")')
        conn.execute(f'CREATE TABLE IF NOT EXISTS "{table}" (\n  ' + ",\n  ".join(ddl) + "\n)")
        built.append(table)
    conn.commit()
    return built


def build(reset_data: bool = False) -> pathlib.Path:
    """Ensure the DB holds config + data tables. Config must already be loaded."""
    cfg = Cfg()
    conn = sqlite3.connect(DB_PATH)
    if reset_data:
        for t in cfg.tables():
            conn.execute(f'DROP TABLE IF EXISTS "{t}"')
    build_data_tables(cfg, conn)
    conn.close()
    cfg.close()
    return DB_PATH


class Db:
    """Data access. Column set and dedup keys come from config (cfg), not from here."""

    def __init__(self, cfg: Cfg | None = None, path: pathlib.Path = DB_PATH):
        self.cfg = cfg or Cfg(path)
        self._own_cfg = cfg is None
        # ONE connection per process — the data layer SHARES the config handle's
        # connection, so a write transaction and a config read never self-contend
        # ('database is locked'). FKs declared in DDL but NOT hard-enforced — the raw
        # model references before its referent (word_strong before strong).
        self.conn = self.cfg.conn

    def close(self):
        self.conn.commit()
        if self._own_cfg:          # the shared connection is closed by whoever owns the Cfg
            self.cfg.close()

    def write(self, table: str, row: dict) -> int:
        allowed = self.cfg.column_names(table)      # <- config decides the columns
        bad = set(row) - allowed
        if bad:
            raise ValueError(f"{table}: columns not in config schema: {sorted(bad)}")
        keys = list(row)
        ph = ",".join("?" * len(keys))
        cur = self.conn.execute(
            f'INSERT INTO "{table}" ({",".join(chr(34)+k+chr(34) for k in keys)}) VALUES ({ph})',
            [row[k] for k in keys])
        return cur.lastrowid

    def upsert(self, table: str, row: dict) -> tuple[int, bool]:
        """Dedup by the config's UNIQUE key. A row already keyed is reused, not
        duplicated — the global 'no duplicates on any level' rule, from config."""
        key = self.cfg.unique_key(table)            # <- config decides the dedup key
        where = " AND ".join(f'"{k}"=?' for k in key)
        found = self.conn.execute(
            f'SELECT rowid, * FROM "{table}" WHERE {where}', [row[k] for k in key]).fetchone()
        if found:
            pkcol = self._pk(table)
            return (found[pkcol] if pkcol in found.keys() else found["rowid"]), False
        return self.write(table, row), True

    def _pk(self, table: str) -> str:
        for c in self.cfg.columns(table):
            if c["is_pk"]:
                return c["name"]
        return "rowid"

    def get(self, table: str, **where):
        clause = " AND ".join(f'"{k}"=?' for k in where)
        return self.conn.execute(
            f'SELECT * FROM "{table}" WHERE {clause}', list(where.values())).fetchone()

    def update(self, table: str, where: dict, **sets):
        s = ", ".join(f'"{k}"=?' for k in sets)
        w = " AND ".join(f'"{k}"=?' for k in where)
        self.conn.execute(f'UPDATE "{table}" SET {s} WHERE {w}',
                          list(sets.values()) + list(where.values()))

    def count(self, table: str, **where) -> int:
        if where:
            w = " AND ".join(f'"{k}"=?' for k in where)
            return self.conn.execute(
                f'SELECT COUNT(*) FROM "{table}" WHERE {w}', list(where.values())).fetchone()[0]
        return self.conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]

    def rows(self, sql: str, params=()):
        return self.conn.execute(sql, list(params)).fetchall()


if __name__ == "__main__":
    import sys
    from . import cfgload
    if "--load" in sys.argv:
        cfgload.load()
    p = build(reset_data="--reset" in sys.argv)
    cfg = Cfg()
    print(f"data tables built from config in {p}")
    print("  ", ", ".join(cfg.tables()))
    cfg.close()
