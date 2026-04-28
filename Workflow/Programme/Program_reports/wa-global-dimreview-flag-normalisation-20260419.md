# Bulk `dim_review_status` Flag Normalisation — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-dimreview-flag-normalisation-20260419.md |
| Operation | Quick-win bulk update — set `dim_review_status = 'Complete'` where review data demonstrably supports it |
| Trigger | Programme scan 2026-04-19 revealed status flag has lagged actual review state |
| Authorisation | "A - the quick win" 2026-04-19 |
| Pre-backup | `backups/bible_research_pre_dimreview_flag_20260419_165024.db` (167 MB) |
| Patch audit-trail | `Sessions/Patches/wa-global-dimreview-flag-normalisation-v1-20260419.json` |
| Status | **APPLIED successfully 2026-04-19T16:50:24Z** |

---

## Criteria (STRICT)

Registry is eligible if:

- `carry_forward = 1`
- `dim_review_status IS NULL OR != 'Complete'`
- Has ≥1 active row in `wa_dimension_index`
- **Zero** rows with `dimension_confidence IN ('KEYWORD_STRONG','KEYWORD_WEAK','ROOT_INFERRED','UNCLASSIFIED')`
- **Zero** rows with `dimension IS NULL`

SQL:

```sql
SELECT wr.no, wr.word, wr.cluster_assignment
FROM word_registry wr
LEFT JOIN wa_dimension_index wdi
  ON wdi.owning_registry_no = wr.no AND wdi.delete_flagged = 0
WHERE wr.carry_forward = 1
  AND (wr.dim_review_status IS NULL OR wr.dim_review_status != 'Complete')
GROUP BY wr.no
HAVING COUNT(wdi.id) > 0
   AND SUM(CASE WHEN wdi.dimension_confidence IN
     ('KEYWORD_STRONG','KEYWORD_WEAK','ROOT_INFERRED','UNCLASSIFIED')
       THEN 1 ELSE 0 END) = 0
   AND SUM(CASE WHEN wdi.dimension IS NULL THEN 1 ELSE 0 END) = 0;
```

---

## Registries Updated (8)

| no | word | cluster | dim_index rows | All CLAUDE_AI? |
|---:|---|---|---:|---|
| 18 | brokenness | C05 | 6 | Yes |
| 93 | intention | C02 | 2 | Yes |
| 113 | mourning | C05 | 11 | Yes |
| 182 | Soul | C01 | 61 | Yes |
| 184 | spirit | C01 | 37 | Yes |
| 185 | flesh | C01 | 30 | Yes |
| 188 | weeping | C05 | 10 | Yes |
| 211 | being | C01 | 15 | Yes |

---

## Outcome

- **Pre-update:** 34 registries at `dim_review_status = 'Complete'` (carry_forward=1)
- **Post-update:** 42 registries at Complete
- **Delta:** +8

Verified by re-running pilot on 3 of the 8:

- r18 brokenness: 26 → 25 findings (−1 hard-gate Path 4)
- r182 Soul: 73 → 72 findings (−1)
- r184 spirit: 253 → 252 findings (−1)

**Total programme-wide finding reduction: 8 Path 4 hard-gate items eliminated.**

---

## Honest Scope Assessment

The initial "quick win" framing suggested a 44% drop in Path 4 findings. **That estimate was wrong.** Actual impact is 8 findings out of ~6,076 Path 4 (~0.13%). The misestimate came from assuming the `dim_review_status = None` finding was frequent across all registries — which it is — but only 8 registries have the status flag lagging data that's already in review-complete state. The rest of the programme genuinely has residual automated-confidence dimensions that need Dimension Review work (not just flag normalisation).

**The real "review lag" story:**

- 34 registries had `dim_review_status = 'Complete'` pre-update
- 42 registries now have it
- **179 registries still at NULL** — of which:
  - 41 have 0 dim rows at all (VC not completed or excluded)
  - ~132 have partial review (mix of CLAUDE_AI + automated confidence — genuine review pending)
  - ~6 have dimensional data but `dim_review_status` set to something other than 'Complete'

So the honest programme-level picture is: Dimension Review is partially done across many clusters; bulk flag-flip is not a valid shortcut for the remaining 179. They need actual review work.

---

## Integrity Anomalies Discovered

During diagnostic, two registries surfaced with contradictory state — **both marked `dim_review_status='Complete'` AND `verse_context_status='Complete'` BUT zero underlying data:**

| no | word | dim rows | VC groups | Status |
|---:|---|---:|---:|---|
| 27 | consciousness | 0 | 0 | Both status flags Complete, no data |
| 129 | recognition | 0 | 0 | Same pattern |

These are **data integrity issues predating the DBR**. Neither was surfaced by the programme scan (they don't have findings to surface because they have no data to check). Recorded for Path 4 RD disposition:

- **Option 1:** Status flags were set prematurely; data is genuinely missing → reset flags to NULL; re-run Phase 1 and VC
- **Option 2:** Data was deleted post-hoc; flags are the historical record → retain flags, investigate what happened

Raised as **RD-DBR-004** in the RD accumulator (to be filed next obslog update).

---

## Files Written

1. `Sessions/Patches/wa-global-dimreview-flag-normalisation-v1-20260419.json` — audit-trail patch file
2. `backups/bible_research_pre_dimreview_flag_20260419_165024.db` — pre-update backup
3. Re-run pilot reports for 3 affected registries (r18, r182, r184) — findings verified −1 each
4. This report

---

## Next Logical Steps

With this quick win applied, the pre-process priority list is clearer:

1. **OT-DBR-001 (audit_word.py rewrite)** remains the highest-leverage unlocker — affects 86 registries with re-extraction needs
2. **Dimension Review on 104 registries** — the genuine analytical work; bulk flag-flip won't substitute. Recommend cluster-level batches starting with C01 (6 registries, 175 avg findings) and C20 (7 registries, 168 avg)
3. **Verse Context completion for 32 registries** — varies in scope
4. **RD disposition for r27 consciousness + r129 recognition** — data/state mismatch
5. **Session A extract generator** — unblocks Path 5 across all 213 registries

---

*End of bulk normalisation report — 2026-04-19*
