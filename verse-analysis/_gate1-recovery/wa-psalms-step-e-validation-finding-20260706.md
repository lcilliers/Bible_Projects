# Psalms pipeline Step (e) — full-integrity validation: FINDING

> Ran the Psalms characteristic-span completeness validation after the Gate-1 orphan onboarding. It surfaces a **systematic, larger gap** that needs a decision before the pipeline can be called complete for Psalms. Date: 2026-07-06. Probe: `scripts/_probe_psalms_gate1_validate_v1_20260706.py` + ad-hoc breakdown.

## What passed
- Onboarded (gate1) verse-records: verse_id / verse_span_id / mti_term_id all resolve; no NULL verse-text; no links to delete-flagged terms; **no active duplicates**. (dup_owner_strong back to baseline; collateral +0.)

## The finding — 1,082 of 3,810 Psalms characteristic spans (28%) have NO verse-record

Breaking the miss down by the span's strong:

| category | spans | meaning |
|---|---:|---|
| **onboarded gate1 strongs** | 445 | the 97 terms we just onboarded still miss 445 of their Psalms characteristic spans |
| **other already-registered strongs** | 637 | terms registered *before* gate1 (e.g. H3045 *know* 92, H2617 *chesed* 70, H0157 *love* 38, H2896 *good* 25) with **0 Psalms verse-records** for these spans |
| **unregistered (missed orphans)** | **0** | ✅ every characteristic strong in Psalms IS registered — the 97 was the complete orphan set |

141 distinct strongs; **all registered**. Example: H3045 (*yada*, know) — 92 characteristic spans in Psalms, **0 Psalms verse-records**.

## Root cause — the verse-record layer is STEP-limited; the span layer is full-text

- The **role/span layer** (`ve_lexical` + `verse_span_index`) was built from the **full Hebrew text** — it has *every* occurrence, so the role reassessment (Step 2, 150/150) is complete.
- The **verse-record layer** (`wa_verse_records`) is built from **STEP API pulls** — subject to the 60-cap and span-match filtering, so it does **not** capture every master-index occurrence. Even proper onboarding (which we just did, correctly) only pulls what STEP returns.
- Hence the mismatch: complete spans, incomplete verse-records — for onboarded *and* pre-existing registered terms alike. This is the concrete face of "the book-reading phase added zero verse-records."

## Why this matters / why I stopped

The compliant onboarding (STEP-based) is correct but **cannot by itself close Gate-1 completeness** at the "every characteristic span has a verse-record" level. Closing it requires **backfilling verse-records from the master index** (`verse_span_index`, which holds every occurrence) — with **full scaffolding** (term_inv_id, word_registry_fk, mti_term_id from the now-registered term). That is *not* the rejected bypass (sentinel file_index / thin mti / characteristic-only); it is proper records for registered, owned terms, sourced from the authoritative full-text index instead of STEP.

## Decision needed (options)

1. **Master-index backfill (recommended).** For every registered term with Psalms occurrences in `verse_span_index` but no verse-record, create a fully-scaffolded `wa_verse_records` row from the index (all occurrences, not just characteristic). This closes the gap completely and correctly, and generalises to every book. Needs a new reusable script + integrity gate.
2. **Accept STEP-limited coverage** as "good enough" for now; mark the 1,082 spans as a known, surfaced completeness debt; proceed to the reading/synthesis phase with the verse-records we have.
3. **Hybrid:** backfill only the **445 onboarded-term** spans now (finish what we started), defer the 637 pre-existing-registered gap as a separate programme-wide task.

**My recommendation: Option 1** — it's the real fix for the "zero verse-records" problem, uses the authoritative source, and is reusable per book. But it's a new phase (a master-index → verse-record backfill), so I'm surfacing it rather than launching it unilaterally.

*Filed 2026-07-06. Gate-1 orphan onboarding (the 97) is complete and correct; this is the next layer the validation exposes.*
