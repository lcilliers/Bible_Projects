# WA Cluster M15 — Findings Record Directive

**File:** WA-cluster-M15-dir-findings-record-v1-20260512.md
**Date:** 2026-05-12
**Directive type:** Cluster-process — findings recording (§11.5 pattern B, `wa-directive-instruction-v1_4-20260506`)
**Previous outputs:** WA-M15-consolidated-findings-v1-20260511 (Parts 1–4); wa-obslog-M15-phase8-v1/v2-20260511
**Patch instruction version:** wa-patch-instruction-v2_11-20260507

---

## DIRECTIVE ID

DIR-20260512-001

---

## MOTIVATION

The M15 cluster (Wisdom, Understanding, Knowledge and Related Inner Capacities) has completed a full Phase 8 catalogue pass. The 189-prompt T0–T7 catalogue was applied to each of 8 active sub-groups (M15-A through M15-H), plus a structural characterisation pass for BOUNDARY, producing one finding per (prompt × sub-group) cell plus cluster-level synthesis findings.

The analytical record is held in four source documents:

- `WA-M15-consolidated-findings-v1-20260511-part1.md` — T0 (12 prompts) and T1 (24 prompts)
- `WA-M15-consolidated-findings-v1-20260511-part2-T2.md` — T2 (31 prompts)
- `WA-M15-consolidated-findings-v1-20260511-part3-T3-T4.md` — T3 (33 prompts) and T4 (24 prompts)
- `WA-M15-consolidated-findings-v1-20260511-part4-T5-T7.md` — T5 (21 prompts), T6 (24 prompts), T7 (20 prompts)

Catalogue version: `wa-obs-catalogue-tiered-v2-20260511` (generated 2026-05-11T18:56:01Z, schema 3.21.0, 189 active prompts).

These findings need to be recorded in `cluster_finding` so they are queryable, linked to `wa_obs_question_catalogue.obs_id`, and available for cross-cluster synthesis in Session D.

**Path determination:** If `cluster_finding` already exists (established during M06 processing per DIR-20260506-002), CC proceeds with Path A (UPSERT). If `cluster_finding` does not exist in the current schema, CC halts and produces a schema enablement directive (§10) before proceeding.

---

## SCOPE

**Table:** `cluster_finding`

**Cluster code:** `M15`

**Sub-group codes (active, with full catalogue pass):**

| Code | Label |
|---|---|
| `M15-A` | Wisdom as holistic inner character and orientation |
| `M15-B` | Understanding as inner perceptive faculty |
| `M15-C` | Knowledge as inner content and covenantal knowing |
| `M15-D` | Discernment and practical judgment |
| `M15-E` | Deliberative planning, counsel, and purposive intent |
| `M15-F` | Meditative and reflective inner activity |
| `M15-G` | Inner thought-content — the mind's formed thoughts |
| `M15-H` | Logos — the word as inner-being engagement |
| `BOUNDARY` | Functional-mediating infrastructure (structural characterisation only — not full 189-prompt pass per §11 BOUNDARY treatment) |

**Source files:** The four parts of the consolidated findings document listed under MOTIVATION.

**Operation:** UPSERT one row per (prompt × scope) into `cluster_finding`.

**Parsing rules:**

1. **Prompt identification:** Each finding block is headed by `#### T#.#.# —` (e.g. `#### T3.1.1 —`). The `question_code` is the `T#.#.#` string. Map to `obs_id` via `wa_obs_question_catalogue.question_code`.

2. **Sub-group scope markers:** Within each prompt block, sub-group findings are marked `**[X — Label]**` where X is the sub-group letter (A–H) or `[CLUSTER]` for cluster-level synthesis findings. Map X to `cluster_subgroup_id` via the sub-group codes table above. `[CLUSTER]` maps to a cluster-level scope row (no sub-group id).

3. **Outcome codes → `finding_status`:**
   - `E —` (evidenced) → `finding`
   - `S —` (silent) → `silent`
   - `G —` (gap requiring external investigation) → `gap`
   - `**[CLUSTER]**` or `**[Cluster-level finding]**` → `cluster_synthesis`

4. **`finding_text`:** Set to the verbatim prose paragraph following the outcome code marker. Include the verse reference(s) embedded in the text. Do not truncate.

5. **`source_file`:** Set to the part-N filename from which the row was parsed (e.g. `WA-M15-consolidated-findings-v1-20260511-part3-T3-T4.md`).

6. **`catalogue_version`:** Set to `v2-20260511` (from the catalogue header: generated 2026-05-11T18:56:01Z, schema 3.21.0).

7. **Cells not separately addressed:** Where a prompt block provides only a cluster-level synthesis finding and no individual sub-group entries, the sub-group rows receive the structural stub: `[Sub-group not separately addressed in source — see cluster-level finding for this prompt]` with `finding_status='finding'`.

8. **BOUNDARY rows:** BOUNDARY structural characterisation is recorded under T1.2.1 only (per §11 BOUNDARY treatment). All other (prompt × BOUNDARY) cells receive: `[BOUNDARY — structural characterisation note only; full catalogue pass not applicable per §11 BOUNDARY treatment rule]` with `finding_status='finding'`.

**Two-step load is acceptable:**
- Step 1: Structural loader — creates one row per (189 prompts × 9 sub-groups including BOUNDARY + 189 cluster-level rows) with status defaults and stub text.
- Step 2: Full-text loader — parses the consolidated findings document and updates `finding_text` and `finding_status` for every authored marker.

**Stray verse correction — prerequisite (FLAG-M15-006):**
Before executing this directive, CC must confirm that FLAG-M15-006 has been executed: 5 stray H2803G cha.shav verses (vr_ids 54610, 54611, 54612, 54613, 54626) assigned to M15-E-VCG05. If not yet executed, execute it before loading findings.

---

## OUTCOME REQUIRED

1. **Row count:** One row in `cluster_finding` per (question_code × scope) marker present in the source documents. Exact count confirmed in completion confirmation query. Approximate expectation: 189 prompts × 8 active sub-groups = 1,512 sub-group rows + up to 189 cluster-level rows + BOUNDARY stubs = approximately 1,700–1,900 total rows for cluster_code = 'M15'.

2. **`finding_status` distribution (approximate):**
   - `finding` (E-coded responses and unaddressed stubs): majority
   - `silent` (S-coded): significant minority across all sub-groups
   - `gap` (G-coded): approximately 15–20 rows (LXX gap flags M15-002 through M15-015 parked; T6.6/T6.7 CC queries parked)
   - `cluster_synthesis` (CLUSTER-coded): minimum 10 rows (CF-01 through CF-10) plus additional cluster-level observations in T6 and T7

3. **`finding_text`:** Verbatim prose from source documents. No truncation. Verse references preserved in text body.

4. **`source_file`:** Correctly assigned to the part-N filename from which each row was parsed.

5. **`wa_session_b_findings` row count:** UNCHANGED. No writes to `wa_session_b_findings`. Confirmed in completion confirmation query.

6. **FLAG-M15-006 confirmed executed before findings load.**

---

## COMPLETION CONFIRMATION

CC provides the following after execution:

**1. Row count by status:**
```sql
SELECT finding_status, COUNT(*)
FROM cluster_finding
WHERE cluster_code = 'M15'
GROUP BY finding_status;
```

**2. Sample rows (3 representative):**
Provide 3 rows with `question_code`, `cluster_subgroup_id` (or NULL for cluster-level), `finding_status`, and first 100 characters of `finding_text`.

**3. Gap list — all gap rows:**
Every row where `finding_status = 'gap'`, with `question_code`, scope (sub-group code or CLUSTER), and first 80 characters of `finding_text`. This list is required for Phase 10 gap resolution planning.

**4. wa_session_b_findings unchanged:**
```sql
SELECT COUNT(*)
FROM wa_session_b_findings
WHERE registry_id IN (
  SELECT DISTINCT wr.id
  FROM word_registry wr
  JOIN mti_terms mt ON mt.strongs_number = wr.strongs_number
  WHERE mt.cluster_code = 'M15'
);
```
Confirm count is unchanged from pre-directive state.

**5. FLAG-M15-006 confirmation:**
```sql
SELECT vr.id, vr.reference, vc.cluster_subgroup_id, vcg.group_code
FROM verse_records vr
JOIN verse_context vc ON vc.verse_record_id = vr.id
JOIN verse_context_group vcg ON vc.group_id = vcg.id
WHERE vr.id IN (54610, 54611, 54612, 54613, 54626)
  AND vcg.mti_term_id = (SELECT id FROM mti_terms WHERE strongs_number = 'H2803G');
```
Confirm all 5 verse_context rows are assigned to M15-E-VCG05.

---

## NOTES

**Cluster status:** Remains `Analysis - In Progress` through Phase 9. Status transition to `Analysis Completed` occurs after Phase 10 verification confirms clean state.

**LXX gap rows (FLAGS M15-002 through M15-015):** 8 gap rows (one per active sub-group at T7.1.8) remain as `finding_status = 'gap'` pending a dedicated Logos Bible Software research session. Not resolvable by CC DB query.

**T6.6/T6.7 gap rows (FLAGS M15-008, M15-010, M15-012, M15-014):** Gap rows at T6.6.1 and T6.7.1 for M15-F, M15-G, M15-H, and BOUNDARY require CC to run shared verse anchor and dimensional sharing queries once findings data is loaded. These are Phase 10 gap-resolution candidates.

**Directive sequence for M15:** This is the findings-record directive for M15. Previous M15-specific directives include sub-group assignment and group-verse mapping directives referenced in the comprehensive report (DIR-20260508-002). Per-cluster sequence numbering; this directive uses date-based identifier DIR-20260512-001.
