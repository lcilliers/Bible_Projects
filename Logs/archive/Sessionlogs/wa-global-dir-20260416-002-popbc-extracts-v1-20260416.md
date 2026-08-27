# WA — CC Extraction Directives: T-POP-B and T-POP-C
**Filename:** wa-global-dir-20260416-002-popbc-extracts-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Directive reference:** DIR-20260416-002
**Governed by:** wa-global-general-rules-v2_2-20260415.json (GR-DIR-001 through GR-DIR-005)
**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_6-20260416.md (T-POP-B and T-POP-C)
- PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json (T-POP-A — must be applied before T-POP-B extract)

---

## Purpose

Two extraction queries are required to enable Claude AI to prepare the patches for T-POP-B and T-POP-C. These are read-only queries — no database changes. Results are returned as JSON for Claude AI to analyse and construct patches.

**Important sequencing note:** T-POP-A patch (`PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json`) must be applied and confirmed before the T-POP-B extract is run. T-POP-B cross-references `wa_obs_question_catalogue.obs_id` values, which do not exist until T-POP-A is applied.

Additionally: after T-POP-A is applied, CC should run a follow-up update to populate `source_registry_no` for the five source words. See Section 3 below.

---

## Section 1 — T-POP-B Extract: Finding-to-Question Mapping

**Purpose:** Return all `wa_session_b_findings` records with their current catalogue link status, plus the populated `wa_obs_question_catalogue` questions, so Claude AI can prepare the `wa_finding_catalogue_links` population patch.

**Query:**

```sql
SELECT
    f.id                        AS finding_id,
    f.finding_id                AS finding_code,
    f.registry_id,
    wr.no                       AS registry_no,
    wr.word,
    f.finding_type,
    f.finding,
    f.status                    AS finding_status,
    f.delete_flag,
    f.pass_ref,
    f.raised_date,
    -- existing catalogue links if any
    fcl.id                      AS existing_link_id,
    fcl.question_id             AS linked_question_id,
    fcl.coverage                AS link_coverage,
    fcl.status                  AS link_status,
    -- catalogue question details where linked
    oq.question_code            AS linked_question_code,
    oq.section                  AS linked_question_section,
    oq.question_text            AS linked_question_text
FROM wa_session_b_findings f
JOIN word_registry wr ON f.registry_id = wr.id
LEFT JOIN wa_finding_catalogue_links fcl
    ON fcl.finding_id = f.id AND fcl.delete_flagged = 0
LEFT JOIN wa_obs_question_catalogue oq
    ON oq.obs_id = fcl.question_id AND oq.deleted = 0
WHERE f.delete_flag = 0
ORDER BY f.registry_id, f.id;
```

**Also return:** The full question catalogue for Claude AI reference:

```sql
SELECT
    obs_id,
    question_code,
    section,
    source_word,
    question_text,
    scope,
    status
FROM wa_obs_question_catalogue
WHERE deleted = 0
ORDER BY obs_id;
```

**Return format:** Two JSON arrays — `findings_with_links` and `catalogue_questions`. Include row counts for both.

**Expected counts:**
- `findings_with_links`: 171 rows (all active findings)
- `catalogue_questions`: 194 rows (after T-POP-A applied)

**What Claude AI will do with this:** Review each finding without an existing catalogue link, identify the best matching question from the catalogue, and prepare insert statements for `wa_finding_catalogue_links` with `status = 'suggested'` and appropriate `coverage` (FULL/PARTIAL). Findings that clearly map to no existing question will be flagged for new question formulation in Stage 2b.

---

## Section 2 — T-POP-C Extract: Session Research Flags B-Target Alignment

**Purpose:** Return all `wa_session_research_flags` rows with `session_target = 'B'` and `resolved = 0` for Claude AI to review and confirm correct attribution before Session B begins for any word.

**Query:**

```sql
SELECT
    srf.id,
    srf.registry_id,
    wr.no                   AS registry_no,
    wr.word,
    wr.session_b_status,
    srf.flag_code,
    srf.flag_label,
    srf.priority,
    srf.session_target,
    srf.description,
    srf.session_raised,
    srf.raised_date,
    srf.resolved,
    srf.resolved_note
FROM wa_session_research_flags srf
JOIN word_registry wr ON srf.registry_id = wr.id
WHERE srf.session_target = 'B'
  AND srf.resolved = 0
ORDER BY wr.no, srf.raised_date;
```

**Return format:** JSON array `b_target_flags`. Include row count and list of distinct registries represented.

**Expected count:** 9 rows (confirmed from assessment dated 2026-04-14).

**What Claude AI will do with this:** Review each flag for correct attribution — does the `registry_id` correspond to the correct word, does the `flag_code` and `description` make sense as a pre-Session-B item, is there any flag that should be reclassified as `session_target = 'D'` or closed. Produce a patch or note confirming alignment or corrections required.

---

## Section 3 — Follow-up: Populate `source_registry_no` in `wa_obs_question_catalogue`

**After T-POP-A is applied**, run this lookup and update to populate `source_registry_no` for the five source words:

```sql
-- First: confirm the registry IDs
SELECT id, no, word
FROM word_registry
WHERE word IN ('grace', 'forgiveness', 'love', 'mercy', 'compassion')
ORDER BY word;
```

Return the result to Claude AI for confirmation, then apply updates:

```sql
UPDATE wa_obs_question_catalogue
SET source_registry_no = (SELECT id FROM word_registry WHERE word = 'grace')
WHERE source_word = 'Grace';

UPDATE wa_obs_question_catalogue
SET source_registry_no = (SELECT id FROM word_registry WHERE word = 'forgiveness')
WHERE source_word = 'Forgiveness';

UPDATE wa_obs_question_catalogue
SET source_registry_no = (SELECT id FROM word_registry WHERE word = 'love')
WHERE source_word = 'Love';

UPDATE wa_obs_question_catalogue
SET source_registry_no = (SELECT id FROM word_registry WHERE word = 'mercy')
WHERE source_word = 'Mercy';

UPDATE wa_obs_question_catalogue
SET source_registry_no = (SELECT id FROM word_registry WHERE word = 'compassion')
WHERE source_word = 'Compassion';
```

**Confirm:** Return count of rows updated per source_word. Expected: Grace 147, Forgiveness 14, Love 14, Mercy 11, Compassion 8. Total 194.

---

## Execution Sequence

1. Apply `PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json` (T-POP-A) — confirm 194 rows in `wa_obs_question_catalogue`
2. Run Section 3 lookup → confirm registry IDs with Claude AI → apply `source_registry_no` updates → confirm counts
3. Run Section 1 queries (T-POP-B extract) → return JSON to Claude AI
4. Run Section 2 query (T-POP-C extract) → return JSON to Claude AI

---

## Completion Confirmation Required

CC must return:
1. T-POP-A confirmation: row count in `wa_obs_question_catalogue` = 194
2. Section 3: registry ID lookup results; then update confirmation with per-word counts
3. Section 1: `findings_with_links` JSON (171 rows) + `catalogue_questions` JSON (194 rows)
4. Section 2: `b_target_flags` JSON (9 rows) + distinct registry list

---

*End of wa-global-dir-20260416-002-popbc-extracts-v1-20260416.md*
*Governed by wa-global-general-rules-v2_2-20260415.json*
