# Debate-process rebuild — readiness assessment before testing Dan 8

**Date:** 2026-08-06 (updated same day, twice). **Purpose:** the researcher asked for an assessment
of the 2026-08-05 debate rebuild (BUILD.md §59-63, commit `bba9c22e`) and what's missing before
testing Daniel chapter 8.

**Living document — read in this order:** Part A (below) is the original investigation, corrected
in place as findings were refined rather than rewritten (§2.1's correction, §2.1a's fix). **Part B**
(new, end of document) is the requested dry run — the pipeline walked start to finish on paper for
Dan 8, step by step, with the config/method rules each step reads and how they apply.

**Status of the code fix.** §2.1a below found a real gap (writers did blind "clean re-derivation"
instead of read-compare-adjudicate-correct) and it has now been **fixed and verified** —
BUILD.md §64, `handlers/operations.py` rewritten, tested end-to-end via the real
`Operations-Ingest.ps1` entry point against the real Dan 8:1-27 passage (synthetic data, cleaned up
after), DB confirmed back to a clean state. Part B's dry run below describes the pipeline **as it
now stands, post-fix**.

## 1. What's actually built and verified (§59-63)

- **B1 — renamed** `span_reading`/T1-T3 → `verse_lexical`/"the lexical" throughout table, work
  package, steps, code, config. Verified against Dan 8 (593 rows, `dan-8-1-27-verse-lexical-v3-20260805.md`).
- **B2 — report versioning app-wide** (`report.version_on_regenerate`). Verified: 3 consecutive
  `VerseLexical.ps1` runs produced `v1`/`v2`/`v3`, older versions moved to `archive/`, nothing
  overwritten.
- **B3 — operations schema built**: `hib`, `hib_referent_option`, `verse_hib`, `phenomenon`,
  `operation`, `operation_party`, plus `passage.phenomena_complete_at` (the Step 3 phase gate).
  All six tables exist, registered in `cfg_table`/`cfg_column`/`cfg_unique`. **Confirmed live —
  all six are genuinely empty (0 rows) right now**, i.e. no real analytical content exists yet for
  any book, Daniel included.
- **B4 — `passage.build` redefined around HIB-continuity**, reactivated, wired into
  `Chapter-Generate.ps1` as its own gated pre-step. Verified: fails cleanly
  (`"book 'Dan' has no verse_hib data"`) when a book has no HIB data — which is Daniel's actual
  current state (see §2.1).
- **Writer mechanism** (`operations-ingest`: `hib.set` / `phenomenon.set` / `operation.set`) —
  registered (confirmed in `cfg_step`, `kind='operations'`, all 3 active), grant-checked, and the
  phase gate (`operation.set` refusing while `phenomena_complete_at` is NULL) verified end-to-end
  against a **synthetic** test on the real Dan 8:1-27 passage row (id `37425`), then cleaned up.

All of this checks out against the live DB/code exactly as BUILD.md describes it — the mechanism
itself is real, tested, and grant-governed, not just documented.

## 2. What's missing / open before a real Dan 8 test

### 2.1 Not a gap — Daniel simply has no HIB run history yet, and Step 1 is a first-time run

**Correction (researcher, 2026-08-06):** `hib`/`verse_hib`/`phenomenon`/`operation` all being empty
is not a blocker — it's the expected, correct state before Step 1 has ever been run for a book.
The researcher's own description of how Step 1 actually works, first-time or re-run alike:
(a) read every verse in scope and identify every HIB per the definition; (b) compare that reading
against whatever's already in the DB for those verses; (c) validate the list against the DB; (d)
where the fresh reading differs from what's recorded, adjudicate and update the DB with the
correct HIB. On a first-time run (Daniel's actual state) step (b)/(c) trivially find nothing to
reconcile against — the mechanism is exactly the same either way. `passage.build`'s clean refusal
on empty `verse_hib` (§B4) is doing its job correctly here, not surfacing a defect: it's declining
to build passages before Step 1 has run at all, which is correct sequencing, not a blocking gap.

**Open note, not a decision:** the digest (`debate-analytic-process-digest-20260805.md`, Step 1)
as written describes the read/list sweep but doesn't spell out this compare-against-DB/validate/
adjudicate sub-loop explicitly — worth deciding whether that should be added to the authoritative
Step 1 text so it's not only carried in this session's direction, per
`governance.rules_must_be_config_driven`'s spirit (a real process step should live in the doc, not
only be reconstructed from a chat correction). Not changed here — your call.

### 2.1a Confirmed gap — the build does not mechanically support read→compare-with-DB→adjudicate→correct; every writer does blind clean re-derivation instead

**Researcher's stated expectation (2026-08-06):** each stage should (a) read the verses in scope
and get every HIB/phenomenon/operation per the definition; (b) compare that reading against what's
already in the DB; (c) validate the list against the DB; (d) where the fresh reading differs,
*adjudicate* and update the DB with the correct answer (targeted soft-delete/add) — not just
recreate from scratch.

**Checked directly against the code — this is not what's built, at any of the four write points.**
`hib.set`, `phenomenon.set`, `operation.set` (`handlers/operations.py`), and `passage.build`
(`handlers/passage.py`) all follow the identical "clean re-derivation" convention (confirmed by
grep across the app, including `candidate.py`'s older restamp step using the same shape):
unconditionally soft-delete everything currently in the write's scope (book / passage /
phenomenon-set), then blind-insert everything in the incoming payload. Specifically missing:

- **No read/report surface exists** that returns current DB content for a scope back to the
  analyst before writing — checked `handlers/reports.py` and every `lib/*.py`; there is no
  hib/phenomenon/operation reader today.
- **No diff or reconciliation record.** Each writer reports counts written (`"3 HIB(s), 2 referent
  option(s)..."`), never what changed versus what was there before.
- **No mechanical distinction between "compared and confirmed/corrected" and "ignored the DB and
  re-derived from scratch."** Both produce an identical call and an identical DB result — the
  mechanism can't tell them apart, and neither can anyone reading the DB afterward.

**Why this doesn't show up yet.** Daniel's tables are genuinely empty (§2.1) — a first-time run has
nothing to compare against, so clean re-derivation and "compare-then-correct" are indistinguishable
right now. The gap becomes real the first time any of these steps is *re-run* against a book that
already has rows: whatever's in the new payload silently replaces whatever was there, with no
record of what was reconciled versus what was simply overwritten.

**Not decided here:** whether this is acceptable as-is (the adjudication is meant to happen in the
analytical pass, upstream of the payload, and the payload IS the already-adjudicated result — clean
re-derivation is then just the correct mechanical write-in step) or whether the mechanism itself
needs extending (expose current DB state to the analyst before a write; require/record an explicit
reconciliation note per item — kept / added / corrected-with-reason / soft-deleted-with-reason).
Genuinely your call, not something to default past.

> **RESOLVED, 2026-08-06 (same day, second pass).** Researcher's direction: fix the design so every
> point of interaction with the DB is properly designed and encoded — extend the mechanism, don't
> just note the gap. Done: `_reconcile()` (new, shared by all three writers) classifies every
> incoming item against current DB rows by natural key into unchanged (untouched) / changed
> (requires a `reconciliation_note`, or the call fails before any write) / new (no note needed);
> **any pre-existing row the payload doesn't address at all — not repeated, not in an explicit
> `remove` list with a reason — fails the call** (`unreconciled`), the direct mechanical form of
> "use the DB info to ensure the read isn't missing something." A reconciliation report is written
> on every call via `reportkit.oneoff_path` (no new config needed — see BUILD.md §64). Verified
> end-to-end via the real `Operations-Ingest.ps1` entry point: new/unchanged/changed-no-note-
> refused/changed-with-note-corrected/unaddressed-refused/explicit-remove, all confirmed against
> the live Dan 8:1-27 passage, then cleaned up. A genuine bug was caught and fixed in the same pass:
> the Step 3 phase gate (`phenomena_complete_at`) only ever moved forward in the original build —
> now it explicitly re-opens (back to NULL) if a legitimate removal makes the register incomplete
> again, confirmed by test. Full detail: BUILD.md §64.

### 2.2 Blocking-adjacent — the existing Dan-8 passage row predates the new rule, and covers a shape the new rule exists to prevent

The live `passage` table already has 16 rows for Daniel — **the whole book**, including
`id=37425, ref='Dan 8:1-27', rule=NULL, source=NULL, debate_status='filled'`. These are legacy
rows from before B4 (char-continuity / pre-retirement), never touched by the redefined
`passage.build` (which requires `verse_hib` to run at all, and Daniel has none). `WA-dan-8-1-27-
debate.md` (the old, hand-filled prose debate this passage row backs) is a **single 27-verse
passage** — precisely the shape failure-mode (b) in the digest warns against ("a large passage
papering over a real subject change is not correct, regardless of how convenient the chapter
boundary looks").

Once real HIB data is entered and `Build-Passages.ps1 -Book Dan` is actually run, it will **delete
and rebuild all 16 of Daniel's passage rows** (clean re-derivation, confirmed in
`handlers/passage.py:build`) from whatever `verse_hib` exists at that point — almost certainly
producing several smaller HIB-continuous passages within Dan 8, not the one 27-verse block. That
directly retires `id=37425` and detaches it from `WA-dan-8-1-27-debate.md`.

**Sharpened by the Part B dry run below — the blast radius is bigger than "one detached debate."**
`passage.build`'s clean-re-derivation `DELETE`s are `WHERE book=?`, not chapter-scoped. The moment
`Build-Passages.ps1 -Book Dan` (or `Chapter-Generate.ps1`'s new automatic pre-step) runs even once —
triggered by testing Dan 8 alone — **it wipes all 16 of Daniel's existing passage rows**, not just
`id=37425`. Chapters 1-7 and 9-12 all currently have `debate_status='filled'` old-model prose
debates too (confirmed live in the DB — every chapter of Daniel already has one). Every one of them
loses its passage-row backing at that moment, not only Dan 8's. See Part B, Step 2, for the full
walkthrough.

**This is a genuine judgement call, not something to decide silently:** does testing Dan 8 mean
(a) running the real HIB sweep for Dan 8 only and rebuilding Dan's passages now (accepting that
*all twelve* of Daniel's old filled prose debates lose their passage-row backing, not just Dan 8's),
or (b) something else you have in mind? `debate-prep-validation-20260805.md` (written the same day, before the B1-B4
build) asked this exact question and it doesn't appear to have been explicitly answered:
*"Dan 8 already has a filled debate (predating the lexical fix and current guidance versions) — is
this session re-checking/re-doing Dan 8 specifically, or moving to a chapter that hasn't been
debated yet?"* Separately, that same doc flagged `WA-dan-8-1-27-debate.md` as stale on two counts
even under the *old* model — built before the lexical fix, and citing superseded guidance-doc
versions (v1.3/v1.2 vs. current v1.5/v1.4).

### 2.3 No writer for Step 7 (closing sections) — nowhere for that content to go

`passage_linkage` / `passage_insufficiency` / `passage_emergent_question` / `passage_validation_note`
were explicitly **not built** (BUILD.md §61 — "the design doc's own easiest tier to cut," neither
table nor writer exist). A real Dan-8 pass will reach Step 7 (Q7 linkages, insufficiencies register,
emergent-questions log, validation notes) with no structured place to record it under the new
schema.

### 2.4 No report renders the new tables — Step 6's own stated purpose isn't built yet

The digest's Step 6 says the `.md` document should become "a generated extract off those DB
records... not left as prose inside an `.md` file." BUILD.md §61 confirms this explicitly:
*"the working/analysis surface and the published report surface are two different things — not
yet designed."* Right now, after writing real `hib`/`phenomenon`/`operation` rows there is **no way
to review the result as a document** — only direct SQL. `report.passage_debate` is unchanged and
still produces the old prose-scaffold format, disconnected from the new tables.

### 2.5 Two escalations are sitting open in the live queue right now

Checked directly (`escalation` table, most recent rows):

| run_id | state | question (start) |
|---|---|---|
| `RUN-20260805_210820_872-CONFIGMAINT` | **raised** (unanswered) | cfg_* structurally coherent, but 6 stale `filled_by` + 1 stale GOVERNANCE.md — same advisory `debate-prep-validation-20260805.md` asked you to Approve/Reject/Revise |
| `RUN-20260805_210724_502-OPERATIONS-INGEST` | **raised** (unanswered) | "passage 37425's phenomena register is not complete yet" — the deliberate negative-case test from §63's verification, left in the queue after cleanup |

Neither blocks a new run mechanically, but both are genuine open items from the last session that
were never closed out — worth clearing (or explicitly leaving) before a fresh Dan 8 run adds new
escalations on top of them.

### 2.6 Deferred documentation debt (named, not re-raised as new)

`GOVERNANCE.md`/`USER-GUIDE.md §12b` still cite the old `span_reading`/T1-T3 names — deliberately
deferred by your own instruction "until the debate-process build (B2-B5) is complete." B1-B4 +
writer are done; **B5 (the working-record/control-total artifact) was folded into B3's DB columns
rather than built as its own JSON sidecar** (per the design doc's own note that B3/B5 aren't
separable) — so B5 is arguably satisfied mechanically, but there's no human-readable "what's done,
what's left" view short of querying the DB mid-pass. Whether that counts as "B2-B5 complete" enough
to trigger the deferred GOVERNANCE.md/USER-GUIDE.md update is your call, not mine to assume.

## 3. Not a gap — confirmed working, no action needed

- Verse-lexical (Step 0) for Dan 8 is current and complete: 593 rows, most recent version
  `dan-8-1-27-verse-lexical-v3-20260805.md`, verified against the researcher's own screenshot fix.
- Write-grant governance is real and enforced (checked `_may()` calls in `operations.py`; every
  table write is grant-checked, confirmed against `cfg_write_grant`).
- `configmaint.validate` itself reports 0 structural-coherence findings beyond the 2 advisories
  named in §2.5 — nothing new introduced by the rebuild.

## 4. Suggested order, pending your call on §2.2

1. Resolve the two open escalations (§2.5) — Approve/Reject/Revise each.
2. Decide §2.2 — proceed with rebuilding Daniel's passages under HIB-continuity now (retiring the
   old `Dan 8:1-27` passage row and its prose debate as historical), or hold.
3. If proceeding: do the real Step 1 HIB sweep for Dan 8 → `hib.set` → `Build-Passages.ps1 -Book
   Dan` → Step 3 phenomena sweep → `phenomenon.set` (confirm phase gate sets) → Step 4-5 →
   `operation.set`.
4. Step 6/7 (report render, closing-section tables) have no home yet (§2.3-2.4) — decide whether
   to build them first, or run the Step 1-5 mechanism now and hold Step 6-7 output as a plain
   working note pending that design.

No writes were made to `iba.db` or any config in the course of this assessment (Part A). Part B
below **did** make and revert writes — see its own note.

---

## Part B — Dry run on paper: Dan 8 through the pipeline, Step 0 → Step 7

**What this is.** Not a live analytical run — no real HIB/phenomenon/operation content is asserted
below as genuine findings. This walks the pipeline **as it now stands, post-§2.1a-fix**, one step
at a time, for Dan 8 specifically: what triggers the step, which rule governs it and where that
rule is actually read from (a `cfg_setting`/`cfg_write_grant` row the code reads, or a method doc a
human/AI reading pass consults), what happens to Dan 8's real current data, and what decision point
comes next — so each step can be evaluated on paper before anything real is submitted. (The code fix
itself WAS exercised live, with synthetic `"(MECHANISM TEST)"` data against the real Dan 8:1-27
passage, then fully reverted — see BUILD.md §64. Nothing below states or implies that a real Dan 8
reading has happened.)

Two kinds of "rule" recur throughout, named separately at every step, since they're read from
different places by different readers:

- **Config rules** — read by the *code*, from `cfg_setting`/`cfg_write_grant`/`cfg_step` at
  `ctx.cfg.setting(key, default)` / `ctx.cfg.may_write(writer)` call sites. Cited below as
  `key = value` (live values, checked directly against the DB for this document).
- **Method rules** — read by the *analyst* (me, doing the reading pass), from the governing docs
  (`debate-analytic-process-digest-20260805.md`, `WA-passage-read-guidance-v1.5`,
  `WA-interpretation-questions-v1.4`). The code doesn't know these exist; it only validates that
  whatever the analyst decided is internally consistent (references resolve, notes are present,
  every prior row is accounted for).

### Step 0 — Get the lexical for every verse in scope

**Trigger.** Prerequisite gate, run once before Step 1 begins — per the digest, not a coded
`cfg_step` of its own inside `operations-ingest`.

**Method rule.** Digest Step 0: the lexical must be complete in grammatical fact for the scope
before anything downstream touches raw span/Strong's/morph data again.

**Config rule.** None specific to this gate — `verse_lexical` is produced by the separate
`verse-lexical` work package (`lexical.build` → `report.verse_lexical`), governed by its own
settings (`report.verse_lexical_output_pattern`, etc.), unrelated to `operations-ingest`.

**Applied to Dan 8 — already satisfied, checked directly.** `verse_lexical` has 593 live rows for
`Dan.8.%` (confirmed by SQL, this session). `debate-prep-validation-20260805.md` recorded 100%
resolution (362 spans, 593 codes) after the two regression fixes (§57-58). Most recent render:
`dan-8-1-27-verse-lexical-v3-20260805.md`.

**Not mechanically enforced, worth naming.** `hib.set` validates that each verse reference resolves
in the `verse` table (`_verse_id`) — it does **not** check that `verse_lexical` rows exist for that
verse before accepting a HIB entry for it. Step 0's completeness is currently a fact the analyst
confirms by reading (as done here), not a gate the code refuses to bypass. Not a blocker for Dan 8
specifically (already genuinely complete) — flagged as a gap in the mechanism, same category as
§2.3/§2.4, not fixed in this pass.

**Decision point.** Confirmed complete → proceed to Step 1. (If it weren't, the rule is: stop, build
it first, via `VerseLexical.ps1`.)

### Step 1 — Identify every HIB across the verses in scope

**Trigger.** A reading pass over Dan 8's 27 verses, working from the lexical's row-level data
(morph/Strong's), not the printed English gloss.

**Method rule.** Digest Step 1: every human mentioned is a presumptive candidate (named or
collective, however brief, however outward the stated act); collectives stay collective (one HIB,
not decomposed); referential/implied HIBs are named, not skipped; referent cruxes (ambiguous
pronouns/parties) are enumerated with textual grounds, one reading explicitly adopted, alternatives
kept on record. **Plus the researcher's 2026-08-06 refinement, not yet folded into the digest text
itself (flagged §2.1 above):** compare the fresh reading against what's already in the DB for these
verses, and adjudicate any difference — trivial on a first pass (nothing there yet), load-bearing on
any re-read.

**Config rule — read and enforced by `hib.set` itself (`handlers/operations.py`):**
`cfg_write_grant` rows `hib.set → hib`, `hib.set → hib_referent_option`, `hib.set → verse_hib` (all
active, confirmed) gate the actual writes. No `cfg_setting` governs the analytical content — the
handler's only mechanical rules are: every verse reference must resolve (`unknown-verse` fail
otherwise), and `_reconcile()`'s gate (§2.1a fix, BUILD.md §64): every item already live in the DB
for book `Dan` must be repeated (unchanged/corrected-with-note) or explicitly removed
(reason required), or the call fails (`unreconciled`) before any row is touched.

**Applied to Dan 8.** `hib` is genuinely empty for `Dan` right now (confirmed by SQL, this session,
after this dry run's own mechanism test was cleaned up) — a first-time run. `hib.set` is **book-
scoped only** (`Operations-Ingest.ps1` doesn't accept `-Chapters`/`-Range` for this step) but does
**not** require the whole book to be read at once: since nothing exists yet for `Dan`, a payload
covering only Dan 8's HIBs is a clean `new` case for every entry, no `unaddressed` failures possible
(there's nothing pre-existing to fail to address). **Consequence worth flagging for later chapters:**
the *next* `hib.set` call for `Dan` — whenever another chapter's HIBs are entered — must repeat
Dan 8's own HIBs too (unchanged, or corrected with a note), because the gate is whole-book-scoped
and will otherwise refuse the call as `unreconciled` (Dan 8's rows "not addressed"). This is a
mechanical consequence of the fix, not a defect — it forces every `hib.set` call to submit the
analyst's full current understanding of the book to date, never a silent partial update.

**Output.** A flat list of Dan 8's HIBs (e.g. Daniel himself; the ram/goat as non-human forms
directly resolved to named human referents Media-Persia/Greece per 8:20-21; the "little horn"
figure; Gabriel/the "holy ones" as non-human but in-scope per the digest's note (b) — the old,
pre-rebuild `WA-dan-8-1-27-debate.md` preliminaries section already names this same cast under the
old model; a fresh Step 1 sweep would confirm or revise it, not invent from nothing), each tagged
stated/named vs. referential, any genuine referent-crux resolved and recorded. **Not asserted here**
— this is what the step produces, not a claim that this is the corrected result.

**Decision point.** `hib.set` called with the payload → `ok` (counts: new/unchanged/changed/removed)
or `unreconciled`/`unknown-verse`/`bad-payload` (nothing written) → only on `ok` does Step 2 have
data to work from.

### Step 2 — Divide the verses into passages, boundary = HIB continuity

**Trigger.** `Build-Passages.ps1 -Book Dan` standalone, or automatically as `Chapter-Generate.ps1`'s
own gated pre-step (B4, BUILD.md §62) — its own separate `run_id`, not chained.

**Method rule.** Digest Step 2: a passage is a maximal run of consecutive same-chapter verses that
keep sharing a live HIB; the boundary falls where the tracked cast genuinely changes, not at a
chapter number. Failure mode (b): a large passage papering over a real subject change is wrong
regardless of how convenient the chapter boundary looks.

**Config rule — read live by `handlers/passage.py:build`:**
`passage.default_rule = "hib-continuity"` (the active rule — HIB-sharing runs, not the retired
char-continuity); `passage.min_shared_hibs = 1` (adjacent verses need ≥1 HIB in common to stay in
the same run); `passage.review_over = 10` (a run longer than 10 verses is flagged `needs_review`,
not blocked); `passage.cross_chapter = false` (a run never crosses a chapter boundary, regardless of
HIB continuity — Dan 8's own passages will always stay within chapter 8). `cfg_write_grant`:
`passage.build → passage`, `passage.build → verse_passage` (both active).

**Applied to Dan 8 — the concrete mechanical consequence.** `passage.build` queries `verse_hib` for
`WHERE v.osisId LIKE 'Dan.%'` — **book-scoped, not chapter-scoped.** If only Dan 8's HIBs have been
entered (Step 1 above), that query returns only Dan 8's verses — the algorithm forms runs purely
from those, so the *resulting* passages are correctly scoped to chapter 8 either way. **But the
`DELETE`s that precede rebuilding are also book-scoped, unconditionally**
(`DELETE FROM passage WHERE book='Dan'`, then `verse_passage` for those ids) — this removes **all
16 of Daniel's existing passage rows**, not just the one backing the old Dan 8 debate. Checked live:
every one of Daniel's 12 chapters currently has a `debate_status='filled'` old-model prose debate
(`WA-dan-N-*-debate.md`), each backed by one of those 16 legacy rows (`rule=NULL`, `source=NULL`,
pre-dating B4). **The instant `passage.build` runs for `Dan` — even to test chapter 8 alone — all
twelve chapters' old debates lose their passage-row backing**, not only Dan 8's. New rows are
created only for whatever `verse_hib` currently covers (chapter 8, if that's all that's been read)
— chapters 1-7 and 9-12 would be left with **zero** passage rows at all until their own HIB sweeps
are done, meaning their old filled debates become untracked (`passagetrack.find_tracked_passage`
would return nothing for them) until re-processed under the new method.

**Decision point.** This is the sharpened version of §2.2's judgement call, now concrete: running
`Build-Passages.ps1 -Book Dan` (or letting `Chapter-Generate.ps1` trigger it) to test Dan 8 has a
whole-book side effect on the other eleven chapters' passage tracking, not a Dan-8-only one. Worth
deciding explicitly before the first real Step 1/Step 2 run, not discovered after.

**Output (illustrative, not asserted).** However many HIB-continuity runs the real Step 1 data
produces within Dan 8:1-27 — plausibly several, given the digest's own failure-mode (b) concern
about the old single 27-verse block; each ≤10 verses avoids a `needs_review` flag automatically,
longer runs are still created but flagged, not blocked.

### Step 3 — Per passage: phenomena register (Phase 1, complete before Step 4)

**Trigger.** For each passage Step 2 produced within Dan 8, a reading pass over every verse in it,
for every HIB present.

**Method rule.** Digest Step 3 + the phase-separation rule: Step 3 must be **complete for the whole
passage** before any Step 4 work begins for any verse in it — the direct fix for the Amos 1-3 drift
(phenomenon identification sliding into pattern-fitting once operation-writing momentum bleeds in).
A genuine literary/structural observation is not a phenomenon — logged as an emergent question
(Step 7) instead. Silence is a valid, recorded result.

**Config rule — read/enforced by `phenomenon.set`:** `cfg_write_grant` rows `phenomenon.set →
phenomenon`, `phenomenon.set → passage` (the phase-gate write) — both active. Mechanically,
`phenomenon.set` needs an already-tracked passage for the exact `-Chapters`/`-Range` given
(`passagetrack.find_tracked_passage` — fails `no-passage` otherwise, so Step 2 must have run first
for this range). `_reconcile()`'s gate applies exactly as Step 1's, scoped to this one passage's
phenomena instead of the whole book.

**The digest's own "control total" — how it's actually enforced, mechanically.** Not by
`_reconcile()` (which only guards against *losing* previously-written phenomena) — by a **separate**
completeness check inside `phenomenon.set`: it computes every `(verse_id, hib_id)` pair from
`verse_hib` for the passage's verses, compares against the pairs that end up live after this call
(unchanged ∪ new ∪ corrected — removed pairs drop back out), and only sets `passage.
phenomena_complete_at` when the two sets match exactly. This IS the digest's control total, made
literal: the exact number of HIB×verse crossings from Step 1/2, checked against what Step 3
actually delivered, no self-report involved. **Confirmed re-openable, not just settable** — a real
bug in the original §61-63 build (the gate only ever moved forward), found and fixed in this pass
(BUILD.md §64): removing a phenomenon that was covering a required pair correctly flips the gate
back to NOT set.

**Applied to Dan 8.** Once Step 2 has produced real passages, each needs its own `phenomenon.set`
call (scoped by `-Range`), covering every HIB×verse pair in that specific passage — not the whole
chapter at once unless the passage happens to be the whole chapter.

**Decision point.** `ok` with `gate_set=true` → Step 4 may proceed for this passage. `gate_set=false`
(or `unreconciled`/`unresolved-reference`) → Step 4 remains refused for this passage no matter what
`operation.set` is given — checked at the DB, not trusted from memory.

### Step 4-5 — Per phenomenon: operation + description (Phase 2)

**Trigger.** Only once Step 3's gate is set for the passage.

**Method rule.** Digest Step 4-5: process/source/target per phenomenon, action-type label,
Q1-Q12 interrogative discipline (referent debates, divine/human juxtaposition only where textually
anchored, insufficiency flagged not filled from outside knowledge), the retain/set-aside/
retain-referential/recorded-silence decision, prose description carrying it all with Strong's codes
cited from Step 0's lexical.

**Config rule — enforced by `operation.set`:** `cfg_write_grant` rows `operation.set → operation`,
`operation.set → operation_party` (both active). **Hard refusal** (`phenomena-incomplete`) if
`passage.phenomena_complete_at` is NULL for this passage — checked at call time, not assumed.
`_reconcile()`'s gate applies per-operation, keyed by (verse, hib_label, phenomenon_ordinal).

**Applied to Dan 8.** Same per-passage scoping as Step 3 — one `operation.set` call per passage
(after that passage's own `phenomenon.set` gate is set), one operation per phenomenon in the
register, `operation_party` rows for each source/target.

**Decision point.** `ok` (counts) → passage's Step 4-5 done. `phenomena-incomplete` → back to
Step 3 for this passage, nothing written.

### Step 6 — DB record for each operation (+ report render)

**The write side is exactly Steps 1/3-5 above** — `hib`/`phenomenon`/`operation`/`operation_party`
rows are the DB record the digest calls for, not a separate step.

**Not built — confirmed again, unaffected by this fix.** No renderer turns those rows into a
reviewable document (BUILD.md §61: "the working/analysis surface and the published report surface
are two different things — not yet designed"). After a real Dan 8 pass through Steps 1-5, the only
way to review what was written is direct SQL — the reconciliation reports (`hib.set-reconciliation-
Dan-*.md` etc., new in this fix) show *what changed on each call*, not a consolidated view of the
whole passage's current state. `report.passage_debate` is unchanged, still the old prose-scaffold
generator, disconnected from these tables.

**Decision point (yours, not mine to default).** Build the Step 6 renderer before generating real
Dan 8 content, or run Steps 1-5 for real now and review by SQL/reconciliation-log in the meantime.

### Step 7 — Passage/book-level closing sections

**Method rule.** Digest Step 7: Q7 linkages (between already-registered phenomena/operations in the
*same* passage only), insufficiencies register, emergent-questions log (literary/structural
observations diverted from Step 3, interpretive forks not resolved now), debate quality validation
(Phase 3 — re-examine every phenomenon/operation, correct failures before considering the passage
done, not just log them), open decisions, whole-book read.

**Not built — confirmed again, unaffected by this fix.** No `passage_linkage`/
`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note` tables, no writer
(BUILD.md §61 — "the design doc's own easiest tier to cut"). A real Dan-8 pass reaches Step 7 with
nowhere structured to record any of it.

**Decision point (yours).** Build these four tables/writer now, or hold Step 7's output as a plain
working `.md` note against a specific passage until that design work happens. Either way, Step 7 as
currently built has no DB home — flagged, not solved, by this dry run.

### Summary — what actually blocks a first real Dan 8 attempt right now

1. **Nothing blocks Step 0/1 mechanically.** Lexical is ready; `hib.set`'s reconciliation gate is
   built, tested, and — for a first-time book — trivially satisfied (nothing pre-existing to
   address).
2. **Step 2 has a real, whole-book side effect** (this dry run's sharpened §2.2 finding) that needs
   an explicit decision before `passage.build`/`Chapter-Generate.ps1` is run for `Dan` even once.
3. **Steps 3-5 are mechanically sound and gate-enforced**, including the now-fixed phase gate.
4. **Steps 6-7 have no DB home** — real content can be written (1-5) but not rendered (6) or closed
   out (7) yet. Whether to build those first or proceed and hold the gap is your call.
