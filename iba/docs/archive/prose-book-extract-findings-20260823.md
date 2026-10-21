# Prose book extract — `Findings` (structure only, no body text)

**Escalation #784.** Companion to the `Detail design` extract. Same discipline: structure and
rollup numbers from `prose_section_type` + aggregate counts, no body text. Live queries against
`bible_research.db`, run 2026-08-23.

---

## 1. Book-level summary

| Metric | Value |
|---|---|
| Section-types defined | 6 |
| Types with zero populated content | **0 of 6** — every defined type is in active use |
| Current (active, non-superseded) `prose_section` rows | 583 |
| Superseded (historical) rows | **0** — nothing here has ever been revised |
| Total current-row body size | ~5.8M characters |
| Scope: per-word rows | 1 |
| Scope: programme/cluster-wide rows | 582 |
| Status: `approved` | 583 (100%) |
| Status: `draft` | 0 |
| Author: `claude_code` | 583 (100%) |
| Author: `claude_ai` | 0 |

**Reading this — the opposite character to `Detail design` in almost every respect:** nothing
unused, nothing superseded, nothing in draft, and — notably — **zero rows authored by Claude AI**.
Every row here was written by Claude Code, all already `approved`. That's an unusual profile for a
book named "Findings" if the expectation is analytical/interpretive content; see §3.

---

## 2. Section-type extract, by source stage

### `synthesis` (3 types, 13 rows, ~120K chars — the small end of this book)

| code | label | rows | chars | description |
|---|---|---:|---:|---|
| `lexical_synthesis_psalter` | Psalter inner-being synthesis (per characteristic) | 1 | 21,026 | Psalter inner-being synthesis (per characteristic) |
| `lexical_synthesis_psalter_essay` | Psalter inner-being synthesis — ESSAY (story voice) | 2 | 29,153 | Psalter inner-being synthesis — ESSAY (story voice) |
| `ib_characteristic_discovery` | Inner-being characteristic — discovery document | 10 | 69,860 | Inner-being characteristic — discovery document |

Small, Psalms-scoped, exploratory-reading in its own descriptions ("discovery document," "essay —
story voice"). Looks like early trial output for the current lexical method, scoped to one book of
the Bible.

### `verse-analysis` (3 types, 570 rows, ~5.7M chars — the bulk of this book)

| code | label | rows | chars | description |
|---|---|---:|---:|---|
| `lexical_prose` | Lexical Prose (single-term story) | 1 | 2,834 | The accepted single-term first-tier story built from lexical-model-2026 ve-records only (method v1-20260702). One per owner term. |
| `lexical_prose_chapter` | Lexical Prose (chapter reading) | **452** | **2,519,276** | Whole-chapter inner-being reading for poetic books (Psalms/Proverbs), built from lexical-model-2026 Phase-1 lexicals. Multi-characteristic. One per book+chapter. |
| `lexical_prose_passage` | Lexical Prose (passage reading) | **117** | **1,202,980** | Per-passage inner-being reading for narrative books, built from verse-first lexicals over an operation-web passage (segment_unit). Multi-characteristic. One per unit_code. |

452 + 117 + 1 = 570 of this book's 583 rows (98%) sit here, and their own descriptions name the
**current, live method directly** — `lexical-model-2026`, `method v1-20260702`, `verse-first
lexicals`, `operation-web passage` — the terminology CLAUDE.md's top banner names as the *live*
verse-first/passage/term-driven method (2026-07-02 onward), not anything superseded.

---

## 3. What this adds up to — and why it matters for the `Detail design` comparison

**This book is not in the same category as `Detail design`.** Where `Detail design` is old-pipeline
content (Session A–D, superseded 2026-06-25, mostly unused scaffolding, a small uneven pilot),
`Findings` is **predominantly current-method output**: 570 of 583 rows are `lexical_prose*` content
whose own descriptions cite the live lexical-model-2026 / verse-first method by name. Whatever
question gets asked about `Detail design`'s disposition, it is a **different question** for
`Findings` — this book is closer to "what the current method has actually produced so far" than to
"legacy content from an abandoned pipeline."

**The `author='claude_code'` / `status='approved'` uniformity — checked, not left open.** Searched
for what actually writes `lexical_prose*` rows: not `iba/app/handlers/lexical.py` or any current
IBA code (no hits at all) — the writers are two one-off scripts,
`scripts/_apply_file_chapter_lexical_prose_v1_20260702.py` and
`_apply_file_passage_lexical_prose_v1_20260704.py`, both already `inactive=1` in `cfg_utility`, both
dated July 2026, predating the current IBA rebuild. Read the first one directly: its INSERT
statement hardcodes `'approved'` and `'claude_code'` as literal values —
`(None,tid,HEADING,body,wc,'approved',new_ver,prev['id'] if prev else None,'claude_code',NOW,meta,STORY)`.
**"Approved" here is not a researcher-review signal — it's a constant the script always wrote,
regardless of whether anyone looked at the content.** The 583-row uniformity isn't evidence of
uniform quality; it's evidence of a mechanical stamp. This matters directly for treating this book's
content as trustworthy: it's current-method output (§3 above still holds — the terminology and
method really are live), but "approved" doesn't mean reviewed here the way it would in a book where
that status is set by an actual approval action.
