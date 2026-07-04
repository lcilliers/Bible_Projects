# Project State Report — Soul Word Analysis Programme

- **Date:** 2026-07-04
- **Scope:** full-project state after completing the major prophets + backup cleanup.
- **Method:** all figures read live from `database/bible_research.db` (single source of truth); no estimates.

---

## 1. Headline

The **segmentation-first / chapter-driven inner-being reading** now covers **21 books — the entire poetic/wisdom corpus, Lamentations, all Twelve Minor Prophets, and all four Major Prophets (Isaiah, Jeremiah, Ezekiel, Daniel)**. That is **452 readings / ~397,000 words** of Phase-2 meaning-synthesis, filed as `prose_section` type `lexical_prose_chapter` (section_type_id 104). Coverage of non-T2 evidence verses is **complete (0 gaps)** for every segmentation-pipeline book; the two exceptions are explained in §4.

- **Schema:** v**3.37.0** (M63 applied 2026-07-02 — ve_lexical Phase 1: legacy rows archived to `ve_lexical_legacy`, live table = live model only).
- **Verse corpus:** 24,931 verses across all 66 books present.
- **Disk / backups:** `backups/` reduced 124 GB → **20 GB** this session (freed ~104 GB total); 147 GB free on C:. Two loop-invoked `_apply_*` scripts now self-prune their pre-op snapshots.

---

## 2. Pipeline output by book (section_type_id 104)

| Book | Readings | Chapters | Words | Non-T2 gaps |
|---|---:|---:|---:|---:|
| **Psalms** | 150 | 150/150 | 123,772 | chapter-granularity ✓ (see §4) |
| **Proverbs** | 31 | 31/31 | 32,201 | **2** (Pro 17:24, 30:31) |
| **Ecclesiastes** | 12 | 12/12 | 20,693 | 0 |
| **Job** | 42 | 42/42 | 49,990 | 0 |
| **Lamentations** | 5 | 5/5 | 9,293 | 0 |
| **Isaiah** | 64 | 66/66¹ | 52,141 | 0 |
| **Jeremiah** | 44 | 52/52¹ | 35,209 | 0 |
| **Ezekiel** | 26 | 48/48¹ | 20,844 | 0 |
| **Daniel** | 12 | 12/12 | 8,157 | 0 |
| **Hosea** | 14 | 14/14 | 6,200 | 0 |
| **Joel** | 3 | 3/3 | 2,435 | 0 |
| **Amos** | 8 | 8/8 | 5,457 | 0 |
| **Obadiah** | 1 | 1/1 | 807 | 0 |
| **Jonah** | 4 | 4/4 | 2,345 | 0 |
| **Micah** | 7 | 7/7 | 4,515 | 0 |
| **Nahum** | 3 | 3/3 | 1,903 | 0 |
| **Habakkuk** | 3 | 3/3 | 2,762 | 0 |
| **Zephaniah** | 3 | 3/3 | 2,399 | 0 |
| **Haggai** | 2 | 2/2 | 2,039 | 0 |
| **Zechariah** | 14 | 14/14 | 9,332 | 0 |
| **Malachi** | 4 | 4/4 | 4,424 | 0 |
| **TOTAL** | **452** | — | **396,918** | **2 real** |

¹ Reading-count < chapter-count because cross-chapter oracle/vision units are filed once at their anchor chapter (e.g. Ezekiel's Gog oracles 38–39 = one reading). Every chapter's verses are still covered — confirmed by the non-T2 gap check.

- **Segmentation units:** 671 across 20 books (Psalms excepted — see §4). Largest: Proverbs 251, Job 101, Isaiah 79, Jeremiah 46, Ezekiel 26.

---

## 3. Coverage integrity

A verse is an **evidence verse** if it carries at least one study term whose `mti_terms.cluster_code` is NULL or ≠ `T2` (T2 = reference/proper-noun terms that inflate coverage). Every such verse should be answered by a segment-unit and its reading.

**Result: 0 non-T2 coverage gaps across all segmentation-pipeline books** — the entire prophetic corpus (16 books), Job, Ecclesiastes, and Lamentations are watertight. Only Proverbs has 2 stray verses (§4).

---

## 4. Two accounting notes (not defects)

1. **Psalms is chapter-granularity, not verse-segmented.** The Psalter was completed under the earlier *chapter-driven* method (Phase-1 per-verse lexical + Phase-2 whole-chapter reading), which does **not** create `segment_unit`/`segment_unit_verse` rows. So the verse-level coverage check reports ~1,916 "uncovered" verses for Psalms — this is a **metric artifact**, not a gap: all **150/150 psalms have a complete whole-chapter reading**. If verse-level segment linkage is ever wanted for Psalms (for uniformity with the prophets), it would be a back-fill exercise, not new analysis.
2. **Proverbs — 2 genuine minor gaps:** **Pro 17:24** and **Pro 30:31**. These non-T2 evidence verses fell outside their chapter's segment units. Small, easily reconciled by extending the relevant unit's `verse_refs` and reloading (idempotent). *Recommend closing before the next book.*

---

## 5. Remaining scope (books with evidence, not yet read)

**Old Testament narrative/history (18 books):** Genesis (1,250 evidence verses), Exodus (793), Leviticus (688), Numbers (1,009), Deuteronomy (811), Joshua (387), Judges (556), Ruth (72), 1–2 Samuel (633/484), 1–2 Kings (496/439), 1–2 Chronicles (345/551), Ezra (142), Nehemiah (270), Esther (135). **+ Song of Solomon (93).**

**New Testament (27 books):** Gospels (Mat 733, Mar 429, Luk 740, Joh 473), Acts (603), Pauline + General epistles, Revelation (275). Total NT evidence-bearing verses across all 27 books.

These require the **narrative-scene / epistle-argument** genre handling (the pipeline already supports narrative scenes — used for Jonah, Daniel 1–6, Jeremiah's Baruch narratives, Ezekiel's sign-acts).

---

## 6. Synthesis products to date

- **Twelve Minor Prophets** cross-book inner-being synthesis (10 emergent operation-types + God-less coda): `verse-analysis/_synthesis/wa-minor-prophets-inner-being-operations-synthesis-20260704.md`.
- **Major Prophets** cross-book synthesis: *in progress this session* → `verse-analysis/_synthesis/wa-major-prophets-inner-being-operations-synthesis-20260704.md`.

---

## 7. Operational / housekeeping

- **Backups:** bucket B (transient AUDIT_WORD engine auto-snapshots + per-word pre-op copies + duplicate 07-04 snapshots) deleted — 24 files / 15 GB. Retained: 6 schema-migration markers (`pre_migration_v3.28–3.33`), the KEEP-RESET baseline, and recent full-DB restore points. `backups/` now 20 GB / 49 files.
- **Root-cause fix:** both loop-invoked filing scripts (`_apply_file_chapter_lexical_prose` and `_apply_backfill_chapter_verses`) now carry `--no-backup` + a self-pruning `snapshot_db()` helper (keep newest 2–3). The disk-full recurrence cannot repeat from these scripts.
- **Safety net:** live DB current + NAS daily DB backup (18:00) + git memory mirror.

---

## 8. Recommended next steps

1. **Close the 2 Proverbs gaps** (quick, closes OT poetic/prophetic coverage to 100% at verse level).
2. **Major-prophets synthesis** (this session).
3. Then choose the next corpus: **Song of Solomon** (small, poetic, completes the poetic books) or begin the **OT narrative books** (Genesis-first, narrative-scene genre) or the **Gospels**.
4. *(Optional/uniformity)* back-fill Psalms verse-level segment linkage if a single coverage metric across all books is wanted.
