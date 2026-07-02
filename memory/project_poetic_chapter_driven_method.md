---
name: project_poetic_chapter_driven_method
description: "METHOD (2026-07-02): the specialised POETIC books (Psalms then Proverbs) are done FIRST, CHAPTER by chapter. Driver = the chapter (not a term); passage process does NOT apply. Phase 1 = per-verse base lexical built independently (cross-verse items OFF); Phase 2 = read the whole chapter as MULTI-CHARACTERISTIC (delight/meditation/moral-poles/rootedness) and file to prose type lexical_prose_chapter. Reusable parameterised scripts."
metadata:
  node_type: memory
  type: project
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Researcher direction + first execution, 2026-07-02 (Psalm 1).** Extends [[project_term_driven_genre_aware_lexical_method]] (which set the poetic two-phase) into a documented, reusable process. Governing question per chapter: **"what do these verses tell us about the inner being?"**

**Poetic books first, chapter by chapter (Psalms → Proverbs). Driver = the CHAPTER, not a term; the passage process does NOT apply.**
- **Phase 0 — chapter completeness (backfill).** The `verse`/measure layer is TERM-SPARSE (~23,600 of ~31,100 Bible verses — only verses a study term touches), so chapters can be missing verses (Psa 2 lacked vv.3–4; Psa 119 lacks 14). Chapter-driven reading needs WHOLE chapters → **backfill decided (researcher, 2026-07-02), not read-with-gaps.** Reusable: `scripts/_apply_backfill_chapter_verses_v1_20260702.py --book --chapter [--live]` — probes STEP for the chapter's verses, ingests missing ones (verse + verse_morphology + verse_span_index projection, genre inherited). Missing verses are often the hinge (Psa 2:3 rebels' cry, 2:4 divine derision) and are gate-2 content only. Backfill → then Phase 1.
- **Phase 1 — base lexical, verse by verse, independently.** Each verse built on its own spans only; **no adjacent-verse load; cross-verse items OFF** (source-across-verses/effect/process are noise between poetic lines). Within-verse items on (sense/type/operation/seat/bearer/target/manner/coupling/intensity/prohibition). Two gates (§12). Sanity-check + `role` (§13). Sets `verse.process_marker`.
- **Phase 2 — evaluate the whole chapter.** MULTI-characteristic (a poem carries several at once, from different angles). Psalm 1: *delight* (M04) + *meditation* (M42) = the righteous inner life; *wicked/sinners* (M10) vs *righteous* (M26) = the two moral poles; tree/chaff simile = rootedness/fruitfulness. Output = the chapter reading (inferences tagged stated|inferred), filed to prose type **`lexical_prose_chapter`** (registry_id NULL, one per book+chapter). Psalm 1 = prose_section id 399.

**Reusable engine scripts (per [[feedback_reusable_engine_scripts_and_continuous_learning]], NOT one-off):** `scripts/_apply_poetic_chapter_lexical_v1_20260702.py --book --chapter [--live]` (Phase 1) and `scripts/_apply_file_chapter_lexical_prose_v1_20260702.py --book --chapter --story [--live]` (Phase 2 filing). New chapter = new parameters.

**Learned this run (continuous improvement, encoded in the script + method §14):**
- **Role rule (per-occurrence):** a **gate-1 tagged term that itself functions adverbially** (derived a `manner`/`coupling` on a verb — a prep-marked noun qualifying the predicate) is a **process-qualifier**, NOT the verse's characteristic (Psa 1:1 *counsel*, 1:5 *judgment*). Same lemma can be a characteristic elsewhere.
- **Simile is not mechanically detectable here:** the comparative *kaf* ("like") is **fused** into the vehicle noun as a generic `HR` preposition (tree/chaff), not a separable morph segment — so simile vehicles can't be auto-flagged; the tree-predicates (*yields*/*wither*) are kept as characteristics and read as the tenor's fruitfulness/stability in Phase 2.
- A **cursor-reuse bug** (inner `cur.execute` truncating the outer tagged-term loop to the first term/verse; fix = `.fetchall()` first) was caught precisely because the script was built reusable and read back. Method doc: `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` §14.
