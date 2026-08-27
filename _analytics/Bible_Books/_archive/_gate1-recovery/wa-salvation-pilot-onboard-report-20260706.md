# Salvation onboarding pilot — completion report

> Pilot of the compliant engine-onboarding path for the 97 Gate-1 orphan terms (the first registry: new `salvation`, 4 terms). Validates the full chain end-to-end before the remaining 93. Date: 2026-07-06. Governing plan: `wa-gate1-registry-assignment-proposal-v2-20260706.md`.

## Result: ✅ SUCCESS — full chain built, integrity clean

**Terms onboarded** (registry `salvation`, id=220; file_id=248):

| Strong | Translit | Gloss | Verse-records |
|---|---|---|---|
| H3468 | yeshaʿ | salvation | 35 |
| H8668G | teshuʿah | deliverance/salvation (IB sense; H8668H "victory" excluded) | 21 |
| H4190 | moshaʿah | salvation | 1 |
| H5826 | ʿazar | to help | 77 |

## Chain built (established architecture, no bypass)

- `word_registry` "salvation" (REGISTER) → `wa_file_index` 248 → `wa_term_inventory` (4 OWNER) → `wa_verse_records` (**134, all occurrences programme-wide**, 100% scaffolded: term_inv_id + word_registry_fk + mti_term_id) → `verse_context` (121 created) → `mti_terms` (4, owned, `cluster_code='M38'`, status='extracted', delete_flagged=0).
- Meanings parsed (4), quality flags (8), WR-audit 19 PASS / 1 REVIEW (WR-09 testament_coverage — populated `OT_only`). Engine A12 integrity: **clean**.

## Procedure (the reusable recipe, curated gate)

1. `word_study_extract.py --word salvation --anchors H3468,H4190,H8668,H5826` → 85 terms (relatedNos cascade).
2. **Curated** the `terms` array to exactly the 4 intended (excludes the family cascade + the H8668H "victory" sense) → `220_salvation_step_data_20260706_curated.json`. **This is the contamination gate — NOT `--fetch-step`.**
3. `--mode=audit_word --registry=220 --extract-file=<curated>` (live).
4. Finishing fields (engine leaves NULL): `mti_terms.status='extracted'`, `delete_flagged=0`, `cluster_code='M38'`; `wa_term_inventory.term_owner_type='OWNER'`.
5. `_apply_create_vc_for_onboarded.py --registries 220` → 121 verse_context.
6. Integrity snapshot/compare gate around it all.

## Integrity compare (pre → post) — all deltas expected

```
mti_active            +4      verse_records_active  +134
inv_owner             +4      verse_context_active  +121
word_registry         +1      cluster M38        20 -> 24 (+4)
INVARIANTS: no new breach (dup_owner_strong=1 pre-existing; velex_orphan_vc unchanged)
```

## Two surfaced conditions (expected; no action now)

1. **`vr_out_of_corpus` +13** — 13 occurrences (12× H5826 "to help", 1× H8668G) fall in verses not in the `verse` measure-corpus (e.g. 2Sa 8:5, Deu 32:38, Jos 10:4). The occurrence is correctly recorded; it becomes analysable when that book is role-reassessed under the corrective pipeline. Accepted as pointers (the designed "2Sa 12:15 class").
2. **`vc_no_velex` +121** — ve-lexical **deliberately deferred**. Per the companion-file recommendation (Part A + B2), the fine `mti_term_subgroup` placement and ve-lexical/role reading are left to **M38 cluster rework**, where membership emerges from the read rather than being imputed. `cluster_code='M38'` is set now so the terms are attached and cannot be silently dropped.

## Deferred to M38 rework (not part of onboarding)
- `mti_term_subgroup` (fine subgroup: M38-A…G) — analytical, emerges from the read.
- ve-lexical generation + role for these terms' Psalms spans (Step 5 of the pipeline).

## Verdict
The compliant path works end-to-end and is safe. **Ready to proceed** with the remaining 93 terms across 52 registries, in integrity-gated batches (Group C existing registries next, then Group B promotions, then Group A light mti-reconciles).

## Artefacts
- Backup: `backups/bible_research.pre-salvation-onboard-20260706T150356Z.db`
- Curated extract: `research/discovery/220_salvation_step_data_20260706_curated.json`
- Snapshots: `outputs/integrity/snap-salvation-{pre,post}.json`

*Filed 2026-07-06.*
