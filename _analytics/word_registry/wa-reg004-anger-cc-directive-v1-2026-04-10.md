# CC Directive — Registry 004 Anger — CHAR Root Code Correction
**File:** wa-reg004-anger-cc-directive-v1-2026-04-10.md
**Date:** 2026-04-10
**From:** Claude AI — discovered during Reg 068 (grace) Session B Stage 1
**Registry:** 004 — anger
**Source:** CC query result from wa-068-grace-sessionB-cc-directive-v6-2026-04-10.md

---

## Background

During Reg 068 (grace) Session B Stage 1, a root code collision was identified. The root code CHAR has been assigned to two etymologically unrelated term families:

- **Reg 068 (grace):** Greek χάρις family — G5483 charizō, G5485 charis, G5487 charitoō. Root: Greek χαρ- (joy, favour, grace). Records fully enriched: root_gloss='grace', root_language='Greek'.
- **Reg 004 (anger):** Hebrew חרה family — H2734 cha.rah, H2740 cha.ron, H8474 ta.cha.rah. Root: Hebrew חרה (charah — to burn, be angry/incensed). Records not enriched: root_gloss=None, root_language=None.

These two roots share no etymological connection. The collision is causing the correlations.root_families CHAR entry to show root_gloss=null and registry_count=2, incorrectly linking anger and grace as a cross-cluster root family.

---

## What this directive covers

Reassign the three Reg 4 CHAR records to a new distinct root code, and enrich them with the correct gloss and language. Then trigger a recompute of the correlations root_families signal for both Reg 4 and Reg 68.

---

## Operations required

**Step 1 — Identify the wa_term_root_family record IDs for Reg 4 CHAR terms**

Before updating, CC must confirm the specific wa_term_root_family record ids for the three Reg 4 CHAR records. The query result showed three distinct terms but duplicate rows from the mti_terms join. Use:

```sql
SELECT rf.id, rf.term_inv_id, ti.strongs_number, mt.transliteration, rf.root_code, rf.root_gloss, rf.root_language
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number AND mt.owning_registry_fk = wr.id
WHERE wr.no = 4
  AND rf.root_code = 'CHAR';
```

This join on owning_registry_fk eliminates the duplicates from the earlier query. Report the distinct record ids before proceeding.

**Step 2 — Update root code, gloss, language and note on all three Reg 4 CHAR records**

For each of the three wa_term_root_family records identified in Step 1:

- root_code: 'CHAR' → 'CHARAH'
- root_gloss: None → 'burn/anger'
- root_language: None → 'Hebrew'
- note: 'Updated 2026-04-10 — root code corrected from CHAR to CHARAH. Original CHAR code caused collision with Greek charis root (Reg 068 grace). Hebrew charah root (to burn, be incensed) is etymologically unrelated to Greek charis root.'

**Step 3 — Recompute correlations root_families signal for Reg 4 and Reg 68**

After Step 2 is confirmed:

- Recompute the correlations.root_families block for Reg 004 (anger) — CHAR will no longer appear; CHARAH will appear with registry_count=1.
- Recompute the correlations.root_families block for Reg 068 (grace) — CHAR will now appear with registry_count=1 and root_gloss='grace', as the collision is resolved.
- Update correlation_root_family_count in statistics for both registries if the count changes.

---

## Expected state after application

| Registry | Root code | root_gloss | root_language | registry_count in correlations |
|---|---|---|---|---|
| Reg 004 (anger) | CHARAH | burn/anger | Hebrew | 1 (Reg 4 only) |
| Reg 068 (grace) | CHAR | grace | Greek | 1 (Reg 68 only) |

The correlations.root_families entry that previously showed CHAR with registry_count=2, root_gloss=null, cross_cluster=true will be replaced by two separate single-registry entries.

---

## Reporting required

1. Step 1: Report the distinct wa_term_root_family record ids for the three Reg 4 CHAR records
2. Step 2: Confirm all three records updated with new code, gloss, language, and note
3. Step 3: Confirm correlations recomputed for both registries — report new root_families entries for both Reg 4 (CHARAH) and Reg 68 (CHAR)
4. Report updated correlation_root_family_count for both registries if changed
5. Produce updated exports for both Reg 004 and Reg 068 reflecting the corrections
