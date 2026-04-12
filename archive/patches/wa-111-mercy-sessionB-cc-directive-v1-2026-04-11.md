# Session B — CC Directive
## Registry 111 — mercy
## Stage 1 Investigation Directives
## Version: v1 | 2026-04-11
## Governing instruction: WA-SessionB-Analysis-Instruction-v4.7-2026-04-11

---

## Context

Stage 1 audit of Registry 111 (mercy) identified four items requiring Claude Code database investigation before a determination can be made. These are not patches — they are queries. Each directive names the question, the SQL required, and what Claude Code should return.

These directives accompany `PATCH-20260411-111-PREANALYSIS-V1.json`. The patch should be applied first. The investigation results should be returned to Claude AI before Stage 2 begins.

---

## CI-001 — ELE root family cross-registry check

**Question:** Does root code `ELE` appear in the `wa_term_root_family` table for any registry other than Registry 111?

**Why it matters:** G0415, G1653, G1655, G1656 all carry root code `ELE` (Greek eleos mercy root) in Registry 111. Registry 23 (compassion) shares G1653 and G1656 via xref. If Registry 23 also carries ELE as a root code on those terms, the root family should appear in the `correlations.root_families` block for both registries. Currently it does not appear there.

**SQL:**
```sql
SELECT rf.root_code, rf.root_gloss, rf.root_language, ti.term_id, wr.no as registry_no, wr.word
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON rf.term_inv_id = ti.id
JOIN word_registry wr ON ti.file_id = wr.id
WHERE rf.root_code = 'ELE'
  AND rf.delete_flagged = 0
ORDER BY wr.no, ti.term_id;
```

**Return:** Full result set.

---

## CI-002 — CHANAN root family cross-registry check

**Question:** Does root code `CHANAN` appear in the `wa_term_root_family` table for any registry other than Registry 111?

**Why it matters:** H2603A, H2604, H8467 carry root code `CHANAN` in Registry 111. Registry 68 (grace) shares H2603A via xref, and Registry 212 (pray) shares H8467. If those registries carry CHANAN as a root code, the root family correlation signal should fire for these pairs.

**SQL:**
```sql
SELECT rf.root_code, rf.root_gloss, rf.root_language, ti.term_id, wr.no as registry_no, wr.word
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON rf.term_inv_id = ti.id
JOIN word_registry wr ON ti.file_id = wr.id
WHERE rf.root_code = 'CHANAN'
  AND rf.delete_flagged = 0
ORDER BY wr.no, ti.term_id;
```

**Return:** Full result set.

---

## CI-003 — G8849 verse record gap

**Question:** Are there any `wa_term_verses` records for G8849 (*polueleos*) in Registry 111 that are not appearing in the export?

**Context:** G8849 has `occurrence_count = 8` in the term record (STEP Bible total) but 0 verse records in the extract. The audit has determined this is likely a corpus scope issue (LXX-only term, ESV programme corpus) rather than an extraction failure. However, this should be verified directly.

**SQL:**
```sql
-- Check wa_term_verses
SELECT COUNT(*) as verse_count, tv.term_inv_id
FROM wa_term_verses tv
JOIN wa_term_inventory ti ON tv.term_inv_id = ti.id
WHERE ti.term_id = 'G8849'
  AND ti.file_id = (SELECT id FROM word_registry WHERE no = 111)
GROUP BY tv.term_inv_id;

-- Also check mti_terms record directly
SELECT mt.id, mt.strongs_number, mt.status, mt.status_note, mt.exclusion_reason,
       mt.owning_registry_fk
FROM mti_terms mt
WHERE mt.strongs_number = 'G8849';
```

**Return:** Both result sets. If verse records exist in the database but are not appearing in the export, identify why. If none exist, confirm this matches the audit conclusion (corpus scope exclusion).

---

## CI-004 — session_b_findings export schema

**Question:** Is the `session_b_findings` top-level array in the export deliberately empty, or is it a schema inconsistency?

**Context:** The export for Registry 111 contains:
- Top-level `session_b_findings` array: empty (`[]`)
- `session_b.findings` block: contains 1 record (DIM-111-001)

The statistics field `session_b_finding_count = 1` correctly reflects the finding in `session_b.findings`. The top-level array appears to be a legacy or alternative path in the export schema.

**SQL:**
```sql
-- Check where session_b findings live in the database
SELECT table_name FROM information_schema.tables 
WHERE table_name LIKE '%session_b%' OR table_name LIKE '%finding%';

-- If a session_b_findings table exists:
SELECT * FROM session_b_findings WHERE registry_id = 111;

-- Check the wa_session_b_findings or equivalent
SELECT * FROM wa_session_b_findings WHERE registry_id = 111 LIMIT 5;
```

**Return:** Clarify which table stores session_b findings, whether the top-level array in the export is a bug or by design, and whether the export script needs correction. If the schema uses `session_b.findings` as the canonical path, the top-level `session_b_findings` array should either be removed from the export or populated correctly.

---

## Delivery summary

| Item | Type | Action |
|---|---|---|
| `PATCH-20260411-111-PREANALYSIS-V1.json` | Patch | Apply to database |
| CI-001 | Investigation | Query and return results to Claude AI |
| CI-002 | Investigation | Query and return results to Claude AI |
| CI-003 | Investigation | Query and return results to Claude AI |
| CI-004 | Investigation | Query and return results to Claude AI |

**After patch application and investigations:** Claude Code to produce fresh extract R1:

```
CC DIRECTIVE — FRESH EXTRACT R1
Registry: 111 — mercy
Action: Produce fresh complete export
Filename: wa-111-mercy-complete-2026-04-11.json (overwrite) or wa-111-mercy-complete-[date]-r1.json
Reason: All Stage 1 patches applied and confirmed. Stage 2 requires clean data.
Confirm: G8849 mti_status=delete with exclusion_reason; H3724B/C/D exclusion_reasons populated;
         strongs_list contains G8849 entry with count=0.
```

---
