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
PROJECT_ROOT = APP_ROOT.parent.parent   # repo root — scanned by find_unregistered_project_scripts (Phase 0, #672)

# Escalation #712, part 2 (2026-08-18) -- the hardcoded CFG_TABLES tuple this used to be is
# retired. History: found live 2026-08-17 trying to propose a cfg_content_index_exclude row that
# the tuple was hardcoded and not derived from cfg_table, so every cfg_* table created since it
# was last updated was invisible to configmaint.propose entirely, before ever checking grants --
# 6 tables missing that day (#712), 2 more the very next day (cfg_behaviour_class/_rule, #715/
# BUILD.md §145), each requiring a second, easy-to-forget hardcoded-tuple edit alongside the
# migration that created the table. NOT switchable to a dynamic SELECT until now because the 20
# foundational cfg_* tables (cfg_meta, cfg_table, cfg_setting, etc.) weren't themselves registered
# IN cfg_table -- deriving from it would have silently dropped them. That backfill is done
# (migration/backfill_foundational_cfg_tables_v1_20260818.py, part 1 -- verified live: 29/29
# cfg_* tables registered), so this now derives live instead of duplicating a second list by hand.
def _known_cfg_tables(conn: sqlite3.Connection) -> set[str]:
    """The set of cfg_* tables configuration_maintenance may touch — live from cfg_table
    (database='iba'), not a hardcoded tuple. A newly created cfg_* table becomes visible here as
    soon as ITS OWN migration registers it in cfg_table (governance.tables already requires this
    in the same unit of work) — no second edit to this file required, closing the recurring gap
    this class of bug kept reproducing.

    `category='rule'` (escalation #1146, 2026-08-31): a cfg_-prefixed name alone is not enough —
    `cfg_change_detail`/`cfg_change_log` share the prefix but are audit-log tables, not rule
    definitions, and must never be a configmaint.propose write target (they found live to have a
    grant that let the sanctioned gate hand-edit an immutable audit trail). Only `category='rule'`
    tables are genuine configuration; `category='log'` and `category='data'` are excluded here."""
    return {r[0] for r in conn.execute(
        "SELECT name FROM cfg_table WHERE database='iba' AND name LIKE 'cfg\\_%' ESCAPE '\\' "
        "AND inactive=0 AND category='rule'")}

# module -> the dedicated table it already has, if any (rule c's "very good reason" check).
# Moved to lib/cfgquality.py 2026-07-21 so lib/cfgreport.py can share it without a circular import.
MODULE_DEDICATED_TABLE = cfgquality.MODULE_DEDICATED_TABLE


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── validate: coherence-check the LIVE cfg_* tables (ports lib/cfgcheck.py to the DB) ──
def _validate_live(conn: sqlite3.Connection) -> list[str]:
    e: list[str] = []
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()

    # Escalation #723, 2026-08-18: this used to hardcode database='iba' throughout (escalation
    # #653's reasoning still applies — iba.db and bible_research.db share table names, e.g.
    # 'cluster'/'passage'/'verse'/'word_registry', for DIFFERENT tables, so per-database scoping
    # within each check is still required). What changed: WHICH databases to loop over is now
    # read from cfg_enum 'project_database' (bootstrap_project_database_enum_v1_20260818.py)
    # instead of being a literal — this is also the direct fix for why escalation #722's 7
    # bible_research.db tables were invisible to this check: it simply never looked.
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

    # everything below is inherently iba-only (cfg_step/cfg_on_fail/cfg_setting/cfg_api have no
    # database column at all — they're this app's own control-plane data, not per-database
    # concepts; bible_research.db has no work packages/steps/settings in this cfg_* system, it
    # still runs on the legacy engine/ pipeline). columns/tables below = iba.db's own, for the
    # span/strong column-name checks further down.
    columns = {}
    for r in q("SELECT table_name, name FROM cfg_column WHERE database='iba'"):
        columns.setdefault(r["table_name"], set()).add(r["name"])

    # STEP apis (inactive=0: escalation #310, deactivated config is excluded from validation)
    for r in q("SELECT name, route FROM cfg_api WHERE inactive=0"):
        if "{version}" not in (r["route"] or ""):
            e.append(f"step: api {r['name']} route has no {{version}} placeholder")

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

    # cfg_prose_chapter + enum.prose_chapter_status REMOVED 2026-08-27 (escalation #918 --
    # chapter-review status was workflow data about content, not a rule, and required the full
    # config-approval cycle for what is an ordinary content edit; the live equivalent is
    # bible_research.db's prose_section.status, set via Prose.ps1 -Step SetStatus, which this
    # iba.db-only validator cannot check directly -- it never ATTACHes bible_research.db (see this
    # function's own note above on that limitation). The check that used to live here is not
    # replaced; it is gone along with the table it checked.

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

    # the reverse gap — a cfg_* table with NO configmaint.propose grant at all — added 2026-08-17
    # after it crashed live twice (escalations #539/#550 historical, #666/#667 today): the checks
    # above validate that every GRANT points somewhere real; this validates every TABLE has a grant
    # to be reached through in the first place. See cfgquality.find_cfg_tables_missing_configmaint_grant.
    e.extend(cfgquality.find_cfg_tables_missing_configmaint_grant(conn))

    # step classification completeness — added 2026-07-30 (the operations/utility model). Hard
    # error: an active, dispatchable step with no classification is exactly the state run.py's
    # dispatch gate now refuses to run, so this check keeps surfacing why, not just crashing at
    # dispatch time with no coherence-report trail.
    e.extend(cfgquality.find_unclassified_active_steps(conn))

    # cfg_report_csv_table.table_name referential integrity — added 2026-07-30 (researcher: "your
    # validations is only touching settings and enum"). Same class as the on_fail.step/report-
    # step-reference checks already here; this specific table's own column was never checked.
    e.extend(cfgquality.find_bad_report_csv_table_references(conn))

    # live-schema vs cfg_table/cfg_column drift — added 2026-08-30 (escalation #1058's follow-on).
    # Every check above validates that cfg_* rows are internally coherent with EACH OTHER; nothing
    # checked cfg_table/cfg_column against the two databases' actual, live schema until now. Found
    # live the day this was built: finding_verse_index (bible_research.db, 475,790 rows, built the
    # day before) had zero cfg_table/cfg_column rows. See cfgquality.find_unregistered_tables_and_columns.
    e.extend(cfgquality.find_unregistered_tables_and_columns(conn, PROJECT_ROOT))

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
        # Phase 0 of the engine-controls migration (escalation #672) — the project-wide counterpart
        # to unregistered_lib_modules above, whole-repo not just iba/app/lib/. ADVISORY (see the
        # function's own docstring): ~345 pre-existing files are a known, already-tracked backlog
        # (Phase 2 of the same plan), not new drift — this check's job is catching what's added
        # AFTER today, not hard-failing validate over what's already known and queued.
        "unregistered_project_scripts": (
            cfgquality.find_unregistered_project_scripts(ctx.db.conn, PROJECT_ROOT),
            "project-wide script(s) missing a cfg_utility row"),
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
        # D28 (register v9) — Escalation.ps1's ValidateSet literals vs. the live cfg_enum groups
        # they're meant to mirror.
        "escalation_ps_validateset_drift": (
            cfgquality.find_escalation_ps_validateset_drift(ctx.db.conn, APP_ROOT),
            "Escalation.ps1 ValidateSet drift finding(s)"),
        # 2026-08-28 (escalation #971/#976, researcher: "configmaint should validate every
        # location reference in every config") — every *_dir/*_path/*_folder value, cfg_setting
        # AND every per-module table shaped like it, must resolve to a real folder on disk.
        "unresolvable_locations": (
            cfgquality.find_unresolvable_location_settings(ctx.db.conn, PROJECT_ROOT),
            "location setting(s) pointing at a folder that does not exist"),
        # 2026-08-28 (escalation #971/#977) — FolderPurpose.ps1's own -Type/-Status ValidateSet
        # vocabulary, checked the same way Escalation.ps1's already was.
        "folderpurpose_ps_validateset_drift": (
            cfgquality.find_folderpurpose_ps_validateset_drift(ctx.db.conn, APP_ROOT),
            "FolderPurpose.ps1 ValidateSet drift finding(s)"),
        # 2026-08-28 (escalation #863/#971/#992) — filing.archiving-trigger/naming-shape as a
        # standing check: a write hand-imitating -v{n} versioning instead of calling
        # filingkit.versioned_path()/reportkit.oneoff_path().
        "hand_rolled_versioning": (
            cfgquality.find_hand_rolled_versioning(ctx.db.conn, PROJECT_ROOT),
            "script(s) building a -v{n} filename by hand instead of via filingkit"),
        # 2026-08-29 (escalation #1007 follow-on, researcher: "any change to any PS instruction
        # will find its way into the two excel worksheets") — a script's live param() list against
        # its own tab (ps tools worksheet.xlsx) or, for Escalation.ps1, against every -Flag header
        # used anywhere in the researcher's own model sheet (escalation actions worksheet.xlsx).
        "ps_worksheet_drift": (
            cfgquality.find_ps_worksheet_drift(ctx.db.conn, APP_ROOT, PROJECT_ROOT),
            "PS script/worksheet drift finding(s)"),
        "escalation_worksheet_drift": (
            cfgquality.find_escalation_worksheet_drift(ctx.db.conn, APP_ROOT, PROJECT_ROOT),
            "Escalation.ps1/worksheet drift finding(s)"),
        # 2026-09-03 (escalation #1384, researcher: "every validation report must include a
        # detail list of all configs that is not enforced, and the reason") — the master finding
        # this whole cycle exists for. Reads cfg_behaviour_rule.enforcement_status directly, not a
        # fragile hedge-phrase text scan (the scan that FOUND this gap is exactly the kind of
        # check that stops matching the moment wording drifts).
        "unenforced_behaviour_rules": (
            cfgquality.find_unenforced_behaviour_rules(ctx.db.conn),
            "behaviour rule(s) not mechanically enforced"),
        # 2026-09-03 (escalation #1388, researcher correction of #1384's own audit): a
        # not_mechanically_checkable/context_delivered classification asserted its delivery
        # mechanism in free text and was never actually verified — this check verifies it, every
        # run, so a memory file getting deleted or a governance.* setting getting deactivated is
        # caught immediately instead of silently going stale like #1384's own miss did.
        "undelivered_conversational_rules": (
            cfgquality.find_undelivered_conversational_rules(ctx.db.conn, PROJECT_ROOT),
            "behaviour rule(s) claiming conversational delivery that does not actually verify"),
        # 2026-09-03 (escalation #1384) — the mechanical checks built the same session as the
        # rules they check, so 'buildable_not_built' doesn't silently sit unbuilt again.
        "unpushed_commits": (
            cfgquality.find_unpushed_commits(PROJECT_ROOT), "unpushed local commit finding(s)"),
        "ps_scripts_bypassing_runpy": (
            cfgquality.find_ps_scripts_bypassing_runpy(APP_ROOT),
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
    preset = {k: v[0] for k, v in findings.items()}
    if not any(preset.values()):
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

    # Full detail persists to CONFIG-REPORT.md's "findings" section (cfgreport.py mirrors the
    # same cfgquality functions) — refreshed here so the report reflects THIS run's findings, not
    # a stale prior one, before the escalation references it by path.
    report_path = cfgreport.generate(
        out_path=pathlib.Path(ctx.cfg.required_setting("configmaint.report_path")))
    summary = ", ".join(f"{len(v)} {label}" for v, label in findings.values() if v)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # escalation #798/#799 SS4: decision_required now resolves via Update()'s manual
        # vocabulary (approved) not AnswerRun's dispatcher vocabulary (approve).
        if decision in ("approve", "approved"):
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
              "comment on what to check",
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
    # escalation #1328, 2026-08-31: found live, root-caused after actually corrupting a row --
    # _apply()'s insert branch builds the INSERT entirely from `set_`; `where` is silently IGNORED
    # for insert (there is nothing to "locate" -- the row doesn't exist yet). Every correctly-shaped
    # insert in this table's own history puts identifying/key fields in Set (e.g. cfg_change_detail
    # #335/#336: {"key": "governance...", ...} all in set_json, where_json '{}'). Nothing stopped a
    # caller using Where the way it's used for update/delete instead -- exactly what happened here:
    # -Where '{"key":"configmaint.csv_export_on_auto_report"}' -Set '{"value":"0",...}' silently
    # dropped "key" from the actual INSERT, and cfg_setting.key (TEXT PRIMARY KEY, not
    # INTEGER -- SQLite does not auto-enforce NOT NULL on a non-integer PK) accepted the row with
    # key=NULL instead of erroring. Reject at the gate now, loudly and immediately, instead of
    # silently corrupting the target table.
    if op == "insert" and where:
        e.append(f"insert has no Where clause -- identifying/key fields go in Set instead "
                 f"(Where only locates an EXISTING row, for update/delete); got Where={where!r}")
    # Defense in depth, same finding: a NOT NULL column with no default, missing from Set entirely
    # (whether or not it was wrongly put in Where), would otherwise either crash uncaught or --
    # for a non-integer PRIMARY KEY, which SQLite does not auto-enforce NOT NULL on -- silently
    # insert as NULL, exactly as just reproduced live.
    if op == "insert":
        # required = NOT NULL with no default, OR a non-INTEGER primary key (SQLite auto-assigns
        # a rowid for an INTEGER PRIMARY KEY if omitted -- that's the one legitimate "optional PK"
        # case; every other PK type, like cfg_setting.key TEXT PRIMARY KEY, silently accepts NULL
        # if omitted, exactly as just reproduced).
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
    # `or "{}"` alone doesn't catch a WHITESPACE-only value (truthy in Python, but json.loads(" ")
    # still raises "Expecting value: line 1 column 1 (char 0)") -- root cause of escalation #579
    # (2026-08-10), reproduced exactly from its own recorded traceback: crashed on this line before
    # this .strip() existed. `.strip()` first so a stray space/blank -Where/-Set behaves the same as
    # an omitted one, instead of crashing.
    where = json.loads((ctx.params.get("Where") or "").strip() or "{}")
    set_ = json.loads((ctx.params.get("Set") or "").strip() or "{}")
    question = ctx.params.get("Question", f"{op} on {table} — approve?")
    title = ctx.params.get("Title")

    if table not in ctx.cfg.may_write("configmaint.propose"):
        raise PermissionError(f"write-grant violation: 'configmaint.propose' may not write {table!r}")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # escalation #798/#799 SS4: found live (escalation #809) -- decision_required now
        # resolves via Update()'s manual vocabulary (approved) not AnswerRun's dispatcher
        # vocabulary (approve); without this, an approved decision_required proposal silently
        # fell through to "needs-revision" with no actual revision requested.
        if decision in ("approve", "approved"):
            # escalation #1364, 2026-08-31: found live -- this resume/apply path called _apply()
            # directly with no validation at all, unlike the fresh-proposal path below (which runs
            # _check_proposal first). A malformed payload that was never caught at proposal time
            # (or a proposal built by hand against an already-answered run_id, bypassing the
            # gate entirely) crashed here as a raw uncaught IntegrityError instead of a routed
            # fail("invalid-proposal", ...) -- same gate, applied on both paths now.
            errors = _check_proposal(ctx.db.conn, table, op, where, set_)
            if errors:
                return fail("invalid-proposal", f"{len(errors)} problem(s): " + "; ".join(errors))
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

    # escalation #1326, 2026-08-31: -Question alone used to be forced to serve as BOTH the
    # representative description and the escalation's title, silently word-sliced to 60 chars by
    # raise_()'s lossy fallback -- every real short_description was a truncated fragment (e.g.
    # "Researcher instruction 2026-08-31: enforce that whoever pro…"). -Title is now required and
    # validated HERE, at the source, so a bad title fails loudly and immediately (a clean,
    # well-logged crash escalation, same as any other caught-by-run.py exception) instead of
    # silently degrading into a mangled record three layers downstream. -Question stays free to be
    # the real, longer description; it always survives verbatim in context (raise_()'s
    # preset["full_message"]).
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
        # escalation #798/#799: this is decision_required, which now resolves via Update() (the
        # manual ready_for_approval -> approved handshake), not AnswerRun -- corrected from the
        # pre-#798 text, which pointed at the wrong mechanism entirely.
        tried="coherence-checked against the live cfg_* schema — awaiting researcher decision via "
              "`Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then "
              "`-NextAction approved` (or reject/revise), then re-run this exact "
              "Config-Maintenance.ps1 command with -RunId to apply",
        resolution_kind="decision_required",
        # found live 2026-08-31 (escalation #1301): a plain decision_required escalation goes
        # straight to 'completed' on approval (correct for most judgement calls, which really are
        # finished once decided). A propose is different -- approval only records the decision;
        # the actual DB write happens on the SEPARATE re-run-with-RunId call below. Without this,
        # 'approved' reads as 'done' while the write is still outstanding -- exactly what happened
        # to escalations #1238-1256, caught only because they were independently re-verified
        # against the live DB rather than trusted from the escalation's own terminal state.
        needs_followup=True)


# ── report: regenerate CONFIG-REPORT.md ─────────────────────────────────────────
def report(ctx: Ctx) -> Outcome:
    # configmaint.report_path exists precisely so this step doesn't hard-code the path —
    # found unused during the 2026-07-21 review (see _find_orphan_configs) and fixed here.
    out_path = pathlib.Path(ctx.cfg.required_setting("configmaint.report_path"))
    # escalation #1314: an explicit, deliberate report run always gets its CSV pairing; the
    # auto-triggered regeneration inside validate() (below) does not, unless the researcher opts
    # in via configmaint.csv_export_on_auto_report.
    #
    # escalation #1351-1356, 2026-08-31: Config-Maintenance.ps1's OWN auto_report chain (fired
    # after every successful Propose) calls this exact same step -- a THIRD call site #1314 never
    # accounted for, neither the "explicit -Step Report" case nor the "auto-triggered inside
    # validate()" case, but which was silently defaulting to the "explicit" (always-CSV) behaviour
    # because it hits this same handler. Six Proposes in quick succession (the schema-overview
    # registration chain) each re-wrote the same CSV pairing back-to-back, and one collided with
    # its own predecessor's still-in-flight archive-rename of workflow\schema\cfg_table.csv ->
    # WinError 32 (#1351-1356). -Param Auto=1 (set by Config-Maintenance.ps1's auto_report chain
    # only) now routes this call through the SAME deferred-to-setting path validate() already
    # uses (csv_export=None -> configmaint.csv_export_on_auto_report, default 0/suppressed) --
    # a deliberate `-Step Report` call passes no such param and keeps the always-CSV guarantee.
    is_auto = str(ctx.params.get("Auto", "")).strip().lower() in ("1", "true", "yes")
    csv_export = None if is_auto else True
    path = cfgreport.generate(out_path=out_path, csv_export=csv_export)
    return ok(f"config report written: {path}")
