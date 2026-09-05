# Window 1 Layer 2 is verse-scoped, not passage-scoped — design correction

> Escalation #1451. Supersedes every prior framing of `lexical.enrich` as passage-gated,
> including my own recommendation on this same escalation (retracted, 2026-09-05) and the
> `#1376` consolidation proposal's "target shape" line (also wrong, flagged separately below).
> Authoritative source: the researcher's own 4-question design pass, verbatim, this session.

## The design, stated as the researcher gave it

1. **Why would Window 1 Layer 2 ever need more than the target verse?** Only to confirm an
   enriched-lexical assessment that cannot be gathered from the target verse alone (e.g. a
   pronoun's referent, a chain's continuation, an entity link's other end).
2. **Does that need require reading a large passage together?** Highly unlikely.
3. **Does the old (Window 2, debate-pipeline) `passage` mechanism apply here?** No.
4. **What method satisfies the need in (1)?** If the need arises, the analysis reads adjacent
   verses — one at a time, as needed — until the need is satisfied. This is a **targeted read**
   to satisfy one specific need, never a full lexical build of every adjacent verse touched. If
   the need is still not satisfied, that must be recorded explicitly as a lexical finding
   (`resolution_status='unresolved'`), not guessed or silently left ambiguous.

**Confirmed by the researcher, 2026-09-05: if per-verse Layer 2 enrichment works without
compromises, the whole `passage` concept falls away for Window 1 entirely.**

## The incompatibility this corrects

`lexical.enrich` (`handlers/lexical.py:enrich()`) currently hard-requires a pre-existing
`passage` row (`passagetrack.find_tracked_passage`) and refuses with `no-passage` otherwise.
`passage`/`passage.build` is Window 2's own debate-pipeline construct — gated by `hib.set`
(escalation #1451's original finding). Requiring *any* Window-2 object as a prerequisite for a
Window-1 write makes Layer 2 structurally dependent on HIB-gated infrastructure it must never
touch — Window 1 categorically does not consider or determine inner-being value. That is the
actual incompatibility, not a bug in the gate's logic — the coupling itself is a category error.

## Why the schema already supports the corrected design, mostly unchanged

`verse_lexical_note.target_verse_lexical_id`/`related_verse_lexical_ids` reference `verse_lexical`
rows generically — nothing about them requires the target to sit in the same verse, let alone the
same pre-registered passage. A note resolved by reading one adjacent verse already fits this shape
with no schema change. `resolution_status='unresolved'` already exists as a value used elsewhere in
Layer 2 — question 4's "must be clearly stated as a lexical finding" is the schema's own existing
convention, not a new mechanism to build.

## What actually needs to change

- `handlers/lexical.py:enrich()` — drop the `passagetrack.find_tracked_passage`/`no-passage`
  gate entirely. Operate against a target verse (or a small explicit set) directly.
- `lexicalenrich.py:enrich_passage()` — reworks to a verse-scoped entry point; `passage_id` is no
  longer a required input.
- **Completeness tracking** (`passage.lexical_complete_at`, `check_completeness`/
  `set_lexical_complete`) needs a new home — there is no passage row left to hang it on. Verse-
  scoped completeness (e.g. a `verse_lexical_note` aggregate check, or a new per-verse column) is
  the likely shape; not designed here.
- `verse_lexical_note.passage_id` — the column itself needs a decision: drop it, or repurpose it
  to mean something verse-scoped. Not designed here.
- `passage.build`/`Build-Passages.ps1`/#1451's own no-hibs gate **do not change** — they remain
  exactly as they are, but become irrelevant to Layer 2, which will never call them again. This is
  why #1451 itself (the no-hibs gate) needs no fix under this design — the gate was never the
  problem; calling it from Layer 2 at all was.

## A related error already sitting in approved work — flagged, not yet corrected

Escalation #1376's consolidation proposal (already approved) contains the same category error:
*"`hib`/`phenomenon`/`operation`... keep and treat as the target shape... what a
`verse_lexical`-grounded characteristic model should look like once scaled past Daniel."* That
describes Window 1 (`verse_lexical`) as something that should eventually produce or scale into
HIBs/phenomena — the same conflation this document corrects. That line needs to come back out of
the approved #1376 disposition; not actioned here, named so it isn't lost.

## Status

Design confirmed by the researcher. **Not implemented.** Nothing in `handlers/lexical.py`,
`lexicalenrich.py`, or the `verse_lexical_note`/`passage` schema has been touched under this
document yet.
