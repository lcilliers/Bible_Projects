"""cfgcheck.py — the config-maintenance / validation utility for the app config.

The framework's discipline (from iba/config's own hard-won lesson): config is not
loaded until it is validated. A hand-edit that is incoherent — a may_source pointing at
a table that does not exist, an on_fail path that is not a real path, a handler that does
not resolve — must be REFUSED, not loaded and run.

cfgload.py calls check() on the assembled seeds BEFORE writing them to the DB. If any
check fails, nothing is written and the load is rejected. This is the app's equivalent
of cfg_apply's validate-before-write.

Read-only over the seed dicts. Returns (ok, errors). No side effects.
"""

from __future__ import annotations

import importlib
import re


def check(schema: dict, step: dict, run: dict, rules: dict, report: dict) -> tuple[bool, list[str]]:
    e: list[str] = []
    tables = set(schema["tables"])
    columns = {t: set(c) for t, c in ((t, ts["columns"]) for t, ts in schema["tables"].items())}
    enums = schema.get("enums", {})

    # ── schema integrity ──
    for t, ts in schema["tables"].items():
        pk = [c for c, s in ts["columns"].items() if s.get("pk")]
        if len(pk) > 1:
            e.append(f"schema: {t} has {len(pk)} primary keys")
        for c, s in ts["columns"].items():
            if "fk" in s:
                rt, rc = s["fk"].split(".")
                if rt not in tables:
                    e.append(f"schema: {t}.{c} FK -> unknown table {rt!r}")
                elif rc not in columns[rt]:
                    e.append(f"schema: {t}.{c} FK -> unknown column {rt}.{rc}")
            src = s.get("source")
            # a source may name an api (call1_meanings.*) or a parse/derived/run marker
            if src and "." in src and src.split(".")[0] in step.get("apis", {}):
                pass  # named api — fine
        for u in ts.get("unique", []):
            if u not in ts["columns"]:
                e.append(f"schema: {t} unique names unknown column {u!r}")

    # ── step / may_source: every sourced table must exist ──
    for api, spec in step["apis"].items():
        if "{version}" not in spec["route"]:
            e.append(f"step: api {api} route has no {{version}} placeholder")
        for tbl in spec.get("may_source", []):
            if tbl not in tables:
                e.append(f"step: api {api} may_source unknown table {tbl!r}")

    # ── write grants: every granted table must exist ──
    for writer, tbls in rules.get("write_grants", {}).items():
        if writer.startswith("_"):
            continue
        for tbl in tbls:
            if tbl not in tables:
                e.append(f"rules: write_grant {writer!r} -> unknown table {tbl!r}")

    # ── run: every step's handler must resolve; scope non-empty ──
    for wp, spec in run["work_packages"].items():
        for s in spec["sequence"]:
            h = s.get("handler", "")
            if ":" not in h:
                e.append(f"run: {wp}/{s['step']} handler {h!r} is not module:function")
                continue
            mod, fn = h.split(":")
            try:
                if not hasattr(importlib.import_module(mod), fn):
                    e.append(f"run: {wp}/{s['step']} handler {h!r} — function not found")
            except Exception as exc:
                e.append(f"run: {wp}/{s['step']} handler {h!r} — import failed: {exc}")

    # ── rules: on_fail paths and steps must be valid ──
    valid_paths = set(enums.get("on_fail", []))
    known_steps = {s["step"] for wp in run["work_packages"].values() for s in wp["sequence"]}
    for r in rules["on_fail"]:
        if r["path"] not in valid_paths:
            e.append(f"rules: on_fail path {r['path']!r} not in enum.on_fail {sorted(valid_paths)}")
        if r["step"] not in known_steps:
            e.append(f"rules: on_fail step {r['step']!r} is not a step in any work package")
    # status flow targets must be in enum.word_status
    valid_status = set(enums.get("word_status", []))
    for entity, flow in rules["status_flow"].items():
        for f in flow:
            if entity == "word" and f["to"] not in valid_status:
                e.append(f"rules: status {f['to']!r} not in enum.word_status {sorted(valid_status)}")

    # ── settings: a regex setting must compile ──
    for k, s in rules["settings"].items():
        if "pattern" in k:
            try:
                re.compile(s["value"])
            except re.error as exc:
                e.append(f"rules: setting {k} is not a valid regex: {exc}")

    # ── report: fields it names must exist on their tables ──
    span_cols = columns.get("span", set()) | {"sense"}          # 'sense' is a derived render field
    strong_cols = columns.get("strong", set()) | columns.get("strong_sense", set()) | {"verses"}
    for f in report["settings"].get("report.span_fields", {}).get("value", []):
        if f not in span_cols:
            e.append(f"report: span_fields names {f!r} which is not a span column")
    for f in report["settings"].get("report.strong_fields", {}).get("value", []):
        if f not in strong_cols:
            e.append(f"report: strong_fields names {f!r} which is not a strong/sense field")

    return (not e), e


if __name__ == "__main__":
    import json
    import pathlib
    import sys
    C = pathlib.Path(__file__).resolve().parent.parent / "config"
    load = lambda n: json.loads((C / n).read_text(encoding="utf-8"))
    ok, errs = check(load("schema.json"), load("step.json"), load("run.json"),
                     load("rules.json"), load("report.json"))
    if ok:
        print("config VALID — coherent, safe to load")
    else:
        print(f"config INVALID — {len(errs)} error(s):")
        for x in errs:
            print(f"  {x}")
    sys.exit(0 if ok else 1)
