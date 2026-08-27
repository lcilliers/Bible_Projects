# Directive DIR-20260516-001 — M01 Phase 4 term transfer + status transition

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-sessionb-cluster-instruction-v2_0-20260515 §7
> Scope: cross-cluster (M01 → M02 Anger; M01 → M03 Grief; M01 → M10 Guilt; M01 → M20 Doubt; M01 → M24 Weakness) + M01 cluster status transition
> Produced date: 2026-05-16

---

## DIRECTIVE ID

`DIR-20260516-001`

---

## MOTIVATION

Phase 3 cluster constitution debate for M01 (Fear, Dread and Terror) is complete. Source documents:

- `Sessions/Session_Clusters/M01/wa-M01-constitution-debate-v1-20260516.md` (main debate; 80 of 94 terms verdicted)
- `Sessions/Session_Clusters/M01/wa-cluster-M01-constitution-focused-rereadgreek-v1-20260516.md` (addendum; 10 Greek terms re-read after first-pass context overflow)

AI's analytical verdicts:

- **13 terms TRANSFER out** of M01 to their characteristic-appropriate clusters — meaning corpora evidence non-fear inner-being content (cognitive perplexity → M20 Doubt; constrictive suffering → M24 Weakness; burning anger → M02 Anger; grief-faintness/restlessness → M03 Grief; conscience-staggering → M10 Guilt).
- **12 terms BOUNDARY** — analytical questions or empty corpora; remain in M01 for Phase 5 sub-group placement (no Phase 4 DB action required for BOUNDARY per v2_0 §7.4).
- **69 terms STAY** in M01 (includes 3 terms — e.mah, tromos, a.yom — that AI did not explicitly verdict but are uncontroversially core M01 fear vocabulary; default verdict STAYS).

Per v2_0 §2.5 (directive packaging discipline), this directive bundles all 13 transfer operations plus the `Data - In Progress` → `Analysis - In Progress` status transition into a single transactional directive.

---

## SCOPE

**Tables affected:**

- `mti_terms` — 13 `cluster_code` UPDATEs (Op A1 through Op A13)
- `cluster` — 1 `status` + `last_updated_date` UPDATE on row `cluster_code='M01'` (Op B)

**Schema notes** (per v2_0 §A1):

- `verse_context` has no `cluster_code` column — verses for transferred terms automatically resolve to the new cluster via `mti_term_id → mti_terms.cluster_code`.
- `verse_context_group` has no `cluster_code` column — VCG ownership resolves via `vcg_term → mti_terms.cluster_code`.
- No `vcg_term`, `verse_context`, or `verse_context_group` rows require updates.

**Pre-condition:** `cluster.status = 'Data - In Progress'` for M01; `mti_terms.cluster_code = 'M01'` for all 13 transfer mti_ids; all 5 destination clusters exist.

**Verified at preflight (2026-05-16):** ✓ all 13 mti_ids in M01 with correct Strong's; ✓ all 5 destinations exist (M02 Not started, M03 Not started, M10 Not started, M20 Analysis Completed, M24 Not started); ✓ M01 status `Data - In Progress`.

---

## OUTCOME REQUIRED

### Operation A — Term transfers (13 ops, run in mti_id order)

| Op | mti_id | Strong's | Translit | M01 → | Rationale (AI debate) |
|---|---:|---|---|---|---|
| A1 | 21 | G2347 | thlipsis | **M24 Weakness** | 42-verse corpus: suffering-pressure-tribulation, no fear |
| A2 | 51 | G4730 | stenochoria | **M24 Weakness** | constrictive suffering-hardship |
| A3 | 156 | H4164 | mu.tsaq | **M24 Weakness** | constrictive inner pressure |
| A4 | 162 | H4712 | me.tsar | **M24 Weakness** | constrictive anguish, not fear |
| A5 | 198 | H6330 | pu.qah | **M10 Guilt** | conscience-staggering at potential bloodshed (1Sa 25:31) |
| A6 | 1552 | H2750 | cho.ri | **M02 Anger** | burning anger in all 5 verses |
| A7 | 2494 | H8513 | te.la.ah | **M24 Weakness** | hardship-burden-weariness |
| A8 | 4481 | G1280 | diaporeō | **M20 Doubt** | cognitive bewilderment, no fear content |
| A9 | 4482 | G0639 | aporeō | **M20 Doubt** | cognitive bewilderment, no fear content |
| A10 | 4483 | H7672 | she.vash | **M20 Doubt** | cognitive bewilderment, no fear content |
| A11 | 5572 | H5076 | ne.dud | **M03 Grief** | suffering-induced restlessness |
| A12 | 6210 | H6115 | o.tser | **M24 Weakness** | coercive pressure/suffering |
| A13 | 6385 | H1742 | dav.va | **M03 Grief** | exhausted faintness under grief |

SQL pattern per op:
```sql
UPDATE mti_terms SET cluster_code='{destination}', last_changed='{utc_iso}'
WHERE id={mti_id} AND cluster_code='M01' AND COALESCE(delete_flagged,0)=0;
```

### Operation B — Cluster status transition

```sql
UPDATE cluster SET status='Analysis - In Progress', last_updated_date='{utc_iso}'
WHERE cluster_code='M01' AND status='Data - In Progress';
```

### Operation N — Not applicable (this is Op B above; v2_0 §2.6 forbids standalone status-bump)

---

## COMPLETION CONFIRMATION

**1. M01 term count post-transfer:**
```sql
SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0;
```
Expected: **81** (94 pre − 13 transfers).

**2. Destination term counts (pre vs post):**
```sql
SELECT cluster_code, COUNT(*) FROM mti_terms WHERE cluster_code IN ('M02','M03','M10','M20','M24') AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0 GROUP BY cluster_code;
```
Expected deltas: M02 +1, M03 +2, M10 +1, M20 +3, M24 +6.

**3. Each transferred mti has new cluster_code:**
```sql
SELECT id, strongs_number, cluster_code FROM mti_terms
WHERE id IN (21,51,156,162,198,1552,2494,4481,4482,4483,5572,6210,6385)
ORDER BY id;
```
Expected: all 13 rows with cluster_code matching the Op A table above.

**4. M01 cluster status:**
```sql
SELECT status, last_updated_date FROM cluster WHERE cluster_code='M01';
```
Expected: `'Analysis - In Progress'` with last_updated_date matching the directive apply timestamp.

**5. Verse / VCG carry-along (no direct updates; verify auto-resolution):**
```sql
-- Verses now resolving to destinations
SELECT mt.cluster_code, COUNT(DISTINCT vc.id) AS vc_count
FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.id IN (21,51,156,162,198,1552,2494,4481,4482,4483,5572,6210,6385)
  AND COALESCE(vc.delete_flagged,0)=0
GROUP BY mt.cluster_code;
```
Expected: vc rows now grouped under the destination cluster codes.

```sql
-- VCGs now resolving to destinations
SELECT mt.cluster_code, COUNT(DISTINCT vcg.id) AS vcg_count
FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id=vcg.id
JOIN mti_terms mt ON mt.id=vt.mti_term_id
WHERE mt.id IN (21,51,156,162,198,1552,2494,4481,4482,4483,5572,6210,6385)
  AND COALESCE(vcg.delete_flagged,0)=0
GROUP BY mt.cluster_code;
```

**6. wa_session_b_findings unchanged:**
No rows in this table are inserted, updated, or deleted by this directive.

**7. Application report:** `Sessions/Session_Clusters/M01/WA-M01-dir-001-term-transfer-applied-v1-20260516.md`.

---

## NOTES

1. **Sub-group placements** are NOT created by this directive. M01-A/B/.../H/BOUNDARY sub-groups will be created in Phase 6 by the subgroup-assign directive after AI's Phase 5 sub-group formation completes.

2. **BOUNDARY terms** (12) remain in M01 with no Phase 4 action — their `mti_term_subgroup` placement (to `M01-BOUNDARY`) happens in Phase 6.

3. **Destination cluster status** — most destinations are `Not started` (M02, M03, M10, M24). M20 is `Analysis Completed`. Adding terms into M20 does not automatically reopen it; researcher decides whether to revisit M20's analysis with the 3 new terms (aporeō, diaporeō, she.vash). The cluster_code transfer is purely structural.

4. **3 STAYS terms not verdicted by AI** (e.mah mti=284, tromos mti=308, a.yom mti=1722) take default STAYS — uncontroversial core M01 fear vocabulary; no Phase 4 action required. Confirmed in applied report.

5. **mo.rah / mo.ra (H4172A mti=270 / H4172B mti=271)** share an identical 11-verse set across the same references. Flagged as a database-level dedup question (likely OT-DBR-009 family); not addressed by this directive.

---

*DIR-20260516-001 | wa-global-dir-001-M01-term-transfer-v1-20260516.md | Phase 4 (v2_0 methodology) | Source: wa-M01-constitution-debate-v1-20260516.md + addendum | Next: AI Phase 5 sub-group formation*
