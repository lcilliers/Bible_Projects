"""wordaudit.py — the `word-audit` work package (escalation #672, plan v4 Phase 1).

**Deliberately stub handlers, not a port.** Per escalation #656's standing rule ("redesign, don't
auto-adopt") and `feedback_never_model_output_on_prior_unreviewed_pass`, this is NOT
`engine/audit_word.py`'s logic copied over. Registering these 10 steps (`BUILD.md` §127) made the
work package real and dispatchable — `run.py`'s gates (`module_blocking`, `step_kind`,
`cfg_write_grant`) all apply to it exactly like every other work package. What each step actually
DOES, beyond the minimal real bookkeeping below, is deliberately left `not-yet-implemented` rather
than faked, because writing this handler surfaced a genuine open question that has to be answered
first, not guessed at:

**The word-identity question.** `engine/audit_word.py`'s file-discovery convention
(`research/discovery/{registry_no:03d}_{word}_..._{YYYYMMDD}.json`) keys off
`bible_research.db.word_registry.no` — the LEGACY 222-word registry (32 columns, `no`/
`phase1_status`/`cluster_assignment`/... — see `BUILD.md` §126). `run.py`'s `Ctx.word_id` resolves
against `iba.db`'s OWN `word_registry` (6 columns: `id`/`word`/`source`/`status`/...) — a different,
newer, currently-smaller table for the raw/new-word pipeline. These are NOT the same registry, and
nothing yet states how (or whether) a word progressing through `word-audit` should read/write
`bible_research.db`'s legacy row at all — that's exactly the same "does `word.*` need a second,
`bible_research.db`-scoped DB connection" question `bootstrap_word_audit.py`'s own docstring
already flagged for `cfg_write_grant`. One open question, two symptoms — not answered here.

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
