"""cycleview -- escalation #2637, plan v3 X6 and X7 (outputs/escalation/2637-build-plan-v3-20261126.md): the reading cycle of a collection (or one
subgroup) in one view, and the audit of a run that B:138 requires.

The view: each step of the loop with its state, the ledger rows by step and state, the packages the read commands wrote (by name), and every
refusal and crash kept in read_failure with its rule keys. The audit (the run passes only when all three hold):
  stated         every problem line of every refusal names its rule ([KEY], refusalrules.annotate): a line with no key is a rule the packet did
                 not state
  no crash       no crash of a read or record command in the window
  no other file  every file of the collection in the working folder written in the window is one a package command writes
                 (cfg_setting layer.cycle package_patterns, {c} the collection's slug)
The window starts at `since` (ISO-8601 UTC), or covers all time. Read-only; the handler writes the report (cfg_setting layer.cycle report_name).
"""
from __future__ import annotations

import datetime
import json
import pathlib
import re

from . import layerloop
from . import refusalrules


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def build(conn, cfg, name: str, subgroup: str | None = None, since: str | None = None) -> dict:
    """{lines: the report, verdict: pass or fail, unstated, crashes, other_files}."""
    cyc = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.cycle'").fetchone()[0])
    wd = pathlib.Path(json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.working_dir'").fetchone()[0]))
    prog = layerloop.progress(conn, cfg, name)
    coll, cid = prog["collection"], prog["cid"]
    subs = [g for g in prog["subgroups"] if subgroup is None or g["name"].lower() == subgroup.lower()]
    lines = [f"# Reading cycle -- {coll}" + (f" / {subgroup}" if subgroup else ""), "",
             f"Window: {'since ' + since if since else 'all time'}. Read-only view (Collection-Build.ps1 -Action Cycle; #2637 X6, X7).", "", "## Steps", ""]
    for g in subs:
        lines.append(f"- {g['name']}: " + ", ".join(f"{s} {v}" for s, v in g["steps"].items()) + (" -- complete" if g["complete"] else ""))
    lines.append("- the collection: " + ", ".join(f"{s} {v}" for s, v in prog["collection_steps"].items()))
    gids = [g["id"] for g in subs] or [0]
    q = "SELECT step, state, validated, count(*) FROM collection_layer_item WHERE collection_id=? AND deleted=0"
    args = [cid]
    if subgroup:
        q += f" AND subgroup_id IN ({','.join('?' * len(gids))})"
        args += gids
    lines += ["", "## Ledger", ""] + [f"- {r[0]} {r[1]}{' validated' if r[2] else ''}: {r[3]}" for r in conn.execute(q + " GROUP BY 1, 2, 3 ORDER BY 1, 2", args)]

    c = _slug(coll)
    pats = [re.compile(p.replace("{c}", re.escape(c))) for p in cyc["package_patterns"]]
    t0 = datetime.datetime.fromisoformat(since.replace("Z", "+00:00")).timestamp() if since else 0
    mine = sorted(p for p in wd.glob(f"*{c}*") if p.is_file() and p.stat().st_mtime >= t0
                  and (not subgroup or _slug(subgroup) in p.name or p.name.startswith(("group-", "readbehaviours-"))))
    pk = [p for p in mine if any(x.match(p.name) for x in pats)]
    other = [p for p in mine if p not in pk]
    lines += ["", "## Packages written", ""] + [f"- {p.as_posix()}" for p in pk]

    q = "SELECT created_at, step, kind, subgroup, rule_keys, problems FROM read_failure WHERE collection=?"
    args = [coll]
    if subgroup:
        q += " AND lower(subgroup)=?"
        args.append(subgroup.lower())
    if since:
        q += " AND created_at >= ?"
        args.append(since)
    fails = conn.execute(q + " ORDER BY id", args).fetchall()
    heads = [h.split("{}")[-1].strip() for h in refusalrules.load(conn).get("scan", {}).get("headings", [])]
    unstated, crashes = [], []
    lines += ["", "## Refusals and crashes", ""]
    for at, step, kind, sub, keys, probs in fails:
        lines.append(f"- {at} {step} {kind}" + (f" ({sub})" if sub else "") + f": rules {keys or 'none'}")
        if kind == "crash":
            crashes.append(f"{at} {step}: {(probs or '').splitlines()[0][:200] if probs else ''}")
            continue
        for ln in (probs or "").split("\n"):
            s = ln.strip()
            if s and not s.startswith("[") and not any(s.startswith(h) or s.endswith(h) for h in heads):
                unstated.append(f"{at} {step}: {s[:200]}")
    ok = not unstated and not crashes and not other
    lines += ["", "## Audit (B:138)", "", f"- verdict: {'PASS' if ok else 'FAIL'}",
              f"- refusal lines naming no rule (unstated): {len(unstated)}"] + [f"  - {x}" for x in unstated]
    lines += [f"- crashes: {len(crashes)}"] + [f"  - {x}" for x in crashes]
    lines += [f"- files in the working folder no package command writes: {len(other)}"] + [f"  - {p.as_posix()}" for p in other]
    return {"lines": lines, "verdict": "pass" if ok else "fail", "unstated": unstated, "crashes": crashes, "other_files": [p.as_posix() for p in other]}
