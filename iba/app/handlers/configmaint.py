"""configuration_maintenance handlers — the ONE sanctioned path for changing a cfg_* row.

Three steps, all config-governed like every other module:

  validate — read-only coherence check of the LIVE cfg_* tables as they stand. Ports
             lib/cfgcheck.py's checks (originally written against JSON seed dicts) to
             query the DB instead — the seed is no longer the thing being checked, the
             live tables are (per the researcher's 2026-07-21 ruling: the DB is master).
  propose  — DB-direct, single-row, APPROVAL-GATED. Never writes silently. Mirrors
             handlers/registry.py's create(): check for an existing answer on this run's
             escalation; act on it if present; otherwise coherence-check the proposed
             change and escalate for a decision, then pause. The answer is three-way
             (approve / reject / revise — see lib/escalation.py's run-scoped functions),
             not yes/no, per the researcher's standing rule that an approval screen must
             show REPRESENTATIVE data and never force a binary choice.
  report   — regenerate CONFIG-REPORT.md from the live cfg_* tables (lib/cfgreport.py).
             Read-only; safe to run any time; chains automatically after an approved
             propose when configmaint.auto_report is true.

Every write `propose` actually applies is logged to `cfg_change_detail` — the ROW-LEVEL
change log `cfg_change_log` was never able to hold (it only ever recorded whole-reload
events). See iba/docs/iba-configuration-maintenance-layered-design-v1-20260721.md.
"""

from __future__ import annotations

import datetime
import importlib
import json
import pathlib
import re
import sqlite3

from ..lib import cfgreport, cfgquality, valuequality, escalation as esc
from .base import Ctx, Outcome, ok, fail, escalate

APP_ROOT = pathlib.Path(__file__).resolve().parent.parent   # iba/app — scanned for orphan configs

# every cfg_* table configuration_maintenance may touch (kept in step with the bootstrap
# migration's CFG_TABLES — both name the same set on purpose, rule j: one rule, one home,
# would eventually pull this from a single source; noted, not solved, in this first pass)
CFG_TABLES = (
    "cfg_meta", "cfg_table", "cfg_column", "cfg_unique", "cfg_enum", "cfg_connection",
    "cfg_api", "cfg_write_grant", "cfg_work_package", "cfg_step", "cfg_setting",
    "cfg_on_fail", "cfg_status_flow", "cfg_book_order", "cfg_candidate_rule",
    "cfg_change_log", "cfg_change_detail", "cfg_report", "cfg_report_section",
    "cfg_report_csv_table", "cfg_utility",
)

# module -> the dedicated table it already has, if any (rule c's "very good reason" check).
# Moved to lib/cfgquality.py 2026-07-21 so lib/cfgreport.py can share it without a circular import.
MODULE_DEDICATED_TABLE = cfgquality.MODULE_DEDICATED_TABLE


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── validate: coherence-check the LIVE cfg_* tables (ports lib/cfgcheck.py to the DB) ──
def _validate_live(conn: sqlite3.Connection) -> list[str]:
    e: list[str] = []
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()

    tables = {r["name"] for r in q("SELECT name FROM cfg_table")}
    real_cfg_tables = {r[0] for r in q(
        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg\\_%' ESCAPE '\\'")}
    columns: dict[str, set[str]] = {}
    for r in q("SELECT table_name, name FROM cfg_column"):
        columns.setdefault(r["table_name"], set()).add(r["name"])

    # schema integrity
    for t in tables:
        pk_n = q("SELECT COUNT(*) n FROM cfg_column WHERE table_name=? AND is_pk=1", (t,))[0]["n"]
        if pk_n > 1:
            e.append(f"schema: {t} has {pk_n} primary keys")
    for r in q("SELECT table_name, name, fk FROM cfg_column WHERE fk IS NOT NULL"):
        rt, _, rc = r["fk"].partition(".")
        if rt not in tables:
            e.append(f"schema: {r['table_name']}.{r['name']} FK -> unknown table {rt!r}")
        elif rc not in columns.get(rt, set()):
            e.append(f"schema: {r['table_name']}.{r['name']} FK -> unknown column {rt}.{rc}")
    for r in q("SELECT table_name, col FROM cfg_unique"):
        if r["col"] not in columns.get(r["table_name"], set()):
            e.append(f"schema: {r['table_name']} unique names unknown column {r['col']!r}")

    # STEP apis (inactive=0: escalation #310, deactivated config is excluded from validation)
    for r in q("SELECT name, route FROM cfg_api WHERE inactive=0"):
        if "{version}" not in (r["route"] or ""):
            e.append(f"step: api {r['name']} route has no {{version}} placeholder")

    # write grants: every granted table must be a real table (data OR cfg_*)
    for r in q("SELECT DISTINCT writer, table_name FROM cfg_write_grant WHERE inactive=0"):
        if r["table_name"] not in tables and r["table_name"] not in real_cfg_tables:
            e.append(f"rules: write_grant {r['writer']!r} -> unknown table {r['table_name']!r}")

    # step names must be globally unique ACROSS work packages, not just within one (the PK is
    # (work_package, step), which would silently allow a duplicate) — escalation.pending_for_word/
    # answered_for_word and cfg_on_fail both match on `step` alone with no work_package in the
    # WHERE clause, so two work packages sharing a step name would collide at runtime. Found
    # 2026-07-21 during review; not in the original lib/cfgcheck.py checks either.
    for r in q("SELECT step, COUNT(DISTINCT work_package) n FROM cfg_step WHERE inactive=0 "
              "GROUP BY step HAVING n > 1"):
        e.append(f"schema: step {r['step']!r} is registered under {r['n']} different work packages "
                 f"— step names must be globally unique (escalation/on_fail match by step alone)")

    # run: every step's handler must resolve
    known_steps = {r["step"] for r in q("SELECT step FROM cfg_step WHERE inactive=0")}
    for r in q("SELECT work_package, step, handler FROM cfg_step WHERE inactive=0"):
        h = r["handler"] or ""
        if ":" not in h:
            e.append(f"run: {r['work_package']}/{r['step']} handler {h!r} is not module:function")
            continue
        mod, fn = h.split(":")
        try:
            if not hasattr(importlib.import_module(mod), fn):
                e.append(f"run: {r['work_package']}/{r['step']} handler {h!r} — function not found")
        except Exception as exc:
            e.append(f"run: {r['work_package']}/{r['step']} handler {h!r} — import failed: {exc}")

    # on_fail: path in enum, step known
    valid_paths = {r["value"] for r in q("SELECT value FROM cfg_enum WHERE name='on_fail'")}
    for r in q("SELECT step, path FROM cfg_on_fail WHERE inactive=0"):
        if r["path"] not in valid_paths:
            e.append(f"rules: on_fail path {r['path']!r} not in enum.on_fail {sorted(valid_paths)}")
        if r["step"] not in known_steps:
            e.append(f"rules: on_fail step {r['step']!r} is not a step in any work package")

    # status_flow: word targets in enum.word_status
    valid_status = {r["value"] for r in q("SELECT value FROM cfg_enum WHERE name='word_status'")}
    for r in q("SELECT status FROM cfg_status_flow WHERE entity='word' AND inactive=0"):
        if r["status"] not in valid_status:
            e.append(f"rules: status {r['status']!r} not in enum.word_status {sorted(valid_status)}")

    # settings: a *pattern setting must compile; report.*_fields must name real columns
    span_cols = columns.get("span", set()) | {"sense"}
    strong_cols = columns.get("strong", set()) | columns.get("strong_sense", set()) | {"verses"}
    for r in q("SELECT key, value FROM cfg_setting WHERE inactive=0"):
        if "pattern" in r["key"]:
            try:
                re.compile(json.loads(r["value"]))
            except (re.error, json.JSONDecodeError, TypeError) as exc:
                e.append(f"rules: setting {r['key']} is not a valid regex: {exc}")
        if r["key"] in ("report.span_fields", "report.strong_fields"):
            cols = span_cols if r["key"] == "report.span_fields" else strong_cols
            for f in json.loads(r["value"]):
                if f not in cols:
                    e.append(f"report: {r['key']} names {f!r} which is not a real column")

    # every cfg_setting must have a module, and it must be a real one (cfg_enum config_module) —
    # catches typos/drift the moment they're written, added 2026-07-21 per the researcher's rule
    # against cfg_setting drifting into an untracked catch-all.
    valid_modules = {r["value"] for r in q("SELECT value FROM cfg_enum WHERE name='config_module'")}
    for r in q("SELECT key, module FROM cfg_setting WHERE inactive=0"):
        if not r["module"]:
            e.append(f"consistency: cfg_setting {r['key']!r} has no module — every setting must "
                     f"be attributed to a module/utility")
        elif r["module"] not in valid_modules:
            e.append(f"consistency: cfg_setting {r['key']!r} names unknown module {r['module']!r} "
                     f"(not in enum.config_module {sorted(valid_modules)})")

    # governance.reports_must_persist, enforced: every quality-check step must have somewhere its
    # findings actually persist to (a report file), not just a terminal print + an escalation row
    # that scrolls away. Added 2026-07-21 per the researcher's ruling that a deviation from an
    # already-established standard (report.py/validation.py/cfgreport.py all persist) is a bug,
    # not a judgement call, and must be enforced by the app itself, not only remembered.
    standard = q("SELECT value FROM cfg_setting WHERE key='governance.reports_must_persist'")
    if standard:
        for msg in cfgquality.find_missing_report_paths(conn):
            e.append(f"governance ({json.loads(standard[0]['value'])}): {msg}")

    # report content-governance, enforced the same way: every known report-producing step needs
    # its cfg_report row, every chained work package needs its complete_message — added 2026-07-22
    # per PLAN-reports-config-governance-v1-20260722.md §10.1 ("will you miss configs" gets a
    # check, not a promise).
    for msg in cfgquality.find_missing_cfg_report_rows(conn):
        e.append(f"report-governance: {msg}")
    for msg in cfgquality.find_chained_packages_missing_complete_message(conn):
        e.append(f"report-governance: {msg}")

    # value-quality: every cfg_column declaring expectation enum.<name> must actually hold only
    # values from that enum, live. Found 2026-07-21: candidate_seed.decision/.layer already
    # declared enum.candidate_decision/enum.candidate_source but nothing checked it — the enums
    # were referenced nowhere in the app's code. A hard coherence fault, not a judgement call.
    e.extend(valuequality.find_enum_violations(conn))

    # report-step / write-grant-writer coherence — added 2026-07-29 (the passage config audit):
    # cfg_report/cfg_report_section/cfg_report_csv_table.step and cfg_write_grant.writer were never
    # checked against cfg_step at all before this, the same class of gap the existing on_fail.step
    # check already closed for a different table. Both hard errors — a report row or write grant
    # for a step that doesn't exist (or was retired) is broken plumbing, not a judgement call.
    e.extend(cfgquality.find_report_step_references(conn))
    writer_identities = set(_writer_identities(conn))
    e.extend(cfgquality.find_unknown_write_grant_writers(conn, writer_identities))

    # step classification completeness — added 2026-07-30 (the operations/utility model). Hard
    # error: an active, dispatchable step with no classification is exactly the state run.py's
    # dispatch gate now refuses to run, so this check keeps surfacing why, not just crashing at
    # dispatch time with no coherence-report trail.
    e.extend(cfgquality.find_unclassified_active_steps(conn))

    # cfg_report_csv_table.table_name referential integrity — added 2026-07-30 (researcher: "your
    # validations is only touching settings and enum"). Same class as the on_fail.step/report-
    # step-reference checks already here; this specific table's own column was never checked.
    e.extend(cfgquality.find_bad_report_csv_table_references(conn))

    return e


def _writer_identities(conn: sqlite3.Connection) -> tuple[str, ...]:
    return tuple(r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='writer_identity' AND inactive=0")) \
        or cfgquality._WRITER_IDENTITY_FALLBACK


# moved to lib/cfgquality.py 2026-07-21 so lib/cfgreport.py can share these without a circular
# import (configmaint.py already imports cfgreport). Thin aliases kept so the rest of this file's
# call sites don't need to change.
_find_settings_needing_justification = cfgquality.find_settings_needing_justification


def _find_orphan_configs(conn: sqlite3.Connection) -> list[str]:
    return cfgquality.find_orphan_configs(conn, APP_ROOT)


def validate(ctx: Ctx) -> Outcome:
    """Hard coherence errors (schema/FK/enum breaks — genuine structural faults) still fail
    outright, report-stop, no question to ask. But a FINDING that needs a researcher JUDGMENT
    CALL (an orphan config, a setting that maybe belongs in its own table) is not information to
    leave sitting in a JSON blob — per the researcher's 2026-07-21 correction, that's what
    escalation is for, the same as every other "the app can't decide this itself" moment in the
    dispatcher. One escalation per run, listing everything found (small counts here — orphans
    and justification flags are single digits to low tens, not the tens-of-thousands scale
    candidate.validate has to handle differently, see handlers/candidate.py)."""
    errors = _validate_live(ctx.db.conn)
    if errors:
        error_summary = "; ".join(errors)
        # 2026-08-07: the 2026-08-06 dedup fix (open_duplicate, see below) was only ever wired
        # into the ADVISORY path (needs-review, further down this function) -- this hard-error
        # path had its own separate `fail()` call, going through run.py's generic (run_id, step_id)
        # idempotency guard instead, which never catches a cross-run duplicate because every
        # invocation mints a fresh run_id. Found live 2026-08-07 (researcher: "too many of these
        # escalations... it is notifications to you for stuff you did not do properly, or
        # completed and not cleared") -- successive validate re-runs each stacked their own
        # report-stop escalation for what was often the SAME still-open coherence error (#534,
        # #537, #539's crash all piled up this way). Same fix, same rationale, applied here too --
        # matched on the error text (stable across re-runs of the same broken state), not a
        # versioned path.
        # Mirrors the advisory branch below exactly: return ok(), not fail() -- a `fail()` here
        # would still hit run.py's own report-stop write, which has no knowledge of `dup` and
        # would write a fresh row regardless of the message text. Only ok() skips the write
        # (condition == "ok" takes no on_fail path at all). Trade-off accepted deliberately, same
        # as the advisory case: this run's own `outcome`/`state` reads as ok even though the
        # underlying cfg_* is still broken -- the point is "no NEW escalation", not "this run
        # succeeded"; the still-open #dup['id'] remains the one place that record lives.
        dup = esc.open_duplicate(ctx.db, ctx.step_id, error_summary)
        if dup:
            return ok(f"identical to already-open escalation #{dup['id']} (raised "
                      f"{dup['raised_at']}) — not re-raised; answer #{dup['id']} to resolve. "
                      f"{len(errors)} coherence error(s): {error_summary}",
                      errors=error_summary, existing_escalation_id=dup["id"])
        return fail("invalid", f"{len(errors)} coherence error(s)", errors=error_summary)

    # Every advisory (judgement-call, not structural-fault) finding — a dict, not one variable per
    # check, so a 7th/8th finding never needs touching four separate places again the way orphans/
    # needs_justification/stale_filled_by/stale_docs did one at a time on 2026-07-21/29. Each value
    # is (list-of-findings, one-line label used in messages).
    findings: dict[str, tuple[list[str], str]] = {
        "orphans": (_find_orphan_configs(ctx.db.conn), "orphan config(s)"),
        "needs_justification": (_find_settings_needing_justification(ctx.db.conn),
                                "setting(s) needing justification"),
        "stale_filled_by": (cfgquality.find_filled_by_referencing_inactive_step(ctx.db.conn),
                           "column(s) with a stale filled_by"),
        "stale_docs": (cfgquality.find_stale_governance_docs(ctx.db.conn, APP_ROOT),
                      "stale-doc finding(s)"),
        "unregistered_lib_modules": (cfgquality.find_unregistered_lib_modules(ctx.db.conn, APP_ROOT),
                                    "lib module(s) missing a cfg_utility row"),
        "low_config_density_utilities": (cfgquality.find_utility_config_density(ctx.db.conn),
                                        "utility module(s) with zero cfg.setting()/cfg.enum() usage"),
        # 2026-07-30 — extending find_orphan_configs' "actually used, not just structurally valid"
        # check past cfg_setting/cfg_enum to the three other tables that had zero usage checking.
        "orphan_book_order": (cfgquality.find_orphan_book_order(ctx.db.conn, APP_ROOT),
                             "cfg_book_order finding(s)"),
        "orphan_connection": (cfgquality.find_orphan_connection_keys(ctx.db.conn, APP_ROOT),
                             "cfg_connection finding(s)"),
        "orphan_candidate_rule": (cfgquality.find_orphan_candidate_rules(ctx.db.conn, APP_ROOT),
                                "cfg_candidate_rule finding(s)"),
        # 2026-08-08 (BUILD.md §83) -- oneoff_path() versioned but never archived; fixed at the
        # source, this is the active detector that a future regression doesn't silently recur.
        "report_version_clutter": (cfgquality.find_report_version_clutter(ctx.db.conn, APP_ROOT),
                                  "report lineage(s) with more than one live version"),
    }
    preset = {k: v[0] for k, v in findings.items()}
    if not any(preset.values()):
        return ok("cfg_* tables are coherent — schema FKs, may_source, handlers, on_fail, "
                  "status flow, regex settings, report fields all check out; no orphans, no "
                  "settings needing justification, no stale filled_by references, GOVERNANCE.md "
                  "current, every lib module registered, no zero-config-density utilities, no "
                  "book_order/connection/candidate_rule usage gaps, no report-version clutter")

    # Full detail persists to CONFIG-REPORT.md's "findings" section (cfgreport.py mirrors the
    # same cfgquality functions) — refreshed here so the report reflects THIS run's findings, not
    # a stale prior one, before the escalation references it by path.
    report_path = cfgreport.generate(
        out_path=pathlib.Path(ctx.cfg.setting("configmaint.report_path",
                                             "iba/app/config/CONFIG-REPORT.md")))
    summary = ", ".join(f"{len(v)} {label}" for v, label in findings.values() if v)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        if decision == "approve":
            return ok(f"acknowledged: {summary} — researcher confirmed these are known/acceptable "
                      f"(full detail in {report_path})",
                      **preset)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these findings as needing action, not just acknowledgement",
                       **preset)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    question = (f"cfg_* is structurally coherent, but has findings needing your judgement: "
               f"{summary}. Full detail (every item, by category) written to {report_path} — "
               f"see the \"findings\" section.")

    # 2026-08-06: don't raise a fresh escalation for a finding that's already sitting open,
    # unanswered, from an earlier run -- see lib/escalation.py:open_duplicate for why this is
    # scoped to advisory self-checks like this one specifically (not a generic run.py fix), and
    # why it matches on `summary` (stable) rather than `question` (embeds a versioned report_path
    # that changes every call -- the bug in this fix's own first attempt, caught by re-running it).
    dup = esc.open_duplicate(ctx.db, ctx.step_id, summary)
    if dup:
        return ok(f"identical to already-open escalation #{dup['id']} (raised {dup['raised_at']}) "
                  f"— not re-raised; answer #{dup['id']} to resolve this finding. Full detail in "
                  f"{report_path}", **preset, existing_escalation_id=dup["id"])

    return escalate(
        "needs-review",
        question=question,
        preset={**preset, "report_path": str(report_path)},
        tried="coherence checks passed; these are advisory findings, not errors — approve to "
              "acknowledge as known/acceptable, reject to flag for action, or revise with a "
              "comment on what to check")


# ── propose: DB-direct, single-row, approval-gated ──────────────────────────────
def _table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')}


def _check_proposal(conn: sqlite3.Connection, table: str, op: str, where: dict, set_: dict) -> list[str]:
    e: list[str] = []
    if table not in CFG_TABLES:
        e.append(f"{table!r} is not a recognised cfg_* table (known: {sorted(CFG_TABLES)})")
        return e                                             # nothing else is checkable
    if op not in ("insert", "update", "delete"):
        e.append(f"op must be one of insert/update/delete, got {op!r}")
    cols = _table_columns(conn, table)
    if op in ("insert", "update"):
        bad = set(set_) - cols
        if bad:
            e.append(f"{table}: Set names unknown column(s) {sorted(bad)}")
    if op in ("update", "delete") and not where:
        e.append(f"{op} needs a Where clause identifying the row")
    if where:
        bad = set(where) - cols
        if bad:
            e.append(f"{table}: Where names unknown column(s) {sorted(bad)}")
    # targeted checks mirroring validate()'s rules, for the tables most likely to break
    # something if written wrong — a full hypothetical-state validate() is future work,
    # named not built (see the design doc §2.4).
    if table == "cfg_on_fail" and "path" in set_:
        valid = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='on_fail'")}
        if set_["path"] not in valid:
            e.append(f"cfg_on_fail.path {set_['path']!r} not in enum.on_fail {sorted(valid)}")
    if table == "cfg_status_flow" and set_.get("entity") == "word" and "status" in set_:
        valid = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='word_status'")}
        if set_["status"] not in valid:
            e.append(f"cfg_status_flow.status {set_['status']!r} not in enum.word_status {sorted(valid)}")
    # cfg_setting must always carry a real module — the researcher's rule against it drifting
    # into an untracked catch-all: "there must be a very good reason why a config goes into
    # settings, rather than the specific module or utility." Enforced at proposal time, not just
    # by validate() after the fact.
    if table == "cfg_setting" and op in ("insert", "update"):
        valid_modules = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='config_module'")}
        module = set_.get("module")
        if op == "insert" and not module:
            e.append("cfg_setting inserts must set 'module' — every setting is owned by a "
                     "specific module/utility, never left unattributed")
        elif module and module not in valid_modules:
            e.append(f"cfg_setting.module {module!r} not in enum.config_module {sorted(valid_modules)}")
        # Found 2026-07-22, twice in one session (raw.meaning_tree_clean_pattern, then
        # retention.report_path): cfg.setting() always does json.loads() on read, but propose
        # never checked that the proposed 'value' IS valid JSON — a bare string slipped through
        # both times and crashed the first caller. Caught here now, at propose time, not by a
        # runtime crash three steps later.
        if "value" in set_:
            try:
                json.loads(set_["value"])
            except (json.JSONDecodeError, TypeError):
                e.append(f"cfg_setting.value {set_['value']!r} is not valid JSON — cfg.setting() "
                         f"always json.loads()s it on read; a plain string must be quoted "
                         f'(e.g. \'"my string"\'), matching every other cfg_setting.value')
    return e


def _settings_justification_warning(conn: sqlite3.Connection, table: str, op: str, set_: dict) -> str | None:
    """For a NEW cfg_setting row proposed for a module that already has its own dedicated table:
    build the mandatory warning attached to the escalation payload, so the "very good reason"
    question is part of what the researcher actually sees at approval time (the representative-
    payload rule), not left to be caught later by validate()'s advisory pass."""
    if table != "cfg_setting" or op != "insert":
        return None
    module = set_.get("module")
    dedicated = MODULE_DEDICATED_TABLE.get(module)
    if not dedicated:
        return None
    return (f"NEEDS JUSTIFICATION: module {module!r} already has its own dedicated table "
           f"({dedicated}) — confirm this setting genuinely belongs in shared cfg_setting "
           f"rather than there before approving.")


def _apply(ctx: Ctx, table: str, op: str, where: dict, set_: dict) -> dict | None:
    """Perform the write; return the row's prior state (or None for insert)."""
    conn = ctx.db.conn
    before = None
    if op in ("update", "delete") and where:
        wsql = " AND ".join(f'"{k}"=?' for k in where)
        row = conn.execute(f'SELECT * FROM "{table}" WHERE {wsql}', list(where.values())).fetchone()
        before = dict(row) if row else None
    if op == "insert":
        cols = list(set_)
        ph = ",".join("?" * len(cols))
        conn.execute(f'INSERT INTO "{table}" ({",".join(chr(34)+c+chr(34) for c in cols)}) '
                     f'VALUES ({ph})', [set_[c] for c in cols])
    elif op == "update":
        ssql = ", ".join(f'"{k}"=?' for k in set_)
        wsql = " AND ".join(f'"{k}"=?' for k in where)
        conn.execute(f'UPDATE "{table}" SET {ssql} WHERE {wsql}',
                     list(set_.values()) + list(where.values()))
    elif op == "delete":
        wsql = " AND ".join(f'"{k}"=?' for k in where)
        conn.execute(f'DELETE FROM "{table}" WHERE {wsql}', list(where.values()))
    return before


def propose(ctx: Ctx) -> Outcome:
    table = ctx.params["Table"]
    op = ctx.params["Op"]
    where = json.loads(ctx.params.get("Where") or "{}")
    set_ = json.loads(ctx.params.get("Set") or "{}")
    question = ctx.params.get("Question", f"{op} on {table} — approve?")

    if table not in ctx.cfg.may_write("configmaint.propose"):
        raise PermissionError(f"write-grant violation: 'configmaint.propose' may not write {table!r}")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        if decision == "approve":
            before = _apply(ctx, table, op, where, set_)
            ctx.db.conn.execute(
                'INSERT INTO cfg_change_detail (run_id, table_name, op, where_json, set_json, '
                'before_json, applied_at) VALUES (?,?,?,?,?,?,?)',
                (ctx.run_id, table, op, json.dumps(where) or None, json.dumps(set_) or None,
                 json.dumps(before) if before is not None else None, _now()))
            return ok(f"approved and applied: {op} {table} {where or ''} -> {set_}",
                      table=table, op=op)
        if decision == "reject":
            return fail("change-rejected", f"proposal rejected: {op} {table} {where or ''} -> {set_}")
        # decision == "revise"
        return fail("needs-revision",
                    f"researcher asked for revision: {answered['comment'] or '(no comment given)'}")

    errors = _check_proposal(ctx.db.conn, table, op, where, set_)
    if errors:
        return fail("invalid-proposal", f"{len(errors)} problem(s): " + "; ".join(errors))

    warning = _settings_justification_warning(ctx.db.conn, table, op, set_)
    if warning:
        question = f"{warning}\n\n{question}"           # part of the REPRESENTATIVE payload shown

    return escalate(
        "needs-approval",
        question=question,
        preset={"table": table, "op": op, "where": where, "set": set_},
        tried="coherence-checked against the live cfg_* schema — awaiting researcher decision "
              "(approve / reject / revise-with-comment via "
              "`Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise> "
              "[-Comment ...]`)")


# ── report: regenerate CONFIG-REPORT.md ─────────────────────────────────────────
def report(ctx: Ctx) -> Outcome:
    # configmaint.report_path exists precisely so this step doesn't hard-code the path —
    # found unused during the 2026-07-21 review (see _find_orphan_configs) and fixed here.
    out_path = pathlib.Path(ctx.cfg.setting("configmaint.report_path", "iba/app/config/CONFIG-REPORT.md"))
    path = cfgreport.generate(out_path=out_path)
    return ok(f"config report written: {path}")
