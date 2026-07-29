---
name: project_iba_book_by_book_debate_phase
description: "Current major IBA phase (started 2026-07-28) — complete the passage-debate stage for every book of the Bible; prophets first, then other genres; ~1.5 months estimated."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8e7abc11-4c98-4a3a-8770-1da0a8756a12
  modified: 2026-07-29T05:21:58.300Z
---

As of 2026-07-28, the IBA app's passage-debate method ([[project_movement_operation_definition_written]], [[project_iba_passage_debate_no_separate_ai_chat_needed]]) is considered stable enough to run as a sustained, book-by-book campaign rather than a one-book pilot. The researcher named this the next major phase of the study: **complete the passage-debate stage (base extract → passage debate → whole-book read) for every book of the Bible**, working through the **prophets first**, then switching to other genres (order across Torah/history/wisdom/poetry/gospels/epistles/apocalyptic not yet fixed). Researcher's own estimate: roughly **1.5 months** for the whole phase.

**Progress so far:**
- Book 1 — **Daniel** (12 chapters / 16 passage debates), complete 2026-07-27. Includes three narrative-synthesis passes (`-v1`/`-v2`/`-v3-consolidated`) plus a reflection log and a whole-book-read gathering document. See [[project_daniel_passage_debates_complete_narrative_next]] (now resolved — narrative was written).
- Book 2 — **Jonah** (4 chapters / 4 passage debates), complete 2026-07-28. Whole-book-read done; no narrative pass written (not requested for this book).
- A new method dimension — **Q12, divine mirroring** (companion to Q11/action-type) — was added mid-Jonah, from a researcher observation on Daniel-era leftover material, and proven out with three textually-anchored instances in Jonah alone (3:8-10 "turn"; 4:1-2/4:9 "anger"; 4:10-11 "pity"). Now permanent live method (`WA-interpretation-questions-v1.3-2026-07-28.md` + `WA-passage-read-guidance-v1.4-2026-07-28.md`) — every future book's debates apply it automatically via `cfg_setting`.
- Book 3 — **Joel**, started 2026-07-29, **PARKED (not complete, not abandoned)**. Base extract + scaffold generated for Joel 1, but Joel.1.15 and Joel.2.4 are entirely missing from the DB's `verse` table — surfaced a core-assumption question about verse-existence being gated on prior term discovery. See [[project_iba_verse_existence_gated_on_term_discovery]] — a dedicated session is needed to resolve this before Joel 1 (or any further book) resumes. `iba/app/verse-analysis/Joel/` has unfilled artifacts only.

**Why:** the researcher judged the method has reached a genuinely repeatable, working shape — per-book pipeline (`VerseSpanMeaning-Report.ps1` → `PassageDebate-Report.ps1`, filled by hand applying the method → `WholeBookRead-Report.ps1`), fully config-driven, with corpus-continuity auto-cited between debates. This is the "stream that finally works" moment after a long run of method corrections (RESET 2026-06-25, cycle authority 2026-07-08, verse-first pivot 2026-07-02, passage-debate correction/app-integration 2026-07-21 through 07-27).

**How to apply:** at the start of any future session touching this phase, check this memory for current book-by-book status before assuming what's done or picking a book. When a book completes, **update this memory's progress list in place** — don't spawn a fresh phase memory per book. Which specific book is "next" within "prophets first" is the researcher's own call each session (same as it always was — confirm before running the pipeline against anything new). Whether a completed book also gets a narrative-synthesis pass, and in what shape, is a separate, per-book decision — see [[project_daniel_passage_debates_complete_narrative_next]] for the one-time three-channel narrative requirement, which is scoped to narratives that ask that specific question, not automatic for every book.
