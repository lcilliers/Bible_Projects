# M01 (Fear) — V3_2 pre-evaluation

> **READ-ONLY pre-flight · wa-cluster-M01-v3_2-preeval-v1-20260608.md · CC.** Sanctioned V3_2 assessment (`scripts/_assess_cluster_v3_2_preeval.py`). Assembles the whole cluster in focus and reports readiness for the V3_2 roll-up (rollup instruction v3_2 §3 / audit PRE-L2). No DB writes.

**Cluster:** M01 — *Fear, Dread and Terror* · bucket `NAMED` · status **Analysis Completed (Terms Added)** · v6

## A · Term layer

- Active terms: **83**
- By language: Greek 18, Hebrew 65
- By status: `extracted` 78, `extracted_thin` 5
- OWNER-type terms (per inventory): 83

## B · Verse layer (`verse_context` for this cluster's terms)

- verse_context rows: **1026** · relevant **945** · set-aside 81
- with AI `analysis_note` (existing L3-layer meaning): **949** · with `keywords`: 0 · in a VCG (`group_id`): 945

## C · Existing analysis — re-run inputs (V3_2 respects + refines these)

- existing **VCGs** (verse_context_group used): 38
- existing **sub-groups** (`cluster_subgroup`): 8
- existing **characteristics**: 7
- existing **findings** (`cluster_finding`): **805**
  - by `finding_status`: `finding` 543, `cluster_synthesis` 147, `silent` 115
  - by `finding_type` (new M55 field): `(null/new)` 805

## D · STEP-sense + morphology readiness (for L1 mechanical)

- terms with a parsed STEP sense-set (`parsed_meaning_id`): **83 / 83**
- stem-conditioned multi-sense terms (≥2 binyanim in sense_text): **10** (the within-stem-select residue goes to L2 per discipline 2)
- **morphology captured?** `wa_verse_records.morph`/`stem` populated: 0 rows system-wide → **PENDING** (run in L1).
- **`wa_meaning_sense.stem_label` populated?** 0 → **PENDING** (run in L1).
- **`is_homonym` populated?** 0 → **PENDING** (filter pass).

## E · V3_2 L1 fields — population state (expect empty pre-run)

- `verse_context.step_meaning_applied` populated: 0
- `verse_context.sense_id` populated: 0
- `verse_context.sense_multiplicity` populated: 0
- `verse_context.pole` populated: 0
- `verse_context.pole_is_metaphor` populated: 0 *(DEFAULT 0 on all rows; counting non-default)*
- `verse_context.residue_flag` populated: 0 *(DEFAULT 0 on all rows; counting non-default)*

## F · Readiness verdict

- **Schema:** V3_2 (3.29.0) — L1 fields present and empty, ready to populate. ✅
- **Foundation:** term layer deduped (2026-06-08); STEP sense-sets present. ✅
- **To run in L1 (population, not yet done):** capture per-verse morphology → `morph`/`stem`; parse `stem_label`; `is_homonym` filter. ⏳
- **Existing analysis is a re-run input** (prior VCGs/sub-groups/findings above) — V3_2 evaluates + refines, does not discard (discipline 6 / L2–L5 dynamic d).
- **Next V3_2 step:** L1 verse establishment (mechanical STEP-sense application) for this cluster.

*This pre-evaluation is read-only and records state only; it makes no analytical decisions.*