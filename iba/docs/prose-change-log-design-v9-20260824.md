# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v8-20260824.md](prose-change-log-design-v8-20260824.md) (v1–v8
kept on disk for history). This round is a correction: v8 §30 was **wrong**. The researcher's
original framing (payload = what a change overwrites, not what it produces) was correct all along —
reverting to it, and explaining plainly where the confusion actually came from.

---

## 33. The correction — payload is prior-state, v8 was the mistake

Researcher, verbatim: *"how it looks like after the change is in the prose (current record); what is
not retained is what it looked like before — I thought that is the payload — maybe the confusion is
in the naming."* That's right, and it's not a naming issue on the researcher's side — it's a mistake
in v8.

**The reasoning, straight:** `prose_section`/`prose_section_type` already hold the current content,
live, always (that's the entire point of Model A). There is never a reason to *also* copy the current
content into `record_change_log` — that would just duplicate data the live table already has. The
**only** thing that stops existing the moment an edit lands is what the row used to say. That's the
one thing worth logging. So: **payload = the content a given change overwrote or removed — its
prior state, not its resulting state.** v8's "correction" had this backwards; reverting to what v4/v7
already had.

**Why this still answers "look back at any previous version" (§18), with zero redundancy:** each edit
writes exactly one log row, and that row's payload is what existed *immediately before* that specific
edit. Walking a row's full history is then: read the live row for the current content, and walk its
`record_change_log` rows (by `target_table`/`target_id`, ordered by `id`/`change_datetime`) for
everything that came before it — each one holding exactly the state that edit replaced. Nothing is
ever stored twice: the live table holds the current state exactly once; the log holds every prior
state exactly once each. v8's resulting-state framing would have briefly duplicated the current
content between the live row and the newest log row until the next edit — small, but real, and
exactly the kind of redundancy the researcher's own compression/bulk instinct (§16.2/§18) has been
pushing against throughout this thread.

**What `version` actually means, precisely, now that this is settled:** `prose_section.version` (=
`record_change_log.id`) is a pointer to **the record of this row's own most recent edit** — not a
pointer to "my current content" (redundant; that's just the live row) and not a pointer to "version
N's content" in the naive numbering sense either. It answers *"what did I most recently replace, when,
and why"* — an audit/undo pointer, not a content-lookup pointer. That's the correct, minimal meaning,
and it's a coherent one: nothing about "look back at a previous version" requires `version` itself to
resolve directly to that version's content — it requires the *chain* of log rows to be walkable, which
it is.

**Where the actual confusion came from:** v5 §16.1's own research (system-versioned temporal tables)
already described this correctly — "a paired history table captures the prior row automatically" —
and v6/v7 followed that correctly too. v8 drifted from it while trying to make the migration
instruction (§29) feel intuitive, and reasoned itself into the wrong framing in the process. Owning
that plainly rather than treating it as a wording ambiguity: it was a real design mistake, now fixed.

---

## 34. Consequences, worked through

- **§29's migration instruction now fits *more* naturally, not less.** The 91 existing superseded
  `prose_section` rows are literally prior states — each one's own content, exactly as it stood before
  being superseded, is precisely what belongs in `record_change_log.payload`. v8's claim that
  resulting-state was "the only reading that makes the migration instruction... work" was itself
  wrong — withdrawn.
- **`insert` events have no prior state to log** — payload is legitimately empty/NULL for
  `change_type='insert'`. The log row still gets created (so the new row has something for `version`
  to point at), it just carries no payload content. Not a gap, an expected case.
- **The §29 baseline-backfill rows (949 live `prose_section` rows + 108 `prose_section_type` rows)
  need revisiting under this correction.** Under resulting-state (v8), the natural baseline payload
  would have been "a copy of the row's current content." Under prior-state (corrected), there genuinely
  *is* no prior state for these at migration time — nothing was overwritten to produce them, migration
  is just giving them their first `version` pointer. Proposing payload = NULL for the baseline batch
  too, same as a fresh `insert` — consistent, no invented content. Flagging as a proposal, not
  asserting it's the only sane choice: the alternative (a one-time snapshot of current content, purely
  for safety) is defensible too, just re-introduces the exact redundancy §33 argues against, and only
  at this one seam. Researcher's call.
- **`delete` events** — payload = the row's content immediately before the delete (today's soft-delete
  sets `delete_flagged`; the row's `body` etc. doesn't change at the moment of deletion) — fits the
  prior-state model cleanly without needing separate reasoning.

---

## 35. Updated field note

`payload` (§31's field list, unchanged in shape) — clarified: **nullable**. Populated for `change`
and `delete` events (holding what was overwritten/removed); NULL for `insert` events and for the §34
migration-baseline rows (nothing preceded them).

No other change to §31's field list.

---

## 36. Still open

- §34's baseline-payload choice (NULL vs. one-time current-content snapshot) — proposal given, not
  decided.
- Diff-based storage for `payload` (v5 §16.2) — still a named future option, not scheduled.
- §25's findings-integration choice — parked, not this item's decision.
