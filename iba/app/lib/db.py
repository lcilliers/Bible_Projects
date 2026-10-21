"""db.py — the DATA layer, built from the config in the database: build_data_tables() creates the
data tables from cfg_column; Db.write validates against cfg_column; upsert takes its key from
cfg.unique_key. The code enforces; config decides.
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


def table_ddl(cfg: Cfg, table: str, name: str | None = None) -> tuple[str, list[str]]:
    """(create_table_sql, [index_sql, ...]) for `table`, entirely from current config -- the one place
    this logic lives (also used by `migration/retrofit_debate_lexicon_tables.py`). `name` overrides the
    physical table name (e.g. a `{table}__retrofit` staging table) while FK/index definitions keep the
    config-declared relationships.

    Uniqueness: a table with a `deleted` column (soft-delete-and-reconcile) gets a partial unique
    index (`CREATE UNIQUE INDEX ... WHERE deleted=0`), unique among live rows only, so its history
    never collides. A table without one gets a plain inline UNIQUE."""
    phys = name or table
    cols = cfg.columns(table)
    col_names = {c["name"] for c in cols}
    has_deleted = "deleted" in col_names
    ddl = [_col_ddl(c) for c in cols]
    key = cfg.unique_key(table)
    pk = [c["name"] for c in cols if c["is_pk"]]
    composite = bool(key) and (len(key) > 1 or key != pk)
    if composite and not has_deleted:
        ddl.append(f'UNIQUE ({", ".join(key)})')
    for c in cols:
        if c["fk"]:
            rt, rc = c["fk"].split(".")
            ddl.append(f'FOREIGN KEY ("{c["name"]}") REFERENCES "{rt}"("{rc}")')
    create_sql = f'CREATE TABLE "{phys}" (\n  ' + ",\n  ".join(ddl) + "\n)"

    index_sql = []
    if composite and has_deleted:
        idx_name = f"idx_{phys}_live_unique"
        cols_sql = ", ".join(f'"{c}"' for c in key)
        index_sql.append(f'CREATE UNIQUE INDEX "{idx_name}" ON "{phys}" ({cols_sql}) WHERE deleted=0')
    for idx_name, idx_cols in cfg.indexes(table):
        cols_sql = ", ".join(f'"{c}"' for c in idx_cols)
        index_sql.append(f'CREATE INDEX "{idx_name}" ON "{phys}" ({cols_sql})')
    return create_sql, index_sql


def trigger_ddl(cfg: Cfg, table: str) -> list[str]:
    """The CREATE TRIGGER statements for `table`, from `cfg_trigger` (#2110). Kept apart from
    `table_ddl()`: a trigger may name other tables, so `build_data_tables()` creates every table first."""
    return cfg.triggers(table)


def build_data_tables(cfg: Cfg, conn: sqlite3.Connection) -> list[str]:
    """Create every DATA table from cfg_column. Config-governed, from line one — DDL from
    `table_ddl()` above; then every registered trigger (`trigger_ddl()`), once all tables exist."""
    built = []
    for table in cfg.tables():
        create_sql, index_sql = table_ddl(cfg, table)
        conn.execute(create_sql.replace("CREATE TABLE ", "CREATE TABLE IF NOT EXISTS ", 1))
        for sql in index_sql:
            conn.execute(sql.replace("CREATE INDEX ", "CREATE INDEX IF NOT EXISTS ", 1)
                             .replace("CREATE UNIQUE INDEX ", "CREATE UNIQUE INDEX IF NOT EXISTS ", 1))
        built.append(table)
    for table in built:
        for sql in trigger_ddl(cfg, table):
            conn.execute(sql.replace("CREATE TRIGGER ", "CREATE TRIGGER IF NOT EXISTS ", 1))
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
