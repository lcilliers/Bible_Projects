# L0 morph backfill — LIVE — M33, M34, M35, M36, M37, M38, M39, M41, M42, M43, M44, M45, M46

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| M33 | 44 | 671 | 673 | 671 | 0 | 2 | 100% | Hiphil:154, Qal:90, Piel:14, Hophal:4, Niphal:3, Hithpael:1 |
| M34 | 22 | 220 | 228 | 220 | 0 | 8 | 96% | Niphal:5, Hiphil:4, Qal:2, Hithpael:1 |
| M35 | 25 | 194 | 240 | 194 | 0 | 46 | 81% | — |
| M36 | 23 | 621 | 695 | 621 | 0 | 74 | 89% | Qal:244, Piel:21, Hiphil:8, Hophal:4, Niphal:4, Pual:2 |
| M37 | 22 | 1107 | 1143 | 1107 | 0 | 36 | 97% | Qal:838, Niphal:67, Pual:7, Hiphil:1 |
| M38 | 13 | 355 | 410 | 355 | 0 | 55 | 87% | Piel:85, Qal:43, Pual:7, Niphal:2, Hithpael:1, Hiphil:1 |
| M39 | 16 | 743 | 746 | 743 | 0 | 3 | 100% | Qal:209, Piel:180, Hiphil:71, Hithpael:24, Niphal:9, Pual:8 |
| M41 | 33 | 971 | 1494 | 971 | 0 | 523 | 65% | Qal:521, Piel:209, Hiphil:43, Niphal:30, Pual:3 |
| M42 | 34 | 527 | 586 | 527 | 0 | 59 | 90% | Qal:132, Niphal:77, Piel:69, Hithpael:24, Hiphil:23, Hophal:1 |
| M43 | 13 | 144 | 145 | 144 | 0 | 1 | 99% | — |
| M44 | 17 | 642 | 669 | 642 | 0 | 27 | 96% | Qal:310, Piel:2, ?c:2, Hiphil:1 |
| M45 | 14 | 176 | 203 | 176 | 0 | 27 | 87% | Qal:61, Hiphil:16 |
| M46 | 22 | 294 | 397 | 294 | 0 | 103 | 74% | Hiphil:16, Qal:5, Piel:5, Pual:4, Hithpael:2, ?u:1 |

**WROTE morph to 6664 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).