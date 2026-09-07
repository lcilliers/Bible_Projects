# wa-cluster-M26-dir-001-findings-record-v1-20260511.md

**Directive ID:** DIR-20260511-M26-001
**Cluster:** M26 — Righteousness and Justice
**Type:** Cluster-process — findings recording (§11.5, worked pattern B)
**Produced by:** Claude AI — M26 Phase 8 catalogue pass session, 2026-05-10/11
**Researcher approval required:** YES — do not execute without researcher confirmation
**Date:** 2026-05-11
**Supersedes:** none (first findings directive for M26)

---

## DIRECTIVE ID

DIR-20260511-M26-001

---

## MOTIVATION

The M26 (Righteousness and Justice) cluster has completed Phase 8 — the full T0–T7 catalogue pass. All 189 prompts from `wa_obs_question_catalogue` have been applied across 8 sub-groups (M26-A1, M26-A2, M26-B, M26-C, M26-D, M26-E, M26-F, M26-G) plus cluster-level synthesis. The BOUNDARY sub-group has received a structural characterisation note. A cross-sub-group review pass produced 9 cluster-level findings. Four findings documents have been produced and reviewed (including post-debate gap additions confirmed on 2026-05-11).

The findings must be recorded in the database so they are queryable, linked to `wa_obs_question_catalogue.obs_id`, and available for cross-cluster synthesis in Session D.

**Source documents (authoritative input for this directive):**
- `WA-M26-consolidated-findings-v1-20260510-part1.md` — T0–T1
- `WA-M26-consolidated-findings-v1-20260510-part2-T2.md` — T2
- `WA-M26-consolidated-findings-v1-20260510-part3-T3-T4.md` — T3–T4
- `WA-M26-consolidated-findings-v1-20260510-part4-T5-T7.md` — T5–T7, BOUNDARY, cross-sub-group review

**Obslog reference:** WA-obslog-M26-phase8-catalogue-v1-20260510.md
**Session log reference:** WA-M26-session-log-v2-20260510.md (includes revision record from 2026-05-11)
**Catalogue version:** CC must retrieve from `SELECT DISTINCT catalogue_version FROM wa_obs_question_catalogue LIMIT 1` and record in the application report.

---

## SCHEMA PRE-FLIGHT (mandatory — execute before any data write)

The schema available to Claude AI at directive-authoring time is v3.17.0 (2026-04-27), which does not contain `cluster_finding`, `cluster_subgroup`, or `cluster_code` on `mti_terms`. However, M06 cluster work was completed after that schema version, and M06's directive sequence (DIR-20260506-001 through DIR-20260506-003) established these tables as part of the live database.

**CC must perform the following schema verification before proceeding:**

```sql
SELECT name FROM sqlite_master
WHERE type='table'
  AND name IN ('cluster_finding', 'cluster_subgroup', 'mti_terms')
ORDER BY name;
```

Additionally, verify that `mti_terms` has `cluster_code` and `cluster_subgroup_id` columns:
```sql
PRAGMA table_info(mti_terms);
```

**Decision rule:**
- If `cluster_finding` and `cluster_subgroup` exist AND `mti_terms` has `cluster_code` and `cluster_subgroup_id` → proceed with this directive per the instructions below.
- If any of these are absent → **HALT**. Report the missing structures to Claude AI. Do not proceed with any data writes. A schema enablement directive must be authored and executed first.

---

## SCOPE

**Cluster code:** `M26`

**Primary table:** `cluster_finding`
- Operation: UPSERT one row per (`obs_id` × `scope`)
- Where `scope` ∈ {`A1`, `A2`, `B`, `C`, `D`, `E`, `F`, `G`, `CLUSTER`, `BOUNDARY`}
- Where `obs_id` is resolved from `wa_obs_question_catalogue.obs_id` by matching `question_code` from the findings document headers

**Supporting table (read-only for resolution):**
- `wa_obs_question_catalogue` — resolve `obs_id` from `question_code` (e.g. `T0.1.1`, `T1.2.3`, `T2.1.1`)
- `cluster_subgroup` — resolve `cluster_subgroup_id` for each scope label (M26-A1, M26-A2, M26-B, M26-C, M26-D, M26-E, M26-F, M26-G)

**Source files (parse in order):**
1. `WA-M26-consolidated-findings-v1-20260510-part1.md` — T0, T1
2. `WA-M26-consolidated-findings-v1-20260510-part2-T2.md` — T2
3. `WA-M26-consolidated-findings-v1-20260510-part3-T3-T4.md` — T3, T4
4. `WA-M26-consolidated-findings-v1-20260510-part4-T5-T7.md` — T5, T6, T7, BOUNDARY, cross-sub-group findings

**Tables NOT written by this directive:**
- `wa_session_b_findings` — this table is registry-scope; cluster findings live exclusively in `cluster_finding`
- `verse_context`, `verse_context_group` — not modified by this directive
- `mti_terms` — not modified by this directive (sub-group assignment is a separate directive if needed)

---

## OUTCOME REQUIRED

### Row structure per `cluster_finding` row

Each row requires the following fields (CC resolves from context and source document):

| Field | Value / Resolution rule |
|---|---|
| `cluster_code` | `M26` |
| `obs_id` | resolved from `wa_obs_question_catalogue` by `question_code` matching `**T#.#.#**` header |
| `question_code` | the code string (e.g. `T0.1.1`) from the `**T#.#.#**` header |
| `scope` | one of: `A1`, `A2`, `B`, `C`, `D`, `E`, `F`, `G`, `CLUSTER`, `BOUNDARY` |
| `cluster_subgroup_id` | resolved from `cluster_subgroup` for scope ∈ {A1..G}; NULL for CLUSTER and BOUNDARY |
| `finding_status` | per marker type — see mapping below |
| `finding_text` | verbatim prose paragraph from the source document for this (question_code × scope) cell |
| `source_file` | part-N filename (e.g. `WA-M26-consolidated-findings-v1-20260510-part1.md`) |

### Marker-to-status mapping

| Marker type in source | `finding_status` value |
|---|---|
| `**[X — Sub-group label]** E.` | `finding` |
| `**[X — Sub-group label]** S.` | `silent` |
| `**[X — Sub-group label]** G —` | `gap` |
| `**[CLUSTER]**` | `cluster_synthesis` |
| `**[BOUNDARY]**` | `finding` (structural characterisation) |
| `**[X — qualification: ...]**` | `finding` (append to prior finding text for same scope/question_code, or create as subordinate finding row if the schema supports it) |

### Qualification entries (Gap 1 and Gap 2 additions)

The source documents contain extended qualification entries added on 2026-05-11 post-debate review:
- T1.2.3 A2: `**[A2 — qualification: conduct/state bidirectionality]**` — treat as an additional `finding` row for (T1.2.3 × A2), or append to the primary A2 finding text for T1.2.3, per schema capability.
- T1.3.2 A2: the multi-paragraph extension beginning "The resistance to self-generated righteousness..." — part of the A2 finding for T1.3.2. Include in full as part of the `finding_text` for that row.
- T1.3.3 A2: the `**[A2 — qualification...]**` paragraph about the Phili 3:9 two-righteousness distinction — part of the A2 finding for T1.3.3.
- T2.10.2 CLUSTER: the `**[Note on bidirectionality — from debate analysis]**` paragraph — append to the CLUSTER finding for T2.10.2.

**If the schema supports only one row per (obs_id × scope):** append all qualification text to the finding_text for that cell. Do not create separate rows that would violate the unique constraint.

### Expected row count

| Scope | Prompts addressed | Expected rows |
|---|---|---|
| A1 | 189 prompts (many S — all still create a row) | 189 |
| A2 | 189 | 189 |
| B | 189 | 189 |
| C | 189 | 189 |
| D | 189 | 189 |
| E | 189 | 189 |
| F | 189 | 189 |
| G | 189 | 189 |
| CLUSTER | 189 (synthesis note per prompt or S where no cluster note present) | 189 |
| BOUNDARY | 1 structural characterisation note (mapped to the prompt most relevant, or to a BOUNDARY-level pseudo-row if schema supports it) | 1 |
| **Total** | | **~1,702** |

**Two-step load is acceptable (per §11.5 and cluster instruction §12):**

**Step 1 — Structural loader:**
Create one stub row per (189 prompts × 9 scopes + 1 BOUNDARY row) with:
- `finding_status = 'finding'` as default
- `finding_text = 'Sub-group not separately addressed in source — see cluster-level finding for this prompt'` for any (prompt × scope) cell not explicitly authored in the source
- All `obs_id`, `question_code`, `cluster_code`, `scope` fields resolved and populated

**Step 2 — Full-text loader:**
Parse each of the four source documents and UPDATE `finding_text` + `finding_status` for every cell that has an authored finding, using verbatim prose from the source.

After Step 2, any row still carrying the stub text is the legitimate "no per-sub-group finding required" marker. Do not treat remaining stubs as errors.

### Outcome verification queries (CC runs after load)

```sql
-- 1. Row counts by status and scope
SELECT scope, finding_status, COUNT(*) as n
FROM cluster_finding
WHERE cluster_code = 'M26'
GROUP BY scope, finding_status
ORDER BY scope, finding_status;

-- 2. Total row count for M26
SELECT COUNT(*) as total_m26_rows
FROM cluster_finding
WHERE cluster_code = 'M26';

-- 3. Gap rows (for researcher attention)
SELECT question_code, scope, LEFT(finding_text, 100) as excerpt
FROM cluster_finding
WHERE cluster_code = 'M26'
  AND finding_status = 'gap'
ORDER BY question_code, scope;

-- 4. Confirm wa_session_b_findings unchanged for M26 terms
SELECT COUNT(*) as sb_rows_m26
FROM wa_session_b_findings sbf
JOIN mti_terms mt ON mt.id = sbf.term_id
WHERE mt.cluster_code = 'M26';
-- (Record baseline before directive; confirm count is same after)

-- 5. Three-row sample of cluster_synthesis rows
SELECT question_code, LEFT(finding_text, 150) as excerpt
FROM cluster_finding
WHERE cluster_code = 'M26'
  AND finding_status = 'cluster_synthesis'
ORDER BY question_code
LIMIT 3;
```

---

## COMPLETION CONFIRMATION

CC produces a completion report containing:

1. **Schema pre-flight result** — confirm all required tables and columns exist (or halt explanation if absent)
2. **Catalogue version** — from `SELECT DISTINCT catalogue_version FROM wa_obs_question_catalogue LIMIT 1`
3. **Step 1 result** — structural loader row count inserted/created
4. **Step 2 result** — full-text loader: number of rows updated with authored finding text; number of rows remaining with stub text
5. **Outcome verification query results** — all five queries above, results in full
6. **Gap list** — every `finding_status='gap'` row with `question_code`, `scope`, and `finding_text` excerpt (for T1.8, T6.7, T7.1.8, and any others)
7. **Known gaps (pre-declared from obslog):**
   - T1.8.1, T1.8.2, T1.8.3 (all scopes) — dimension classification: requires CC dimension vocabulary query against `wa_obs_question_catalogue` dimension table
   - T6.7.1, T6.7.2, T6.7.3 (all scopes) — dimensional sharing: same dependency as T1.8
   - T7.1.8 (all scopes) — LXX analysis: deferred, requires Logos Bible Software research
8. **Sunoida (G6083/mti:2739) status** — confirm 1Cor 4:4 remains unrouted (scope = NULL or unrouted); note researcher decision pending
9. **`wa_session_b_findings` row count** — confirm unchanged for M26 terms (query 4 result matches pre-directive baseline)
10. **Completion report file** — saved to `Sessions/Session_Clusters/M26/WA-M26-dir-001-completion-report-v1-{date}.md`

---

## DIRECTIVE SELF-CHECK (per §7)

Before submitting to CC, Claude AI confirms:

- [x] Five elements present: DIRECTIVE ID, MOTIVATION, SCOPE, OUTCOME REQUIRED, COMPLETION CONFIRMATION
- [x] Schema pre-flight required before any write — halt path specified
- [x] `wa_session_b_findings` explicitly excluded from writes
- [x] Cluster code M26 stated in all relevant elements
- [x] Source file names are exact (match the files on disk in `/mnt/user-data/outputs/`)
- [x] Two-step load pattern documented per §11.5 and cluster instruction §12
- [x] Known gap list pre-declared (T1.8, T6.7, T7.1.8) so CC can confirm them rather than discover them
- [x] Qualification entries (post-debate additions) addressed with explicit instruction for single-row-per-cell schema
- [x] Completion report file save location specified

---

## NOTES FOR RESEARCHER REVIEW

**Before approving this directive, please confirm:**

1. The gap list reflects your priorities — T1.8 (dimensions) and T7.1.8 (LXX) are the two substantive analytical gaps. Both require further CC work (dimension query and LXX research respectively).

2. The sunoida (1Cor 4:4) routing decision remains open. The verse is analytically relevant to E (self-condemnation) and F (reckoning faculty / clear conscience). A routing recommendation is recorded in the obslog. Your decision is needed before Phase 10 can close this cleanly.

3. The two-step load is recommended — it is more robust than a single-pass parse for a 1,700+ row load from four documents with varied formatting. If the live DB schema requires adjustments to the structural loader (e.g. different unique constraint structure than expected from M06 precedent), CC should halt at Step 1 and report before proceeding.

4. Cluster status remains `Analysis - In Progress` through Phase 9 (cross-sub-group review pass is complete; Phase 9 is complete as part of the cross-sub-group review in Part 4). Phase 10 (gap resolution and verification) follows after this directive is applied.

---

*wa-cluster-M26-dir-001-findings-record-v1-20260511.md*
*Produced by Claude AI from WA-M26 Phase 8 catalogue pass session 2026-05-10/11*
*Per wa-directive-instruction-v1_4-20260506.md §11.5*
