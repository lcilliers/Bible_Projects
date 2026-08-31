# Why this programme keeps stalling — a control-gap diagnosis

**Date:** 2026-08-30. Prompted directly: *"read through the programme prose, read through the
objectives of IBA and think through the study program... what areas of controls, configuration,
rules would you expect a program of this nature... should be in place... what is left in the air...
what of the absence of these areas is exactly the reasons why this program have been stalling,
restarting, reworking, falling apart... time and time again."*

**Method.** Read the current programme prose in full (`wa-programme-prose-extract-20260827.md`,
chapters 0–6) — the programme's own self-description, not a summary of it — and derived, from
what the prose itself says the programme is trying to do and how it says it operates, what control
areas a project of this shape structurally needs. Then checked each area against what's actually in
place, using the prose's own admissions where it makes them (it makes several, unprompted) plus
direct schema/config checks. This is a diagnosis to think about, not a fix list to execute — no
escalation raised, nothing proposed as a change.

---

## The timeline this diagnosis has to explain

Started January 2026. Eight months later:

- At least **five distinct method resets** for the analytical layer: the original characteristic/
  tier/C-code model → the 2026-06-25 "characteristics to movements" reset (all M01–M11 "completed"
  work declared legacy) → the 2026-07-02 verse-first/passage/self-learning lexical method →
  2026-07-08's cycle+dimension authority layer → the 2026-08-03 closure of that whole line (v3
  verse-reading tested on Jonah 3, judged failed) → the 2026-08-05 IBA reopening → the current
  HIB/phenomenon/operation debate model, itself already at guidance-document v1.5 after a
  documented mid-course failure (the Amos 1-3 drift into literary-pattern analysis, caught only
  after production work had already been done under v1.4).
- A **database loss** (2026-06-03, Google Drive sync corruption) cost roughly six weeks outright.
- The prose's own Chapter 4 admits: of **18,558 passages** in the whole Bible, **49** currently
  carry any debate status, across **six books** — roughly 0.3% coverage under the current method,
  after eight months.
- The prose's own Chapter 2 admits: **"The programme does not currently have a mechanism producing
  a per-word reader-facing study"** — the exact thing Chapter 1 defines as what success looks like
  at the individual-word level.
- The finding store carries 438,000 rows, of which the prose itself says **92% are
  `delete_flagged`** — the residue of repeated re-reads and reworks, not 438,000 live findings.
- The question catalogue's own two lifecycle markers (`deleted` and `status`) **disagree with each
  other in count** — the prose names this directly rather than glossing over it.

None of this is my inference — every figure above is the programme's own prose stating it about
itself. The question is what's missing that would explain a pattern this consistent, this early,
recurring across a method that has been rewritten from the ground up multiple times.

---

## What a programme of this shape structurally needs — derived from its own stated method

The prose is explicit and detailed about *what* the method is (registry → collation → analysis →
synthesis; nine principles; nine constraints) and about the disciplines that keep data trustworthy
once produced (soft-delete, backup, field authority, patch review). It is far thinner — in most
places silent — on a different category: **the controls that would catch a bad method before
scaling it, and reconcile method changes with what was produced under the old one.** That thinness
is where this diagnosis concentrates, because it's the category the actual history keeps failing
on.

### 1. A pilot-before-scale gate on the method itself — MISSING, and the single largest candidate cause

Every method version in this programme's history has been discovered broken *after* production
work had already been committed under it, at a scale beyond a small pilot — never proven on a
bounded sample first. The Amos 1-3 case is the clearest, most recent, best-documented instance:
`WA-passage-read-guidance-v1.4` was applied across a real multi-chapter passage, drifted into
identifying literary/structural patterns instead of per-verse phenomena, and the drift was only
caught by the researcher's own review *after* the debate had been produced — triggering the v1.5
rewrite (the three-phase restructure) that governs the method today. The same shape recurs across
every earlier reset named above: a method runs for a period, is found wanting at a scale where the
cost of the finding is a rewrite, not a tuning pass.

What's missing is a **standing rule that a new method version is piloted on a small, bounded set of
passages first, independently re-validated (a second read reaching the same conclusion on the same
evidence), and only cleared for wider application once that pilot holds** — with the pilot's
outcome recorded, not just the eventual production run's. Nothing in `cfg_method_rule`,
`cfg_quality_check`, or the escalation system currently gates a method-version's *scale-up*, only
a passage's own closing validation (Phase 3, per-passage). The Phase 3 validation this programme
already has is real and it works — it's the mechanism that caught Amos 1-3 — but it fires per
passage, after the fact, at whatever scale the work happened to reach before someone looked. There
is no equivalent gate at the *method-version* level, checked *before* scaling past a pilot.

### 2. Version-stamping the data itself against the method that produced it — MISSING

Checked directly this session: neither `phenomenon` nor `operation` (the current method's core
analytical tables) carries an `updated_at`, a revision history, or a method-version stamp of any
kind — only `created_at`. When the method changes, there is no way to ask, mechanically, "which
rows were produced under the prior method version, and does the new version actually invalidate
them, or can they stand as-is." Every method reset in this programme's history has therefore had to
be resolved at the coarse level of a whole-line-of-work judgement — "all M01–M11 work is legacy,"
"the whole verse-reading line is closed" — rather than a targeted, row-level re-check of what
specifically the new method requires that the old one didn't test for. The 2026-08-28 "augment,
not harvest or redo" decision is the researcher's own direct correction against exactly this
pattern — but the correction is a stated policy, not yet a mechanism; nothing in the schema
currently lets a targeted re-check even be *expressed*, let alone run, because there's no column
recording which method version touched a given row. Without that, every future method revision is
structurally more likely to repeat the all-or-nothing framing the 08-28 decision was written to
stop.

### 3. Completeness of the check-set behind each step, not just correctness of the checks present — MISSING, demonstrated live this session

This is the finding this session's own cfg audit produced directly: `cfg_quality_check` and
`cfg_method_rule` were tested, up to now, only on whether each *existing* row is wired to real code
— never on whether the row *set* for a step actually covers every requirement the method's own
governing document states. Applying the corrected test to `phenomenon.set` surfaced a real,
previously invisible hole (whether a phenomenon's stated-vs-inferred status is honestly assigned
has no check of any kind). The Amos 1-3 failure is the same shape of gap playing out at production
scale before it was named: nothing was systematically checking, ahead of time, whether the
check-set in place actually covered "is this a genuine phenomenon, not a literary pattern" —
`not-a-literary-pattern` exists as a check now, but only because the failure happened first and the
gap was filled reactively. **The programme's quality layer has, so far, been built by finding gaps
after a failure, not by proving completeness against the method document before one.**

### 4. Reconciliation governance between parallel mechanisms — MISSING, and the prose names it twice, unprompted

Chapter 2 states plainly: *"Deriving understanding of the inner being currently runs through two
mechanisms that have not been unified into one pipeline... the programme has not yet reconciled the
two into a single analytical account of a word."* Chapter 4 states a second instance of the exact
same shape: the cluster/characteristic model is *"in practice, doing a version of the cross-word
synthesis work the SD pointer mechanism was built to feed... they have not been formally
reconciled."* Both are the programme's own words, not an inference. There is no rule, anywhere in
`cfg_*`, governing what happens when two live mechanisms turn out to be doing overlapping work — no
trigger that says "when this is discovered, it gets resolved by date X," no owner, no forcing
function. Each mechanism keeps receiving investment; neither converges into the single account
Chapter 1 defines as the deliverable. Effort split across two unreconciled tracks, indefinitely, is
by itself a plausible structural driver of "always in progress, never finished" — independent of
whether either mechanism, on its own, is working correctly.

### 5. A build path from analytical unit to the actual defined deliverable — ABSENT, not merely incomplete

Chapter 1's own definition of success is explicit and specific: *"At the level of the individual
word, [success] is a written study..."* Chapter 2's own Programme Flow section states, in the
programme's own words: *"The programme does not currently have a mechanism producing a per-word
reader-facing study."* Eight months of registry-building, base-data extraction, debate-pipeline
construction, and cluster/characteristic modelling have been infrastructure feeding toward a
deliverable that, as of this writing, has no build mechanism at all — not a rough one, not a
draft-quality one, none. Every other control gap in this document describes something incomplete
or unreconciled; this one describes something that has not been started, at the exact point the
programme's own definition of success is anchored. Whatever else gets fixed among the gaps above,
this is the one whose absence most directly explains "eight months in, nothing has reached the
finish line" — because the finish line itself has no path drawn to it yet.

### 6. Pace-versus-scope forecasting — MISSING

The programme's own constraint (Chapter 2) is corpus-level treatment: every verse read, every term
classified, no survey-level shortcut. Measured against that commitment, 49 of 18,558 passages after
eight months is a real data point about achievable pace under the current method's cost per
passage — and nothing in `cfg_*` or the escalation system currently tracks it, forecasts from it,
or asks whether the corpus-level commitment and the demonstrated pace are compatible. This isn't a
missing report; it's a missing question. Nobody — human or config — is currently positioned to
notice if the answer is "not compatible" before another several months pass.

---

## What is genuinely strong, for contrast

This is not a diagnosis that the programme lacks discipline generally — the opposite is true in
several areas, and the contrast is informative about *where* the gap actually sits. Data integrity
once something is written (soft-delete, backup, patch review, field authority), the two-AI
division of responsibility, session continuity discipline, and the escalation/config-change
machinery itself are all mature, well-tested, and — per this session's own audit — largely doing
what they claim to do. The gap this diagnosis identifies is narrower and more specific than
"insufficient governance": it's specifically the controls that operate *at the level of the method
itself* — proving it before scaling it, reconciling it when it forks, stamping data with which
version of it produced a row, and connecting it all the way through to the deliverable it exists to
produce. The programme has built extensive machinery for executing a method faithfully and
recording that execution defensibly. It has built much less machinery for knowing, ahead of a
costly production run, whether the method being executed so faithfully is actually the right one —
and that is exactly the category of failure the eight-month history keeps producing.
