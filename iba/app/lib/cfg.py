"""cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG.

Reads exclusively from the cfg_* tables in the DATABASE. Never opens a JSON file.
The JSON is the seed (cfgload.py wrote it into the DB); this is what the running app
consults, from its first decision to its last.

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

# every cfg_* table that is actual CONFIG CONTENT (an input the app reads) — excludes the audit
# trails (cfg_change_log, cfg_change_detail) and cfg_meta itself, which would make the hash
# depend on its own prior value. Kept as a named list (not a LIKE 'cfg_%' scan) so a future
# audit-only cfg_* table doesn't silently start affecting the version.
_VERSION_TABLES = (
    "cfg_table", "cfg_column", "cfg_unique", "cfg_enum", "cfg_connection", "cfg_api",
    "cfg_write_grant", "cfg_work_package", "cfg_step", "cfg_setting", "cfg_on_fail",
    "cfg_status_flow", "cfg_book_order", "cfg_candidate_rule", "cfg_utility",
)

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
        # inactive=0 filter added 2026-07-29 (escalation #334) — until this, `inactive` was
        # validator-only metadata: EVERY reader in this class ignored it, so "retiring" a row
        # never actually stopped it being read and applied. See BUILD.md sec37/GOVERNANCE.md sec15D.
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
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

    def may_write(self, writer: str) -> set[str]:
        """Which tables this writer (an api, a step, or 'run') is granted to write."""
        rows = {r["table_name"] for r in self.conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=? AND inactive=0", (writer,))}
        _trace(f"may_write({writer})", rows)
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
        """True if every step of this work package runs under one run_id in one PS invocation
        (so 'done' should wait for the last step); False if each step is invoked independently
        (so 'done' should fire on that step's own first ok/report-continue/self-heal). See
        cfg_work_package.chained, migration/add_work_package_chained_column.py. Not filtered by
        inactive here — by the time this is called, `run.py`'s own dispatch gate has already
        refused an inactive package/step outright; this only ever runs for an active one."""
        r = self.conn.execute("SELECT chained FROM cfg_work_package WHERE name=?",
                              (work_package,)).fetchone()
        return bool(r["chained"]) if r else True   # default chained=True: the old, safer behaviour

    def work_package_inactive(self, work_package: str) -> bool:
        """True if `work_package` has a `cfg_work_package` row and it is `inactive=1`, OR it has no
        row at all (an unknown package is never dispatchable either). Used by `run.py`'s dispatch
        gate (escalation #334) — checked explicitly, before anything else happens, not inferred
        from `step()`/`sequence()` silently returning nothing."""
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
        """`cfg_step.kind` (`'operations'` | `'utility'`) for `(work_package, step)`, or `None` if
        unset/unknown. Added 2026-07-30 — the researcher's operations/utility classification
        (`migration/bootstrap_step_kind.py`). Used by `run.py`'s dispatch gate: a step with no kind
        is refused the same way an inactive one already is — "routines not in the table[s] need
        special permission [a `configmaint.propose` classification] to be used.\""""
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
        """Found 2026-07-22: this was a static string from config/rules.json's seed, written
        once by cfgload.py and never touched again — configmaint.propose (the primary way config
        changes now) doesn't update it, so every run since 2026-07-21 pinned the SAME stale
        version regardless of how many real changes had been applied. Fixed by computing it live
        from the actual content of every cfg_* table (_VERSION_TABLES) — no write, no discipline
        required, always accurate, and it changes the moment the config actually does. The
        'app-0.1.0' prefix is kept as the human-readable major-version label from the original
        seed; the hash is what makes it a real fingerprint of current state."""
        base = self.conn.execute(
            "SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        prefix = base["value"] if base else "app"
        h = hashlib.sha256()
        for t in _VERSION_TABLES:
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
