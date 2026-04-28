# C01 DimReview — Post-Patch Plan — 2026-04-20

| Field | Value |
|---|---|
| Filename | dim-c01-post-patch-plan-20260420.md |
| Purpose | Plan for CC behaviour when Claude AI's full C01 dimension analysis + DIMREVIEW patches arrive |
| Trigger | Researcher direction 2026-04-20 evening: "keep this analysis and findings in mind … I am shortly going to hand the full analysis for dimensions to you, including the patch to update" |
| Carry-over context | Phase A analysis (`dim-c01-phase-a-incoming-analysis-20260420.md`) + pre-checks findings (DV-1..DV-5 embedded in `build_dimension_extract.py --bundle`) |
| Status | PENDING — awaiting Claude AI handoff of Phase B/C output |

---

## 1. What CC will receive

Expected artefacts from Claude AI (based on handoff kickoff + DimReview instruction v3.3):

- **Observations log** — Phase B + C content appended to `wa-dim-c01-observations-v{version}-20260420.md`
- **DIMREVIEW patch(es)** — one per target registry:
  - `PATCH-20260420-DIMREVIEW-C01-REG112-V1.json` (r112 mind, ~73 groups)
  - `PATCH-20260420-DIMREVIEW-C01-REG183-V1.json` (r183 heart, ~59 groups)
- **SD pointer additions** — may be embedded in the patches as `wa_session_research_flags` inserts (session_target='D'), or as a separate SDPOINTERS patch
- **Any new dimension-vocabulary candidates** — may be raised as SD pointers citing OT-DBR-015 (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied carry-over from Phase A)

---

## 2. CC execution sequence (when patch arrives)

### 2.1 Pre-apply

1. Read observations log — record Phase B QA summary + Phase C rationale
2. Run pre-apply validation on the patch(es): schema-valid JSON, expected registry scope, operation types (`update` on `wa_dimension_index`), expected count (~132 rows across both patches)
3. Backup live DB: `backups/bible_research_pre_C01_dimreview_{timestamp}.db`

### 2.2 Apply

1. Apply each DIMREVIEW patch via `scripts/apply_session_patch.py`
2. Record outcomes (rows updated, any errors)
3. Apply any SDPOINTERS patch if separate

### 2.3 Post-apply — free-flight checks (action (a) from researcher direction)

This is where CC identifies issues and alignments **to be added to the pre-handoff pipeline for next time**. Checks to run:

| Check | Purpose | Action if fails |
|---|---|---|
| **FF-1 Vocabulary-vintage consistency** | All r112 + r183 groups now use current §7.7 vocabulary | If any still on legacy → report as correction candidate |
| **FF-2 Manual-override lock resolution** | Were DR-8 locked groups unlocked cleanly? Count `manual_override=1` pre vs post | If locked groups remain with legacy labels → flag |
| **FF-3 `dominant_subject` completeness** | No literal `'NONE'` values introduced | Any 'NONE' → flag OT-DBR-012 |
| **FF-4 dimension_confidence stamp** | All updated groups carry `CLAUDE_AI` confidence (not KEYWORD_*/UNCLASSIFIED/NULL) | Mixed confidence → flag |
| **FF-5 DR status transition** | `word_registry.dim_review_status` for r112 and r183 → Complete; `dim_review_version` stamped | Missing → apply CC-authored update |
| **FF-6 Cross-registry coherence** | For any group whose `mti_term_id` has a canonical row in a non-target registry, does the new dimension align with the canonical? | Divergence → record as note, not failure (divergence can be informative per Phase A findings) |
| **FF-7 SD pointer increment** | Any new `wa_session_research_flags` rows (session_target='D') correctly numbered post-existing pointers (existing: 37 in C01) | Misnumbered → flag |
| **FF-8 Legacy-label residue check** | Programme-wide — did the patch accidentally touch legacy-label rows in non-target registries? | Any unintended change → flag STOP |
| **FF-9 Coverage verification replay** | §6.5 coverage check — 132 target groups accounted for in patch ops | Gap → flag |
| **FF-10 Q-COV question linkage** | If r112/r183 have terms with `VERSE_EVIDENCE_*` flags, are the linked Q-COV questions referenced in any new SD pointers or findings? | Missing → note for next pre-check enhancement |

**Output:** a post-apply verification report `outputs/reports/wa-dim-C01-post-apply-verification-20260420.md` capturing FF-1..FF-10 results.

### 2.4 Fold learnings into pre-handoff pipeline

Any FF check that surfaces a recurring issue becomes a **DV-6+ pre-check** to be added to `build_dimension_extract.py --bundle` before the next DimReview handoff. Candidates already anticipated:

- **DV-6** (from FF-8) — cross-registry referential integrity: ensure a DIMREVIEW patch does not unintentionally affect groups outside the declared target scope
- **DV-7** (from FF-4) — confidence-stamp audit: warn if target registries have mixed dimension_confidence values going in
- **DV-8** (from FF-6) — cross-registry coherence: summarise how each target's dimensions will relate to canonical rows in other registries, so Claude AI has this visible pre-analysis

### 2.5 OT-DBR-015 status update

After patch applies, update OT-DBR-015:
- r112 + r183 now on current vocabulary → 2 of 6 C01 registries remediated
- 4 of 6 C01 registries still on legacy vocabulary → **cluster is mixed-vintage**
- This naturally raises the question in §3 below

---

## 3. Researcher question (b) — rerun C01 to align the cluster?

**Situation post-patch:** C01 will have 2 registries on current §7.7 vocabulary and 4 on legacy. This is exactly the mixed-vintage state OT-DBR-015 is about.

**Options for the researcher:**

- **Option 1 — Accept mixed-vintage state.** Move on to other clusters. Document that C01 is heterogeneous. Any future cross-cluster analysis navigates both vocabularies.

- **Option 2 — Full C01 realignment now.** Re-review r182 Soul, r184 spirit, r185 flesh, r211 being under current vocabulary. Effort: ~137 groups (61 + 37 + 30 + 15 minus the 2 in r211 already on current). Same Phase A/B/C workflow — but Phase A is already done via the current session, so essentially Phase B + C.

- **Option 3 — Hybrid.** Do a **label-mapping patch** on the 4 already-Complete registries using the Phase A mapping table (§3.5 of the incoming analysis, OT-DBR-015 mapping column). Mechanical where mapping is clean; flag the 3 unmapped legacy labels (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied) for per-group researcher decision. Effort: perhaps ½ day of mechanical mapping + researcher-only decision on the ~40 groups with unmapped legacy labels.

**CC analysis:**

- **Option 1** is fastest but permanently degrades cross-cluster analytical coherence. Not recommended.
- **Option 2** is thorough but burns analytical cycles on registries that have already been analysed — risk of re-deciding something previously settled. Expensive.
- **Option 3** is the pragmatic middle — preserves existing analytical decisions where the label maps cleanly, escalates only the genuinely-unmapped cases to researcher. The 3 unmapped labels (Spiritual/God-ward 25, Identity/Selfhood 9, Somatic/Embodied 6 — 40 groups) are real analytical questions regardless of realignment, so they surface naturally.

**CC recommendation: Option 3.** Can be driven by a dedicated script (`scripts/align_c01_legacy_to_current.py`) that:
1. Reads wa_dimension_index for the 4 Complete registries
2. Applies the OT-DBR-015 mapping table mechanically where mapping is clean
3. Lists the unmapped-legacy-label rows for researcher decision
4. Produces a DIMREVIEW patch for the clean mappings

This is analogous to the M29 coverage-flag rename — a programme-wide data migration with a small per-case decision residue.

**Decision deferred to researcher** — awaiting direction after reviewing the C01 Phase B/C patch.

---

## 4. What CC must NOT do

- Do not apply the DIMREVIEW patch without running the pre-apply validation (§2.1)
- Do not assume all FF checks will pass — report failures transparently even if the overall pattern is clean
- Do not proactively rerun C01 (Option 2 or 3) without explicit researcher approval
- Do not mutate other clusters' dimensions as a side-effect of C01 work

---

## 5. Items to carry across context compaction

If this conversation compacts before the patch arrives, the following must survive:

1. OT-DBR-015 (vocabulary vintage, 265/275 C01 legacy) — in OT register
2. OT-DBR-016 (rootfamily over-reports) — in OT register
3. FF-1..FF-10 checks — in this file (§2.3)
4. Candidate DV-6..DV-8 pre-checks — in this file (§2.4)
5. Option 1/2/3 decision pending — in this file (§3)
6. Bundle generator standardised (`--bundle` mode) — in `build_dimension_extract.py`

Saved via memory: `project_dim_c01_post_patch_plan.md` (in user memory directory).

---

*Standing plan — in force until Claude AI's C01 Phase B/C output arrives.*
