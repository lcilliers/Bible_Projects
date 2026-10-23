"""prose handlers — thin dispatcher adapters over `iba.app.lib.prosestore`, the `prose` work package.
extract, search, chapter export and chapter import are read-only against `prose_section`/
`prose_section_type` (`prose.import_chapter` generates a patch). `prose.flag` writes directly to
`wa_data_quality_flags`. `prose.flag_fix_propose` writes a review report only; `prose.flag_fix_apply`
and `prose.set_status` generate a patch. `prose.apply_patch` applies a reviewed patch (#2212), the
one write to the prose tables.
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
        f"(review, then Prose.ps1 -Step ApplyPatch -PatchFile <it>)",
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
        f"(review, then Prose.ps1 -Step ApplyPatch -PatchFile <it>)",
        **result,
    )


def set_status(ctx: Ctx) -> Outcome:
    p = ctx.params
    section_ids_raw = p.get("SectionIds")
    if not section_ids_raw or not p.get("Status"):
        return fail("bad-params", "set_status needs -SectionIds and -Status")
    try:
        section_ids = [int(x) for x in str(section_ids_raw).split(",") if x.strip()]
    except ValueError:
        return fail("bad-params", f"-SectionIds must be a comma-separated list of ints, got "
                                   f"{section_ids_raw!r}")
    try:
        result = prosestore.run_set_status(
            ctx.cfg, section_ids, p["Status"], author=p.get("Author", "researcher"),
            out=p.get("Out"))
    except ValueError as e:
        return fail("bad-params", str(e))
    return ok(
        f"generated patch for {result['sections']} section(s) -> {result['path']} "
        f"(review, then Prose.ps1 -Step ApplyPatch -PatchFile <it>)",
        **result,
    )


def apply_patch(ctx: Ctx) -> Outcome:
    p = ctx.params
    if not p.get("PatchFile"):
        return fail("bad-params", "apply_patch needs -PatchFile <patch .json>")
    dry_run = _truthy(p.get("DryRun"))
    try:
        result = prosestore.run_apply_patch(ctx.cfg, p["PatchFile"], dry_run=dry_run)
    except (ValueError, FileNotFoundError) as e:
        return fail("bad-params", str(e))
    done = "dry run, nothing written" if dry_run else "applied"
    return ok(
        f"{result['patch_id']}: {result['operations']} operation(s) {done} -> {result['counts']}",
        path=result["path"], patch_id=result["patch_id"], operations=result["operations"],
        dry_run=dry_run, **result["counts"],
    )
