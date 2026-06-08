# L0 morph backfill — LIVE — M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, M26, M27, M28, M29, M30, M31

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| M16 | 30 | 165 | 165 | 165 | 0 | 0 | 100% | Hithpael:7, Pual:6, Piel:4, Qal:4, Niphal:4 |
| M17 | 17 | 280 | 289 | 280 | 0 | 9 | 97% | Piel:42, Qal:7 |
| M18 | 28 | 276 | 279 | 276 | 0 | 3 | 99% | Piel:38, Qal:31, Hiphil:16, Niphal:5, Hophal:2, Hithpael:1 |
| M19 | 31 | 366 | 366 | 366 | 0 | 0 | 100% | Qal:153, Niphal:20, Hiphil:5, Piel:2 |
| M20 | 15 | 67 | 67 | 67 | 0 | 0 | 100% | Niphal:9, Qal:7, Hiphil:2, Piel:1 |
| M21 | 32 | 540 | 548 | 540 | 0 | 8 | 99% | Qal:135, Niphal:10, Hiphil:9, Piel:1 |
| M22 | 46 | 1463 | 1553 | 1463 | 0 | 90 | 94% | Piel:154, Hiphil:92, Hithpael:13, Pual:10, Qal:5, Niphal:2 |
| M23 | 120 | 2324 | 2612 | 2324 | 0 | 288 | 89% | Qal:393, Hiphil:277, Piel:80, Hithpael:28, Niphal:1 |
| M24 | 76 | 793 | 969 | 793 | 0 | 176 | 82% | Qal:115, Piel:74, Niphal:52, Hiphil:43, Hithpael:11, Pual:4 |
| M25 | 15 | 987 | 987 | 987 | 0 | 0 | 100% | Qal:201, Piel:63, Hiphil:51, Niphal:9, Hithpael:4, Pual:1 |
| M26 | 42 | 995 | 995 | 995 | 0 | 0 | 100% | Qal:98, Hiphil:37, Piel:6, Niphal:1, Hithpael:1 |
| M27 | 19 | 557 | 610 | 557 | 0 | 53 | 91% | Hiphil:157, Piel:46, Qal:37, Niphal:14, Hophal:5 |
| M28 | 40 | 573 | 574 | 573 | 0 | 1 | 100% | Qal:115, Piel:15, Hithpael:14, Niphal:8, Hiphil:6, Pual:1 |
| M29 | 12 | 297 | 297 | 297 | 0 | 0 | 100% | Hiphil:18, Hithpael:12, Qal:4 |
| M30 | 29 | 888 | 896 | 888 | 0 | 8 | 99% | Qal:619, Hiphil:129, Niphal:49, Hophal:3, Hithpael:3, Piel:2 |
| M31 | 13 | 320 | 323 | 320 | 0 | 3 | 99% | — |

**WROTE morph to 10889 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).