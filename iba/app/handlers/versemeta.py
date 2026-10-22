"""handlers/versemeta.py -- the run.py handler for work package verse-meta (VerseMeta.ps1, #1661;
through run.py since #2207): verse_meta.set_status. The logic is in lib/versemeta.py; this checks
the write grant and turns its per-reference report into an Outcome. A bad status or an unknown
reference is a usage outcome (cfg_on_fail report-continue), not an escalation.
"""

from __future__ import annotations

from .base import Ctx, Outcome, ok, fail
from ..lib import versemeta

STEP = "verse_meta.set_status"


def set_status(ctx: Ctx) -> Outcome:
    if "verse_meta" not in ctx.cfg.may_write(STEP):
        raise PermissionError(f"write-grant violation: {STEP!r} may not write 'verse_meta' "
                              f"(cfg_write_grant)")
    refs = str(ctx.params.get("References", "")).split(",")
    status = str(ctx.params.get("Status", "")).strip()
    try:
        r = versemeta.run_set_status(ctx.cfg, refs, status)
    except ValueError as exc:
        return fail("bad-parameter", str(exc))
    msg = (f"status={status!r}: {len(r['updated'])} updated, {len(r['unchanged'])} already set, "
           f"{len(r['not_found'])} not found")
    counts = {"updated": ", ".join(r["updated"]), "already_set": ", ".join(r["unchanged"]),
              "not_found": ", ".join(r["not_found"])}
    if r["not_found"]:
        return fail("not-found", msg, **counts)
    return ok(msg, **counts)
