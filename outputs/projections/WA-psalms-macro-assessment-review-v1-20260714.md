# Assessment of the AI's first Psalms macro pass (my view)

**Reviewing:** `outputs/projections/outputs/WA-session-log-psalms-macro-v1.0-2026-07-14.md` (the AI's session log).
**Date:** 2026-07-14 · **Reviewer:** Claude Code · **Verified against:** live DB (`reread-psalms-2026`).

---

## Headline view

**The test succeeded — better than a clean pass would have.** The projection was handed to a fresh
analyst with only the preamble, and it (a) navigated the data unaided, (b) honoured the one rule that
matters most — `NONE` (assessed silence) ≠ `ABSENT` (unread), (c) kept observation / interpretation /
reflection separate, (d) flagged its *own* confirmation bias, and (e) **surfaced a real data bug we did
not know we had**. A projection that lets a downstream reader find a defect in the source is doing exactly
the job it was built for. The design is fit for purpose.

Two of its four open questions I have now verified against the DB. One is a **real, actionable bug** we
should fix at source; the other is a **fair hit on the weakest of the five retrofit dimensions**, and the
AI is right to distrust it.

---

## The two claims I verified

### DQ-01 — coupling/locus transposition — CONFIRMED, real, Psalms-only, ~665 spans
- Span 268779 (Psa 100:1): `coupling(112) = 'external:god'`, `locus(116) = 'paired with serving with gladness'` — the two fields are swapped.
- **665 Psalms spans** carry the full swap signature (coupling holds an enum-locus value AND locus holds a "paired with…" phrase). The AI counted 666 — essentially exact.
- coupling(112) holds **737** enum-locus values (387 `internal:ib-state`, 276 `external:god`, …); locus(116) holds **713** off-enum values (mostly coupling-phrases).
- **Proverbs = 0** such rows. This is a **Psalms-read-specific** defect, not a projection artefact and not from the retrofit (which only wrote 109/110/111/117/118).
- **Verdict / recommendation (answers the AI's Q-2):** fix at **source**, not by in-analysis normalisation. A targeted swap patch — for the 665 clean-signature spans, exchange the `value` of ve_nr 112 and 116 — is safe and mechanical. In-analysis normalisation should be a stop-gap only; every future consumer would otherwise have to re-discover and re-patch the same swap. I can prepare the patch.

### Q-1 — `effect` 97.7% NONE — the AI is right to distrust it; my honest concession
- `effect(111)` is the **weakest** of the five retrofit dimensions. It is **derived** by a result/consequence regex over the reading+operation prose. So `NONE` means "no consequence-verb was found in the prose" — which conflates **genuine genre-silence** (Psalms names the movement, withholds the outcome) with **deriver conservatism** (an implied consequence the regex didn't catch).
- Therefore `effect = 97.7% NONE` is a **floor, not a measured silence**. It should **not** carry any consequence-analysis until a proper `effect` read is done (the Phase-2, book-level effect pass envisaged in the catalogue).
- The same caveat applies, in lesser degree, to `intensity`(109) and `specifier`(110) — both are qualifier-signal-derived. **`device`(117) and `direction`(118) are the strongest** (device is corroborated by the verse text + the pairs control; direction reads off the target/locus/operation and matches the genre — Psalter runs Godward).
- **This is the most valuable methodological output of the test:** it tells us precisely which dimension to deepen from derivation to a real read.

---

## Where the AI's instincts match our own governance (good signs)

- **Singleton tail** — 385 of 657 characteristics occur once (58.6%). It refused to let the top-30 head (heart 77, praise 73, soul 65) stand for the book. This *is* our `resist_grouping_preserve_distinctions` and `verse_fanout` discipline, arrived at independently.
- **Psalm 119 outlier** (244 readings, 11.3%) flagged as a control before trusting any unstratified figure — correct.
- **Refused to import a verse-count denominator from memory** — correct under our factual-discipline rule.
- **Flagged its own convergence bias** on the God-ward finding ("we built a column called `direction`, so we found directions") — exactly the epistemic hygiene we want.

## The one design gap the test exposed (self-critical)

The projection ships **only `role='characteristic'` rows**. But intensity/specifier/effect/device are, in our
own model, **qualifier-derived**. By withholding the qualifier/standalone rows, the projection hides the very
evidence that would let a reader separate *assessed-NONE* from *under-read* on effect — which is exactly why
Q-1 is unanswerable from the supplied files, and exactly what the AI asked for in its next-steps. **Projection
v2 should ship the qualifier + standalone spans** (or link each char to its qualifier spans). This is a real
improvement the first test earned.

---

## My answers to the AI's four questions (for relay)

- **Q-1 (effect NONE):** Both — but treat it as a derived floor, not measured genre-silence. Do not build consequence-analysis on it until `effect` is read properly. device/direction are trustworthy; intensity/specifier are indicative.
- **Q-2 (transposition):** Fix at source. Targeted swap patch for the 665 spans (Psalms only). Normalisation-in-analysis only until the patch lands.
- **Q-3 (unit):** **Readings** — it is the finest grain and the unit the whole model is built on. But supply the **verse universe** so coverage can also be stated. (Characteristics/lemmas are roll-ups of readings, available on demand.)
- **Q-4 (next move):** (ii) the **faculty↔inward asymmetry** (I-3) — it is a *structural movement* claim, the most testable and the most on-method. But first give it: the **qualifier/standalone rows**, the **verse universe**, the **companion spec**, a **Psalm-119-excluded** control, and the **Proverbs projection** as contrast.

## Actions this review recommends (in priority order)

1. **Prepare the DQ-01 swap patch** (665 Psalms spans, 112↔116) — highest value, mechanical, safe.
2. **Projection v2: ship qualifier + standalone rows** so effect/intensity/specifier are auditable (unblocks Q-1).
3. **Supply the four requested inputs** (verse universe, qualifier rows, companion spec, Proverbs projection) and re-run with Psalm 119 excluded.
4. **Schedule a real `effect` read** for Psalms (Phase-2 book-level) before any consequence-analysis.
