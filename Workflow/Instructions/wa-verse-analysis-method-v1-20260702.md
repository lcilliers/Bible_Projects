# Verse-analysis method — v1 (the live lexical process, 2026-07-02)

> The authoritative method for producing the verse-lexical under the **verse-first / passage / self-learning** model. Companion: `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (the item list). Supersedes the per-verse `01b`/tier framing for process. **The programme has fundamentally shifted to a self-learning, self-checking, passage-anchored, term-driven process** — this doc records it.

## 1. Governing principles (what changed)
- **Verse-first.** The verse is the unit; it yields a term-list + verse-level items. (memory `project_ve_lexical_is_verse_first`)
- **Passage = a consecutive run.** A passage is a maximal run of consecutive verses (sort by book, chapter, verse_num; length ≥ 2). Purely mechanical — no isolable/openers/semantic detection, **no reading to establish boundaries**. `verse.passage_id`; anchor = first verse (`is_passage_anchor`). The lexical is derived **on the passage as one unit**, anchored on the first verse.
- **Term-driven batching.** Work an OWNER term at a time: its **anchor verse's passage first**, then **every verse of the term, one by one**. This makes the **focus point emerge** (reading a term across all its verses).
- **Genre-aware.** `verse.genre` decides the passage treatment (§3).
- **Self-learning + self-checking.** Read back every result and evaluate it for **sensibility**; when uncertain, write a **D11 note** rather than assert. **Discovering and adjusting the rules is part of the process, not an afterthought.**
- **Completion-marked.** `verse.process_marker` records done verses; re-runs skip them.
- **The span is the unit within the verse** (span-completeness pre-pass, §5).

## 2. The processing pipeline (per passage)
1. **Select** an owner term → its verses → passages (anchor passage first). Skip any verse already marked complete.
2. **VALIDATOR A — passage membership.** Look up the consecutive run (`verse.passage_id`). (Trivial — no walking.)
3. **VALIDATOR B — spans present.** Every member verse must have `verse_morphology`. If any is missing → write `process_marker='B-BLOCKED:<refs>'` and **move on** (do not halt the batch).
4. **Anchor** = the first verse (the ve-records attach here).
5. **Read all passage morphology together** (one batch) — READ ONCE, USE MANY.
6. **Derive** each term's items across the passage span-set (per the catalogue rules), genre-gated (§3).
7. **Read back / sensibility check** — does each value make sense against the text? Uncertain or odd → **D11 note**. Wrong-in-general → **adjust the rule** and note the learning.
8. **Mark complete** (`process_marker`), and move to the next verse/passage.

## 3. Genre treatment (the key refinement)
- **prose** (law/narrative · narrative · prophetic · gospel-narrative · epistle) → passage = consecutive run; **cross-verse items ON** (source D2, effect D8, process D7). Validated on narrative (Exo 1, Gen 4, 1Sa 1).
- **poetic/wisdom** (Job · Psalms · Proverbs · Ecclesiastes · Song) → **TWO PHASES** (consecutive verses are independent, so cross-verse items would be noise):
  1. **Phase 1 — per-verse.** Use the **chapter/poem as the batch**; derive a per-verse lexical for **each** verse (per-verse items only; cross-verse OFF).
  2. **Phase 2 — poem read.** On completion, **read the whole poem** and **enrich** the verse-lexicals from the **interrelatedness** of its verses (discover cross-verse links deliberately, not by proximity).
- **Prophetic / Song of Solomon / Proverbs** may each need their own tuning — treat as open, flag with D11.
- **Option-3 (require a grammatical cross-verse link)** is itself a **method to test**, not to assume.

## 4. Self-learning loop (why accuracy jumped)
Different treatment of passage/verse in different scenarios sharply increases accuracy; **reading back and evaluating for sensibility makes a huge difference.** The loop: derive → read back → is it sensible? → (yes: keep) / (uncertain: D11 note) / (systematically wrong: **fix the rule, record the learning, re-run**). Example learning (perek trial): the `source` rule cannot yet tell a **driver** (dread→ruthlessness) from a **restraint** (fear-of-God restrains ruthlessness) — banked as a refinement.

## 5. Span-completeness pre-pass (the term-list, decided ahead)
Before analysis, for each verse: **verse → spans** (`verse_span_index`) → is each span a primary term? if not, should it be (a **missing primary** or a **qualifier**)? → confirm it is pulled into the DB → the confirmed set is the **term-list**. Mechanical narrows to a candidate list; judgement confirms per occurrence. (memory `project_ve_lexical_is_verse_first`)

## 6. Storage + markers
- Values → `ve_lexical` (+ pair columns `from_span/to_span/direction/resolution/pair_kind`). Verse-level → `verse.passage_id/is_passage_anchor/genre`.
- **Completion:** `verse.process_marker` (e.g. `lexical-v7-20260702`, `B-BLOCKED:…`, `A-REVIEW:…`). Re-runs skip completed verses.

## 7. Status (2026-07-02)
- **Solid:** per-verse items across genres; narrative cross-verse movement (source/manner/effect/process); passage layer (3,650 consecutive-run passages); term-driven order + markers.
- **Open (tracked in the catalogue §6 + validation reports):** source driver/restraint split; bearer (D3); target word-order; the poetic two-phase (to exercise on a Psalms/Proverbs term); item convergence + `ib_observation` retirement (pending finalised derivation).
- **Trials/harnesses:** `_probe_lexical_derivation_all14_v6_20260701.py` (14-item genre-aware) · `_apply_term_driven_lexical_ruthlessness_v7_20260702.py` (term-driven) · results in `verse-analysis/_reports/wa-lexical-*`, `wa-term-driven-ruthlessness-trial-20260702.md`.
