---
name: project_iba_book_by_book_debate_phase
description: "Current major IBA phase (started 2026-07-28) — complete the passage-debate stage for every book of the Bible; prophets first, then other genres; ~1.5 months estimated."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8e7abc11-4c98-4a3a-8770-1da0a8756a12
  modified: 2026-07-29T09:24:29.036Z
---

As of 2026-07-28, the IBA app's passage-debate method ([[project_movement_operation_definition_written]], [[project_iba_passage_debate_no_separate_ai_chat_needed]]) is considered stable enough to run as a sustained, book-by-book campaign rather than a one-book pilot. The researcher named this the next major phase of the study: **complete the passage-debate stage (base extract → passage debate → whole-book read) for every book of the Bible**, working through the **prophets first**, then switching to other genres (order across Torah/history/wisdom/poetry/gospels/epistles/apocalyptic not yet fixed). Researcher's own estimate: roughly **1.5 months** for the whole phase.

**Progress so far:**
- Book 1 — **Daniel** (12 chapters / 16 passage debates), complete 2026-07-27. Includes three narrative-synthesis passes (`-v1`/`-v2`/`-v3-consolidated`) plus a reflection log and a whole-book-read gathering document. See [[project_daniel_passage_debates_complete_narrative_next]] (now resolved — narrative was written).
- Book 2 — **Jonah** (4 chapters / 4 passage debates), complete 2026-07-28. Whole-book-read done; no narrative pass written (not requested for this book).
- A new method dimension — **Q12, divine mirroring** (companion to Q11/action-type) — was added mid-Jonah, from a researcher observation on Daniel-era leftover material, and proven out with three textually-anchored instances in Jonah alone (3:8-10 "turn"; 4:1-2/4:9 "anger"; 4:10-11 "pity"). Now permanent live method (`WA-interpretation-questions-v1.3-2026-07-28.md` + `WA-passage-read-guidance-v1.4-2026-07-28.md`) — every future book's debates apply it automatically via `cfg_setting`.
- Book 3 — **Joel** (3 chapters / 3 passage debates), complete 2026-07-29 — same day it started.
  Chapter 1 was briefly parked mid-session over a verse-existence/term-discovery gating question,
  resolved same day ([[project_iba_verse_existence_gated_on_term_discovery]]: 6.59% of verses
  missing Bible-wide, judged within tolerance; `report.verse_span_meaning`/`report.passage_debate`
  now note a detected gap inline and continue) — chapters 2 and 3 were debated first per the
  researcher's direction, then chapter 1 filled last to complete the book before the whole-book
  read. Whole-book-read done. Three real Q12 (divine-mirroring) instances found: "return/turn"
  (H7725, 2:12-14 extended 3:1/3:4/3:7 — the dominant thread), "calls" (H7121, 2:32,
  self-contained), "sold" (H4376, 3:3-8 — the book's clearest, most precisely talionic instance).
  Whole-book synthesis found the "day of the LORD" phrase threading five points across the book
  (seeded at the missing 1:15, then 2:1/2:11/2:31/3:14) and the locust/army identity resolving
  only across all three chapters (literal species, 1:4 → martial imagery, 2:2-11 → the LORD's own
  claimed "army... which I sent," 2:25). No narrative-synthesis pass requested for Joel. Full
  detail across five session logs, all dated 2026-07-29: `...joel-1-parked-verse-
  discoverability-assumption.md` (the gating question), `...joel-2-passage-debate.md`,
  `...joel-3-passage-debate.md`, `...joel-1-passage-debate-book-complete.md`,
  `...joel-whole-book-read.md`.

**Why:** the researcher judged the method has reached a genuinely repeatable, working shape — per-book pipeline (`VerseSpanMeaning-Report.ps1` → `PassageDebate-Report.ps1`, filled by hand applying the method → `WholeBookRead-Report.ps1`), fully config-driven, with corpus-continuity auto-cited between debates. This is the "stream that finally works" moment after a long run of method corrections (RESET 2026-06-25, cycle authority 2026-07-08, verse-first pivot 2026-07-02, passage-debate correction/app-integration 2026-07-21 through 07-27).

**How to apply:** at the start of any future session touching this phase, check this memory for current book-by-book status before assuming what's done or picking a book. When a book completes, **update this memory's progress list in place** — don't spawn a fresh phase memory per book. Which specific book is "next" within "prophets first" is the researcher's own call each session (same as it always was — confirm before running the pipeline against anything new). Whether a completed book also gets a narrative-synthesis pass, and in what shape, is a separate, per-book decision — see [[project_daniel_passage_debates_complete_narrative_next]] for the one-time three-channel narrative requirement, which is scoped to narratives that ask that specific question, not automatic for every book.
