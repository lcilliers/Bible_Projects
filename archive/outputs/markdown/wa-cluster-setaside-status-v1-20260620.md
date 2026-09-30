# Cluster set-aside (out-of-scope verses) — status & mechanism · 2026-06-20

> Researcher direction: non-inner-being verses must be **properly set aside in the DB** (a disposition), not
> only filtered in the extract. This records the mechanism, what's done, and the per-cluster status.

## Two distinct things (clarification)

- **T2 co-term noise filter** (extract-level, `build_ve_lexical_extract.py`): drops *T2-cluster co-terms* with no
  qualifier bearing (seed/sow/hand/name). These are reference words, never analysed; the filter just keeps them
  out of the payload. **It does NOT touch focus-term homonyms.**
- **Out-of-scope set-aside** (DB-level, this work): *focus-term* occurrences whose sense is a homonym/literal
  with no inner-being content (che.vel cord, tsur besiege, pid disaster). These pollute the cluster and must be
  **set aside in the DB**.

## DB set-aside mechanism (per M01 precedent)

- **Fully-contaminated sub-entry** (every occurrence is the homonym) → `mti_terms.cluster_code = NULL` +
  `exclusion_reason` (the sub-entry leaves the cluster entirely; engine skips NULL-cluster).
- **Mixed-sense sub-entry** (some occurrences valid) → occurrence-level `verse_context.set_aside_reason` only,
  preserving the valid occurrences.
- The extract now **honours both**: it skips `set_aside_reason` occurrences and `cluster_code IS NULL` co-terms,
  and the verse-set excludes set-aside-only anchors. Reversible throughout.

## Per-cluster status

| Cluster | out-of-scope list | DB set-aside | notes |
|---|---|---|---|
| **M01** Fear | (set aside during analysis) | **done** | H2119B crawl, H3724B/C/D henna/pitch/village, H3070 — already `cluster_code=NULL`+reason |
| **M02** Anger | `wa-m02-tsur-excl-proposal` | **done 2026-06-20** | tsur H6696B (32 occ, 0/32 anger) → `cluster_code=NULL`; 28 were already set aside, term-NULL caught all 32. M02 active focus → **671** (matches proposal 703→671) |
| **M03** Grief | `wa-m03-ve-out-of-scope` (69 occ) | **done 2026-06-20** | 4 fully-homonym sub-entries NULL'd (che.vel, cha.val, tsir, ne.ha.mah); 2 mixed (ma.ror 2/3, tsar 2/31) occurrence-level. Active focus 760→**691** |
| **M04** Joy | not characterised | — (113 pre-existing) | M04 had **113 pre-existing** set-asides the old extract wrongly included — now honoured (1103→999 verses) |
| **M05–M47** | not characterised | per characterise pass | the out-of-scope list is an analyst judgement produced **during** each cluster's characterise pass (GR-PROG-007). Can't be pre-set-aside without it. Any pre-existing set-asides are now honoured by the extract |

## Key finding

There is a layer of **pre-existing DB set-asides** (set_aside_reason populated in an earlier era) that the extract
was **not honouring** — so they leaked into extracts. The extract fix now honours them programme-wide, so as each
cluster is characterised its set-aside list is applied (NULL/ set_aside) and the extract reflects it automatically.

## Reversal

M02 tsur: `UPDATE mti_terms SET cluster_code='M02' WHERE strongs_number='H6696B'`. M03: clear `set_aside_reason`
+ restore `cluster_code='M03'` on the affected sub-entries (`_apply_m03_out_of_scope_setaside` rows).
