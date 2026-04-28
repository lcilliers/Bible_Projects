# CC Directive — Registry 068 Grace — CHAR Root Investigation Query
**File:** wa-068-grace-sessionB-cc-directive-v6-2026-04-10.md
**Date:** 2026-04-10
**Supersedes:** previous v6 draft (investigation query only — no database changes)
**From:** Claude AI — Session B Stage 1 — Gap 10
**Registry:** 068 — grace

---

## What this directive covers

A data question only. No database changes required.

The CHAR root code in correlations.root_families shows root_gloss = null with registry_count = 2, spanning Reg 4 (anger) and Reg 68 (grace). Reg 68's term records carry root_gloss = 'grace'. The null suggests a gloss conflict across the two registries. Before any correction can be determined, CC must confirm what terms in Reg 4 carry CHAR and what their root_gloss values are.

---

## Query required

```sql
SELECT 
    wr.no as registry_no,
    wr.word as registry_word,
    ti.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.status as mti_status,
    ti.delete_flagged as inv_delete_flagged,
    rf.root_code,
    rf.root_gloss,
    rf.root_language,
    rf.note
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = 4
  AND rf.root_code = 'CHAR';
```

---

## Reporting required

Return the full query result. Claude AI will assess whether the CHAR root code assignment on Reg 4 is correct before determining whether any correction is needed. No changes to be made pending that assessment.
