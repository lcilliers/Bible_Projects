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
    "cfg_table", "cfg_column", "cfg_unique", "cfg_index", "cfg_enum", "cfg_connection", "cfg_api",
    "cfg_write_grant", "cfg_work_package", "cfg_step", "cfg_setting", "cfg_on_fail",
    "cfg_status_flow", "cfg_book_order", "cfg_candidate_rule", "cfg_utility",
)
# NOTE (2026-08-07): several cfg_* tables added after this list was written (cfg_quality_check,
# cfg_method_rule, cfg_report*, cfg_change_detail) are NOT in this list either — an existing,
# unresolved gap noted here rather than silently fixed as a side effect of the schema-remediation
# work this session; widening _VERSION_TABLES policy is a separate decision from adding cfg_index,
# which belongs here on its own terms (it drives DDL exactly like cfg_column/cfg_unique already do).

DB_PATH = pathlib.Path(__file__).resolve().parent.parent / "db" / "iba.db"
TRACE = os.environ.get("IBA_TRACE") == "1"


def _trace(what: str, value) -> None:
    if TRACE:
        v = value if isinstance(value, (str, int, float, bool, type(None))) else f"<{len(value)} rows>"
        print(f"    [cfg] {what:44} = {v}", file=sys.stderr)


class NonCompliantUtility(RuntimeError):
    """Raised by `Cfg.assert_utility_compliant()` — the module has a live `cfg_utility` row
    flagging hardcoded values that should be `cfg_setting`-driven (escalation #648), so it must
    not run as-is."""


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

    def required_setting(self, key: str):
        """Same lookup as `.setting()`, but NO literal default parameter -- raises if the key is
        missing or inactive, exactly the discipline `database_path()` already applies to database
        paths (`no database.{name}.path setting`, no silent fallback). Added 2026-08-29, researcher
        direct instruction after a full-codebase sweep found 41 of 60 `.setting(key, "literal")`
        call sites for output locations had a hardcoded literal that had drifted out of sync with
        the live `cfg_setting` row it was meant to default from -- current runtime behaviour was
        never actually wrong (`.setting()` always reads the live row first), but the literal was
        genuinely hardcoded, unverified, and unenforced: nothing ever checked it stayed in sync,
        and it silently would have taken over the moment the row went missing/inactive. Every call
        site that resolves a report/output path, or any other value that must be a single live
        config source of truth (not "config, or else this string"), now uses this instead of
        `.setting(key, "literal/path")` -- a missing/renamed/deactivated setting fails loudly here,
        not silently at the last hardcoded value it happened to agree with. See BUILD.md sec209."""
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        if r is None:
            raise KeyError(f"no active cfg_setting {key!r} -- every output location/value that "
                          f"must be config-driven needs a live row, not a hardcoded fallback in "
                          f"the calling code (governance.rules_must_be_config_driven)")
        val = json.loads(r["value"])
        _trace(f"required_setting {key}", val)
        return val

    def module_setting(self, table: str, key: str, default=None):
        """Generic reader for a per-module settings table shaped like cfg_setting (key/value/use/
        inactive) but scoped to one module -- e.g. cfg_passage (escalation #798/#799,
        governance.module.config). `table` is always a literal name supplied by the calling code,
        never external input."""
        r = self.conn.execute(
            f'SELECT value FROM "{table}" WHERE key=? AND inactive=0', (key,)).fetchone()
        val = json.loads(r["value"]) if r else default
        _trace(f"module_setting({table}, {key})", val)
        return val

    def required_module_setting(self, table: str, key: str):
        """Same as `.required_setting()`, for a per-module settings table instead of `cfg_setting`
        -- no literal default parameter, raises if the row is missing/inactive. Companion to
        `.module_setting()`, added the same round (2026-08-29, no-hardcoded-locations ruling)."""
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
        """Project-root-relative path to a registered project database, per `cfg_enum
        'project_database'`/`database.<name>.path` (escalation #723's settings; this method is
        their real consumer, added escalation #727 after both sat as genuine orphans — nothing
        read them). `database.<name>.path` is always READ (real `.setting()` usage either way, not
        skipped for 'iba') — but the RETURN VALUE for `name='iba'` is the already-known `DB_PATH`,
        not a value re-derived from the setting: bootstrapping the very first connection has to use
        the hardcoded `DB_PATH` constant (reading it from a row inside the database it locates
        would be circular, the same class of exception `lib/cfg.py` itself is `config_exempt`
        for) — but by the time this method runs, that connection already exists, so reading the
        setting here is a genuine post-bootstrap VERIFICATION (does the configured value still
        match where the DB actually lives?), not a bootstrap dependency. A mismatch is real drift,
        surfaced by `init.py`'s startup check, not silently ignored."""
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
    # `database='iba'` explicit on both queries below — escalation #653 (2026-08-17) widened
    # cfg_table/cfg_column to describe bible_research.db too (governance.tables/.table_columns:
    # "applies to all databases"), and the two DBs genuinely share table names (cluster/passage/
    # verse/word_registry, confirmed live) for DIFFERENT tables. `Cfg` is *"THE ONLY WAY THE APP
    # READS CONFIG"* for THIS running app's own DB — it must never resolve the other database's
    # row by accident (lib/db.py:build_data_tables() reads cfg_column and creates data tables from
    # it; scoping wrong here would try to build bible_research.db's tables inside iba.db).
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
        """Secondary (non-unique) indexes to build for this table — [(index_name, [cols])],
        cols in cfg_index.ordinal order, indexes in name order. `cfg_index` added 2026-08-07
        (schema-remediation-design-20260807.md): `build_data_tables()` already emitted FK/UNIQUE
        from config but had no mechanism for plain indexes at all — every FK column app-wide was a
        full-table-scan join target, invisible only because current row counts are still small."""
        rows = self.conn.execute(
            "SELECT name, col FROM cfg_index WHERE table_name=? ORDER BY name, ordinal",
            (table,)).fetchall()
        out: dict[str, list[str]] = {}
        for r in rows:
            out.setdefault(r["name"], []).append(r["col"])
        result = sorted(out.items())
        _trace(f"indexes({table})", result)
        return result

    def unique_key(self, table: str, database: str = "iba") -> list[str]:
        """The dedup key — the composite UNIQUE, else the single UNIQUE column, else the PK.
        `database` defaults to 'iba' (matches `may_write()`'s convention) — added escalation
        #723's supporting infra: all three queries here were missing a database filter entirely,
        the same shared-table-name ambiguity (`passage` exists in both DBs) `may_write()`/
        `columns()` were already fixed for, just never applied to this method."""
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
        """Raises `NonCompliantUtility` if `file_path`'s own `cfg_utility` row is flagged
        non-compliant (`purpose` prefixed `'NON-COMPLIANT (escalation #648'`) — the enforcement
        half of the researcher's 2026-08-17 instruction: a script with known hardcoded-config
        violations, put back into use, must signal that it needs revision (move the flagged
        values to `cfg_setting`) before running, not run silently as before. Called by a module's
        own entry point (its real caller — a handler dispatched via `run.py` — is the only place
        this can be checked in code); a caller passes its own `file_path` (typically `__file__`
        made project-relative). Deliberately narrow: only the ~2 of 105 flagged files that are
        importable library modules with a real dispatcher-reachable caller can be checked this
        way — the other ~103 are standalone scripts invoked directly (`python scripts/foo.py`),
        with no code-level checkpoint to hook into at all; enforcement for those is process
        discipline (check `cfg_utility` before running one), not something code can gate. See
        `governance.noncompliant_script_gate` for the full policy text."""
        row = self.conn.execute(
            "SELECT purpose FROM cfg_utility WHERE file_path=?", (file_path,)).fetchone()
        if row and row["purpose"] and row["purpose"].startswith("NON-COMPLIANT (escalation #648"):
            raise NonCompliantUtility(
                f"{file_path!r} is flagged non-compliant in cfg_utility and must be revised "
                f"(hardcoded values moved to cfg_setting) before use -- see its own purpose text, "
                f"or iba/app/reports/hardcoded-constants-sweep-20260817.md, for what needs to move.")

    def may_write(self, writer: str, database: str = "iba") -> set[str]:
        """Which tables this writer (an api, a step, or 'run') is granted to write.
        `database='iba'` default — escalation #680 widened cfg_write_grant to differentiate
        iba.db from bible_research.db (they share table names for different tables); every
        current call site writes to iba.db only, so the default keeps them all unchanged."""
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
