"""handlers/compliance.py -- the session compliance file (escalation #2173 P2), as steps:
compliance.template (write the skeleton for this session, one row per active rule) and
compliance.check_start (parts B and C: every rule restated or marked not engaged, none copied,
the acknowledgement, every rule naming a retired thing named in the conflicts section). The close
check (part D) runs inside session.close (SC6). Read-only except for writing the template file.
"""

from __future__ import annotations

from .base import Ctx, Outcome, ok, fail
from ..lib import compliance, sessionwindow as sw


def _session(ctx: Ctx):
    sid, _, how = sw.identify("Compliance.ps1")
    return sid, how


def template(ctx: Ctx) -> Outcome:
    sid, how = _session(ctx)
    if not sid:
        return fail("no-session", f"cannot identify this session: {how}")
    mode = str(ctx.params.get("Mode", "standard")).strip().lower()
    if mode not in compliance.MODES:
        return fail("no-session", f"unknown mode {mode!r}: one of {compliance.MODES}")
    path, made = compliance.template(ctx.cfg, sid, mode)
    rel = path.relative_to(sw.repo_root()).as_posix()
    return ok(f"{'wrote' if made else 'already present'}: {rel} -- restate every rule, then "
              f"Compliance.ps1 -Action Check -Phase Start", path=rel, created=int(made))


def check_start(ctx: Ctx) -> Outcome:
    sid, how = _session(ctx)
    if not sid:
        return fail("no-session", f"cannot identify this session: {how}")
    path = compliance.find_file(ctx.cfg, sid)
    if path is None:
        return fail("findings-open", "no compliance file for this session -- run "
                                     "Compliance.ps1 -Action Template first", findings=1)
    F = compliance.check_start(ctx.cfg, path)
    rel = path.relative_to(sw.repo_root()).as_posix()
    if not F:
        return ok(f"compliance file passes the start check: {rel}", path=rel, findings=0)
    lines = [f"{len(F)} finding(s) in {rel}:"] + [f"  {f['key']}: {f['reason']}" for f in F[:60]]
    if len(F) > 60:
        lines.append(f"  ... and {len(F) - 60} more")
    return fail("findings-open", "\n".join(lines), path=rel, findings=len(F))
