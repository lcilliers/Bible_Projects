"""wordaudit.py — the `word-audit` work package (#672): registered, dispatchable steps under run.py's
gates, with stub handlers. Each step does minimal bookkeeping and otherwise returns
`not-yet-implemented`; it is not a port of `engine/audit_word.py`.

Open question blocking the real steps: `engine/audit_word.py` keys off
`bible_research.db.word_registry.no` (the legacy registry), while `Ctx.word_id` resolves against
`iba.db`'s own `word_registry`. How, or whether, a word in `word-audit` reads or writes the legacy row
is not decided.

    python -m iba.app.run word-audit --step word.load_json --run-id <id> --param Word=<word>
"""

from __future__ import annotations

from .base import Ctx, Outcome, fail, ok


def _stub(ctx: Ctx, step: str, note: str) -> Outcome:
    return fail("not-yet-implemented",
               f"{step} registered and dispatchable (kind/on_fail/write_grant gates all apply) "
               f"but not yet built — {note}. See wordaudit.py's own module docstring: the "
               f"word-identity question (iba.db word_registry vs bible_research.db word_registry) "
               f"needs an answer before this step's real logic can be written.")


def load_json(ctx: Ctx) -> Outcome:
    """Real bookkeeping done: confirms a Word param was actually given (run.py's dispatcher
    normalises it via lib.words.normalise before any handler runs — checked here defensively,
    not re-implemented). Everything past that — finding/parsing the Step 1 JSON file — is the
    word-identity question."""
    if not ctx.word:
        return fail("no-word", "word-audit requires --param Word=<word>")
    return _stub(ctx, "word.load_json",
                "needs the word-identity question resolved to know WHICH registry's row + "
                "discovery-file convention applies")


def confirm(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.confirm", "registry display needs a resolved source row to display")


def gap_report(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.gap_report",
                "the gap streams (Term/Related/Verse/VTL) are bible_research.db tables")


def gap_display(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.gap_display", "displays word.gap_report's output")


def apply_changes(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.apply_changes",
                "the actual data mutation — squarely blocked on the cross-database write "
                "mechanism bootstrap_word_audit.py's docstring flags as not yet built")


def meaning(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.meaning", "parses into bible_research.db's wa_meaning_* tables")


def flag_reset(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.flag_reset", "resets bible_research.db's wa_data_quality_flags")


def audit_checks(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.audit_checks",
                "the 20 WR-* checks — each needs individual review against whichever "
                "bible_research.db tables persist, per the plan's own §Phase 1 note, not a "
                "batch port")


def registry_close(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.registry_close", "updates the (still-ambiguous) source registry row")


def export(ctx: Ctx) -> Outcome:
    return _stub(ctx, "word.export", "exports the (still-ambiguous) source registry's full word")
