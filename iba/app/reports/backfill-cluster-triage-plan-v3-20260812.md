+# Cluster-assignment as an app module — v3: strong expectations table + a single-strong reconciler

> Supersedes v2's open questions with your decision table + answers to Q2.4.1/Q2.4.2, plus three
> new requirements (a single-strong reconciler handler, `new-word` completeness, and the formal
> expectations table itself). v1/v2 kept for provenance — the architecture in v2 (choke point at
> `detail_one()`, mechanical-vs-judgment tiering, work-package shape) still stands; this version
> makes it concrete enough to build.

## a) The Strong Expectations Table — formalised from your spreadsheet

Read row-by-row against the live schema. Most rows map cleanly; **two need your confirmation**
because they read as an actual behaviour change from what the code does today, not just a
description of it — flagged inline, not assumed either way.

| # | Expectation | Active | Backfill | Maps to (live schema) |
|---|---|---|---|---|
| 1 | Has `word_registry` | Y | N | `word_strong` link exists |
| 2 | Has cluster | Y | largely no, but T2 allowed | `cluster_strong` (Active: non-T2 expected; Backfill: T2 is a legitimate stable state, not a defect) |
| 3 | In `strong` table | Y | Y | `strong` row exists (both origins already do this) |
| 4 | Has verses in verse table | Y | Y | the `verse` row(s) for whatever verse(s) the code's spans sit in — **exist**, because a `backfill` code only ever surfaces from a span in an *already-pulled* verse. This is **not** `strong_verse` (the code→verse assertion) — that's the row genuinely missing for `backfill` today (confirmed: 0/11,837), and Q2.4.2 below is about fetching it, not about this row. |
| 5 | Appear in span of verse in verse-table | Y | Y | `span.strong_variant` — confirmed live: 100% of checked `backfill` codes already appear here |
| 6 | Has entry in meaning tables | Y | Y | `strong_sense`/`strong_meaning_tree`/`strong_lexicon` |
| 7 | Has entry in parse tables | Y | Y | `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` |
| 8 | Appear in related lexicals | Y | Y | `verse_lexical` — confirmed live: 100% of checked non-T2 `backfill` codes already have rows here (book-scoped `lexical.build` is origin-blind) |
| 9 | Use span variant in Lexical for every instance | Y | Y | `resolve_code()`'s exact/base-variant resolution — same for both, no bare-gloss-only restriction |

**Reverted 2026-08-12, same day — T2/`backfill` keeps full parse.** Researcher direction: rows 6/7/9
are **not** a behaviour change — `backfill` carries the same meaning/parse depth as `word`-origin,
matching what `detail_one()` and the corpus-wide `lexicon.parse` rebuild already do today
unconditionally. No code change needed for this row group; struck from the build. The Q2.4.1/Q2.4.2
promotion cascade below is corrected to match (meaning/parse are already present, not something
promotion newly populates).

### Invariants (rows 14–20), as standing rules

- A lexical (verse_lexical) can reference multiple strongs; a verse's span-set and lexical-build are
  each singular/canonical (version-aware supersede, never multiple coexisting sets) — matches the
  existing convention already used for `span`/`verse_lexical` rewrites.
- An Active strong must have exactly one *current* set of meaning + parse entries (ties directly to
  the rows-5–7 staleness/freshness work already queued — same invariant, shouldn't be built twice).
- A verse touches multiple clusters (via its multiple strongs); a strong can legitimately sit in
  multiple clusters (already established — T3+M-code edge cases, `receive`'s multi-cluster
  precedent).
- **Row 20 — the one genuinely new rule: "a T2 strong should be promoted to a different cluster if
  it is used to derive meaning (as a qualifier, for another strong with a cluster) in a verse."**
  This is a **third promotion pathway**, distinct from both the mechanical precedent-match and the
  judgment-tier batch review in v2 — it's **verse-analysis-triggered**, discovered only once a
  verse is actually read, not knowable from the gloss alone. This directly resolves the
  "descriptors" question the cluster-allocation session's obslog left open (your own reflection
  there: *"the descriptor is paired with an operation and therefore belong in T3... when the verse
  is analysed, these will be pulled in automatically"*) — row 20 turns that passive expectation into
  an explicit rule. **Proposing this itself escalates rather than auto-reclassifies** — a single
  verse's usage pattern reclassifying a strong's *general* cluster membership is exactly the failure
  shape the `classify_role`/role-gating precedent already got burned by once (BUILD.md §56-57,
  silently dropped real content) — flagging as a design default, not deciding unilaterally.

## b) A single-strong reconciler — the comprehensive handler you asked for

**New step, `strong.reconcile(code)`** — one code in, full sequence out, the single entry point
both new-strong-creation paths and any future backlog-clearing run call. Sequence:

1. **Classify** — cluster lookup against `cluster_strong`. If none exists, attempt the mechanical
   HIGH-precedent match (P1/P2, v2 §2.2). If that resolves, write the row
   (`source='auto-precedent'`). If it doesn't resolve, leave unclassified — this is the queue
   `cluster.validate` finds by absence (v2 §2.3), not a failure state here.
2. **Exception check (Q2.4.1, below)** — before touching anything else, check for the two named
   exception shapes. If either matches, **raise and stop** — no further steps run for this code
   until the exception is resolved.
3. **Promotion decision** — if the code's cluster assignment (existing or just-written) is
   non-`T2`/non-empty and `origin='backfill'`: promote (Q2.4.2 cascade, below). If `T2`-only:
   confirm/leave as `backfill`, done. If unclassified: leave pending, done (nothing to promote yet).
4. **Promotion cascade (Q2.4.2)** — `origin` flips to `'word'`; full STEP verse fetch (§ below);
   span rebuild for any newly-discovered verses; `verse_lexical` rebuilt/extended to cover those new
   verses. Meaning/parse tables need no new action — already present for both origins (rows 6/7,
   reverted above) — only the *verse coverage* they get read against changes.

This is the **one place** all of v2's separately-sketched pieces (mechanical match, promotion
cascade, `strong_verse` fetch) actually live — `cluster.assign`'s DB-wide sweep and `lexical.build`'s
auto-backfill hook both become "call `strong.reconcile(code)` for each candidate," not separate
re-implementations.

## c) `new-word` completeness — ties directly into the reconciler, not a separate wiring task

Your instruction: `new-word` must complete the entire process through building/updating
`verse_lexical` for **qualifying strongs** (i.e. whatever `strong.reconcile` resolves as
non-`T2`/`FLAG`-appropriate). Concretely: `raw.write`/`raw.validate` (the chain's last two steps
today) should call `strong.reconcile(code)` for each of the word's own codes. Because
`strong.reconcile` already fully owns the parse/related/lexical cascade (§b, step 4), this **absorbs
what the `receive` rebuild was scoped to wire in** (v2 §2.5) — that rebuild's job becomes "extend
`new-word` to call the reconciler," not a separate hand-wired set of three steps. Still the right
live end-to-end test for both mechanisms together, per your earlier direction — not restarting that
decision, just noting the two pieces of work converge into one.

## Q2.4.1 — exceptions, not silent fixes

Two shapes, both raised via the standing `escalation` table (same mechanism every other
judgment-requiring check in this app already uses — nothing new to build there):

1. **A strong has a cluster assignment but no `word_registry` link at all.**
2. **A `backfill` strong is found where a related strong** (reading this as: a sibling
   exact-variant/same-lemma code, or the same code under a different context) **is already
   `origin='word'` and/or already carries a cluster assignment.**

**Two-mode handling, exactly as you specified:**
- **Historical backlog** (today's data — the 865-with-cluster / 419-non-T2 set from v1, and any
  other pre-existing instance of either shape): a **bounded, one-time clearing run**, same shape as
  every other one-off migration script already in this codebase (`bootstrap_*`, `apply_*`) — clears
  what's there now, reports what it did.
- **Standing behaviour, going forward:** `strong.reconcile` hitting either shape **always
  escalates**, never silently resolves it the way the one-time run did. This is the actual
  distinction your comment draws ("if it is happening again, then I need to know, not just a silent
  fix") — the one-time run and the standing reconciler are **not the same code path**, even though
  they clear the same *kind* of problem, because their job is different: one closes a known backlog,
  the other watches for the backlog reopening.

## Q2.4.2 — the promotion cascade, confirmed in full

**Settles v2's open depth question: always a real STEP fetch, never derived-from-existing-span.**
Every `backfill→active` promotion:

1. **Verses** — `call3_strong`-equivalent STEP fetch for the code (the same mechanism
   `raw.py:verses_one()` already uses for `word`-origin codes) — its *complete* Bible-wide
   occurrence set, not just the incidental subset already sitting in the DB from other words' pulls.
2. **Span** — for any verse this fetch surfaces that wasn't already in the DB, parse and write spans
   (reuses `verses_one()`'s own span-writing path unchanged).
3. **Meaning/parse** — no new action (rows 6/7 reverted — both already present regardless of origin).
   A defensive re-confirm is cheap and harmless (the parse rebuild is a full corpus rebuild anyway),
   but nothing is *newly* populated here the way v3's first draft assumed.
4. **Lexical** — rebuild/extend `verse_lexical` to cover whatever verses step 1 newly surfaced —
   the *existing* verses this code already had lexical rows for (100% coverage, confirmed) don't
   need rebuilding, only the newly-fetched ones need building for the first time.

This is exactly `verses_one()` + `lexical.build_for_verse_ids()` for the newly-fetched verses,
called in sequence for one code — no new fetching mechanism needs inventing, only the sequencing and
the trigger (§b/§Q2.4.1 above). Smaller cascade than first drafted, now that rows 6/7 are reverted.

## What's still open

Only one real gap remains after this round: **row 20's own promotion path** (verse-triggered T2→
cluster reclassification) needs its trigger point designed — most likely a check inside
`lexical.build`/`resolve_code()` itself (it already knows, per verse, which codes co-occur and which
carry a cluster) — but that's genuinely new mechanism, not a restatement of anything existing, and
deserves its own pass rather than folding into `strong.reconcile`'s already-full sequence above.
Flagging rather than designing further until the rest of this is confirmed.

## Addendum — row 20, sized and prototyped (2026-08-12, same day)

Your reflection: not sure how real an issue this is; you'd notice it by seeing "missing meaning" in
a verse lexical, tracing it to a T2 code that's bare-gloss-only, and wondering how to spot that
systematically. Checked both halves directly rather than reasoning abstractly.

**How big is it, today?** Not an issue. Checked all 1,227 T2-classified codes' existing
`verse_lexical` rows (96,315 of them): **0 are bare-gloss-only** — every one currently carries real
parsed content, because `lexicon.parse` is origin/cluster-blind. **Now that rows 6/7/9 are reverted
(T2/`backfill` keeps full parse, standing decision), this stays true going forward, not just today**
— the completeness gap row 20 exists to catch can no longer arise from that direction. Row 20's own
promotion trigger (a T2 code reclassified because verse-level usage shows it qualifying a clustered
term) is therefore lower-priority than first scoped — worth keeping the detection idea on file
(below), not worth building now.

**How to detect it — prototyped, not just theorised.** Two attempts, both using data that already
exists (`span.position`, `verse_lexical`, `cluster_strong`) — no new mechanism needed for the
signal itself:

- **Naive: raw adjacency count** (T2 code's span sits next to a clustered code's span, count how
  often). **Doesn't work** — dominated entirely by the highest-frequency particles in the language
  (`H0853` the untranslated direct-object marker, 3,581 adjacencies to `T3` alone; `H3808` "not";
  `G2532` "and"). These are adjacent to *everything* because they're everywhere — the count tells
  you nothing beyond "this word is common," which you already know.
- **Refined: concentration, not count** — for each T2 code, what *share* of its own total
  occurrences sit next to the *same one* cluster (excluding `T3`, which is itself too generic a
  neighbour to be meaningful here — operations sit next to almost every preposition/particle as a
  matter of grammar, not semantic pairing). This filters the 1,227 down to **~148–184 codes** with a
  real concentrated pattern — a reviewable-sized list, same shape as the T2-likeness review's 64
  flagged items. Spot-checked the top of the list: some clearly real (`H0639G` "face" — the Hebrew
  anger-idiom, 89/148 = 60% of its occurrences sit next to `M02` Anger; `H1881` "law" next to `M15`
  Wisdom), some plausibly coincidental (`G0220` "rooster" next to `M42` Speech — almost certainly
  just Peter's denial narrative, not a real pairing).

**Recommendation:** this is a **report, not a pipeline trigger** — matches how you actually described
noticing it ("I will notice it when I look at a verse lexical"), and matches every other tier in
this whole exercise (a statistical signal surfaces candidates; a human decides). Proposing it as a
periodic, config-registered report (same shape as `report.cluster`/`lexicon.validate` — persisted,
read-only, escalates only if the researcher wants it to) rather than new logic inside
`lexical.build` itself. Not built — sized and prototyped only, per your steer that you're not yet
sure it's worth building at all.
