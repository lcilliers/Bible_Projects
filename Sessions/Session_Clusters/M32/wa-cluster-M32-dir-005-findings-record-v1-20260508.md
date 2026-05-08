# wa-cluster-M32-dir-005-findings-record-v1-20260508

> Framework B Soul Word Analysis Programme — Cluster-Process Directive
> Cluster: M32 — Conscience and Self-Awareness
> Directive ID: DIR-20260508-004
> Version: v1 | Date: 2026-05-08
> Pattern: §11.5 Worked pattern B (cluster findings recording)
> Governing instruction: wa-directive-instruction-v1_4-20260506
> Catalogue: wa-obs-catalogue-tiered-v1-20260506

---

## Element 1 — MOTIVATION

The M32 (Conscience and Self-Awareness) catalogue pass has been completed under the Phase 8 redo (Session B, 2026-05-08). The pass applied all 189 prompts from `wa-obs-catalogue-tiered-v1-20260506` to sub-groups M32-A (Conscience) and M32-B (Self-Awareness / Inner Attention), plus structural characterisation notes for three BOUNDARY terms (kardiognōstēs, enthumeomai, autokatakritos). A cross-sub-group review pass identified five cluster-level findings. All findings were documented in four consolidated findings documents:

- `WA-M32-consolidated-findings-v1-20260508-part1.md` (T0–T1)
- `WA-M32-consolidated-findings-v1-20260508-part2-T2.md` (T2)
- `WA-M32-consolidated-findings-v1-20260508-part3-T3-T4.md` (T3–T4)
- `WA-M32-consolidated-findings-v1-20260508-part4-T5-T7.md` (T5–T7 + cluster-level findings)

These findings must now be recorded in `cluster_finding` so they are queryable, linked to `wa_obs_question_catalogue.obs_id`, and available for cross-cluster synthesis at Session D.

The obslog covering the full analytical session is: `wa-obslog-M32-conscience-self-awareness-v2-20260508.md`

---

## Element 2 — SCOPE

**Table:** `cluster_finding`

**Cluster:** `M32`

**Sub-groups in scope:**
- `M32-A` (Conscience) — terms G4894 suneidō (mti=454), G6083 sunoida (mti=2739)
- `M32-B` (Self-Awareness / Inner Attention) — term H7896K shit (mti=3578)
- `BOUNDARY` — terms G2589 kardiognōstēs (mti=599), G1760 enthumeomai (mti=3392), G0843 autokatakritos (mti=4848)

**Source files:** The four parts listed in Element 1. All files located at `/mnt/user-data/outputs/` and mirrored at `/home/claude/Sessions/Session_Clusters/M32/`.

**Operations:**

**Step A — Structural loader (first):**
Create one row per (189 prompts × 2 active sub-groups) + (189 prompts × cluster-level scope) + (3 BOUNDARY structural note rows) with default stub content where a full authored finding is not provided. Default stub text: `"Sub-group not separately addressed in source — see cluster-level finding at this prompt."` Default `finding_status = 'finding'`.

This ensures full coverage of the matrix before the full-text loader runs.

**Step B — Full-text loader (second):**
Parse the four source files and UPSERT `finding_text` and `finding_status` for every authored marker. Parsing rules:

- Header `**T#.#.#** — {prompt text}` identifies the `question_code` (map to `obs_id` in `wa_obs_question_catalogue` by matching `question_code` = `T#.#.#`)
- `**[A — Conscience]**` or `**[A]**` → scope = M32-A sub-group row
- `**[B — Self-Awareness / Inner Attention]**` or `**[B]**` → scope = M32-B sub-group row
- `**[CLUSTER]**` or `**[CLUSTER — ...]**` → scope = cluster-level synthesis row
- `**S — [scope]**` within a sub-group block → `finding_status = 'silent'`
- `**G — [scope]**` or `**G**` within a sub-group block → `finding_status = 'gap'`
- `**E**` (evidenced, no explicit marker — any response not marked S or G) → `finding_status = 'finding'`
- `**[CLUSTER — Finding N: ...]**` blocks in Part 4 → `finding_status = 'cluster_synthesis'`, scope = cluster-level
- BOUNDARY structural notes at T1.2.1 → three rows with `finding_status = 'finding'`, `cluster_subgroup_id = NULL` (BOUNDARY terms not assigned to a named sub-group), `boundary_term_mti` = the relevant mti id

**UPSERT key:** (`obs_id`, `cluster_code`, `cluster_subgroup_id`, `version`). If a row with that key already exists, update `finding_text`, `finding_status`, `source_file`. If not, insert.

**`source_file` field:** Set to the part-N filename (e.g. `WA-M32-consolidated-findings-v1-20260508-part1.md`) matching where the finding appears.

**`version` field:** Set to `1` for all rows in this directive.

**No writes to `wa_session_b_findings` or `wa_session_research_flags`.** These tables are registry-scope and must not be touched. Cluster findings live exclusively in `cluster_finding`.

**Cluster status:** remains `Analysis - In Progress` through Phase 9. Do not update `cluster.status`.

---

## Element 3 — OUTCOME REQUIRED

After both steps complete:

1. `cluster_finding` contains one row per authored (prompt × scope) marker in Parts 1–4, plus one row per structural loader stub for all unadressed cells.

2. Row count breakdown expected (approximate — CC to confirm actual from structural loader):
   - `finding` rows: the majority — E-coded sub-group findings + structural stubs
   - `silent` rows: numerous — M32-A and M32-B each have substantial S-coded responses (particularly across T2 body-link prompts, T5.1–T5.3 for M32-A, T4 gaps for M32-A)
   - `gap` rows: at minimum 12 rows — T6.6 (both sub-groups × T6.6.1–T6.6.3), T6.7 (both sub-groups × T6.7.1–T6.7.3), T7.1.8 (both sub-groups × T7.1.8 single prompt) = 12+ gap rows
   - `cluster_synthesis` rows: 5 — the five cluster-level findings in Part 4

3. `finding_text` set to the verbatim prose paragraph for each authored marker.

4. `source_file` set correctly per row (part1, part2, part3, or part4).

5. `wa_session_b_findings` row count for terms in M32 is **unchanged** from pre-directive state.

6. BOUNDARY: three rows present at T1.2.1 — one per BOUNDARY term (kardiognōstēs, enthumeomai, autokatakritos) with `cluster_subgroup_id = NULL` or equivalent BOUNDARY designation per schema.

---

## Element 4 — COMPLETION CONFIRMATION

CC is required to produce confirmation covering all of the following:

**4.1 Row counts by status:**
```sql
SELECT finding_status, COUNT(*)
FROM cluster_finding
WHERE cluster_code = 'M32'
GROUP BY finding_status;
```

**4.2 Three representative rows (sample):**
Produce three rows showing `question_code`, `cluster_subgroup_id`, `finding_status`, and a 50-word excerpt of `finding_text`. Select one from M32-A, one from M32-B, and one cluster-level synthesis row.

**4.3 Gap list:**
Produce every `finding_status = 'gap'` row with:
- `question_code`
- `cluster_subgroup_id`
- 30-word excerpt of `finding_text`

This list is required for Phase 10 gap-resolution work.

**4.4 Session_b_findings unchanged confirmation:**
```sql
SELECT COUNT(*) AS session_b_count
FROM wa_session_b_findings sbf
JOIN wa_session_a sa ON sbf.session_a_id = sa.id
JOIN mti_term_inventory mt ON sa.mti_term_id = mt.id
WHERE mt.cluster_code = 'M32';
```
Confirm this count matches the pre-directive count.

**4.5 Application report:**
Save a brief application report to:
`Sessions/Session_Clusters/M32/WA-M32-findings-record-applied-v1-20260508.md`

Report must include: directive ID, date applied, row counts by status, gap list, session_b_findings confirmation count.

---

## Element 5 — NOTES

**Pre-flight checks CC must run before any write:**

1. Confirm `cluster_finding` table exists with expected schema (per database-schema [current]).
2. Confirm `cluster_code = 'M32'` exists in `cluster` table with `status = 'Analysis - In Progress'`.
3. Confirm all four source files are readable at their stated paths.
4. Confirm `wa_obs_question_catalogue` contains rows for question_code pattern `T#.#.#` with `obs_id` linkable to the source headers.
5. Confirm sub-group codes M32-A and M32-B exist in `cluster_subgroup` table.

**Halt-on-error:** If pre-flight fails on any point, CC reports the failure and waits. No writes proceed until pre-flight passes.

**G items flagged for Phase 10:**
The following prompts carry `finding_status = 'gap'` for both M32-A and M32-B and require CC query resolution in Phase 10:
- T6.6.1–T6.6.3: Does 1Cor 4:4 / Jer 31:21 serve as primary anchor in other clusters? Requires query against `verse_context` anchor flags across clusters.
- T6.7.1–T6.7.3: Dimensional sharing counts for M32-A (Dim 05, 03, 11) and M32-B (Dim 03, 04, 05). Requires query against `mti_dimension_assignments` or equivalent.
- T7.1.8: LXX mapping for M32-A (suneidō/sunoida → Hebrew equivalents) and M32-B (LXX Greek equivalent for shit). Requires external or STEP-based query.

**BOUNDARY handling:**
The three BOUNDARY terms (kardiognōstēs mti=599, enthumeomai mti=3392, autokatakritos mti=4848) received structural characterisation notes only (per §11 Phase 8 BOUNDARY treatment). Their rows in `cluster_finding` are keyed to T1.2.1 only, with `cluster_subgroup_id = NULL` or equivalent BOUNDARY designation. No full 189-prompt matrix rows are created for BOUNDARY terms.

**Two-step load sequence:**
Structural loader MUST complete and be confirmed before full-text loader begins. Do not interleave the two steps.

**Directive ID:** DIR-20260508-004
**Cluster status post-directive:** remains `Analysis - In Progress`

---

*wa-cluster-M32-dir-005-findings-record-v1-20260508*
*Produced under Phase 9 of wa-sessionb-cluster-instruction-v1_1-20260507*
*Pattern: wa-directive-instruction-v1_4-20260506 §11.5 (worked pattern B)*
*Source: WA-M32-consolidated-findings-v1-20260508 Parts 1–4*
