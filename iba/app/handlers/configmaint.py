"""configuration_maintenance handlers — the ONE sanctioned path for changing a cfg_* row.

  validate — read-only coherence check of the live cfg_* tables (the DB is master).
  propose  — DB-direct, single-row, APPROVAL-GATED; never writes silently. If this run's
             escalation has an answer, act on it; otherwise coherence-check the proposed change,
             escalate it with representative data, and pause. Approval goes through the manual
             ready_for_approval -> approved / reject / revise handshake.
  report   — regenerate CONFIG-REPORT.md from the live cfg_* tables (lib/cfgreport.py).
             Read-only; chains after an approved propose when configmaint.auto_report is true.

Every applied write is logged to `cfg_change_detail` (apply_logged).
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
PROJECT_ROOT = APP_ROOT.parent.parent   # repo root — scanned by find_unregistered_project_scripts

def _known_cfg_tables(conn: sqlite3.Connection) -> set[str]:
    """The cfg_* rule tables configuration_maintenance may touch, live from cfg_table
    (database='iba', category='rule'): a new cfg_* table is visible once its own migration registers
    it. Audit-log tables (cfg_change_detail, cfg_change_log) are never a propose target (#1146)."""
    return {r[0] for r in conn.execute(
        "SELECT name FROM cfg_table WHERE database='iba' AND name LIKE 'cfg\\_%' ESCAPE '\\' "
        "AND inactive=0 AND category='rule'")}

# module -> the dedicated table it already has (shared with lib/cfgreport.py via cfgquality)
MODULE_DEDICATED_TABLE = cfgquality.MODULE_DEDICATED_TABLE


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── validate: coherence-check the LIVE cfg_* tables ──
def _validate_live(conn: sqlite3.Connection) -> list[str]:
    e: list[str] = []
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()

    # The databases come from cfg_enum 'project_database'. iba.db and bible_research.db share table
    # names for different tables, so each check is scoped per database.
    databases = [r["value"] for r in q("SELECT value FROM cfg_enum WHERE name='project_database'")]
    real_cfg_tables = {r[0] for r in q(
        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg\\_%' ESCAPE '\\'")}
    tables: dict[str, set[str]] = {}       # database -> table names (used below for cfg_write_grant)

    for db in databases:
        db_tables = {r["name"] for r in q("SELECT name FROM cfg_table WHERE database=?", (db,))}
        tables[db] = db_tables
        columns: dict[str, set[str]] = {}
        for r in q("SELECT table_name, name FROM cfg_column WHERE database=?", (db,)):
            columns.setdefault(r["table_name"], set()).add(r["name"])

        # schema integrity
        for t in db_tables:
            pk_n = q("SELECT COUNT(*) n FROM cfg_column WHERE database=? AND table_name=? "
                    "AND is_pk=1", (db, t))[0]["n"]
            if pk_n > 1:
                e.append(f"schema: {db}.{t} has {pk_n} primary keys")
        for r in q("SELECT table_name, name, fk FROM cfg_column WHERE database=? AND "
                  "fk IS NOT NULL", (db,)):
            rt, _, rc = r["fk"].partition(".")
            if rt not in db_tables:
                e.append(f"schema: {db}.{r['table_name']}.{r['name']} FK -> unknown table {rt!r}")
            elif rc not in columns.get(rt, set()):
                e.append(f"schema: {db}.{r['table_name']}.{r['name']} FK -> unknown column "
                         f"{rt}.{rc}")
        for r in q("SELECT table_name, col FROM cfg_unique WHERE database=?", (db,)):
            if r["col"] not in columns.get(r["table_name"], set()):
                e.append(f"schema: {db}.{r['table_name']} unique names unknown column "
                         f"{r['col']!r}")

        # write grants: every granted table must be a real table (data OR cfg_*, cfg_* tables
        # only physically exist in iba.db, hence the real_cfg_tables fallback applying to every
        # database's grants — a bible_research grant naming a cfg_* table would be a real error).
        for r in q("SELECT DISTINCT writer, table_name FROM cfg_write_grant WHERE database=? "
                  "AND inactive=0", (db,)):
            if r["table_name"] not in db_tables and r["table_name"] not in real_cfg_tables:
                e.append(f"rules: write_grant ({db}) {r['writer']!r} -> unknown table "
                         f"{r['table_name']!r}")

    # below is iba-only: cfg_step/cfg_on_fail/cfg_setting/cfg_api are this app's control plane, with
    # no database column. columns = iba.db's own, for the span/strong column-name checks.
    columns = {}
    for r in q("SELECT table_name, name FROM cfg_column WHERE database='iba'"):
        columns.setdefault(r["table_name"], set()).add(r["name"])

    # STEP apis (inactive config is excluded from validation)
    for r in q("SELECT name, route FROM cfg_api WHERE inactive=0"):
        if "{version}" not in (r["route"] or ""):
            e.append(f"step: api {r['name']} route has no {{version}} placeholder")

    # step names must be unique across work packages: escalation and cfg_on_fail match by step alone
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

    # every cfg_setting must have a real module (cfg_enum config_module)
    valid_modules = {r["value"] for r in q("SELECT value FROM cfg_enum WHERE name='config_module'")}
    for r in q("SELECT key, module FROM cfg_setting WHERE inactive=0"):
        if not r["module"]:
            e.append(f"consistency: cfg_setting {r['key']!r} has no module — every setting must "
                     f"be attributed to a module/utility")
        elif r["module"] not in valid_modules:
            e.append(f"consistency: cfg_setting {r['key']!r} names unknown module {r['module']!r} "
                     f"(not in enum.config_module {sorted(valid_modules)})")

    # governance.reports_must_persist: every quality-check step has a report path
    standard = q("SELECT value FROM cfg_setting WHERE key='governance.reports_must_persist'")
    if standard:
        for msg in cfgquality.find_missing_report_paths(conn):
            e.append(f"governance ({json.loads(standard[0]['value'])}): {msg}")

    # every known report-producing step needs its cfg_report row; every chained work package its
    # complete_message
    for msg in cfgquality.find_missing_cfg_report_rows(conn):
        e.append(f"report-governance: {msg}")
    for msg in cfgquality.find_chained_packages_missing_complete_message(conn):
        e.append(f"report-governance: {msg}")

    # value-quality: every cfg_column declaring expectation enum.<name> holds only that enum's values
    e.extend(valuequality.find_enum_violations(conn))

    # report rows and write grants must name an active step (hard errors)
    e.extend(cfgquality.find_report_step_references(conn))
    writer_identities = set(_writer_identities(conn))
    e.extend(cfgquality.find_unknown_write_grant_writers(conn, writer_identities))

    # every cfg_* rule table needs a configmaint.propose grant (cfgquality.find_cfg_tables_missing_configmaint_grant)
    e.extend(cfgquality.find_cfg_tables_missing_configmaint_grant(conn))

    # every active step must have a kind (run.py refuses to dispatch one without)
    e.extend(cfgquality.find_unclassified_active_steps(conn))

    # cfg_report_csv_table.table_name referential integrity
    e.extend(cfgquality.find_bad_report_csv_table_references(conn))

    # live schema vs cfg_table/cfg_column, both databases (cfgquality.find_unregistered_tables_and_columns)
    e.extend(cfgquality.find_unregistered_tables_and_columns(conn, PROJECT_ROOT))
    # live triggers vs cfg_trigger, both databases (#2110)
    e.extend(cfgquality.find_unregistered_triggers(conn, PROJECT_ROOT))

    return e


def _writer_identities(conn: sqlite3.Connection) -> tuple[str, ...]:
    return tuple(r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='writer_identity' AND inactive=0")) \
        or cfgquality._WRITER_IDENTITY_FALLBACK


# shared with lib/cfgreport.py through cfgquality
_find_settings_needing_justification = cfgquality.find_settings_needing_justification


def _find_orphan_configs(conn: sqlite3.Connection) -> list[str]:
    return cfgquality.find_orphan_configs(conn, APP_ROOT)


_ADVISORY_TRIED = ("coherence checks passed; these are advisory findings, not errors — approve to "
                   "acknowledge as known/acceptable, reject to flag for action, or revise with a "
                   "comment on what to check")


def validate(ctx: Ctx) -> Outcome:
    """Hard coherence errors (schema/FK/enum breaks) fail outright, report-stop. Findings that need
    a researcher judgement (an orphan config, a setting that may belong in its own table) go to
    CONFIG-REPORT.md in full; an escalation is raised only for findings not yet acknowledged, and
    carries counts, fingerprints and the report path, never the lists (BUILD.md sec 42, #2206)."""
    errors = _validate_live(ctx.db.conn)
    # a live script in no utility or module is a hard error (#2198, #2200)
    errors += cfgquality.find_unregistered_project_scripts(ctx.db.conn, PROJECT_ROOT)
    # every rule linked to the operations it governs (#2209)
    errors += cfgquality.find_rule_scope_gaps(ctx.db.conn, APP_ROOT)
    if errors:
        error_summary = "; ".join(errors)
        # Every run has a fresh run_id, so run.py's idempotency guard never catches a repeat: an
        # identical still-open escalation is matched on the error text instead. ok(), not fail(),
        # because fail() would write a fresh report-stop row regardless; the open escalation stays
        # the record.
        dup = esc.open_duplicate(ctx.db, ctx.step_id, error_summary)
        if dup:
            return ok(f"identical to already-open escalation #{dup['id']} (raised "
                      f"{dup['raised_at']}) — not re-raised; answer #{dup['id']} to resolve. "
                      f"{len(errors)} coherence error(s): {error_summary}",
                      errors=error_summary, existing_escalation_id=dup["id"])
        return fail("invalid", f"{len(errors)} coherence error(s)", errors=error_summary)

    # every advisory (judgement-call) finding: key -> (findings, label used in messages)
    findings: dict[str, tuple[list[str], str]] = {
        "orphans": (_find_orphan_configs(ctx.db.conn), "orphan config(s)"),
        "needs_justification": (_find_settings_needing_justification(ctx.db.conn),
                                "setting(s) needing justification"),
        "stale_filled_by": (cfgquality.find_filled_by_referencing_inactive_step(ctx.db.conn),
                           "column(s) with a stale filled_by"),
        "unregistered_lib_modules": (cfgquality.find_unregistered_lib_modules(ctx.db.conn, APP_ROOT),
                                    "lib module(s) missing a cfg_utility row"),
        "low_config_density_utilities": (cfgquality.find_utility_config_density(ctx.db.conn),
                                        "utility module(s) with zero cfg.setting()/cfg.enum() usage"),
        # usage checks beyond cfg_setting/cfg_enum
        "orphan_book_order": (cfgquality.find_orphan_book_order(ctx.db.conn, APP_ROOT),
                             "cfg_book_order finding(s)"),
        "orphan_connection": (cfgquality.find_orphan_connection_keys(ctx.db.conn, APP_ROOT),
                             "cfg_connection finding(s)"),
        "orphan_candidate_rule": (cfgquality.find_orphan_candidate_rules(ctx.db.conn, APP_ROOT),
                                "cfg_candidate_rule finding(s)"),
        # a one-off report lineage with more than one live version (oneoff_path archives first)
        "report_version_clutter": (cfgquality.find_report_version_clutter(ctx.db.conn, APP_ROOT),
                                  "report lineage(s) with more than one live version"),
        # Escalation.ps1 ValidateSet literals vs. the cfg_enum groups they mirror
        "escalation_ps_validateset_drift": (
            cfgquality.find_escalation_ps_validateset_drift(ctx.db.conn, APP_ROOT),
            "Escalation.ps1 ValidateSet drift finding(s)"),
        # every *_dir/*_path/*_folder value, in cfg_setting and every per-module table, must be a folder
        "unresolvable_locations": (
            cfgquality.find_unresolvable_location_settings(ctx.db.conn, PROJECT_ROOT),
            "location setting(s) pointing at a folder that does not exist"),
        # FolderPurpose.ps1 -Type/-Status ValidateSet vs. cfg_enum
        "folderpurpose_ps_validateset_drift": (
            cfgquality.find_folderpurpose_ps_validateset_drift(ctx.db.conn, APP_ROOT),
            "FolderPurpose.ps1 ValidateSet drift finding(s)"),
        # a write building -v{n} by hand instead of filingkit.versioned_path()/reportkit.oneoff_path()
        "hand_rolled_versioning": (
            cfgquality.find_hand_rolled_versioning(ctx.db.conn, PROJECT_ROOT),
            "script(s) building a -v{n} filename by hand instead of via filingkit"),
        # PS param() lists vs. the ps tools worksheet, and Escalation.ps1 vs. the escalation actions worksheet
        "ps_worksheet_drift": (
            cfgquality.find_ps_worksheet_drift(ctx.db.conn, APP_ROOT, PROJECT_ROOT),
            "PS script/worksheet drift finding(s)"),
        "escalation_worksheet_drift": (
            cfgquality.find_escalation_worksheet_drift(ctx.db.conn, APP_ROOT, PROJECT_ROOT),
            "Escalation.ps1/worksheet drift finding(s)"),
        # every behaviour rule with no control, with its reason (enforcement_status, #2206)
        "unenforced_behaviour_rules": (
            cfgquality.find_unenforced_behaviour_rules(ctx.db.conn),
            "behaviour rule(s) with no control"),
        # conversational rules whose claimed delivery does not verify
        "undelivered_conversational_rules": (
            cfgquality.find_undelivered_conversational_rules(ctx.db.conn, PROJECT_ROOT),
            "behaviour rule(s) claiming conversational delivery that does not actually verify"),
        # mechanical checks of individual behaviour rules (#1384)
        "unpushed_commits": (
            cfgquality.find_unpushed_commits(PROJECT_ROOT), "unpushed local commit finding(s)"),
        "ps_scripts_bypassing_runpy": (
            cfgquality.find_ps_scripts_bypassing_runpy(ctx.db.conn, APP_ROOT),
            "PS script(s) bypassing run.py"),
        "steps_without_ps_script": (
            cfgquality.find_steps_without_ps_script(ctx.db.conn),
            "active step(s) with no PS entry point"),
        "escalation_file_naming": (
            cfgquality.find_escalation_file_naming_violations(ctx.db.conn, PROJECT_ROOT),
            "escalation-tied file(s) not carrying their escalation-id prefix"),
        "config_hedge_phrases": (
            cfgquality.find_hedge_phrases_in_active_config(ctx.db.conn),
            "cfg_method_rule/cfg_setting row(s) still carrying an unresolved hedge phrase"),
        "restated_authoritative_content": (
            cfgquality.find_restated_authoritative_content(ctx.db.conn, PROJECT_ROOT),
            "governance-doc paragraph(s) restating cfg_* content instead of pointing to it"),
        "query_file_convention": (
            cfgquality.find_query_file_convention_violations(PROJECT_ROOT),
            "SQL scratch file(s) violating the scripts/SQLite/ folder convention"),
    }
    # counts only: the full lists live in CONFIG-REPORT.md, never in the escalation (BUILD.md sec 42)
    counts = {k: len(v) for k, (v, _) in findings.items() if v}
    if not counts:
        return ok("cfg_* tables are coherent — schema FKs, may_source, handlers, on_fail, "
                  "status flow, regex settings, report fields all check out; no orphans, no "
                  "settings needing justification, no stale filled_by references, GOVERNANCE.md "
                  "current, every lib module registered, no zero-config-density utilities, no "
                  "book_order/connection/candidate_rule usage gaps, no report-version clutter, no "
                  "Escalation.ps1/FolderPurpose.ps1 ValidateSet drift, no unresolvable location "
                  "settings, no hand-rolled versioning, no PS script/worksheet drift, no "
                  "unenforced behaviour rules, no unpushed commits, no run.py bypass, every step "
                  "has a PS entry point, no escalation-file naming drift, no config hedge phrases, "
                  "no restated authoritative content, no query-file convention violations")

    # refresh CONFIG-REPORT.md's findings section before the escalation references it
    report_path = cfgreport.generate(
        out_path=pathlib.Path(ctx.cfg.required_setting("configmaint.report_path")))
    summary = ", ".join(f"{len(v)} {label}" for v, label in findings.values() if v)
    fingerprints = {k: sorted(esc.finding_fingerprint(i) for i in v)
                    for k, (v, _) in findings.items() if v}

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # decision_required resolves via Update's vocabulary (approved)
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {summary} — researcher confirmed these are known/acceptable "
                      f"(full detail in {report_path})",
                      **counts)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these findings as needing action, not just acknowledgement",
                       **counts)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    # #2206 option 1: a finding already acknowledged (the latest approved advisory escalation) is
    # not asked again; only findings new since then are
    base_id, acknowledged = esc.acknowledged_findings(ctx.db, ctx.step_id, _ADVISORY_TRIED[:40])
    new = {k: [i for i in v if esc.finding_fingerprint(i) not in acknowledged.get(k, set())]
           for k, (v, _) in findings.items() if v}
    new_summary = ", ".join(f"{len(new[k])} {label}" for k, (v, label) in findings.items()
                            if new.get(k))
    if base_id and not new_summary:
        return ok(f"no new findings: {summary}, all acknowledged in #{base_id}. Full detail in "
                  f"{report_path}", **counts, acknowledged_in=base_id)
    since = f" since #{base_id} was acknowledged" if base_id else ""
    question = (f"cfg_* is structurally coherent, but has new findings{since} needing your "
               f"judgement: {new_summary}. All findings: {summary}. Full detail (every item, by "
               f"category) written to {report_path} — see the \"findings\" section.")
    # `summary` stays in the stored context: open_duplicate matches an unchanged re-run on it
    preset = {"summary": summary, "counts": counts, "new": {k: len(v) for k, v in new.items() if v},
              "fingerprints": fingerprints, "report_path": str(report_path)}

    # an identical finding already open from an earlier run is not raised again; matched on
    # `summary` (stable), not `question` (embeds a versioned report path)
    dup = esc.open_duplicate(ctx.db, ctx.step_id, summary)
    if dup:
        return ok(f"identical to already-open escalation #{dup['id']} (raised {dup['raised_at']}) "
                  f"— not re-raised; answer #{dup['id']} to resolve this finding. Full detail in "
                  f"{report_path}", **counts, existing_escalation_id=dup["id"])

    # the findings changed while an advisory escalation is still open: record them on it (#2108)
    prior = esc.open_for_step(ctx.db, ctx.step_id, _ADVISORY_TRIED[:40])
    if prior:
        esc.update(ctx.cfg, ctx.db, prior["id"], originator="Claude",
                   comment=f"configmaint.validate re-run {ctx.run_id}: the findings changed, now "
                           f"{new_summary} new{since}; all findings: {summary}. Full detail in "
                           f"{report_path}.",
                   # one JSON line: approving this item acknowledges exactly this set
                   context=json.dumps({"findings_as_of": ctx.run_id, **preset}),
                   # D26: work cannot be attached to an item left at 'raised'
                   state="in-progress" if prior["state"] == "raised" else None)
        return ok(f"findings changed since open escalation #{prior['id']} -- recorded on it as a new "
                  f"version, not re-raised. Full detail in {report_path}",
                  **counts, existing_escalation_id=prior["id"])

    return escalate(
        "needs-review",
        question=question,
        preset={**preset, "report_path": str(report_path)},
        tried=_ADVISORY_TRIED,
        resolution_kind="decision_required")


# ── propose: DB-direct, single-row, approval-gated ──────────────────────────────
def _table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')}


def _check_proposal(conn: sqlite3.Connection, table: str, op: str, where: dict, set_: dict) -> list[str]:
    e: list[str] = []
    known = _known_cfg_tables(conn)
    if table not in known:
        e.append(f"{table!r} is not a recognised cfg_* table (known: {sorted(known)})")
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
    # an insert takes its key fields from Set; a Where on insert would be ignored silently and could
    # insert a NULL key (#1328)
    if op == "insert" and where:
        e.append(f"insert has no Where clause -- identifying/key fields go in Set instead "
                 f"(Where only locates an EXISTING row, for update/delete); got Where={where!r}")
    if op == "insert":
        # every required column (NOT NULL without default, or a non-INTEGER primary key, which SQLite
        # lets be NULL) must be in Set
        required = {r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')
                   if (r[3] and r[4] is None) or (r[5] and r[2].upper() != "INTEGER")}
        missing = required - set(set_)
        if missing:
            e.append(f"{table}: insert is missing required column(s) {sorted(missing)} in Set "
                     f"(NOT NULL/primary-key, no default)")
    if where:
        bad = set(where) - cols
        if bad:
            e.append(f"{table}: Where names unknown column(s) {sorted(bad)}")
    # targeted checks mirroring validate()'s rules, for the tables most likely to break something
    if table == "cfg_on_fail" and "path" in set_:
        valid = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='on_fail'")}
        if set_["path"] not in valid:
            e.append(f"cfg_on_fail.path {set_['path']!r} not in enum.on_fail {sorted(valid)}")
    if table == "cfg_status_flow" and set_.get("entity") == "word" and "status" in set_:
        valid = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='word_status'")}
        if set_["status"] not in valid:
            e.append(f"cfg_status_flow.status {set_['status']!r} not in enum.word_status {sorted(valid)}")
    # cfg_setting must always carry a real module
    if table == "cfg_setting" and op in ("insert", "update"):
        valid_modules = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='config_module'")}
        module = set_.get("module")
        if op == "insert" and not module:
            e.append("cfg_setting inserts must set 'module' — every setting is owned by a "
                     "specific module/utility, never left unattributed")
        elif module and module not in valid_modules:
            e.append(f"cfg_setting.module {module!r} not in enum.config_module {sorted(valid_modules)}")
        # cfg.setting() json-decodes on read, so a proposed value must be valid JSON
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
    the warning attached to the escalation payload, so the "very good reason" question is part of
    what the researcher sees at approval time."""
    if table != "cfg_setting" or op != "insert":
        return None
    module = set_.get("module")
    dedicated = MODULE_DEDICATED_TABLE.get(module)
    if not dedicated:
        return None
    return (f"NEEDS JUSTIFICATION: module {module!r} already has its own dedicated table "
           f"({dedicated}) — confirm this setting genuinely belongs in shared cfg_setting "
           f"rather than there before approving.")


def apply_logged(conn: sqlite3.Connection, run_id: str, table: str, op: str, where: dict,
                 set_: dict) -> dict | None:
    """The ONE audited cfg_* write: performs it and logs it to cfg_change_detail (run_id, table,
    op, where, set, the row's prior state, applied_at). Used by propose (after approval) and by
    Developer Mode config migrations (Developer Mode removes the approval gate, never the audit).
    The caller owns the transaction. Returns the prior state."""
    before = _apply_conn(conn, table, op, where, set_)
    conn.execute(
        'INSERT INTO cfg_change_detail (run_id, table_name, op, where_json, set_json, '
        'before_json, applied_at) VALUES (?,?,?,?,?,?,?)',
        (run_id, table, op, json.dumps(where) or None, json.dumps(set_) or None,
         json.dumps(before) if before is not None else None, _now()))
    return before


def _apply(ctx: Ctx, table: str, op: str, where: dict, set_: dict) -> dict | None:
    return _apply_conn(ctx.db.conn, table, op, where, set_)


def _apply_conn(conn: sqlite3.Connection, table: str, op: str, where: dict,
                set_: dict) -> dict | None:
    """Perform the write; return the row's prior state (or None for insert)."""
    before = None
    if op in ("update", "delete") and where:
        wsql = " AND ".join(f'"{k}"=?' for k in where)
        cur = conn.execute(f'SELECT * FROM "{table}" WHERE {wsql}', list(where.values()))
        row = cur.fetchone()      # by column name, whatever the connection's row_factory
        before = dict(zip([d[0] for d in cur.description], row)) if row else None
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
    # .strip() first: a blank or whitespace-only -Where/-Set means none (#579)
    where = json.loads((ctx.params.get("Where") or "").strip() or "{}")
    set_ = json.loads((ctx.params.get("Set") or "").strip() or "{}")
    question = ctx.params.get("Question", f"{op} on {table} — approve?")
    title = ctx.params.get("Title")

    if table not in ctx.cfg.may_write("configmaint.propose"):
        raise PermissionError(f"write-grant violation: 'configmaint.propose' may not write {table!r}")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # decision_required resolves via Update's vocabulary (approved)
        if decision in ("approve", "approved"):
            # the apply path runs the same proposal check as a fresh proposal (#1364)
            errors = _check_proposal(ctx.db.conn, table, op, where, set_)
            if errors:
                return fail("invalid-proposal", f"{len(errors)} problem(s): " + "; ".join(errors))
            apply_logged(ctx.db.conn, ctx.run_id, table, op, where, set_)
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

    # -Title is required and title-shape checked here (#1326); -Question carries the full
    # description, kept in the escalation context
    if not title:
        raise ValueError(
            "propose requires -Title -- a short, title-shaped name for this change (<=60 chars, "
            "no clause-stitching, e.g. 'Add configmaint.csv_export_on_auto_report setting'). "
            "-Question is the fuller representative description (what/why/effect), not the title.")
    title_err = esc._title_shape_error(title)
    if title_err:
        raise ValueError(f"-Title {title_err}")

    return escalate(
        "needs-approval",
        question=question,
        title=title,
        preset={"table": table, "op": op, "where": where, "set": set_},
        tried="coherence-checked against the live cfg_* schema — awaiting researcher decision via "
              "`Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then "
              "`-NextAction approved` (or reject/revise), then re-run this exact "
              "Config-Maintenance.ps1 command with -RunId to apply",
        resolution_kind="decision_required",
        # approval only records the decision; the write happens on the re-run with -RunId, so the item
        # routes back to Claude rather than completing (#1301)
        needs_followup=True)


# ── report: regenerate CONFIG-REPORT.md ─────────────────────────────────────────
def report(ctx: Ctx) -> Outcome:
    out_path = pathlib.Path(ctx.cfg.required_setting("configmaint.report_path"))
    # an explicit -Step Report always writes its CSV pairing; the auto-triggered runs (inside
    # validate, and Config-Maintenance.ps1's auto_report chain via -Param Auto=1) defer to
    # configmaint.csv_export_on_auto_report (#1314, #1351-1356)
    is_auto = str(ctx.params.get("Auto", "")).strip().lower() in ("1", "true", "yes")
    csv_export = None if is_auto else True
    path = cfgreport.generate(out_path=out_path, csv_export=csv_export)
    return ok(f"config report written: {path}")
