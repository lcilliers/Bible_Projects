# NT verse_lexical — analysis, 2026-08-09

Ad-hoc analysis of the `verse_lexical` table (schema per [`iba/app/ps/VerseLexical.ps1`](../ps/VerseLexical.ps1) docstring: T1–T3 mechanical engine — per-span, per-code role + morph-selected sense) scoped to the 27 NT books. Queried directly against `iba/app/db/iba.db`; all figures below are live counts, not estimates.

## 1. Coverage — complete, no gaps

| Metric | Value |
| --- | --- |
| NT books with ≥1 active `verse_lexical` row | 27 / 27 |
| NT verses covered | 7,605 / 7,605 (100%) |
| NT spans (`span` table) with no active `verse_lexical` row | 0 |
| Active rows (`deleted=0`) | 111,410 |
| Superseded/deleted rows | 0 |

No NT book, verse, or span is missing lexical resolution. Contrast — OT stands at only 6 books processed (Dan, Hos, Joel, Jonah, Mic, Obad; 10,446 active rows, 423 verses), matching the book-by-book debate campaign record (memory: `project_iba_book_by_book_debate_phase`).

## 2. Role split (content vs. function)

| Role | Codes | % |
| --- | --- | --- |
| `content` | 81,509 | 73.2% |
| `function` | 29,901 | 26.8% |

Ratio is stable across books (roughly 70–75% content in every book checked individually — no outliers).

## 3. Resolution status

| Status | NT rows |
| --- | --- |
| `resolved` | 111,410 (100%) |
| `unregistered` | 0 |

Whole-table (OT+NT) comparison: only 3 `unregistered` rows exist anywhere, all in Dan (H3673, Dan 3:2/3:3/3:27) — an OT condition, not present in the NT at all.

## 4. Data completeness (nulls / notes)

Across all 111,410 NT rows: **zero** nulls in `strong`, `morph_code`, or `resolved_sense`, and **zero** `ambiguity_note` entries. (Whole-table: exactly one `ambiguity_note` exists anywhere — Dan 10:16, H8193G lip/language/shore sense, base Strong's shared with H8193J — again OT-only.)

## 5. Per-book breakdown

| Book | Verses | Codes | Content | Function |
| --- | --- | --- | --- | --- |
| Matt | 990 | 14,476 | 10,797 | 3,679 |
| Mark | 633 | 9,010 | 6,601 | 2,409 |
| Luke | 1,077 | 15,676 | 11,470 | 4,206 |
| John | 848 | 12,658 | 9,442 | 3,216 |
| Acts | 950 | 14,711 | 10,912 | 3,799 |
| Rom | 424 | 5,766 | 4,044 | 1,722 |
| 1Cor | 425 | 5,667 | 4,048 | 1,619 |
| 2Cor | 255 | 3,779 | 2,550 | 1,229 |
| Gal | 144 | 1,863 | 1,315 | 548 |
| Eph | 155 | 1,968 | 1,404 | 564 |
| Phil | 102 | 1,383 | 987 | 396 |
| Col | 93 | 1,290 | 925 | 365 |
| 1Thess | 88 | 1,271 | 867 | 404 |
| 2Thess | 47 | 703 | 493 | 210 |
| 1Tim | 110 | 1,398 | 1,063 | 335 |
| 2Tim | 80 | 1,044 | 776 | 268 |
| Titus | 46 | 588 | 453 | 135 |
| Phlm | 21 | 242 | 180 | 62 |
| Heb | 301 | 4,126 | 3,012 | 1,114 |
| Jas | 108 | 1,489 | 1,120 | 369 |
| 1Pet | 103 | 1,426 | 1,047 | 379 |
| 2Pet | 61 | 948 | 720 | 228 |
| 1John | 103 | 1,734 | 1,240 | 494 |
| 2John | 12 | 203 | 139 | 64 |
| 3John | 15 | 184 | 136 | 48 |
| Jude | 25 | 398 | 311 | 87 |
| Rev | 389 | 7,409 | 5,457 | 1,952 |
| **Total** | **7,605** | **111,410** | **81,509** | **29,901** |

## 6. Observation flagged for researcher confirmation — bulk-run timeline

`created_at` timestamps show all 27 NT books were built **today, 2026-08-09, in a single unbroken run from 06:00:34Z to 07:09:57Z** (~70 minutes), each book taking seconds (e.g. Matt: 06:00:34–06:00:44Z for 990 verses / 14,476 codes; Rev: 06:09:49–06:09:57Z for 389 verses / 7,409 codes). Each book also has exactly one rendered `report.verse_lexical` MD extract on disk under `iba/app/verse-analysis/{Book}/`, confirming the full `VerseLexical.ps1` pipeline (both steps) ran per book, not just `lexical.build`.

This is a mechanical, deterministic step (per the script's own docstring: "the mechanical T1–T3 engine" — role + morph-selected sense off existing `span`/`strong`/`strong_meaning_parsed` data, STEP called only for codes with no `strong` row yet), so a fast bulk run across 27 books is plausible without implying corner-cutting on this table specifically.

Flagging it anyway because memory `project_iba_study_reopened_20260805_v4` records the researcher reopening **the verse-lexical line specifically** on 2026-08-05 with instructions to proceed in **small dictated steps**, not self-synthesized bulk runs. I have no record in this session of having run this batch, and don't know if it was run by the researcher directly, by a separate session, or predates that instruction's intended scope (which may be about the interpretive T4–T9 debate layer downstream of this table, not this mechanical build step — the docstring language supports that reading, but I'm not asserting it). Worth a direct confirmation before this NT-wide `verse_lexical` base is treated as settled input to any downstream debate/synthesis work.
