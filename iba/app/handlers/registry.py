"""Registry handlers — config-governed. New-word creation is a STANDARD OPERATIONAL routine, not a
development/design control (researcher, 2026-08-20 — the run.py escalation-volume review that
found configmaint.propose/registry.create/configmaint.validate together made up 79% of all
escalation rows): "if the standard new word create routine are used, then running should be logged
in the engine, it does not need another approval mechanism." Config writes (configmaint.propose)
are the opposite case — changes to the app's own behaviour — and correctly keep their real
escalation-gated approval; this file no longer does.

**No per-word approval gate as of 2026-08-20** (was: create as 'proposed', raise an escalation,
researcher answers Approve/Reject, resume). A new word is now created and marked 'approved'
directly, in one call — its outcome (including the duplicate/typo warning `_ask_approval` used to
gate on) is logged via `run.outcome`, the engine's own standard-run log, per the researcher's
instruction. `Escalation.ps1 -Action Answer -Word ...` (word-scoped answer) is now dead code for
this handler; kept in `lib/escalation.py` only because `handlers/configmaint.py`'s crash/report-stop
paths are unrelated to it and nothing else currently calls it, not because anything here still
does.
"""

from __future__ import annotations

import datetime

from .base import Ctx, Outcome, ok, fail

# Fallback only — the real value is `cfg_enum` group `word_status_built` (added 2026-07-29,
# closing a completeness gap: `cfg_status_flow` exists for exactly this kind of fact, but which
# statuses count as "already built" used to live only here, in code). Kept byte-identical so
# behaviour is unchanged whether or not the cfg_enum rows have been approved yet.
_BUILT_FALLBACK = ("raw-complete", "signed-off")     # a word past approval — a real duplicate


def _built_statuses(ctx: Ctx) -> tuple[str, ...]:
    return tuple(ctx.cfg.enum("word_status_built")) or _BUILT_FALLBACK


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _status_for(ctx: Ctx, set_by: str) -> str:
    for r in ctx.cfg.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='word' AND set_by LIKE ?",
            (f"%{set_by}%",)):
        return r["status"]
    return None


def _find(ctx: Ctx):
    """The registry row for this word, matched CASE-INSENSITIVELY (soft-deletes excluded)."""
    rows = ctx.db.rows(
        "SELECT * FROM word_registry WHERE lower(word)=lower(?) AND deleted=0", (ctx.word,))
    return rows[0] if rows else None


def exists(ctx: Ctx) -> Outcome:
    """Say the TRUE state of the word — not one vague 'new or mid-build'. Only a fully
    BUILT word stops here; every other state routes on to create with a clear message."""
    row = _find(ctx)
    if not row:
        return ok(f"{ctx.word!r} is not in the registry — a new word")
    st = row["status"]
    if st in _built_statuses(ctx):
        return fail("word-exists", f"{row['word']!r} is already built (status {st})")
    msgs = {
        "proposed": f"{row['word']!r} is a stale 'proposed' row from before the 2026-08-20 "
                    f"approval-gate removal — will register it now",
        "approved": f"{row['word']!r} is approved but its raw layer is not built — will build it",
        "rejected": f"{row['word']!r} was rejected before the 2026-08-20 approval-gate removal — "
                    f"will register it now",
    }
    return ok(msgs.get(st, f"{row['word']!r} is in the registry (status {st})"))


def create(ctx: Ctx) -> Outcome:
    row = _find(ctx)

    # already approved or built -> proceed idempotently (unchanged)
    if row and row["status"] in ("approved",) + _built_statuses(ctx):
        ctx.word_id = row["id"]
        return ok(f"{row['word']!r} already registered (id {row['id']}) — proceeding")

    # a word rejected under the old gate, before 2026-08-20 -- re-running now just creates it,
    # same as any other new word (no gate left to re-propose against).
    if row and row["status"] == "rejected":
        return _register(ctx, row["id"], row["word"], is_new=False)

    # a word stuck 'proposed' from before this change (none live as of 2026-08-20, but a stale
    # dump/backup could still have one) -- treat it the same as brand new, not a special case.
    if row and row["status"] == "proposed":
        return _register(ctx, row["id"], row["word"], is_new=False)

    # brand new: create it, approved, in one call -- no gate.
    rid = ctx.db.write("word_registry", {
        "word": ctx.word, "source": ctx.params.get("Source", ""),
        "status": "approved", "created_at": _now()})
    return _register(ctx, rid, ctx.word, is_new=True)


def _possible_duplicates(ctx: Ctx, seeds: list[str], self_id: int) -> list[dict]:
    """Existing words that already hold these strongs — a typo/variant check. Returns
    each such word with how many of the seed strongs it shares, most-overlapping first."""
    if not seeds:
        return []
    ph = ",".join("?" * len(seeds))
    rows = ctx.db.rows(
        f"SELECT wr.word AS word, wr.status AS status, COUNT(DISTINCT ws.strong) AS shared "
        f"FROM word_strong ws JOIN word_registry wr ON wr.id = ws.word_id "
        f"WHERE ws.strong IN ({ph}) AND ws.deleted=0 AND wr.deleted=0 AND wr.id != ? "
        f"GROUP BY wr.id ORDER BY shared DESC",
        seeds + [self_id])
    return [dict(r) for r in rows]


def _register(ctx: Ctx, word_id: int, word: str, is_new: bool) -> Outcome:
    """No approval gate (2026-08-20) -- creates/confirms the word and returns ok(). The
    duplicate/typo check the old _ask_approval() used to escalate on is kept, but now as a note
    in the outcome message (logged to run.outcome, the engine's standard-run log) rather than a
    blocking decision -- per the researcher's instruction, the standard routine gets no separate
    approval mechanism at all, not even for this case."""
    ctx.word_id = word_id
    d = ctx.step.call1_meanings(word)
    seeds = [x["strongNumber"] for x in d.get("definitions", [])
             if x.get("strongNumber") and not ctx.step.is_particle(x["strongNumber"])]
    dups = _possible_duplicates(ctx, seeds, word_id)

    # same threshold/signal as before -- registry.duplicate_shared_threshold (cfg_setting,
    # module 'registry', default 1.0 = ALL strongs shared).
    threshold = ctx.cfg.setting("registry.duplicate_shared_threshold", 1.0)
    warning = None
    if seeds and dups and dups[0]["shared"] >= threshold * len(seeds):
        other = dups[0]["word"]
        warning = (f" -- POSSIBLE DUPLICATE: shares ALL {len(seeds)} strongs with existing word "
                   f"{other!r}, may be a typo/duplicate, not blocked, logged for review")

    verb = "registered" if is_new else "re-registered"
    return ok(f"{word!r} {verb} (id {word_id}){warning or ''}")
