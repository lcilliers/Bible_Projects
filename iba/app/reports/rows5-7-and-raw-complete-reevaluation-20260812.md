# Re-evaluation — "Rows 5–7 build spec" + "raw-complete redefinition", as a package

> Requested 2026-08-12, after approving the `lexicon.validate` escalation and postponing the
> `receive` rebuild (now earmarked as the live end-to-end test of "does adding a new word trigger
> every underlying process"). Re-checked the source plan against live data before scoping any
> build — nothing below has been built yet.

## Source recovered

The session log's "rows 5–7" phrase pointed at a full plan document that was never committed to
the repo — it survived only in Claude Code's own plan store:
`C:\Users\lerouxc\.claude\plans\first-raw-data-vivid-fairy.md` (415 lines, dictated the same
power-failure-recovery session, §1 of the session log). Read in full; re-verified its factual
claims against the live DB below rather than trusting the write-up as still-current.

## What rows 5–7 actually are (the plan's own 7-point expectation)

A word's raw data is "complete" only if, per registry word: (1) has Strong's codes, (2) each code
has verses, (3) each code has raw meaning, (4) verses have spans that recover every asserted verse,
**(5) each code has a *parsed* meaning**, **(6) its verses have verse lexicals**, **(7) each
`verse_lexical` row is correctly traceable to that code's parsed meaning**. `raw.write` today only
gates on 1–4; rows 5–7 are unchecked at word level, run (if ever) as separate, independently-scoped
work packages.

## Live re-verification (today, not trusted from the plan's write-up)

- **`cfg_step` for `new-word` still has no `lexicon.parse`/`raw.related`/`raw.lexical` step** —
  unchanged since the escalation review earlier today.
- **178 raw-complete words**, unchanged.
- **Row 5 gap, corpus-wide:** 474 distinct Strong's codes (across raw-complete words) have no
  *exact* `strong_meaning_parsed` row. Of those, **472 resolve correctly via the base-lemma
  fallback** (mirrors `resolve_code()`'s own exact-then-base lookup exactly) — only **`G6507` /
  `G7167`** (blindness, already reviewed above) have *true* zero coverage, and both have zero verse
  occurrences, so they can never produce a `verse_lexical` row anyway.
- **Row 7 gap, corpus-wide:** of 534,071 `resolved`-status `verse_lexical` rows, only **4** are
  genuine bare `stepGloss:`-only fallbacks (the plan's failure mode) — all four are `H5945H`
  ("[LORD] Most High", a divine-title code), verses 1430/9384/9386/25672. Not blindness, not
  anything in the plan's own worked example.
- **Blindness specifically:** still 276/276 verses carry ≥1 `verse_lexical` row (the book-wide
  `lexical.build` already covered it); its 3 base-fallback codes (`H3543A`/`H5788A`/`H8173A`)
  resolve correctly via base fallback, confirmed live.

**Conclusion: the actual live failure surface for rows 5–7 is tiny** — 2 zero-coverage codes (both
already zero-verse, so zero practical impact) and 4 bare-fallback rows corpus-wide, not a sweeping
178-word problem. The gate is still worth building (nothing stops a *future* word from landing in
the same hole, at scale — `receive`'s 64-code pull is the cautionary case), but the retroactive
"178-word recheck" is not high-risk, contrary to how it might sound stated cold.

**One more scoping fact:** 98 of the 178 raw-complete words already have ≥1 verse touched by
completed downstream HIB work (the six debated books' 21 `hib` rows happen to co-occur with these
words' codes). Redefining `raw-complete` retroactively doesn't rebuild or invalidate that work —
matches the researcher's own standing instruction that analytic work "will be revisited... nothing
to worry about" — but it's worth having in view before signing off on the recheck.

## Judgment calls the plan itself left open — status now

The plan named 6 judgment calls, framed as needing confirmation before it could be turned into a
real build spec. Re-checked each against what's been decided since (this session, and the
power-failure-recovery session's §1):

1. **Row 7 check granularity (per-code-once vs. every span-occurrence)** — still open, not
   addressed by anything since. Needs a direct answer: does "row 7 holds" mean *at least one*
   `verse_lexical` row for a code correctly reflects its parsed meaning, or *every* row for every
   occurrence?
2. **Redefine `raw-complete` in place vs. new downstream status** — **answered** by your
   instruction ("the new rule ... raw-complete requires the underlying strongs' lexicals to be
   complete... in place, not a new downstream status" — recorded already in the session log §1).
3. **Staleness = failure, not accepted lag** — **answered inline** while the plan was being
   written; carried into the plan's own §6 design ("a live re-derivation, not a plain existence
   probe").
4. **Build stage-b (Strong relevance filtering) before rows 5–7?** — this is the plan's name for
   what the session log calls **"filter re-triage"**, and the session's own sequencing put it
   **before** rows 5–7 ("Filter re-triage → rows 5–7 build → raw-complete redefinition"). Your
   instruction today moves straight to rows 5–7 + raw-complete without it. **Flagging, not
   assuming either way** — is filter re-triage now deliberately deferred past rows 5–7 (order
   changed), or should it still land first and this package waits?
5. **Stage f (lexical exclusion) framing dropped** — no objection raised since; treating as closed,
   per the plan's own default.
6. **Stage-b two-precedent split (mechanical lexical-family filter + reframed GR-PROG-007)** — same
   bucket as #4, not part of rows 5–7 itself.

## The real scope conflict with today's "receive postponed" decision

The plan's own build spec for **item 5** and the closing recommendation both include: *"Wire
`lexicon.parse` into `cfg_step` for `work_package='new-word'`, right after `raw.detail`"* and
*"Wire `handlers/raw.py:lexical()` into `cfg_step` for `new-word` (after `raw.validate`)"*. **This
is the identical wiring work the `receive` rebuild exists to do** — the two dormant functions
(`raw.py:related()`/`lexical()`) the plan itself names as "written for the 'wire the complete cycle
into `new-word`' ask... never wired into `cfg_step`" are exactly what a `receive` rebuild would
register.

Since you've just directed that the `receive` rebuild is postponed and repurposed as the live
end-to-end test of "adding a new word triggers everything" — **building rows 5–7's own spec
verbatim would wire that same chain in today, before the test exists to prove it.** Two ways to
resolve this, not decided here:

- **(a)** Build rows 5–7 as **checks + one-time correction/sweep only** this pass (the
  `validation.py` §5/§7 additions, the DB-wide `lexicon.parse` re-run, the `raw-complete`
  redefinition applied to the 178 words) — but leave `cfg_step` wiring of
  `lexicon.parse`/`raw.related`/`raw.lexical` into `new-word` itself for the `receive`-rebuild
  session, so that rebuild is genuinely the first time the automatic chain gets proven end-to-end.
- **(b)** Wire it now as the plan specifies, and let `receive` serve as a *confirmation* run rather
  than the *first* test of newly-wired code.

**(a) is what "receive rebuild is therefore postponed" reads as meaning to me** — flagging for your
confirmation rather than assuming, since it changes what "rows 5–7 build spec" concretely ships
this round.

## Also buried inside item 5's own spec — a real scope adder

The plan's item 5 additionally recommends a **new `lexicon.correct`/`raw.correct` step** (approval-
gated, `cfg_step`-registered, its own write-grant, a `debate_change_detail`-style audit row) to
replace today's bespoke one-off migration-script pattern for correcting a Strong's raw meaning —
because it found **no correction path exists at all** today (`raw.detail_one`'s unconditional
early-return on an existing `strong` row means nothing short of a manual migration script can ever
fix a bad raw value). This is real and true, but it's a materially bigger, separate piece of work
from "add a completeness check" — worth confirming whether it's in scope for this package or a
later one.

## Recommendation

Build this pass as: (1) the `validation.py` §5/§7 completeness + freshness checks (word-scoped and
DB-wide), reusing `resolve_code()` exactly per the plan's own design; (2) the one-time DB-wide
`lexicon.parse` re-run + sweep to confirm the count above (already known to be tiny); (3)
`raw-complete` redefinition wired into `cfg_status_flow`/`raw.write`'s gate, plus the 178-word
recheck (low-risk per the scan above); (4) the verse-level auto-reset cascade (item 6b) and content
fingerprint (item 7) built as designed. **Defer:** wiring `lexicon.parse`/`raw.related`/
`raw.lexical` into `cfg_step` for `new-word` itself, and the new `lexicon.correct` step — both left
for the `receive`-rebuild pass, so that pass is a genuine first test, not a re-confirmation.

Two things need your direct answer before I start: **judgment call #1** (row-7 check granularity)
and **the filter-re-triage sequencing question** above. Everything else in this package is either
already decided or low-risk enough to proceed on once those two are settled.
