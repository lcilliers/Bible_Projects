# Passages — extract + a passage-reference field proposal

- **File:** wa-passages-extract-and-field-proposal-v1-20260701.md · **2026-07-01 · Author:** Claude Code · **status: extract + DRAFT proposal.**
- **Purpose:** answer "do we have a passage marker; how many passages, how big?" and design the researcher-requested **passage-reference field**.

## 1. The passage marker — what exists
- **The live marker = the `isolable` ve-lexical item (item 28).** `isolable='no'` on **5,406 verse-contexts** (2,775 distinct verses) means *"not self-contained — read WITH the preceding verse"* (the reset adjacency-checker, 2026-06-25). Notes are **backward-pointing**: 5,406 say "preceding"; only 4 "next", 1 "both", 41 "after".
- **`verse_context_group` is NOT it** — 4,155 rows, but **all bulk soft-deleted 2026-05-27** (legacy VCG cleared). Dead.
- **`verse_context.step_envelope_note`** — 0 populated. Dead.
- **So the marker is real but COARSE:** per-term (not per-verse), backward-only ("preceding"), and it stores **no explicit passage span** — a passage has to be *inferred* by chaining the backward links. This is why passages will need manual adjustment.

## 2. Passages compiled (from chaining `isolable='no'` backward links)
Method: aggregate `isolable='no'` to the **verse** level (a verse reads-back if any of its terms is flagged); a readback verse N links to its immediate canonical predecessor (N-1, same chapter); union the links into maximal runs; a **passage = a run of ≥2 verses**.

| metric | value |
|---|---|
| readback verses (verse-level) | **2,775** |
| **passages (≥2 verses)** | **2,182** |
| verses covered by passages | **4,894** (~25.5% of the 19,171 analysed verses) |
| verses / passage | min 2 · **median 2 · mean 2.2** · max 8 |
| primary (OWNER) terms / passage | min 0 · **median 4 · mean 4.6** · max 20 |
| cross-chapter readbacks (verse 1 → prior chapter) | **63** — flagged, not auto-joined |

**Size distribution (verses : passages):** 2→1,793 · 3→293 · 4→67 · 5→18 · 6→7 · 7→3 · 8→1.
**Largest:** Luk 1:43-50 (8v/14 terms) · Act 1:15-21 (7v/**20 terms**) · Mar 14:31-37 (7v/11) · Mar 10:43-49 (7v/9).

**Read: passages are small and numerous** — 82% are just 2-verse pairs; nothing exceeds 8 verses. So manual adjustment is a per-passage review of ~2,182 mostly-tiny units, not a few huge ones.

## 3. Caveats (why manual adjustment is needed)
1. **Backward-only + coarse.** The marker says "read with the preceding verse" — no forward links, no explicit span. Chains approximate the true passage.
2. **63 cross-chapter cases** (a verse-1 reading with the prior chapter's last verse) are flagged, not auto-joined — need manual handling.
3. **Per-term aggregation.** A verse can be readback on one term and isolable on another; I treated *any* readback term as making the verse readback.
4. **Immediate-predecessor assumption.** "The preceding verse" is taken as verse_num−1; occasionally the real link is wider (the exegesis gate could exceed ±1).

## 4. Proposal — a passage-reference field
The researcher asked to **add a passage-reference field on the verse-record.** Design decision — **where it lives:**

- **Recommended — on the `verse` master index** (`verse.passage_ref` TEXT, or a `passage_id` FK to a small `passage` table). Passage is a **verse-level** property (independent of term), so one row per verse is the normalised home; `wa_verse_records` reaches it via `verse_id`. No duplication.
- **As suggested — on `wa_verse_records`** (`passage_ref` TEXT). Matches the researcher's words, but `wa_verse_records` is **per-term**, so every term-row of a verse repeats the same passage_ref (denormalised; edits must touch all of a verse's rows).

**Recommended shape — a `passage` table + FK** (cleanest for manual adjustment):
```
passage(id, ref TEXT, book_id, start_chapter, start_verse, end_chapter, end_verse,
        source TEXT ['auto'|'manual'], notes TEXT, created_at)
verse.passage_id  INTEGER  -> passage.id      (one passage per verse)
```
- **Populate** from §2 (the 2,182 auto-passages, `source='auto'`), leaving singletons NULL.
- **Manual adjustment** then edits the `passage` table (merge/split/extend) — a first-class, auditable object, not a string smeared across term-rows.
- A denormalised `passage_ref` string can still be mirrored onto `wa_verse_records` later if a flat field is wanted for extracts.

## 5. Decisions needed before building
1. **Field home** — `verse.passage_id` + `passage` table (recommended) vs a flat `passage_ref` on `wa_verse_records` (as suggested).
2. **Auto-populate now** from the 2,182 computed passages, or leave the field empty for manual entry?
3. **Cross-chapter 63** — auto-join across chapter boundaries, or leave for manual review?

---

## 6. REVISED design (per researcher corrections, 2026-07-01)

Supersedes §4's "where it lives" reasoning. Corrections received:

- **(a) The ve-lexical is VERSE-FIRST.** The verse is the top lexical unit → a list of terms (each a full per-term lexical) **plus verse-level elements that are not per-term**. Passage is one such **verse-level** element. (My earlier "repeats across term-rows" reasoning was wrong-framed — see memory `project_ve_lexical_is_verse_first`.)
- **(b) Auto-populate** the passages, **isolating the exceptions** (cross-chapter + extended) for individual review.
- **(c) Passage anchor = the FIRST verse.** Only the first verse links to a ve-id; its ve-lexical carries records for **ALL terms across ALL verses in the passage** (the passage is read as one consolidated lexical unit).

### Confirmed schema
```
passage(
  id            INTEGER PK,
  ref           TEXT,          -- "Luk 1:43-50"
  anchor_verse_id INTEGER,     -- FK verse.id = FIRST verse (carries the ve-id + consolidated lexical)
  book_id, start_chapter, start_verse, end_chapter, end_verse,
  verse_count   INTEGER,
  source        TEXT,          -- 'auto' | 'manual'
  review_flag   TEXT,          -- NULL | 'cross-chapter' | 'extended' | 'direction-anomaly'
  notes TEXT, created_at TEXT )
verse.passage_id  INTEGER  FK -> passage.id      -- every member verse points to its passage
```
- Verse-level home (on `verse`), matching (a). `anchor_verse_id` encodes (c).

### Populate plan (from §2)
- **Auto (`source='auto'`, no review_flag):** the clean adjacent **2–3 verse** passages (~2,086).
- **Created but flagged for review (`review_flag` set):**
  - `cross-chapter` — the **63** verse-1→prior-chapter cases.
  - `extended` — passages **≥4 verses** (~93) — longer chains, higher error risk.
  - `direction-anomaly` — the ~46 notes saying next/both/after (not "preceding").
- Thresholds adjustable — say the word to move the "extended" line.

### Build = schema migration + populate (backup + dry-run + verify, as usual)
1. migration: create `passage`, add `verse.passage_id` (via engine `--migrate` or a guarded `_apply_` script).
2. populate auto-passages + flag exceptions.
3. report: counts written, exceptions isolated.
