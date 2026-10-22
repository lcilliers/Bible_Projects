"""cfgquality.py — shared config-quality checks, used by handlers/configmaint.py (propose and
validate) and lib/cfgreport.py (CONFIG-REPORT.md). Kept separate to avoid a circular import
(configmaint imports cfgreport).
"""

from __future__ import annotations

import difflib
import io
import json
import pathlib
import re
import sqlite3
import tokenize

# module -> the dedicated table it already has: a new cfg_setting row for such a module needs a
# justification, since the module has a purpose-built home.
MODULE_DEDICATED_TABLE = {
    "candidate": "cfg_candidate_rule",
}

# quality-check step -> (table, key) of the setting holding where its findings persist
# (governance.reports_must_persist). Usually cfg_setting; a module with its own settings table
# (governance.module.config, e.g. cfg_passage) keeps it there.
QUALITY_CHECK_REPORT_PATH = {
    "configmaint.validate": ("cfg_setting", "configmaint.report_path"),  # -> CONFIG-REPORT.md
    "candidate.validate": ("cfg_setting", "candidate.quality_report_path"),
    "passage.validate": ("cfg_passage", "passage.quality_report_path"),
    "lexicon.validate": ("cfg_setting", "lexicon.quality_report_path"),
}

# Every step that writes a persistent report via reportkit.render_scaffold: the list cfg_report is
# checked against, so a step missing its row entirely is caught.
REPORT_STEPS = (
    "configmaint.report", "candidate.validate", "candidate.load", "passage.validate",
    "report.word", "validation.word", "validation.book", "retention.report",
    "report.seed_candidate", "report.strong_meaning", "report.span_analysis",
    "report.schema_overview", "report.registry", "lexicon.validate",
)


def _step_inactive(conn: sqlite3.Connection, step: str) -> bool:
    """True if `step` has cfg_step rows and all are inactive. REPORT_STEPS/QUALITY_CHECK_REPORT_PATH
    are hardcoded names, so checks keyed off them ask cfg_step explicitly (#310)."""
    rows = conn.execute("SELECT inactive FROM cfg_step WHERE step=?", (step,)).fetchall()
    return bool(rows) and all(r[0] for r in rows)


def find_missing_cfg_report_rows(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE step in REPORT_STEPS must have an active cfg_report row (title/ToC/footer/
    naming/CSV pairing); otherwise its report shape is still hardcoded. Inactive steps are skipped."""
    missing = []
    for step in REPORT_STEPS:
        if _step_inactive(conn, step):
            continue
        if not conn.execute(
                "SELECT 1 FROM cfg_report WHERE step=? AND inactive=0", (step,)).fetchone():
            missing.append(f"{step} produces a persistent report but has no active cfg_report row "
                          f"(title/sections/CSV pairing still hardcoded, or the row is inactive)")
    return missing


def find_chained_packages_missing_complete_message(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE chained work package needs cfg_work_package.complete_message, the wording of the
    COMPLETE banner PS prints at the end of its sequence. Inactive packages are skipped."""
    missing = []
    for r in conn.execute(
            "SELECT name FROM cfg_work_package WHERE chained=1 AND inactive=0 AND "
            "(complete_message IS NULL OR complete_message='')"):
        missing.append(f"{r[0]} is chained but has no cfg_work_package.complete_message")
    return missing


def find_settings_needing_justification(conn: sqlite3.Connection) -> list[str]:
    """A cfg_setting row whose module already has its own dedicated table -- advisory: surfaces
    each case needing a justification, without judging it. Inactive settings are skipped."""
    flags = []
    for module, table in MODULE_DEDICATED_TABLE.items():
        for r in conn.execute(
                "SELECT key FROM cfg_setting WHERE module=? AND inactive=0", (module,)):
            flags.append(f"cfg_setting {r[0]!r} (module {module!r}) — {module} already has its "
                         f"own dedicated table ({table}); confirm this belongs in shared "
                         f"cfg_setting rather than there")
    return flags


# Modules whose cfg_setting rows are documentation only -- facts for a human or an external process
# (e.g. 'backup': Windows Scheduled Tasks, standalone scripts), never applied via .setting(). Add a
# module only after checking its live rows (#719).
_NARRATIVE_MODULES = frozenset({"backup"})

# module='database' keys `database.<name>.path`, read via Cfg.database_path()'s f-string key, which
# the literal scan cannot see. Matched narrowly against that call site (#748).
_DATABASE_PATH_KEY = re.compile(r"^database\.[^.]+\.path$")


def find_orphan_configs(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """cfg_setting keys / cfg_enum groups without real usage -- configs the app would not respond to
    if they changed. ADVISORY: an orphan may be pre-staged for a step not yet built. Excludes
    iba/app/migration/ (migrations write initial values, so they always name the key).

    "Usage" differs by kind (#305):
      - a plain cfg_setting: the key literal appears in the same file as a `.setting(` /
        `.required_setting(` call (same file, not same call site, since some settings are read
        through a dict or loop).
      - a module='governance' setting: read by the startup routine (init.py / lib/compliance.py),
        by key or by the generic `module='governance'` read.
      - a cfg_enum group: queried by name at runtime (`cfg.enum(name)` or raw `cfg_enum WHERE
        name=...` SQL). Its values appearing as literals elsewhere is not usage.
    A setting or group read through `cfg_column.expectation` ('pattern:<key>', 'enum.<name>') is
    enforced by lib/valuequality.py and excluded first."""
    # .ps1 too: a PS script may read a setting through an inline `python -c` (e.g.
    # configmaint.auto_report in Config-Maintenance.ps1).
    per_file: dict[pathlib.Path, str] = {}
    for pattern in ("*.py", "*.ps1"):
        for f in app_root.rglob(pattern):
            if "migration" in f.relative_to(app_root).parts:
                continue
            try:
                per_file[f] = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
    corpus = "".join(per_file.values())
    init_corpus = per_file.get(app_root / "init.py", "")
    # the startup routine is init.py plus lib/compliance.py, where the rules are delivered (#2173)
    startup_corpus = init_corpus + per_file.get(app_root / "lib" / "compliance.py", "")
    governance_generic_read = (
        "module='governance'" in startup_corpus or 'module="governance"' in startup_corpus)

    expectations = {r[0] for r in conn.execute(
        "SELECT expectation FROM cfg_column WHERE expectation IS NOT NULL")}
    pattern_keys = {e[len("pattern:"):] for e in expectations if e.startswith("pattern:")}
    enum_names = {e[len("enum."):] for e in expectations if e.startswith("enum.")}

    orphans: list[str] = []
    for r in conn.execute("SELECT key, module FROM cfg_setting WHERE inactive=0"):
        key, module = r[0], r[1]
        if key in pattern_keys:
            continue
        if module == "governance":
            if (governance_generic_read or f'"{key}"' in init_corpus
                    or f"'{key}'" in init_corpus):
                continue
            orphans.append(f"cfg_setting {key!r} (module 'governance' — not read by "
                           f"iba/app/init.py, the startup routine)")
            continue
        if module in _NARRATIVE_MODULES:
            # documentation-only module (_NARRATIVE_MODULES): nothing to apply
            continue
        # .setting( or .required_setting( (the no-default accessor)
        used = any((f'"{key}"' in text or f"'{key}'" in text)
                  and (".setting(" in text or ".required_setting(" in text)
                  for text in per_file.values())
        if not used and module == "database" and _DATABASE_PATH_KEY.match(key):
            # Cfg.database_path() reads it through an f-string key (#748); confirmed by its call site
            cfgpy = per_file.get(app_root / "lib" / "cfg.py", "")
            if 'self.setting(f"database.{name}.path")' in cfgpy:
                used = True
        if not used:
            orphans.append(f"cfg_setting {key!r} (key not found together with a "
                           f"cfg.setting(...) call in any one file)")

    # clusterstatus._assert_enum_parity() reads both groups through a loop variable, which the regex
    # below cannot see (#1796); exempt only while that call site is confirmed present.
    _PARITY_CHECKED_ENUMS = {"cluster.status", "cluster_subgroup.status"}
    clusterstatus_py = per_file.get(app_root / "lib" / "clusterstatus.py", "")
    parity_confirmed = (
        "_assert_enum_parity" in clusterstatus_py
        and "cfg_enum WHERE name=?" in clusterstatus_py)

    for r in conn.execute("SELECT DISTINCT name FROM cfg_enum WHERE inactive=0"):
        name = r[0]
        if name in enum_names:
            continue
        if name in _PARITY_CHECKED_ENUMS and parity_confirmed:
            continue
        looked_up = re.search(
            r'(\.enum\(\s*|name\s*=\s*)["\']' + re.escape(name) + r'["\']', corpus)
        if not looked_up:
            orphans.append(f"cfg_enum group {name!r} (not looked up by name at runtime — "
                           f"no cfg.enum({name!r}) or cfg_enum WHERE name={name!r} call site)")
    return orphans


# Usage checks beyond cfg_setting/cfg_enum: cfg_book_order, cfg_connection, cfg_candidate_rule.

def find_orphan_book_order(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """`cfg.book_order()` reads the whole table as one dict, so the question is whether the accessor
    is called anywhere (migrations excluded). Also flags duplicate book/ordinal rows."""
    out: list[str] = []
    used = False
    for f in app_root.rglob("*.py"):
        if "migration" in f.relative_to(app_root).parts:
            continue
        try:
            text = _code_only_text(f)
        except OSError:
            continue
        if ".book_order(" in text:
            used = True
            break
    if not used:
        out.append("cfg_book_order: cfg.book_order() is not called anywhere outside migration/ "
                  "— the whole table is unused")

    books = [r[0] for r in conn.execute("SELECT book FROM cfg_book_order WHERE inactive=0")]
    for b in sorted({b for b in books if books.count(b) > 1}):
        out.append(f"cfg_book_order: {b!r} appears more than once")
    ordinals = [r[0] for r in conn.execute("SELECT ordinal FROM cfg_book_order WHERE inactive=0")]
    for o in sorted({o for o in ordinals if ordinals.count(o) > 1}):
        out.append(f"cfg_book_order: ordinal {o} is used by more than one book")
    return out


def find_orphan_connection_keys(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """Every active `cfg_connection.key` must co-occur with a `.connection(` call in the same file
    (the same method as find_orphan_configs's cfg_setting check)."""
    # raw text, not _code_only_text: the key being searched for is itself a string literal
    per_file: dict[pathlib.Path, str] = {}
    for f in app_root.rglob("*.py"):
        if "migration" in f.relative_to(app_root).parts:
            continue
        try:
            per_file[f] = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
    out = []
    for r in conn.execute("SELECT key FROM cfg_connection WHERE inactive=0"):
        key = r[0]
        used = any((f'"{key}"' in text or f"'{key}'" in text) and ".connection(" in text
                  for text in per_file.values())
        if not used:
            out.append(f"cfg_connection {key!r} — not read together with a cfg.connection(...) "
                      f"call in any one file")
    return out


# The steps whose code calls `.candidate_rules(...)`. While both are inactive, the first direction
# of the check (a kind called with no active rows) is skipped; the reverse direction always runs.
_CANDIDATE_RULES_CALLER_STEPS = ("candidate.seed", "candidate.curate")
_CANDIDATE_RULES_CALL_RE = re.compile(r"\.candidate_rules\(\s*[\"']([^\"']+)[\"']")


def find_orphan_candidate_rules(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """Two-directional usage check for `cfg_candidate_rule`: (a) code calls the accessor for a kind
    with zero active rows (skipped while _CANDIDATE_RULES_CALLER_STEPS are inactive); (b) a kind with
    active rows that no code asks for. Raw text, not _code_only_text: the kind name is a string
    literal. (This docstring avoids spelling out the call syntax, which the regex would match.)"""
    called_kinds: set[str] = set()
    for f in app_root.rglob("*.py"):
        if "migration" in f.relative_to(app_root).parts:
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        called_kinds.update(_CANDIDATE_RULES_CALL_RE.findall(text))

    active_kinds = {r[0] for r in conn.execute(
        "SELECT DISTINCT kind FROM cfg_candidate_rule WHERE inactive=0")}

    out = []
    callers_inactive = all(_step_inactive(conn, s) for s in _CANDIDATE_RULES_CALLER_STEPS)
    if not callers_inactive:
        for kind in sorted(called_kinds - active_kinds):
            out.append(f"cfg_candidate_rule: code calls candidate_rules({kind!r}) but there are "
                      f"ZERO active rows of that kind — the call will silently return []")
    for kind in sorted(active_kinds - called_kinds):
        out.append(f"cfg_candidate_rule: kind {kind!r} has active rows but no code calls "
                  f"candidate_rules({kind!r}) anywhere")
    return out


def find_bad_report_csv_table_references(conn: sqlite3.Connection) -> list[str]:
    """Every `cfg_report_csv_table.table_name` must name a real data table (`cfg_table`) or `cfg_*`
    table, or the `cfg_*` wildcard `reportkit.write_csv_pairing` recognises, or be marked `virtual`
    (a row_filter-supplied pairing whose rows the handler computes). A hard fault: a pairing for a
    missing, non-virtual table crashes write_csv_pairing when the report runs. A `virtual` row
    without a `join_note` is still flagged."""
    # database='iba': this app's own data tables
    data_tables = {r[0] for r in conn.execute("SELECT name FROM cfg_table WHERE database='iba'")}
    cfg_tables = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg\\_%' ESCAPE '\\'")}
    known = data_tables | cfg_tables
    out = []
    for r in conn.execute(
            "SELECT DISTINCT step, table_name, virtual, join_note FROM cfg_report_csv_table "
            "WHERE inactive=0"):
        name, is_virtual, join_note = r[1], r[2], r[3]
        if is_virtual:
            if join_note is None:
                out.append(f"schema: cfg_report_csv_table ({r[0]}).table_name {name!r} is marked "
                          f"virtual but carries no join_note explaining what it is")
            continue
        if name.endswith("*"):
            prefix = name[:-1]
            if not any(t.startswith(prefix) for t in known):
                out.append(f"schema: cfg_report_csv_table ({r[0]}) wildcard {name!r} matches no "
                          f"known table")
            continue
        if name not in known:
            out.append(f"schema: cfg_report_csv_table ({r[0]}).table_name {name!r} is not a "
                      f"known data or cfg_* table")
    return out


# Writer identities in cfg_write_grant that are not a cfg_step.step (dispatcher/API internals).
# Fallback only: the live list is cfg_enum `writer_identity`.
_WRITER_IDENTITY_FALLBACK = ("run", "escalation", "migration",
                             "call1_meanings", "call2_getInfo", "call3_strong")


def find_report_step_references(conn: sqlite3.Connection) -> list[str]:
    """Every active `cfg_report`/`cfg_report_section`/`cfg_report_csv_table.step` must name an
    ACTIVE `cfg_step.step` (as `_validate_live` does for `cfg_on_fail.step`). A hard fault."""
    active_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0")}
    out: list[str] = []
    for table in ("cfg_report", "cfg_report_section", "cfg_report_csv_table"):
        for r in conn.execute(f'SELECT DISTINCT step FROM "{table}" WHERE inactive=0'):
            if r[0] not in active_steps:
                out.append(f"schema: {table}.step {r[0]!r} is not a currently-active cfg_step")
    return out


def find_unknown_write_grant_writers(conn: sqlite3.Connection,
                                     writer_identities: set[str] | None = None) -> list[str]:
    """Every active `cfg_write_grant.writer` must be an ACTIVE `cfg_step.step` or a declared non-step
    writer identity (`_WRITER_IDENTITY_FALLBACK`/`enum.writer_identity`)."""
    active_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0")}
    identities = writer_identities or set(_WRITER_IDENTITY_FALLBACK)
    out: list[str] = []
    # database='iba': this app's own step/writer coherence
    for r in conn.execute("SELECT DISTINCT writer FROM cfg_write_grant WHERE database='iba' "
                          "AND inactive=0"):
        if r[0] not in active_steps and r[0] not in identities:
            out.append(f"schema: cfg_write_grant.writer {r[0]!r} is not an active cfg_step and "
                      f"not a declared writer identity")
    return out


def find_cfg_tables_missing_configmaint_grant(conn: sqlite3.Connection) -> list[str]:
    """Every `cfg_*` rule table (`category='rule'`) must have a `cfg_write_grant` row for writer
    `configmaint.propose`, the one sanctioned path for changing a `cfg_*` row
    (governance.config_control). Audit-log tables (cfg_change_detail, cfg_change_log) are not rule
    tables. A hard fault."""
    cfg_tables = {r[0] for r in conn.execute(
        "SELECT name FROM cfg_table WHERE database='iba' AND name LIKE 'cfg\\_%' ESCAPE '\\' "
        "AND category='rule'")}
    granted = {r[0] for r in conn.execute(
        "SELECT table_name FROM cfg_write_grant WHERE writer='configmaint.propose' "
        "AND database='iba'")}
    missing = sorted(cfg_tables - granted)
    return [f"schema: {t!r} has no cfg_write_grant row for writer 'configmaint.propose' — "
            f"nothing can maintain it through the sanctioned gate (governance.config_control)"
            for t in missing]


def find_unregistered_tables_and_columns(conn: sqlite3.Connection,
                                         project_root: pathlib.Path) -> list[str]:
    """`governance.tables`/`governance.table_columns`: every table in either database must be listed
    in `cfg_table`/`cfg_column`. Four shapes of drift, all hard errors:
    1. a live table with no `cfg_table` row;
    2. an ACTIVE `cfg_table` row naming a table that is not live (should be `inactive=1`);
    3. for a live, actively registered table, a live column with no `cfg_column` row;
    4. an ACTIVE `cfg_column` row naming a column not on its live table.
    `sqlite_%` tables are skipped."""
    def _db_path(name: str) -> pathlib.Path:
        r = conn.execute("SELECT value FROM cfg_setting WHERE key=?",
                         (f"database.{name}.path",)).fetchone()
        return project_root / json.loads(r["value"])

    out: list[str] = []
    for db_key in ("iba", "bible_research"):
        live_conn = conn if db_key == "iba" else sqlite3.connect(_db_path(db_key))
        try:
            live_tables = {r[0] for r in live_conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")}
            registered = {r["name"]: r["inactive"] for r in conn.execute(
                "SELECT name, inactive FROM cfg_table WHERE database=?", (db_key,))}
            for t in sorted(live_tables - registered.keys()):
                out.append(f"schema: table {t!r} ({db_key}.db) exists live but has no cfg_table "
                          f"row (governance.tables)")
            for t in sorted(n for n, inactive in registered.items()
                            if inactive == 0 and n not in live_tables):
                out.append(f"schema: cfg_table {t!r} ({db_key}) is active but the table no longer "
                          f"exists live — dropped/renamed without updating cfg_table.inactive")
            for t in sorted(live_tables & registered.keys()):
                if registered[t] != 0:
                    continue          # table itself inactive -- its columns aren't checked either
                live_cols = {r[1] for r in live_conn.execute(f'PRAGMA table_info("{t}")')}
                reg_cols = {r["name"]: r["inactive"] for r in conn.execute(
                    "SELECT name, inactive FROM cfg_column WHERE database=? AND table_name=?",
                    (db_key, t))}
                for c in sorted(live_cols - reg_cols.keys()):
                    out.append(f"schema: {t}.{c} ({db_key}.db) exists live but has no cfg_column "
                              f"row (governance.table_columns)")
                for c in sorted(cc for cc, inactive in reg_cols.items()
                                if inactive == 0 and cc not in live_cols):
                    out.append(f"schema: cfg_column {t}.{c} ({db_key}) is active but the column no "
                              f"longer exists live on that table")
        finally:
            if db_key != "iba":
                live_conn.close()
    return out


def _norm_sql(sql: str | None) -> str:
    return re.sub(r"\s+", " ", sql or "").strip()


def find_unregistered_triggers(conn: sqlite3.Connection, project_root: pathlib.Path) -> list[str]:
    """Live triggers against `cfg_trigger`, in both databases (#2110): `lib/db.py:trigger_ddl()`
    rebuilds them from config. Hard errors: a live trigger with no row; an active row naming a trigger
    that is not live; a live trigger whose SQL differs from its row (whitespace ignored)."""
    def _db_path(name: str) -> pathlib.Path:
        r = conn.execute("SELECT value FROM cfg_setting WHERE key=?",
                         (f"database.{name}.path",)).fetchone()
        return project_root / json.loads(r["value"])

    out: list[str] = []
    for db_key in ("iba", "bible_research"):
        live_conn = conn if db_key == "iba" else sqlite3.connect(_db_path(db_key))
        try:
            live = {r[0]: r[1] for r in live_conn.execute(
                "SELECT name, sql FROM sqlite_master WHERE type='trigger'")}
            reg = {r["name"]: (r["sql"], r["inactive"]) for r in conn.execute(
                "SELECT name, sql, inactive FROM cfg_trigger WHERE database=?", (db_key,))}
            for n in sorted(live.keys() - reg.keys()):
                out.append(f"schema: trigger {n!r} ({db_key}.db) exists live but has no "
                           f"cfg_trigger row (governance.tables)")
            for n in sorted(k for k, (_, inactive) in reg.items()
                            if inactive == 0 and k not in live):
                out.append(f"schema: cfg_trigger {n!r} ({db_key}) is active but the trigger is "
                           f"not live")
            for n in sorted(live.keys() & reg.keys()):
                if reg[n][1] == 0 and _norm_sql(live[n]) != _norm_sql(reg[n][0]):
                    out.append(f"schema: trigger {n!r} ({db_key}.db) differs from its cfg_trigger "
                               f"sql")
        finally:
            if db_key != "iba":
                live_conn.close()
    return out


def find_unregistered_project_scripts(conn: sqlite3.Connection,
                                      project_root: pathlib.Path) -> list[str]:
    """Every live `.py`/`.ps1` in the project outside an `archive/` folder must be in a utility or
    module (#2200, #2198; governance.new_utility_registration_timing): an active `cfg_utility` row,
    the handler module of a `cfg_step`, the `ps_script` of an active `cfg_work_package`, a hook or
    script named in `.claude/settings.json`, or a package marker (`__init__.py`). `temp_*` files are
    exempt (governance.scripts_and_routines). A file whose `cfg_utility` row is inactive but which
    still sits outside `archive/` is a retired script left live. A HARD error in configmaint.validate:
    anything else is retired into its folder's `archive/` (the researcher's ruling, #2200)."""
    # excluded on any path component (nested virtualenvs such as scripts/analytics/venv/)
    _EXCLUDE_ANYWHERE = {".git", "archive", "__pycache__", ".venv", "venv", "node_modules",
                        "site-packages"}
    util = {r[0]: r[1] for r in conn.execute("SELECT file_path, inactive FROM cfg_utility")}
    handlers = {r[0].split(":")[0].replace(".", "/") + ".py" for r in conn.execute(
        "SELECT handler FROM cfg_step WHERE handler IS NOT NULL")}
    ps_scripts = {(r[0] or "").replace("\\", "/") for r in conn.execute(
        "SELECT ps_script FROM cfg_work_package WHERE inactive=0")}
    settings = project_root / ".claude" / "settings.json"
    settings_text = settings.read_text(encoding="utf-8", errors="ignore") if settings.exists() else ""
    out: list[str] = []
    for f in sorted(list(project_root.rglob("*.py")) + list(project_root.rglob("*.ps1"))):
        rel = f.relative_to(project_root)
        if not rel.parts or _EXCLUDE_ANYWHERE & set(rel.parts):
            continue
        if f.stem == "__init__" or f.stem.startswith("temp_"):
            continue
        rel_posix = rel.as_posix()
        if util.get(rel_posix) == 0 or rel_posix in handlers or rel_posix in ps_scripts:
            continue
        if rel.parts[0] == ".claude" and f.name in settings_text:
            continue
        if util.get(rel_posix) == 1:
            out.append(f"{rel_posix} is retired (cfg_utility inactive) but not in archive/ -- move it")
        else:
            out.append(f"{rel_posix} is in no utility or module -- register it or retire it to archive/")
    return out


def find_filled_by_referencing_inactive_step(conn: sqlite3.Connection) -> list[str]:
    """`cfg_column.filled_by` naming an inactive step -- ADVISORY: each needs a judgement (the column
    may be dormant, or another active mechanism may now write it)."""
    inactive_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=1")}
    if not inactive_steps:
        return []
    out: list[str] = []
    for r in conn.execute(
            "SELECT table_name, name, filled_by FROM cfg_column WHERE filled_by IS NOT NULL "
            "AND inactive=0"):   # an inactive column is already settled as dormant (#2107)
        if r["filled_by"] in inactive_steps:
            out.append(f"{r['table_name']}.{r['name']} filled_by={r['filled_by']!r} "
                      f"(an inactive step) — confirm dormant or update to the real current writer")
    return out


def find_missing_report_paths(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE quality-check step (QUALITY_CHECK_REPORT_PATH) must have its output-path setting
    present, non-null and active (governance.reports_must_persist). Inactive steps are skipped."""
    missing = []
    for step, (table, key) in QUALITY_CHECK_REPORT_PATH.items():
        if _step_inactive(conn, step):
            continue
        row = conn.execute(
            f'SELECT value FROM "{table}" WHERE key=? AND inactive=0', (key,)).fetchone()
        if not row or not row[0]:
            missing.append(f"{step} has no active {key} setting in {table} — its findings would "
                          f"not persist to a report")
    return missing


def find_report_version_clutter(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """Detects a superseded one-off report version left live: `reportkit.oneoff_path()` archives
    before writing, so more than one live version per stem means a caller bypassed it."""
    from . import reportkit
    out_dir_setting = _cfg_setting(conn, "governance.oneoff_report_dir")
    if not out_dir_setting:
        return []
    # governance.oneoff_report_dir is relative to the repo root (app_root.parent.parent)
    out_dir_path = pathlib.Path(out_dir_setting)
    out_dir = out_dir_path if out_dir_path.is_absolute() else app_root.parent.parent / out_dir_path
    findings = []
    for base, items in reportkit.group_oneoff_versions(out_dir).items():
        if len(items) > 1:
            versions = sorted(v for v, _ in items)
            findings.append(f"{base}: {len(items)} versions simultaneously live "
                           f"({versions}) — only the highest should be; the rest belong in "
                           f"{out_dir_setting.rstrip('/')}/archive/")
    return findings


def _cfg_setting(conn: sqlite3.Connection, key: str):
    import json
    r = conn.execute("SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
    return json.loads(r["value"]) if r else None


def find_unregistered_lib_modules(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """Every `iba/app/lib/*.py` module must have a `cfg_utility` row, or find_utility_config_density
    cannot see it. ADVISORY: a new file mid-edit is a normal transient state."""
    registered = {r[0] for r in conn.execute("SELECT module FROM cfg_utility")}
    lib_dir = app_root / "lib"
    out = []
    if not lib_dir.exists():
        return out
    for f in sorted(lib_dir.glob("*.py")):
        if f.stem == "__init__":
            continue
        if f.stem not in registered:
            out.append(f"iba/app/lib/{f.name} has no cfg_utility row — run "
                      f"migration/bootstrap_cfg_utility.py to register it")
    return out


# Every method the `Cfg` class exposes, computed from the class itself, so any config-consuming call
# (`.setting(`, `.tables(`, ...) under any variable name counts.
_STRING_TOKEN_TYPES = {tokenize.COMMENT, tokenize.STRING}
for _name in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):    # Python 3.12+ only
    if hasattr(tokenize, _name):
        _STRING_TOKEN_TYPES.add(getattr(tokenize, _name))


def _code_only_text(path: pathlib.Path) -> str:
    """Source with every COMMENT/STRING (and f-string piece) span blanked to spaces in place, so a
    call-site scan isn't fooled by prose that mentions the pattern, while real call sites keep their
    exact adjacency. Falls back to raw text if a file doesn't tokenize."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError):
        return text
    line_starts = [0]
    for line in text.splitlines(keepends=True):
        line_starts.append(line_starts[-1] + len(line))
    chars = list(text)
    for tok in tokens:
        if tok.type not in _STRING_TOKEN_TYPES:
            continue
        start = line_starts[tok.start[0] - 1] + tok.start[1]
        end = line_starts[tok.end[0] - 1] + tok.end[1]
        for i in range(start, min(end, len(chars))):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


def _cfg_method_pattern() -> re.Pattern:
    from .cfg import Cfg
    methods = [m for m in dir(Cfg) if not m.startswith("_") and callable(getattr(Cfg, m))
              and m != "close"]
    return re.compile(r"\.(?:" + "|".join(re.escape(m) for m in methods) + r")\(")


_CFG_METHOD_RE = None  # built on first use, keeping the dependency on cfg one-way
_CFG_SQL_RE = re.compile(r"\b(?:FROM|JOIN|UPDATE|INTO)\s+cfg_\w+", re.IGNORECASE)


def find_utility_config_density(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE, non-exempt `cfg_utility` module with zero `Cfg`-method call sites in its own file
    (any method, any variable name; `_cfg_method_pattern`). ADVISORY: a module whose caller resolves
    its config is declared via `cfg_utility.config_exempt`. `file_path` is repo-root-relative,
    resolved against the CWD (every PS entry point sets the repo root)."""
    global _CFG_METHOD_RE
    if _CFG_METHOD_RE is None:
        _CFG_METHOD_RE = _cfg_method_pattern()
    out = []
    for r in conn.execute(
            "SELECT module, file_path FROM cfg_utility WHERE inactive=0 AND config_exempt=0"):
        path = pathlib.Path(r["file_path"])
        if not path.exists():
            out.append(f"cfg_utility {r['module']!r} — {path} no longer exists on disk")
            continue
        code = _code_only_text(path)
        # config read through a Cfg method, or by SQL on a cfg_* table (#2207 E)
        # SQL lives in string literals, so it is searched in the raw text
        if not (_CFG_METHOD_RE.search(code) or _CFG_SQL_RE.search(path.read_text(encoding="utf-8", errors="ignore"))):
            out.append(f"cfg_utility {r['module']!r} ({path}) has zero Cfg-method call sites "
                      f"(.setting()/.enum()/.tables()/... under any variable name) — confirm this "
                      f"is a legitimate zero (mark `cfg_utility.config_exempt=1` via "
                      f"`configmaint.propose`) or a real completeness gap")
    return out


# Escalation.ps1's `[ValidateSet(...)]` literals are a hardcoded copy of escalation vocabulary held
# in cfg_enum; this map names the parameters that must match their group exactly (PS -Parameter ->
# (cfg_enum group, value transform)). -State's ValidateSet is a deliberate subset (only settable
# states) and is not listed.
_PS_VALIDATESET_ENUM_MAP = {
    "NextAction": ("escalation_next_action_manual", lambda v: v),
    "Decision": ("escalation_next_action_dispatcher", lambda v: v.lower()),
    "Type": ("escalation_type", lambda v: v),
    "AnsweredBy": ("escalation_assignee", lambda v: v),
    "AssignedTo": ("escalation_assignee", lambda v: v),
}
_VALIDATESET_RE = re.compile(
    r"\[ValidateSet\((?P<items>(?:'[^']*'|\"[^\"]*\"|\s*,\s*)+)\)\]\s*\[\w+(?:\[\])?\]\s*\$(?P<param>\w+)")
_VALIDATESET_ITEM_RE = re.compile(r"'([^']*)'|\"([^\"]*)\"")


def ps_dir(conn: sqlite3.Connection, app_root: pathlib.Path) -> pathlib.Path:
    """The PS entry-point folder, from cfg_setting governance.scripts_ps_dir (repo-root-relative;
    #2208). `app_root` is iba/app, so the repo root is two levels up."""
    row = conn.execute("SELECT value FROM cfg_setting WHERE key='governance.scripts_ps_dir' AND "
                       "inactive=0").fetchone()
    if row is None:
        raise KeyError("cfg_setting governance.scripts_ps_dir is missing or inactive")
    return app_root.parent.parent / json.loads(row[0])


def _ps_validateset_drift(conn: sqlite3.Connection, ps_path: pathlib.Path, ps_label: str,
                          enum_map: dict) -> list[str]:
    """Every `enum_map` parameter's `[ValidateSet(...)]` values in `ps_path` must exactly match the
    live `cfg_enum` group it mirrors (#977)."""
    if not ps_path.exists():
        return [f"{ps_label} not found at {ps_path} — cannot check ValidateSet drift"]
    text = ps_path.read_text(encoding="utf-8", errors="ignore")
    found: dict[str, list[str]] = {}
    for m in _VALIDATESET_RE.finditer(text):
        param = m.group("param")
        if param not in enum_map:
            continue
        items = [a or b for a, b in _VALIDATESET_ITEM_RE.findall(m.group("items"))]
        found[param] = items

    out = []
    for param, (enum_name, transform) in enum_map.items():
        if param not in found:
            out.append(f"{ps_label}: -{param} has no [ValidateSet(...)] found (expected to "
                      f"mirror cfg_enum {enum_name!r})")
            continue
        ps_values = {transform(v) for v in found[param]}
        live_values = {r[0] for r in conn.execute(
            "SELECT value FROM cfg_enum WHERE name=? AND inactive=0", (enum_name,))}
        missing = live_values - ps_values
        extra = ps_values - live_values
        if missing:
            out.append(f"{ps_label}: -{param} ValidateSet is missing {sorted(missing)} "
                      f"(present in live cfg_enum {enum_name!r} but not the PS ValidateSet)")
        if extra:
            out.append(f"{ps_label}: -{param} ValidateSet has {sorted(extra)} which is not in "
                      f"live cfg_enum {enum_name!r} — stale or renamed")
    return out


def find_escalation_ps_validateset_drift(conn: sqlite3.Connection, app_root: pathlib.Path
                                         ) -> list[str]:
    """Escalation.ps1's `_PS_VALIDATESET_ENUM_MAP` parameters against their cfg_enum groups
    (after `-Decision`'s lowercase transform). ADVISORY: the script may not be updated yet."""
    return _ps_validateset_drift(conn, ps_dir(conn, app_root) / "Escalation.ps1", "Escalation.ps1",
                                 _PS_VALIDATESET_ENUM_MAP)


_FOLDERPURPOSE_PS_VALIDATESET_ENUM_MAP = {
    "Type": ("folder_purpose_type", lambda v: v),
    "Status": ("folder_purpose_status", lambda v: v),
}


def find_folderpurpose_ps_validateset_drift(conn: sqlite3.Connection, app_root: pathlib.Path
                                            ) -> list[str]:
    """`FolderPurpose.ps1`'s `-Type`/`-Status` `[ValidateSet(...)]` values against the live cfg_enum
    groups they mirror (#977). folderpurpose.auto_assess() checks its own literal vocabulary at run
    time."""
    return _ps_validateset_drift(conn, ps_dir(conn, app_root) / "FolderPurpose.ps1", "FolderPurpose.ps1",
                                 _FOLDERPURPOSE_PS_VALIDATESET_ENUM_MAP)


# ── PS-script vs. Excel-worksheet drift ─────────────────────────────────────────────────────────
# Two workbooks are the researcher's CLI interface to iba/app/ps: `iba/docs/ps tools worksheet.xlsx`
# (one tab per script, row 4 = flag headers, built from each script's param() block) and
# `iba/docs/escalation actions worksheet.xlsx` (hand-built, one sheet, fixed action shapes for
# Escalation.ps1). The first gets a strict per-script tab match; the second a subset check.
_PS_WORKSHEET_SKIP_STEMS = {"Escalation"}  # its tab is a pointer to the model sheet, not real headers
# PowerShell automatic variables that can appear inside a param() block without being a parameter,
# e.g. `[Parameter(Mandatory = $true)]`.
_PS_AUTOMATIC_VARS = {"true", "false", "null"}


def _ps_param_names(ps_path: pathlib.Path) -> set[str]:
    """Every declared parameter name in `ps_path`'s outer `param(...)` block, bracket-depth aware
    (a `[ValidateSet('a','b')]` closing paren must not end the block)."""
    text = ps_path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"\bparam\s*\(", text, re.I)
    if not m:
        return set()
    i, depth = m.end(), 1
    while i < len(text) and depth > 0:
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
        i += 1
    body = text[m.end():i - 1]
    return {mm.group(1) for mm in re.finditer(r"\$(\w+)", body)
           if mm.group(1).lower() not in _PS_AUTOMATIC_VARS}


def _load_worksheet_setting(conn: sqlite3.Connection, key: str, project_root: pathlib.Path
                            ) -> tuple[pathlib.Path | None, str | None]:
    """Resolves a `governance.*_worksheet_path` setting to a real file — returns (path, None) or
    (None, error-string) so callers can surface a config gap as a finding rather than crashing."""
    row = conn.execute(
        "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
    if not row:
        return None, f"{key} is not set — cannot check PS/worksheet drift"
    wb_path = project_root / json.loads(row[0])
    if not wb_path.exists():
        return None, f"{key} points at {wb_path} — file does not exist"
    return wb_path, None


def _index_ps_worksheet_tabs(wb) -> dict[str, "openpyxl.worksheet.worksheet.Worksheet"]:
    """Maps a script's embedded path cell (e.g. `iba\\app\\ps\\Behaviour.ps1`, row 6 col A of its tab)
    back to that worksheet, scanning every tab once. The path, not the tab name, is the anchor: Excel's
    31-char limit shortens some tab names."""
    idx: dict[str, object] = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=1, max_row=8, max_col=3, values_only=True):
            for cell in row:
                if isinstance(cell, str) and cell.strip().lower().endswith(".ps1"):
                    idx[cell.strip().replace("/", "\\").lower()] = ws
    return idx


def find_ps_worksheet_drift(conn: sqlite3.Connection, app_root: pathlib.Path,
                            project_root: pathlib.Path) -> list[str]:
    """Every `iba/app/ps/*.ps1` script's live `param()` names against its tab's row-4 flag headers
    in `governance.ps_worksheet_path`. ADVISORY. `Escalation.ps1` is skipped: its tab points to the
    other worksheet, checked below."""
    try:
        import openpyxl
    except ImportError:
        return ["openpyxl not importable — cannot check PS/worksheet drift"]
    wb_path, error = _load_worksheet_setting(conn, "governance.ps_worksheet_path", project_root)
    if error:
        return [error]
    wb = openpyxl.load_workbook(wb_path, data_only=False)
    tabs = _index_ps_worksheet_tabs(wb)
    out = []
    for ps_file in sorted(ps_dir(conn, app_root).glob("*.ps1")):
        if ps_file.stem in _PS_WORKSHEET_SKIP_STEMS:
            continue
        key = f"iba\\app\\ps\\{ps_file.name}".lower()
        ws = tabs.get(key)
        if ws is None:
            out.append(f"{ps_file.name}: no tab found in {wb_path.name} (expected an embedded "
                      f"path cell {key!r} in some tab's first rows)")
            continue
        live = _ps_param_names(ps_file)
        sheet = {c[1:] for row in ws.iter_rows(min_row=4, max_row=4, values_only=True)
                for c in row if isinstance(c, str) and c.startswith("-")}
        # PowerShell parameter names are case-insensitive
        sheet_lower = {s.lower() for s in sheet}
        live_lower = {p.lower() for p in live}
        missing = {p for p in live if p.lower() not in sheet_lower}
        extra = {s for s in sheet if s.lower() not in live_lower}
        if missing:
            out.append(f"{ps_file.name}: {wb_path.name} tab {ws.title!r} is missing flag "
                      f"column(s) {sorted(missing)} — the script has these parameters now")
        if extra:
            out.append(f"{ps_file.name}: {wb_path.name} tab {ws.title!r} has flag column(s) "
                      f"{sorted(extra)} the script no longer has — stale or renamed")
    return out


def find_escalation_worksheet_drift(conn: sqlite3.Connection, app_root: pathlib.Path,
                                    project_root: pathlib.Path) -> list[str]:
    """Each of `Escalation.ps1`'s live `param()` names must appear somewhere as a `-Flag` header in
    `governance.escalation_worksheet_path` -- a subset check, since that one sheet shares columns
    across several action shapes."""
    try:
        import openpyxl
    except ImportError:
        return ["openpyxl not importable — cannot check PS/worksheet drift"]
    wb_path, error = _load_worksheet_setting(conn, "governance.escalation_worksheet_path",
                                             project_root)
    if error:
        return [error]
    live = _ps_param_names(ps_dir(conn, app_root) / "Escalation.ps1")
    wb = openpyxl.load_workbook(wb_path, data_only=False)
    used = {c[1:] for ws in wb.worksheets for row in ws.iter_rows(values_only=True)
           for c in row if isinstance(c, str) and c.startswith("-") and " " not in c}
    used_lower = {u.lower() for u in used}
    missing = {p for p in live if p.lower() not in used_lower}
    if missing:
        return [f"Escalation.ps1 has parameter(s) {sorted(missing)} not used as a -Flag header "
                f"anywhere in {wb_path.name} — the researcher's model sheet may need updating"]
    return []


def find_unclassified_active_steps(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE `cfg_step` must have `kind` set (`operations` | `utility`). A hard error:
    `run.py` refuses to dispatch a step with no kind. (`find_enum_violations` catches an invalid
    value; this catches a missing one.)"""
    return [f"cfg_step ({r['work_package']}, {r['step']}) is active but has no kind "
           f"(operations|utility) — classify it via configmaint.propose before it can be "
           f"dispatched (run.py now refuses undispatched steps with no kind)"
           for r in conn.execute(
               "SELECT work_package, step FROM cfg_step WHERE inactive=0 AND kind IS NULL")]


def find_unresolvable_location_settings(conn: sqlite3.Connection, project_root: pathlib.Path
                                       ) -> list[str]:
    """Every location-shaped config value (`cfg_setting` and every per-module table shaped like it;
    `lib/folderpurpose.location_settings()`) must resolve to a real folder, project-root-relative.
    ADVISORY: a report folder may be created on first write (#971/#976)."""
    from . import folderpurpose as fp_mod

    out = []
    for table, key, raw_value in fp_mod.location_settings(conn):
        norm = fp_mod.normalize_setting_value(raw_value)
        if norm is None:
            continue  # not a bare folder path (a sentence, a {template}, a JSON list)
        if not (project_root / norm).is_dir():
            out.append(f"{table}.{key} = {raw_value!r} — {norm!r} does not exist as a folder "
                      f"on disk (project-root-relative)")
    return out


# `filing` behaviour class item 4: a write that builds a "-v{...}" / "-v" + str(...) filename by hand
# instead of calling filingkit.versioned_path() / reportkit.oneoff_path().
_HAND_VERSION_RE = re.compile(r"-v\{[^}]*\}|-v[\"']\s*\+")
_FILINGKIT_CALL_RE = re.compile(r"\b(?:versioned_path|oneoff_path)\s*\(")
_FILING_SCAN_EXCLUDE_ANYWHERE = {".git", "archive", "__pycache__", ".venv", "venv",
                                "node_modules", "site-packages", "migration",
                                # engine/ is superseded; its -v{n} matches are documentary naming patterns
                                "engine"}


def _strip_comments(text: str) -> str:
    """Blanks COMMENT token spans only (string literals stay), so a comment that mentions '-v{n}'
    does not match."""
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError):
        return text
    line_starts = [0]
    for line in text.splitlines(keepends=True):
        line_starts.append(line_starts[-1] + len(line))
    chars = list(text)
    for tok in tokens:
        if tok.type != tokenize.COMMENT:
            continue
        start = line_starts[tok.start[0] - 1] + tok.start[1]
        end = line_starts[tok.end[0] - 1] + tok.end[1]
        for i in range(start, min(end, len(chars))):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


def find_hand_rolled_versioning(conn: sqlite3.Connection, project_root: pathlib.Path
                                ) -> list[str]:
    """`filing` behaviour class rule 4 (archiving-trigger, naming-shape): every active (or
    unregistered) `.py` file building a `-v{n}` filename by hand should call
    `filingkit.versioned_path()` or `reportkit.oneoff_path()`. ADVISORY. `iba/app/migration/` is
    excluded (its filename literals are seed data)."""
    inactive = {r[0] for r in conn.execute("SELECT file_path FROM cfg_utility WHERE inactive=1")}
    out = []
    for f in sorted(project_root.rglob("*.py")):
        rel = f.relative_to(project_root)
        parts = rel.parts
        if not parts or _FILING_SCAN_EXCLUDE_ANYWHERE & set(parts):
            continue
        if f.stem == "__init__" or f.stem.startswith("temp_"):
            continue
        rel_posix = rel.as_posix()
        if rel_posix in inactive:
            continue
        if rel_posix in ("iba/app/lib/filingkit.py", "iba/app/lib/reportkit.py"):
            continue  # the canonical implementation itself, not a caller reinventing it
        # exempt by researcher ruling (#2108 F): prosestore.py's cross-day edit-cycle counter and the
        # one-off analysis scripts under _analytics/
        if rel_posix == "iba/app/lib/prosestore.py" or parts[0] == "_analytics":
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        code_text = _strip_comments(text)
        if _HAND_VERSION_RE.search(code_text) and not _FILINGKIT_CALL_RE.search(text):
            out.append(f"{rel_posix} builds a -v{{n}} filename by hand — no filingkit."
                      f"versioned_path()/reportkit.oneoff_path() call site in the same file")
    return out


# ── unenforced behaviour rules ─────────────────────────────────────────────────────────────────
def find_rule_scope_gaps(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """#2209: every rule knows the operations it governs. A coherence ERROR, each case must be zero:
    an active rule (behaviour, escalation, governance setting that is a rule) with no active
    cfg_rule_scope link; a link to a rule that is missing or inactive; a `ps` link naming a script
    not in the PS folder; an active method rule on a step that is not active."""
    if not conn.execute("SELECT 1 FROM sqlite_master WHERE name='cfg_rule_scope'").fetchone():
        return ["cfg_rule_scope is missing (#2209)"]
    values = set()
    row = conn.execute("SELECT value FROM cfg_setting WHERE key='compliance.value_settings' AND "
                       "inactive=0").fetchone()
    if row:
        values = set(json.loads(row[0]))
    live = {f"B:{i}" for (i,) in conn.execute("SELECT id FROM cfg_behaviour_rule WHERE active=1")}
    live |= {f"E:{i}" for (i,) in conn.execute("SELECT id FROM cfg_escalation WHERE active=1")}
    live |= {f"G:{k}" for (k,) in conn.execute(
        "SELECT key FROM cfg_setting WHERE module='governance' AND inactive=0") if k not in values}
    links = conn.execute("SELECT rule_ref, scope_kind, scope_value FROM cfg_rule_scope "
                         "WHERE inactive=0").fetchall()
    linked = {r[0] for r in links}
    out = [f"rule {r} has no cfg_rule_scope link" for r in sorted(live - linked)]
    out += [f"cfg_rule_scope links {r}, which is missing or inactive" for r in sorted(linked - live)]
    folder = ps_dir(conn, app_root)
    for ref, kind, value in links:
        if kind == "ps" and not (folder / value.split(" ")[0]).exists():
            out.append(f"cfg_rule_scope {ref} names PS script {value.split(' ')[0]}, not in {folder.name}/")
    out += [f"method rule {i} ({k}) is active on step {s}, which is not active" for i, k, s in conn.execute(
        "SELECT m.id, m.rule_key, m.step FROM cfg_method_rule m LEFT JOIN cfg_step s ON s.step = m.step "
        "WHERE m.active=1 AND COALESCE(s.inactive, 1)=1 ORDER BY m.id")]
    return out


def find_unenforced_behaviour_rules(conn: sqlite3.Connection) -> list[str]:
    """Every active `cfg_behaviour_rule` with no control (#1384): its `enforcement_status` (cfg_enum
    `behaviour_rule_enforcement_status`) is neither `mechanically_enforced` nor `context_delivered`.
    A context_delivered rule is restated at session start and proved at close by the compliance
    file (#2173 P2, lib/compliance.py), so it is not counted here (#2206 option 2a). ADVISORY."""
    rows = conn.execute(
        "SELECT id, class, rule_key, enforcement_status FROM cfg_behaviour_rule "
        "WHERE active=1 AND (enforcement_status IS NULL OR enforcement_status NOT IN "
        "('mechanically_enforced', 'context_delivered')) "
        "ORDER BY class, id").fetchall()
    out = []
    for r in rows:
        status = r["enforcement_status"] or "UNCLASSIFIED (missing enforcement_status — audit gap itself)"
        out.append(f"[{r['class']}] #{r['id']} {r['rule_key']} — {status}")
    return out


# ── mechanically checkable behaviour rules (#1384) ─────────────────────────────────────────────
def find_unpushed_commits(project_root: pathlib.Path) -> list[str]:
    """`cfg_behaviour_rule` 26 (git-commit-and-push-together): no unpushed commit, via
    `git rev-list --count @{u}..HEAD`. Returns an empty list if there is no repo or upstream."""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "rev-list", "--count", "@{u}..HEAD"],
            cwd=project_root, capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            return []
        count = int(result.stdout.strip() or "0")
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return []
    if count == 0:
        return []
    return [f"{count} local commit(s) ahead of the upstream branch, not pushed"]


def find_ps_scripts_bypassing_runpy(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """`cfg_behaviour_rule` 43: every PS script under iba/app/ps/ that performs an operation calls
    `python -m iba.app.run`, not a module directly. Named exceptions: Start-Iba.ps1, and
    Escalation.ps1's manual front-door actions. A simple substring scan."""
    folder = ps_dir(conn, app_root)
    if not folder.exists():
        return []
    exempt = {"Start-Iba.ps1", "Escalation.ps1"}
    out = []
    for f in sorted(folder.glob("*.ps1")):
        if f.name in exempt:
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        has_runpy = re.search(r"python\s+-m\s+iba\.app\.run\b", text) is not None
        has_direct = re.search(r"python\s+-m\s+iba\.app\.(handlers|lib|tools)\b", text) is not None
        if has_direct and not has_runpy:
            out.append(f"{f.relative_to(app_root.parent.parent).as_posix()} calls iba.app.(handlers|lib|tools) directly, no "
                      f"iba.app.run dispatch found in the same file")
    return out


def find_steps_without_ps_script(conn: sqlite3.Connection) -> list[str]:
    """`cfg_behaviour_rule` 41: every active `cfg_step` belongs to a `cfg_work_package` with a
    `ps_script` set."""
    rows = conn.execute(
        "SELECT DISTINCT s.work_package FROM cfg_step s LEFT JOIN cfg_work_package w "
        "ON s.work_package = w.name WHERE s.inactive=0 AND "
        "(w.ps_script IS NULL OR w.ps_script = '' OR w.name IS NULL)").fetchall()
    return [f"work package '{r['work_package']}' has an active step but no cfg_work_package."
            f"ps_script (or no cfg_work_package row at all)" for r in rows]


_ESCALATION_HEADER_RE = re.compile(r"Escalation\s+#(\d+)(?:/#(\d+))?")


def find_escalation_file_naming_violations(conn: sqlite3.Connection, project_root: pathlib.Path
                                           ) -> list[str]:
    """`cfg_behaviour_rule` 64 + 56: a file in Workflow/Catalogue/ or iba/docs/ whose first 15 lines
    declare '> Escalation #N' should be named '{N}-...'. Also flags a filename with a raw space or an
    'Untitled' stem. ADVISORY; a file with no escalation header is out of scope."""
    out = []
    for folder in (project_root / "Workflow" / "Catalogue", project_root / "iba" / "docs"):
        if not folder.exists():
            continue
        for f in sorted(folder.rglob("*.md")):
            rel = f.relative_to(project_root).as_posix()
            if "archive" in f.relative_to(folder).parts[:-1]:   # history is not renamed (#2207 A)
                continue
            if " " in f.name:
                out.append(f"{rel} — filename contains a space (naming-shape: hyphens only)")
            if f.stem.lower().startswith("untitled"):
                out.append(f"{rel} — literally untitled")
            try:
                head = "\n".join(f.read_text(encoding="utf-8", errors="ignore").splitlines()[:15])
            except OSError:
                continue
            matches = _ESCALATION_HEADER_RE.findall(head)
            if not matches:
                continue
            candidate_ids = sorted({g for pair in matches for g in pair if g}, key=int)
            # any escalation named in the header satisfies the check
            if any(f.name.startswith(f"{eid}-") for eid in candidate_ids):
                continue
            out.append(f"{rel} — header names Escalation #{'/#'.join(candidate_ids)}, filename "
                      f"doesn't start with any of them")
    return out


def find_hedge_phrases_in_active_config(conn: sqlite3.Connection) -> list[str]:
    """`cfg_behaviour_rule` 32 applied to the config's own text: an ACTIVE cfg_behaviour_rule /
    cfg_method_rule / cfg_setting row still carrying a bare 'not yet'/'TBD'/'to be decided'.
    Behaviour rules with an enforcement_status are excluded (that column is the authority)."""
    hedges = ("not yet mechanically checked", "not yet built", "not yet applied", "not yet done",
             "not yet decided", "not yet determined", "not yet resolved", "not yet implemented",
             "not yet enforced", "not yet reviewed", "not yet confirmed", "not-yet-decided",
             "not resolved here", "TBD", "to be decided")
    out = []
    rows = conn.execute("SELECT id, rule_key, rule_text, enforced_by FROM cfg_method_rule "
                        "WHERE active=1").fetchall()
    for r in rows:
        blob = f"{r['rule_text'] or ''} {r['enforced_by'] or ''}"
        if any(h.lower() in blob.lower() for h in hedges):
            out.append(f"cfg_method_rule #{r['id']} {r['rule_key']} — hedge phrase in rule_text/"
                      f"enforced_by with no resolution")
    rows = conn.execute("SELECT key, value, use FROM cfg_setting WHERE inactive=0").fetchall()
    for r in rows:
        blob = f"{r['value'] or ''} {r['use'] or ''}"
        if any(h.lower() in blob.lower() for h in hedges) and "deferred-transaction" not in blob:
            out.append(f"cfg_setting {r['key']} — hedge phrase in value/use")
    return out


def find_query_file_convention_violations(project_root: pathlib.Path) -> list[str]:
    """`cfg_behaviour_rule` 14 (query-file-conventions): an SQL scratch file lives under
    scripts/SQLite/{IBA_DB,Research_DB}/, hyphenated, never untitled. Detection only; no rename."""
    sql_dir = project_root / "scripts" / "SQLite"
    out = []
    if sql_dir.exists():
        for f in sorted(sql_dir.rglob("*.sqlite3-query")):
            if " " in f.name:
                out.append(f"{f.relative_to(project_root).as_posix()} — contains a space, "
                          f"should use hyphens")
            if f.stem.lower().startswith("untitled"):
                out.append(f"{f.relative_to(project_root).as_posix()} — untitled, needs a real "
                          f"descriptive name")
    scripts_dir = project_root / "scripts"
    if scripts_dir.exists():
        for f in sorted(scripts_dir.glob("SQLite_*.sqlite3-query")):
            out.append(f"{f.relative_to(project_root).as_posix()} — uses the retired flat "
                      f"SQLite_-prefix form, should live under scripts/SQLite/"
                      f"{{IBA_DB,Research_DB}}/")
    return out


def find_restated_authoritative_content(conn: sqlite3.Connection, project_root: pathlib.Path,
                                        min_ratio: float = 0.8) -> list[str]:
    """`cfg_behaviour_rule` 3: a paragraph in a control file or USER-GUIDE.md that near-duplicates an
    active cfg_setting/cfg_behaviour_rule/cfg_method_rule row is a restatement, not a pointer.
    Compared in memory: difflib quick_ratio() as a pre-filter, ratio() on survivors, min_ratio 0.8."""
    # the control files (cfg_control_home, session_close.control_kinds) plus USER-GUIDE.md
    docs = {}
    files = [f for _, f, _ in control_files(conn, project_root)]
    files += [project_root / "iba/app/USER-GUIDE.md"]
    for p in dict.fromkeys(files):
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        try:
            rel = p.relative_to(project_root).as_posix()
        except ValueError:
            rel = "memory/" + p.name
        docs[rel] = [x.strip() for x in text.split("\n\n") if len(x.strip()) > 150]

    rows: list[tuple[str, str]] = []
    for table, col, where in (("cfg_setting", "value", "inactive=0"),
                              ("cfg_behaviour_rule", "rule_text", "active=1"),
                              ("cfg_method_rule", "rule_text", "active=1")):
        for r in conn.execute(f"SELECT {col} AS txt FROM {table} WHERE {where}").fetchall():
            if r["txt"] and len(r["txt"]) > 150:
                rows.append((table, r["txt"]))

    out = []
    for table, txt in rows:
        for docname, paras in docs.items():
            for p in paras:
                sm = difflib.SequenceMatcher(None, txt, p)
                if sm.quick_ratio() < min_ratio:
                    continue
                if sm.ratio() >= min_ratio:
                    out.append(f"{table} row (starts: {txt[:60]!r}) closely matches a paragraph "
                              f"in {docname} (starts: {p[:60]!r}) — restatement, not a pointer?")
    return out


# ── control files (#2186) ───────────────────────────────────────────────────────────────────────
_CTRL_PATH_RX = re.compile(
    r"(?:\]\(|`)((?:~|\.{1,2}/)?[\w.-]+(?:/[\w. -]+)*\.(?:md|py|ps1|json|csv|xlsx|txt))(?:\)|`)")


def _setting(conn, key):
    row = conn.execute("SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
    if row is None:
        raise KeyError(f"cfg_setting {key} missing")
    return json.loads(row[0])


def control_files(conn: sqlite3.Connection, project_root: pathlib.Path) -> list[tuple[str, pathlib.Path, str]]:
    """[(kind, file, read_when)] -- the live files of the control-map kinds that
    session_close.control_kinds names (cfg_control_home). A folder home contributes its *.md files
    (never its archive/); the memory home is the Claude memory folder."""
    kinds = set(_setting(conn, "session_close.control_kinds"))
    out = []
    for kind, home, read_when in conn.execute(
            "SELECT kind, home, read_when FROM cfg_control_home WHERE inactive=0 ORDER BY rowid"):
        if kind not in kinds:
            continue
        m = re.search(r"(~?[\w./-]*/[\w./-]*|[\w.-]+\.md)", home)
        if not m:
            continue
        ref = m.group(1)
        base = (pathlib.Path.home() / ref[2:]) if ref.startswith("~/") else project_root / ref
        if base.is_dir():
            out += [(kind, f, read_when) for f in sorted(base.glob("*.md"))]
        elif base.is_file():
            out.append((kind, base, read_when))
        else:
            out.append((kind, base, read_when))  # reported as missing by the check
    return out


def find_control_file_problems(conn: sqlite3.Connection, project_root: pathlib.Path) -> list[tuple[str, str]]:
    """Session-close SC15 (#2186): [(key, text)] for every control file (control_files):
      - the file is missing
      - a path it names does not resolve (relative to the file, then the project root)
      - a path it names is in an archive/ folder, on a line that does not carry the history marker
        (session_close.history_pointer_word): a live pointer into history
      - it carries replaced-history text (session_close.history_markers; rule 96)
      - an always-read file is over session_close.always_read_max_bytes."""
    marker = _setting(conn, "session_close.history_pointer_word").lower()
    patterns = [re.compile(p) for p in _setting(conn, "session_close.history_markers")]
    max_bytes = int(_setting(conn, "session_close.always_read_max_bytes"))
    out = []
    for kind, f, read_when in control_files(conn, project_root):
        try:
            rel = f.relative_to(project_root).as_posix()
        except ValueError:
            rel = "memory/" + f.name
        if not f.is_file():
            out.append((f"SC15:{rel}:missing", f"`{rel}` (control kind {kind}) does not exist"))
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        always_read = read_when == "always" and (kind != "claude_memory" or f.name == "MEMORY.md")
        if always_read and len(text.encode("utf-8")) > max_bytes:
            out.append((f"SC15:{rel}:size", f"`{rel}` is read every conversation and is "
                        f"{len(text.encode('utf-8'))} bytes, over {max_bytes}"))
        in_fence = False
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            for p in patterns:
                if p.search(line):
                    out.append((f"SC15:{rel}:{n}:history", f"`{rel}` line {n} carries replaced-"
                                f"history text ({p.pattern!r}): {line.strip()[:90]}"))
                    break
            if in_fence:
                continue
            for ref in _CTRL_PATH_RX.findall(line):
                if any(ch in ref for ch in "*{}<>") or "..." in ref:
                    continue
                cand = [(f.parent / ref), (project_root / ref)]
                if ref.startswith("~/"):
                    cand = [pathlib.Path.home() / ref[2:]]
                hit = next((c for c in cand if c.exists()), None)
                if hit is None:
                    out.append((f"SC15:{rel}:{n}:{ref}", f"`{rel}` line {n} names `{ref}`, which "
                                f"does not resolve"))
                elif "archive" in hit.resolve().parts and marker not in line.lower():
                    out.append((f"SC15:{rel}:{n}:{ref}", f"`{rel}` line {n} points into an archive "
                                f"(`{ref}`) without marking it as history"))
    return out
