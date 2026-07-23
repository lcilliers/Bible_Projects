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


def _inactive_configs(q) -> list[str]:
    """Every deactivated config row, escalation #310 — DEACTIVATED, not deleted: excluded from
    configmaint.validate's coherence/orphan/justification checks (see cfgquality.py), but listed
    here in full so nothing goes quietly missing. cfg_candidate_rule is summarised by kind+count
    (individual Strong's codes at real volume would swamp the report, not inform it)."""
    lines: list[str] = []
    total_rows = 0
    total_tables = 0
    for table, expr in _INACTIVE_LABEL.items():
        rows = q(f'SELECT {expr} AS label FROM "{table}" WHERE inactive=1 ORDER BY label')
        if not rows:
            continue
        total_rows += len(rows)
        total_tables += 1
        lines.append(f"- **{table}** ({len(rows)}): " + ", ".join(f"`{r['label']}`" for r in rows))
    cand = q("SELECT kind, COUNT(*) n FROM cfg_candidate_rule WHERE inactive=1 GROUP BY kind "
             "ORDER BY kind")
    if cand:
        total_rows += sum(r["n"] for r in cand)
        total_tables += 1
        lines.append("- **cfg_candidate_rule** (by kind): "
                     + ", ".join(f"{r['kind']}={r['n']}" for r in cand))
    return [f"**Inactive configs** ({total_rows} row(s) across {total_tables} table(s)) — "
            f"deactivated, not deleted; excluded from validation above:"] + (
        lines if lines else ["_(none)_"])


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

    orphans = cfgquality.find_orphan_configs(conn, APP)
    needs_justification = cfgquality.find_settings_needing_justification(conn)
    missing_report_paths = cfgquality.find_missing_report_paths(conn)
    S = [
        "_Computed fresh on every regenerate; also what `configmaint.validate` escalates on "
        "if any are present. Not errors — advisory. See GOVERNANCE.md §5B._",
        "",
        f"**Orphan configs** ({len(orphans)}) — a `cfg_setting`/`cfg_enum` not referenced by "
        f"any code:",
    ]
    S += ["- " + o for o in orphans] if orphans else ["_(none)_"]
    S += ["", f"**Settings needing justification** ({len(needs_justification)}) — module already "
             f"has its own dedicated table:"]
    S += ["- " + n for n in needs_justification] if needs_justification else ["_(none)_"]
    S += ["", f"**Missing report paths** ({len(missing_report_paths)}) — a quality-check step with "
             f"nowhere for its findings to persist (governance.reports_must_persist violation):"]
    S += ["- " + m for m in missing_report_paths] if missing_report_paths else ["_(none)_"]
    S += [""] + _inactive_configs(q)
    sections["findings"] = S

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
    reportkit.write_report(conn, STEP, out_path, L)
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
