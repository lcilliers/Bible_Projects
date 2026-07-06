# Psalms — Step (d) Gate-1 completeness & Step (e) validation

> Completes the per-book corrective pipeline for **Psalms** (steps a–e). Follows the role-reassessment completion (`wa-psalms-step2-role-completion-report-20260706.md`). Date: 2026-07-06. Backup: `backups/bible_research.pre-psalms-gate1-*.db`.

## What Step (d) does
For every **characteristic** span in Psalms (3,810 spans, the reviewed inner-being cut from Step 2), ensure the chain is complete and indexed: **the term is recorded → the verse occurrence is a verse-record → the links are intact.** Scope is characteristic spans only (not qualifier/standalone) — this is the reviewed IB selection, not the whole vocabulary, so it does not flood the curated tables.

No STEP round-trip was needed: Psalms occurrences already exist in the master index (`verse_span_index`) with morphology, and the verse text is in `verse`. Records were assembled from that in-DB data (more reliable than STEP, which has the 60-cap truncation issue). Full programme-wide STEP onboarding of the newly registered terms remains a separate **global** action, deferred under the by-book discipline (recorded as debt, below).

## The gap that was found (and what it reveals)

| Gap | Count |
|---|---:|
| characteristic strongs **not registered** in `mti_terms` | 97 |
| characteristic spans with **no verse-record** | 1,081 |
| verse-records present but **missing `verse_span_id`/`mti_term_id` link** | 149 |

The missing terms were **the core vocabulary of the inner life** — the strongest confirmation yet that the registry was an incomplete index:

- **H8605 prayer (təphillah) ×31**, H0835 blessedness (ʼashrê) ×26, H5641 to hide [your face] ×23, H7646 to satisfy ×23, H5800 to forsake ×21, **H3468 salvation (yeshaʿ) ×20**, H5826 to help ×17, H8668 deliverance ×13, H5341 to keep/watch ×13, H5046 to tell ×12, H2555 violence ×11, H4784 to rebel ×10, H0974 to test ×9, **H2451 wisdom (ḥokmah) ×7**, H2898 goodness ×7, H5937 to exult ×7, H6817 to cry ×5, H6419 to pray (palal) ×4, H6165 to long for (the deer panting) ×2 … and 78 more.

### A second, deeper finding — over-deletion in the registry
Of the 97 missing terms, **17 existed in `mti_terms` but every row was delete-flagged** — no active term at all. These include **prayer (H8605), wisdom (H2451), to pray (H6419), desire (H3970), goodness (H2898)**. They had been entirely removed from the active inner-being registry — almost certainly casualties of the unresolved **OT-DBR-009** dedup, which over-deleted. This is a real integrity defect the corrective pass surfaced, not just an indexing gap.

## What was applied (reversible; all stamped `gate1-psalms-2026`)

1. **79 new terms registered** into `mti_terms` (thin records: strongs_number, transliteration, gloss, language; `status='extracted_thin'`, `anchor_note='gate1-psalms-2026'`), assembled from `lexicon`.
2. **17 wrongly-deleted terms reactivated** — exactly the row each new verse-record references was set `status='extracted_thin'`, `delete_flagged=0`, `anchor_note='gate1-psalms-2026-reactivated'`. Because no active row existed for these strongs, this yields **exactly one active term each** (no active-duplicate created).
3. **H6199 (Psa 102:17 "the prayer of the destitute", ʿarʿar)** — had no lexicon gloss so was skipped in the main pass, then registered by sense (`gloss='destitute'`) and its record created.
4. **1,081 verse-records created** for characteristic spans (linked by the bypass FKs `verse_id` + `verse_span_id` + `mti_term_id`; legacy `file_id` points to one dedicated sentinel `wa_file_index` row `GATE1-PSALMS-2026` — never joined for data, per `reference_file_index_legacy_use_bypass_fks`).
5. **149 broken links repaired** on existing characteristic-span verse-records.

## Step (e) — full-integrity validation (`_probe_psalms_gate1_validate_v1_20260706.py`)

| Check | Result |
|---|---|
| gate1 records with unresolved `verse_id` / `verse_span_id` / `mti_term_id` | 0 / 0 / 0 ✓ |
| gate1 records with NULL `verse_text` | 0 ✓ |
| gate1 records linked to a delete-flagged term | 0 ✓ |
| gate1 terms with >1 active row (duplicate) | 0 ✓ |
| characteristic spans with no verse-record (forward) | 0 ✓ |
| **completeness probe: unregistered strongs / spans w/o record / broken links** | **0 / 0 / 0 ✓** |

**RESULT: ALL PASS.** All 3,810 Psalms characteristic spans now have a registered term, a complete verse-record, and intact forward/backward indexed links.

## Debt recorded (not skipped — deferred by design)
- **Full programme-wide STEP onboarding** of the 79+17+1 = 97 terms (all-book occurrences, meanings, related terms). Only the Psalms occurrences were completed here, per by-book discipline. When later books are processed, their occurrences of these terms complete then; a full onboarding can also be run globally once the by-book pass concludes.
- **OT-DBR-009** (mti_terms dedup) remains the root cause of the 17 over-deletions — flagged again here as materially affecting study integrity.

## Psalms — pipeline status
| Step | State |
|---|---|
| (a) scope: one book | ✓ Psalms |
| (b) reading units confirmed + linkages | ✓ chapter = reading unit; `verse_span_id` FK + indexes |
| (c) role reassessed | ✓ 150/150 |
| (d) Gate-1 completeness | ✓ 0 gaps |
| (e) full-integrity validation | ✓ ALL PASS |

**Psalms is complete.** Next book follows the same pipeline, in original working order.

*Filed 2026-07-06. Loaders: `_apply_psalms_gate1_completeness_v1_20260706.py`, `_apply_psalms_gate1_reactivate_v1_20260706.py`. Probes: `_probe_psalms_gate1_completeness_v1_20260706.py`, `_probe_psalms_gate1_validate_v1_20260706.py`. All figures reproducible from the DB.*
