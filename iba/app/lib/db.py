"""db.py — the DB layer for the IBA app.

The schema is NOT in this file. It is `config/schema.json`. This module reads that
config and:
  - build_db()  creates the SQLite DB and its tables from the config (CREATE TABLE
                generated from the column definitions — types, PK, NOT NULL, UNIQUE, FK)
  - Db          a thin connection with the CRUD helpers the handlers use, including
                upsert-by-key, which is how "no duplicates on any level" is enforced
                globally: a row keyed on an existing key is skipped, not duplicated.

Nothing writes a column the schema does not declare (write() validates against it),
so a handler cannot invent a column and the schema stays the single source of truth.
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
from typing import Any, Iterable

APP = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = json.loads((APP / "config" / "schema.json").read_text(encoding="utf-8"))
DB_PATH = APP / "db" / "iba.db"


# ── build ────────────────────────────────────────────────────────────────────
def _col_ddl(name: str, spec: dict) -> str:
    parts = [f'"{name}"', spec.get("type", "TEXT")]
    if spec.get("pk"):
        parts.append("PRIMARY KEY")
        if spec.get("type") == "INTEGER":
            parts.append("AUTOINCREMENT")
    if spec.get("notnull"):
        parts.append("NOT NULL")
    if spec.get("unique"):
        parts.append("UNIQUE")
    if "default" in spec:
        parts.append(f"DEFAULT {spec['default']}")
    return " ".join(parts)


def _table_ddl(name: str, tspec: dict) -> str:
    cols = [_col_ddl(c, s) for c, s in tspec["columns"].items()]
    # table-level UNIQUE (composite)
    if "unique" in tspec:
        cols.append(f"UNIQUE ({', '.join(tspec['unique'])})")
    # FKs, declared but not enforced hard (SQLite FK off by default; kept as documentation + optional PRAGMA)
    for c, s in tspec["columns"].items():
        if "fk" in s:
            ref_t, ref_c = s["fk"].split(".")
            cols.append(f'FOREIGN KEY ("{c}") REFERENCES "{ref_t}"("{ref_c}")')
    return f'CREATE TABLE IF NOT EXISTS "{name}" (\n  ' + ",\n  ".join(cols) + "\n)"


def build_db(reset: bool = False) -> pathlib.Path:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if reset and DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    for name, tspec in SCHEMA["tables"].items():
        conn.execute(_table_ddl(name, tspec))
    # a tiny meta table so the DB knows which schema/config built it
    conn.execute('CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT)')
    conn.execute('INSERT OR REPLACE INTO _meta VALUES (?,?)',
                 ("database", SCHEMA["database"]))
    conn.commit()
    conn.close()
    return DB_PATH


# ── access ───────────────────────────────────────────────────────────────────
class Db:
    def __init__(self, path: pathlib.Path = DB_PATH):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        # FKs are declared in the DDL for documentation and joins, NOT hard-enforced.
        # The raw model legitimately records a reference before (or without) its
        # referent: word_strong lists the seed strongs before `detail` fetches them,
        # and `span` names every code in a verse — including strongs this word does
        # not hold (other lemmas). Enforcing FKs would reject both. Left off by design.

    def close(self):
        self.conn.commit()
        self.conn.close()

    def _cols(self, table: str) -> set[str]:
        return set(SCHEMA["tables"][table]["columns"])

    def write(self, table: str, row: dict) -> int:
        """Insert a row. Rejects any column the schema does not declare."""
        cols = self._cols(table)
        bad = set(row) - cols
        if bad:
            raise ValueError(f"{table}: columns not in schema: {sorted(bad)}")
        keys = list(row)
        ph = ",".join("?" * len(keys))
        cur = self.conn.execute(
            f'INSERT INTO "{table}" ({",".join(chr(34)+k+chr(34) for k in keys)}) VALUES ({ph})',
            [row[k] for k in keys])
        return cur.lastrowid

    def upsert(self, table: str, row: dict, key: list[str]) -> tuple[int, bool]:
        """Write the row unless one with the same key exists. Returns (id, created).

        This is the global-dedup rule: a strong/verse/span already present is not
        re-written, whatever finds it. Returns the existing id and created=False.
        """
        where = " AND ".join(f'"{k}"=?' for k in key)
        found = self.conn.execute(
            f'SELECT rowid, * FROM "{table}" WHERE {where}', [row[k] for k in key]).fetchone()
        if found:
            pk = self._pk(table)
            return (found[pk] if pk in found.keys() else found["rowid"]), False
        rid = self.write(table, row)
        return rid, True

    def _pk(self, table: str) -> str:
        for c, s in SCHEMA["tables"][table]["columns"].items():
            if s.get("pk"):
                return c
        return "rowid"

    def get(self, table: str, **where) -> sqlite3.Row | None:
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

    def rows(self, sql: str, params: Iterable[Any] = ()) -> list[sqlite3.Row]:
        return self.conn.execute(sql, list(params)).fetchall()


if __name__ == "__main__":
    import sys
    p = build_db(reset="--reset" in sys.argv)
    print(f"built {p}  ({p.stat().st_size} bytes)")
    print("tables:", ", ".join(SCHEMA["tables"]))
