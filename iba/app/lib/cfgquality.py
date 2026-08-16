"""cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the
propose-time / validate-time checks) and lib/cfgreport.py (so CONFIG-REPORT.md can show current
findings, not just the live escalation). Split out 2026-07-21 to avoid a circular import
(configmaint.py already imports cfgreport; cfgreport importing configmaint back would cycle).
"""

from __future__ import annotations

import io
import pathlib
import re
import sqlite3
import tokenize

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


# Extended 2026-07-30 per the researcher's correction ("your validations is only touching settings
# and enum and not incorporating all the other config tables") — `find_orphan_configs` above was
# the ONLY usage check in the whole app, and it only ever covered `cfg_setting`/`cfg_enum`. Every
# other table got at most a structural/referential check (does an FK point somewhere real), never
# "is this actually consumed." These three close that gap for `cfg_book_order`/`cfg_connection`/
# `cfg_candidate_rule` — the same "not referenced anywhere" concern, extended past the two tables
# it happened to start with.

def find_orphan_book_order(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """`cfg.book_order()` — the WHOLE table is read as one dict, not looked up by individual key,
    so (unlike cfg_setting/cfg_enum) there is no per-row "is this ONE book used" question — the
    question is whether the accessor itself is called anywhere (same corpus-scan convention as
    `find_orphan_configs`, `migration/` excluded for the same reason: those scripts exist to
    populate/consume the seed once, not to represent ongoing app usage). ALSO flags duplicate
    book/ordinal rows — free to check while already reading the table, the same class of internal-
    coherence gap `_validate_live`'s schema checks already catch for other tables."""
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
    — identical methodology to `find_orphan_configs`'s cfg_setting check, just scoped to this
    table (which that check never covered)."""
    # NOT `_code_only_text` here — that blanks OUT string-literal tokens, and the thing this check
    # needs to find (`"base_url"`) is itself a string literal. `_code_only_text` only helps when
    # searching for bare CODE SYNTAX that never legitimately appears inside a string/comment (a
    # method-call pattern with no argument, like `find_orphan_book_order`'s `.book_order(` check);
    # here it would silently blank out every real call site too — caught 2026-07-30 by re-testing
    # immediately after switching to it and seeing genuinely-used keys (`base_url` et al., real
    # calls in `stepapi.py`) suddenly flagged as unused.
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


# The only two steps whose code calls `.candidate_rules(...)` (`candidate.seed`/`candidate.curate`
# — verified by direct grep, 2026-07-30, not guessed). Both are currently INACTIVE (2026-07-23
# candidate-system retraction) — when both are inactive, "code calls kind X but 0 active rows back
# it" is not a live gap, it's the same already-recorded retraction every other inactive-scoped
# check already excludes (escalation #310); skip the whole first direction of the check rather than
# re-surface a fact GOVERNANCE.md §15D already covers. The reverse direction (rows nobody calls) is
# NOT step-gated — a config value with no code path to it at all is a gap regardless of whether the
# would-be caller happens to be active right now.
_CANDIDATE_RULES_CALLER_STEPS = ("candidate.seed", "candidate.curate")
_CANDIDATE_RULES_CALL_RE = re.compile(r"\.candidate_rules\(\s*[\"']([^\"']+)[\"']")


def find_orphan_candidate_rules(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """Two-directional usage check for `cfg_candidate_rule` — "orphan" means something different
    here than a single cfg_setting key, since a row is a candidate WORD, not a configurable key:
    (a) code calls the candidate_rules accessor for a kind with ZERO active rows — the call will
    silently return an empty list, which may be exactly what's happening right now and going
    unnoticed (skipped while `_CANDIDATE_RULES_CALLER_STEPS` are both inactive — see that
    constant's comment); (b) a kind WITH active rows that no code anywhere asks for — config
    nobody reads, the same direction `find_orphan_configs` already checks for cfg_setting/
    cfg_enum.

    Deliberately raw `read_text`, NOT `_code_only_text` — `_CANDIDATE_RULES_CALL_RE` needs to see
    the actual quoted argument (the kind name IS a string literal), and `_code_only_text` blanks
    string-literal tokens out; using it here would silently blank every real call site too (caught
    2026-07-30 the same way as the `cfg_connection` check above — re-tested immediately after
    switching and found real usage in `candidate.py` suddenly detected as zero). Also deliberately
    NOT spelling out the literal call-with-a-quoted-kind syntax in prose anywhere in this docstring
    (unlike the previous draft of this exact paragraph, which did, and matched its own regex
    against this file's own text) — same class of self-collision `cfgreport.py`'s own "NOTE" already
    documents for `find_utility_config_density`."""
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
    """Every `cfg_report_csv_table.table_name` must name a real table — a DATA table (`cfg_table`)
    or a `cfg_*` infrastructure table — or the wildcard `cfg_*` prefix `reportkit.write_csv_pairing`
    itself recognises (a literal trailing `*`) — **or be marked `virtual`** (a row_filter-supplied
    CSV pairing: the handler computes the rows itself and passes them to `write_csv_pairing` under
    this `table_name` as a key, so no `SELECT * FROM {table_name}` ever runs against it — see
    `write_csv_pairing`'s `row_filter` parameter). The same referential-integrity discipline
    `find_report_step_references`/`_validate_live`'s write-grant check already apply to `.step`/
    write-grant table references — never applied to THIS table's own column before (2026-07-30,
    researcher: "your validations is only touching settings and enum"). A hard structural fault:
    a CSV pairing for a table that doesn't exist AND isn't `virtual` would crash `write_csv_pairing`
    the moment that report actually runs, not just sit as a cosmetic gap.

    **`virtual` added 2026-08-15** — this check itself was a false positive against two entries
    that were never broken (`report.registry`/`word_registry_strong_pairing`,
    `report.cluster`/`strong_without_cluster`, both legitimate `row_filter` keys), re-raised across
    three separate `configmaint.validate` escalations (#591, #597, #642) over five days because the
    check had no way to represent "this is intentionally not a literal table." A `virtual` row
    without a `join_note` is still flagged — the exemption cannot silently hide an actually-wrong
    entry with no explanation attached."""
    data_tables = {r[0] for r in conn.execute("SELECT name FROM cfg_table")}
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


# Writer identities in cfg_write_grant that are NOT a cfg_step.step — dispatcher/API internals,
# not steps. Fallback only — the real value is `cfg_enum` group `writer_identity` (added
# 2026-07-29); kept byte-identical to that group's proposed values so this check works correctly
# even before the enum rows are approved. Found 2026-07-29: cfg_write_grant.writer was never
# checked against anything at all — a typo'd writer name would have gone unnoticed structurally
# forever, the same class of gap `find_orphan_configs` already closes for cfg_setting/cfg_enum.
_WRITER_IDENTITY_FALLBACK = ("run", "escalation", "migration",
                             "call1_meanings", "call2_getInfo", "call3_strong")


def find_report_step_references(conn: sqlite3.Connection) -> list[str]:
    """Every active `cfg_report`/`cfg_report_section`/`cfg_report_csv_table.step` must name a
    currently-ACTIVE `cfg_step.step` — the same discipline `_validate_live`'s existing `on_fail`
    check already applies to `cfg_on_fail.step`, extended to the three report-shape tables that
    were never checked against anything at all. A hard structural fault: a report row for a step
    that doesn't exist (or was retired) is broken plumbing, not a judgement call."""
    active_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0")}
    out: list[str] = []
    for table in ("cfg_report", "cfg_report_section", "cfg_report_csv_table"):
        for r in conn.execute(f'SELECT DISTINCT step FROM "{table}" WHERE inactive=0'):
            if r[0] not in active_steps:
                out.append(f"schema: {table}.step {r[0]!r} is not a currently-active cfg_step")
    return out


def find_unknown_write_grant_writers(conn: sqlite3.Connection,
                                     writer_identities: set[str] | None = None) -> list[str]:
    """Every active `cfg_write_grant.writer` must resolve to a currently-ACTIVE `cfg_step.step`,
    OR be a declared non-step writer identity (dispatcher/API internals — see
    `_WRITER_IDENTITY_FALLBACK`/`enum.writer_identity`). Anything else is an unchecked typo/orphan
    reference — found live 2026-07-29 to be clean today, but never actually checked before."""
    active_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0")}
    identities = writer_identities or set(_WRITER_IDENTITY_FALLBACK)
    out: list[str] = []
    for r in conn.execute("SELECT DISTINCT writer FROM cfg_write_grant WHERE inactive=0"):
        if r[0] not in active_steps and r[0] not in identities:
            out.append(f"schema: cfg_write_grant.writer {r[0]!r} is not an active cfg_step and "
                      f"not a declared writer identity")
    return out


def find_filled_by_referencing_inactive_step(conn: sqlite3.Connection) -> list[str]:
    """`cfg_column.filled_by` naming a step that is now `inactive=1` — ADVISORY, not a hard error,
    because the correct fix needs a human judgement call per column (is the column now genuinely
    dormant, as `passage.rule`/`.source` are, or has a DIFFERENT currently-active mechanism quietly
    taken over — `passage.created_at`/`verse_passage.created_at` are in fact written by
    `lib/passagetrack.py` today, not `passage.build`, and simply clearing `filled_by` there would
    be its own new inaccuracy). Found 2026-07-29: 21 columns across the candidate/passage
    retirements had this defect, silent, because nothing checked it — see
    `passage-config-full-extract-20260729.md`."""
    inactive_steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=1")}
    if not inactive_steps:
        return []
    out: list[str] = []
    for r in conn.execute(
            "SELECT table_name, name, filled_by FROM cfg_column WHERE filled_by IS NOT NULL"):
        if r["filled_by"] in inactive_steps:
            out.append(f"{r['table_name']}.{r['name']} filled_by={r['filled_by']!r} "
                      f"(an inactive step) — confirm dormant or update to the real current writer")
    return out


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


def find_stale_governance_docs(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """`GOVERNANCE.md`'s own §8 rule (LIVE `cfg_setting` rows `governance.governance_md_on_rule_change`/
    `build_md_on_code_change`, escalations #238/#239): any `cfg_*` rule change updates GOVERNANCE.md,
    same unit of work — a rule §8 itself named as "follow-up work, not done in this pass" on
    2026-07-22, still unbuilt when a 2026-07-29 audit found 7 real rule changes (2026-07-26 to
    2026-07-28) with no matching GOVERNANCE.md entry. ADVISORY only (a doc update is a human act
    this can prompt, not perform): flags if the newest applied `cfg_change_detail` row is more
    recent than GOVERNANCE.md's own last-modified time. A coarse signal (a doc edit unrelated to
    config also resets the clock) — good enough to prompt a look, not precise enough to hard-fail
    on."""
    row = conn.execute("SELECT MAX(applied_at) FROM cfg_change_detail").fetchone()
    latest_change = row[0] if row else None
    if not latest_change:
        return []
    gov = app_root / "GOVERNANCE.md"
    if not gov.exists():
        return [f"{gov} does not exist — cannot check currency against the newest applied "
                f"config change ({latest_change})"]
    import datetime
    gov_mtime = datetime.datetime.fromtimestamp(
        gov.stat().st_mtime, tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if gov_mtime < latest_change:
        return [f"GOVERNANCE.md was last modified {gov_mtime}, before the newest applied "
                f"cfg_change_detail row ({latest_change}) — check whether that change needs an "
                f"entry (GOVERNANCE.md §8's own rule)"]
    return []


def find_report_version_clutter(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    """`lib/reportkit.oneoff_path()` was found 2026-08-08 (BUILD.md §83) to version correctly
    (`-v2`/`-v3`/...) but never archive the superseded version — every reconciliation report and
    several extract tools accumulated their whole lineage flat in `governance.oneoff_report_dir`
    forever, unlike `write_report`'s own reports (fixed 2026-08-05, §60) which correctly hold
    exactly one live file per stem. Fixed at the source (`oneoff_path` now archives before writing)
    — this is the ACTIVE detector that a future regression (a new caller bypassing `oneoff_path`,
    or the archiving logic breaking) doesn't silently recur unnoticed, matching this app's own
    "not stated, enforced" convention rather than trusting the fix to hold by inspection alone."""
    from . import reportkit
    out_dir_setting = _cfg_setting(conn, "governance.oneoff_report_dir")
    if not out_dir_setting:
        return []
    # governance.oneoff_report_dir's value ("iba/app/reports/") is already relative to the REPO
    # ROOT (same resolution oneoff_path() itself relies on, via cwd) -- NOT relative to app_root
    # (iba/app, one level in) the way other checks in this file use it. app_root.parent.parent
    # recovers the repo root correctly either way, without assuming cwd.
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
    """Every `iba/app/lib/*.py` module must have a `cfg_utility` row (added 2026-07-29, Phase 4 of
    `PLAN-config-system-remediation-v1-20260729.md`) — a NEW module added later and never
    registered would otherwise be invisible to `find_utility_config_density` below, the same
    "found by chance, not by a check" gap this whole registry exists to close. ADVISORY: a brand
    new file mid-edit is a normal transient state, not a coherence error."""
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


# Every real method the `Cfg` class exposes — computed live from the class itself (not a hand-
# maintained list) so this stays accurate as `Cfg` grows. Used to detect genuine config-consumption
# call sites (`<anything>.setting(`, `<anything>.tables(`, ...), not just the two most common ones.
# Escalation review 2026-07-30 (`cfg-utility-density-check-review-20260730.md`) found this check's
# OWN pattern was the bug for two modules: `db.py` genuinely consumes config via `.tables()`/
# `.columns()`/`.unique_key()` — real usage the old `.setting(`/`.enum(` -only pattern never
# counted; `dbsnapshot.py` genuinely calls `.setting(` but on a `Cfg` instance bound to `c`, not
# `cfg` — the old pattern hardcoded the literal text `cfg.setting(`/`cfg.enum(`, missing any other
# variable name entirely.
_STRING_TOKEN_TYPES = {tokenize.COMMENT, tokenize.STRING}
for _name in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):    # Python 3.12+ (PEP 701) only
    if hasattr(tokenize, _name):
        _STRING_TOKEN_TYPES.add(getattr(tokenize, _name))


def _code_only_text(path: pathlib.Path) -> str:
    """Source with every COMMENT/STRING(/f-string literal piece) span blanked to spaces IN PLACE —
    so a call-site scan can't be fooled by a docstring or comment that merely MENTIONS the pattern
    in prose, while every real call site keeps its EXACT original adjacency (`cfg.setting(` stays
    literally `cfg.setting(`, not spread apart). Found 2026-07-30, twice in one session:
    `cfgreport.py` (fixed by rewording one line) and then `cfgquality.py` itself — THIS file's own
    docstrings talk about `.setting(`/`.enum(`/`.tables(` (they document the exact check below),
    which falsely satisfied the old raw-text substring scan. First attempt at this fix (joining
    non-string tokens with a space) was itself wrong — it broke every REAL match too, by inserting
    spaces between `cfg`/`.`/`setting`/`(`, caught immediately by re-testing `db.py`/`dbsnapshot.py`
    (known-good cases) and finding them suddenly failing. Blanking spans in the original string,
    same length, fixes both directions at once. Falls back to raw text if a file doesn't tokenize
    cleanly (better a possible false negative than a hard crash on some edge-case file)."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenizeError, IndentationError, SyntaxError, ValueError):
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


_CFG_METHOD_RE = None  # lazy: built on first use, not at import time (avoids a circular import —
                       # cfg.py doesn't import cfgquality, but this keeps the dependency one-way)


def find_utility_config_density(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE, NON-EXEMPT `cfg_utility` module with ZERO real `Cfg`-method call sites in its
    own file (any method `Cfg` exposes — `.setting(`/`.enum(` and every schema/write-grant/sequence
    method alike, under any variable name — see `_cfg_method_pattern`) — ADVISORY, the same "could
    be legitimate" caveat `find_orphan_configs` already carries: a module like `retention.py`/
    `seedreport.py` genuinely has no config of its own because its caller resolves paths for it (a
    legitimate zero — now declared via `cfg_utility.config_exempt`, not re-derived every run); a
    module like `lexiconparse.py` — six regexes and a hardcoded tag-set deciding a real parse, zero
    `Cfg` reference anywhere — is the actual gap this check exists to surface (found by hand
    2026-07-29, `core-module-config-intent-vs-effect-20260729.md`). `cfg_utility.file_path` is
    already repo-root-relative (e.g. `iba/app/lib/cfg.py`) — resolved against the CWD, which every
    PS entry point already sets to the repo root (`Set-Location $RepoRoot`), not recombined with
    any other path."""
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
        if not _CFG_METHOD_RE.search(_code_only_text(path)):
            out.append(f"cfg_utility {r['module']!r} ({path}) has zero Cfg-method call sites "
                      f"(.setting()/.enum()/.tables()/... under any variable name) — confirm this "
                      f"is a legitimate zero (mark `cfg_utility.config_exempt=1` via "
                      f"`configmaint.propose`) or a real completeness gap")
    return out


def find_unclassified_active_steps(conn: sqlite3.Connection) -> list[str]:
    """Every ACTIVE `cfg_step` must have `kind` set (`operations` | `utility` — the researcher's
    own classification, 2026-07-30, `migration/bootstrap_step_kind.py`). A HARD error, not a
    judgement call: `run.py`'s dispatch gate (escalation, same day) refuses to dispatch a step with
    no classification at all — this is the structural check that keeps that gate's premise true
    (a NEW step, added later without a `kind`, would otherwise silently sit undispatchable with no
    coherence check pointing at why). `find_enum_violations` (value-quality) already catches an
    INVALID `kind` value; this catches a MISSING one, which that check explicitly does not (it
    skips `NULL` by design)."""
    return [f"cfg_step ({r['work_package']}, {r['step']}) is active but has no kind "
           f"(operations|utility) — classify it via configmaint.propose before it can be "
           f"dispatched (run.py now refuses undispatched steps with no kind)"
           for r in conn.execute(
               "SELECT work_package, step FROM cfg_step WHERE inactive=0 AND kind IS NULL")]
