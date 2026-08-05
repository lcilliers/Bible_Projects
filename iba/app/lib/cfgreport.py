"""cfgreport.py — full-visibility config report, generated FROM the config store.

Reads only the cfg_* tables in the DATABASE (the authoritative config at runtime — not
the JSON seeds) and writes one readable markdown snapshot of EVERY configuration the app
holds. Regenerated automatically at the end of every accepted cfgload (config only reaches
the DB through the loader, so that is the 'after each change' trigger), and runnable on
demand:

    python -m iba.app.lib.cfgreport            # refresh the snapshot now

Read-only. No writes to the DB. No AI calls.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sqlite3

from . import cfgquality, reportkit

APP = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = APP / "db" / "iba.db"
OUT_PATH = APP / "config" / "CONFIG-REPORT.md"
STEP = "configmaint.report"


def _disp(v) -> str:
    if v is None:
        return ""
    try:
        return str(json.loads(v))
    except Exception:
        return str(v)


def _cell(v) -> str:
    return _disp(v).replace("|", "\\|").replace("\n", " ")


def _table(headers: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(_cell(c) for c in r) + " |")
    if not rows:
        out.append("| " + " | ".join("_(none)_" for _ in headers) + " |")
    return out


# the same 14 config-content tables the escalation #310 bootstrap added `inactive` to
# (bootstrap_inactive_column.py) — kept here too rather than imported, so this list stays a
# deliberate, reviewable fact the same way CFG_TABLES/REPORT_STEPS are, not a generic scan.
INACTIVE_TABLES = (
    "cfg_setting", "cfg_step", "cfg_work_package", "cfg_write_grant", "cfg_report",
    "cfg_report_section", "cfg_report_csv_table", "cfg_candidate_rule", "cfg_enum",
    "cfg_on_fail", "cfg_status_flow", "cfg_book_order", "cfg_api", "cfg_connection",
)

# table -> the SQL expression identifying one inactive row, readably. cfg_candidate_rule is
# grouped by kind+count instead (below) — individual accept/reject Strong's codes would make the
# list unreadable at real volume (289 rows in one kind alone).
_INACTIVE_LABEL = {
    "cfg_setting": "key",
    "cfg_step": "work_package || '/' || step",
    "cfg_work_package": "name",
    "cfg_write_grant": "writer || ' -> ' || table_name",
    "cfg_report": "step",
    "cfg_report_section": "step || '/' || section_key",
    "cfg_report_csv_table": "step || '/' || table_name",
    "cfg_enum": "name || '=' || value",
    "cfg_on_fail": "step || '/' || condition",
    "cfg_status_flow": "entity || '/' || status",
    "cfg_book_order": "book",
    "cfg_api": "name",
    "cfg_connection": "key",
}


# Known whole-subsystem retirements — a bulk `inactive=1` sweep for a deliberately closed decision,
# not evidence of stalled/unfinished work. Named explicitly (same discipline `DATA_TABLES`/
# `REPORT_STEPS` already use elsewhere) so "Inactive configs (367 rows...)" doesn't read as an
# unexplained pile — found 2026-07-30 (researcher's own read of this section) that it does exactly
# that with no attribution at all. Checked, not assumed: every one of the 367 rows was individually
# traced and every single one belongs to one of these two events, zero left over.
_RETIREMENT_EVENTS = (
    ("candidate", "candidate-system retraction, 2026-07-23 (GOVERNANCE.md §15D; "
                 "migration/retract_candidate_system.py)"),
    ("passage", "passage-system retirement, 2026-07-26 "
               "(reports/archive/passage-system-retirement-record-20260726.md)"),
)


def _classify_retirement(table: str, label: str) -> str | None:
    """Which known retirement event a deactivated row belongs to, or None if unattributed.
    Checked by substring on the row's own identity (module/step/table names), not by table alone
    or a hardcoded count, so this stays accurate as either event's rows change AND so a genuinely
    NEW/unrelated deactivation surfaces as unattributed instead of silently blending into the
    total the way the plain count already was doing."""
    if table == "cfg_candidate_rule":
        return "candidate"          # the table's entire purpose is candidate meaning-net inputs
    low = label.lower()
    for key, _ in _RETIREMENT_EVENTS:
        if key in low:
            return key
    return None


def _utilities_table(q) -> list[str]:
    """Full `cfg_utility` registry — module/file/purpose/active/exempt — added 2026-07-30 per the
    researcher's own read of §0: "is the utility in the cfg.utility table? the contents page of
    the report does not include the utility table." There was no way to cross-reference a §0
    finding against the actual registry without a raw SQL query; this makes it browsable in the
    same document, with `config_exempt`/`config_exempt_reason` (new columns, `migration/
    add_cfg_utility_config_exempt.py`) visible right next to each module."""
    rows = q("SELECT module, file_path, purpose, inactive, config_exempt, config_exempt_reason "
             "FROM cfg_utility ORDER BY module")
    n_exempt = sum(1 for r in rows if r["config_exempt"])
    n_inactive = sum(1 for r in rows if r["inactive"])
    S = [
        f"**{len(rows)}** registered module(s) — **{n_exempt}** declared `config_exempt` (a "
        f"legitimate zero for config-setting/enum usage, not a completeness gap), **{n_inactive}** "
        f"inactive (module removed/merged). See §0 \"Low config-density utilities\" for any "
        f"NON-exempt module still flagged.",
        "",
        "| module | file | purpose | active | exempt | exempt reason |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        S.append("| " + " | ".join([
            r["module"],
            r["file_path"],
            (r["purpose"] or "").replace("|", "\\|"),
            "" if r["inactive"] else "✓",
            "✓" if r["config_exempt"] else "",
            (r["config_exempt_reason"] or "").replace("|", "\\|"),
        ]) + " |")
    return S


def _inactive_configs(q) -> list[str]:
    """Every deactivated config row, escalation #310 — DEACTIVATED, not deleted: excluded from
    configmaint.validate's coherence/orphan/justification checks (see cfgquality.py), but listed
    here in full so nothing goes quietly missing. cfg_candidate_rule is summarised by kind+count
    (individual Strong's codes at real volume would swamp the report, not inform it). Also
    attributes every row to a known retirement event (`_RETIREMENT_EVENTS`) where one applies —
    see that constant's comment for why."""
    lines: list[str] = []
    total_rows = 0
    total_tables = 0
    tally: dict[str | None, int] = {}
    unattributed: list[str] = []
    for table, expr in _INACTIVE_LABEL.items():
        rows = q(f'SELECT {expr} AS label FROM "{table}" WHERE inactive=1 ORDER BY label')
        if not rows:
            continue
        total_rows += len(rows)
        total_tables += 1
        lines.append(f"- **{table}** ({len(rows)}): " + ", ".join(f"`{r['label']}`" for r in rows))
        for r in rows:
            event = _classify_retirement(table, r["label"])
            tally[event] = tally.get(event, 0) + 1
            if event is None:
                unattributed.append(f"{table}.{r['label']}")
    cand = q("SELECT kind, COUNT(*) n FROM cfg_candidate_rule WHERE inactive=1 GROUP BY kind "
             "ORDER BY kind")
    if cand:
        n = sum(r["n"] for r in cand)
        total_rows += n
        total_tables += 1
        lines.append("- **cfg_candidate_rule** (by kind): "
                     + ", ".join(f"{r['kind']}={r['n']}" for r in cand))
        tally["candidate"] = tally.get("candidate", 0) + n

    attribution = [f"{tally[key]} from the {desc}" for key, desc in _RETIREMENT_EVENTS if tally.get(key)]
    if unattributed:
        attribution.append(f"**{len(unattributed)} UNATTRIBUTED** (not part of a known retirement "
                           "— needs a look): " + ", ".join(unattributed))
    header = (f"**Inactive configs** ({total_rows} row(s) across {total_tables} table(s)) — "
             f"deactivated, not deleted; excluded from validation above.")
    if attribution:
        header += " " + "; ".join(attribution) + "."
    return [header] + (lines if lines else ["_(none)_"])


def generate(db_path: pathlib.Path = DB_PATH, out_path: pathlib.Path = OUT_PATH) -> pathlib.Path:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()
    meta = {r["key"]: r["value"] for r in q("SELECT key, value FROM cfg_meta")}
    latest = q("SELECT * FROM cfg_change_log ORDER BY id DESC LIMIT 1")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    intro = [
        "> **Generated snapshot of the live config store** (`iba/app/db/iba.db`, tables "
        "`cfg_*`). The DB is master — do not hand-edit this file. Change config only via "
        "`configmaint.propose` (approval-gated; see GOVERNANCE.md §5A); this report "
        "regenerates automatically after an approved change and is overwritten in place.",
        "",
    ] + _table(["field", "value"], [
        ["database", meta.get("database")],
        ["config_version", meta.get("config_version")],
        ["generated_at", now],
        ["current_seed_hash", latest[0]["seed_hash"] if latest else "(no load logged)"],
    ])

    sections: dict[str, list[str]] = {}

    finding_groups = [
        ("Orphan configs", "a `cfg_setting`/`cfg_enum` not referenced by any code",
         cfgquality.find_orphan_configs(conn, APP)),
        ("Settings needing justification", "module already has its own dedicated table",
         cfgquality.find_settings_needing_justification(conn)),
        ("Missing report paths", "a quality-check step with nowhere for its findings to persist "
         "(governance.reports_must_persist violation)",
         cfgquality.find_missing_report_paths(conn)),
        ("Stale filled_by", "cfg_column.filled_by names a now-inactive step",
         cfgquality.find_filled_by_referencing_inactive_step(conn)),
        ("Stale governance docs", "GOVERNANCE.md older than the newest applied config change",
         cfgquality.find_stale_governance_docs(conn, APP)),
        ("Unregistered lib modules", "iba/app/lib/*.py with no cfg_utility row",
         cfgquality.find_unregistered_lib_modules(conn, APP)),
        # NOTE: deliberately NOT spelling out the literal call-site pattern here (see the
        # `find_utility_config_density` docstring for why) — `find_orphan_configs`-style checks in
        # this app work by substring-scanning a file's raw text, docstrings and comments included;
        # writing the literal pattern into THIS file's own source would falsely mark cfgreport.py
        # itself as "using" it. Found live 2026-07-30: an earlier draft of this exact line did
        # exactly that, silently dropping cfgreport.py off its own report's flagged list.
        ("Low config-density utilities", "NON-EXEMPT cfg_utility module with zero real Cfg-method "
         "call sites of its own (see §2 Utilities registry for the full module list, including "
         "the 11 already declared config_exempt)",
         cfgquality.find_utility_config_density(conn)),
        # 2026-07-30 — extending find_orphan_configs' usage check past cfg_setting/cfg_enum to the
        # three other tables that had none (researcher: "your validations is only touching settings
        # and enum and not incorporating all the other config tables").
        ("Orphan book_order", "cfg.book_order() unused, or a duplicate book/ordinal",
         cfgquality.find_orphan_book_order(conn, APP)),
        ("Orphan connection keys", "a cfg_connection key not read via cfg.connection(...) anywhere",
         cfgquality.find_orphan_connection_keys(conn, APP)),
        ("Orphan candidate rules", "a kind called with zero active rows, or active rows no code "
         "asks for",
         cfgquality.find_orphan_candidate_rules(conn, APP)),
    ]
    # this section is the ACTIONABLE detail behind configmaint.validate's escalation — that
    # escalation question stays short (counts + this report path) precisely because every item
    # is listed here in full, once, not repeated inline in the question every time it fires.
    # Deliberately NOT including "Inactive configs" here (moved to its own §1, 2026-07-30, per the
    # researcher's own read: "the section 0 Finding for researcher action should only include items
    # that need my decision. The list of soft deleted items does not belong there" — a deactivated
    # row is, by definition, an already-made decision recorded for the audit trail, not a live ask.
    S = [
        "_Computed fresh on every regenerate — the full detail behind `configmaint.validate`'s "
        "escalation, which references this section by path rather than repeating it. Not errors "
        "— advisory. See GOVERNANCE.md §5B._ Items are numbered (running count across every "
        "category below) so any one item can be referenced by number, e.g. \"item 7\" — the "
        "numbering is a snapshot of THIS regenerate, not a stable ID across runs. Historical/"
        "already-decided records (inactive configs) are §1, not here — everything below is "
        "something that actually needs your judgement.",
        "",
    ]
    n = 0
    for title, note, items in finding_groups:
        S.append(f"**{title}** ({len(items)}) — {note}:")
        if items:
            for i in items:
                n += 1
                S.append(f"{n}. {i}")
        else:
            S.append("_(none)_")
        S.append("")
    sections["findings"] = S

    sections["inactive_configs"] = _inactive_configs(q)

    sections["utilities"] = _utilities_table(q)

    sections["connection"] = _table(["key", "value"], [[r["key"], r["value"]] for r in q(
        "SELECT key, value FROM cfg_connection ORDER BY key")])

    sections["settings"] = [
        "_Every setting must have a module (enum.config_module) — configmaint.propose "
        "enforces this on every new row; see GOVERNANCE.md §5A._",
    ] + _table(["module", "key", "value", "use"], [
        [r["module"], r["key"], r["value"], r["use"]] for r in q(
            'SELECT module, key, value, "use" AS "use" FROM cfg_setting ORDER BY module, key')])

    sections["apis"] = _table(["name", "route", "input", "returns"], [
        [r["name"], r["route"], r["input"], r["returns"]] for r in q(
            "SELECT name, route, input, returns FROM cfg_api ORDER BY name")])

    S = []
    for wp in q("SELECT name, ps_script, runs_over FROM cfg_work_package ORDER BY name"):
        S.append(f"**{wp['name']}** — runs over `{wp['runs_over']}` · script `{wp['ps_script']}`")
        S += _table(["#", "step", "handler", "scope", "does"], [
            [r["ordinal"], r["step"], r["handler"], r["scope"], r["does"]] for r in q(
                "SELECT ordinal, step, handler, scope, does FROM cfg_step "
                "WHERE work_package=? ORDER BY ordinal", (wp["name"],))])
        S.append("")
    sections["work_packages"] = S

    all_fail = [dict(r) for r in q(
        "SELECT step, condition, path, message FROM cfg_on_fail ORDER BY step, condition")]
    escalates = [r for r in all_fail if r["path"] == "pause-continue"]
    non_escalating = [r for r in all_fail if r["path"] != "pause-continue"]
    S = [
        f"**{len(escalates)} of {len(all_fail)} conditions ESCALATE** (pause-continue — the "
        f"researcher is asked); the rest either stop the run outright (report-stop) or continue "
        f"with a logged warning (report-continue). Per the researcher's 2026-07-21 rule: any "
        f"finding that needs a judgement call must be in the first group, not silently in the "
        f"second or third.",
        "",
        "### 5a. Escalates (pause-continue) — the researcher is asked, every time",
    ]
    S += _table(["step", "condition", "message"], [
        [r["step"], r["condition"], r["message"]] for r in escalates]) if escalates else ["_(none)_"]
    S += ["", "### 5b. Does not escalate — report-stop (hard fail) or report-continue (logged, no ask)"]
    S += _table(["step", "condition", "path", "message"], [
        [r["step"], r["condition"], r["path"], r["message"]] for r in non_escalating])
    sections["on_fail"] = S

    sections["write_grants"] = _table(["writer", "tables"], [
        [w, ", ".join(t)] for w, t in _grants(q).items()])

    sections["status_flow"] = _table(["entity", "order", "status", "set_by"], [
        [r["entity"], r["ordinal"], r["status"], r["set_by"]] for r in q(
            "SELECT entity, ordinal, status, set_by FROM cfg_status_flow "
            "ORDER BY entity, ordinal")])

    uniq = {}
    for r in q("SELECT table_name, col FROM cfg_unique ORDER BY table_name, ordinal"):
        uniq.setdefault(r["table_name"], []).append(r["col"])
    S = []
    for t in q('SELECT name, grain, "use" AS "use" FROM cfg_table ORDER BY rowid'):
        S.append(f"### {t['name']}")
        S.append(f"_{t['grain'] or ''}_ — {t['use'] or ''}")
        if t["name"] in uniq:
            S.append(f"dedup key: `{', '.join(uniq[t['name']])}`")
        S += _table(["column", "type", "pk", "notnull", "unique", "fk", "use", "source/filled_by"], [
            [c["name"], c["type"],
             "✓" if c["is_pk"] else "", "✓" if c["notnull"] else "", "✓" if c["is_unique"] else "",
             c["fk"] or "", c["use"] or "", c["source"] or c["filled_by"] or ""]
            for c in q('SELECT name, "type" AS "type", is_pk, "notnull" AS "notnull", is_unique, '
                       'fk, "use" AS "use", source, filled_by FROM cfg_column '
                       "WHERE table_name=? ORDER BY ordinal", (t["name"],))])
        S.append("")
    sections["schema"] = S

    en = {}
    for r in q("SELECT name, value FROM cfg_enum ORDER BY name, ordinal"):
        en.setdefault(r["name"], []).append(r["value"])
    sections["enums"] = _table(["enum", "values"], [[k, ", ".join(v)] for k, v in en.items()])

    bo = q("SELECT book, ordinal FROM cfg_book_order ORDER BY ordinal")
    sections["book_order"] = (
        [f"{len(bo)} books, canonical order — first `{bo[0]['book']}`, last `{bo[-1]['book']}`."]
        if bo else [])

    sections["change_log"] = _table(["#", "loaded_at", "config_version", "seed_hash", "validated"], [
        [r["id"], r["loaded_at"], r["config_version"], r["seed_hash"], r["validated"]] for r in q(
            "SELECT id, loaded_at, config_version, seed_hash, validated "
            "FROM cfg_change_log ORDER BY id")])

    sections["report_governance"] = _report_governance(q)

    L = reportkit.render_scaffold(conn, STEP, sections, intro=intro)
    reportkit.write_csv_pairing(conn, STEP, out_path.parent / "export")
    out_path = reportkit.write_report(conn, STEP, out_path, L)
    conn.close()
    return out_path


def _report_governance(q) -> list[str]:
    """Per PLAN-reports-config-governance-v1-20260722.md §10.1 — the answer to 'when I look at a
    report, am I seeing everything related to it': one block per report, every config item that
    governs it, joined together here so nothing needs to be found by cross-referencing 5 tables by
    hand. Generated fresh every run — can't drift from the live rows the way a hand-written summary
    could."""
    L = [
        "_One block per registered report — everything that governs it, joined from `cfg_report`, "
        "`cfg_report_section`, `cfg_report_csv_table`, `cfg_work_package`, and `cfg_on_fail`. The "
        "ownership ledger (which config item governs what) is in GOVERNANCE.md._", "",
    ]
    for rep in q("SELECT step, title, show_toc, footer_text, output_kind, naming_scheme, "
                "archive_dir FROM cfg_report ORDER BY step"):
        step_row = q("SELECT work_package FROM cfg_step WHERE step=?", (rep["step"],))
        wp_name = step_row[0]["work_package"] if step_row else None
        wp = q("SELECT ps_script, chained, complete_message, next_step_hint, paused_message "
              "FROM cfg_work_package WHERE name=?", (wp_name,)) if wp_name else []
        L.append(f"### `{rep['step']}`")
        L.append(f"**{rep['title']}** — output `{rep['output_kind']}` · naming "
                 f"`{rep['naming_scheme']}` · archived to `{rep['archive_dir']}/` · ToC "
                 f"{'on' if rep['show_toc'] else 'off'}"
                 + (f" · footer: {rep['footer_text']}" if rep["footer_text"] else ""))
        if wp:
            w = wp[0]
            L.append(f"work package `{wp_name}` → `{w['ps_script']}` (chained={w['chained']})")
            if w["complete_message"]:
                L.append(f"- on completion: _{w['complete_message']}_")
            if w["next_step_hint"]:
                L.append(f"- next-step hint: _{w['next_step_hint']}_")
            if w["paused_message"]:
                L.append(f"- paused override: _{w['paused_message']}_")
        L.append("")
        L += _table(["#", "section", "heading", "toc label", "in ToC"], [
            [r["ordinal"], r["section_key"], r["heading"], r["toc_label"] or "",
             "✓" if r["include"] else ""]
            for r in q("SELECT ordinal, section_key, heading, toc_label, include FROM "
                      "cfg_report_section WHERE step=? ORDER BY ordinal", (rep["step"],))])
        csv_tables = q("SELECT table_name, join_note FROM cfg_report_csv_table WHERE step=? "
                      "ORDER BY table_name", (rep["step"],))
        if csv_tables:
            L.append("CSV pairing: " + "; ".join(
                f"`{r['table_name']}`" + (f" ({r['join_note']})" if r["join_note"] else "")
                for r in csv_tables))
        on_fail = q("SELECT condition, path, route, message FROM cfg_on_fail WHERE step=? "
                   "ORDER BY condition", (rep["step"],))
        if on_fail:
            L.append("")
            L += _table(["condition", "path", "route", "message"], [
                [r["condition"], r["path"], r["route"], r["message"]] for r in on_fail])
        L.append("")
    return L


def _grants(q) -> dict[str, list[str]]:
    g: dict[str, list[str]] = {}
    for r in q("SELECT writer, table_name FROM cfg_write_grant ORDER BY writer, table_name"):
        g.setdefault(r["writer"], []).append(r["table_name"])
    return g


if __name__ == "__main__":
    p = generate()
    print(f"config report written: {p}")
