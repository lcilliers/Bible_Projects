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

---

## RESOLUTION (2026-07-06) — Option 1 executed: master-index backfill

Researcher chose Option 1 ("the master index is supposed to pull everything together"). Built `scripts/_apply_master_index_backfill_v1_20260706.py` — creates **fully-scaffolded** `wa_verse_records` from `verse_span_index` (term_inv_id + word_registry_fk + mti_term_id + **verse_span_id** link), for every registered OWNER-term occurrence lacking one. Per-book, integrity-gated.

**Psalms result — characteristic-span miss 1082 → 172:**
| pass | records | char miss after |
|---|---:|---:|
| v1 unambiguous (single OWNER) | +2,888 | 286 |
| ambiguous tier (dominant-sense: OWNER sub-entry with most records; e.g. H2617→H2617A *kindness*) | +381 | **172** |

**+3,269 records total; no new invariant breach; all in-corpus.** ✅

### The residual 172 = a SECOND orphan set (27 stub terms)
The 172 remaining characteristic spans map to **27 legacy span-orphan stub `mti_terms`** created 2026-07-05 (`anchor_note='Gate-1 recovery 2026-07-05: span-orphan inner-being term…'`) — **NULL registry, no inventory**, survived the rollback. They are a *second* orphan set beyond the 97:
`H0157 love · H1350 redeem · H3467 save · H5382/H7911 forget · H7307 spirit · H5087/H5088 vow · H5358 avenge · H2449 be-wise · H7891 sing · H3238/H3905/H3906 oppress · H5678 fury · H6973 loathe · H0014 be-willing · H2670 free · H7309 relief · H7810 bribe · H0079/H5319 wrestle · H0034 needy · H1800 poor · H0490 widow · H3490 orphan · H0833 bless`

**Next step (needs your steer):** these 27 need the **same gate-1 treatment** — registry assignment (the analytical call, as with the 97) → `audit_word --add-terms` → then re-run the backfill to close the last 172 spans. Some are clearly IB (love, save, forget, spirit, vow); a few are social-category third parties (widow, orphan, needy, poor) that may be reference/qualifier like Satan. I've stopped here to bring you the 27-term registry mapping for review rather than impute it.

---

## CLOSED (2026-07-06) — Psalms Step (e) COMPLETE: characteristic-span miss = 0

Researcher approved the 27-term mapping (`wa-second-orphan-set-27-registry-proposal-20260706.md`) "all registries as suggested" + social quartet as **third party**.

- **New registry `the afflicted`** (id 221) REGISTERed for the third-party vulnerable (widow/orphan/needy/poor); role=reference.
- **22 clean stubs** onboarded fresh via `audit_word --add-terms` into their proposed homes; **5 tangled** (already-owned: H0157→love, H7307→anger, H0014→desire, H6973→distress, H0034→desire) reconciled to existing owners (no re-assign).
- **Master-index backfill re-run** (+178) then a **targeted H7307 fix** (+39; its OWNER inventory is H7307H/I sub-entries, base-mismatch to the mti).
- **Result: Psalms characteristic spans 3810 / covered 3810 / MISS 0.** Official probe `_probe_psalms_gate1_validate_v1` → **ALL PASS ✓**. No new invariant breach (dup_owner_strong=1 baseline). All 27 NULL-registry stubs cleared.

**Total this phase:** ~3,486 fully-scaffolded verse-records added from the master index across the three backfill passes + H7307. **Psalms corrective pipeline steps (a)–(e) are all complete.**

*Known minor: the backfill owner-join is exact-strong; base-vs-sub-entry mismatches (like H7307) need the targeted path or a base-matching owner resolver in a future v2 — noted for the next book.*
