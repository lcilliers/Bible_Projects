# Directive DIR-20260515-001 — M01 Phase 3 term transfer to M24, M03, and BOUNDARY

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-global-rules-all-v2-20260427
> Scope: cross-cluster (M01 → M24, M01 → M03, M01 internal BOUNDARY)
> Produced date: 2026-05-15

---

## DIRECTIVE ID

`DIR-20260515-001`

---

## MOTIVATION

Phase 3 characteristic debate for cluster M01 (Fear, Dread and Terror) has determined that 12 of the cluster's 94 terms do not carry the fear/dread/alarm characteristic. They carry either (a) the inner experience of suffering and affliction under pressure — belonging in M24 (Weakness, Vulnerability and Suffering), or (b) burning grief/anguish and staggering — belonging in M03 (Grief, Sorrow and Mourning). A further 3 terms carry the characteristic of cognitive perplexity/bewilderment — distinct from fear and not currently homed in any programme cluster — and are to be held in M01-BOUNDARY pending a future programme-level cluster assignment decision.

The transfer must be executed before M01 Phase 4 sub-group assignment proceeds, so that the sub-group structure is built on the correct reduced term set and no distress/suffering vocabulary contaminates the fear analytical pass. All verse_context rows, verse_context_group rows, and cluster-level associations travel with the terms to their destination clusters.

Analytical basis: wa-obslog-M01-cluster-m01-v1-20260515.md, Phase 3 sections — characteristic debate Step 3 (T1 testing), Step 4 (cluster split analysis), and transfer decisions confirmed by researcher 2026-05-15.

---

## SCOPE

**Tables affected:**
- `mti_terms` — `cluster_code` update for 12 terms; `cluster_subgroup_id` confirmation (all 12 are currently NULL — no sub-group assigned yet, none to clear)
- `verse_context` — `cluster_subgroup_id` is NULL for all affected rows (pre-Phase-4 state); no sub-group field to update. The `mti_term_id` link travels with the term automatically; no row-level update needed to verse_context unless CC identifies a cluster_code denormalisation field in the schema that must be updated.
- `verse_context_group` — all VCG rows owned by the transferred terms travel to the destination cluster. CC must confirm whether `verse_context_group` has a `cluster_code` field that requires updating, or whether the VCG ownership is resolved purely through `mti_terms.cluster_code`. If a `cluster_code` column exists on `verse_context_group`, update it for all VCG rows whose `mti_term_id` is in the transfer set.
- `cluster_subgroup` — no rows yet exist for M01 sub-groups (Phase 4 not yet run). No action needed on this table for transferred terms.

**Term set — transfer to M24 (Weakness, Vulnerability and Suffering):**

| Strong's | Transliteration | Gloss | mti_id (from report) |
|---|---|---|---|
| G2347 | thlipsis | pressure | 21 |
| G4730 | stenochoria | hardship | 51 |
| H4867 | mish.bar | wave | 4814 |
| H5076 | ne.dud | tossing | 5572 |
| H1742 | dav.va | faint | 6385 |
| H8513 | te.la.ah | hardship | 2494 |
| H7661 | sha.vats | agony | 240 |
| H6125 | a.qah | pressure | 5157 |
| H4164 | mu.tsaq | constraint | 156 |
| H6115 | o.tser | coercion | 6210 |

**Term set — transfer to M03 (Grief, Sorrow and Mourning):**

| Strong's | Transliteration | Gloss | mti_id (from report) |
|---|---|---|---|
| H6330 | pu.qah | staggering | 198 |
| H2750 | cho.ri | burning | 1552 |

**Note on mti_id values:** the mti_id values above are drawn from the comprehensive report `wa-cluster-M01-comprehensive-v3-20260515.md`. CC must verify each mti_id by querying `SELECT id, strongs_number, cluster_code FROM mti_terms WHERE strongs_number IN (...)` before updating, to confirm the IDs match and that the current `cluster_code = 'M01'` in each case. Do not update any row where `cluster_code ≠ 'M01'`.

**Term set — assign to M01-BOUNDARY (remain in M01, cluster_code unchanged):**

| Strong's | Transliteration | Gloss | mti_id (from report) | Action |
|---|---|---|---|---|
| G1280 | diaporeō | be perplexed | 4481 | Mark for BOUNDARY — see Outcome below |
| G0639 | aporeō | be perplexed | 4482 | Mark for BOUNDARY — see Outcome below |
| H7672 | she.vash | be perplexed | 4483 | Mark for BOUNDARY — see Outcome below |

---

## OUTCOME REQUIRED

### 1. M24 transfers (10 terms)

For each of the 10 terms in the M24 transfer set:
- `mti_terms.cluster_code` updated from `'M01'` → `'M24'`
- `mti_terms.cluster_subgroup_id` remains NULL (M24 has no sub-groups yet; this is correct)
- If `verse_context_group` has a `cluster_code` column: all VCG rows where `mti_term_id` matches the transferred mti_id are updated to `cluster_code = 'M24'`
- If `verse_context` has a denormalised `cluster_code` column: update similarly
- No verse_context rows are deleted or set_aside-adjusted; they travel as-is

### 2. M03 transfers (2 terms)

For each of the 2 terms in the M03 transfer set:
- `mti_terms.cluster_code` updated from `'M01'` → `'M03'`
- `mti_terms.cluster_subgroup_id` remains NULL
- VCG rows updated as above if column exists

### 3. BOUNDARY terms (3 terms — remain in M01)

For diaporeō (G1280, mti_id=4481), aporeō (G0639, mti_id=4482), she.vash (H7672, mti_id=4483):
- `mti_terms.cluster_code` remains `'M01'` — no change
- `mti_terms.cluster_subgroup_id` remains NULL — they will be assigned to a BOUNDARY sub-group in DIR-20260515-002 (Phase 4 sub-group assignment directive)
- No verse_context or VCG changes at this stage

### 4. M01 post-transfer state

After execution:
- M01 term count (active, `status IN ('extracted','extracted_thin')`): 94 − 12 = **82 terms**
- M24 term count: prior count + 10
- M03 term count: prior count + 2
- The 3 BOUNDARY terms remain counted within M01's 82

### 5. No other tables touched

- ❌ Do not modify `verse_context.is_relevant`, `verse_context.is_set_aside`, or any analytical field
- ❌ Do not create or modify `cluster_subgroup` rows — that is Phase 4
- ❌ Do not touch `cluster_finding` rows — none exist yet for M01
- ❌ Do not modify `wa_session_b_findings` rows

---

## COMPLETION CONFIRMATION

CC must return all of the following before this directive is closed:

**1. Pre-execution verification (run before any updates):**
```sql
SELECT id, strongs_number, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE strongs_number IN (
  'G2347','G4730','H4867','H5076','H1742','H8513','H7661','H6125','H4164','H6115',
  'H6330','H2750',
  'G1280','G0639','H7672'
)
ORDER BY strongs_number;
```
Expected: 15 rows, all with `cluster_code = 'M01'`, all with `cluster_subgroup_id = NULL`.
If any row has `cluster_code ≠ 'M01'` — halt and report; do not proceed with that term.

**2. Post-execution M01 term count:**
```sql
SELECT COUNT(*) FROM mti_terms mt
WHERE mt.cluster_code = 'M01'
AND mt.status IN ('extracted','extracted_thin');
```
Expected: **82**

**3. Post-execution M24 term count:**
```sql
SELECT COUNT(*) FROM mti_terms mt
WHERE mt.cluster_code = 'M24'
AND mt.status IN ('extracted','extracted_thin');
```
Expected: prior M24 count + 10. State both the prior count and the post-execution count.

**4. Post-execution M03 term count:**
```sql
SELECT COUNT(*) FROM mti_terms mt
WHERE mt.cluster_code = 'M03'
AND mt.status IN ('extracted','extracted_thin');
```
Expected: prior M03 count + 2. State both counts.

**5. Confirmation of transferred terms:**
```sql
SELECT strongs_number, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE strongs_number IN (
  'G2347','G4730','H4867','H5076','H1742','H8513','H7661','H6125','H4164','H6115',
  'H6330','H2750'
)
ORDER BY cluster_code, strongs_number;
```
Expected: 10 rows with `cluster_code = 'M24'`; 2 rows with `cluster_code = 'M03'`; all `cluster_subgroup_id = NULL`.

**6. Confirmation of BOUNDARY terms (unchanged):**
```sql
SELECT strongs_number, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE strongs_number IN ('G1280','G0639','H7672');
```
Expected: 3 rows, all `cluster_code = 'M01'`, all `cluster_subgroup_id = NULL`.

**7. VCG schema check and update confirmation:**
CC must report: does `verse_context_group` have a `cluster_code` column?
- If YES: report count of VCG rows updated for the 12 transferred terms.
- If NO: confirm no VCG action required and state the basis (ownership resolved through mti_terms).

**8. verse_context schema check:**
CC must report: does `verse_context` have a denormalised `cluster_code` column?
- If YES: report count of verse_context rows updated.
- If NO: confirm no verse_context cluster_code action required.

---

*DIR-20260515-001 | wa-global-dir-001-m01-term-transfer-v1-20260515.md | Cross-cluster transfer: M01 → M24 (10 terms), M01 → M03 (2 terms), M01 BOUNDARY hold (3 terms) | Analytical basis: wa-obslog-M01-cluster-m01-v1-20260515.md Phase 3 | Next: DIR-20260515-002 Phase 4 sub-group assignment*
