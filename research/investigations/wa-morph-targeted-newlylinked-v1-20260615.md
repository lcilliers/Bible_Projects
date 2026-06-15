# L0 morph backfill — LIVE — strongs:13

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| targeted | 13 | 1621 | 1621 | 1621 | 0 | 0 | 100% | — |

**WROTE morph to 1828 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).

**Language reconciled from morph:** 2 term(s) relabelled (e.g. H7032G:Hebrew->Aramaic, H7032H:Hebrew->Aramaic).