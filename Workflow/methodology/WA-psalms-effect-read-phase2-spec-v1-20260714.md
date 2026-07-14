# Phase-2 book-level EFFECT read — Psalms (and thereafter every re-read book)

**Version:** v1 · **Date:** 2026-07-14 · **Status:** SCHEDULED (not yet executed).
**Trigger:** the AI's first Psalms macro pass raised Q-1 — `effect(111)` is 97.7% `NONE`. Verified: `effect` is
currently **derived** (a result/consequence regex over the reading prose), so `NONE` is a **floor**, conflating
genuine genre-silence with under-reading. Before any consequence-analysis, `effect` must be **read**, not derived.

## What this read is (and is not)

- **Is:** for each read-2026 characteristic, the **consequence/outcome the verse (and its passage) attaches to that inner-being movement** — what it produces, leads to, kindles, saves from, ends in. Read *on the verse*, strictly verse/passage-bounded (no imported theology). Follows `feedback_lexical_strictly_verse_bounded_no_implied_evidence` and `feedback_verse_meaning_grounded_not_imported`.
- **Is not:** a re-derivation from the existing prose (that is what we are replacing); nor a whole-book theme. It is a per-char, evidence-anchored effect value.

## Why derivation is insufficient (the Q-1 finding)

The deriver reads `effect` off consequence-verbs already present in the reading note. Where the read did not
*state* a consequence, the deriver returns `NONE` even if the verse plainly attaches one. So the 97.7% `NONE`
is not a measured silence — it is the reading prose's silence, inherited. Only a fresh read can distinguish
"the psalm withholds the outcome" (real, and itself a finding) from "we didn't read the outcome" (a miss).

## Method (mirrors the reread cadence)

1. **Unit:** the characteristic, read within its **passage** (never a bare verse in isolation; per `feedback_read_by_passage_not_whole_chapter`).
2. **Cadence:** per-passage cycles with a read-back each cycle (as the retrofit roll ran), so the effect layer is auditable as it lands.
3. **Value contract (self-interpretable):** an effect value must read without the verse — `"<consequence> — <the movement it flows from>"` (e.g. `"drives the psalmist to cry out — the terror of v3"`), or an **assessed** `none` where the passage genuinely attaches no outcome. **Never silent `ABSENT`.**
4. **Secondary control:** the `linked_qualifiers` / `qualifiers.csv` layer — a consequence-bearing qualifier beside an `effect=none` char is a re-read trigger (as `salvation` beside `hope` at Psa 42:5). Control, not sole trigger.
5. **Provenance:** write as `ve_nr=111` rows under `source_provenance='reread-psalms-2026'`, superseding the derived row (soft-delete prior, like the retrofit apply). Mark the value's origin as read-grade (distinct from the derivation floor) so the projection can show which is which.
6. **Gate:** a passage is complete when every char in it carries a read-grade effect (value or assessed-none) and the read-back confirms self-interpretability.

## Scope + sequencing

- **Psalms first** (2,168 chars). Then bake the same effect-read step into the standard book read so future books never ship a derived-floor effect.
- Roughly the size of one retrofit roll; run it as its own cycle series with its own read-back log.
- **Blocks:** any consequence / outcome / "what does this movement produce" analysis on Psalms until this lands. `device` and `direction` are unaffected (read-grade already).

## Handoff

Until executed, the projection marks `effect` as **derivation-grade** (see `AI-handoff-package-psalms-v1-20260714.md` Q-1). The AI has been told not to build consequence-analysis on it, and to audit any specific `effect=NONE` via the qualifier layer.
