"""Registry handlers — the word enters (frame; the full registry process is the
researcher's, taken separately). This slice does the two steps the raw run needs:
exists? and create."""

from __future__ import annotations

import datetime

from .base import Ctx, Result, ok, stop, pause


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def exists(ctx: Ctx) -> Result:
    """Stop if the word is already registered. A refresh run (not built) handles that."""
    row = ctx.db.get("word_registry", word=ctx.word)
    if row and not row["deleted"]:
        return stop(f"the word {ctx.word!r} already exists (registry id {row['id']}). "
                    f"Use a refresh run, not new-word.")
    return ok("word is new")


def create(ctx: Ctx) -> Result:
    """Create the registry entry. In the full app this is preceded by a researcher
    approval escalation (word_status proposed -> approved); here we approve directly
    and record it, so the slice runs end to end. The escalation point is marked."""
    # NOTE: the approval escalation is where util.escalation would pause for a
    # researcher yes/no with preset details (term count, verse count, terms already
    # held). Stubbed to auto-approve so the slice completes; the seam is here.
    rid = ctx.db.write("word_registry", {
        "word": ctx.word,
        "source": ctx.params.get("Source", ""),
        "status": "approved",
        "created_at": _now(),
    })
    ctx.word_id = rid
    return ok(f"registered {ctx.word!r} as id {rid}, status approved", word_id=rid)
