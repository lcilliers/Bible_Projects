# ve_lexical per-book census (DB extraction only)

> Researcher request (2026-07-05): *"for each book, extracting from the DB only, count unique verse/passage ve-lexical records per span, and dimensions per verse/passage."*
> Source: `ve_lexical` (active rows only), keyed span → verse → book via `verse_span_index`. 99.99% of `ve_lexical` rows are span-keyed (`verse_span_id`), so the span join is authoritative. Tool: `scripts/_probe_ve_lexical_per_book_census_v1_20260705.py`. Extraction date 2026-07-05.

**Columns:** records = active `ve_lexical` rows · spans = distinct `verse_span_id` coded · verses = distinct verses touched · passages = distinct `passage_id` touched · dims = distinct dimensions (`ve_nr`) · rec/span = records per coded span · dim/vs = avg distinct dimensions per coded verse · dim/psg = avg distinct dimensions per coded passage.

## A. Books WITH ve_lexical coding

| Book | records | spans | verses | passages | dims | rec/span | dim/vs | dim/psg |
|---|---|---|---|---|---|---|---|---|
| Exodus | 327 | 63 | 8 | 1 | 13 | 5.19 | 8.8 | 13.0 |
| Leviticus | 7,778 | 1,172 | 648 | 104 | 23 | 6.64 | 7.3 | 10.5 |
| Job | 24,420 | 5,450 | 1,070 | 97 | 14 | 4.48 | 6.7 | 11.5 |
| Psalms | 73,220 | 14,974 | 2,461 | 314 | 14 | 4.89 | 7.6 | 11.9 |
| Proverbs | 24,045 | 5,610 | 915 | 71 | 14 | 4.29 | 7.0 | 12.0 |
| Ecclesiastes | 9,108 | 2,063 | 222 | 25 | 14 | 4.41 | 7.9 | 11.8 |
| Isaiah | 55,563 | 11,944 | 1,291 | 107 | 13 | 4.65 | 7.8 | 12.0 |
| Jeremiah | 75,702 | 14,922 | 1,362 | 152 | 13 | 5.07 | 8.6 | 11.8 |
| Lamentations | 5,816 | 1,175 | 154 | 17 | 14 | 4.95 | 8.0 | 10.6 |
| Ezekiel | 61,809 | 13,589 | 1,273 | 152 | 13 | 4.55 | 7.9 | 11.0 |
| Daniel | 16,770 | 4,184 | 357 | 29 | 13 | 4.01 | 6.8 | 9.6 |
| Hosea | 7,899 | 1,598 | 197 | 17 | 13 | 4.94 | 7.9 | 11.9 |
| Joel | 3,462 | 742 | 73 | 11 | 13 | 4.67 | 8.3 | 11.3 |
| Amos | 7,539 | 1,495 | 146 | 23 | 13 | 5.04 | 8.5 | 11.1 |
| Obadiah | 1,111 | 219 | 21 | 3 | 13 | 5.07 | 9.0 | 12.3 |
| Jonah | 2,292 | 465 | 48 | 6 | 13 | 4.93 | 8.4 | 12.2 |
| Micah | 4,692 | 969 | 105 | 10 | 13 | 4.84 | 8.3 | 12.1 |
| Nahum | 1,933 | 415 | 47 | 6 | 13 | 4.66 | 8.0 | 11.8 |
| Habakkuk | 2,123 | 461 | 56 | 6 | 13 | 4.61 | 7.6 | 11.5 |
| Zephaniah | 2,698 | 556 | 53 | 5 | 13 | 4.85 | 8.2 | 12.4 |
| Haggai | 1,942 | 412 | 38 | 4 | 13 | 4.71 | 8.1 | 11.2 |
| Zechariah | 10,884 | 2,217 | 211 | 30 | 13 | 4.91 | 8.3 | 11.3 |
| Malachi | 2,839 | 585 | 55 | 5 | 13 | 4.85 | 8.7 | 12.0 |
| **TOTAL** | **403,972** | **85,280** | **10,811** | | | | | |

## B. Books with ZERO ve_lexical coding (no rows in the table)

Genesis · Numbers · Deuteronomy · Joshua · Judges · Ruth · 1 Samuel · 2 Samuel · 1 Kings · 2 Kings · 1 Chronicles · 2 Chronicles · Ezra · Nehemiah · Esther · Song of Solomon.

(NT excluded per instruction — not yet started.)

## C. What the numbers state (facts only)

- **All coded books are the poetic/prophetic set + Leviticus.** These are the books that ran through an **index-driven** build (`verse_span_index`) — the poetic method and the Leviticus loader.
- **Genesis = 0 ve_lexical records.** The entire Genesis narrative reading (69 passages) produced **no lexical span-coding in the DB** — it exists only as `prose_section` (type 108).
- **Exodus = 327 records / 63 spans / 8 verses / 1 passage.** That is **only the ruthlessness pilot** (Exo 1:11–14, `perek`) from 2026-07-02 — **not** the Exodus narrative reading. The Exodus narrative (48 passages) likewise produced only `prose_section`, no `ve_lexical`.
- **Every other narrative book** (Numbers → Esther) and Song of Solomon = 0 ve_lexical: not yet read.
- **Dimensions:** the poetic/prophetic books carry **13–14** distinct dimensions; **Leviticus carries 23** (it used the extended axis/polarity/reset dimension set). Per coded verse, ~7–9 distinct dimensions; per coded passage, ~10–13.

*Filed 2026-07-05 as a factual DB extraction. Companion to the root-cause anchor (`wa-root-cause-what-and-when-the-script-went-wrong-20260705.md`) and the verse-record completeness assessment (`wa-verse-record-completeness-impact-assessment-20260705.md`).*
