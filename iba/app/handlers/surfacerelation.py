"""surfacerelation handlers -- work package `surface-relation` (#2548), one step per Surface-Relation.ps1 action.

The relations between the single-word surfaces of the relation study, linked by an outside source (WordNet 3.0): Load writes the pairs into
surface_relation, Groups the connected groups into surface_network_group, Flag one surface_flag for each surface left with no pair (from a
reviewed list), Validate compares the WordNet same_base pairs and groups with surface_term.base_id (writes a report, nothing to base_id).
Status says how far the stored rows are from what the source gives. -Check previews every writing step. A usage problem (a missing setting,
a list that does not match) is the routed condition 'refused' and writes nothing. See lib/surfacerelation.py for the rule."""
from __future__ import annotations

import json

from ..lib import filingkit
from ..lib import surfacerelation as sr
from .base import Ctx, Outcome, fail, ok


def _check(ctx: Ctx) -> bool:
    return str(ctx.params.get("Check", "")).lower() in ("1", "true", "yes")


def _count(ctx: Ctx, done: dict) -> None:
    ctx.cfg.conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps(done), ctx.run_id))
    ctx.cfg.conn.commit()


def _load_lines(pl: dict) -> list[str]:
    return [f"study surfaces: {len(pl['terms'])}; held by WordNet: {len(pl['in_wn'])}; pairs computed: {len(pl['want'])} ("
            + ", ".join(f"{k} {v}" for k, v in sorted(pl["counts"].items(), key=lambda kv: -kv[1])) + ")",
            f"stored live: {len(pl['have'])}; to add: {len(pl['add'])}; to change: {len(pl['readd'])}; to flip (no longer linked): {len(pl['flip']) - len(pl['readd'])}"]


def _group_lines(pl: dict) -> list[str]:
    return [f"surfaces {len(pl['surf'])}; live pairs read {pl['relations']} ({pl['outside']} reach a surface outside the study scope and are left out)",
            f"groups {pl['groups']}: largest sizes {pl['sizes']}; kinds: " + ", ".join(f"{k} {v}" for k, v in sorted(pl["counts"].items())),
            "stored grouping: " + ("the same as computed" if pl["same"] else f"differs ({len(pl['have'])} stored rows)")]


def status(ctx: Ctx) -> Outcome:
    try:
        pl = sr.plan_load(ctx.cfg.conn, ctx.cfg)
    except sr.RelationError as exc:
        return fail("refused", str(exc))
    lines = _load_lines(pl)
    live = ctx.cfg.conn.execute("SELECT count(*) FROM surface_relation WHERE deleted=0").fetchone()[0]
    grp = ctx.cfg.conn.execute("SELECT kind, count(*) FROM surface_network_group WHERE deleted=0 GROUP BY kind").fetchall()
    flags = ctx.cfg.conn.execute("SELECT status, count(*) FROM surface_flag WHERE deleted=0 AND kind='wordnet_no_pair' GROUP BY status").fetchall()
    lines += [f"surface_relation live rows: {live}", "surface_network_group live rows by kind: " + (", ".join(f"{k} {n}" for k, n in grp) or "none"),
              "wordnet_no_pair flags: " + (", ".join(f"{k} {n}" for k, n in flags) or "none")]
    return ok("\n  ".join(lines), to_add=len(pl["add"]), to_change=len(pl["readd"]), live=live)


def load(ctx: Ctx) -> Outcome:
    try:
        pl = sr.plan_load(ctx.cfg.conn, ctx.cfg)
    except sr.RelationError as exc:
        return fail("refused", str(exc))
    lines = _load_lines(pl)
    if _check(ctx):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_add=len(pl["add"]))
    done = sr.write_load(ctx.cfg.conn, ctx.run_id, pl)
    _count(ctx, done)
    return ok("\n  ".join(lines) + f"\n  written: {done['added']} added, {done['changed']} changed, {done['flipped']} flipped to deleted", **done)


def groups(ctx: Ctx) -> Outcome:
    try:
        pl = sr.plan_groups(ctx.cfg.conn, ctx.cfg)
    except sr.RelationError as exc:
        return fail("refused", str(exc))
    lines = _group_lines(pl)
    if _check(ctx):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), groups=pl["groups"])
    done = sr.write_groups(ctx.cfg.conn, ctx.run_id, pl)
    _count(ctx, done)
    return ok("\n  ".join(lines) + f"\n  written: {done['inserted']} rows, {done['flipped']} earlier rows flipped to deleted", **done)


def flag(ctx: Ctx) -> Outcome:
    f = (ctx.params.get("File") or "").strip()
    if not f:
        return fail("refused", "-File is required: the reviewed list of the surfaces with no pair (the workbook, sheet review)")
    try:
        esc = int(ctx.params.get("Escalation") or 2545)
        pl = sr.plan_flags(ctx.cfg.conn, ctx.cfg, f)
    except (sr.RelationError, ValueError) as exc:
        return fail("refused", str(exc))
    lines = [f"reviewed list: {pl['total']} surfaces; flags already held: {pl['already']}; to write: {len(pl['todo'])}",
             "classes: " + "; ".join(f"{k} {v}" for k, v in sorted(pl["classes"].items()))]
    if _check(ctx):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_write=len(pl["todo"]))
    done = sr.write_flags(ctx.cfg.conn, ctx.run_id, pl, esc)
    _count(ctx, done)
    return ok("\n  ".join(lines) + f"\n  written: {done['flags']} flags (escalation #{esc})", **done)


def validate(ctx: Ctx) -> Outcome:
    """WordNet same_base pairs and groups against surface_term.base_id; writes the report, nothing to base_id."""
    try:
        v = sr.validate(ctx.cfg.conn, ctx.cfg)
        st = sr.read_settings(ctx.cfg)
    except sr.RelationError as exc:
        return fail("refused", str(exc))
    s, base = v["surf"], v["base"]
    nm = lambda i: s.get(i) or ctx.cfg.conn.execute("SELECT surface FROM surface_term WHERE id=?", (i,)).fetchone()[0]  # noqa: E731
    sb_total = v["same_base_agree"] + len(v["same_base_disagree"])
    out = ["# Surface relations: WordNet against the study bases (#2548)", "",
           "WordNet is an outside source and modern English: a disagreement is a case to read, not a correction. Nothing is written to `surface_term.base_id`.", "",
           f"- WordNet `same_base` pairs: {sb_total}; the two surfaces have the same `base_id`: {v['same_base_agree']}; they have different bases: {len(v['same_base_disagree'])}",
           f"- Study base groups (a `base_id` shared by two or more surfaces of the study): {v['base_groups']}; all members inside one WordNet group: {v['base_inside']}; "
           f"split across WordNet groups or with a no-pair member: {len(v['base_split'])}", "",
           "## same_base pairs whose study bases differ", ""]
    out += [f"- {nm(a)} (base {nm(base[a]) if base.get(a) else 'none'}) / {nm(b)} (base {nm(base[b]) if base.get(b) else 'none'})" for a, b in v["same_base_disagree"]] or ["- none"]
    out += ["", "## Study base groups not inside one WordNet group", ""]
    out += [f"- base {nm(b)}: {', '.join(nm(i) for i in ms)}; WordNet groups {gs}" + (f"; no pair: {', '.join(nm(i) for i in np_)}" if np_ else "")
            for b, ms, gs, np_ in v["base_split"]] or ["- none"]
    st["exports"].mkdir(parents=True, exist_ok=True)
    path = filingkit.versioned_path(ctx.cfg, "surface-relation-validation", out_dir=st["exports"], ext="md")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    rel = path.relative_to(sr.ROOT).as_posix()
    return ok(f"same_base pairs {sb_total}: agree {v['same_base_agree']}, differ {len(v['same_base_disagree'])}; study base groups {v['base_groups']}: "
              f"inside one WordNet group {v['base_inside']}, not {len(v['base_split'])}\n  report: {rel}",
              same_base=sb_total, agree=v["same_base_agree"], base_groups=v["base_groups"], inside=v["base_inside"])
