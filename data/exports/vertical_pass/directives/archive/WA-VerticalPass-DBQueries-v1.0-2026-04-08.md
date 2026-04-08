# WA-VerticalPass-DBQueries-v1.0-2026-04-08

**Framework B — Soul Word Analysis Programme**
**Vertical Pass Experiment — Database Query Instruction**
**Version 1.0 | 2026-04-08 | Status: Active**

| **Document** | **Value** |
|---|---|
| Filename | WA-VerticalPass-DBQueries-v1.0-2026-04-08.md |
| Supersedes | wa-vertical-pass-db-queries-v1.0-2026-04-08.md (incorrect naming — superseded immediately) |
| For | Claude Code |
| Purpose | Pull cross-registry term links and verse_context classifications for three experiment verses |
| Database | bible_research.db (schema v3.8.0 + VCB-031 additions) |

---

## Naming convention reference

All programme files follow these patterns (from WA-Reference-v5.5-20260330.md §1):

| Pattern | Used for |
|---|---|
| `WA-{DescriptiveName}-v{n}-{date}.{ext}` | Instruction documents (PascalCase) |
| `wa-vcb-{batch_id}-{scope}-v{n}-{date}.{ext}` | VCB batch outputs (lowercase) |
| `wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext}` | Word-level files (lowercase) |
| `wa-verticalpass-{scope}-{date}.{ext}` | Vertical pass outputs (lowercase) |
| `PATCH-{YYYYMMDD}-VCB{batch_id}-VERSECONTEXT-V{n}.json` | VCB patch files (uppercase) |

Output file requested from this instruction:
```
wa-verticalpass-dbresults-20260408.json
```

---

## Schema reference — tables and key columns used in these queries

Confirmed from database_schema_20260408.json + VCB-031 additions:

**`wa_verse_records`** — one row per term-verse occurrence
- `id` — primary key (this is the verse_record_id referenced by verse_context)
- `reference` — e.g. "Jer 7:24"
- `verse_text` — full verse text
- `mti_term_id` — FK to mti_terms.id
- `delete_flagged` — 0 = active

**`mti_terms`** — one row per extracted term
- `id` — primary key
- `strongs_number`, `transliteration`, `gloss`, `language`
- `owning_registry_fk` — FK to word_registry.id (note: join to word_registry.id not word_registry.no)
- `status` — e.g. 'extracted', 'extracted_thin'
- `delete_flagged`

**`word_registry`** — one row per registry
- `id` — primary key
- `no` — registry number (e.g. 213)
- `word` — registry word (e.g. 'listen')
- `session_b_status`, `verse_context_status`, `cluster_assignment`

**`verse_context`** — one row per term-verse classification
- `id` — primary key
- `verse_record_id` — FK to wa_verse_records.id
- `mti_term_id` — FK to mti_terms.id
- `group_id` — FK to verse_context_group.id (INTEGER, NULL if set aside)
- `is_anchor`, `is_relevant`, `is_related`
- `delete_flagged`
- `vertical_pass_flag` — added VCB-031 (INTEGER DEFAULT 0)
- `set_aside_reason` — added VCB-031 (TEXT DEFAULT NULL)

**`verse_context_group`** — one row per classification group
- `id` — primary key
- `mti_term_id` — FK to mti_terms.id
- `group_code` — e.g. '7498-001'
- `context_description`
- `vertical_pass_flag` — added VCB-031 (INTEGER DEFAULT 0)

---

## Query 1 — Resolve verse record IDs for the three experiment verses

```sql
SELECT
    id              AS verse_record_id,
    reference,
    verse_text,
    delete_flagged
FROM wa_verse_records
WHERE reference IN ('Jer 7:24', 'Rom 10:17', 'Isa 55:3')
AND delete_flagged = 0
ORDER BY reference;
```

If no results (reference format variation), use:
```sql
SELECT
    id              AS verse_record_id,
    reference,
    verse_text,
    delete_flagged
FROM wa_verse_records
WHERE (
    reference LIKE '%Jer%7%24%'
    OR reference LIKE '%Rom%10%17%'
    OR reference LIKE '%Isa%55%3%'
)
AND delete_flagged = 0
ORDER BY reference;
```

Note: the same verse text appears multiple times in wa_verse_records — once per term that occurs in it. Query 2 uses this intentionally. Query 1 returns one row per term-verse occurrence; there will be multiple rows per reference.

---

## Query 2 — All term links for the three verses across all registries

Replace `<ids>` with the `verse_record_id` values from Query 1 (use the distinct set of IDs — same verse may appear multiple times).

```sql
SELECT
    wvr.id              AS verse_record_id,
    wvr.reference,
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    mt.language,
    mt.status,
    mt.owning_registry_fk,
    wr.no               AS registry_no,
    wr.word             AS registry_word,
    wr.session_b_status,
    wr.verse_context_status
FROM wa_verse_records wvr
JOIN mti_terms mt
    ON wvr.mti_term_id = mt.id
JOIN word_registry wr
    ON mt.owning_registry_fk = wr.id
WHERE wvr.id IN (<verse_record_ids from Query 1>)
AND mt.status IN ('extracted', 'extracted_thin')
AND mt.delete_flagged = 0
AND wvr.delete_flagged = 0
ORDER BY wvr.reference, wr.no;
```

---

## Query 3 — Existing verse_context classifications for these verses

```sql
SELECT
    vc.verse_record_id,
    wvr.reference,
    mt.id               AS mti_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    wr.no               AS registry_no,
    wr.word             AS registry_word,
    vcg.group_code,
    vcg.context_description,
    vc.is_anchor,
    vc.is_relevant,
    vc.is_related,
    vc.set_aside_reason,
    vc.vertical_pass_flag
FROM verse_context vc
JOIN wa_verse_records wvr
    ON vc.verse_record_id = wvr.id
JOIN mti_terms mt
    ON vc.mti_term_id = mt.id
JOIN word_registry wr
    ON mt.owning_registry_fk = wr.id
LEFT JOIN verse_context_group vcg
    ON vc.group_id = vcg.id
WHERE vc.verse_record_id IN (<verse_record_ids from Query 1>)
AND vc.delete_flagged = 0
ORDER BY wvr.reference, wr.no, mt.id;
```

---

## Query 4 — Registry overview for all registries appearing in results

After Query 2 returns the `registry_no` values, pull registry details:

```sql
SELECT
    wr.id,
    wr.no               AS registry_no,
    wr.word,
    wr.session_b_status,
    wr.verse_context_status,
    wr.cluster_assignment
FROM word_registry wr
WHERE wr.no IN (<distinct registry_no values from Query 2>)
ORDER BY wr.no;
```

---

## Output format

Return all results as a single JSON file named:

```
wa-verticalpass-dbresults-20260408.json
```

Structure:
```json
{
  "produced_date": "2026-04-08",
  "produced_by": "Claude Code — WA-VerticalPass-DBQueries-v1.0-2026-04-08.md",
  "experiment_verses": ["Jer 7:24", "Rom 10:17", "Isa 55:3"],
  "query_1_verse_records": [...],
  "query_2_term_links": [...],
  "query_3_vc_classifications": [...],
  "query_4_registries": [...]
}
```

---

*WA-VerticalPass-DBQueries-v1.0-2026-04-08 | Supersedes wa-vertical-pass-db-queries-v1.0-2026-04-08.md*
