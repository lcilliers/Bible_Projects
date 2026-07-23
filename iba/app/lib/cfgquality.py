"""cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the
propose-time / validate-time checks) and lib/cfgreport.py (so CONFIG-REPORT.md can show current
findings, not just the live escalation). Split out 2026-07-21 to avoid a circular import
(configmaint.py already imports cfgreport; cfgreport importing configmaint back would cycle).
"""

from __future__ import annotations

import pathlib
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
    "report.schema_overview",
)


def find_missing_cfg_report_rows(conn: sqlite3.Connection) -> list[str]:
    """Every step in REPORT_STEPS must have a cfg_report row (title/ToC/footer/naming/CSV
    pairing) — a report-producing step with no cfg_report row means its content-shape is still
    hardcoded Python, the exact gap this plan closed for the original 8, re-checked so it can't
    silently reopen for a 9th."""
    missing = []
    for step in REPORT_STEPS:
        if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (step,)).fetchone():
            missing.append(f"{step} produces a persistent report but has no cfg_report row "
                          f"(title/sections/CSV pairing still hardcoded)")
    return missing


def find_chained_packages_missing_complete_message(conn: sqlite3.Connection) -> list[str]:
    """Every CHAINED work package prints a COMPLETE banner at the end of its sequence (PS-side) —
    if cfg_work_package.complete_message is NULL, that banner's wording has nowhere to come from
    but a hardcoded PS string again."""
    missing = []
    for r in conn.execute(
            "SELECT name FROM cfg_work_package WHERE chained=1 AND "
            "(complete_message IS NULL OR complete_message='')"):
        missing.append(f"{r[0]} is chained but has no cfg_work_package.complete_message")
    return missing


def find_settings_needing_justification(conn: sqlite3.Connection) -> list[str]:
    """A cfg_setting row whose module ALREADY has its own dedicated table — advisory. Doesn't
    (and can't) judge whether the reason is good — just surfaces every case where the question
    needs asking, so it isn't silently missed."""
    flags = []
    for module, table in MODULE_DEDICATED_TABLE.items():
        for r in conn.execute("SELECT key FROM cfg_setting WHERE module=?", (module,)):
            flags.append(f"cfg_setting {r[0]!r} (module {module!r}) — {module} already has its "
                         f"own dedicated table ({table}); confirm this belongs in shared "
                         f"cfg_setting rather than there")
    return flags


def find_orphan_configs(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """cfg_setting keys / cfg_enum groups not referenced (as a literal string in .py source, OR
    as DATA in cfg_column.expectation) anywhere — configs with no code AND no data-driven check
    reading them. ADVISORY, not a coherence error: an orphan may be legitimately pre-staged for a
    not-yet-built step rather than a mistake.
    EXCLUDES iba/app/migration/: those scripts exist to WRITE a setting's initial value, so they
    always mention its name — counting that as "usage" would mask genuine orphans.

    FIXED 2026-07-22: a setting/enum read dynamically via `cfg_column.expectation` data
    ('pattern:<key>' for a cfg_setting, 'enum.<name>' for a cfg_enum group) is genuinely enforced
    by lib/valuequality.py's engine, but the value lives in a DB row, not literal .py source — the
    original grep-only scan couldn't see it and wrongly flagged 10 actively-used configs as
    orphans (candidate.tag_clean_pattern, raw.meaning_tree_clean_pattern, and 6 of 7 flagged
    enums — confirmed each has a real cfg_column.expectation reference; deleting any of them would
    have broken find_enum_violations, which hard-fails when a declared enum has zero members)."""
    # .ps1 too, not just .py: "PowerShell orchestrates, Python works" means a PS script reading
    # a setting via an inline `python -c "...c.setting('key')..."` (e.g. configmaint.auto_report,
    # read by Config-Maintenance.ps1 this way) is real usage the .py-only scan used to miss.
    corpus = ""
    for pattern in ("*.py", "*.ps1"):
        for f in app_root.rglob(pattern):
            if "migration" in f.relative_to(app_root).parts:
                continue
            try:
                corpus += f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
    expectations = {r[0] for r in conn.execute(
        "SELECT expectation FROM cfg_column WHERE expectation IS NOT NULL")}
    pattern_keys = {e[len("pattern:"):] for e in expectations if e.startswith("pattern:")}
    enum_names = {e[len("enum."):] for e in expectations if e.startswith("enum.")}
    orphans: list[str] = []
    for r in conn.execute("SELECT key FROM cfg_setting"):
        key = r[0]
        if key in pattern_keys:
            continue
        if f'"{key}"' not in corpus and f"'{key}'" not in corpus:
            orphans.append(f"cfg_setting {key!r}")
    for r in conn.execute("SELECT DISTINCT name FROM cfg_enum"):
        name = r[0]
        if name in enum_names:
            continue
        if f'"{name}"' not in corpus and f"'{name}'" not in corpus:
            orphans.append(f"cfg_enum group {name!r}")
    return orphans


def find_missing_report_paths(conn: sqlite3.Connection) -> list[str]:
    """Every quality-check step (QUALITY_CHECK_REPORT_PATH) must have its output-path setting
    actually present and non-null in cfg_setting — the code-backed enforcement of
    governance.reports_must_persist. A registered quality-check step with no report path means
    its findings can only ever live in a terminal print + an escalation row, which is exactly the
    standard violation the researcher found and required fixed 2026-07-21."""
    missing = []
    for step, key in QUALITY_CHECK_REPORT_PATH.items():
        row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()
        if not row or not row[0]:
            missing.append(f"{step} has no {key} setting — its findings would not persist to a report")
    return missing
