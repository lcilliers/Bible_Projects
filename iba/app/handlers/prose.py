"""prose handlers — thin dispatcher adapters over `iba.app.lib.prosestore`.

Registers the DB-canonical prose store's operations as the `prose` work package. The original four
(extract, search, chapter export, chapter import — escalation #784: these tables/columns were fully
catalogued in `cfg_table`/`cfg_column` but had zero live IBA code operating on them) are read-only
against `prose_section`/`prose_section_type`; `prose.import_chapter` generates a patch file but
writes nothing to the database itself (same boundary the standalone script always had — apply via
`scripts/apply_session_patch.py`). A fifth, `prose.flag` (escalation #829 sec12.4, angle a), writes
directly to `wa_data_quality_flags` — the one write this module performs itself, not gated behind a
patch file. Two more, `prose.flag_fix_propose`/`prose.flag_fix_apply` (escalation #890 D5, angle
b), add propose/apply on top of angle a — propose writes a review report only, apply generates a
patch (same read-only/patch-generating boundary as import_chapter, no new DB-write exception).
"""

from __future__ import annotations

from .base import Ctx, Outcome, ok, fail
from ..lib import prosestore


def _truthy(value, default=False) -> bool:
    if value is None:
        return default
    return str(value).strip().lower() in ("1", "true", "yes", "on")


def extract(ctx: Ctx) -> Outcome:
    p = ctx.params
    try:
        result = prosestore.run_extract(
            ctx.cfg,
            include_body=_truthy(p.get("IncludeBody")),
            book=p.get("Book"),
            chapter=int(p["Chapter"]) if p.get("Chapter") else None,
            also_markdown=_truthy(p.get("AlsoMarkdown")),
            also_docx=_truthy(p.get("AlsoDocx")),
            out=p.get("Out"),
        )
    except ValueError as e:
        return fail("bad-params", str(e))
    return ok(
        f"wrote {result['json']} ({result['type_count']} types, {result['section_total']} sections)",
        **result,
    )


def search(ctx: Ctx) -> Outcome:
    p = ctx.params
    if not p.get("Query"):
        return fail("bad-params", "search needs -Query")
    result = prosestore.run_search(
        ctx.cfg, p["Query"], book=p.get("Book"),
        limit=int(p["Limit"]) if p.get("Limit") else None,
        raw_fts=_truthy(p.get("Fts")), out=p.get("Out"),
    )
    return ok(f"wrote {result['path']} (showing {result['shown']} of {result['total']})", **result)


def export_chapter(ctx: Ctx) -> Outcome:
    p = ctx.params
    type_id = int(p["TypeId"]) if p.get("TypeId") else None
    book = p.get("Book")
    chapter = int(p["Chapter"]) if p.get("Chapter") else None
    if type_id is None and book is None:
        return fail("bad-params", "export_chapter needs -TypeId or -Book (+ -Chapter)")
    try:
        result = prosestore.run_export_chapter(ctx.cfg, type_id=type_id, book=book,
                                               chapter=chapter, out=p.get("Out"))
    except ValueError as e:
        return fail("bad-params", str(e))
    return ok(f"exported {result['sections']} section(s) -> {result['path']}", **result)


def import_chapter(ctx: Ctx) -> Outcome:
    p = ctx.params
    if not p.get("Input"):
        return fail("bad-params", "import_chapter needs -Input <edited chapter .md>")
    try:
        result = prosestore.run_import_chapter(
            ctx.cfg, p["Input"], author=p.get("Author", "researcher"), out=p.get("Out"))
    except (ValueError, FileNotFoundError) as e:
        return fail("bad-params", str(e))
    return ok(
        f"generated patch for {result['sections']} section(s) -> {result['path']} "
        f"(review + apply with scripts/apply_session_patch.py)",
        **result,
    )


def flag(ctx: Ctx) -> Outcome:
    p = ctx.params
    try:
        result = prosestore.run_flag(ctx.cfg, p.get("FlagCode"), p.get("Description"))
    except ValueError as e:
        return fail("bad-params", str(e))
    return ok(f"raised flag #{result['id']} ({result['flag_code']})", **result)


def flag_fix_propose(ctx: Ctx) -> Outcome:
    p = ctx.params
    try:
        result = prosestore.run_flag_fix_propose(
            ctx.cfg, p.get("FlagCode"), p.get("Find"), p.get("Replace"), out=p.get("Out"))
    except ValueError as e:
        return fail("bad-params", str(e))
    return ok(f"wrote proposal -> {result['path']} ({result['match_count']} match(es))", **result)


def flag_fix_apply(ctx: Ctx) -> Outcome:
    p = ctx.params
    section_ids_raw = p.get("SectionIds")
    if not p.get("ProposalFile") or not section_ids_raw:
        return fail("bad-params", "flag_fix_apply needs -ProposalFile and -SectionIds")
    try:
        section_ids = [int(x) for x in str(section_ids_raw).split(",") if x.strip()]
    except ValueError:
        return fail("bad-params", f"-SectionIds must be a comma-separated list of ints, got "
                                   f"{section_ids_raw!r}")
    try:
        result = prosestore.run_flag_fix_apply(
            ctx.cfg, p["ProposalFile"], section_ids, p.get("FlagCode"), out=p.get("Out"))
    except (ValueError, FileNotFoundError) as e:
        return fail("bad-params", str(e))
    return ok(
        f"generated patch for {result['sections']} section(s) -> {result['path']} "
        f"(review + apply with scripts/apply_session_patch.py)",
        **result,
    )
