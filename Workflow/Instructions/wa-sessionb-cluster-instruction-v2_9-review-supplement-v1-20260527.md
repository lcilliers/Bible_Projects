# Supplement to v2_9 review — DB retirement scope + VCG analytics findings

**Date:** 2026-05-27
**Parent:** `wa-sessionb-cluster-instruction-v2_9-review-v1-20260527.md`
**Purpose:** answer two follow-up questions from the researcher and **revise the parent review's VCG conclusion** based on the analytics data.

---

## §1. DB components retiring or stalling under v3_0 (your first question)

If v3_0 follows the slim brief in the parent review, the retirement scope is **narrow** — bounded to the VCG family plus a couple of incidental columns.

### §1.1 No new writes (becomes legacy/read-only for new clusters)

| Component | Current active rows | Status under v3_0 |
|---|---:|---|
| `verse_context_group` (table) | 3,262 | Frozen — no new VCG rows created for new clusters |
| `vcg_term` (table) | 4,154 | Frozen — same |
| `verse_context.group_id` (column) | 35,114 populated | Frozen on new verses; legacy values preserved |

That's the entire VCG family. The closed clusters' VCG rows stay in the DB (they back Session C navigation and remain queryable); they just stop being authored.

### §1.2 Columns whose only use was VCG-related polysemy

Two columns currently used by only 2 rows out of 74:

| Column | Rows using it | Status under v3_0 |
|---|---:|---|
| `characteristic_subgroup.is_partial` | 2 | Effectively unused; could keep for safety or drop |
| `characteristic_subgroup.partial_register_note` | 2 | Same |

These tracked the case where a sub-group serves a characteristic only in some VCGs (the SPLIT_SUBGROUP pattern). Without VCGs, the pattern can't be expressed in this form — but its analytical purpose can be served by writing the register-note into `cluster_subgroup.notes` instead.

### §1.3 Everything else still actively written under v3_0

The bulk of the schema continues unchanged:

- `cluster`, `cluster_subgroup`, `mti_term_subgroup` (packet structure)
- `verse_context` (most columns including `analysis_note`, `keywords`, `cluster_subgroup_id`, `is_anchor`)
- `characteristic`, `characteristic_subgroup`, `cluster_observation`
- `cluster_finding`
- `mti_terms`, `wa_verse_records`, `wa_term_inventory`
- `wa_obs_question_catalogue`, `wa_quality_flag_types`, `wa_data_quality_flags`
- `wa_session_research_flags`
- `engine_run_log`, `prose_section`, `session_d_*`, etc.

### §1.4 Already-legacy (not new)

Pre-cluster-pivot tables that aren't written by current pipeline anyway:

- `wa_session_b_dimensions` — pre-v2_0 dimensions work
- `wa_session_b_findings` — pre-v2_0 Session B findings (the inherited-findings fold in Phase 10 reads these)
- `wa_finding_entity_links` — pre-cluster (287 active rows)

These remain readable for backward compatibility (Phase 10 fold for legacy clusters) but no v2_9 or v3_0 process writes to them.

### §1.5 Summary answer

**Drop VCGs, drop nothing else of substance.** The retirement scope is one table family. Everything else in the schema continues to serve v3_0 unchanged.

---

## §2. VCG analytics findings — and the correction they force

Full report: `Workflow/Clusters/wa-vcg-analytics-v1-20260527.md`

### §2.1 Programme-wide counts

| Metric | Value |
|---|---:|
| Clusters with active VCGs | 48 (including FLAG, T2) |
| Total active VCG rows | **2,849** |
| Total active is_relevant verses in VCGs | 31,663 |
| Singleton VCGs (exactly 1 verse) | 528 (**18.5%**) |
| Orphan VCGs (no active verses) | 413 |
| Anchors set inside VCGs | 3,726 |

### §2.2 Description distinctness is real

Average Jaccard similarity between a VCG's description and its parent sub-group's `core_description`: **0.02**. 91.7% of VCGs have Jaccard < 0.10.

**Interpretation:** VCG descriptions are NOT duplicates of sub-group descriptions. They say analytically distinct things. The descriptions hold genuine within-sub-group texture.

### §2.3 The citation pattern — and the correction it forces

§4 of the analytics report — the test of whether VCGs paid Phase 9 rent — shows a sharply bimodal distribution:

**Clusters where VCGs were heavily cited in `cluster_finding`:**

| Cluster | Citation rate | When it ran |
|---|---:|---|
| M03 | **100%** | Closed under v2_0+ Phase 9 |
| M08 | **100%** | Closed under v2_6+ |
| M02 | **89%** | Closed under v2_0+ |
| M04 | **91%** | Closed v2_6 with full pipeline |
| M01 | **82%** | Closed under v2_0+ |
| M10c | **81%** | Closed 2026-05-26 under v2_8 |
| M26 | **77%** | Closed under v2_0+ |
| M39 | **91%** | Closed under v2_0+ |
| M07 | 50% | Closed under v2_6 |
| M09 | 67% | Closed under v2_6 |

**Clusters where VCGs were rarely cited:**

| Cluster | Citation rate | Why |
|---|---:|---|
| M11 | 0% | Phase 9 never ran (parked) |
| M12-M46 (Not started) | mostly 0% | Phase 9 never ran |
| M10 | 1% | Closed with `char_structure='aspect_based'` — single characteristic, didn't cite VCGs |
| M15, M5 | 2% | Closed with pre-v2_0 method that didn't cite VCG codes |
| FLAG, T2 | 2-3% | Special-purpose, not analytically active |

### §2.4 The correction to my earlier review

In the parent review (`wa-sessionb-cluster-instruction-v2_9-review-v1-20260527.md` §2.1), I wrote:

> *"Phase 9 fires at characteristic scope. Each AI batch is one characteristic; verses are pulled by `cluster_subgroup → characteristic_subgroup → characteristic`. The VCG layer is loaded into the structural input as navigation labels, but Phase 9 prompts do not require VCG-scoped reasoning... VCG-as-third-layer adds no Phase 9 reasoning."*

**This was wrong.** The data shows the opposite for clusters that actually ran the full v2_0+ pipeline:

- 10 clusters ran the full pipeline (M01, M02, M03, M04, M07, M08, M09, M10c, M26, M39)
- Their **average VCG citation rate is ~83%**
- VCGs are routinely referenced by code inside characteristic-scope findings (e.g. "in M10c-A-VCG-07 the corpse-contact register evidences X")
- The VCG layer **is** analytically active — it provides the verse-cohort references the AI uses to ground Phase 9 prompts at characteristic scope

The headline "13%" citation rate in the analytics report is dragged down by 27 not-yet-processed clusters (their VCGs were created by a pre-cluster-pivot process and Phase 9 never ran), 2 closed clusters that ran older methods (M10 aspect-based; M15 pre-v2_0), and FLAG/T2.

### §2.5 The revised view of VCG value

VCGs serve **three** functions, not the one I originally credited them with:

1. **Sub-group-internal grouping** (the design intent — verses within a sub-group that cohere by shared analytical sub-axis). This is what Phase 7 produces.
2. **Anchor selection** (every VCG has one anchor verse — the primary evidence for the VCG's sub-register). 3,726 anchors set at this granularity.
3. **Citation hooks for Phase 9** (AI references VCG codes when writing findings at characteristic scope to point to the specific sub-cohort that evidences a claim). **This is the function I missed.**

Functions 2 and 3 mean dropping VCGs has real cost:

- **Anchor selection** would need to move up to sub-group level — but sub-groups can be 90+ verses (M10c-A had 93V); selecting one anchor for a 90-verse sub-group is harder than selecting one for an 8-verse VCG. The fine-grained anchor signal would be lost.
- **Phase 9 citation hooks** would need a replacement — perhaps citing specific verses directly rather than VCG codes. That's heavier text-wise and less abstract.

### §2.6 Where the VCG layer IS costly

The analytics also surface real overhead:

- **528 singleton VCGs (18.5%)** — single-verse VCGs that can't internally cluster. Each is functionally a per-verse note dressed up as a group.
- **413 orphan VCGs** — VCG rows with zero active is_relevant verses. Pure structural debris.
- **Description writing cost** — for clusters with 50+ VCGs (M05 123, M22 80, M23 158, M24 94, M26 79), authoring distinct descriptions for each is real Phase 7 AI cost.

---

## §3. Revised v3_0 direction (or held-open option)

In light of §2, the original "drop VCGs" recommendation in the parent review needs softening. Three options now visible:

### Option A — Keep VCGs as v3_0 has them (minimal change)

Accept that the VCG layer is paying rent in the current pipeline. v3_0 still consolidates Phases 3 + 5 + 7 into one AI design session, but the session produces both sub-groups AND VCGs in one pass (the design output is two nested levels of grouping, not three sequential AI sessions). Saves AI session cycles without dropping the layer.

**Net effect on the parent review's slim sketch:** Phase B produces a 2-level packet structure (sub-group + within-sub-group cohorts). The terminology can change but the structure stays.

### Option B — Drop VCGs entirely (parent review's original sketch)

Sub-group becomes the only grouping level. Phase 7 disappears. Anchor selection at sub-group level (lossier). Phase 9 citations refer to verses directly rather than VCG codes (heavier text but more grounded).

**Net effect:** ~25% reduction in per-cluster AI cost. Loss of cited sub-group texture. Closed clusters keep their VCGs as legacy reads (Session C navigation preserved).

### Option C — Keep VCGs but tighten the rules

Stay with the v2_9 model but add a discipline: **no singleton VCGs unless researcher-approved.** A VCG must contain ≥2 verses. The 528 singletons would be absorbed into their nearest peer VCG or expanded to absorbed-into-a-richer-group during Phase 7 design.

**Net effect:** ~18% fewer VCGs (528 fewer); description quality up; cluster overhead down without losing the layer.

### Recommendation matrix

| If you value most | Pick |
|---|---|
| Minimal change to a working pipeline | Option A or C |
| Maximum slim-down and willing to lose VCG-grain citation | Option B |
| Cleaner data without restructuring | Option C |

The analytics suggest Option B is **more aggressive than the data justified.** Options A and C honor the principle "the verse meaning and context is the data" by preserving the structural layer where the AI is currently citing the data; they don't sacrifice analytical resolution for slimming.

---

## §4. Other suggested revisions to the parent review

If we step back from the VCG question, the other slimming findings in the parent review remain valid:

- §2.2 Phase 3 mechanical sanity-check (still good)
- §2.4 Phase 5 + Phase 6 merge into design+apply (still good)
- §2.5 Phase 8 / 8.5 / 8.7 conditional collapse (still good)
- §2.6 Phase 10 / 11 / 12 closure trio (still good)
- §2.7 §2 sub-rules consolidation (still good)
- §2.8 Two new principles as numbered rules in §2 (still good)
- §3 Reduce reads of cluster meaning corpus (still good — Phases 3 + 5 can collapse to one read; if VCGs kept, Phase 7 produces nested groupings from that same read)

**Net slim estimate (revised):**

| | v2_9 | v3_0 (Option A — keep VCGs, merge design steps) | v3_0 (Option B — drop VCGs) |
|---|---:|---:|---:|
| Phase sections | 14 | 6-7 | 5 |
| AI sessions per cluster | 4-6 | 3 | 3 |
| Cluster meaning corpus reads | 3-4 | 2 (1 for design, 1 for analytics) | 1 (design) + N (analytics) |
| Grouping levels analytically used | 3 | 3 | 2 |

The big savings come from Phase 3/5/7 merging into one AI design session — whether or not VCGs are kept.

---

## §5. Open for your decision

1. **VCG question (Options A / B / C from §3 above).** This is the biggest remaining call. The data softens my original "drop VCGs" recommendation.
2. **Other slim moves from parent review §8** — all still valid regardless of the VCG decision.
3. **Whether v3_0 publishes as a draft now** (to be tested on M12 or against M11's un-park), or after more reflection.

---

*Supplement v1 — 2026-05-27. Read alongside the parent review.*
