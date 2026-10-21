"""narrativeregister handlers -- work package `narrative-register` (#2110).

One handler per Narrative-Register.ps1 action, dispatched through run.py (cfg_behaviour_rule 43).
The logic is in lib/narrativeregister.py; a handler only checks the caller, opens the step's write
grants and turns a lib Refused into the routed condition 'refused' (cfg_on_fail: report-continue,
not recorded as an escalation). Write actions need -By Claude|Researcher (no silent default --
the same rule as Escalation.ps1 -AnsweredBy)."""
from __future__ import annotations

import pathlib

from ..lib import narrativeregister as nr
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok


def _who(ctx: Ctx) -> str:
    who = ctx.params.get("By")
    if who not in ("Claude", "Researcher"):
        raise nr.Refused("-By Claude|Researcher is required for a write action (who made the change)")
    return who


def _write(ctx: Ctx, fn) -> Outcome:
    """A write action, then the published files regenerated (spec sec5: 'The register file is the
    published copy, regenerated from the database after each change')."""
    try:
        w = nr.Writer(ctx.cfg.conn, ctx.step_id, _who(ctx))
        message = fn(ctx.cfg, w, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    if w.unresolved:                     # an unresolved reference is an error (#2134)
        eid = nr.raise_unresolved(ctx.cfg, ctx.db, w)
        message += "".join(f"\n  unresolved: {u}" for u in w.unresolved)
        message += f"\n  escalation #{eid} raised for {len(w.unresolved)} unresolved reference(s)"
    paths = nr.export(ctx.cfg)
    return ok(f"{message}\n  published: {', '.join(p.name for p in paths)}")


def _report(ctx: Ctx, fn, stem: str) -> Outcome:
    try:
        lines, console = fn(ctx.cfg, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    out_dir = pathlib.Path(ctx.cfg.required_setting("narrative.register_report_dir"))
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, out_dir / f"{stem}.md", lines)
    return ok("\n  ".join([f"-> {out}"] + console), path=str(out))


def add_claim(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.add_claim)


def edit(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit)


def tell(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.tell)


def untell(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.untell)


def withdraw(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.withdraw)


def edit_note(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_note)


def add_chapter(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.add_chapter)


def edit_chapter(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_chapter)


def edit_section(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_section)


def record(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.record)


def find(ctx: Ctx) -> Outcome:
    return _report(ctx, nr.find, "narrative-register-find")


def history(ctx: Ctx) -> Outcome:
    claim = (ctx.params.get("Claim") or "claim").replace(" ", "")
    return _report(ctx, nr.history, f"{claim}-narrative-claim-history")


def check(ctx: Ctx) -> Outcome:
    return _report(ctx, nr.check, "narrative-register-check")


def export(ctx: Ctx) -> Outcome:
    paths = nr.export(ctx.cfg)
    return ok("\n  ".join(["wrote"] + [str(p) for p in paths]), files=len(paths))


def quote_check(ctx: Ctx) -> Outcome:
    """`Narrative-Register.ps1 -Action QuoteCheck -File <chapter.md> [-Against <previous.md>]` (#2173):
    every quotation in the file (or only in the lines it added against -Against) must be found in the
    ESV text (lib/quotecheck.py). Read-only."""
    import pathlib
    from ..lib import quotecheck
    f = ctx.params.get("File")
    if not f:
        return fail("refused", "QuoteCheck needs -File")
    p = pathlib.Path(f)
    if not p.is_file():
        return fail("refused", f"no such file: {f}")
    against = ctx.params.get("Against")
    old = pathlib.Path(against).read_text(encoding="utf-8") if against else None
    lines = quotecheck.added_lines(old, p.read_text(encoding="utf-8"))
    corpus = quotecheck.Corpus(ctx.db.conn)
    n, bad = quotecheck.check_lines(corpus, lines,
                                    int(ctx.cfg.required_setting("narrative.quote_min_words")),
                                    quotecheck.titles(ctx.db.conn))
    report = [f"# Quote check: {p.name}", "",
              f"{'Lines added against ' + pathlib.Path(against).name if against else 'Whole file'}. "
              f"{n} quoted part(s) checked; {len(bad)} not found in the ESV text.", ""]
    report += [f"- \"{b}\"" for b in bad]
    out_dir = pathlib.Path(ctx.cfg.required_setting("narrative.register_report_dir"))
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, out_dir / f"{p.stem}-quote-check.md",
                                 report)
    msg = [f"{n} quote part(s), {len(bad)} failing -> {out}"] + [f"  ! {b[:150]}" for b in bad[:30]]
    if bad:
        return fail("quotes-failing", "\n".join(msg), parts=n, failing=len(bad), path=str(out))
    return ok("\n".join(msg), parts=n, failing=0, path=str(out))
