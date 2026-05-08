# wa-cluster-M05-dir-012-findings-record-v1-20260507

> Framework B Soul Word Analysis Programme — Cluster-process Directive
> Cluster: M05 — Love, Compassion and Kindness
> Directive sequence: dir-012 (findings recording — Phase 9)
> Version: v1 | Date: 20260507
> Pattern: wa-directive-instruction-v1_4-20260506 §11.5 (Worked pattern B)
> Session B Instruction: wa-sessionb-cluster-instruction-v1_1-20260507 §12
> Status: READY FOR CC EXECUTION — researcher confirmed Phase 9 proceed 20260507
> Previous directive in sequence: wa-cluster-M05-dir-011-followup-v1-20260507.md

---

## DIRECTIVE ID

`DIR-20260507-M05-012`

---

## MOTIVATION

The M05 cluster (Love, Compassion and Kindness) has completed the full Phase 8 catalogue pass across all seven substantive sub-groups (M05-A through M05-G) plus structural characterisation of M05-BOUNDARY. The pass applied all 189 prompts from the tiered observation catalogue (`wa-obs-catalogue-tiered-v1-20260506.md`) to each sub-group, followed by a cross-sub-group review pass, producing a self-contained four-part consolidated findings document.

**Source documents (all dated 20260507):**

| File | Content |
|---|---|
| `WA-M05-consolidated-findings-v1-20260507-part1.md` | Tiers T0–T1 (36 prompts) |
| `WA-M05-consolidated-findings-v1-20260507-part2.md` | Tier T2 (31 prompts) |
| `WA-M05-consolidated-findings-v1-20260507-part3.md` | Tiers T3–T4 (57 prompts) |
| `WA-M05-consolidated-findings-v1-20260507-part4.md` | Tiers T5–T7 (65 prompts) |
| `wa-obslog-M05-love-compassion-kindness-v1-20260507.md` | Authoritative working log, Phase 8 records |

**Sub-group findings files (supporting evidence, not primary load source):**

| File | Sub-group |
|---|---|
| `WA-M05-A-findings-v1-20260507.md` | M05-A — Love |
| `WA-M05-B-findings-v1-20260507.md` | M05-B — Compassion |
| `WA-M05-C-findings-v1-20260507.md` | M05-C — Mercy |
| `WA-M05-D-findings-v1-20260507.md` | M05-D — Kindness and Goodness |
| `WA-M05-E-findings-v1-20260507.md` | M05-E — Gentleness |
| `WA-M05-F-findings-v1-20260507.md` | M05-F — Comfort and Encouragement |
| `WA-M05-G-findings-v1-20260507.md` | M05-G — Fellowship and Participation |
| `WA-M05-BOUNDARY-findings-v1-20260507.md` | M05-BOUNDARY — structural characterisation only |

**Catalogue version:** CC must confirm the `catalogue_version` identifier from `wa_obs_question_catalogue` for `wa-obs-catalogue-tiered-v1-20260506.md` before proceeding. Record this value in the completion confirmation.

**Purpose of this directive:** Record the Phase 8 findings in `cluster_finding` so they are queryable by catalogue prompt, linked to `wa_obs_question_catalogue.obs_id`, scoped to sub-group, and available for cross-cluster synthesis in Session C and Session D.

**Standing constraint — RD-T713-001:** T7.1.3 is parked programme-wide. No G-codes or gap markers for T7.1.3 appear in the source documents. CC must not create `cluster_finding` rows for T7.1.3 prompts unless they are explicitly present in the source.

---

## SCOPE

**Table:** `cluster_finding`
**Cluster:** `M05`
**Cluster sub-groups in scope:** M05-A, M05-B, M05-C, M05-D, M05-E, M05-F, M05-G, M05-BOUNDARY

**Primary load source:** The four parts of the consolidated findings document — not the individual sub-group findings files. The consolidated document is the authoritative, cross-sub-group-reviewed output. Sub-group files are available for cross-reference only if CC cannot resolve ambiguity in the consolidated document.

**Operation type:** UPSERT — one row per (`obs_id`, `cluster_code`, `cluster_subgroup_id`, `version`) combination. If rows already exist for this cluster and catalogue version, update; do not duplicate.

**Row generation — two-step approach is authorised:**

**Step 1 — Structural loader:** Create one stub row per (189 prompts × 7 sub-groups + 189 cluster-level rows = 1,512 structural rows). Use `finding_status = 'finding'` and `finding_text = '[Sub-group not separately addressed in source — see cluster-level finding for this prompt]'` for cells not individually authored in the source. M05-BOUNDARY does not receive full catalogue rows — it receives structural characterisation notes only (see §BOUNDARY handling below).

**Step 2 — Full-text loader:** Parse the consolidated findings document (parts 1–4) and update `finding_text` and `finding_status` for every authored marker found. Do not overwrite stub rows that were not authored in the source.

**Marker recognition — CC must parse the following patterns:**

| Source marker | `finding_status` | Notes |
|---|---|---|
| `**[A]**`, `**[B]**` … `**[G]**` | `finding` | Per-sub-group finding (E-coded — evidenced) |
| `**[A — Label]**` etc. | `finding` | Per-sub-group finding with label variant |
| `**[A, B, C]**` etc. | `finding` | Shared finding — create one row per named sub-group |
| `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` | `cluster_synthesis` | Cluster-level synthesis; `cluster_subgroup_id = NULL` |
| `**S — [scope]**` or `**S —` within a sub-group block | `silent` | Silent — intentional; silence is a finding |
| `**G — [scope]**` or `**G**` | `gap` | Gap requiring CC database query |
| `**P —**` or `Partial` within a sub-group block | `finding` | Partial evidence — use `finding_status = 'finding'`; note partial nature in `finding_text` |

**Prompt identification:** Each `cluster_finding` row must be linked to the correct `wa_obs_question_catalogue` row by `obs_id`. Prompts are identified in the source by their `question_code` pattern (`T#.#.#` — e.g. `T0.1.1`, `T2.3.4`). CC must resolve `question_code` → `obs_id` by querying `wa_obs_question_catalogue WHERE question_code = 'T#.#.#'` for each prompt before inserting.

**Sub-group identification:** `cluster_subgroup_id` is resolved from `cluster_subgroup WHERE cluster_code = 'M05' AND subgroup_code = 'M05-A'` (etc.). These rows were created by DIR-20260507-M05-002. CC must resolve all 7 sub-group ids before loading.

**Source file attribution:** Set `source_file` on each row to the part-N filename that contained the finding:
- Part 1 → `WA-M05-consolidated-findings-v1-20260507-part1.md`
- Part 2 → `WA-M05-consolidated-findings-v1-20260507-part2.md`
- Part 3 → `WA-M05-consolidated-findings-v1-20260507-part3.md`
- Part 4 → `WA-M05-consolidated-findings-v1-20260507-part4.md`

**`finding_text` content:** Set to the verbatim prose paragraph from the consolidated findings document for the named marker. Do not truncate, summarise, or paraphrase. The `finding_text` field must reproduce the authored text exactly, preserving verse references cited in the body.

---

## BOUNDARY handling

M05-BOUNDARY received structural characterisation only — not a full 189-prompt catalogue pass. This was an intentional analytical decision recorded in the Phase 8 completion gate.

**CC action for BOUNDARY:** Do not create 189-row stubs for M05-BOUNDARY. Instead, create a small number of rows from the structural characterisation content in `WA-M05-BOUNDARY-findings-v1-20260507.md`, using:
- `cluster_subgroup_id` = id of M05-BOUNDARY sub-group row
- `finding_status = 'finding'`
- `source_file = 'WA-M05-BOUNDARY-findings-v1-20260507.md'`
- `obs_id = NULL` (structural characterisation rows are not catalogue-prompt-anchored)

The number of BOUNDARY rows is determined by the structural characterisation sections in the source file. CC reads that file and creates one row per named structural category or finding. Do not force-fit BOUNDARY content into T-code prompts.

---

## G-codes deferred to this directive

Three G-codes were raised during the Phase 8 passes (confirmed in the session log and obslog) and are to be resolved by CC as part of this directive's completion confirmation queries. These are not separate directives — they are incorporated here as completion tasks:

| G-code | Scope | CC query required |
|---|---|---|
| T6.4.3 | Cross-registry chesed distribution count | How many registries contain `mti_terms` with H2617A (mti=536)? Count verse_context rows per registry for this term. |
| T6.6.3 | Anchor verse cross-registry overlap counts | How many cluster_finding anchor verses (is_anchor=1) in M05-A through M05-G also appear as anchor verses in other clusters? |
| T6.7.3 | Dimensional overlap counts | How many prompts in the M05 cluster_finding table produce `finding_status = 'finding'` for both sub-group scope and cluster_synthesis scope simultaneously? |

CC records the results of these queries in the completion confirmation report. The results do not trigger additional DB writes at this stage — they are informational, available for the researcher to determine whether a follow-up directive is needed.

---

## VCREVISE patch — companion action

**Patch file:** `wa-cluster-M05-patch-boundary-pverses-v1-20260507.json`

This patch file (2 operations, VCREVISE type) must be applied either immediately before or immediately after this directive. The patch assigns G-status to two P-status BOUNDARY verses (Amo 5:21 vr=192566; 2Pe 1:3 vr=215044). The patch is independent of the `cluster_finding` writes — applying either first is acceptable. CC confirms both applications in the completion confirmation.

The patch was validated (JSON well-formed, 2 operations confirmed) and is ready for application.

---

## Schema pre-flight

**Before writing any rows, CC must confirm:**

1. `cluster_finding` table exists in the schema.
2. Required columns exist: `obs_id` (FK to `wa_obs_question_catalogue`), `cluster_code`, `cluster_subgroup_id` (nullable FK to `cluster_subgroup`), `finding_status` (check constraint), `finding_text`, `source_file`, `version`.
3. `finding_status` check constraint permits: `'finding'`, `'silent'`, `'gap'`, `'cluster_synthesis'`.
4. `wa_obs_question_catalogue` table is populated with 189 rows for the tiered catalogue — confirm `SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE catalogue_version = '[confirmed version]'` returns 189.

**If the `cluster_finding` table does not exist or is missing required columns:** HALT. Produce a schema enablement directive (per wa-directive-instruction-v1_4-20260506 §10) before proceeding. Do not improvise schema changes within this directive.

---

## OUTCOME REQUIRED

On successful execution, the following state must hold:

1. **`cluster_finding` rows for M05 exist** covering:
   - 7 sub-groups × 189 prompts = up to 1,323 sub-group-scoped rows
   - Up to 189 cluster-level synthesis rows (`cluster_subgroup_id = NULL`, `finding_status = 'cluster_synthesis'`)
   - A small number of BOUNDARY structural characterisation rows (`obs_id = NULL`)

2. **`finding_status` distribution:**
   - `finding` — all cells with E-coded (evidenced) or Partial responses from the source
   - `silent` — all cells with S-coded responses from the source; silence is intentional and is itself a finding
   - `gap` — all cells with G-coded responses from the source; these require follow-up CC queries
   - `cluster_synthesis` — all `[CLUSTER]` marker cells

3. **Every `finding_text`** for a `finding`- or `silent`- or `cluster_synthesis`-status row contains the verbatim prose from the consolidated findings document, including verse references cited in the body of the finding.

4. **Every `finding_text`** for a stub row (cell not individually authored) contains the explanatory stub: `[Sub-group not separately addressed in source — see cluster-level finding for this prompt]`

5. **`source_file`** is populated on every row with the correct part-N filename.

6. **`wa_session_b_findings` row count is unchanged** — this directive does not write to that table.

7. **VCREVISE patch applied:** The two BOUNDARY P-verses (Amo 5:21, 2Pe 1:3) have `vc_status = 'G'`, `group_id` set per the patch, `set_aside_reason = NULL`.

8. **Cluster status:** Remains `Analysis - In Progress`. Status is not changed by this directive.

---

## COMPLETION CONFIRMATION

CC returns the following after execution. All queries must be run post-application and their results included verbatim in the application report.

---

**Query 1 — Schema confirmation (pre-flight result):**
```sql
SELECT name FROM sqlite_master WHERE type='table' AND name='cluster_finding';
-- Expected: 1 row ('cluster_finding')

SELECT COUNT(*) AS catalogue_rows
FROM wa_obs_question_catalogue
WHERE catalogue_version = '[confirmed version string]';
-- Expected: 189
```

---

**Query 2 — Row counts by finding_status for M05:**
```sql
SELECT finding_status, COUNT(*) AS row_count
FROM cluster_finding
WHERE cluster_code = 'M05'
GROUP BY finding_status
ORDER BY finding_status;
```
Expected: rows for `finding`, `silent`, `gap`, `cluster_synthesis`. Total row count stated. Researcher will review distribution against the source document's expected marker counts.

---

**Query 3 — Per-sub-group row counts:**
```sql
SELECT cs.subgroup_code, cs.label, COUNT(cf.id) AS finding_rows
FROM cluster_subgroup cs
LEFT JOIN cluster_finding cf ON cf.cluster_subgroup_id = cs.id
                             AND cf.cluster_code = 'M05'
WHERE cs.cluster_code = 'M05'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```
Expected: 7 sub-group rows with finding counts; BOUNDARY row with its smaller structural characterisation count; 1 NULL sub-group row (cluster-level synthesis rows).

---

**Query 4 — Gap list (all `gap`-status rows):**
```sql
SELECT cf.id, oq.question_code, cs.subgroup_code, LEFT(cf.finding_text, 120) AS excerpt
FROM cluster_finding cf
LEFT JOIN wa_obs_question_catalogue oq ON oq.id = cf.obs_id
LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
WHERE cf.cluster_code = 'M05'
  AND cf.finding_status = 'gap'
ORDER BY oq.question_code, cs.subgroup_code;
```
Expected: Full list of all gap rows. These are queued for follow-up CC query work. G-codes T6.4.3, T6.6.3, T6.7.3 should appear here if recorded as gap in the source document.

---

**Query 5 — 3-row representative sample:**
```sql
SELECT oq.question_code, cs.subgroup_code, cf.finding_status,
       LEFT(cf.finding_text, 200) AS text_excerpt, cf.source_file
FROM cluster_finding cf
JOIN wa_obs_question_catalogue oq ON oq.id = cf.obs_id
JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
WHERE cf.cluster_code = 'M05'
  AND oq.question_code IN ('T0.1.1', 'T2.1.1', 'T5.1.1')
  AND cs.subgroup_code IN ('M05-A', 'M05-D', 'M05-G')
ORDER BY oq.question_code, cs.subgroup_code;
```
Expected: 3 rows (one per question_code × sub-group combination named). `finding_text` excerpt must match the consolidated findings source for those cells.

---

**Query 6 — `wa_session_b_findings` unchanged:**
```sql
SELECT COUNT(*) AS session_b_count
FROM wa_session_b_findings
WHERE registry_id IN (
  SELECT DISTINCT registry_id FROM mti_terms WHERE cluster_code = 'M05'
);
```
Expected: Same count as before this directive. No new rows written.

---

**Query 7 — VCREVISE patch confirmation:**
```sql
SELECT vc.id, vc.verse_record_id, vc.mti_term_id, vc.is_relevant,
       vc.group_id, vc.set_aside_reason, vr.reference
FROM verse_context vc
JOIN verse_ref vr ON vr.id = vc.verse_record_id
WHERE vc.verse_record_id IN (192566, 215044);
```
Expected:
- vr=192566 (Amo 5:21, mti=6209): `is_relevant=1`, `group_id=2148`, `set_aside_reason=NULL`
- vr=215044 (2Pe 1:3, mti=6845): `is_relevant=1`, `group_id=2597`, `set_aside_reason=NULL`

---

**Query 8 — G-code resolution results (informational — no writes):**

```sql
-- G-code T6.4.3: Cross-registry chesed distribution
SELECT mt.registry_id, COUNT(vc.id) AS verse_context_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.strongs_number = 'H2617A'
  AND mt.status IN ('extracted', 'extracted_thin')
GROUP BY mt.registry_id
ORDER BY verse_context_rows DESC;

-- G-code T6.6.3: Anchor verse cross-cluster overlaps
SELECT vc.verse_record_id, vr.reference, COUNT(DISTINCT vcg.mti_term_id) AS term_count,
       COUNT(DISTINCT mt.cluster_code) AS cluster_count
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
JOIN verse_ref vr ON vr.id = vc.verse_record_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE vc.is_anchor = 1
  AND mt.cluster_code = 'M05'
GROUP BY vc.verse_record_id
HAVING cluster_count > 1 OR term_count > 1
ORDER BY vr.reference;

-- G-code T6.7.3: Prompts with both sub-group and cluster-synthesis findings
SELECT oq.question_code, COUNT(cf.id) AS total_rows,
       SUM(CASE WHEN cf.cluster_subgroup_id IS NULL THEN 1 ELSE 0 END) AS synthesis_rows,
       SUM(CASE WHEN cf.cluster_subgroup_id IS NOT NULL THEN 1 ELSE 0 END) AS subgroup_rows
FROM cluster_finding cf
JOIN wa_obs_question_catalogue oq ON oq.id = cf.obs_id
WHERE cf.cluster_code = 'M05'
  AND cf.finding_status IN ('finding', 'cluster_synthesis')
GROUP BY oq.question_code
HAVING synthesis_rows > 0 AND subgroup_rows > 0
ORDER BY oq.question_code;
```

CC records all three result sets in the application report. No writes triggered by these queries.

---

**Application report:** Save to `Sessions/Session_Clusters/M05/WA-M05-dir012-findings-applied-v1-20260507.md`

Report must include:
1. Schema pre-flight result
2. Catalogue version string confirmed
3. Row counts by finding_status (Query 2)
4. Per-sub-group row counts (Query 3)
5. Full gap list (Query 4) — every row, not a sample
6. 3-row representative sample (Query 5) — with full excerpt text
7. `wa_session_b_findings` count confirmation (Query 6)
8. VCREVISE patch confirmation (Query 7)
9. G-code T6.4.3, T6.6.3, T6.7.3 results (Query 8)
10. Any anomalies encountered during loading (verses not resolving, prompt codes not found, schema mismatches)
11. Count of BOUNDARY structural characterisation rows created

---

## Execution sequence

Apply in the following order:

1. Schema pre-flight (confirm `cluster_finding` table and columns exist)
2. Resolve `catalogue_version` string from `wa_obs_question_catalogue`
3. Resolve all 7 sub-group ids from `cluster_subgroup WHERE cluster_code = 'M05'`
4. Apply VCREVISE patch (`wa-cluster-M05-patch-boundary-pverses-v1-20260507.json`) — 2 operations
5. Step 1: Structural loader — create 1,323 stub rows + cluster-level synthesis stub rows
6. Step 2: Full-text loader — parse parts 1–4; update `finding_text` and `finding_status` per marker
7. Create BOUNDARY structural characterisation rows from `WA-M05-BOUNDARY-findings-v1-20260507.md`
8. Run all Completion Confirmation queries
9. Resolve G-codes T6.4.3, T6.6.3, T6.7.3 (informational queries)
10. Save application report

**Halt conditions:** Halt and report to researcher before proceeding if:
- `cluster_finding` table does not exist or is missing required columns
- `wa_obs_question_catalogue` returns fewer than 189 rows for the confirmed catalogue version
- Any prompt code (`T#.#.#`) in the source document does not resolve to an `obs_id`
- Any sub-group code does not resolve to a `cluster_subgroup_id` for cluster M05
- The VCREVISE patch fails validation (wrong vr_id, wrong mti_term_id, version mismatch)
- Step 1 row count differs from expected by more than 5 rows (flag for review, do not auto-correct)

---

*wa-cluster-M05-dir-012-findings-record-v1-20260507*
*Cluster: M05 — Love, Compassion and Kindness*
*Phase 9 findings recording directive | Pattern: wa-directive-instruction-v1_4-20260506 §11.5*
*Source: WA-M05-consolidated-findings-v1-20260507 parts 1–4 | Obslog: wa-obslog-M05-love-compassion-kindness-v1-20260507*
*Companion patch: wa-cluster-M05-patch-boundary-pverses-v1-20260507.json*
*Prior directive in sequence: wa-cluster-M05-dir-011-followup-v1-20260507*
