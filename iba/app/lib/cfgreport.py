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

APP = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = APP / "db" / "iba.db"
OUT_PATH = APP / "config" / "CONFIG-REPORT.md"


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


def generate(db_path: pathlib.Path = DB_PATH, out_path: pathlib.Path = OUT_PATH) -> pathlib.Path:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()
    meta = {r["key"]: r["value"] for r in q("SELECT key, value FROM cfg_meta")}
    latest = q("SELECT * FROM cfg_change_log ORDER BY id DESC LIMIT 1")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    L: list[str] = []
    L.append("# IBA app — configuration report")
    L.append("")
    L.append("> **Generated snapshot of the live config store** (`iba/app/db/iba.db`, tables "
             "`cfg_*`). Auto-produced after every accepted config load; do not hand-edit — edit "
             "the JSON seeds and reload. Overwritten in place on each change.")
    L.append("")
    L += _table(["field", "value"], [
        ["database", meta.get("database")],
        ["config_version", meta.get("config_version")],
        ["generated_at", now],
        ["current_seed_hash", latest[0]["seed_hash"] if latest else "(no load logged)"],
    ])
    L.append("")

    L.append("## 1. Connection (STEP)")
    L += _table(["key", "value"], [[r["key"], r["value"]] for r in q(
        "SELECT key, value FROM cfg_connection ORDER BY key")])
    L.append("")

    L.append("## 2. Settings — every rule / threshold")
    L += _table(["key", "value", "use"], [[r["key"], r["value"], r["use"]] for r in q(
        'SELECT key, value, "use" AS "use" FROM cfg_setting ORDER BY key')])
    L.append("")

    L.append("## 3. STEP apis")
    L += _table(["name", "route", "input", "returns"], [
        [r["name"], r["route"], r["input"], r["returns"]] for r in q(
            "SELECT name, route, input, returns FROM cfg_api ORDER BY name")])
    L.append("")

    L.append("## 4. Work packages & steps (the sequence)")
    for wp in q("SELECT name, ps_script, runs_over FROM cfg_work_package ORDER BY name"):
        L.append(f"**{wp['name']}** — runs over `{wp['runs_over']}` · script `{wp['ps_script']}`")
        L += _table(["#", "step", "handler", "scope", "does"], [
            [r["ordinal"], r["step"], r["handler"], r["scope"], r["does"]] for r in q(
                "SELECT ordinal, step, handler, scope, does FROM cfg_step "
                "WHERE work_package=? ORDER BY ordinal", (wp["name"],))])
        L.append("")

    L.append("## 5. on_fail — condition -> path (the fork rules)")
    L += _table(["step", "condition", "path", "message"], [
        [r["step"], r["condition"], r["path"], r["message"]] for r in q(
            "SELECT step, condition, path, message FROM cfg_on_fail ORDER BY step, condition")])
    L.append("")

    L.append("## 6. Write grants — who may write what")
    L += _table(["writer", "tables"], [
        [w, ", ".join(t)] for w, t in _grants(q).items()])
    L.append("")

    L.append("## 7. Status flow")
    L += _table(["entity", "order", "status", "set_by"], [
        [r["entity"], r["ordinal"], r["status"], r["set_by"]] for r in q(
            "SELECT entity, ordinal, status, set_by FROM cfg_status_flow "
            "ORDER BY entity, ordinal")])
    L.append("")

    L.append("## 8. Schema — data tables built from config")
    uniq = {}
    for r in q("SELECT table_name, col FROM cfg_unique ORDER BY table_name, ordinal"):
        uniq.setdefault(r["table_name"], []).append(r["col"])
    for t in q('SELECT name, grain, "use" AS "use" FROM cfg_table ORDER BY rowid'):
        L.append(f"### {t['name']}")
        L.append(f"_{t['grain'] or ''}_ — {t['use'] or ''}")
        if t["name"] in uniq:
            L.append(f"dedup key: `{', '.join(uniq[t['name']])}`")
        L += _table(["column", "type", "pk", "notnull", "unique", "fk", "use", "source/filled_by"], [
            [c["name"], c["type"],
             "✓" if c["is_pk"] else "", "✓" if c["notnull"] else "", "✓" if c["is_unique"] else "",
             c["fk"] or "", c["use"] or "", c["source"] or c["filled_by"] or ""]
            for c in q('SELECT name, "type" AS "type", is_pk, "notnull" AS "notnull", is_unique, '
                       'fk, "use" AS "use", source, filled_by FROM cfg_column '
                       "WHERE table_name=? ORDER BY ordinal", (t["name"],))])
        L.append("")

    L.append("## 9. Enums")
    en = {}
    for r in q("SELECT name, value FROM cfg_enum ORDER BY name, ordinal"):
        en.setdefault(r["name"], []).append(r["value"])
    L += _table(["enum", "values"], [[k, ", ".join(v)] for k, v in en.items()])
    L.append("")

    L.append("## 10. Book order")
    bo = q("SELECT book, ordinal FROM cfg_book_order ORDER BY ordinal")
    if bo:
        L.append(f"{len(bo)} books, canonical order — first `{bo[0]['book']}`, last `{bo[-1]['book']}`.")
    L.append("")

    L.append("## 11. Change-log — every accepted load (audit)")
    L += _table(["#", "loaded_at", "config_version", "seed_hash", "validated"], [
        [r["id"], r["loaded_at"], r["config_version"], r["seed_hash"], r["validated"]] for r in q(
            "SELECT id, loaded_at, config_version, seed_hash, validated "
            "FROM cfg_change_log ORDER BY id")])
    L.append("")

    conn.close()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(L) + "\n", encoding="utf-8")
    return out_path


def _grants(q) -> dict[str, list[str]]:
    g: dict[str, list[str]] = {}
    for r in q("SELECT writer, table_name FROM cfg_write_grant ORDER BY writer, table_name"):
        g.setdefault(r["writer"], []).append(r["table_name"])
    return g


if __name__ == "__main__":
    p = generate()
    print(f"config report written: {p}")
