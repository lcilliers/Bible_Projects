# M05 VCG deep-dive — why 2% citation? (and what it reveals about the VCG inventory programme-wide)

**Date:** 2026-05-27
**Source:** investigation of M05 prompted by the 2% citation rate flagged in `wa-vcg-analytics-v1-20260527.md`

---

## §1. The headline finding

**M05's 123 VCGs are not Phase 7 design output.** They are pre-cluster-pivot artefacts that travelled into M05 when the cluster's terms were anchored to the new term-cluster system in 2026-05-04. M05 was closed under a sub-group-scoped Phase 9 that didn't cite VCG codes by design. The 2% citation rate is the natural result, not a defect.

More broadly: **89% of the programme's active VCG rows are legacy pre-cluster-pivot artefacts**, and they are uniformly low-cited. Only 339 VCGs (~10%) are Phase 7 design output under v2_0+ — and those ARE cited.

---

## §2. The data — two eras of VCGs

Active VCG inventory classified by code-format:

| Era | What it is | # VCGs | # cited | Citation rate | Singletons | Orphans |
|---|---|---:|---:|---:|---:|---:|
| **Era 1** — legacy registry-format (e.g. `1633-001`, `536-001-a`) | Created by pre-cluster-pivot VC pipeline (≤2026-04); travelled into clusters via term-anchor migration | **2,825** | 148 | **5%** | 566 | 155 |
| **Era 2/3** — cluster-aware (`M07-A-VCG-01`, `M10c-A-VCG-07`) | Created by Phase 7 design under v2_0+ | **339** | 206 | **61%** | 5 | 3 |
| Other format | Edge cases (a few hyphenated variants) | 98 | 30 | 31% | 10 | 0 |
| **Total active** | | **3,262** | **384** | 12% | 581 | 158 |

The bimodal split is dramatic: Era 1 is barely-cited debris; Era 2/3 is analytically active.

---

## §3. Per-cluster: which clusters carry which era?

### §3.1 Phase 7 designed VCGs only (Era 2/3 pure)

These clusters had their VCGs designed in v2_0+ Phase 7 sessions:

| Cluster | Era 2/3 VCGs | Citation rate | Status |
|---|---:|---:|---|
| M03 | 25 | 100% | Analysis Completed |
| M04 | 47 | 91% | Analysis Completed |
| M08 | 24 | 100% | Analysis Completed |
| M10c | 26 | 81% | Analysis Completed |
| M10b | 36 | 25% | Analysis Completed |

These VCGs are paying rent — citation rate well above 50% on the clusters where the pipeline emphasised VCG-code citation (M03, M04, M08, M10c). M10b's lower rate reflects the Phase 9 synthesis citing verse-references directly rather than VCG codes for some characteristics.

### §3.2 Mixed (Era 2/3 + Era 1) — partial Phase 7 redesign

| Cluster | Era 2/3 | Era 1 | Citation rates |
|---|---:|---:|---|
| M01 | 36 (86%) | 2 (0%) | The 2 legacy VCGs never got re-designed; the 36 Phase 7 VCGs are cited heavily |
| M02 | 25 (96%) | 2 (0%) | Same pattern |
| M06 | 46 (50%) | 5 (40%) | Partial Phase 7 redesign; 5 Era 1 VCGs remain |
| M07 | 28 (50%) | 0 | All Era 2/3 |
| M09 | 21 (67%) | 0 | All Era 2/3 |
| M15 | 3 (0%) | 55 (2%) | Mostly legacy; closed under pre-v2_0 method |
| M20 | 12 (33%) | 14 (36%) | Half-Phase-7 redesign |
| M26 | 56 (71%) | 23 (91%) | Both eras cited; interesting hybrid |

### §3.3 Pure legacy (Era 1 only) — never had Phase 7 redesign

| Cluster | Era 1 VCGs | Citation rate | Notes |
|---|---:|---:|---|
| **M05** | 123 | **2%** | The cluster you flagged |
| M10 | 68 | 1% | char_structure='aspect_based'; Phase 9 used aspect markers, not VCGs |
| M11 | 26 | 0% | Phase 9 never ran (parked) |
| M12 | 58 | 2% | Not-started — Phase 9 never ran |
| M13 | 46 | 0% | Not-started |
| M14 | 53 | 0% | Not-started |
| M16-M46 (mostly) | various | mostly 0% | Not-started |
| FLAG | 188 | 2% | Holding pen, no analytics |
| T2 | 621 | 2% | Supplementary, not analytically active |

---

## §4. Why M05 specifically has 123 legacy VCGs

M05 is "Love, Compassion and Kindness" — one of the largest semantic territories in the programme (1,560 active is_relevant verses across ~50+ terms). Under the pre-cluster-pivot pipeline, the VCG system worked per-registry: each registry's verses were grouped into 1-N VCGs by sense. M05's 50+ terms were attached to many registries; when those terms anchored to M05 in 2026-05-04, every associated VCG row travelled along.

Sample of M05's VCG codes: `1633-001` (99V), `1633-003` (24V), `1009-001` (1V), `1402-001` (1V), `1582-001` (2V), `1641-001` (1V), `1642-001` (1V), `3164-001` (2V), `3980-001` (1V). The first prefix is the legacy `registry_id`. The structure tells the story — many singletons because the legacy pipeline created per-(registry, sense) VCGs whether or not they had multi-verse content.

When M05's Phase 9 ran, it fired at sub-group scope (`SUB-M05-A` through `SUB-M05-G`). The findings cite:
- Verse references (e.g. `Psa 86:5`)
- Sub-group codes (`M05-A`)
- Sometimes Strong's numbers (`H2617`)

Findings do **not** cite legacy VCG codes like `1633-001` because:
1. The codes are not human-meaningful (they're database IDs, not register names)
2. The AI session prompts at sub-group level — VCG codes weren't part of the citation vocabulary in pre-v2_6 Phase 9
3. Pre-v2_0 Phase 9 instruction didn't ask for VCG-grain citations

So M05's 123 VCGs hold analytical content (description-distinctness Jaccard 0.02 confirms they say new things) — but Phase 9 didn't consume that content because it wasn't designed to. The VCG descriptions are useful as legacy reading material; they don't appear in the structured findings.

---

## §5. M01's mixed pattern as the counter-example

M01 has 36 Era 2/3 VCGs (86% cited) + 2 Era 1 legacy VCGs (0% cited). What happened?

The 2 legacy VCGs (`105-001`, `1153-001`) were left over from pre-pivot processing of M01's pre-existing registry. When M01 closed under early v2_x, the Phase 7 design created 36 new cluster-aware VCGs covering most verses, but a tiny remainder of legacy VCGs persisted. The 36 new VCGs are cited routinely; the 2 legacy ones aren't.

This pattern is reassuring: Phase 7 design under v2_0+ produces VCGs that get cited; legacy VCGs that escape redesign do not. The system has been working as designed where Phase 7 ran.

---

## §6. Implications for the v3_0 decision

### §6.1 The earlier supplement softened "drop VCGs" — but the picture is more specific

In `wa-sessionb-cluster-instruction-v2_9-review-supplement-v1-20260527.md` §2.4 I corrected the parent review by saying "VCGs pay rent at ~83% in the current pipeline." That's still true but masks the legacy/Phase-7 split:

- **Era 2/3 (Phase 7 designed)** pays rent (~61% headline; 80-100% on the clusters that ran sub-group-scoped Phase 9 with VCG-code citation).
- **Era 1 (legacy)** doesn't pay rent (~5%) and won't unless re-designed.

### §6.2 The real question is bifurcated

Two separable decisions, not one:

**Decision 1 — what to do with the 2,825 Era 1 legacy VCGs?**

These are mostly in not-yet-processed clusters (M12-M46) plus a residue in some closed clusters plus FLAG/T2. Under v2_9, Phase 8's silent dissolution already targets exactly this case: when a cluster begins active processing, its inherited Era 1 VCGs are silently soft-deleted at Phase 8 (now silent under v2_9). Phase 7 then creates fresh Era 2/3 VCGs.

**This is already the design.** Era 1 VCGs are scheduled debris that clears as clusters process. No v3_0 work needed for this.

For closed clusters that retain Era 1 VCGs uncited (M05's 123, M15's 55, etc.) — these could be silently soft-deleted right now as cleanup, with no analytical loss. Optional housekeeping.

**Decision 2 — should new clusters under v3_0 create VCGs at all?**

This is the open question. The evidence:
- Era 2/3 VCGs pay rent where the pipeline emphasises VCG-code citation
- Phase 9 under v2_6+ fires at characteristic scope; VCG codes appear in citations but characteristic-scope findings can also cite verses directly
- The cost of Phase 7 design is real (one AI session per cluster)
- The benefit is anchor-grain texture and citation hooks

A defensible middle: **make Phase 7 conditional on sub-group size.** Sub-groups with >40 verses (e.g. M10c-A at 93V; M10-D at 145V) benefit from VCG-grain anchors and citation hooks. Sub-groups with ≤40 verses (single-cohort small groups) don't — Phase 9 can cite verses directly without VCG intermediation. This would cut Phase 7 work by half or more, retain the layer where it pays rent, drop it where it doesn't.

### §6.3 Practical M05-specific call

If you want M05's 123 unused VCG rows cleared up:

- Add `delete_flagged=1` to all 123 M05 VCG rows + their `vcg_term` links (silent soft-delete, same operation as v2_9 Phase 8)
- Optionally clear `verse_context.group_id` for the 1,560 M05 verses (NULLing the FK)
- Cluster status unchanged; cluster_finding rows preserved (they don't cite the VCGs anyway)

That's a one-script housekeeping move. Same applies to M15 (55 legacy VCGs), M12-M46 (the not-yet-started clusters carrying inherited VCG debt), FLAG, T2. Programme-wide it would soft-delete ~2,825 rows of debris.

I won't do this without your direction — it's a sizeable cleanup move.

---

## §7. Bottom line for your review

The 2% on M05 was not a bug in the methodology — it's the natural reading of legacy pre-pivot VCGs that were never re-designed and were never cited because Phase 9 didn't ask for VCG citations at the time M05 closed.

The bimodal split between Era 1 (debris) and Era 2/3 (active) clarifies the v3_0 decision:

- The "drop VCGs" question is really "drop VCG creation for new clusters under v3_0" — separable from clearing the existing legacy debris.
- The case for keeping VCG creation rests on the 61-100% citation rate of Era 2/3 VCGs in the clusters that ran the full pipeline.
- A size-conditional Phase 7 (only build VCGs for large sub-groups) is a middle path worth considering.

---

*M05 deep-dive v1 — 2026-05-27. Investigation of the 2% citation flag.*
