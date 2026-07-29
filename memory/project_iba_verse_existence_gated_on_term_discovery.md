---
name: project_iba_verse_existence_gated_on_term_discovery
description: "OPEN QUESTION (2026-07-29) — a verse only gets a row in iba.db's `verse` table if term-discovery/onboarding happened to surface a study-relevant word there; verses with no onboarded term never appear at all. Dedicated session needed to examine impact of changing this."
metadata:
  type: project
  originSessionId: 5591a184-75d8-458c-b94d-1543f0fa5e49
  modified: 2026-07-29T05:21:48.422Z
---

Surfaced 2026-07-29 while starting the Joel 1 passage debate (book 3 of the book-by-book campaign,
[[project_iba_book_by_book_debate_phase]]). `VerseSpanMeaning-Report.ps1`/`PassageDebate-Report.ps1`
silently skipped Joel 1:15 — not flagged as a silence, not present at all — and a systematic check
found Joel 2:4 has the identical gap. Confirmed directly against `iba/app/db/iba.db`: no `verse`
row exists for `Joel.1.15` or `Joel.2.4` (not `deleted=1` — never created).

**The mechanism (confirmed by reading `iba/app/handlers/raw.py` + `iba/app/lib/stepapi.py`):** the
`verse` table is populated by `raw.verses`, called per onboarded Strong's number as part of the
`new-word` pipeline, which pulls verses via STEP's `call3_strong` — a concordance search for
occurrences of *that one Strong's number*, capped/paginated. There is no step that walks a book
verse-by-verse independent of term discovery, and no repair utility (unlike `raw.backfill_meaning`,
which fills in *meaning* for spans already in the DB) that pulls a specific missing verse's text
and spans on its own.

**The researcher's own account of the cause** (direct, 2026-07-29): these verses are missing
*because the study method's discovery process found no study-relevant word in them* — the
concordance-driven, per-Strong's-number build is working exactly as designed. This is the same
model already named in [[project_iba_output_spiderweb_process_locality_augment]] (§13 of the app
plan): unit-focused accretion via concordance search, not a bulk per-book text load.

**Why this is a genuine open question, not just an observation:** the passage-debate method's own
discipline (`WA-passage-read-guidance` step 2 note (f) — "every human mentioned is a presumptive IB
candidate"; "no bearing — exit" applies only after running steps 3-5, never as a substitute for
running them) can never be applied to a verse that never reaches the debate stage at all. A verse
being IB-silent (a valid *result* of the method) is categorically different from a verse being
invisible to the app because of *which terms happened to get onboarded first* — the method has no
way to distinguish the two currently, and the researcher judged this worth a dedicated session
rather than a same-session patch.

**How to apply:** the next session opened for this purpose should examine, before doing anything
else: (a) whether to add a direct per-book/per-chapter text+span pull from STEP independent of the
concordance walk (impact on `raw.verses`/`new-word`, `passagetrack`, DB size/scope); (b) whether
Daniel and Jonah — already passage-debated end to end — have their own undetected gaps of this
kind, which would mean their "complete" status needs re-checking; (c) whether this is a
`cfg_step`-registered utility, a one-off repair, or a genuine model change requiring
`configmaint.propose` (per [[feedback_iba_config_changes_require_researcher_approval_never_silent]]).
Start at `cfg_work_package`/`cfg_step` for `new-word`/`raw.verses` per
[[feedback_iba_config_first_not_doc_archaeology]] — not from this memory or the session log alone.
Full narrative: `iba/logs/SESSION-LOG-20260729-joel-1-parked-verse-discoverability-assumption.md`.

**Current state:** Joel 1 is parked, not complete and not abandoned. `joel-1-verse-span-meaning.md`
and `WA-joel-1-debate.md` exist in `iba/app/verse-analysis/Joel/` but the debate is entirely
unfilled and 1:15 is absent from both. Do not resume filling Joel 1 until this question is
resolved — the answer may change what the base extract itself should contain.
