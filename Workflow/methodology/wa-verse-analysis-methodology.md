# Verse Analysis Methodology

> **Living document · Doc version: 1 · 2026-06-05 · DRAFT for review.**
> **Purpose:** how a verse is analysed in this study — to produce its **meaning** and **keywords** (Pass A).
> It combines a **simplified Seven Principles** (operational form of
> `Workflow/methodology/Seven_Principles_of_Biblical_Interpretation.md`) with the **span-handling rules**.
> Governed by `wa-study-foundations.md` §c and `feedback_span_pairing_and_reciprocal_findings`.

---

## 0. First principle — the unit is the **span**, not the verse

- A **span** = one term occurrence in a verse (the Hebrew/Greek word actually hit). A **verse** =
  `(book, chapter, verse)`. There are ~2.6 spans per verse (up to 17).
- **We analyse the meaning the *span* carries, read in its verse.** "The meaning of the verse" is shorthand
  for "the meaning this span carries, in this verse's context."
- Binding throughout (foundations §c): the **verse meaning is the data and rules all analytics**; readings
  are **neutral** and **full-scope** (any inner-being state, no theological narrowing); **no guessing**;
  where a reading is contested, **surface it — never hide it**.

---

## 1. The Seven Principles — in focus (one line each)

The lens. Each principle becomes a question asked *of the span in its verse*.

| # | Principle | What it asks of the span |
|---|-----------|--------------------------|
| 1 | **Establish the text** | Is the wording of this span secure? (Usually yes — flag only a variant that *changes* the span's sense.) |
| 2 | **Original language** | What does this term mean **in use here** — its sense in this grammar/syntax? Do **not** import the term's whole range (no etymologising, no totality transfer). |
| 3 | **Historical context** | What situation / author / audience is this inner-being state arising in? |
| 4 | **Literary context** | What does the **rest of the verse** (its other spans) do to this span's meaning? A span without its verse is a pretext. |
| 5 | **Genre** | Is this poetry, narrative, law, apocalyptic? — it sets how literal vs figurative the inner-being language is. |
| 6 | **Canonical / analogy of Scripture** | Where the span is **unclear**, what do the term's **other occurrences** and parallel passages clarify? Where the reading is **contested**, present the options. |
| 7 | **Meant → means** | Record **what it meant** (the inner-being content evidenced here). *Significance/application is downstream — not Pass A.* |

---

## 2. The verse-analysis workflow (simplified, span-focal)

Six steps. Principles in brackets.

**Step 1 — Fix the span.** [P1] Identify the term occurrence (`target_word` + Strong's). Take the text as
given; only pause if a textual variant materially changes the sense.

**Step 2 — Sense in use.** [P2] Determine what the term means **in this verse's grammar and syntax** — its
gloss/lexical sense *as used here*, not its whole lexical range. This is the core lexical judgement.

**Step 3 — Read the whole verse and pair the siblings.** [P4 + span rules] Read the full verse. Classify
each **other span** as **T1** (another named cluster — a second characteristic), **T2** (supplementary —
recipient / object / locus / modifier / particle), or **FLAG** (pending). Then (see §3):
- **pair the T2 siblings in** — they *expand* this span's meaning (its object, trigger, locus);
- **name any T1 sibling** — the verse is cross-functional; the other characteristic is named, not ignored.

**Step 4 — Place it: setting & genre.** [P3, P5] Let the historical occasion and the literary genre
condition the reading (a poetic dread ≠ a legal "fear of the LORD" ≠ a narrative fright).

**Step 5 — Clarify the unclear; surface the contested.** [P6] If the span's meaning is **not settled from
this verse alone**, clarify it from the **term's other occurrences** (where the sense is clearer) and
parallels — *at this stage*, not later. If more than one reading is genuinely defensible, **state the
readings; do not adjudicate**.

**Step 6 — Record what it meant.** [P7] Write the **meaning** + **keywords** (§4). Stay **descriptive** —
the inner-being content evidenced here — not applied. If the span carries **no** inner-being content,
**set it aside** with an evidence-based reason.

---

## 3. Span-handling rules (the integration — `feedback_span_pairing_and_reciprocal_findings`)

**A sibling span is never silently ignored.** Every other span in the verse is either paired-in (T2) or
named + reciprocally-seeded (T1).

- **T2 sibling → paired into the meaning, explicitly.** A T2 span is *not* a second faculty; it **expands
  the definition** of this span — its object (fear *of the Most High*), its locus (dread *in the hand*), its
  trigger (afraid *at the sound*). Name that expansion in the meaning.
- **T1 sibling (multi-T1 verse) → name it, both ways and onward.**
  - the **meaning** and the **keywords** of the cluster under review **name the other T1 span**;
  - *(downstream, Phase D)* the **finding** mentions the other span, and the pipeline **auto-creates a
    candidate finding in each sibling cluster** for their consideration. **The verse is not moved** — a
    finding lives in each cluster it genuinely touches.
- **FLAG sibling →** treat as pending; note it, resolve its bucket when the term is allocated.

**Worked examples**
- *Gen 9:2* — `fear`/`dread` (M01) + T2 `hand`: the locus "into your hand" *expands* the dread. → one
  meaning, T2 paired in.
- *2 Cor 7:11* — `fear` (M01) **+** `grief` (M03) **+** `zeal` (M21) … : multi-T1. M01's meaning names fear
  *and notes* the surrounding repentant affections; keywords include the sibling; reciprocal candidate
  findings seeded in M03, M21, … .

---

## 4. The output of verse analysis (Pass A)

For each **inner-being** span:

- **Meaning** (`verse_context.analysis_note`): one neutral, plain-English statement of what *this span*
  means here — span-focal, **naming paired T2 expansions and any T1 sibling**, no totality transfer, no
  guessing, contested readings stated not resolved. *(Length band: ≤ ~60 words / ≤ 2 sentences — confirm.)*
- **Keywords** (`verse_context.keywords`, JSON list): **3–7**, each **1–2 words, lowercase, never
  hyphenated**, open-class, no particles/proper-names/sentences; **atomic and reused** across verses for the
  same operation; include a keyword for a named T1 sibling. *(Keyword structure/normalisation — open
  decision, `project_keyword_analytics_revision_parked`.)*

For a span with **no** inner-being content:

- **Set aside** with `set_aside_reason ∈ {no_inner_being | physical_only | spatial_only | unclear}`, written
  as an **evidence-based, verse-specific** note (it still informs the term's semantic record), not a curt
  label.

Where Step 5 left something open: record the **clarifying verses** used, and/or mark the reading
**contested / unclear** so it surfaces (the verse-meaning-corroboration worklist).

---

## 5. What stays OUT of verse analysis

- **Significance / application** ("what it *means* for us today", Principle 7's second half) — downstream.
- **Grouping** into sub-groups / VCGs — a *derived* view from the meaning+keyword layer, not authored here
  (`project_meaning_centric_direction_emerging`).
- **Cluster-frame compression** — forbidden. Record *all* the inner-being content the span evidences, even
  where it exceeds the cluster's characteristic (`feedback_two_governing_principles` P2).

---

## Sources
- `Workflow/methodology/Seven_Principles_of_Biblical_Interpretation.md` (the full scholarly form).
- `wa-study-foundations.md` §c (the analysis rules); the governing inputs collated in
  `research/investigations/verse-meaning-keyword-instructions-v29-v30-extract-20260605.md`.
- `research/investigations/verse-span-cross-cluster-usage-20260605.md` (the span / T1-T2 evidence).
- Memory: `feedback_span_pairing_and_reciprocal_findings`, `feedback_t1_vs_t2_ontology`,
  `feedback_inner_being_full_scope`, `feedback_two_governing_principles`, `feedback_brief_classifier_pass`.
