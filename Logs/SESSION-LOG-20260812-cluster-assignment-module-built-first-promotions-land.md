# SESSION LOG — 2026-08-12 — cluster-assignment made a repeatable app module (`strong.reconcile`, `cluster-assign`); the T2/T3 word-ownership rule corrected; first 313 real promotions land; `report.cluster` gets a comprehensive summary

Continues the same day's arc from `SESSION-LOG-20260812-power-failure-recovery-span-fix-cluster-
adoption-complete.md` (BUILD.md §§100-106) — this session picks up immediately after that one
closed, working entirely inside the queued backlog it left open.

## 1. Escalation review — `lexicon.validate` (RUN-20260811_172851_742)

Re-evaluated rather than blindly approved: traced the escalation's "6 coverage gaps" to their exact
rows — all six trace to two Strong's codes (`G6507`/`G7167`, both `blindness`'s, both genuinely
zero-verse LXX-only lemmas). Root cause, not just the symptom: `lexicon.parse`/`related` are
standalone steps, never auto-chained after `new-word` — confirmed via `cfg_step`, and confirmed the
dormant `raw.py:related()`/`lexical()` functions (BUILD.md §98/99, from the rolled-back `receive`
build) were written to close exactly this gap but never wired in. Approved as known state (genuinely
zero-risk: 2 codes, 0 verse occurrences); the systemic gap tracked separately as the `receive`
rebuild, which the researcher then explicitly **postponed and repurposed** as the live end-to-end
test for "does adding a new word trigger every underlying process" once the mechanism below exists.

## 2. Filter re-triage re-evaluated against the now-built cluster model

Read the original filter-re-triage plan (recovered from Claude Code's own plan store — it never
made it into the repo) against the cluster-allocation work from the prior session. Finding: the
cluster model (T2/T3/FLAG/M01-M46, then 4,398 `cluster_strong` rows) **replaces most of what that
plan scoped as new-mechanism work** — "build a POS/proper-noun classifier" becomes "look one up."
Validated directly against `receive`'s own 9 worst-offender codes: 3 land correctly in `T3`, one
(`G2192` "have/be") turns out to sit in a genuine content cluster (`M23`) — independently confirming
the researcher's own re-litigation that the "79% noise" framing overstated it.

## 3. Rows 5-7 / `raw-complete` — sized, not built this session

Full re-evaluation written up (`rows5-7-and-raw-complete-reevaluation-20260812.md`): live-verified
the actual failure surface is tiny (2 zero-coverage codes, 4 bare-fallback `verse_lexical` rows
corpus-wide out of 534,071) — not the sweeping 178-word problem it sounds like cold. Flagged a real
scope conflict with the `receive` postponement (the plan's own build spec would wire the `new-word`
chain today, before the test exists to prove it) — left for the researcher's direction, not built.

## 4. The cluster-assignment module — the main work of the session

**Read every doc in `iba/docs/cluster assignment process/`** (session log, obslog, both review
docs) before designing anything. Researcher then reframed the whole approach from a one-off
corrective to a proper architectural build: *"a clear definition of the expectations of a strong,"*
*"a handler that can take a single strong as input... and perform all the related corrective
actions in sequence,"* *"new-word must complete the entire process... for qualifying strongs,"*
plus a full Strong Expectations Table (spreadsheet) and answers to the two open design questions
(Q2.4.1 ownership exceptions, Q2.4.2 promotion depth).

**Traced "when do new strongs surface" from the code, not assumed:** (a) `new-word` → `raw.detail`
→ `detail_one(origin="word")`, confirmed. (b) `verse-lexical` build → `handlers/lexical.py:build()`
auto-calls `raw.backfill_meaning_for()` → `detail_one(origin="backfill")` — confirmed live,
scenario (b) is real and working. (c), as posed, **doesn't exist** — once a `strong` row exists at
any completeness level, nothing re-examines it; that absence is what this session builds.

**Built:**
- `lib/clusterassign.py` — the mechanical HIGH-precedent matcher (P1/P2 from the cluster-allocation
  session's own reusable method), config-driven.
- `lib/strongreconcile.py` — `reconcile(ctx, code)`, the single-strong handler: classify →
  exception-check → promote-or-leave. Traced `run.py`'s dispatcher first and found only a top-level
  handler's Outcome reaches `escalation` — so exception reporting concentrates in `cluster.validate`
  rather than threading escalation through every call site, which also gives the researcher's
  "one-time clearing vs. standing watch" split for free with no separate code path.
- `handlers/cluster.py` — `cluster.assign` (DB-wide sweep) + `cluster.validate` (coverage/exception
  report, same shape as `lexicon.validate`).
- Wired into both real strong-creation paths: `backfill_meaning_for()` inline, and a new ordinal-7
  `strong.reconcile` step on the `new-word` chain — absorbing what the `receive` rebuild was scoped
  to wire in.
- 16 `configmaint.propose` rows, self-approved per the researcher's standing authorisation for this
  build ("I do not have to approve individual configs for this development... I will look at it
  separately"). One real coherence-check catch along the way (a path-string setting needed
  JSON-quoting) — caught, fixed, reapplied clean, not skipped.
- Rows 6/7/9 of the expectations table (restricting `backfill`'s meaning/parse depth) drafted, then
  **reverted same day** on researcher correction — `backfill` keeps full parse, matching current
  behaviour; no code change needed there.

**First live runs, real findings, not left unexplained:**
- `cluster.validate`'s first-ever run: 10,972/15,293 unclassified; 428 no-word exceptions; 481
  sibling-conflict exceptions. Escalated cleanly, left open for the researcher (a data-content
  decision, outside the config pre-authorisation).
- `cluster.assign`'s first sweep: 1,410 new mechanical classifications, **0 promotions**. Traced
  why rather than shipped unexplained: every candidate hit the no-word exception, because
  `backfill`-origin codes structurally almost never carry their own `word_registry` link.

## 5. The ownership rule corrected — first real promotions

Researcher, on reviewing the 0-promotions finding: *"the whole purpose of having a word, is to
generate the verse, which we have"* — a code found afterward in an already-generated verse doesn't
need its own dedicated word. `T3` specifically is *"by its nature ... not word specific."* Only a
real M-cluster/FLAG classification still needs a word. Fixed config-driven, not hard-coded:
`cfg_setting cluster.assign.word_optional_clusters` (default `["T2","T3"]`), `reconcile()`'s
exception-1 gate and `cluster.validate`'s queries both corrected to match exactly.

Re-ran both steps clean: **313 real promotions** (first ever), exceptions down to 782 (from 1,095 —
the `T3` share exempted). Backward check: `strong.origin='word'` count now exactly 3,769 = 3,456 +
313 (reconciles exactly); `hib` count, `blindness`, and every other existing-data check unchanged.

Also produced, on request, the full 1,095-code candidate list grouped by cluster
(`backfill-promotion-candidates-20260812.md`) — since superseded in size by the rule correction
above, kept as the record of what the pre-correction population looked like.

## 6. `report.cluster` extended — comprehensive cluster summary

Researcher: *"by cluster, count of strongs, top 10 meanings by cluster (optimised so related words
are together e.g grace, gracious, graciously etc), number of spans, number of lexicals, number of
verses."* Built as a new section on the existing `report.cluster` (not a parallel report) — strong/
span/lexical/verse counts fall out of one query joining `cluster_strong` to `verse_lexical`; top-10
meanings via a deliberately simple English-gloss stemmer (`_stem_key()` — one-pass suffix strip +
short config-driven prefix), verified against the researcher's own example and spot-checked clean
across M01/M03/M05/M14/M15/M23. One accepted limitation flagged, not hidden: naive suffix-stripping
mishandles a trailing silent-e drop. While there, found and retrofitted `report.cluster`'s original
3 sections, which had **zero** `cfg_report_section` rows registered at all (carried since §104 by
`reportkit.render_scaffold()`'s "extra_keys" fallback, un-config-governed) — fixed alongside the new
one rather than left inconsistent.

Config: 7 more `configmaint.propose` rows, same self-approval authorisation.

## Left open, not silently dropped

- `cluster.validate`'s first escalation (782 exceptions post-correction) — awaiting researcher
  review.
- Rows 5-7 / `raw-complete` redefinition — sized, not built; the `receive`-postponement scope
  conflict flagged in §3 above still needs the researcher's call.
- Row 20 (verse-triggered T2→cluster reclassification) — sized and a detection approach prototyped
  earlier in the day's arc; researcher wasn't sure it was worth building yet.
- Filter re-triage's own build (raw.discover-time exclusion) — the re-evaluation is done (§2), the
  actual wiring is not.
- `backfill-promotion-candidates-20260812.md` is now stale (pre-dates the T2/T3 rule correction) —
  not regenerated this session; regenerate on request if still wanted.

## Files touched (this session)

**New code:** `iba/app/lib/clusterassign.py`, `iba/app/lib/strongreconcile.py`,
`iba/app/handlers/cluster.py`, `iba/app/ps/Cluster-Assign.ps1`.

**Modified code:** `iba/app/handlers/raw.py` (`backfill_meaning_for()` +reconcile call; new
`reconcile()` function/step); `iba/app/lib/clusterreport.py` (`_stem_key()` + `cluster_summary`
section).

**Config, via `configmaint.propose`** (escalations 615→640 this session): the full `cluster-assign`
work package (enum, 2 write grants, work package, 3 steps, 3 on_fail rows, 2 settings, report +3
sections) — BUILD.md §107; the `word_optional_clusters` correction — BUILD.md §108; the cluster-
summary section's 3 settings + 4 report-section rows (1 new + 3 retrofit) — BUILD.md §109.

**Data:** `cluster_strong` — 1,410 new auto-precedent rows (§4), then 218/203 unaffected by this
session (already applied prior session); `strong.origin` — 313 rows `backfill`→`word` (§5), with
`strong_verse`/`span`/`verse_lexical` extended for their newly-fetched verses.

**Planning/progress files:** `iba/app/reports/backfill-cluster-triage-plan-{v1,v2,v3}-20260812.md`,
`iba/app/reports/cluster-assign-build-spec-20260812.md`, `iba/app/reports/filter-retriage-
reevaluation-20260812.md`, `iba/app/reports/rows5-7-and-raw-complete-reevaluation-20260812.md`,
`iba/app/reports/lexicon-validate-escalation-review-20260812.md`,
`iba/app/reports/backfill-promotion-candidates-20260812.md`.

**Report output:** `iba/app/reports/cluster-assign-v1-20260812.md`,
`iba/app/reports/lexicon-parse-v2-20260812.md`, `iba/app/reports/cluster-v2-20260812.md`.

## Next

Researcher reviewing `cluster-v2-20260812.md` (the cluster summary) directly. Otherwise: the
`cluster.validate` escalation (782 exceptions) is the nearest open item; rows 5-7/`raw-complete`
and the `receive` rebuild remain queued behind it, in that order per the standing sequencing.
