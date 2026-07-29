# Session log — 2026-07-29 — Joel 1 (book 3) parked: verse-discoverability core assumption surfaced

**Session closed at the researcher's request.** Not a clean book completion like Daniel/Jonah — Joel
1 was started, hit a real methodological question mid-flight, and was deliberately parked rather
than pushed through with a workaround. A new session is to be opened specifically to explore the
impact of changing the underlying assumption this surfaced.

---

## What this session did, in order

### 1. IBA app started
`Start-Iba.ps1` — config loaded, data tables present, STEP up and tagged, known-answer probe
passed.

### 2. Joel 1 (book 3, prophets-first sequence) — base extract + scaffold generated
Continuing the book-by-book passage-debate campaign ([[project_iba_book_by_book_debate_phase]])
after Daniel (book 1) and Jonah (book 2). Book-code lookup needed correcting: the `books` table's
`short_code`/`abbreviation` is `"Joe"`, but the app's own `verse.osisId` prefix is `"Joel"` (OSIS
standard) — `VerseSpanMeaning-Report.ps1 -Book Joe` fails with an `IndexError` deep in
`passagetrack._upsert_passage` (empty verse list, unhelpful error surface) rather than a clean
"no verses found for that book code." Re-ran with `-Book Joel -Chapters 1 -BookLabel Joel` —
succeeded, wrote `joel-1-verse-span-meaning.md` (auto-backfilled 54 previously-unregistered
Strong's before rendering, 100% meaning coverage reported for the verses that exist).
`PassageDebate-Report.ps1 -Book Joel -Chapters 1 -BookLabel Joel` then wrote the debate scaffold
`WA-joel-1-debate.md`.

### 3. Discovered: Joel 1:15 is missing from the DB entirely
The scaffold's per-verse sections jump straight from Joe 1:14 to Joe 1:16 — no placeholder for
1:15 at all. Confirmed against `iba/app/db/iba.db`'s `verse` table directly: no row for
`Joel.1.15` (not `deleted=1` — simply never created). A systematic check of the whole book found
a second gap: `Joel.2.4` is also missing. Chapter 3 is complete (21/21).

Investigated the mechanism before concluding anything: the `verse` table is populated by
`raw.verses` (`iba/app/handlers/raw.py`), called per onboarded Strong's number as part of
`new-word`'s pipeline, which pulls verses via STEP's `call3_strong` (a concordance search for that
one Strong's number, capped/paginated). No registered step currently walks a book verse-by-verse
independent of term discovery, and no `raw.backfill_meaning`-style repair exists for "pull this
specific missing verse."

### 4. Researcher clarified the actual cause — not a bug, a live consequence of the current model
The researcher's own account, given directly: these verses aren't in the `verse` table **because
the study method's discovery process found no study-relevant word in them** — i.e., the
concordance-driven, per-Strong's-number build is working as designed; Joel 1:15 and 2:4 simply
never surfaced a term the study has onboarded. This is the same model already named in
[[project_iba_output_spiderweb_process_locality_augment]] (§13 of the app plan: unit-focused
accretion via concordance search, not a bulk per-book text load).

**The researcher named this a core assumption worth deliberately examining**, not something to
patch inline: if a verse can be entirely invisible to the app whenever it happens not to contain
an already-onboarded term, the passage-debate method's own step 2/Q1 discipline ("every human
mentioned is a presumptive candidate," "no bearing — exit is not a substitute for running steps
3-5") can never even be applied to that verse, because the verse never reaches the debate stage to
begin with. Whether that's acceptable (some verses genuinely carry no IB-relevant content and a
term-driven build will naturally skip them) or a real gap (an IB-relevant verse can be skipped
purely because of which terms happened to get onboarded first, not because of what the verse
actually says) is exactly the open question — deliberately not resolved this session.

### 5. Decision: park, don't route around it
Two remediation options were on the table (pull the 2 missing verses directly from STEP as a
one-off fix, vs. proceed with the debate and log 1:15 as an insufficiency) — the researcher chose
neither, judging the question underneath both options ("should verse-existence in this DB ever be
gated on prior term discovery?") more important than either patch. Session closed here; a new,
dedicated session is to open specifically to explore the impact of changing this assumption.

---

## Where to start a fresh session

1. **Joel 1 (book 3) is NOT complete and NOT abandoned — it is parked.** `joel-1-verse-span-
   meaning.md` and `WA-joel-1-debate.md` exist in `iba/app/verse-analysis/Joel/` but the debate
   scaffold is entirely unfilled (`<!-- fill in -->` placeholders throughout) and is missing 1:15
   outright. Do not treat these as usable debate output yet.
2. **The next session's job is narrower than "continue Joel 1."** It is: examine what changes if
   verse-existence in `iba.db`'s `verse` table stops being gated on prior term discovery (e.g. a
   direct per-book/per-chapter text+span pull from STEP, independent of the concordance walk) —
   impact on `raw.verses`/`new-word` pipeline, on `passagetrack`, on every already-debated book
   (Daniel, Jonah — do either have their own undetected gaps of this kind?), on DB size/scope, and
   on whether this is a `cfg_step`-registered utility, a one-off repair, or a genuine model change
   requiring `configmaint.propose`. Per [[feedback_iba_config_first_not_doc_archaeology]], start
   at `cfg_work_package`/`cfg_step` for `new-word`/`raw.verses`, not at this log or at
   `iba-application-plan-v2-20260720.md` §13 from memory.
3. **Joel 2:4 has the identical gap** — confirmed same session, not yet investigated further;
   treat as a second data point for the same question, not a separate issue.
4. **Daniel and Jonah's filled debates are unaffected by this pause** — nothing about their
   already-completed status changes; whether they have their own silent verse-gaps of this kind is
   itself part of the open question in point 2.
5. `git status` after this log should show a clean tree (this session's work committed and pushed
   in the same unit of work, per `governance.session_log_triggers_commit`).

## Artifacts this session

**Verse-analysis output** (`iba/app/verse-analysis/Joel/`, new, both incomplete/unfilled):
`joel-1-verse-span-meaning.md` (base extract, 19/20 verses — 1:15 absent), `WA-joel-1-debate.md`
(scaffold only, no interpretive content, 1:15 absent).

**Memory**: `project_iba_verse_existence_gated_on_term_discovery.md` (new) — records the core
assumption and the open question for the next session; `project_iba_book_by_book_debate_phase.md`
updated in place to reflect Joel as parked, not in progress.

**No code or config changes this session** — the gap was investigated, not patched.
`governance.build_md_on_code_change` does not apply.

**Open**: the core assumption itself — see point 2 above. This is the entire subject of the next
session.
