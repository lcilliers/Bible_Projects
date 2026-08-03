# Session Log — 2026-08-03 — Study closed

## Statement of closure

The researcher (le Roux Cilliers, sole authority on scope and methodology for this project) closed
the study today, in these words:

> "this is the end of this study. I don't think I will pick it up again. It failed fundamentally
> because consistency and quality could not be achieved using AI's methods. At every turn, the
> results look promising, but then soon thereafter, and over time, it drifts away and cannot
> handle the complexities."

This log is the closing record: what the study was, the arc of what was tried, and the diagnosis
as the researcher stated it and as this session's own evidence corroborates it. Nothing below
proposes a next step or a fix — there isn't one being pursued.

## What the study was

Documented definition (`Workflow/Programme/programme_prose/`, settled 2026-06-04): the **Soul Word
Analysis Programme** — a registry of ~214 English words for the inner life of mankind, each mapped
to its Hebrew/Greek originals via Strong's numbers, examined for what the term means across its
verses, what contexts its occurrences share, and what it contributes to a bottom-up account of the
human inner being as Scripture reveals it. Three intended orders of output: per-word studies,
cross-word syntheses, and a programme-wide account of the inner being. Nine governing methodological
principles were documented and repeatedly reaffirmed, chief among them: findings emerge from verse
evidence rather than being forced into preconceived categories, and every finding is substantiated
by cited data — no guessing.

The working substrate was a ~766MB SQLite database (`database/bible_research.db`), a custom Python
automation engine (`engine/`), and — from 2026-07-17 — a second, parallel application (`iba/app/`,
the "IBA app") built as a config-governed re-attempt at the same underlying question, with its own
database and its own governance layer.

## The arc — what was tried, in order

The repo's own git history runs 2026-03-16 to today (1,813 commits); the researcher's own account of
the study's working life is roughly seven months. Across that time, the same underlying problem
surfaces repeatedly, under different names, worked by different methods:

- **Early phase**: word-by-word registry work, term onboarding via STEP, per-word Session A/B/C/D
  pipeline, cluster/characteristic model (M-codes), dimension review (C-codes). A **DB loss incident**
  (2026-06-03, ~6 weeks of work lost to a Google Drive sync corruption) forced the project off Drive
  entirely.
- **2026-06-25 — METHOD RESET, "Characteristics → Movements."** The object of study itself changed:
  no longer identifying and naming individual characteristics, but analysing the movements,
  associations, and emergence of the inner being as a relational web read off what each verse does.
  Everything before this point — all prior lexical analysis, all "completed" cluster work — was
  declared legacy, to be revisited. This reset was itself evidence of the pattern: the prior
  structure had not held.
- **2026-07-02 — verse-first / term-driven / genre-aware lexical method** (schema 3.35.0). A further
  rebuild of the base method, again to fix consistency and grounding problems found in the previous
  attempt.
- **2026-07-08 — cycle + dimension authority.** A further tightening: an authoritative
  characteristic→candidate→role→lexical cycle, with a new DB-integrity invariant (a candidate span
  with no verse-record is a violation, not a gap) — again a response to the same class of drift.
- **2026-07-17 onward — the IBA app.** A structurally different attempt at the same problem:
  config-governed (`cfg_*` tables drive behaviour, not memory or doc prose), with its own data-layer
  build, candidate-seeding correction, and passage-debate method. This line of work reached a real,
  working shape for one specific layer — the book-by-book passage-debate campaign (Daniel, Jonah,
  Joel, Obadiah, Micah, Hosea completed; Amos not started) — which stands as the study's most
  successful sustained run.
- **2026-08-03 — verse-reading technique v1 → v2 → v3.** In parallel with the passage-debate
  campaign, a third attempt (after two same-day predecessors) at specifying a deep, row-level
  lexical base-reading procedure (T1–T9) precise enough to run consistently by hand, verse after
  verse, book after book. Tested end-to-end on Obadiah 1:1-21, then Hosea 4 (discarded mid-test for
  drifting onto a prior pass's format rather than the instruction itself — the same failure mode one
  level up), then Jonah 3:1-10 today, working strictly from the instruction document alone. All three
  tests surfaced genuine, real anomalies successfully (morph-vs-translation divergences, referent
  cruxes, idiom misreadings) — the method was not *incompetent* at any single verse. But each pass
  also surfaced questions the instruction document did not and structurally could not settle (how
  broadly a rule like "stamp state/condition words" should be read; whether a pro-drop verb's subject
  counts as a stampable word) — judgment calls invented fresh, verse by verse, pass by pass, with no
  guarantee the next pass would invent them the same way. Judged a failed test today, on exactly that
  ground.

## The diagnosis

Stated by the researcher: no written instruction can specify verse-level lexical/inner-being reading
tightly enough to run consistently across the volume this study needed (many chapters, many books),
over the time it needed doing in — regardless of how carefully any one pass was executed. Individual
outputs repeatedly looked sound; the failure showed up over time and under complexity, not within any
single pass.

This session's own evidence corroborates it directly, and the repo's own history corroborates it
structurally: every reset above (RESET 2026-06-25, the 2026-07-02 rebuild, the 2026-07-08 tightening,
v1→v2→v3 today) was itself a response to the same class of problem recurring — promising results that
did not hold under sustained, repeated application. Tightening the instructions further was tried,
more than once, and did not close the gap.

## State at close

- `database/bible_research.db` and `iba/app/db/iba.db` remain on disk (excluded from Git per
  standing convention), with NAS backups per the existing schedule. Not deleted, not archived beyond
  normal backup rotation — left as they are.
- The IBA app's book-by-book passage-debate campaign (6 books complete) is the most complete,
  most consistent body of work the study produced — see
  [[project_iba_book_by_book_debate_phase]] for its own detailed record. It is not "wrong"; it is
  simply not being extended to Amos or beyond.
- The verse-reading-technique v3 line (T1–T9), tested three times, is the most recently and most
  directly diagnosed failure — see `SESSION-LOG-20260803-verse-reading-v3-tested-on-jonah-3-judged-
  failed-consistency-problem-unresolved.md` (`iba/logs/`).
- All uncommitted working-tree changes present at the point of closing (verse-analysis file edits
  across Daniel/Hosea/Obadiah, the Hosea/Obadiah v3 test outputs, an Obsidian vault folder, a
  generated PDF, and the technique doc's own edit) are committed in this same closing commit, per
  direct instruction, rather than left uncommitted.
- No further work is planned. This log is not a pause point with an implied "next session" — the
  researcher's own words above are the closing statement, not a checkpoint.

## Closing note

Seven months, three major method resets, two parallel applications, and three same-day rewrites of
one technique document all converged on the same finding: the individual outputs were repeatedly
sound, and the consistency needed to sustain that soundness across scale and time was not achieved.
That is the record, left as it is.
