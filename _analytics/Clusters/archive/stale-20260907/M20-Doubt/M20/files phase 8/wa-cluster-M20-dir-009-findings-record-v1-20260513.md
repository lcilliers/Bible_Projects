# wa-cluster-M20-dir-009-findings-record-v1-20260513

**DIRECTIVE ID:** DIR-20260513-009  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Directive type:** Cluster findings recording (§11.5)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Produced by:** Claude AI — M20 Session B Phase 8  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 8 (catalogue pass) for M20 is complete. All 189 prompts from `wa-obs-catalogue-tiered-v1-20260506.md` (T0–T7) have been answered across four sub-groups (M20-A through M20-D) plus cluster-level synthesis findings. The findings are documented in four consolidated finding documents, all produced 2026-05-13:

- `WA-M20-consolidated-findings-v1-20260513-part1.md` — T0 (12 prompts) and T1 (24 prompts)
- `WA-M20-consolidated-findings-v1-20260513-part2-T2.md` — T2 (31 prompts)
- `WA-M20-consolidated-findings-v1-20260513-part3-T3-T4.md` — T3 (33 prompts) and T4 (24 prompts)
- `WA-M20-consolidated-findings-v1-20260513-part4-T5-T7.md` — T5 (21 prompts), T6 (24 prompts), T7 (20 prompts)

Total: 189 prompts × up to 5 scopes (A, B, C, D, CLUSTER) = up to 945 rows maximum; actual row count will be lower where a single [CLUSTER] finding covers all sub-groups, and where S or G markers are applied at cluster scope rather than per-sub-group.

The findings need to be recorded in `cluster_finding` so they are queryable, linked to `wa_obs_question_catalogue.obs_id`, and available for Phase 9 synthesis and Session C report writing.

---

## SCOPE

**Table:** `cluster_finding`  
**Cluster:** M20  
**Sub-groups:** M20-A, M20-B, M20-C, M20-D, and CLUSTER-level

**Source files (four parts, all to be parsed):**
- Part 1: `WA-M20-consolidated-findings-v1-20260513-part1.md`
- Part 2: `WA-M20-consolidated-findings-v1-20260513-part2-T2.md`
- Part 3: `WA-M20-consolidated-findings-v1-20260513-part3-T3-T4.md`
- Part 4: `WA-M20-consolidated-findings-v1-20260513-part4-T5-T7.md`

**Parsing instructions for CC:**

The source documents use the output style specified at §11.8 of `wa-sessionb-cluster-instruction-v1_4-20260513.md`. CC parses each prompt block and its sub-group markers:

1. **Prompt identification:** headers of the form `**T{tier}.{component}.{seq}** — {prompt text}` identify each prompt. Map to `wa_obs_question_catalogue` via `question_code = 'T{tier}.{component}.{seq}'` to obtain `obs_id`.

2. **Scope markers (recognised):**
   - `**[A — Anxiety and Worry]**` or `**[A]**` → `cluster_subgroup_code = 'M20-A'`
   - `**[B — Despair and Hopelessness]**` or `**[B]**` → `cluster_subgroup_code = 'M20-B'`
   - `**[C — Discouragement and Loss of Heart]**` or `**[C]**` → `cluster_subgroup_code = 'M20-C'`
   - `**[D — Doubt and Indecision]**` or `**[D]**` → `cluster_subgroup_code = 'M20-D'`
   - `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` → `cluster_subgroup_code = NULL`, `is_cluster_level = 1`
   - `**[A, B, C]**` (multi-sub-group shared finding) → one row per named sub-group, identical finding_text

3. **Status mapping:**
   - Finding opens with `**[X]** {text}` where text is substantive → `finding_status = 'finding'`
   - `**S — [scope]**` or finding text is explicitly "S —" → `finding_status = 'silent'`
   - `**G — [scope]**` or finding text begins "G —" → `finding_status = 'gap'`
   - `**[CLUSTER]**` finding → `finding_status = 'cluster_synthesis'`

4. **finding_text:** verbatim prose paragraph from the source document, beginning after the scope marker. Do not truncate. Include verse references as written.

5. **source_file:** set to the part-N filename containing the finding (e.g. `WA-M20-consolidated-findings-v1-20260513-part1.md`).

6. **version:** 1 for all rows (first recording pass).

7. **author:** `claude_ai`

8. **Prompts where a single `[CLUSTER — all sub-groups]` covers all scopes:** insert one row with `is_cluster_level = 1` and `cluster_subgroup_code = NULL`. Do not also insert per-sub-group rows unless the document separately addresses each sub-group.

9. **Prompts addressed per sub-group plus a CLUSTER synthesis:** insert per-sub-group rows AND the CLUSTER synthesis row.

**Schema path check (§11.5):**  
CC must confirm whether `cluster_finding` (post-M45) exists before writing. If the table does not exist, halt and produce a schema enablement directive per §10. Do not improvise.

**Out of scope:** `wa_session_b_findings` (registry-scope; must not be touched), `verse_context`, `verse_context_group`, `mti_terms`, any other table.

---

## OUTCOME REQUIRED

1. One row in `cluster_finding` per scope marker in the four source documents, for cluster_code = 'M20'.
2. `finding_status` correctly set per marker type (finding / silent / gap / cluster_synthesis).
3. `finding_text` is verbatim prose from the source.
4. `source_file` correctly references the part-N file for each row.
5. Every `wa_obs_question_catalogue` prompt (189 total) has at least one row in `cluster_finding` for cluster_code = 'M20' — either a sub-group row, a cluster-level row, or both.
6. No prompt has zero rows (every prompt must be represented).
7. `wa_session_b_findings` row count unchanged (no writes to that table).
8. No `cluster_finding` rows for any cluster other than M20 are modified.

**Gap rows:** Where `finding_status = 'gap'`, the `finding_text` should carry the gap description as written. CC must produce a gap list as part of the completion confirmation (see below) so that gap-resolution follow-up work can be scoped.

---

## COMPLETION CONFIRMATION

CC to provide all of the following:

```sql
-- 1. Row count by finding_status for M20
SELECT finding_status, COUNT(*) as row_count
FROM cluster_finding
WHERE cluster_code = 'M20'
GROUP BY finding_status
ORDER BY finding_status;
-- Expected: rows for 'finding', 'silent', 'gap', 'cluster_synthesis'
-- Total rows should cover all 189 prompts × applicable scopes

-- 2. Row count by sub-group scope
SELECT cluster_subgroup_code, COUNT(*) as row_count
FROM cluster_finding
WHERE cluster_code = 'M20'
GROUP BY cluster_subgroup_code
ORDER BY cluster_subgroup_code;
-- Expected: rows for M20-A, M20-B, M20-C, M20-D, NULL (cluster-level)

-- 3. Prompt coverage check — any prompt with zero M20 rows
SELECT q.question_code
FROM wa_obs_question_catalogue q
WHERE q.deleted = 0
  AND q.tier IS NOT NULL
  AND NOT EXISTS (
    SELECT 1 FROM cluster_finding cf
    WHERE cf.cluster_code = 'M20'
      AND cf.obs_id = q.id
  );
-- Expected: 0 rows (every prompt has at least one M20 finding row)

-- 4. Sample rows (3 representative, one per tier range)
SELECT question_code, cluster_subgroup_code, finding_status,
       SUBSTR(finding_text, 1, 120) as excerpt
FROM cluster_finding cf
JOIN wa_obs_question_catalogue q ON q.id = cf.obs_id
WHERE cf.cluster_code = 'M20'
  AND cf.question_code IN ('T0.1.1', 'T3.7.1', 'T7.3.3')
ORDER BY cf.question_code, cf.cluster_subgroup_code;

-- 5. Gap list — all gap rows for M20
SELECT question_code, cluster_subgroup_code,
       SUBSTR(finding_text, 1, 200) as gap_description
FROM cluster_finding cf
JOIN wa_obs_question_catalogue q ON q.id = cf.obs_id
WHERE cf.cluster_code = 'M20'
  AND cf.finding_status = 'gap'
ORDER BY question_code, cluster_subgroup_code;
-- This list is used for Phase 9 gap-resolution follow-up

-- 6. wa_session_b_findings not touched
SELECT COUNT(*) as unchanged_count
FROM wa_session_b_findings
WHERE cluster_code = 'M20';
-- Compare with pre-apply count; should be unchanged (typically 0 for a cluster-scope term)
```

CC to save application report to: `Sessions/Session_Clusters/M20/WA-M20-findings-record-applied-v1-20260513.md`

This report must include: total rows inserted, count by finding_status, count by sub-group, prompt-coverage check result, gap list, and any parse errors or ambiguities encountered.

---

*wa-cluster-M20-dir-009-findings-record-v1-20260513 | DIR-20260513-009 | Cluster findings recording for M20 Doubt, Despair and Anxiety — 189 prompts, 4 sub-groups + CLUSTER scope | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
