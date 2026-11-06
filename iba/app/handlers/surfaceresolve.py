"""surfaceresolve handlers -- work package `surface-resolve` (#2361, module 4 of 5 of the surface cycle), one step per Surface-Resolve.ps1 action.

Status computes the base of every surface of collection a from the evidence in the tables and says how far the stored bases are from it
(read-only). Run writes the difference (-Check previews): base fields, accepted flags, missing own and Ollama evidence rows, computed terms,
one surface_event per changed term; a second Run with the same evidence changes nothing. Show prints one surface's stored state, the decision
and its evidence rows. No file is read; a missing setting or surface is the routed condition 'refused' and writes nothing.
See lib/surfaceresolve.py for the rule."""
from __future__ import annotations

import json

from ..lib import surfaceresolve as sr
from ..lib import surfacestructure as ss
from .base import Ctx, Outcome, fail, ok


def _lines(pl: dict) -> list[str]:
    c = pl["counts"]
    return ["decided: " + "; ".join(f"{k} {v}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])),
            f"already as decided: {pl['unchanged']}; to change: {len(pl['changes'])}; protected (confirmed or resolved by the researcher): {pl['protected']}"]


def status(ctx: Ctx) -> Outcome:
    try:
        pl = sr.plan(ctx.cfg.conn, ctx.cfg)
    except (sr.ResolveError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    return ok("\n  ".join(_lines(pl)), to_change=len(pl["changes"]), unchanged=pl["unchanged"])


def run(ctx: Ctx) -> Outcome:
    try:
        pl = sr.plan(ctx.cfg.conn, ctx.cfg)
    except (sr.ResolveError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    lines = _lines(pl)
    if str(ctx.params.get("Check", "")).lower() in ("1", "true", "yes"):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_change=len(pl["changes"]))
    conn = ctx.cfg.conn
    done = sr.write(conn, ctx.run_id, pl)
    conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps(done), ctx.run_id))
    conn.commit()
    return ok("\n  ".join(lines) + f"\n  written: {done['terms']} terms, {done['computed']} computed terms, {done['evidence_set']} accepted flags set, "
              f"{done['evidence_added']} evidence rows added", **done)


def show(ctx: Ctx) -> Outcome:
    sf = (ctx.params.get("Surface") or "").strip().lower()
    if not sf:
        return fail("refused", "-Surface is required: the surface text to show")
    conn = ctx.cfg.conn
    row = conn.execute("SELECT t.id, t.form, t.surface_group, t.base_state, t.base_source, b.surface FROM surface_term t "
                       "LEFT JOIN surface_term b ON b.id=t.base_id WHERE t.surface=? AND t.deleted=0", (sf,)).fetchone()
    if row is None:
        return fail("refused", f"{sf!r} is not a live surface")
    try:
        vals, svals, scope_a, terms, recs, ai = sr.load(conn, ctx.cfg)
    except (sr.ResolveError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    t = next((x for x in terms if x["surface"] == sf), None)
    d = sr.decide(t, recs.get(sf), ai.get(t["id"]), vals, scope_a, svals["structure.tested_form"]) if t else None
    rows = conn.execute("SELECT method, evidence, kind, base_word, accepted FROM surface_derivation WHERE term_id=? AND deleted=0 ORDER BY method, evidence",
                        (row[0],)).fetchall()
    lines = [f"{sf}: group {row[2]}, form {row[1]}; stored: {row[3]} base {row[5]} (source {row[4]})",
             f"decided now: {d['state']} base {d['base']} (source {d['source']})" if d else "decided now: not a surface term of the list",
             "evidence rows:"] + [f"  {r[0]} {r[1]} {r[2]} -> {r[3]} (accepted {r[4]})" for r in rows] or ["  none"]
    return ok("\n  ".join(lines), surface=sf)
