# Debate process — full current-state spec + proposed updates (living doc, updated after researcher's terminology questions + decisions)

**Date:** 2026-08-05 (updated same day, second pass)
**Status:** Still nothing applied. This revision (a) answers the terminology questions plainly,
(b) expands Part A3 into a full three-document comparison as requested, (c) folds in the
Q1-Q4 decisions, (d) narrows the remaining open questions to what's genuinely left.

---

## 0. Terminology, plainly

### `ordinal` — just execution order, nothing more

`cfg_step.ordinal` is a work package's step list, numbered like line numbers: `0` runs before `1`,
`1` before `2`, and so on. It carries **no other meaning** — not importance, not a version, not an
active/inactive signal (that's the separate `inactive` column). In `chapter-generate`:
`ordinal 0 = report.verse_span_meaning` (the old extract step), `ordinal 1 = report.passage_debate`
(the scaffold step) — ordinal 0 simply used to run *first*. Since ordinal 0 is now `inactive=1`,
`cfg.sequence()` (`lib/cfg.py:121-126`, `WHERE inactive=0 ORDER BY ordinal`) skips it and returns
only ordinal 1 — so today's live sequence has one entry, not two.

### `chained` — whether the work package auto-runs its whole step list, or each step stands alone

This is a `cfg_work_package` column, one value per package, and it changes how the PS
wrapper/`run.py` behave — not what any individual step does.

- **`chained = 1`**: the PS script loops through *every* live step in the sequence, one after
  another, under **one `run_id`**, in one invocation. The work package only counts as "done" when
  the **last** step in the sequence finishes (`run.py:199-207`). Example: `verse-span-reading` is
  chained — `VerseSpanReading.ps1 -Book Dan -Range 8:1-27` runs `span_reading.build` then
  `report.span_reading` automatically, back to back, no separate invocation needed.
- **`chained = 0`**: each step is invoked **independently** — its own `run_id`, and "done" fires
  the moment *that one step* finishes, with no auto-continuation to whatever the next ordinal is.
  Example: `lexicon-parse` is non-chained by design (its own docstring: "standalone... each invoked
  independently") — you call each of its steps yourself, on your own schedule.

**Applied to `chapter-generate` today:** it's `chained=1`, but since only one step is live, chaining
currently does nothing observable — there's nothing left to chain *to*. Your decision (§3 below,
"will not be part of a chain") is to set `chained → 0`: once the new validate step (§3 below) is
added at ordinal 0, it and `report.passage_debate` become two **separately invoked** steps, not an
auto-sequenced pair — matching how `verse-span-reading` was deliberately kept OUT of this chain in
the first place (t1-t3-design-decisions-20260805.md, "New standalone module, not folded into
chapter-generate — DECIDED").

This also answers **Q4** (you flagged you couldn't follow it without this): the question was
whether the new validate step *replaces* `passagedebatereport.py`'s own inline
`BaseExtractMissing` check, or sits alongside it. With `chained=0` now decided, my recommendation
is **both stay**: the new step is an explicit, informative pre-flight you run and read the result
of on its own; the inline check remains as a safety net that still fires even if someone calls
`report.passage_debate` directly without having run the pre-flight first (it's independently
reachable — the standalone `passage-debate-report` work package, `A1` above). Flagging this as a
recommendation, not yet acted on — say if you'd rather the inline check be removed once the
standalone step exists.

---

## A9. `reportkit.py`, in detail — this is what makes the scaffold what it is

Two functions matter for the debate scaffold specifically:

**`render_scaffold(conn, step, sections, intro, **title_vars)`** — builds the actual Markdown
skeleton. It reads `cfg_report` (title, whether to show a table of contents, footer text) and
`cfg_report_section` (per step: each section's `ordinal`, `heading`, `toc_label`, `include` flag)
straight from the DB — **the section list, their order, and their headings are config, not
something `passagedebatereport.py` hardcodes.** The caller (`write_scaffold`) supplies a Python
dict of `{section_key: [body lines]}` — the actual placeholder text — and `render_scaffold` just
slots each one in under its configured heading, in configured order, and builds the ToC links to
match. This is why the debate document always has the same 8 sections in the same order across
every book: that shape lives in `cfg_report_section` rows for `step='report.passage_debate'`, one
set, read every time.

**`write_report(conn, step, path, lines)`** — the actual disk write. Before writing anything, it
calls `archive_before_write(path)`: **if a file already exists at `path`, it is moved (not
copied) into `path.parent/archive/{stem}-{timestamp}{suffix}`** — e.g. the accidental Dan 8
overwrite (BUILD.md §56) landed the real content at
`archive/WA-dan-8-1-27-debate-20260805-113142.md`. Only *after* that move does it write the new
content to the *original* filename. So today's convention is: **one canonical live filename per
range, forever** — every regenerate pushes the previous version into `archive/` and the live path
never changes. That is precisely why Q3 is a real, needed change, not a preference: nothing about
today's mechanism produces a new, distinctly-named file on each run; it always overwrites the same
path (after archiving the old one).

**There already is a versioned-naming pattern in this codebase**, just not used by the debate
scaffold: `reportkit.oneoff_path(cfg, topic, ext)` (used for ad-hoc investigation reports, not
`report.passage_debate`) computes a filename from `governance.oneoff_report_naming_pattern`, and
if that exact name already exists **on the same day**, bumps to `-v2`, then `-v3`, etc. — the
model to reuse for Q3 (§3 below).

**Confirming your read: yes, the scaffold dictates the analysis work.** `write_scaffold`
(`lib/passagedebatereport.py`) pre-fills every section with fixed prompt text quoting the method
docs almost verbatim (e.g. the Phenomena-register block literally says *"for EVERY inner being
present (read-guidance step 2 note (f))... isolate the phenomenon..."*). Filling in the debate
means replacing each `<!-- fill in -->` with real content **against exactly what that placeholder
already asks for** — nothing more, nothing the placeholder doesn't prompt for. Which is exactly why
§A3 below matters: whatever the three method docs don't have a placeholder for in this scaffold
currently doesn't get analytical attention at all.

---

## A3 (expanded). The three method documents — how they relate, and what isn't wired together yet

You're right that there are three separate documents in play, and that they are **not currently
amalgamated**. Here's exactly how each relates to what the scaffold actually renders.

| Document | Governs | Currently wired into the scaffold? |
|---|---|---|
| `WA-verse-reading-technique-v4-2026-08-05.md` (T1-T9) | Base lexical reading (T1-T3) + lexical-level interpretive work (T4-T5) + preliminary inner-being word-stamping (T6-T9) | **T1-T3 only**, and only indirectly — as `span_reading`, a DB table, not as anything the scaffold reads from yet (see below). **T4-T9 have no home anywhere in the scaffold.** |
| `WA-passage-read-guidance-v1.5-2026-08-02.md` | The 3-phase procedure: Phase 1 phenomenon identification, Phase 2 operation generation, Phase 3 validation | **Fully wired** — the scaffold's per-verse "Phenomena identified (Phase 1)" block and "Per-verse operations" (Phase 2) block, plus the standalone "validation" section (Phase 3), are direct mechanizations of this doc's phases. |
| `WA-interpretation-questions-v1.4-2026-08-02.md` | Q1-Q12 interrogative (Part A), interpretive discipline notes (Part B), and — critically — **Part C, the "Output directive"**: the exact 8-section shape a debate document must have | **Fully wired, 1:1.** Part C's 8 sections (Preliminaries · Phenomena register · Per-verse operations · Passage-level linkages · Insufficiencies register · Emergent questions log · Debate quality validation · Open decisions) are *exactly* `write_scaffold`'s eight `sections` keys (`preliminaries`, `phenomena_register`, `operations`, `linkages`, `insufficiencies`, `emergent`, `validation`, `open_decisions`), in the same order. This document's Part C is, functionally, the scaffold's spec. |

**What this means concretely:** `WA-passage-read-guidance-v1.5` and `WA-interpretation-questions-
v1.4` are already effectively one method, split across two files for readability (they cross-
reference each other throughout, and v1.4's own change-control note says it was revised *in step
with* v1.5). Together they are the scaffold's actual spec. **`WA-verse-reading-technique-v4` (T1-
T9) is the outsider** — a genuinely separate, earlier reading stage the other two documents assume
has already happened (`WA-passage-read-guidance` step 1 just says "read the verse/passage," with no
detail on *how*) but that the scaffold does not currently pull from at all:

- **T1-T3** (mechanical lexical reading) is now built as `span_reading` — but the scaffold's
  `Observation` line is still populated by hand, re-deriving Strong's-coded readings informally
  (see the Dan 8 example: `"In the third [H7969] year [H8141]..."`), the same manual work T1-T3
  was built to make unnecessary. `span_reading` is not yet actually read by `write_scaffold` for
  its `Observation` content — only checked for *existence* (`BaseExtractMissing`). Wiring
  `Observation` to be generated (or at least pre-filled) from `span_reading` directly is the most
  concrete, low-risk amalgamation step available, and was already flagged as future work in the
  design record.
- **T4** (referent cruxes — enumerate every grammatically live reading of an ambiguous pronoun/
  party, adopt one explicitly, keep the rest on record) has no dedicated scaffold field. The
  closest existing text is the Preliminaries "Reading rule applied" line, but that's currently used
  for span-level `[AMBIGUOUS]`-code STEP-precedence notes (T1-T3 territory), not referent-level
  ambiguity (T4 territory) — different kind of ambiguity, same free-text slot today.
- **T5** (genre-conventional elements, including expected-but-absent ones, recorded as their own
  observation) has no dedicated field either — but note it is *not* in tension with
  `WA-interpretation-questions` Part B.12 (which forbids literary/structural patterns from being
  smuggled into the phenomena register): T5's job is to name genre elements *separately*, which is
  exactly what B.12 wants kept out of the phenomena register. They're compatible if a genre-notes
  field exists to receive T5's output — currently there isn't one, so T5 observations, if made at
  all today, would have to be hand-placed into Emergent-questions or Preliminaries without a
  defined home.
- **T6-T9** (IB / Agent / Process / Action word-stamping) is explicitly described in v4 as
  *preliminary* — "Do not perform further analysis to determine which IB is affected by which
  Agent... It will follow later in the study." That "later" is exactly what `WA-passage-read-
  guidance` Phase 1 (phenomenon identification + justification) already does. So T6-T9 reads as a
  **candidate-flagging pre-pass** that could feed Phase 1 (e.g. the scaffold's Phenomena-register
  block could open with a pre-listed set of stamped candidate words per verse, for Phase 1 to work
  from, instead of starting from nothing) — but no DB table or scaffold field exists for it today;
  v4's own JSON output sample says as much ("destination tables not yet defined per researcher
  Q7").

**This is a genuine design decision, not something I'll draft unilaterally**: whether/how to
amalgamate T4/T5/T6-T9 into the scaffold — new dedicated sections, folded into existing ones, or a
new DB layer (parallel to `span_reading`) that pre-populates scaffold content the way `span_reading`
could for `Observation`. Flagging as an open item (§ Open questions, Q5) rather than proposing a
specific shape myself.

---

## Q1 — column rename, confirmed. Proposed new names

Given "yes, rename": proposing names that follow the existing convention (columns are named after
the mechanism that writes them, e.g. `debate_path`/`debate_written_at` after `report.passage_
debate`) —

- `passage.verse_span_meaning_path` → **`passage.span_reading_table`** (stores the literal string
  `"span_reading"` — the table, not a path, since the lexical is DB-resident now)
- `passage.verse_span_meaning_written_at` → **`passage.span_reading_written_at`** (sourced from
  `MAX(span_reading.created_at)` over the range's live rows, per your confirmation this is a valid
  version/date proxy)

Say if you'd rather different names — these are proposals, not yet applied (schema change, goes
through `configmaint.propose` per the app's own rules either way).

## Q2 — book tables found in the old DB, confirmed portable

Checked `database/bible_research.db` directly:

- **`books`** (66 rows) — `name` (plain full name, e.g. `"Daniel"`, `"Genesis"` — this is the field
  that matches how `-BookLabel` values look today), `abbreviation`/`short_code` (e.g. `"Dan"`,
  `"Exo"`), `full_name` (a longer archaic title, e.g. `"The Book of Daniel"` — not what you want for
  `book_label`), `testament`, `book_order`, `verse_count`.
- **`book_code_variants`** (112 rows — 66 canonical + 46 aliases) — maps alternate short codes to
  a `book_id`. Checked directly: **it already carries the OSIS-style codes `iba.db`'s own
  `verse.osisId`/`cfg_book_order` use** as aliases distinct from `books.abbreviation` (e.g. Daniel:
  `abbreviation='Dan'` and `verse.osisId` also uses `Dan` — matches directly; but Exodus:
  `abbreviation='Exo'` while `verse.osisId` uses `Exod` — and `book_code_variants` has *both* `Exo`
  and `Exod` rows pointing at the same `book_id`). So `book_code_variants.code = <OSIS code>` joined
  to `books.id` → `books.name` gives exactly the canonical-label lookup keyed on the same code
  `cfg_book_order` already uses.

**Proposed port:** two small new tables in `iba.db` (`book` / `book_code_variant`, or reuse the
same names — your call), populated once from `bible_research.db`'s `books`/`book_code_variants`
(66 + 112 rows, trivial size). Registered via `configmaint.propose` (new `cfg_table`/`cfg_column`
rows, per `governance.rules_must_be_config_driven`) like every other schema addition in this app.
`passage.book_label` then gets written by looking up the run's `Book` param against
`book_code_variant.code` → `book.name`, instead of trusting a free-text `-BookLabel` argument.

## Q3 — no overwrite; versioned filenames, confirmed

**A directly relevant finding, checked while confirming this:** `WA-interpretation-questions-v1.4`
Part C (the document that already governs the scaffold's output shape) **already specifies** a
versioned filename: *"the output is a single debate document — `WA-[passage]-debate-[version]-
[date].md`."* The live `cfg_setting` (`report.passage_debate_naming_pattern =
"WA-{book}-{range}-debate.md"`) **does not actually implement what its own governing method doc
already calls for** — no `[version]`/`[date]` in the pattern at all. So this isn't a new invention;
it's aligning the config to what Part C already says, using the version-bump mechanism
`reportkit.oneoff_path()` already implements elsewhere (`-v2`, `-v3`... on same-topic collision).

**Proposed change:** `report.passage_debate_naming_pattern` → something like
`"WA-{book}-{range}-debate-v{n}-{date}.md"`, and `passagedebatereport.write_scaffold` switches from
`reportkit.write_report`'s archive-and-overwrite-same-path behaviour to version-bump-on-collision
behaviour (new filename each regenerate, old ones never touched/moved) — for `report.passage_
debate` specifically. Whether this same change should extend to `report.span_reading`/other
book-scoped reports, or stay scoped to just the debate output, is worth confirming (§ Open
questions, Q6) since it's a real behaviour change other steps also rely on `write_report`'s current
archive convention for.

---

## Open questions remaining

- **Q5.** How to amalgamate T4/T5/T6-T9 (§A3 above) into the scaffold — new dedicated sections
  (which ones, worded how), folded into existing sections, or a new mechanical DB layer parallel
  to `span_reading`. Your call — not drafted here.
- **Q6.** Should the versioned-filename behaviour (Q3) be scoped to `report.passage_debate` only,
  or should `report.span_reading`/other book-scoped reports adopt it too (currently they all share
  `reportkit.write_report`'s archive-and-overwrite convention)?
- **Q7.** Confirm the proposed new column names (Q1) and the new `book`/`book_code_variant` table
  names (Q2), or supply your own.

Part B/C/D of the previous version of this document (researcher's directed updates, the change
list, and the Daniel 8 test-run steps) still stand as written — this revision only adds the
terminology explainer, the expanded A3 comparison, and resolves Q1-Q4 as above. Full change list
(Part C) will be updated once Q5-Q7 are answered, since the column-rename and naming-pattern items
depend on those answers being final.
