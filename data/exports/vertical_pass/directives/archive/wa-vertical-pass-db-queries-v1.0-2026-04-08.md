# wa-vertical-pass-db-queries-v1.0-2026-04-08

**For:** Claude Code
**Purpose:** Pull cross-registry term links for three experiment verses — vertical pass experiment
**Date:** 2026-04-08

---

## Background

The vertical pass experiment takes three specific verses and maps every term linked to them across all registries, together with any existing verse_context classifications. This makes the many-to-many relationship between verses, terms and registries visible in live data.

The three verses are:
1. Jer 7:24
2. Rom 10:17
3. Isa 55:3

---

## Query 1 — Resolve verse_record_ids for the three verses

```sql
SELECT 
    verse_record_id,
    reference,
    verse_text,
    verse_delete_flagged
FROM wa_verse_records
WHERE reference IN ('Jer 7:24', 'Rom 10:17', 'Isa 55:3')
AND verse_delete_flagged = 0
ORDER BY reference;
```

Note: reference format may vary (e.g. 'Jer 7:24' vs 'Jer 07:24'). If no results, try:
```sql
SELECT verse_record_id, reference, verse_text
FROM wa_verse_records
WHERE (reference LIKE '%Jer%7%24%' OR reference LIKE '%Rom%10%17%' OR reference LIKE '%Isa%55%3%')
AND verse_delete_flagged = 0;
```

---

## Query 2 — All term links for these three verses across all registries

For each verse_record_id returned by Query 1, run:

```sql
SELECT 
    wvr.verse_record_id,
    wvr.reference,
    mt.mti_term_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.term_owner_type,
    mt.status,
    mt.owning_registry_fk,
    wr.word AS registry_word,
    wr.session_b_status,
    wr.verse_context_status
FROM wa_verse_records wvr
JOIN mti_terms mt ON wvr.mti_term_id = mt.mti_term_id
JOIN word_registry wr ON mt.owning_registry_fk = wr.registry_no
WHERE wvr.verse_record_id IN (<ids from Query 1>)
AND mt.status IN ('extracted', 'extracted_thin')
AND wvr.verse_delete_flagged = 0
ORDER BY wvr.verse_record_id, mt.owning_registry_fk;
```

---

## Query 3 — Existing verse_context classifications for these verses

```sql
SELECT 
    vc.verse_record_id,
    wvr.reference,
    vc.mti_term_id,
    mt.strongs_number,
    mt.transliteration,
    vcg.group_code,
    vcg.context_description,
    vc.is_anchor,
    vc.is_relevant,
    vc.is_related,
    vc.set_aside_reason,
    vc.vertical_pass_flag
FROM verse_context vc
JOIN wa_verse_records wvr ON vc.verse_record_id = wvr.verse_record_id
JOIN mti_terms mt ON vc.mti_term_id = mt.mti_term_id
LEFT JOIN verse_context_group vcg ON vc.group_id = vcg.id
WHERE vc.verse_record_id IN (<ids from Query 1>)
AND vc.delete_flagged = 0
ORDER BY vc.verse_record_id, vc.mti_term_id;
```

---

## Query 4 — Registry overview for all registries that appear in the results

After Query 2 returns the owning_registry_fk values, pull the registry details:

```sql
SELECT 
    registry_no,
    word,
    session_b_status,
    verse_context_status,
    cluster_assignment
FROM word_registry
WHERE registry_no IN (<distinct owning_registry_fk values from Query 2>)
ORDER BY registry_no;
```

---

## Expected output format

Please return all results as JSON, one object per query:

```json
{
  "query_1_verses": [...],
  "query_2_term_links": [...],
  "query_3_vc_classifications": [...],
  "query_4_registries": [...]
}
```

This will be loaded directly into the vertical pass analysis session.
