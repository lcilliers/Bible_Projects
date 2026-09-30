# `location` engine — root cause + fix plan (v1)

**File:** wa-location-engine-fix-plan-v1-20260618.md · **Type:** data-quality root-cause + fix plan (markdown)
**Date:** 2026-06-18 · **Prompted by:** researcher — "the location indicator is not taking the full lexical data into account and is not being assigned correctly."
**Code:** `scripts/_ve_engine_v2.py` — SEAT seed list (lines 31-37); location rule (lines 219-234). **Companion:** `wa-location-coverage-and-spirit-underdetection-20260618.md`.

---

## Confirmed: the diagnosis is correct. Two independent defects.

### Defect 1 — the seat seed list is incomplete (under-coverage)
`SEAT` is explicitly tagged *"01b iteration-1; expand later"* and maps only 8 lemmas: soul (H5315/H5314/G5590), heart (H3820/H3824/G2588), spirit (H7307/G4151), flesh (H1320/G4561). Whole seat categories are **absent**, yet occur as tagged terms in the corpus — so they can **never** receive a location today:

| missing seat | lemma(s) | term-in-verse units | currently |
|---|---|---:|---|
| mind | nous G3563, dianoia G1271 | 22 + 12 = 34 | no location possible |
| conscience | suneidesis G4893 | 29 | no location possible |
| inward part | qereb H7130 | **168** | no location possible |
| bowels (seat of compassion) | me'eh H4578 | 30 | no location possible |
| kidneys (seat of emotion) | kilyah H3629 | 13 | no location possible |

This fully explains why **`mind` and `conscience` are 0 corpus-wide** — there is simply no lemma mapped to them. `qereb` alone (168) is a major Hebrew seat-of-the-inner-being word that is entirely invisible.

### Defect 2 — the spirit sense-gate self-trips on the lemma gloss
The gate at line 227 routes ruach/pneuma to `UNRESOLVED` when `SEAT_NONSEAT_SENSE` (`wind|breath|ghost|life`) matches `w["text"] + " " + gloss`. But `gloss` is the lemma's **full dictionary definition**, which always lists every sense:
- H7307 gloss = `": spirit / 1) wind, breath, mind, spirit ..."` → **trips** (contains "wind, breath")
- G4151 gloss = `"wind, breath, things ..."` → **trips**

So **every** ruach/pneuma occurrence trips the gate regardless of its actual contextual sense, and spirit is **never assigned mechanically** (provenance proves it: all 28 spirit rows are `location_read_api`, zero `v2_engine_iter1`). The gate is testing the dictionary (which is sense-neutral) instead of the verse's **per-occurrence** sense.

## Root cause in one line
Location is derived from a **hand-seeded 8-lemma list** plus a **gloss-based** spirit gate — it does not use (a) the full set of seat lemmas the lexicon contains, nor (b) the per-occurrence contextual `sense`/`target_word` that the rest of the pipeline already has. Hence "not taking the full lexical data into account."

## Decisions needed from the researcher (methodology, not mechanics)
1. **Do the Hebrew visceral seats get their own levels or fold into existing ones?** e.g. qereb/me'eh/kilyah → a new `inward-parts` level, or mapped to `heart`/`soul`? (Hebrew idiom seats emotion in kidneys/bowels.)
2. **`mind` in Hebrew:** Hebrew has no distinct "mind" word — `leb`/`lebab` covers heart+mind. Keep `mind` as a Greek-only level (nous/dianoia), and leave Hebrew "mind" senses under `heart`? 
3. **Spirit gate:** confirm it should gate on the **per-occurrence sense** (target_word / STEP sense), routing to the read only when the *context* (not the dictionary) is genuinely ambiguous.

## Proposed fix (CC domain, once decisions land)
1. Expand `SEAT` to the full seat-lemma set agreed in step 1-2 (add mind, conscience, the visceral seats; verify zero-padded forms per `reference_strongs_zero_padded_4digit_in_db`).
2. Replace the gloss-based spirit gate with a **per-occurrence sense** test: trip to the read only when the verse's `target_word`/sense reads as wind/breath, not when the dictionary merely lists those senses.
3. Re-run the mechanical location pass corpus-wide; route only the genuinely-ambiguous spirit cases to a small read.
4. **Diff before/after** and report: expect spirit to rise from 28 into the low hundreds, plus new mind/conscience/inward-parts rows. The ~11% verse coverage will rise modestly but stay sparse (correct — location is opt-in).

*Read-only investigation; nothing changed. The seed-list expansion is a methodology call — awaiting the step 1-3 decisions before any engine edit + re-run.*
