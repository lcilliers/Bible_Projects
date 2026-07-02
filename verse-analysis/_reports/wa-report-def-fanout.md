# Report Definition — FANOUT (static lexicon substrate for a passage)

- **Type:** living definition spec · Version 2 · 2026-06-30 (reframed per architecture register §8)
- **Report class:** per-passage lexicon **snapshot** → versioned `-vN`, bump-on-change
- **Generator:** `scripts/_assess_verse_raw_data.py` (to be rebuilt to this spec)
- **Output path:** `verse-analysis/{Book}/wa-{book}-{chap}-{verse}-fanout-vN-YYYYMMDD.md` (named on the anchor verse)
- **Sample:** [SAMPLE-fanout-exo-001-013.md](samples/SAMPLE-fanout-exo-001-013.md)
- **Source of truth:** the DB only; read-only; never hand-edited.

---

## 1. Purpose
The **stable, static lexical picture for a passage** — the substrate the reading starts *from*. It holds only lexicon-type data, so it does not go stale when meaning changes. **Findings, observations, ve-narrations, logos and AI-chat are excluded** (they live in Passage_observation). This single boundary is what fixes the old fanout's "holds changing findings → always stale" failure.

## 2. Unit & input
- The unit is a **passage** (a verse-group), or a single verse where no group applies.
- Passage membership = a **group label on `wa_verse_records`** (DEC-1); members share the label. **Delimiting is a reading-time decision** by the researcher (split a group into separate fanouts when warranted); the driver is *the verses that form the end-to-end story for a characteristic*.
- Input: `--ref` / `--group`.

## 3. Sections (each header names its source table — DEC-8 applied here, where tracing is appropriate)
1. **Passage text** — *source `wa_verse_records`* (reference = the DB anchor each datapoint traces to).
2. **Morphology — every span, by verse** — *source `verse_span_index`*: surface, gloss, part, morph_code, stem, lemma. Each study-lemma also shows its **characteristic** (DEC-4: characteristic embedded in the fanout build via `primary_strong → characteristic`).
3. **Related verses by shared lemma** — *source `verse_term_index`* (DEC-2: shared primary lemma; index-not-census, anomalies accepted). Visualisation rule (see sample, open item #12): **≤12 verses → list all; >12 → in-study subset + remainder count, never a full dump.** Each related verse flags **anchor status**.
4. **Coverage note** — *computed*: content spans with no study lemma (untracked, not errors).

## 4. Anchor handling (DEC-3)
- Use an existing anchor where one exists (`verse_analysis_progress`); else one is chosen.
- **The fanout triggers anchor selection:** when §3.3 surfaces a related occurrence whose verse has **no anchor** and one cannot be auto-selected, a checking-possibilities step runs (researcher adjudicates).
- **An anchor may later change** — the repercussions (rebuild of dependent fanouts/links) must be understood and handled.

## 5. Versioning & filing
- Per-passage snapshot → **versioned `-vN`, bump-on-change**: regenerate, hash the DB-derived payload; write next `-vN` only if it differs; else no-op. Because content is static lexicon, versions move rarely. Superseded versions retained.

## 6. Constraints
- Static lexicon only; the exclusion in §1 is a hard rule.
- Every datapoint traceable to its source table + key (DEC-8, applied at section-header level here).
- Read-only; on-demand reproducible.

## 7. Build status & prerequisites
- **Generator to rebuild** to this spec. Prerequisites (architecture register §9): `wa_verse_records` group column (DEC-1); `primary_strong → characteristic` path (DEC-4); related-verse visualisation agreed (#12).

---

## Provenance — researcher comments that shaped this spec (verbatim)
issues eminating from previous work: a) verse is multi-dimensional (many terms; single or verse passage) · b) hard to read (codes versus text; overly technical) · c) incomplete (extracts/interpretations without base data) · d) does not include other verses · dd) hard to figure out where information comes from · e) not easily referencable · f) not cross indexed · ff) holds findings that change → cumbersome to keep current.
What is a fanout: represents a passage (group of verses) or single verse; captures the lexicon of all spans and builds the fanout for all related verses; if a related span has no anchor verse, the anchor must be determined; every datapoint must reference its source; **no findings, observations or other extracts — only static lexicon data**; section headers include source tables. Specifics: (a) verse text + neighbour for all, verse_record reference as DB anchor; (b) morphology for all spans by verse; (c) references of similar verses by morphology; (d) version control bump on change; (e) findings, observations, logos and ai-chat excluded.
