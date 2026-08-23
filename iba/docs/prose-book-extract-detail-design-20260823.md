# Prose book extract — `Detail design` (structure only, no body text)

**Escalation #784.** Requested directly: an extract + summary of `prose_section_type` for
`Detail design` and `Findings`, structure only — no `prose_section` body text. This file covers
`Detail design`; see the companion file for `Findings`. All numbers below are live queries against
`bible_research.db`, run 2026-08-23.

---

## 1. Book-level summary

| Metric | Value |
|---|---|
| Section-types defined | 45 |
| Types with zero populated content (dictionary-only, never used) | **26 of 45** |
| Current (active, non-superseded) `prose_section` rows | 169 |
| Superseded (historical) rows | 20 |
| Total current-row body size | 6.4M characters |
| Scope: per-word rows | 140, across only **20 distinct registry words** |
| Scope: programme/cluster-wide rows | 29 |
| Status: `approved` | 134 |
| Status: `draft` | 35 |
| Author: `claude_code` (mechanical) | 120 |
| Author: `claude_ai` (analytical) | 49 |

**Reading this:** the registry holds ~200 words. This book's per-word content covers **20** of them
— a pilot subset, not comprehensive. Of those 20, only **4** made it past the Session A mechanical
stage into Session B analysis (`sb_*` types below). Over half the defined types (26/45) were never
populated at all — pure scaffolding for a pipeline stage that stopped running.

---

## 2. Section-type extract, by source stage

Columns: current rows / superseded rows / total chars (current rows only) / distinct words. A
`description` is shown only where the type carries one (most `sa_*`/`sb_*`/`sd_*` types don't — they
predate the description field being used).

### `programme` (1 type)

| code | label | ch. | rows | superseded | chars | words | description |
|---|---|---|---:|---:|---:|---:|---|
| `prog_purp_observations_framework` | The Observations Framework — First Tier | 1 | 1 | 0 | 21,706 | 0 | The observation framework defining T0–T7 scope for every characteristic studied. |

### `session_a` — mechanical extracts (6 types, all 20/20 populated)

| code | label | ch. | rows | superseded | chars | words |
|---|---|---|---:|---:|---:|---:|---:|
| `sa_s1_d1` | Word Summary | 1 | 20 | 0 | 29,947 | 20 |
| `sa_s1_d2` | Meaning | 2 | 20 | 0 | 259,026 | 20 |
| `sa_s1_d3` | Verses | 3 | 20 | 0 | 1,431,839 | 20 |
| `sa_s1_d4` | Terms | 4 | 20 | 0 | **2,110,846** | 20 |
| `sa_s1_d5` | Pointers | 5 | 20 | 0 | 201,373 | 20 |
| `sa_s1_d6` | Questions | 6 | 20 | 0 | 715,911 | 20 |

`sa_s1_d4` (Terms) alone is 2.1M characters — a third of this entire book's content, for 20 words.

### `session_b` — analytical output (5 types, all only 4/20 populated)

| code | label | ch. | rows | superseded | chars | words |
|---|---|---|---:|---:|---:|---:|---:|
| `sb_s2c_ch1` | Word Characteristic Summary | 1 | 4 | 1 | 21,496 | 4 |
| `sb_s2c_ch2` | Word Impact Description | 2 | 4 | 1 | 23,281 | 4 |
| `sb_s2c_ch3` | Annotated Verse Evidence | 3 | 4 | 1 | 45,171 | 4 |
| `sb_s2c_ch4` | Original Language Vocabulary | 4 | 4 | 1 | 18,815 | 4 |
| `sb_s2c_ch5` | Connections | 5 | 4 | 1 | 22,538 | 4 |

### `session_b_phase9` — **all 11 types empty, 0 rows**

`sc_v2_tier_T0` through `_T7` (8 types) + `sc_v2_synth_opening`/`_divine_pattern`/`_appendix` (3
types). Each carries a real `description` (a per-tier/synthesis publication-prose spec) but **none
were ever populated**. This is a designed-but-abandoned stage — the description text reads as a
complete, thought-through spec (batch structure, prompt counts, which Session C chapter consumes
each), not a stub.

### `session_c` — two generations, only the newer one populated

**`sc_v1` (5 types) — superseded design, all 5 empty (0 rows).** `sc_v1_ch1`–`ch5` (Synopsis,
Description, Inner being at work, At work in scripture, Lexicon) — replaced by `sc_v2` before ever
being used.

**`sc_v2` (7 types) — the only fully-populated Session C generation, 4 rows each, cluster-scoped
not word-scoped (`distinct_words: 0` — `registry_id` is null on these rows):**

| code | label | ch. | rows | superseded | chars | expected length |
|---|---|---|---:|---:|---:|---|
| `sc_v2_ch1` | What this study is | 1 | 4 | 2 | 122,501 | 300–500 |
| `sc_v2_ch2` | The characteristics in this study | 2 | 4 | 2 | 191,120 | 200–400 |
| `sc_v2_ch3` | The divine pattern | 3 | 4 | 2 | 144,343 | 1500–2500 |
| `sc_v2_ch4` | Where each characteristic lives in the person | 4 | 4 | 3 | 144,135 | 800–1500 |
| `sc_v2_ch5` | How each characteristic works | 5 | 4 | 2 | 141,633 | 800–1500 |
| `sc_v2_ch6` | How each characteristic relates to the others | 6 | 4 | 2 | 116,627 | 400–800 |
| `sc_v2_ch7` | The view from outside Scripture | 7 | 4 | 2 | 103,456 | 400–500 |

Only 4 rows per chapter, well over the stated length target per row (e.g. ch3 averages ~36K chars
against an 1,500–2,500-char target — roughly 15–20× the spec) — consistent with these being
**cluster-level drafts** (the M09/Humility chapter draft sampled earlier), not individual
per-characteristic prose sized to the type's own `expected_length` guide.

### `session_d` — **all 10 types empty, 0 rows**

`sd_synthesis_Cl1` through `Cl10` — one per named cluster (Moral Character, Cognition, Volition,
Relational Disposition, Divine-Human Correspondence, Agency, Dependence, Emotion, Vitality,
Transformation). Defined, never populated.

---

## 3. What this adds up to

- **26 of 45 types (58%) are pure unused scaffolding** — `session_b_phase9` (11) and `session_d`
  (10) entirely, plus `sc_v1` (5). Real design work went into these (the phase9 descriptions in
  particular are detailed specs), but none of it was ever run.
- **The populated content is a small, uneven pilot**: 20 words got Session A; 4 of those 20 got
  Session B; the Session C content that exists is cluster-level (4 cluster drafts), not
  individual-word studies at all.
- **This is unambiguously old-pipeline content** — the Session A→B→C→D structure this book's types
  are named after is the pre-reset method (superseded 2026-06-25 per the CLAUDE.md method-reset
  banner). Nothing here uses the current verse-first/passage/lexical-model-2026 method's vocabulary.
