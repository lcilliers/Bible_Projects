# WA-VerticalPass-HeartQuery-v1.0-2026-04-08

**For:** Claude Code
**Purpose:** Investigate heart (lev/kardia) registry coverage — specifically whether Jer 7:24 is linked to any heart-related term, and what the programme's current state is for heart-family registries
**Date:** 2026-04-08

---

## Background

The vertical pass analysis of Jer 7:24 noted that "evil hearts" (lev ra') is the seat of the stubbornness described in the verse, but no heart term appeared in the Query 2 term links. Before concluding that heart is absent from the data for this verse, we need to verify:

1. Whether any heart-family term (Hebrew lev/lebab, Greek kardia) is linked to Jer 7:24 in wa_verse_records
2. What registry/registries carry heart terms and what their current status is
3. Whether Jer 7:24 appears in any heart registry's verse records at all — regardless of whether it was classified in VCB

---

## Query A — Does Jer 7:24 have any heart-term links?

Search all wa_verse_records rows where the reference matches Jer 7:24 and the linked mti_term has any heart-related strongs number.

```sql
SELECT
    wvr.id              AS verse_record_id,
    wvr.reference,
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.status,
    mt.owning_registry_fk,
    wr.no               AS registry_no,
    wr.word             AS registry_word,
    wr.verse_context_status
FROM wa_verse_records wvr
JOIN mti_terms mt
    ON wvr.mti_term_id = mt.id
JOIN word_registry wr
    ON mt.owning_registry_fk = wr.id
WHERE wvr.reference LIKE '%Jer%7%24%'
AND wvr.delete_flagged = 0
AND mt.delete_flagged = 0
ORDER BY wr.no;
```

This returns ALL term links for Jer 7:24 — not just extracted ones — so include all mt.status values.

---

## Query B — What registries carry Hebrew heart terms?

```sql
SELECT
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.status,
    mt.owning_registry_fk,
    wr.no               AS registry_no,
    wr.word             AS registry_word,
    wr.verse_context_status,
    wr.session_b_status
FROM mti_terms mt
JOIN word_registry wr
    ON mt.owning_registry_fk = wr.id
WHERE mt.strongs_number LIKE 'H3820%'
   OR mt.strongs_number LIKE 'H3824%'
   OR mt.strongs_number LIKE 'G2588%'
AND mt.delete_flagged = 0
ORDER BY mt.strongs_number;
```

H3820 = lev (heart), H3824 = lebab (heart), G2588 = kardia (heart)

---

## Query C — Does Jer 7:24 appear in any heart-registry verse records?

After Query B returns the heart registry numbers, check whether Jer 7:24 appears in wa_verse_records linked to those registries:

```sql
SELECT
    wvr.id              AS verse_record_id,
    wvr.reference,
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.status,
    wr.no               AS registry_no,
    wr.word             AS registry_word
FROM wa_verse_records wvr
JOIN mti_terms mt
    ON wvr.mti_term_id = mt.id
JOIN word_registry wr
    ON mt.owning_registry_fk = wr.id
WHERE wvr.reference LIKE '%Jer%7%24%'
AND wr.no IN (<heart registry_no values from Query B>)
AND wvr.delete_flagged = 0
ORDER BY wr.no, mt.strongs_number;
```

---

## Output format

Return as JSON named:

```
wa-verticalpass-heartquery-20260408.json
```

Structure:
```json
{
  "produced_date": "2026-04-08",
  "produced_by": "Claude Code — WA-VerticalPass-HeartQuery-v1.0-2026-04-08.md",
  "query_a_jer724_all_terms": [...],
  "query_b_heart_registries": [...],
  "query_c_jer724_heart_links": [...]
}
```
