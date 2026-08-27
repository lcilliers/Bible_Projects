# Verse-record completeness — impact assessment (the honest one)

> Prompted by the researcher (2026-07-05): *"the rule was simple — the verse-record is not complete, the span of each verse must come into focus, and any span that is IB-related that is not in the verse-record must be added. Give me a report on all the verses that were added since we started with book analysis, by book, by span, by number of verses added in the verse-record."*
>
> This report answers that question with database facts, and then states the true impact — because the answer to the question is the problem.

---

## 1. The direct answer: how many verses/spans were ADDED to `wa_verse_records` during book analysis

**Zero. In every one of the 66 books.**

`wa_verse_records.created_at` — the creation stamp of each verse-record row — has **no row created on or after 2026-07-01** in any book. The book-reading phase began **2 July 2026** (poetic method) and **4 July** (narrative). The newest verse-record rows in the entire database predate the reading phase (latest `created_at` = 2026-06-29, from the mid-June VE-grounding work).

| Signal | Value |
|---|---|
| verse-records created ≥ 2026-07-01 (all books) | **0** |
| newest `created_at` anywhere | 2026-06-29 (pre-reading) |
| what the reading phase *did* write to `wa_verse_records` | only `updated_at` / `analysis_marker` / `incorporated_in` on **existing** rows (marking, not adding) |

So the foundational rule — *"any IB span not in the verse-record must be added to the verse-record"* — **was never operationalised into the verse-record.** Not for the narratives, not for the poetic/prophetic books, not for Leviticus. The verse-record is still the March–June STEP-extraction seed, untouched by everything the reading discovered.

**Where the discovered evidence actually went** (instead of the verse-record):
- narrative readings → `prose_section` (type 108), built *off the seed* — so they never even saw the orphans;
- poetic/prophetic readings → `ve_lexical` + `analysis_marker`/`incorporated_in` marks on existing records — index-driven, but additions went to `ve_lexical`, not the verse-record;
- my Gate-1 "remediation" this session → `ve_lexical` + `mti_terms` — **the same detour.** I did not add a single span to `wa_verse_records` either.

That is the pattern the researcher named: the fix keeps landing somewhere *other* than the source of truth, so no single table holds "what verses are IB-related." A report pulling from `wa_verse_records` sees the March seed; a report pulling from `ve_lexical` sees a different, partial set; they disagree, and neither is authoritative.

---

## 2. The size of the gap: what SHOULD have been added but wasn't (per book)

Candidate IB span-orphans = content-word Strong's that appear in the full word index (`verse_span_index`) but are **not** registered in `wa_verse_records` for that book, gloss-filtered for inner-being relevance. (Heuristic — over-inclusive; genuine count after human review runs ~30–40% of candidates, per the Genesis/Exodus/Leviticus reviews already done. Treat these as the *review queue*, not the final count.)

Produced by `scripts/_probe_verse_record_orphan_census_v1_20260705.py` (read-only).

| Book | reg | un-reg | **IB-orphan terms** | orphan span-tokens | verses touched |
|---|---|---|---|---|---|
| Genesis | 375 | 1377 | 45 | 424 | 358 |
| Exodus | 284 | 1107 | 54 | 274 | 241 |
| Leviticus | 203 | 659 | 47 | 280 | 238 |
| Numbers | 288 | 905 | 37 | 216 | 194 |
| Deuteronomy | 320 | 969 | 55 | 262 | 242 |
| Joshua | 162 | 679 | 22 | 86 | 72 |
| Judges | 248 | 878 | 36 | 161 | 150 |
| Ruth | 68 | 218 | 9 | 35 | 22 |
| 1 Samuel | 274 | 825 | 48 | 222 | 201 |
| 2 Samuel | 248 | 762 | 43 | 433 | 348 |
| 1 Kings | 211 | 814 | 29 | 332 | 270 |
| 2 Kings | 205 | 790 | 31 | 329 | 251 |
| 1 Chronicles | 189 | 745 | 33 | 178 | 156 |
| 2 Chronicles | 256 | 877 | 36 | 371 | 318 |
| Ezra | 140 | 574 | 23 | 133 | 109 |
| Nehemiah | 216 | 663 | 21 | 133 | 116 |
| Esther | 104 | 318 | 12 | 202 | 131 |
| Job | 466 | 1178 | 70 | 224 | 222 |
| Psalms | 556 | 1579 | 93 | 715 | 694 |
| Proverbs | 393 | 924 | 73 | 344 | 335 |
| Ecclesiastes | 159 | 392 | 34 | 126 | 113 |
| Song of Solomon | 79 | 335 | 13 | 29 | 28 |
| Isaiah | 608 | 1804 | 98 | 478 | 453 |
| Jeremiah | 473 | 1387 | 76 | 735 | 650 |
| Lamentations | 182 | 395 | 33 | 45 | 45 |
| Ezekiel | 325 | 1345 | 74 | 535 | 491 |
| Daniel | 261 | 820 | 37 | 428 | 346 |
| Hosea | 236 | 480 | 28 | 97 | 90 |
| Joel | 79 | 307 | 8 | 11 | 11 |
| Amos | 150 | 478 | 25 | 55 | 54 |
| Obadiah | 28 | 130 | 6 | 7 | 7 |
| Jonah | 64 | 172 | 6 | 9 | 9 |
| Micah | 184 | 381 | 20 | 35 | 35 |
| Nahum | 100 | 243 | 7 | 9 | 7 |
| Habakkuk | 120 | 261 | 14 | 16 | 16 |
| Zephaniah | 100 | 257 | 17 | 24 | 24 |
| Haggai | 58 | 141 | 8 | 15 | 10 |
| Zechariah | 170 | 534 | 26 | 63 | 61 |
| Malachi | 108 | 198 | 14 | 24 | 20 |
| **TOTAL (OT)** | | | **1,361** | **8,095** | **7,138** |

(NT books use Greek Strong's and need the same census with a Greek gloss lexicon — not run here.)

**Reading the numbers:** ~1,361 candidate IB terms across the OT, ~8,095 span-occurrences, touching ~7,138 verses, are inner-being-relevant in the text but absent from the verse-record. After human review (the Gate-1 step), the *genuine* gap is smaller — my three completed reviews suggest roughly **one-third genuine**, i.e. on the order of **~450 terms / ~2,500–3,000 spans / ~2,500 verses** that genuinely belong in the verse-record and are not there. Leviticus still shows 47 candidates / 238 verses *even though I "fixed" it twice this session* — because those fixes went to `ve_lexical`, not `wa_verse_records`. That row is the proof of the problem.

---

## 3. Root cause — why zero were ever added

The reading pipeline never had an *"add orphan span to `wa_verse_records`"* step:

- **Narrative readings** were built *from* `wa_verse_records` (the seed) → they never queried the full index → orphans were invisible, so nothing was even flagged to add.
- **Poetic/prophetic readings** queried `verse_span_index` (the index) → they *could* see orphans → but their output went to `ve_lexical` and to `incorporated_in`/`analysis_marker` marks on existing rows. No new verse-record rows were created.
- **The coverage gate** (`_check_passage_reading_coverage`) checks the reading against `wa_verse_records` — i.e. against the seed. So it can report "CLEAN" while the passage's real IB spans sit un-added in the index. **The gate is circular**: it verifies coverage of the seed, not of the text.
- **My remediation** added to `ve_lexical`/`mti_terms` and re-ran that same circular gate.

So "CLEAN" and "complete" have, throughout the reading phase, meant *"complete with respect to the March seed,"* not *"complete with respect to the text."* That is the gap between what was reported and what holds the truth.

---

## 4. What a PROPER fix requires (no more detours)

Stated plainly so the decision is yours, with the full scope visible:

1. **Re-base the gate on the index.** The coverage gate must diff each passage against `verse_span_index` (the text), not `wa_verse_records` (the seed). Until it does, no "CLEAN" is trustworthy. *(This is the single highest-leverage change — it stops the circularity at source.)*
2. **Add the reviewed orphans to `wa_verse_records`** — a real ADD (term_id, span, morph, verse_id, provenance) per book, after human review of the census queue in §2. This is the operation the original rule specified and that never ran. It is book-by-book across the whole OT (+ NT with the Greek census).
3. **Reconcile the detour data.** The IB spans already coded in `ve_lexical` (Leviticus) and onboarded to `mti_terms` (this session) must *drive* the verse-record adds (or be recognised as the same evidence), so the two stores agree and the verse-record becomes authoritative.
4. **Only then re-derive insights/reports** — because only then does one table hold the truth.

This is a systemic remediation, not a spot-fix, and it should be done as one disciplined pass (gate re-based first, then per-book verse-record completion), not patched book-by-book as issues surface.

---

*Filed 2026-07-05. Census tool: `scripts/_probe_verse_record_orphan_census_v1_20260705.py`. This report supersedes the narrower Gen/Exod recovery framing of `wa-gen-exod-gate1-recovery-20260705.md` — the problem is programme-wide, and the verse-record, not `ve_lexical`, is where the fix has to land.*
