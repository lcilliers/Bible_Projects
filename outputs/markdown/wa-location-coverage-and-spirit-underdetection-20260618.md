# `location` field — coverage reality + spirit under-detection (findings)

**File:** wa-location-coverage-and-spirit-underdetection-20260618.md · **Type:** read-only data-quality finding (markdown)
**Date:** 2026-06-18 · **Prompted by:** researcher noticing only ~20% of inner-being verses show a location, and only 28 reference spirit.
**Companion:** `wa-location-by-cluster-summary-20260618.md`.

---

## Two distinct issues — one expected, one a defect

### 1. Low location coverage (~11%) — largely BY DESIGN
- Focus inner-being corpus (non-T2): **30,569 term-in-verse units across 16,310 distinct verses.**
- Distinct verses with **any** location: **1,726 → ~10.6%** (lower than the ~20% headline, which counted multi-value rows, not verses).
- **Why this is expected:** `location` only fires when a verse *explicitly seats* the state — a constitutional-seat lemma (heart/soul/spirit/flesh) is present and governs/co-occurs with the term ("fear **in his heart**"). The vast majority of verses simply predicate the state ("he **was afraid**") with no seat named. So a low base rate is the correct, faithful result — silence = genuinely not located, not a miss.
- Caveat to carry into analysis: location is therefore a **sparse, opt-in** field — present it as "where the text *explicitly* seats the state," never as "where the state lives" (absence ≠ not-seated-in-reality).

### 2. Spirit is genuinely UNDER-detected — this IS a defect
The seat-assignment ratios expose it. Each seat-lemma appears as a tagged term, and is also *assigned as a seat* to neighbouring state-terms:

| seat | appears as a term (units) | captured as a location (rows) | ratio (loc ÷ term) |
|---|---:|---:|---:|
| heart | 749 | 2,604 | **3.5×** |
| soul | 635 | 2,229 | **3.5×** |
| flesh | 161 | 627 | **3.9×** |
| **spirit (ruach/pneuma)** | **344** | **28** | **0.08×** |

- heart/soul/flesh each get assigned as a seat **~3.5–3.9× more often** than the lemma itself appears (correct — a seat-word seats the state-terms around it).
- **spirit runs the opposite way:** 344 term-appearances but only 28 seat-assignments — a ~**40× shortfall** vs the others. If spirit behaved like the rest, we'd expect spirit-locations in the **hundreds**.
- **Root cause:** spirit is **sense-gated to read-only** (ruach/pneuma can be wind/breath/disposition, not the constitutional seat). The provenance proves it — **every** spirit row (all 28) is `location_read_api`; the mechanical pass (`v2_engine_iter1`) emits **zero** spirit. So spirit is captured *only* when a verse was sent to the verse-read, and only 28 ever were. The other ~316 ruach/pneuma verses were never assigned a spirit seat by the mechanical pass and never surfaced for the read.

## Verdict
- The **~11% coverage is real and acceptable** — location is meant to be sparse. Just frame it correctly in the analysis.
- The **28 spirit count is a detection gap, not Scripture.** The mechanical seat-assignment rule applies heart/soul/flesh to neighbouring terms but does not do the same for spirit (it defers everything to a read that only ran on a tiny candidate set). This under-represents spirit-seated inner life (broken/troubled/haughty/willing spirit, etc.).

## Recommended next step (CC domain — data/generator)
1. Enumerate the ~344 ruach/pneuma term-verses and classify how many are the **constitutional seat** vs wind/breath/disposition (the sense-gate's real target).
2. Extend the mechanical seat-assignment rule to assign `spirit` to neighbouring state-terms the same way it does heart/soul/flesh, **then** route only the genuinely-ambiguous ruach/pneuma to the read (not all of them).
3. Re-run location for the affected verses; expect spirit to rise from 28 into the low-hundreds. Diff before/after.

*Read-only finding; no data changed. Awaiting go-ahead before any generator/rule change.*
