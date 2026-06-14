# L0 morph backfill — LIVE — M47, M26, M25, M22, M44, M23, M03, M05, M04, M30, M28, M27, M34, M39, T2

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| M47 | 32 | 1584 | 1584 | 1584 | 0 | 0 | 100% | — |
| M26 | 56 | 1709 | 1749 | 1709 | 0 | 40 | 98% | Qal:286, Hiphil:37, Niphal:18, Piel:7, Hithpael:1 |
| M25 | 20 | 1395 | 1395 | 1395 | 0 | 0 | 100% | Qal:204, Hiphil:82, Piel:63, Niphal:9, Hithpael:4, Pual:1 |
| M22 | 51 | 1668 | 1758 | 1668 | 0 | 90 | 95% | Piel:180, Hiphil:139, Qal:76, Hithpael:18, Pual:11, Niphal:3 |
| M44 | 23 | 997 | 1028 | 997 | 0 | 31 | 97% | Qal:397, Piel:2, Tiphil:2, Hiphil:1 |
| M23 | 134 | 2470 | 3242 | 2470 | 0 | 772 | 76% | Qal:393, Hiphil:277, Piel:80, Hithpael:28, Niphal:1 |
| M03 | 88 | 970 | 1071 | 970 | 0 | 101 | 91% | Qal:171, Hithpael:20, Niphal:20, Hiphil:11, Piel:6 |
| M05 | 93 | 1567 | 1575 | 1567 | 0 | 8 | 99% | Piel:87, Qal:79, Niphal:15, Hithpael:9, Pual:4 |
| M04 | 62 | 1236 | 1273 | 1234 | 2 | 39 | 97% | Qal:293, Niphal:56, Piel:32, Hiphil:15, Hithpael:13, Pual:2 |
| M30 | 31 | 896 | 956 | 896 | 0 | 60 | 94% | Qal:627, Hiphil:129, Niphal:49, Hophal:3, Hithpael:3, Piel:2 |
| M28 | 44 | 574 | 577 | 574 | 0 | 3 | 99% | Qal:115, Piel:15, Hithpael:14, Niphal:8, Hiphil:6, Pual:1 |
| M27 | 21 | 558 | 611 | 558 | 0 | 53 | 91% | Hiphil:157, Piel:46, Qal:37, Niphal:14, Hophal:5 |
| M34 | 25 | 221 | 235 | 221 | 0 | 14 | 94% | Niphal:5, Hiphil:4, Qal:2, Hithpael:1 |
| M39 | 17 | 744 | 747 | 744 | 0 | 3 | 100% | Qal:209, Piel:180, Hiphil:71, Hithpael:24, Niphal:9, Pual:8 |
| T2 | 867 | 24121 | 34377 | 24121 | 0 | 10256 | 70% | Qal:3364, Hiphil:525, Niphal:477, Piel:395, Hithpael:203, Hophal:39 |

**WROTE morph to 40697 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).