"""surfacehygiene -- the working-file and junk rules of the surface cycle, checked (escalation #2361, stage 6).

The researcher asked for specific rules in config for working-file management. They are cfg_setting rows (module surfaces):
  surfaces.working_files_root / exports_root / discarded_root   the three folders under _analytics/surfaces; every analytic file of the cycle lives in one
  surfaces.junk_rules                                           regular expressions (empty, no letter, punctuation inside) a surface must not match
find_surface_hygiene() reports, as an advisory finding of configmaint.validate and of the config report:
  1. a live surface_term (origin surface) that matches a junk rule: an error of the past that was not marked deleted;
  2. a file under _analytics/surfaces that is in none of the three folders (a stray analytic file: move it into one, or into discarded, and register it).
It reads settings through Cfg and the tables; it reads no working file's content.
"""
from __future__ import annotations

import pathlib
import re

ROOT_KEYS = ["surfaces.working_files_root", "surfaces.exports_root", "surfaces.discarded_root"]


def find_surface_hygiene(cfg, project_root: pathlib.Path) -> list[str]:
    out: list[str] = []
    rules = cfg.setting("surfaces.junk_rules")
    roots = [cfg.setting(k) for k in ROOT_KEYS]
    if not isinstance(rules, dict) or not all(roots):
        return ["surfaces.junk_rules or one of surfaces.working_files_root, exports_root, discarded_root is missing"]
    pats = {name: re.compile(rx) for name, rx in rules.items()}
    for sid, surface in cfg.conn.execute("SELECT id, surface FROM surface_term WHERE deleted=0 AND origin='surface'"):
        hit = [n for n, p in pats.items() if p.search(surface)]
        if hit:
            out.append(f"surface_term {sid} {surface!r} matches the junk rule(s) {hit} and is not marked deleted")
    base = project_root / "_analytics" / "surfaces"
    if base.is_dir():
        allowed = [(project_root / r).resolve() for r in roots]
        for f in sorted(base.rglob("*")):
            if f.is_file() and not any(a == f.resolve() or a in f.resolve().parents for a in allowed):
                out.append(f"{f.relative_to(project_root).as_posix()} is under _analytics/surfaces but in none of the three folders {roots}")
    return out
