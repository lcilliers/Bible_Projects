# L0 morph backfill — LIVE — M02, M03, M04, M05, M06, M07, M08, M09, M10, M10b, M10c, M11, M12, M13, M14, M15

> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.

| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |
|---|---|---|---|---|---|---|---|---|
| M02 | 47 | 703 | 703 | 703 | 0 | 0 | 100% | Qal:165, Hiphil:57, Piel:29, Hithpael:11, Niphal:3 |
| M03 | 80 | 965 | 1002 | 965 | 0 | 37 | 96% | Qal:169, Hithpael:20, Niphal:20, Hiphil:11, Piel:6 |
| M04 | 58 | 1231 | 1268 | 1229 | 2 | 39 | 97% | Qal:293, Niphal:56, Piel:32, Hiphil:15, Hithpael:13, Pual:2 |
| M05 | 91 | 1565 | 1573 | 1565 | 0 | 8 | 99% | Piel:87, Qal:79, Niphal:15, Hithpael:9, Pual:4 |
| M06 | 34 | 437 | 466 | 437 | 0 | 29 | 94% | Qal:156, Piel:77, Niphal:14, Hiphil:12, Hithpael:2 |
| M07 | 33 | 375 | 382 | 375 | 0 | 7 | 98% | Qal:106, Hiphil:59, Niphal:28, Piel:2, Hophal:2, Hithpael:1 |
| M08 | 47 | 689 | 689 | 689 | 0 | 0 | 100% | Hiphil:105, Qal:100, Piel:26, Hithpael:21, Hophal:3, Pual:2 |
| M09 | 17 | 110 | 133 | 110 | 0 | 23 | 83% | Niphal:21, Hiphil:12 |
| M10 | 64 | 1520 | 1535 | 1520 | 0 | 15 | 99% | Qal:310, Hiphil:37, Piel:28, Hithpael:8, Niphal:7, Pual:2 |
| M10b | 17 | 537 | 601 | 537 | 0 | 64 | 89% | — |
| M10c | 8 | 275 | 275 | 275 | 0 | 0 | 100% | Qal:57, Piel:46, Niphal:15, Hithpael:8, ?u:1, Pual:1 |
| M11 | 15 | 340 | 343 | 340 | 0 | 3 | 99% | Piel:88, Niphal:46, Qal:32, Pual:7, Hiphil:7, Hithpael:3 |
| M12 | 48 | 960 | 1166 | 960 | 0 | 206 | 82% | Qal:292, Piel:109, Hiphil:41, Hithpael:39, Niphal:36, Pual:6 |
| M13 | 26 | 698 | 699 | 698 | 0 | 1 | 100% | Hiphil:84, Niphal:43, Qal:9, Piel:5, Hophal:1 |
| M14 | 42 | 393 | 418 | 393 | 0 | 25 | 94% | Qal:21, Niphal:17, Hiphil:11, Piel:8, Hithpael:6 |
| M15 | 85 | 1713 | 1863 | 1713 | 0 | 150 | 92% | Qal:602, Hiphil:149, Niphal:87, Hithpael:27, Piel:20, Hophal:1 |

**WROTE morph to 12509 rows.** DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no matching DB row (expected where our corpus is a subset).