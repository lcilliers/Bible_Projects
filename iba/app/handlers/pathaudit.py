"""pathaudit handler — thin dispatcher adapter over lib/pathaudit.py. One step (Scan), matching
the manifest.rebuild shape: a full project-wide pass, persisted report, no per-row editing (unlike
folder_purpose — a finding here isn't a row to hand-classify, it's a code fix or a considered
"no, this one's fine")."""

from __future__ import annotations

import pathlib

from .base import Ctx, Outcome, ok
from ..lib import pathaudit as pathaudit_mod
from ..lib import reportkit


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return L


def path_audit_scan(ctx: Ctx) -> Outcome:
    result = pathaudit_mod.scan(ctx.cfg)
    findings = result["findings"]
    path = pathlib.Path(ctx.cfg.required_setting("pathaudit.report_path"))
    rows = [[f["file"], f["line"], f["literal"], "yes" if f["registered"] else "NO"]
           for f in findings]
    sections = {
        "summary": [f"- **{result['scanned']}** script(s) scanned (inactive-marked scripts "
                   f"excluded)", f"- **{len(findings)}** hardcoded location literal(s) found in "
                   f"**{result['flagged_files']}** file(s)"],
        "findings": (_tbl(["file", "line", "literal", "cfg_utility registered"], rows) if rows
                    else ["None — every location-shaped string literal found either matches no "
                         "live top-level folder, or sits alongside a live cfg accessor."]),
    }
    L = reportkit.render_scaffold(ctx.cfg.conn, "pathaudit.scan", sections,
                                  intro=["> Project-wide scan for hardcoded folder/file-path "
                                        "string literals not backed by a live cfg accessor — "
                                        "ADVISORY, see lib/pathaudit.py's own docstring for method "
                                        "and honest limits. Escalation #971/#976."])
    out = reportkit.write_report(ctx.cfg.conn, "pathaudit.scan", path, L)
    return ok(f"{result['scanned']} scripts scanned, {len(findings)} finding(s) in "
             f"{result['flagged_files']} file(s) — wrote {out}", path=str(out),
             scanned=result["scanned"], findings=len(findings),
             flagged_files=result["flagged_files"])
