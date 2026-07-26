"""cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the
propose-time / validate-time checks) and lib/cfgreport.py (so CONFIG-REPORT.md can show current
findings, not just the live escalation). Split out 2026-07-21 to avoid a circular import
(configmaint.py already imports cfgreport; cfgreport importing configmaint back would cycle).
"""

from __future__ import annotations

import pathlib
import re
import sqlite3

# module -> the dedicated table it already has, if any. Per the researcher's 2026-07-21 rule
# ("there must be a very good reason why a config goes into settings, rather than the specific
# module or utility"): a module on this list already has a purpose-built home, so a NEW
# cfg_setting row for it needs explicit justification. Grows the same way CFG_TABLES does — a
# small, named fact, not derived generically (only one entry exists so far).
MODULE_DEDICATED_TABLE = {
    "candidate": "cfg_candidate_rule",
}

# module -> the cfg_setting key that must hold WHERE that module's quality-check findings persist.
# Per the researcher's 2026-07-21 rule ("errors is not optional to fix... why is there a standard
# if you don't follow it"): every step whose Outcome is advisory findings (not a data write) must
# persist those findings to a report file, matching report.py/validation.py/cfgreport.py's
# established pattern — not just a terminal print + an escalation row that scrolls away.
QUALITY_CHECK_REPORT_PATH = {
    "configmaint.validate": "configmaint.report_path",     # findings folded into CONFIG-REPORT.md
    "candidate.validate": "candidate.quality_report_path",
    "passage.validate": "passage.quality_report_path",
    "lexicon.validate": "lexicon.quality_report_path",
}

# Every step known to write a persistent report via lib/reportkit.render_scaffold — the ground
# truth cfg_report SHOULD contain a row for, one per report-producing step. A hardcoded list, same
# shape as QUALITY_CHECK_REPORT_PATH above and for the same reason: checking cfg_report against
# itself couldn't catch a step that's missing its row entirely (added 2026-07-22,
# PLAN-reports-config-governance-v1-20260722.md §10.1/§11 — "will you miss configs when you build"
# gets a check, not a promise; this is the check that would have caught the retention/candidate.load
# gaps sooner had it existed then).
REPORT_STEPS = (
    "configmaint.report", "candidate.validate", "candidate.load", "passage.validate",
    "report.word", "validation.word", "validation.book", "retention.report",
    "report.seed_candidate", "report.strong_meaning", "report.span_analysis",
    "report.schema_overview", "report.registry", "lexicon.validate",
)


def _step_inactive(conn: sqlite3.Connection, step: str) -> bool:
    """True if `step` has an cfg_step row and every one of them is inactive — REPORT_STEPS/
    QUALITY_CHECK_REPORT_PATH are hardcoded Python names, disconnected from cfg_step.inactive
    (escalation #310), so checks keyed off them need to ask explicitly rather than silently keep
    flagging a step the researcher has already retired."""
    rows = conn.execute("SELECT inactive FROM cfg_step WHERE step=?", (step,)).fetchall()
    return bool(rows) and all(r[0] for r in rows)


def find_missing_cfg_report_rows(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE step in REPORT_STEPS must have an active cfg_report row (title/ToC/footer/
    naming/CSV pairing) — a report-producing step with no cfg_report row means its content-shape
    is still hardcoded Python, the exact gap this plan closed for the original 8, re-checked so it
    can't silently reopen for a 9th. A retired (inactive) step is skipped entirely (escalation
    #310) — its missing/stale report config is no longer a live defect."""
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
    """Every ACTIVE CHAINED work package prints a COMPLETE banner at the end of its sequence
    (PS-side) — if cfg_work_package.complete_message is NULL, that banner's wording has nowhere to
    come from but a hardcoded PS string again. An inactive work package is excluded (escalation
    #310) — a retired package with no complete_message isn't a live defect."""
    missing = []
    for r in conn.execute(
            "SELECT name FROM cfg_work_package WHERE chained=1 AND inactive=0 AND "
            "(complete_message IS NULL OR complete_message='')"):
        missing.append(f"{r[0]} is chained but has no cfg_work_package.complete_message")
    return missing


def find_settings_needing_justification(conn: sqlite3.Connection) -> list[str]:
    """A cfg_setting row whose module ALREADY has its own dedicated table — advisory. Doesn't
    (and can't) judge whether the reason is good — just surfaces every case where the question
    needs asking, so it isn't silently missed. Inactive settings are excluded (escalation #310) —
    a retired setting doesn't need a live justification decision."""
    flags = []
    for module, table in MODULE_DEDICATED_TABLE.items():
        for r in conn.execute(
                "SELECT key FROM cfg_setting WHERE module=? AND inactive=0", (module,)):
            flags.append(f"cfg_setting {r[0]!r} (module {module!r}) — {module} already has its "
                         f"own dedicated table ({table}); confirm this belongs in shared "
                         f"cfg_setting rather than there")
    return flags


def find_orphan_configs(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """cfg_setting keys / cfg_enum groups without REAL usage — configs the app would not actually
    respond to if their value/membership changed. ADVISORY, not a coherence error: an orphan may
    be legitimately pre-staged for a not-yet-built step rather than a mistake.
    EXCLUDES iba/app/migration/: those scripts exist to WRITE a setting's initial value, so they
    always mention its name — counting that as "usage" would mask genuine orphans.

    REDEFINED 2026-07-23 (researcher's correction — escalation #305): "not referenced anywhere"
    was too loose a test — a key merely appearing as a quoted literal (e.g. in a comment or an
    unrelated docstring) passed it without the code actually applying the config's VALUE. "Usage"
    is not one shape; per the researcher, it differs by config kind:
      - a plain cfg_setting: the app must apply its VALUE at runtime. Proven by the key literal
        co-occurring, IN THE SAME FILE, with an actual `.setting(` accessor call — not just the
        key text appearing anywhere in the multi-file corpus, which could be satisfied by an
        unrelated comment/docstring in a file that never reads config at all. (Same-file rather
        than same-call-site: several settings are read via a level of indirection — e.g.
        validation.py's `_WORD_SECTIONS = {"label": "validation.show_health", ...}` then
        `cfg.setting(key, True)` in a loop — genuinely applied, just not through a literal
        `cfg.setting("validation.show_health", ...)` call site. Settings read via a
        cfg_column.expectation data-driven key, e.g. 'pattern:<key>', are handled by the
        exclusion below — also genuinely applied, also not through a literal call site.)
      - a cfg_setting with module='governance': these are process rules for the AI/researcher
        workflow, not runtime application inputs — there is no "apply the value" behaviour to grep
        for. Per the researcher: they "must be read by the startup routine explicitly to ensure
        that AI complies with it." Usage = referenced specifically in iba/app/init.py (the startup
        routine), not anywhere in the app at large — either by the individual key literal, or by a
        generic `WHERE module='governance'` read (init.py deliberately reads the whole module
        dynamically so a NEW governance setting is picked up without an init.py edit; that generic
        read counts as usage for every row it covers, the same reasoning as the
        cfg_column.expectation exclusion below).
      - a cfg_enum group: per the researcher, this is "a lookup, or options... not hard coded but
        use the config" — usage = the group is actually queried by NAME at runtime (`cfg.enum(name)`,
        or the equivalent raw `cfg_enum WHERE name='<name>'`/`name="<name>"` SQL some handlers use
        directly), so a change to the DB's membership is something code would notice. A group's
        VALUES appearing as hardcoded string literals elsewhere (e.g. `state == "paused"`) is NOT
        usage of the enum — the vocabulary isn't actually being read from cfg_enum in that case.

    FIXED 2026-07-22 (kept): a setting/enum read dynamically via `cfg_column.expectation` data
    ('pattern:<key>' for a cfg_setting, 'enum.<name>' for a cfg_enum group) is genuinely enforced
    by lib/valuequality.py's engine, but the value lives in a DB row, not literal .py source —
    excluded before the source-level checks below run."""
    # .ps1 too, not just .py: "PowerShell orchestrates, Python works" means a PS script reading
    # a setting via an inline `python -c "...c.setting('key')..."` (e.g. configmaint.auto_report,
    # read by Config-Maintenance.ps1 this way) is real usage the .py-only scan used to miss.
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
    governance_generic_read = (
        "module='governance'" in init_corpus or 'module="governance"' in init_corpus)

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
        used = any((f'"{key}"' in text or f"'{key}'" in text) and ".setting(" in text
                   for text in per_file.values())
        if not used:
            orphans.append(f"cfg_setting {key!r} (key not found together with a "
                           f"cfg.setting(...) call in any one file)")

    for r in conn.execute("SELECT DISTINCT name FROM cfg_enum WHERE inactive=0"):
        name = r[0]
        if name in enum_names:
            continue
        looked_up = re.search(
            r'(\.enum\(\s*|name\s*=\s*)["\']' + re.escape(name) + r'["\']', corpus)
        if not looked_up:
            orphans.append(f"cfg_enum group {name!r} (not looked up by name at runtime — "
                           f"no cfg.enum({name!r}) or cfg_enum WHERE name={name!r} call site)")
    return orphans


def find_missing_report_paths(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE quality-check step (QUALITY_CHECK_REPORT_PATH) must have its output-path
    setting actually present, non-null, and active in cfg_setting — the code-backed enforcement of
    governance.reports_must_persist. A registered quality-check step with no report path means
    its findings can only ever live in a terminal print + an escalation row, which is exactly the
    standard violation the researcher found and required fixed 2026-07-21. A retired (inactive)
    step is skipped entirely (escalation #310)."""
    missing = []
    for step, key in QUALITY_CHECK_REPORT_PATH.items():
        if _step_inactive(conn, step):
            continue
        row = conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        if not row or not row[0]:
            missing.append(f"{step} has no active {key} setting — its findings would not persist "
                          f"to a report")
    return missing
