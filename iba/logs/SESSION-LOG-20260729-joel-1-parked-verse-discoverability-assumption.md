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

---

## Follow-on session — 2026-07-29 — mechanism confirmed in depth (config + live STEP evidence)

Per point 2 above, started at `cfg_work_package`/`cfg_step` for `new-word`/`raw.verses`, not from
this log or memory.

### Config trace

`cfg_step` for `new-word` (6 steps, ordinal 0-6): `registry.exists` → `registry.create` →
`raw.discover` (CALL 1 `meanings=` → seed strongs) → `raw.detail` (CALL 2 `getInfo` → meaning) →
**`raw.verses`** (CALL 3 per strong → `strong_verse` + `verse` + `span`) → `raw.write` →
`raw.validate`. The sibling work package `raw-backfill` has exactly one step,
`raw.backfill_meaning`, explicitly scoped `book`, and its own `does` text says it plainly: pulls
**meaning only, not verses** for codes a book's *existing* spans reference — "progressive,
passage-driven DB coverage growth, not a full-Bible bulk pull."

### Code trace (`iba/app/handlers/raw.py`, `iba/app/lib/stepapi.py`)

- `verses()` / `verses_one()` is the **only** code path anywhere that inserts a `verse` row. It
  loops `_strongs_for_word(ctx)` — the word's own seed strongs from `word_strong` (set by
  `raw.discover`, i.e. STEP's `masterSearch meanings=` for the *English headword the researcher
  chose to onboard*) — and calls `Step.call3_strong(code)` per seed, which is a concordance search
  for occurrences of *that one Strong's number* (paginated past `step.cap`=60 via the
  `step.walk_start`→`step.walk_end` forward-walk, max 400 iterations).
- `backfill_meaning_for()` cannot create a `verse` row even in principle: it derives its list of
  "codes to check" by querying the `span` table (`SELECT ... FROM span JOIN verse ...`) — i.e. it
  only ever looks at spans belonging to verses that **already exist**. It has no independent
  source of "what verses exist in this book." It is structurally incapable of closing this gap,
  not just unscoped to do so.
- Conclusion: a `verse` row exists **iff** at least one Strong's number in that verse happens to
  be a seed strong of some *already-onboarded* IB study word. No step anywhere pulls a book/chapter
  verse-by-verse independent of concordance search.

### Live-STEP verification (ruled out a forward-walk/pagination bug as an alternative cause)

Hit STEP directly (`interlinearMode=INTERLEAVED` on the same `masterSearch` route) for both gapped
verses, to see what's actually there and check whether their content words were *studied but
missed by pagination* (a code bug) vs *never queried at all* (the structural gap):

| Verse      | Strong's present (base codes)                                                                              | `strong` row (meaning fetched)?                        | `strong_verse` rows (verses() ever run)? |
| ---------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------- |
| Joel 1:15  | H0162 alas, H3117 day, H3068 LORD, H7138 near, H3588 for, H7701 destruction, H7706 Almighty, H0935 come      | H3117G/H3068G/H7138 yes (backfilled); rest no            | **0 for every single one**                |
| Joel 2:4   | H4758 appearance, H5483 horse, H6571 horseman, H7323 run                                                     | H4758/H7323G yes (backfilled); rest no                   | **0 for every single one**                |

Every content word in both verses has **zero** `strong_verse` rows — not "most," not "a pagination
shortfall," literally none. Three of the seven distinct codes (H7138, H3068G, H3117G, H4758,
H7323G) already have a `strong` row from meaning-only backfill (they're common support words like
"LORD"/"day"/"run" that surfaced while reading *other* already-loaded verses in Joel), which
confirms the backfill path runs correctly but — as the code trace above predicts — never touches
`verse`/`strong_verse` regardless. None of the eight distinct codes across both verses has ever
been the seed strong of an onboarded English word, so `raw.verses` was never invoked for any of
them. This rules out a STEP forward-walk truncation bug: it isn't that `call3_strong` was called
and came back short for a high-frequency term — it's that `call3_strong` was **never called** for
any term that occurs in either verse.

**This confirms the researcher's 2026-07-29 account precisely, with no contradicting evidence**:
the gap is 100% attributable to verse-existence being gated on prior term discovery, not to a
pagination/walk defect, and not fixable by the existing meaning-backfill utility even as a
workaround — that utility reads FROM the verse/span tables it would need to be filling.

### Still open for the next decision point
The three options from the memory's "how to apply" ((a) new per-book/chapter text+span pull
independent of concordance — impact on `raw.verses`/`new-word`, `passagetrack`, DB scope;
(b) whether Daniel/Jonah have their own undetected gaps of this kind; (c) whether this is a new
`cfg_step`-registered utility, a one-off repair, or a `configmaint.propose` model change) are
unchanged and not yet decided — this follow-on only establishes the mechanism with certainty, it
does not choose a remediation.

## Second follow-on session — 2026-07-29 — full-extent census + sample impact read

Per the researcher's instruction ("before deciding on the route... discover the full extent"):
full-Bible census (66 books, 1189 STEP chapter fetches, read-only, no DB writes) plus a per-book
sample read of the missing verses' actual content. Full write-up:
[`iba/app/reports/verse-existence-census-20260729.md`](../app/reports/verse-existence-census-20260729.md)
(data: `verse-existence-census-20260729.json` alongside it).

**Headline:** 2,049 / 31,086 canonical verses (6.59%) have no `verse` row — smaller than the
researcher's ~10% guess, and sharply concentrated (1Chr 44%, Ezra 40%, Neh 31%, Josh 23%, Num 17%
account for over half the entire gap; 12 books have zero gap). Sample read of the missing verses'
actual text confirms the researcher's assumption is directionally right for the bulk of the count
(genealogies/censuses/measurements/place lists in the worst-hit books), **but** surfaces a real
minority — concentrated in poetic/lament/wisdom material, Lamentations 3 above all (3 of 5 sampled
verses there are personal-affliction content) — that plausibly carries inner-being content and is
invisible for the same structural reason. Remediation route still not decided — this closes out
the "discover the extent" instruction only.

## Decision + implementation — 2026-07-29 — accept the gap, mention it, move on

Researcher's decision, given the full-extent read above: the risk of missing real inner-being
content this way is **within tolerance for this study** — the missing verses are not pulled into
the study. Three things to change instead: (a) record that a missing `verse` row is by design, not
an error; (b) have the debate mention the gap inline and continue on the remaining verses; (c) this
is a small footprint — passage-debate runs are chapter-scoped (or sub-chapter when a chapter is
split), and chapters containing a gap are a minority.

**Code (done, live-tested):**
- [`lib/versespanmeaningreport.py`](../app/lib/versespanmeaningreport.py) — new
  `detect_verse_gaps(verses, verse_lo)`: DB-only, no STEP call. Per chapter touched by a debate
  range, finds verse numbers provably missing — a leading gap (chapter's first fetched verse
  isn't 1, or isn't `verse_lo` for a `-Range` sub-chapter call) and internal gaps between fetched
  verses. Documented limitation: it cannot prove a chapter's own TRAILING verse is missing (no
  external verse-count reference in `iba.db`) — an accepted gap in the gap-detector itself, not
  worth a STEP round-trip given the census found leading/internal gaps are the dominant shape.
- [`lib/passagedebatereport.py`](../app/lib/passagedebatereport.py) — `write_scaffold` now merges
  real verses and detected gaps into one reading-order sequence (`_merged_items`) and renders a
  `**Verse gap — by design.**` note (`_gap_block`, template from the new
  `report.passage_debate_gap_note` cfg_setting) wherever a gap falls, instead of silently jumping
  past it.
- Verified against the known live case: regenerated `WA-joel-1-debate.md`
  (`.\iba\app\ps\PassageDebate-Report.ps1 -Book Joel -Chapters 1 -BookLabel Joel` — safe, the
  scaffold had no filled content yet, prior version auto-archived) — the note now appears exactly
  between Joel 1:14 and 1:16, correctly naming the gap instead of silently omitting it.

**Config (proposed, PAUSED — awaiting researcher approval, per
[[feedback_iba_config_changes_require_researcher_approval_never_silent]] / `configmaint.propose`,
never a direct write):**
- `governance.verse_gap_by_design` (insert, run `RUN-20260729_070526_491-CONFIGMAINT`) — records
  the ruling itself as data, per `governance.rules_must_be_config_driven`.
- `report.passage_debate_gap_note` (insert, run `RUN-20260729_070546_193-CONFIGMAINT`) — the note
  template the code above already reads (falls back to an equivalent hardcoded default until
  approved, so the behavior is live either way; approving just makes the wording config-governed
  instead of code-owned).

Not changed: the base extract (`report.verse_span_meaning` / `VerseSpanMeaning-Report.ps1`) does
not get the same inline note — the researcher's instruction named the debate specifically. Open
question, not acted on: should the base extract note gaps too, for consistency with what it cites
as "base data"? Left for the researcher to decide if it matters.
