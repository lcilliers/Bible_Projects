# CC Directive — Registry 103 (love) — Stage 3 Corrections
## WA Framework B Soul Word Analysis Programme
**File:** wa-103-love-sessionB-cc-directive-v2-2026-04-12.md
**Date:** 2026-04-12
**Companion patch:** PATCH-20260412-103-ANALYSIS-V1.json
**Governing instruction:** WA-SessionB-Instruction-v4.7 — Stage 3 (Pass 2 and Pass 4 directives)
**Previous CC directive:** wa-103-love-sessionB-cc-directive-v1-2026-04-12.md (applied)

---

## Purpose

Four manual operations arising from Stage 2 analytical passes:
1. `god_as_subject` field corrections (4 gaps + 1 error identified in Open Questions resolution)
2. `mti_term_flags` GOD_AS_SUBJECT inserts (11 confirmed god-as-subject terms)
3. `mti_term_flags` SOMATIC_INNER_LINK / BODY_INNER_EXPRESSION inserts (6 terms)

Apply PATCH-20260412-103-ANALYSIS-V1.json alongside this directive.

---

## DIR-001 — god_as_subject field corrections

**Context:** Cross-check of god_as_subject field against Pass 2 dimension index dominant_subject analysis identified 4 missing flags and 1 incorrect flag.

**Action A — Set god_as_subject = 1 for 4 under-flagged terms:**
```sql
UPDATE wa_term_inventory
SET god_as_subject = 1
WHERE term_id IN (
    SELECT id FROM mti_terms WHERE strongs_number IN ('G5363','H3033','H3039A','H7349')
);
```

**Action B — Correct god_as_subject = 0 for H2623 (hasid is the human bearer of chesed, not God):**
```sql
UPDATE wa_term_inventory
SET god_as_subject = 0
WHERE term_id = (SELECT id FROM mti_terms WHERE strongs_number = 'H2623');
```

**Verify:**
```sql
SELECT mt.strongs_number, ti.god_as_subject
FROM wa_term_inventory ti
JOIN mti_terms mt ON ti.term_id = mt.id
WHERE mt.strongs_number IN ('G5363','H3033','H3039A','H7349','H2623')
ORDER BY mt.strongs_number;
```
Expected: G5363=1, H2623=0, H3033=1, H3039A=1, H7349=1.

---

## DIR-002 — mti_term_flags GOD_AS_SUBJECT inserts (flag_id=1)

**Context:** Per WA-Reference 13.3, mti_term_flags is the authoritative record for GOD_AS_SUBJECT (flag_id=1). No records currently exist for Reg 103. 11 terms confirmed god-as-subject from Pass 2 analysis.

**Confirmed god-as-subject terms (mti.ids to confirm from DB before insert):**
G0025 (agapaō), G0026 (agapē), G0027 (agapētos), G5363 (philanthropia/benevolence), H0160 (ahavah), H2617A (chesed), H3033 (yedidut/beloved), H3039A (yadid/beloved), H7349 (rachum/compassionate), H7355 (racham), H7356B (rachamim)

```sql
INSERT INTO mti_term_flags (mti_term_id, flag_id, notes, created_at)
SELECT mt.id, 1, 'GOD_AS_SUBJECT confirmed — Session B Pass 2, Registry 103', date('now')
FROM mti_terms mt
WHERE mt.strongs_number IN ('G0025','G0026','G0027','G5363','H0160','H2617A','H3033','H3039A','H7349','H7355','H7356B')
  AND NOT EXISTS (
    SELECT 1 FROM mti_term_flags f WHERE f.mti_term_id = mt.id AND f.flag_id = 1
  );
```

**Verify:** Count should be 11.
```sql
SELECT COUNT(*) FROM mti_term_flags f
JOIN mti_terms mt ON f.mti_term_id = mt.id
WHERE mt.strongs_number IN ('G0025','G0026','G0027','G5363','H0160','H2617A','H3033','H3039A','H7349','H7355','H7356B')
  AND f.flag_id = 1;
```

---

## DIR-003 — mti_term_flags SOMATIC inserts

**Context:** Pass 4 somatic scan identified 6 terms warranting somatic flags. Per WA-Reference 13.3, SOMATIC_INNER_LINK = flag_id 3; BODY_INNER_EXPRESSION = flag_id 4. Confirm flag_ids from phase2_flag_types before inserting.

**BODY_INNER_EXPRESSION (flag_id=4) — kiss terms:**
- G2705 (kataphileō) — kiss is the body's expression of inner love state; primary somatic love gesture in NT
- G5370 (philēma) — same

**SOMATIC_INNER_LINK (flag_id=3) — bodily-root terms:**
- H7355 (racham) — etymologically linked to rechem (womb); bodily metaphor is structural to the meaning
- H7356B (rachamim) — same root; plural form
- H0160 (ahavah) — Song 8:6 and 2Sa 1:26 show love's bodily intensity; heart as primary address
- G0026 (agapē) — heart is agapē's primary address (Rom 5:5); 2Cor 2:4 tears

```sql
-- Confirm flag_ids first:
SELECT id, flag_code FROM phase2_flag_types WHERE flag_code IN ('SOMATIC_INNER_LINK','BODY_INNER_EXPRESSION');

-- Then insert (adjust flag_id values to match confirmed ids):
INSERT INTO mti_term_flags (mti_term_id, flag_id, notes, created_at)
SELECT mt.id, 4, 'BODY_INNER_EXPRESSION — kiss is primary somatic expression of love in NT — Session B Pass 4', date('now')
FROM mti_terms mt
WHERE mt.strongs_number IN ('G2705','G5370')
  AND NOT EXISTS (SELECT 1 FROM mti_term_flags f WHERE f.mti_term_id = mt.id AND f.flag_id = 4);

INSERT INTO mti_term_flags (mti_term_id, flag_id, notes, created_at)
SELECT mt.id, 3, 'SOMATIC_INNER_LINK — etymological or structural bodily connection — Session B Pass 4', date('now')
FROM mti_terms mt
WHERE mt.strongs_number IN ('H7355','H7356B','H0160','G0026')
  AND NOT EXISTS (SELECT 1 FROM mti_term_flags f WHERE f.mti_term_id = mt.id AND f.flag_id = 3);
```

**Verify:** 2 BODY_INNER_EXPRESSION + 4 SOMATIC_INNER_LINK = 6 records.

---

## Confirmation Required

After applying all operations:
1. [ ] god_as_subject corrections: G5363/H3033/H3039A/H7349 = 1; H2623 = 0
2. [ ] mti_term_flags GOD_AS_SUBJECT: 11 records inserted
3. [ ] mti_term_flags SOMATIC: 6 records inserted (2 BODY_INNER_EXPRESSION + 4 SOMATIC_INNER_LINK)
4. [ ] PATCH-20260412-103-ANALYSIS-V1.json applied
5. [ ] Fresh extract produced: wa-103-love-complete-[date].json

