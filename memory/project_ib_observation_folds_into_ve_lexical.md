---
name: project_ib_observation_folds_into_ve_lexical
description: "PLAN (2026-07-01): ib_observation is transitional — once the new ve-lexical (dimensions-as-items) is confirmed, its 81 entries convert INTO the new ve-lexical (re-keyed on verse_context_id) and the ib_observation table then ceases to exist. Do NOT invest in joining/backfilling the two stores — that link is being dropped."
metadata: 
  node_type: memory
  type: project
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Researcher plan, 2026-07-01.** The dimension observations (D1–D13, currently in the `ib_observation` table, 81 rows) are **not** to stay in a separate table. The direction is to make the **dimension part of the ve-lexical**: each dimension expressed as `ve_lexical` items — **span→span pairs** (direction always 1→2) and **events** (processes/actions) — per the researcher comments captured in `Workflow/methodology/wa-observation-dimensions-extract-v1-20260701.md` §5.

**Sequence:** (1) confirm the new ve-lexical item model that carries the dimensions → (2) **convert** the current `ib_observation` rows into that new ve-lexical form (keyed on `verse_context_id`, at the correct term grain) → (3) **retire** `ib_observation` (it ceases to exist).

**Do NOT** backfill/dedup or FK-link `ib_observation`↔`ve_lexical` as two stores — that work is **moot**, the table is being folded in and dropped. The only linkage that matters going forward: `ve_lexical` → `verse_context` → master `verse` index (sound; `ib_observation.origin_verse_id` also → `verse.id`).

**Dimension→item mapping already partly exists** (see the extract doc §6.4): D2 source→term ≈ `cause`+`cause_clause`+`from-source`; D4 ≈ `operation`/`how`; D5 ≈ `object`; D6 qualifier ≈ `compound` role + `intensity`; D14 package-reference ≈ existing `isolable`/`read_with` adjacency field. Two overlaps to converge first: `cause`(17)↔`cause_clause`(22), `how`(18)↔`operation`(27).

Related: [[project_verse_fanout_operating_model]] [[project_ve_lexical_normalisation_and_groundings]] [[feedback_verse_raw_data_must_pull_all_study_evidence]].
