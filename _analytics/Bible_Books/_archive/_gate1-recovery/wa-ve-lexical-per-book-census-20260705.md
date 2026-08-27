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

---

## D. Primary spans, and how many were referenced in the actual prose (extension, 2026-07-05)

**Definitions.** *Primary span* = distinct `ve_lexical.verse_span_id` with `gate='1-primary'` (Gate 1 — the span is a tagged term). *Referenced in prose* = the span's lexicon **transliteration** (dots stripped, whole-word) appears in the body of a prose reading (type 104 poetic / 108 narrative) that covers the span's verse.

**Read this as a LOWER BOUND.** There is **no structural link** in the DB between `ve_lexical` and `prose_section` — the prose was authored as free text. The poetic readings cite inner-being operations by **English concept + verse number**, *not* by transliteration (verified across the corpus). So the transliteration match counts only spans cited by *lexical identity*; spans referenced by their English gloss are not captured and the true "concept-referenced" figure is higher but not cleanly extractable. Tool: `scripts/_probe_primary_span_prose_reference_v1_20260705.py`.

| Book | primary spans | verse has prose | translit in prose | % translit-ref |
|---|---|---|---|---|
| Exodus | 19 | 19 | 18 | 94.7% |
| Leviticus | 18 | 0 | 0 | 0.0% |
| Job | 1,275 | 1,275 | 384 | 30.1% |
| Psalms | 3,925 | 3,925 | 260 | 6.6% |
| Proverbs | 1,796 | 1,796 | 20 | 1.1% |
| Ecclesiastes | 464 | 464 | 29 | 6.2% |
| Isaiah | 2,470 | 2,432 | 45 | 1.8% |
| Jeremiah | 2,042 | 1,710 | 2 | 0.1% |
| Lamentations | 270 | 270 | 113 | 41.9% |
| Ezekiel | 1,552 | 1,005 | 1 | 0.1% |
| Daniel | 533 | 533 | 0 | 0.0% |
| Hosea | 340 | 340 | 17 | 5.0% |
| Joel | 93 | 93 | 0 | 0.0% |
| Amos | 184 | 161 | 4 | 2.2% |
| Obadiah | 21 | 21 | 0 | 0.0% |
| Jonah | 79 | 79 | 10 | 12.7% |
| Micah | 190 | 190 | 7 | 3.7% |
| Nahum | 74 | 74 | 1 | 1.4% |
| Habakkuk | 92 | 92 | 1 | 1.1% |
| Zephaniah | 98 | 98 | 7 | 7.1% |
| Haggai | 46 | 46 | 0 | 0.0% |
| Zechariah | 293 | 293 | 7 | 2.4% |
| Malachi | 115 | 115 | 28 | 24.3% |
| **TOTAL** | **15,989** | **15,031** | **954** | **6.0%** |

**What the numbers state (facts only):**
- Of **15,989 primary spans**, only **954 (6.0%)** have their transliteration cited in the prose that covers their verse. The poetic prose does **not** reference the coded primary spans by lexical identity — it works at the concept level, so this is a floor, not the full picture.
- **One fully clean signal:** `primary spans − verse-has-prose = 15,989 − 15,031 = 958` primary spans sit in verses that have **no filed prose reading at all** — definitively unreferenced (no prose exists to reference them). Concentrated in **Jeremiah (332), Ezekiel (547), Isaiah (38), Amos (23)**: coded verses with no reading on file.
- The two books with high translit-match are the ones whose prose *is* span-and-translit-level: **Exodus** (94.7% — but these are only the 19 spans of the ruthlessness pilot, whose reading cites translits) and **Job / Lamentations / Malachi** (30–42% — readings that happen to cite more Hebrew).
- **Leviticus:** its 18 `gate='1-primary'` spans are residual old-model rows (the terminology study wrote `gate=NULL`), and its prose is synthesis-type, not 104/108 — hence 0 here.

**Bottom line:** the primary-span layer (`ve_lexical`) and the prose layer are **two disconnected stores**. At most 6% of primary spans are traceable into the prose by transliteration, and ~958 are in verses with no prose at all. A clean per-span "referenced?" answer is not recoverable from the DB because the link was never recorded.

---

*Filed 2026-07-05 as a factual DB extraction. Companion to the root-cause anchor (`wa-root-cause-what-and-when-the-script-went-wrong-20260705.md`) and the verse-record completeness assessment (`wa-verse-record-completeness-impact-assessment-20260705.md`).*
