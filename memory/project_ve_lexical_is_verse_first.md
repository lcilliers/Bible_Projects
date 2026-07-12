---
name: project_ve_lexical_is_verse_first
description: "FOUNDATIONAL (2026-07-01): the ve-lexical is VERSE-FIRST, not term-first. The VERSE is the top lexical unit — it produces a list of terms (each with a full per-term lexical) PLUS verse-level lexical elements that are NOT per-term (isolable/passage, discovery, cohabitation). A term-based id has no lexical meaning at the verse level. Passages: only the FIRST verse links to a ve-id, but its lexical carries records for ALL terms across ALL verses in the passage (read as one consolidated unit)."
metadata: 
  node_type: memory
  type: project
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Researcher correction, 2026-07-01 (foundational to the ve-lexical model).**

**The ve-lexical starts with the VERSE, not the term.** The verse is the top unit:
- the verse **produces a list of terms**, and **each term gets a full per-term lexical**;
- the verse **also carries verse-level lexical elements that are NOT per-term** — e.g. `isolable`/passage membership, `discovery`, D13 cohabitation, D14 package-reference;
- a **term-based id has no specific meaning at the verse level** in lexical terms (do not reason about the lexical as "per-term rows that repeat a verse value" — that framing is wrong).

**Passages (the read-with-adjacent unit):**
- **A passage = a maximal run of CONSECUTIVE verses** (sort the DB verses by book, chapter, verse_num; run length ≥2). Purely mechanical — NO isolable / openers / paragraph markers / semantic detection / reading to establish boundaries. Runs break at chapter boundaries. Context verses without terms may sit in a run (fine — each term is evaluated by itself). Rebuilt 2026-07-01 = 3,650 passages (`_apply_rebuild_passages_consecutive_v2`); `verse.passage_id` + `verse.is_passage_anchor`. Do NOT re-complicate this (I chased isolable/opener heuristics for several rounds — wrong; the researcher's definition is just consecutiveness).
- a passage is anchored on its **FIRST verse**; **only the first verse is linked to a ve-id**;
- but that anchor's ve-lexical **includes records for ALL the terms across ALL verses in the passage** — the passage is read as **one consolidated lexical unit** on its first verse (not a per-verse lexical for each member).
- **Processing:** startup validators = (A) passage membership via the consecutive run (`passage_id` lookup — trivial); (B) all member spans present in `verse_morphology`. On a validator fail, write `verse.process_marker` and move on. Then anchor=first verse → load all passage morphology together → derive.

**Implication for storage:** passage / isolable / cohabitation / discovery are **verse-level** (their home is the `verse` master index, not per-term on `wa_verse_records`). The per-term pairs (D2–D9) sit under each term. This is the shape the D1–D14 catalogue redesign must honour.

**INDEX-DRIVEN build with TWO GATES (built 2026-07-02).** The build starts from `verse_span_index` (EVERY span), not a pre-tagged term list. Gate 1 = span is a tagged non-T2 term (link verse_context). **Gate 2 = a content word NOT yet a term → lexicalise it anyway (span-keyed), relevance=candidate** — content words carry the IB impact; skipping them guts the lexical. Function words skipped; T2 excluded. Storage: schema **3.36.0 (M62)** made `ve_lexical` SPAN-KEYABLE (`verse_context_id` nullable + `verse_span_id`→verse_span_index + `gate`). Proof: ruthlessness content-span coverage 14%→94%. (Earlier I built only the coverage diagnostic, not the gate — researcher caught it.) The grain index (sense-level, [[project_term_is_sense_not_lemma]]) = `wa_verse_term_links`.

**The unit within the verse is the SPAN, not the term (2026-07-01).** Verse → **spans** (every word; live in table `verse_span_index`, 305,961 rows, with canonical `primary_strong`) → per span: is it a primary term? if not, should it be — a **missing primary** or a **qualifier** — and must it be pulled into the DB? → the confirmed set = the **term-list for lexical analysis**. Run this **span-completeness check AHEAD** of lexical analysis (it's available from the master verse index), not during it. Mechanical narrows to a **candidate list** (span lemma matches a known primary/T2 but is untagged here); judgment confirms per occurrence (context-dependent — same lemma IB in one verse, ordinary in another). This is the census check on the term-index (cf. [[feedback_term_coverage_cascade_is_index_not_census]]). Feasibility + design: `Workflow/methodology/wa-span-completeness-prepass-v1-20260701.md`.

Corrects my earlier "wa_verse_records is per-term so a passage_ref repeats across term-rows" reasoning (wrong framing). Cf. [[project_verse_fanout_operating_model]] [[project_ib_observation_folds_into_ve_lexical]] [[feedback_verse_raw_data_must_pull_all_study_evidence]]. Passage extract + field proposal: `Workflow/methodology/wa-passages-extract-and-field-proposal-v1-20260701.md`.
