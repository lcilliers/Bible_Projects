"""cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG.

Reads exclusively from the cfg_* tables in the DATABASE. Never opens a JSON file.
The DB is the master copy of the config; this is what the running app consults, from its first
decision to its last.

Every read is TRACED. Set IBA_TRACE=1 and every config lookup prints who read what —
so the governance chain is visible, not asserted.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import sqlite3
import sys

# The config version hashes every active cfg_* rule table (cfg_table category='rule'), so a new rule
# table counts automatically; audit logs (category 'log') and cfg_meta itself (whose value would
# feed its own hash) are left out (#2201).
_VERSION_TABLES_SQL = ("SELECT name FROM cfg_table WHERE database='iba' AND category='rule' "
                       "AND inactive=0 AND substr(name, 1, 4)='cfg_' AND name<>'cfg_meta' ORDER BY name")

DB_PATH = pathlib.Path(__file__).resolve().parent.parent / "db" / "iba.db"
TRACE = os.environ.get("IBA_TRACE") == "1"


def _trace(what: str, value) -> None:
    if TRACE:
        v = value if isinstance(value, (str, int, float, bool, type(None))) else f"<{len(value)} rows>"
        print(f"    [cfg] {what:44} = {v}", file=sys.stderr)


class NonCompliantUtility(RuntimeError):
    """Raised by `Cfg.assert_utility_compliant()`: the module's `cfg_utility` row flags hardcoded
    values that should be `cfg_setting`-driven (#648), so it must not run as-is."""


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

    @classmethod
    def on(cls, conn):
        """A Cfg over a connection the caller already holds (a lib function that is given a conn reads its rules from config
        the same way as one given a Cfg: governance.rules_must_be_config_driven)."""
        obj = cls.__new__(cls)
        obj.conn = conn
        return obj

    # ── settings (scalar rules) ──────────────────────────────────────────────
    def setting(self, key: str, default=None):
        # inactive rows are never read (#334)
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        val = json.loads(r[0]) if r else default
        _trace(f"setting {key}", val)
        return val

    def required_setting(self, key: str):
        """Same lookup as `.setting()`, but with NO default parameter: raises if the key is missing or
        inactive. Used for report/output paths and any value that must have a single live config source,
        so a missing, renamed or deactivated setting fails loudly instead of falling back to a literal."""
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        if r is None:
            raise KeyError(f"no active cfg_setting {key!r} -- every output location/value that "
                          f"must be config-driven needs a live row, not a hardcoded fallback in "
                          f"the calling code (governance.rules_must_be_config_driven)")
        val = json.loads(r[0])
        _trace(f"required_setting {key}", val)
        return val

    def module_setting(self, table: str, key: str, default=None):
        """Generic reader for a per-module settings table shaped like cfg_setting (key/value/use/
        inactive), e.g. cfg_passage (governance.module.config). `table` is always a literal from the
        calling code, never external input."""
        r = self.conn.execute(
            f'SELECT value FROM "{table}" WHERE key=? AND inactive=0', (key,)).fetchone()
        val = json.loads(r["value"]) if r else default
        _trace(f"module_setting({table}, {key})", val)
        return val

    def required_module_setting(self, table: str, key: str):
        """Same as `.required_setting()`, for a per-module settings table: no default, raises if the row
        is missing or inactive."""
        r = self.conn.execute(
            f'SELECT value FROM "{table}" WHERE key=? AND inactive=0', (key,)).fetchone()
        if r is None:
            raise KeyError(f"no active row {key!r} in {table!r} -- every output location/value "
                          f"that must be config-driven needs a live row, not a hardcoded "
                          f"fallback in the calling code (governance.rules_must_be_config_driven)")
        val = json.loads(r["value"])
        _trace(f"required_module_setting({table}, {key})", val)
        return val

    def database_path(self, name: str) -> pathlib.Path:
        """Project-root-relative path to a registered project database (`cfg_enum 'project_database'`,
        `database.<name>.path`). The setting is always read; for `name='iba'` the return value is the
        bootstrap `DB_PATH` (reading it from the database it locates would be circular), and a mismatch
        with the setting is drift that `init.py`'s startup check surfaces."""
        repo_root = DB_PATH.resolve().parent.parent.parent.parent
        rel = self.setting(f"database.{name}.path")
        if rel is None:
            raise KeyError(f"no database.{name}.path setting -- is {name!r} a registered "
                          f"project_database? (cfg_enum 'project_database')")
        if name == "iba":
            configured = (repo_root / rel).resolve()
            if configured != DB_PATH.resolve():
                _trace("database_path(iba) DRIFT", f"configured={configured} actual={DB_PATH}")
            return DB_PATH
        return repo_root / rel

    # ── the schema (data tables built from here) ─────────────────────────────
# `database='iba'` explicit on both queries: cfg_table/cfg_column also describe bible_research.db,
# which shares table names for different tables, and lib/db.py:build_data_tables() builds iba.db's
# tables from cfg_column.
    def tables(self) -> list[str]:
        rows = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_table WHERE database='iba' ORDER BY rowid")]
        _trace("tables()", rows)
        return rows

    def columns(self, table: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_column WHERE database='iba' AND table_name=? ORDER BY ordinal",
            (table,)).fetchall()
        _trace(f"columns({table})", rows)
        return rows

    def column_names(self, table: str) -> set[str]:
        return {r["name"] for r in self.columns(table)}

    def indexes(self, table: str) -> list[tuple[str, list[str]]]:
        """Secondary (non-unique) indexes to build for this table -- [(index_name, [cols])], cols in
        cfg_index.ordinal order, indexes in name order."""
        rows = self.conn.execute(
            "SELECT name, col FROM cfg_index WHERE table_name=? ORDER BY name, ordinal",
            (table,)).fetchall()
        out: dict[str, list[str]] = {}
        for r in rows:
            out.setdefault(r["name"], []).append(r["col"])
        result = sorted(out.items())
        _trace(f"indexes({table})", result)
        return result

    def triggers(self, table: str, database: str = "iba") -> list[str]:
        """The CREATE TRIGGER statements registered for this table (cfg_trigger, #2110), in ordinal then
        name order: `lib/db.py:trigger_ddl()` rebuilds them and `cfgquality.find_unregistered_triggers`
        checks the live databases against them."""
        rows = [r["sql"] for r in self.conn.execute(
            "SELECT sql FROM cfg_trigger WHERE database=? AND table_name=? AND inactive=0 "
            "ORDER BY ordinal, name", (database, table))]
        _trace(f"triggers({table})", rows)
        return rows

    def unique_key(self, table: str, database: str = "iba") -> list[str]:
        """The dedup key -- the composite UNIQUE, else the single UNIQUE column, else the PK. `database`
        defaults to 'iba' (table names are shared across the two databases)."""
        comp = [r["col"] for r in self.conn.execute(
            "SELECT col FROM cfg_unique WHERE database=? AND table_name=? ORDER BY ordinal",
            (database, table))]
        if comp:
            _trace(f"unique_key({table})", comp); return comp
        u = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_column WHERE database=? AND table_name=? AND is_unique=1",
            (database, table))]
        if u:
            _trace(f"unique_key({table})", u); return u
        pk = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_column WHERE database=? AND table_name=? AND is_pk=1",
            (database, table))]
        _trace(f"unique_key({table})", pk); return pk

    def enum(self, name: str) -> list[str]:
        rows = [r["value"] for r in self.conn.execute(
            "SELECT value FROM cfg_enum WHERE name=? AND inactive=0 ORDER BY ordinal", (name,))]
        _trace(f"enum({name})", rows)
        return rows

    # ── STEP ─────────────────────────────────────────────────────────────────
    def connection(self, key: str):
        r = self.conn.execute(
            "SELECT value FROM cfg_connection WHERE key=? AND inactive=0", (key,)).fetchone()
        _trace(f"connection {key}", r["value"] if r else None)
        return r["value"] if r else None

    def route(self, api: str) -> str:
        r = self.conn.execute(
            "SELECT route FROM cfg_api WHERE name=? AND inactive=0", (api,)).fetchone()
        _trace(f"route {api}", r["route"] if r else None)
        return r["route"]

    def assert_utility_compliant(self, file_path: str) -> None:
        """Raises `NonCompliantUtility` if `file_path`'s `cfg_utility` row is flagged non-compliant
        (`purpose` prefixed `'NON-COMPLIANT (escalation #648'`): a script with known hardcoded-config
        violations must be revised before it runs. Called by a module's own entry point with its own
        project-relative `file_path`. Only importable modules with a dispatcher-reachable caller can be
        gated this way; for standalone scripts it is process discipline (governance.noncompliant_script_gate)."""
        row = self.conn.execute(
            "SELECT purpose FROM cfg_utility WHERE file_path=?", (file_path,)).fetchone()
        if row and row["purpose"] and row["purpose"].startswith("NON-COMPLIANT (escalation #648"):
            raise NonCompliantUtility(
                f"{file_path!r} is flagged non-compliant in cfg_utility and must be revised "
                f"(hardcoded values moved to cfg_setting) before use -- see its own purpose text, "
                f"or iba/app/reports/hardcoded-constants-sweep-20260817.md, for what needs to move.")

    def may_write(self, writer: str, database: str = "iba") -> set[str]:
        """Which tables this writer (an api, a step, or 'run') is granted to write. `database` defaults
        to 'iba' (the two databases share table names)."""
        rows = {r["table_name"] for r in self.conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=? AND database=? AND inactive=0",
            (writer, database))}
        _trace(f"may_write({writer}, database={database!r})", rows)
        return rows

    # ── run / sequence ───────────────────────────────────────────────────────
    def sequence(self, work_package: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_step WHERE work_package=? AND inactive=0 ORDER BY ordinal",
            (work_package,)).fetchall()
        _trace(f"sequence({work_package})", rows)
        return rows

    def step(self, work_package: str, step: str) -> sqlite3.Row:
        r = self.conn.execute(
            "SELECT * FROM cfg_step WHERE work_package=? AND step=? AND inactive=0",
            (work_package, step)).fetchone()
        _trace(f"step {step}", r["handler"] if r else None)
        return r

    def is_chained(self, work_package: str) -> bool:
        """True if every step of this work package runs under one run_id in one PS invocation ('done'
        waits for the last step); False if each step runs independently ('done' fires on that step's own
        continue path). cfg_work_package.chained. Only called for an active package (run.py's gate)."""
        r = self.conn.execute("SELECT chained FROM cfg_work_package WHERE name=?",
                              (work_package,)).fetchone()
        return bool(r["chained"]) if r else True   # default chained=True: the old, safer behaviour

    def work_package_inactive(self, work_package: str) -> bool:
        """True if `work_package` has an inactive `cfg_work_package` row, or no row at all. Used by
        `run.py`'s dispatch gate (#334)."""
        r = self.conn.execute("SELECT inactive FROM cfg_work_package WHERE name=?",
                              (work_package,)).fetchone()
        return True if r is None else bool(r["inactive"])

    def step_inactive(self, work_package: str, step: str) -> bool:
        """True if `(work_package, step)` has a `cfg_step` row and it is `inactive=1`, OR no such
        row exists at all. Same reasoning as `work_package_inactive()`."""
        r = self.conn.execute("SELECT inactive FROM cfg_step WHERE work_package=? AND step=?",
                              (work_package, step)).fetchone()
        return True if r is None else bool(r["inactive"])

    def step_kind(self, work_package: str, step: str) -> str | None:
        """`cfg_step.kind` (`'operations'` | `'utility'`) for `(work_package, step)`, or `None` if unset.
        `run.py` refuses a step with no kind."""
        r = self.conn.execute("SELECT kind FROM cfg_step WHERE work_package=? AND step=?",
                              (work_package, step)).fetchone()
        return r["kind"] if r else None

    def book_order(self) -> dict[str, int]:
        rows = {r["book"]: r["ordinal"] for r in self.conn.execute(
            "SELECT book, ordinal FROM cfg_book_order WHERE inactive=0")}
        _trace("book_order()", rows)
        return rows

    def candidate_rules(self, kind: str) -> list[str]:
        """The editable candidate meaning-net inputs of one kind: synonym | accept | reject."""
        rows = [r["value"] for r in self.conn.execute(
            "SELECT value FROM cfg_candidate_rule WHERE kind=? AND inactive=0", (kind,))]
        _trace(f"candidate_rules({kind})", rows)
        return rows

    def config_version(self) -> str:
        """The config version: computed live from the content of every active cfg_* rule table
        (_VERSION_TABLES_SQL), so it changes the moment the config does. 'app-0.1.0' is the
        human-readable major-version prefix."""
        base = self.conn.execute(
            "SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        prefix = base["value"] if base else "app"
        h = hashlib.sha256()
        for (t,) in self.conn.execute(_VERSION_TABLES_SQL).fetchall():
            for row in self.conn.execute(f'SELECT * FROM "{t}" ORDER BY rowid'):
                h.update("|".join("" if v is None else str(v) for v in row).encode("utf-8"))
            h.update(b"\x00")
        return f"{prefix}+{h.hexdigest()[:12]}"

    # ── on_fail (the fork rule) ──────────────────────────────────────────────
    def on_fail(self, step: str, condition: str) -> sqlite3.Row | None:
        r = self.conn.execute(
            "SELECT * FROM cfg_on_fail WHERE step=? AND condition=? AND inactive=0",
            (step, condition)).fetchone()
        _trace(f"on_fail({step}/{condition})", r["path"] if r else "ok")
        return r

    def close(self):
        self.conn.close()
