---
name: project_iba_book_by_book_debate_phase
description: "Current major IBA phase (started 2026-07-28) — complete the passage-debate stage for every book of the Bible; prophets first, then other genres; ~1.5 months estimated."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8e7abc11-4c98-4a3a-8770-1da0a8756a12
  modified: 2026-07-30T16:27:40.451Z
---

As of 2026-07-28, the IBA app's passage-debate method ([[project_movement_operation_definition_written]], [[project_iba_passage_debate_no_separate_ai_chat_needed]]) is considered stable enough to run as a sustained, book-by-book campaign rather than a one-book pilot. The researcher named this the next major phase of the study: **complete the passage-debate stage (base extract → passage debate → whole-book read) for every book of the Bible**, working through the **prophets first**, then switching to other genres (order across Torah/history/wisdom/poetry/gospels/epistles/apocalyptic not yet fixed). Researcher's own estimate: roughly **1.5 months** for the whole phase.

**Progress so far:**
- Book 1 — **Daniel** (12 chapters / 16 passage debates), passage debates + narrative complete 2026-07-27. Includes three narrative-synthesis passes (`-v1`/`-v2`/`-v3-consolidated`) plus a reflection log and a whole-book-read gathering document. See [[project_daniel_passage_debates_complete_narrative_next]] (now resolved — narrative was written). **Correction 2026-07-29:** the "complete" status above is narrower than it reads — a full `passage`-table audit (prompted by the researcher asking whether the table was up to date) found (a) `Dan 1:7-21` was a mislabeled range: verse 7 is a genuine boundary verse but was only ever actually analysed in the sibling `Dan 1:1-7` file (the `1:7-21` file carried just a "carried by reference" stub for it) — corrected to `Dan 1:8-21` via `migration/correct_dan_1_boundary_range.py`, new debate file `WA-dan-1-8-21-debate-v1.3-2026-07-29.md`, full re-audit now clean across all 23 live Daniel-and-other passage rows; (b) **`WA-dan-whole-book-read.md` itself still has 17 unfilled Resolution placeholders** — the gathering step ran but the resolve-by-hand step (the same manual synthesis done for Jonah and Joel) never happened. Daniel's whole-book-read is NOT actually complete despite prior wording here. See `iba/logs/SESSION-LOG-20260729-daniel-1-boundary-correction.md`.
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
- Book 4 — **Obadiah** (1 chapter / 1 passage debate — whole book in one debate), complete
  2026-07-29. Taken deliberately out of `cfg_book_order` canonical sequence (Joel 28, Amos 29,
  Obad 30) as a short, single-chapter book. Whole-book-read done, including real cross-book
  comparison against Joel (not just deferred). Densest Q12 (divine-mirroring) material found in
  the campaign so far: Obad 15-16 pair two CONSECUTIVE explicit lex-talionis constructions,
  identical verb both sides ("as you have done, it shall be done to you"; "as you have drunk...so
  shall they drink") — denser than Joel's own clearest instance ("sold," 3:3-8). Also found: a
  four-stage escalation of Edom's own complicity (vv11-14: stood aloof → gloated/rejoiced/boasted
  → looted → betrayed fugitives), two inner-being faculties (understanding, courage) failing in
  succession (vv7-9), and an omission (v11 "stood aloof") explicitly judged morally equivalent to
  active wrongdoing — a new emergent question about whether this method needs its own category
  for omissions, not just acts/states/silences. Session log:
  `SESSION-LOG-20260729-obadiah-complete-and-guardrail-escalation.md` (commit `2125addd`).
- **Guardrail gap found + escalated 2026-07-29** (same session as Obadiah, unrelated to the method
  itself): no runtime path in the IBA app enforces `cfg_work_package.inactive` or a `deleted=1`
  row anywhere — `run.py` dispatches steps without ever consulting `cfg_work_package`;
  `configmaint.py` is the only place `inactive` is read at all, and only for its own validation
  report. Surfaced when a retired step (`set-candidates`) was about to be run against Obadiah with
  nothing in the app to stop it — the researcher caught it, not the code. Escalation
  `MANUAL-20260729_122829_764060`, open, not yet fixed — next task after this memory update.
- Book 5 — **Micah** (7 chapters / 7 passage debates), complete end to end 2026-07-30, including
  narrative. A real app-completeness gap was found and fixed mid-session first: `passage.
  debate_sync` didn't exist as a registered step, so nothing ever re-checked `passage.
  debate_status` after a scaffold was filled in by hand — the session started to reverse-engineer
  the answer from BUILD.md history/archived files instead of stopping, was caught by the
  researcher live, and the gap was closed properly (new step built + registered, GOVERNANCE.md
  §3B/BUILD.md §53) before Micah's own debates resumed. See
  [[feedback_doc_archaeology_signals_missing_config]]. Whole-book-read done with all 7 chapters'
  Resolution sections filled by hand (not left as placeholders, unlike Daniel's known gap above) —
  closed threads include the divine-empowerment pattern (Mic 3:8/5:4, confirmed twice), "steadfast
  love" (chesed) argument (6:8 → 7:18 → 7:20, the cleanest fully-resolved thread found in the
  campaign so far), and "shepherd" stretching across four registers in one book. The book's own
  clearest genuinely UNRESOLVED feature (peace-vs-conquest, Mic 4:3-4/13, paired again at 5:7-8's
  dew/lion double simile) is held open in the synthesis, not harmonised. Narrative generated same
  session: 126,668 in / 7,670 out tokens, $0.4951, validated clean (all 3 channels present).
- Book 6 — **Hosea** (14 chapters / 14 passage debates — the majority oracles, per the researcher's
  own framing at task start), complete end to end 2026-07-30, including narrative. Done in
  canonical `cfg_book_order` sequence (ordinal 27, directly after Daniel at 26) rather than
  out-of-order like Joel/Obadiah. A genuine judgment call was made and disclosed rather than
  asked: whole-chapter passage granularity throughout (no sub-chapter splits, even for ch1's
  narrative/oracle seam), matching Joel/Obadiah/Micah precedent over Daniel's own early
  narrative-scene splits — reasoned as fitting Hosea's own continuous prophetic-sign-unit shape.
  Whole-book-read done with all 14 chapters' Resolution sections filled by hand. The book's own
  central structural device, confirmed across the full read: the **shuv ("return") arc** — called
  for (14:1) → confessed but transient (6:1-4) → denied (7:10) → hollowed (7:16) → historicised as
  judgment ("return to Egypt," 8:13/9:3,6) → refused (11:5) → reversed by the LORD's own initiative
  (11:11) → realised in both directions at once at the close (14:1/4/7, the identical verb for
  Israel's return AND the LORD's anger turning away). The major judgment/mercy tension (ch9:15 "I
  will love them no more" vs ch11:8-9's resolution, re-complicated by ch13:14 "compassion is hidden
  from my eyes") was resolved as: ch11:8-9 is the real reversal (grounded in "I am God and not a
  man," not in anything Israel did), reaffirmed at ch14:4, with ch13:14 read as belonging to that
  chapter's own internal judgment-oracle rather than a reopening — mercy is the book's own final
  position. Israel/Judah's relative standing (praised ch11:12, re-indicted ch12:2) was confirmed as
  a genuine, deliberate oscillation across the book's own oracles, not a defect to smooth over —
  structurally parallel to the judgment/mercy oscillation itself. One thread was left GENUINELY
  OPEN, not force-resolved: ch13:16's literal violence against Samaria's infants and pregnant women
  reuses the identical verb (baqa) applied figuratively to the whole nation's judgment at ch13:8 —
  the ethical weight of corporate judgment landing on non-culpable individuals is never addressed
  anywhere in the book's own text, and the narrative names this directly rather than manufacturing
  a resolution. Narrative generated same session: 231,610 in / 6,366 out tokens, $0.7903, validated
  clean (all 3 channels present) — the API-call approval escalation (id 415) was answered
  successfully despite `Escalation.ps1 -Action AnswerRun` printing a misleading "no pending
  escalation" message; the DB row itself showed `state='answered', answer='approve'` and resuming
  the run with the same `-RunId` proceeded normally. Worth a quick sanity-check against the
  escalation table directly if that message recurs, rather than assuming the approval failed.

**Why:** the researcher judged the method has reached a genuinely repeatable, working shape — per-book pipeline (`VerseSpanMeaning-Report.ps1` → `PassageDebate-Report.ps1`, filled by hand applying the method → `WholeBookRead-Report.ps1`), fully config-driven, with corpus-continuity auto-cited between debates. This is the "stream that finally works" moment after a long run of method corrections (RESET 2026-06-25, cycle authority 2026-07-08, verse-first pivot 2026-07-02, passage-debate correction/app-integration 2026-07-21 through 07-27).

**How to apply:** at the start of any future session touching this phase, check this memory for current book-by-book status before assuming what's done or picking a book. When a book completes, **update this memory's progress list in place** — don't spawn a fresh phase memory per book. Which specific book is "next" within "prophets first" is the researcher's own call each session (same as it always was — confirm before running the pipeline against anything new). Whether a completed book also gets a narrative-synthesis pass, and in what shape, is a separate, per-book decision — see [[project_daniel_passage_debates_complete_narrative_next]] for the one-time three-channel narrative requirement, which is scoped to narratives that ask that specific question, not automatic for every book.
