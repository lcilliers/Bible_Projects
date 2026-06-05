# Toward a meaning-centric verse process (emerging direction)

> **Emerging — 2026-06-05. Not settled.** Captures the researcher's reflection that the span-pairing rule,
> the Seven-Principles augmentation, and cross-verse clarification together point at a **meaning-centric**
> shape for the cluster pipeline. For review; nothing changed.

## The three observations (researcher, 2026-06-05)

1. **Grouping is largely encapsulated by interpretation + keywording.** Much of what the sub-group (Phase B)
   and VCG processes do appears to be *already carried* by a disciplined verse-meaning + keyword pass.
2. **Open questions are a key driver.** The questions flowing from the Seven-Principles augmentation
   (is the text secure? is the lexical sense contested? is the fulfilment/reference debated? is the meaning
   clear?) are not by-products — they *drive* the verse process.
3. **Unclear → clarified by other verses, at the meaning stage.** When a verse is unclear, it must be
   clarified by other verses, and that clarification must **emerge during Pass A** — not be deferred
   downstream.

## Why these hold (grounding, not just intuition)

- **Keywords were built to be the grouping signal.** Per `feedback_phase2_passa_emits_keywords`: the keyword
  pool "reveals which inner-being faculty axes are present… the structural input that drives Phase 5
  sub-group design." So sub-groups (= faculty axes) and VCGs (= similar-meaning clusters) **derive from**
  the keyword/meaning layer. If keywording is rigorous, the grouping largely *falls out* of it.
- **Scaffolding-not-reality.** Clusters / sub-groups / VCGs are disposable reading aids
  (`feedback_no_forced_structure…`, foundations §a). If the meaning layer is the real data, the grouping is
  a **derived view**, not separate analysis.
- **It attacks bias-compounding at the root.** `feedback_two_governing_principles`: bias compounds Pass A →
  sub-group → VCG → findings — "by Phase 9 the verse has been read through the cluster lens three times."
  Reading the verse **once, richly** (span-focal, sibling-aware, keyworded, questioned) and *deriving* the
  grouping removes two of those three lens-passes. This is a strong argument *for* the direction.
- **It is a candidate answer to the foundations' central open question (§c-Q7, the unit-of-analysis /
  fault-line problem).** If grouping is *emergent from the verse data* rather than *imposed*, the partition
  is far less of a "false claim" about the subject — the fault lines soften.
- **Cross-verse clarification = the analogy of Scripture** (Seven Principles 6: clearer passages illuminate
  obscurer ones) + the term's meaning corpus (`feedback_setaside_verses_inform_word_meaning`: a term's other
  occurrences characterise its sense). The mechanism already exists in the data (a term's verses; sibling
  spans); the move is to **use it at the meaning stage**.

## What it implies for the architecture

A **meaning-centric pipeline**: Pass A becomes the heavy analytical core, and the downstream grouping phases
shrink toward **derived / confirmatory** views.

| | Current (v3 A→B→…) | Meaning-centric |
|---|---|---|
| Pass A | meaning + keywords | meaning + keywords + **span-pairing** + **open questions** + **cross-verse clarification** |
| Sub-groups (Phase B) | fresh AI grouping into faculty axes | **derived** from the keyword pool; human *confirms/adjusts* |
| VCGs | fresh AI grouping by similar meaning | **derived** clusters of like meanings/keywords |
| Findings | per-tier catalogue synthesis | still per-tier, but on a far cleaner, questioned, cross-linked base |

## Concrete Pass A additions this would need (candidate — for the drafts)

- **Emit `open_questions` per verse** — typed by principle: `textual` (variant) · `lexical` (contested
  sense) · `reference/fulfilment` (debated) · `unclear-needs-corpus` (meaning not settled from this verse
  alone). These are the surfaced contested readings (foundations §c) and the verse-meaning-corroboration
  worklist (`project_next_action_audit_surface_verses`).
- **Cross-verse clarification at the meaning stage** — when a verse is `unclear-needs-corpus`, resolve it
  against the **term's own corpus** (its other occurrences, where the sense is clearer) and its **sibling
  spans / cross-references**; record the clarification (which verses settled it). This is a *second look*
  within Pass A, driven by the open question.
- **Grouping signal** — already the keyword pool; formalise that sub-groups/VCGs are *generated* from it and
  then human-confirmed, rather than authored fresh.

## Open questions / risks (for the researcher)

1. **How much grouping truly derives vs still needs judgment?** Test empirically before committing.
2. **Pass A cost & complexity rise materially** — span-pairing + open-questions + clarification per verse.
   Bounded? (per-verse API cost, wall-time, reviewer load).
3. **Storage** — `open_questions` and clarification links need a home (new `verse_context` columns or a side
   table). A schema question, deferrable until the shape is agreed.
4. **Clarification scope** — term corpus only, or wider canonical cross-references (harder to source)?
5. **Does this *collapse* Phases B–C into A, or just *feed* them?** Likely "feed + shrink", not "delete" —
   human confirmation of the derived grouping stays.

## Proposed next step (evidence before architecture)

Do **not** redesign yet. Validate on a slice: take ~15–20 M01 verses (mix of clear, contested, and
multi-T1), and work them **by hand** through span-focal meaning + keywords + open-questions +
clarify-by-corpus. Then ask: (a) how much of M01's sub-group/VCG structure *falls out* of the keywords?
(b) how often do open-questions / clarification actually fire? (c) what does it cost per verse? The answer
tells us whether the meaning-centric shape is real or just elegant. This matches the project's
investigate-first discipline.
