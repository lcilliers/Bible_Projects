"""cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG.

Reads exclusively from the cfg_* tables in the DATABASE. Never opens a JSON file.
The JSON is the seed (cfgload.py wrote it into the DB); this is what the running app
consults, from its first decision to its last.

Every read is TRACED. Set IBA_TRACE=1 and every config lookup prints who read what —
so the governance chain is visible, not asserted.
"""

from __future__ import annotations

import json
import os
import pathlib
import sqlite3
import sys

DB_PATH = pathlib.Path(__file__).resolve().parent.parent / "db" / "iba.db"
TRACE = os.environ.get("IBA_TRACE") == "1"


def _trace(what: str, value) -> None:
    if TRACE:
        v = value if isinstance(value, (str, int, float, bool, type(None))) else f"<{len(value)} rows>"
        print(f"    [cfg] {what:44} = {v}", file=sys.stderr)


class Cfg:
    """One open handle to the config store. Cheap; make one per process."""

    def __init__(self, db_path: pathlib.Path = DB_PATH):
        self.conn = sqlite3.connect(db_path, timeout=30.0)
        self.conn.row_factory = sqlite3.Row
        # WAL + a real busy-timeout: readers don't block writers, and brief lock
        # contention waits instead of failing instantly with 'database is locked'.
        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
            self.conn.execute("PRAGMA busy_timeout=30000")
        except sqlite3.Error:
            pass

    # ── settings (scalar rules) ──────────────────────────────────────────────
    def setting(self, key: str, default=None):
        r = self.conn.execute("SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()
        val = json.loads(r["value"]) if r else default
        _trace(f"setting {key}", val)
        return val

    # ── the schema (data tables built from here) ─────────────────────────────
    def tables(self) -> list[str]:
        rows = [r["name"] for r in self.conn.execute("SELECT name FROM cfg_table ORDER BY rowid")]
        _trace("tables()", rows)
        return rows

    def columns(self, table: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_column WHERE table_name=? ORDER BY ordinal", (table,)).fetchall()
        _trace(f"columns({table})", rows)
        return rows

    def column_names(self, table: str) -> set[str]:
        return {r["name"] for r in self.columns(table)}

    def unique_key(self, table: str) -> list[str]:
        """The dedup key — the composite UNIQUE, else the single UNIQUE column, else the PK."""
        comp = [r["col"] for r in self.conn.execute(
            "SELECT col FROM cfg_unique WHERE table_name=? ORDER BY ordinal", (table,))]
        if comp:
            _trace(f"unique_key({table})", comp); return comp
        u = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_column WHERE table_name=? AND is_unique=1", (table,))]
        if u:
            _trace(f"unique_key({table})", u); return u
        pk = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_column WHERE table_name=? AND is_pk=1", (table,))]
        _trace(f"unique_key({table})", pk); return pk

    def enum(self, name: str) -> list[str]:
        rows = [r["value"] for r in self.conn.execute(
            "SELECT value FROM cfg_enum WHERE name=? ORDER BY ordinal", (name,))]
        _trace(f"enum({name})", rows)
        return rows

    # ── STEP ─────────────────────────────────────────────────────────────────
    def connection(self, key: str):
        r = self.conn.execute("SELECT value FROM cfg_connection WHERE key=?", (key,)).fetchone()
        _trace(f"connection {key}", r["value"] if r else None)
        return r["value"] if r else None

    def route(self, api: str) -> str:
        r = self.conn.execute("SELECT route FROM cfg_api WHERE name=?", (api,)).fetchone()
        _trace(f"route {api}", r["route"] if r else None)
        return r["route"]

    def may_write(self, writer: str) -> set[str]:
        """Which tables this writer (an api, a step, or 'run') is granted to write."""
        rows = {r["table_name"] for r in self.conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=?", (writer,))}
        _trace(f"may_write({writer})", rows)
        return rows

    # ── run / sequence ───────────────────────────────────────────────────────
    def sequence(self, work_package: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_step WHERE work_package=? ORDER BY ordinal", (work_package,)).fetchall()
        _trace(f"sequence({work_package})", rows)
        return rows

    def step(self, work_package: str, step: str) -> sqlite3.Row:
        r = self.conn.execute("SELECT * FROM cfg_step WHERE work_package=? AND step=?",
                              (work_package, step)).fetchone()
        _trace(f"step {step}", r["handler"] if r else None)
        return r

    def book_order(self) -> dict[str, int]:
        rows = {r["book"]: r["ordinal"] for r in self.conn.execute(
            "SELECT book, ordinal FROM cfg_book_order")}
        _trace("book_order()", rows)
        return rows

    def candidate_rules(self, kind: str) -> list[str]:
        """The editable candidate meaning-net inputs of one kind: synonym | accept | reject."""
        rows = [r["value"] for r in self.conn.execute(
            "SELECT value FROM cfg_candidate_rule WHERE kind=?", (kind,))]
        _trace(f"candidate_rules({kind})", rows)
        return rows

    def config_version(self) -> str:
        r = self.conn.execute("SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        return r["value"] if r else "?"

    # ── on_fail (the fork rule) ──────────────────────────────────────────────
    def on_fail(self, step: str, condition: str) -> sqlite3.Row | None:
        r = self.conn.execute("SELECT * FROM cfg_on_fail WHERE step=? AND condition=?",
                              (step, condition)).fetchone()
        _trace(f"on_fail({step}/{condition})", r["path"] if r else "ok")
        return r

    def close(self):
        self.conn.close()
