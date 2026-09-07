# M10 Stage B — gap review

**Date:** 2026-05-26
**Question:** With M10 having taken a different path through Stage B (tier-batched synthesis files + cluster_observation rows, not the standard 189 cluster-scope cluster_finding rows), what's missing that could pose problems later?

---

## What standard Stage B produces (per v2_8 §12.3)

For comparison — the M10b precedent (which closed clean):

- **189 `cluster_finding` rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`** (one per catalogue prompt at cluster scope)
- **One free-form prose appendix** as a standalone `*-appendix-*.md` artefact
- **All `cluster_observation` INTEGRATION_NOTE rows advanced `open` → `confirmed`** (the synthesis addresses them; CC marks them as resolved)
- **finding_citation rows derived from the cluster-scope findings** (the M52 extractor runs against both char-scope + cluster-scope cluster_finding rows)

## What M10 actually has

```
cluster.M10.status: 'Analysis - In Progress'

cluster_finding:
  char_scope finding:  3,820
  char_scope silent:     338
  cluster_synthesis:       0   ← gap

cluster_observation (58 open):
  CLUSTER_SYNTHESIS:      15 open (tier-batched synthesis content)
  TIER_READING_GUIDE:     27 open (per-tier reading guides for Session C)
  INTEGRATION_NOTE:        8 open  ← should be 'confirmed' after Stage B
  INTER_RELATIONSHIP:      7 open
  CROSS_CLUSTER_HANDOFF:   1 open

finding_citation (from char-scope rows only):
  verse:     13,091
  vcg:        8,561
  cross_char: 1,630
  strongs:      374
  cluster_synthesis_scope rows: 0  ← derived gap
```

---

## Gaps ranked by risk

### HIGH risk — likely to cause downstream problems

**1. M10 cannot reach `Analysis Completed` under §15.2.**
The closure pre-flight requires "every prompt × scope cell has a corresponding cluster_finding row." M10 is missing 189 cluster-scope cells. Status stays `Analysis - In Progress` indefinitely. Any tooling that filters clusters by `status='Analysis Completed'` excludes M10.

**2. Cross-cluster queries miss M10's synthesis layer.**
M10b/M01/M07/M08/M09 will all have 189 cluster-scope rows. A cross-cluster comparison query like `SELECT cluster_code, finding_text FROM cluster_finding WHERE characteristic_id IS NULL AND obs_id=<some T6 prompt>` returns rows for every cluster except M10. The structural-comparison work (especially Session D pointer-clustering and any inter-cluster prompt-by-prompt comparison) hits an M10-shaped hole.

**3. `finding_citation` cluster-scope coverage is 0 for M10.**
The M52 extractor runs against cluster_finding rows. Char-scope is covered (23,656 citations). Cluster-scope citations are zero because there are no cluster-scope rows. Queries like "what verses anchor M10's cluster-level synthesis on Psa 51:4" return nothing. The synthesis content exists in cluster_observation prose but isn't in the citation index.

**4. 8 open INTEGRATION_NOTE observations stuck `open`.**
Standard Stage B advances them to `confirmed`. M10's still-open count includes 8 INTEGRATION_NOTEs that the per-char Phase 9 may have addressed but never got formally closed. Any tooling that reports "open observations across the programme" tags M10 incorrectly.

### MEDIUM risk — depends on what downstream work needs

**5. T6 (Structural Relationships With Other Characteristics) cluster-scope answers don't exist as cluster_finding rows.**
Standard T6 cluster-scope rows name "M10 ↔ M02 (Anger) relationship" or "M10 ↔ M11 (Repentance) relationship" as discrete data points. M10's tier-batched approach captured these in the 15 CLUSTER_SYNTHESIS observations + 27 TIER_READING_GUIDE rows — text-rich but not queryable as standard T6 outputs. Session D's traditional cross-cluster pointer work joins against these; M10 doesn't fit the join shape.

**6. No standalone cluster-synthesis appendix file.**
Standard `*-appendix-*.md` is a 20–30 KB free-form prose artefact that Session C consumes as a thematic-overview input. M10 has the tier interrogation files + tier reading guides instead, distributed across multiple files. The content is there; the shape is different.

**7. Phase 11 validation script can't run cleanly.**
If you clone the M10b validator for M10 to check evidence-grounding, the row-count check fails (4,158 vs 4,347 expected), per-scope completeness fails (0 / 189 synthesis), observations-resolved fails (58 open). The validator will report M10 as "not ready for Phase 12 closure" — which is accurate but not what you want as a final state.

### LOW risk — cosmetic or content-equivalent

**8. The synthesis content itself is intact.** The 15 CLUSTER_SYNTHESIS + 27 TIER_READING_GUIDE cluster_observation rows + the tier interrogation files together carry substantial synthesis content — arguably richer than the standard 189-prompt format because the tier-batched approach surfaced cross-prompt patterns within each tier. The information is preserved; it's just shaped differently.

**9. TIER_READING_GUIDE is a non-standard observation_type.** Not formally in any constraint, just a new value the M10 work introduced. Harmless unless a future migration adds a CHECK constraint that doesn't include it.

---

## Paths forward (you decide)

### Option A — Run standard 189-prompt Stage B against M10 anyway
Build the same brief + per-prompt matrix as M10b's Stage B (a 22-char × 189 matrix is ~3× M10b's input size, plausible). Run one Claude AI synthesis session, load via the standard loader. M10 closes cleanly.

- **Cost:** one large AI synthesis session (M10b's was 901 KB input × 189 cluster-scope analyses).
- **Pro:** restores the standard shape; everything downstream works.
- **Con:** somewhat duplicative — the tier-batched outputs already cover the analytical ground. You'd be re-shaping rather than re-discovering.

### Option B — Synthesise from existing M10 artefacts
Build a converter that ingests the 15 CLUSTER_SYNTHESIS + 27 TIER_READING_GUIDE rows + the tier interrogation files and emits 189 cluster_finding cluster-scope rows. Semi-automated — some prompts will have direct matches in the existing content, others may need a fill-in pass.

- **Cost:** one builder script + one fill-in AI session for the gaps.
- **Pro:** preserves the M10-specific synthesis work; produces standard-shape outputs cheaply.
- **Con:** requires careful prompt-by-prompt audit ("does the existing content cover this prompt? if not, how do I fill?").

### Option C — Amend §15.2 closure to accept the tier-batched alternative
Update the Phase 11 validator + Phase 12 closure spec to treat M10's tier-batched-Stage-B shape as a valid closure path. M10 closes; future clusters using the standard path still work too.

- **Cost:** one instruction edit + one validator branch.
- **Pro:** lowest cost; respects that M10's path was a deliberate methodology pivot.
- **Con:** introduces a permanent dual-shape state in the programme. Downstream queries still hit the M10-shaped hole — closure cosmetics aside, problems 2/3/5 above persist.

### Option D — Leave M10 as-is, brace for Session C
Accept M10 won't close formally, Session C will follow a custom path, downstream cross-cluster tooling needs M10-specific branches.

- **Cost:** zero now; uncertain cost downstream every time M10 is touched.
- **Pro:** no work today.
- **Con:** each future tool may need an M10 branch. Compounds.

---

## Recommendation

**Option B**, with **Option C** as the fallback if B's content-coverage audit shows >50% of the 189 prompts have no direct match in the existing M10 artefacts.

Rationale: M10's tier-batched synthesis surfaced richer cross-prompt patterns than the standard 189-row format would have. Discarding that to re-do Stage B in the standard form (Option A) wastes the analytical work. But the structural cost of not having the 189 rows is real — problems 1–5 above will keep biting. Option B lets you keep the analytical content while restoring the standard shape so downstream tooling works uniformly.

The fill-in cost depends on how much of the 189-prompt catalogue is covered by the existing 15 + 27 observation rows. A first-pass audit (does each prompt have an analogous content block already?) takes 1–2 hours of script work; then the fill-in AI session for any uncovered prompts is bounded by how many remain.

---

## What I'd want to know before committing to a path

1. How important is **Phase 12 closure** for M10 in practical terms? If `status='Analysis Completed'` doesn't gate anything Session C cares about, the structural-shape problem matters more than the closure status.
2. How will **Session C** for M10 actually consume the tier-batched outputs? If it works directly from the tier interrogation files + observation rows, the lack of 189 cluster_finding rows is invisible to Session C — but other downstream consumers still see the hole.
3. Are there **specific downstream uses** you have in mind? (Programme-wide cluster comparison reports, cross-cluster T6 analysis, Session D pointer work, etc.) Each has different sensitivity to the gap.

---

*End of review. Marking up welcome — paths A/B/C/D + the open questions are all in-scope.*
