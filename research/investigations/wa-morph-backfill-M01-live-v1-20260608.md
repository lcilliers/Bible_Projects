# L0 morph backfill — LIVE — M01

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| M01 | 85 | 1044 | 1076 | 1044 | 0 | 32 | 97% | Qal:398, Niphal:80, Hiphil:36, Piel:18, Hithpael:6, Pual:2 |

**WROTE morph to 1044 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).