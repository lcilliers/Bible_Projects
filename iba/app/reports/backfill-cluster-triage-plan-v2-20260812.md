# Cluster-assignment as an app module — holistic plan (v2, supersedes v1's staging)

> Supersedes `backfill-cluster-triage-plan-20260812.md`'s framing, per researcher direction: v1
> staged this as a one-off corrective ("run the promotion, then run the big allocation pass") —
> correctly identified in review as **treating a structural gap as a hot fix**. This version
> answers three questions first — where cluster-assignment fits in the app, what must be built for
> it to be a repeatable process, what corrective action aligns existing data — in that order, with
> the correction *last*, not first. v1's live numbers (§3 there) still stand and are reused below;
> not re-derived.

## 0. Question 1, answered from the code — when do new strongs surface?

Traced every code path that writes a `strong` row. There are exactly **two**, both funnelling
through the same function, `handlers/raw.py:detail_one()`:

- **(a) `new-word` chain** — `raw.detail` calls `detail_one(..., origin="word")` for each of a
  word's discovered codes. **Confirmed, live, working.**
- **(b) `verse-lexical` build** — `handlers/lexical.py:build()` (work package `verse-lexical`,
  ordinal 0) **auto-calls `raw.backfill_meaning_for()` before every build**, gated by
  `cfg_setting report.auto_backfill_before_render` (default `True`). That function finds codes
  referenced in `span` rows with no `strong` row yet and calls `detail_one(..., origin="backfill")`
  for each. **Confirmed, live, working** — this is exactly your scenario (b): a code surfaces
  because verse-lexical touches a span whose code was never onboarded, and it gets created as
  `backfill` right there, automatically, mid-build.
- **(c), as you framed it ("verse-lexical discovers a backfill strong should have full
  meaning") — does not exist.** Checked `lib/lexical.py:resolve_code()` (what verse-lexical
  actually calls per code) directly: once a `strong` row exists, at *any* completeness level,
  nothing re-examines it. A `backfill` code that turns out to be inner-being-relevant sits exactly
  as thin as the one that turns out to be pure supplementary noise — verse-lexical has no opinion
  on which is which, and nothing prompts a re-check later. **This absence is the actual gap** — not
  a bug in an existing mechanism, a *missing* one. Everything below is about building it.

One more foundational fact, checked directly: **`cluster`/`cluster_strong` have exactly one write
grant today — `migration`** (`cfg_write_grant`, both rows). Every write either table has ever
received came from a one-off migration script (`bootstrap_cluster_tables_20260811.py`,
`apply_cluster_alloc_v1_3_20260812.py`, `apply_prior_reassignments_v1_1_20260812.py`). **No live
handler is even permitted to write to the cluster tables.** The cluster model, as it stands today,
is a static reference loaded once — not yet a working part of the pipeline. That is the real shape
of "where this needs to fit": nowhere yet.

## 1. Where cluster-assignment fits in the app — the holistic picture

```
strong-creation choke point (BOTH paths go through detail_one())
  ├─ (a) new-word: raw.discover → raw.detail → detail_one(origin="word")
  └─ (b) verse-lexical: lexical.build → auto-backfill → backfill_meaning_for() → detail_one(origin="backfill")
                                                              │
                                                              ▼
                                            [MISSING TODAY] cluster lookup/assignment
                                                              │
                                              ┌───────────────┴───────────────┐
                                              ▼                               ▼
                                   HIGH-confidence match              no match / MEDIUM / LOW
                                   (mechanical, safe to               (needs judgment — queue,
                                    automate — P1/P2 precedent)        don't guess)
                                              │                               │
                                              ▼                               ▼
                                   write cluster_strong row          escalation / batched
                                   (source='auto-precedent')          allocation review
                                              │                               │
                                              └───────────────┬───────────────┘
                                                              ▼
                                    cluster_code != T2  →  origin should be 'word'
                                    (promotion cascade: strong_verse, parsed layer,
                                     related, verse_lexical freshness)
```

**The fit:** this is not a new pipeline running alongside the existing one — it's a **third stage
at the exact same choke point** `origin` stamping already occupies inside `detail_one()`. Every
`strong` row, from either creation path, should leave `detail_one()` with an attempted cluster
classification, the same way it already leaves with an `origin` stamp. Where classification can't
be resolved mechanically, it should leave in a **known, queryable "pending" state** — not silently
unclassified with no trace, which is today's actual state for 10,972 of 11,837 `backfill` codes.

## 2. What must be built — for this to be a repeatable process, not a one-off

### 2.1 A config-defined correctness rule (your framing, taken literally)

A `strong` row is **correct** when:
1. it has **at least one** `cluster_strong` row (not zero — "unclassified" is itself a defect
   state, not a neutral one), **and**
2. **if** any of its `cluster_strong` rows has `cluster_code != 'T2'` (an M-code, `T3`, or `FLAG`),
   **then** `strong.origin = 'word'` — i.e. it carries the full raw-data-integrity chain, not the
   meaning-only `backfill` treatment.

This is a **bidirectional invariant**, registered as data (`cfg_quality_check`, the same table
`hib.set`/`phenomenon.set`'s existing gates use — or a `cfg_setting` if a hard gate isn't wanted
yet), not asserted only in this document. Per `governance.rules_must_be_config_driven`: until this
rule is a `cfg_*` row some code actually reads, it isn't a real rule — it's a one-time judgement
call, exactly what v1 of this plan mistakenly scoped it as.

### 2.2 The mechanical tier — safe to code natively, no LLM needed

The cluster-allocation session's own HIGH tier (`P1` exact gloss match to an existing labelled
`cluster_strong` row; `P2` exact gloss match to `cluster.csv`'s gloss list) was **deterministic and
needed no researcher decision** — the session log says so explicitly, and the pitfalls list (§5
there) already tells you what NOT to do (no TF-IDF/profile scoring for HIGH, exclude the FLAG gloss
list from voting, token/stem-match not substring, watch multi-cluster prior rows). This part is
directly codeable, reusing the exact rules already proven:

- **New library, `lib/clusterassign.py`** — a `match_precedent(strong_row) -> (cluster_code,
  confidence, rationale) | None` function implementing P1/P2 only (HIGH tier), built from the
  session's own decisions register (§3 of the session log) and pitfalls (§5) directly, not
  re-derived from scratch.
- Runs **inside `detail_one()`**, right after a new `strong` row is written (either origin) —
  attempt a HIGH-confidence match immediately, at creation time, not later by accident. On a HIGH
  hit: write the `cluster_strong` row now (`source='auto-precedent'`).

### 2.3 The judgment tier — formalise the existing ad hoc workflow, don't auto-decide it

MEDIUM/LOW (profile-suggestion, no-precedent, competing candidates) **correctly required
researcher/LLM judgment** in the 1,612-code exercise, and the session log's own pitfalls warn
against pretending otherwise (TF-IDF "wanted 'brother' → Deceit"). This tier should **not** be
auto-coded as a blind algorithm. What it needs instead is the same shape every other
judgment-requiring step in this app already has:

- A **queue**, not a silent gap: every `strong` row that leaves `detail_one()` without a HIGH match
  gets a `cluster_strong`-adjacent "pending" marker (or simply: **no row at all is the queue** —
  `cluster.validate`, below, finds them by absence, same convention `lexicon.validate` already
  uses for `strong_related`/`strong_lsj_parsed` coverage).
- A **new work package, `cluster-assign`**, registered via `Config-Maintenance.ps1 -Step Propose`
  (can't create tables, but *can* register steps/settings on the already-existing `cluster`/
  `cluster_strong` tables):
  - `cluster.assign` — runs the mechanical P1/P2 pass DB-wide (catches anything `detail_one()`
    missed, or lets you batch-process a backlog); for anything not resolved, packages a
    **researcher/LLM-review batch** in the exact input shape the 1,612-code exercise already used
    (`cluster.csv`/`cluster_strong.csv`/`strong_without_cluster.csv`-equivalent), so the *same
    external Claude-AI-chat workflow* (proven, not hypothetical) is the standing way to clear the
    judgment tier — this app module's job is producing that package and applying the answer, not
    replacing the judgment itself.
  - `cluster.validate` — read-only, DB-wide coverage report, same shape as `lexicon.validate`:
    counts of unclassified strongs (by origin), `backfill`-origin non-T2 strongs not yet promoted
    (the §2.1 invariant's second half), escalates once if findings exist, persists a report every
    run (`governance.reports_must_persist`).
- **New write grant:** `cluster.assign` → `cluster_strong` (and `cluster` if a future pass can add
  clusters, mirroring `T3`'s creation). `migration`'s grant stays for one-off bootstrap use, not
  removed.

### 2.4 The promotion cascade — wired to the invariant, not a separate manual step

When a `strong` row's classification resolves (or is later confirmed) `!= T2`:
1. `origin` flips `'backfill' → 'word'` — **the sticky-upgrade code for this already exists**
   (`detail_one()`'s existing `origin=='word' and existing['origin']=='backfill'` branch) but is
   only ever triggered by a *word claiming the code*. This needs a **second trigger path**: cluster
   evidence alone, with no word claim. Real design question, not decided here: does a
   cluster-promoted code need a home in `word_registry`, or can `origin='word'` legitimately exist
   with zero `word_strong` links, as its own case? (Carried over from v1 — still open, sharper now
   that it's a wiring decision, not just a data question.)
2. The verse-completeness gap this promotion actually creates — `strong_verse` — needs the SAME
   depth decision v1 raised (derive-from-existing-`span` vs. a real STEP re-pull). This is now
   visibly the **same fork rows-5–7's own build spec depends on** (a word's completeness gate is
   only as honest as what counts as "this code's verses are complete") — build these two pieces of
   work together, not as separate passes touching overlapping rows twice.
3. Parsed layer / `strong_related` / `verse_lexical` freshness — per v1's own live check, **these
   are already current for the 419 codes checked** (100% span, 100% verse_lexical, 98% parsed) —
   the cascade's job for most codes is confirming this stays true going forward, not rebuilding
   from scratch each time.

### 2.5 Fits into work already in flight, not parallel to it

- **Rows 5–7 / `raw-complete` redefinition** (separately queued): a word can't honestly be
  "complete" if its own codes are sitting misclassified as `backfill`/unclassified. Recommend
  folding cluster-correctness into the same completeness gate rather than building two adjacent,
  overlapping checks.
- **`receive` rebuild** (postponed, now the live end-to-end test for "does adding a new word
  trigger everything"): once `detail_one()` carries the §2.2 hook, `receive`'s own onboarding
  becomes a real test of cluster-assignment-at-creation too, not just the parse/related/lexical
  wiring it was originally scoped for. Worth explicitly including in that test's checklist when it
  runs.
- **Filter re-triage** (raw.discover-time exclusion, still separately queued): this module and that
  one share the identical lookup mechanism (`cluster_strong`) but act at different moments — filter
  re-triage decides whether a code *enters* `word_strong` at all; this module classifies a code
  **after** it already has a `strong` row. They should share `lib/clusterassign.py`'s lookup
  function, not each grow their own.

## 3. Corrective action on existing data — now correctly scoped as *first run of the new module*

With §1–2 built, the backlog v1 sized is not a bespoke fix — it's what running the new module
against the current DB produces on its first pass:

- **419 `backfill`-origin codes with an existing non-T2 assignment** (v1 §3) — the promotion
  cascade (§2.4) runs against these immediately; no new classification judgment needed, the
  assignment already exists.
- **446 pure-T2 `backfill` codes** — already correctly classified, already correctly excluded;
  `cluster.validate` should show these as clean, not flag them.
- **10,972 unclassified `backfill` codes** — `cluster.assign`'s mechanical pass (§2.2) clears
  whatever resolves on precedent alone; the remainder packages into judgment-tier batches (§2.3),
  run the same proven way the original 1,612-code exercise was — at roughly 7× the scale, so
  probably several batches, not one.
- **2,705 `word`-origin non-T2 codes** — already correctly `origin='word'`; nothing to do, but a
  useful `cluster.validate` clean-check.
- **751 `word`-origin pure-T2 codes** — worth a second look once the module exists: a `word`-origin
  code classified `T2` (no inner-being relation) sitting inside an onboarded study word is a
  legitimate outcome (not every code STEP returns for a word is itself IB-relevant — that's
  filter-re-triage's exact concern) but worth `cluster.validate` surfacing as its own count, not
  folded silently into "clean."

## 4. What's still open (carried over, not re-litigated)

The five questions v1 raised (§5 there) mostly resolve into the design above, except: **the
ownership question (§2.4.1)** and **the depth-of-`strong_verse` question (§2.4.2)** — both need
your direction before `cluster.assign`'s promotion cascade can be coded, since they determine what
it writes. Everything else in this version is a proposed shape for your review, not a build
already underway.
