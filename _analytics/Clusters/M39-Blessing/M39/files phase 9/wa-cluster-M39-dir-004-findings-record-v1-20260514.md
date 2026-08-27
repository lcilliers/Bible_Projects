# wa-cluster-M39-dir-004-findings-record-v1-20260514

**Cluster:** M39 — Blessing, Favour and Grace  
**Directive sequence:** dir-004  
**Pattern:** cluster-process directive per wa-directive-instruction [current] §11.5  
**Authored by:** Claude AI  
**Date:** 2026-05-14  
**Status:** AWAITING RESEARCHER REVIEW — do not apply until approved

---

## MOTIVATION

Phase 9 records the Phase 8 catalogue-pass findings into `cluster_finding`.

Source documents:
- `Sessions/Session_Clusters/M39/WA-M39-consolidated-findings-v1-20260514-part1.md` (T0–T1)
- `Sessions/Session_Clusters/M39/WA-M39-consolidated-findings-v1-20260514-part2-T2.md` (T2)
- `Sessions/Session_Clusters/M39/WA-M39-consolidated-findings-v1-20260514-part3-T3-T4.md` (T3–T4)
- `Sessions/Session_Clusters/M39/WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md` (T5–T7)
- Obslog: `Sessions/Session_Clusters/M39/wa-obslog-M39-sessionb-v1-20260514.md`
- Catalogue version: v2.1 (`wa-obs-catalogue-tiered-v2_1-20260513.md`)

Phase 8 self-check passed for both sub-groups (§11.7 — obslog confirmed). 189 prompts answered per sub-group. BOUNDARY characterisation notes present.

---

## SCOPE

**Table:** `cluster_finding`  
**Operation:** UPSERT — one row per (prompt × scope). For each authored marker block, create or update the row with the specified fields.

**cluster_code:** `M39`  
**Sub-group ID lookup:** query `cluster_subgroup WHERE cluster_code='M39'` to get ids for M39-A and M39-B before running inserts.  
**Catalogue prompt ID lookup:** query `wa_obs_question_catalogue WHERE tier IS NOT NULL AND deleted=0` to resolve `obs_id` by prompt code (e.g. T0.1.1, T2.3.1, etc.).

### Parser instruction

Parse the four source documents sequentially. For each `**T#.#.#**` header block:

1. Extract prompt code and text.
2. Resolve `obs_id` from `wa_obs_question_catalogue` by prompt code match.
3. For each scope marker `**[A]**`, `**[B]**`, `**[BOUNDARY]**`, `**[CLUSTER]**` on its own line:
   - Determine `cluster_subgroup_id`: A → M39-A id; B → M39-B id; BOUNDARY → M39-BOUNDARY id; CLUSTER → NULL.
   - Determine `finding_status`:
     - Body starts with `S —` → `silent`
     - Body starts with `G —` → `gap`
     - Marker is `**[CLUSTER]**` and body has no S/G prefix → `cluster_synthesis`
     - Otherwise → `finding`
   - Set `finding_text` = the full prose body of that scope marker's block.
   - Set `source_file` = the filename of the part being parsed.

**T1 prompt-code note:** Part 1's T1 section was written under v1 catalogue T1 component headings (Naming, Kind, Constitutional Location, etc.) rather than v2_1 prompt codes. CC should match by heading text where prompt codes are absent. If exact matching fails, flag each unmatchable T1 row for researcher review rather than inserting with a wrong obs_id. The analytical content is valid; only the obs_id assignment requires care.

### Cluster-level synthesis rows to ensure are written

These CLUSTER-scope findings are confirmed in the Phase 9 cross-sub-group review. If the parser does not capture them from the document markers, insert them explicitly:

| Prompt | obs_id lookup | finding_status | finding_text (abbreviated — full text from document) |
|---|---|---|---|
| T3.5.3 | T3.5.3 | `cluster_synthesis` | The creative faculty is silent across both M39-A and M39-B. M39 is not a creativity-engaging cluster — the grace and goodness characteristics are primarily relational, moral, and affective rather than creative. |
| T4.6.4 | T4.6.4 | `cluster_synthesis` | The spiritual beings interface is largely silent across both sub-groups. M39 is positional and constitutive rather than a conflict-domain cluster. The characteristic's primary register is God-human and human-human relational. |
| T6.2.1 | T6.2.1 | `cluster_synthesis` | The most structurally significant cross-sub-group sequence: goodness (M39-B doing well) precedes and produces divine acceptance (M39-A ra.tsah), as evidenced in Gen 4:7 — "if you do well, will you not be accepted?" The two sub-groups are not parallel but connected in sequence: M39-B goodness → M39-A acceptance. |
| T6.7.3 | T6.7.3 | `gap` | G — Dimensional sharing counts for both M39-A and M39-B are not yet available. CC database query required: for each sub-group, count how many confirmed analytical dimensions are shared with at least one other cluster in the programme. |

### Gap rows summary (for COMPLETION CONFIRMATION)

Expected gap rows after load:
- T6.7.1 [A]: G — dimensional sharing count not yet available
- T6.7.1 [B]: G — dimensional sharing count not yet available
- T6.7.3 [CLUSTER]: G — as above (cluster-wide)
- T1 prompt-code mismatches (if any): flagged rows, not inserted — number TBD by CC

---

## OUTCOME REQUIRED

1. `cluster_finding` rows created for cluster M39:
   - Sub-group A (M39-A): 189 rows, one per prompt
   - Sub-group B (M39-B): 189 rows, one per prompt
   - BOUNDARY: rows for T1.2.1 structural characterisation notes (3 terms, one note each)
   - CLUSTER: rows for cluster-level synthesis markers (minimum: T3.5.3, T4.6.4, T6.2.1, T6.7.3; plus any others parsed from [CLUSTER] markers in the document)

2. `finding_status` distribution (expected approximate):
   - `finding`: majority — every E-coded response
   - `silent`: minority — S-coded responses (T2.1 spirit-level for M39-B, T3.5, T4.6 for M39-B, T5.7 for M39-B, etc.)
   - `gap`: T6.7.1 [A], T6.7.1 [B], T6.7.3 [CLUSTER]; T1 mismatches if any
   - `cluster_synthesis`: cluster-level synthesis markers

3. Every `finding` row has non-null `finding_text` with verse references in the body.

4. `wa_session_research_flags` row count for M39 terms is unchanged (no modification to registry-era findings).

5. `cluster.status` unchanged — remains `Analysis - In Progress`.

---

## COMPLETION CONFIRMATION

CC runs the following after applying and returns results:

**Query 1 — Total row counts by status:**
```sql
SELECT finding_status, COUNT(*) as count
FROM cluster_finding
WHERE cluster_code = 'M39'
GROUP BY finding_status
ORDER BY finding_status;
```
Expected: rows for `finding`, `silent`, `gap`, `cluster_synthesis`. Total row count: approximately 400–450 (189×2 sub-groups + BOUNDARY notes + CLUSTER rows).

**Query 2 — Three-row sample (E findings with text):**
```sql
SELECT cf.id, cf.obs_id, cs.subgroup_code, cf.finding_status,
       SUBSTR(cf.finding_text, 1, 120) as text_preview
FROM cluster_finding cf
LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
WHERE cf.cluster_code = 'M39'
  AND cf.finding_status = 'finding'
ORDER BY cf.id
LIMIT 3;
```
Expected: 3 rows with non-null text_preview containing verse references.

**Query 3 — Gap rows:**
```sql
SELECT cf.obs_id, cs.subgroup_code, cf.finding_text
FROM cluster_finding cf
LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
WHERE cf.cluster_code = 'M39'
  AND cf.finding_status = 'gap';
```
Expected: T6.7.1 [A], T6.7.1 [B], T6.7.3 [CLUSTER] minimum; plus any T1 mismatch rows flagged.

**Query 4 — wa_session_research_flags unchanged:**
```sql
SELECT COUNT(*) as flag_count
FROM wa_session_research_flags wsr
JOIN mti_terms mt ON mt.id = wsr.mti_term_id
WHERE mt.cluster_code = 'M39';
```
Expected: same count as before Phase 9 (no insertions or modifications).

**Query 5 — Cluster-level synthesis rows present:**
```sql
SELECT cf.obs_id, cf.finding_status, SUBSTR(cf.finding_text, 1, 80) as preview
FROM cluster_finding cf
WHERE cf.cluster_code = 'M39'
  AND cf.finding_status = 'cluster_synthesis'
ORDER BY cf.obs_id;
```
Expected: T3.5.3, T4.6.4, T6.2.1, T6.7.3 and any other [CLUSTER] markers parsed.

**Application report:** CC saves to `Sessions/Session_Clusters/M39/WA-M39-findings-record-applied-v1-20260514.md`.

---

*wa-cluster-M39-dir-004-findings-record-v1-20260514*  
*References: WA-M39-consolidated-findings-v1-20260514-part1–4 | wa-obslog-M39-sessionb-v1-20260514.md*
