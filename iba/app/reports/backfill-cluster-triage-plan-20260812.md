# Triage plan — promoting `backfill`-origin strongs to active/full-meaning by cluster evidence

> Requested 2026-08-12: read every doc in `iba/docs/cluster assignment process/` (the session log,
> obslog, and both review docs) in full, then build a plan for the rule: *"everything allocatable
> to any cluster except T2 should carry a full meaning section and is therefore no longer a
> backfill strong."* Nothing applied yet — plan only, checked against live data throughout.

## 1. What the cluster-allocation session actually did — read in full, not assumed

Five documents, in order: the session log (reusable-method record), the obslog (full working
trail), the T2-likeness review, the low-tier review, plus the JSON deliverables' schema. Key facts
that bear directly on this triage, not covered in earlier re-evaluations:

- **T2's definition, as the researcher stated it for THIS work (obslog, verbatim):** *"the T2
  cluster is designed to allocate any strong that has not inner being relation. These strongs are
  all regarded as supplementing the strongs that have inner being significance. They must not be
  assigned to an inner being cluster."* **This is a clean, single boundary — no POS-split.**
  **Correction to my own earlier filter-re-triage review** (`filter-retriage-reevaluation-
  20260812.md`, §4): that doc flagged the old *main-project* T2 definition (`01c-T2-treatment-and-
  API-governance.md` — content/grammatical POS split) as a still-missing piece IBA's cluster model
  would need before T2 could be used as an exclusion signal. Having now read the actual IBA
  cluster-allocation instructions, **that concern doesn't apply here** — the researcher gave IBA's
  cluster work its own, simpler T2 definition, and that's the one governing `cluster_strong` today.
  01c was a different, now-closed study's rule; not binding on IBA.
- **T3 "Operations"** = human operation/movement not tied to one cluster; **not itself a exclusion
  signal** — it's a *content* bucket (IB-relevant, just not clean-mapped to one M-cluster). Confirms
  the user's framing: T3 counts as "allocatable to a cluster," T2 doesn't.
- **FLAG** = rare, IB-related but fits no cluster — also a content bucket, same as T3 for this
  purpose.
- **The method is fully reusable** (session log §4, an explicit numbered recipe) — HIGH tier
  (single-cluster gloss precedent) needs no researcher decision; MEDIUM and LOW need trend-spotting
  review passes, same shape as what was just run.
- **Real, named pitfalls to avoid on reuse** (session log §5): the cluster.csv FLAG gloss list is
  not a positive signal; TF-IDF profile scoring is too noisy to decide HIGH, sorting-aid only;
  transliteration-only matches collide on homographs; multi-cluster prior rows drop if keyed by a
  plain dict; substring keyword matching creates false positives (kill/fill, hissing/sin) — use
  token/stem matching with word boundaries; seat words (heart/soul/spirit/mind/flesh/conscience) →
  M47, never T2.
- **The T2-likeness review already flagged a live example this triage would directly resolve**:
  `G6507` (gloss "blindness" — the actual word this session already spent time on) sits in T2 today,
  explicitly flagged `⚠IB?` in that review as a candidate that "read as inner-being" but wasn't
  pulled (only 20 of 64 flagged items were). That's a `word`-origin code, not `backfill`, so it's
  out of this triage's direct scope — but it's a concrete, on-the-record instance of T2's boundary
  being imperfect at the edges, worth remembering when this plan runs its own MEDIUM/LOW review.

## 2. The rule, restated precisely

> A `strong` row currently `origin='backfill'` that carries **at least one `cluster_strong`
> assignment other than `T2`** (i.e. an M-code, `T3`, or `FLAG`) should be promoted: `origin`
> flips to `'word'`, and it should carry the same "full meaning section" a `word`-origin code
> carries — not just the meaning-only pull `raw.backfill_meaning_for()` gives it today.

## 3. Live sizing — checked against the DB, not estimated

| | total `backfill`-origin strongs | have ≥1 cluster row | of those, non-T2 (**promotable now**) | pure-T2-only (**stays backfill**) | **no cluster row at all** |
|---|---:|---:|---:|---:|---:|
| **backfill-origin** | 11,837 | 865 | **419** | 446 | **10,972 (92.7%)** |
| (word-origin, for scale) | 3,456 | 3,456 | 2,705 | 751 | 0 |

The 865-with-a-cluster-row figure exists only because `cluster_strong`'s original seed (BUILD.md
§103) ran against IBA's **full** `strong` table before the `origin` column existed or the
word-only rescoping (§104) happened — so a slice of `backfill`-origin codes got old-system-migration
cluster data "for free," never revisited since. The **419 non-T2 promotable-now** codes are a real,
immediately actionable set. The **10,972 with no cluster row** are the large majority and cannot be
triaged by this rule until they go through an allocation pass — this rule alone does not close that
gap, it only tells you what to do once a code IS classified.

## 4. What "full meaning section" concretely requires — traced through the code, not assumed

Checked the 419 promotable codes against every downstream table `word`-origin completeness depends
on (per the rows-5–7 plan reused directly):

- **`strong_verse`: 0/419.** By design — `raw.backfill_meaning_for()` is explicitly "meaning ONLY,
  no verses" (its own module header). This is the one real, structural gap.
- **`span` occurrences: 419/419 (100%).** Every one of these codes already appears in a `span` row
  — because the verse it occurs in was already pulled by some *other* word's book-scoped
  `raw.verses` run. The text is already in the DB; only the code→verse *assertion* is missing.
- **`strong_meaning_parsed` (exact-or-base): 411/419 (98%).** Matches the pattern already found for
  `blindness` — a handful resolve via base-fallback, consistent and low-risk.
- **`verse_lexical`: 419/419 (100%) already have ≥1 row.** `lexical.build` is book-scoped and
  origin-blind — it resolves every span in a processed book regardless of the underlying strong's
  origin. These codes are **already being read by the debate pipeline today**, under a `backfill`
  label that undersells how complete their data actually is.

**So "promotion" is cheaper than it sounds for these 419** — the real gap is narrow
(`strong_verse`), not the full raw-pull `receive`/`blindness` needed. But there's a real depth
question:

- **(a) Cheap backfill** — derive `strong_verse` rows from the `span` rows that already reference
  the code. Immediate, no STEP calls, zero new data. **Ceiling: only captures verses in books IBA
  has already pulled for some other word** — if the code occurs in an unpulled book, this misses it
  silently.
- **(b) Full pull** — run the equivalent of `raw.verses`/`verses_one()` (a real STEP `call3_strong`
  walk) for the code, matching genuine `word`-origin completeness — the code's *entire* Bible-wide
  occurrence set, not just the incidental subset already in the DB.

**(b) is what "no longer a backfill strong" reads as literally meaning** — `origin='word'` is
defined (§104) as carrying "the full raw-data-integrity chain." (a) would leave a code labelled
`word` while still only having partial verse coverage — a new, worse-than-`backfill` inconsistency
(mislabelled as complete). Flagging as a judgment call, not deciding here.

## 5. Open questions — need your direction before any of this runs

1. **Cheap backfill-from-span vs. full STEP re-pull** (§4 above) — which for the 419 now, and which
   as the standing rule going forward?
2. **Ownership.** `origin='word'` today is defined relative to a registry word's onboarding —
   `word_strong` links it to a specific study word. A code promoted by **cluster evidence alone**
   may belong to no `word_registry` entry at all. Does a cluster-promoted code need a home word (an
   M-cluster's own name, e.g.?), or can `origin='word'` exist validly with zero `word_strong` links,
   as its own new category?
3. **Does promotion feed the rows-5–7 gate directly?** These 419 (and any future promoted batch)
   would need to pass the same completeness checks under discussion for `raw-complete` — worth
   building this triage and that gate together rather than as two separate passes touching the same
   rows.
4. **The 10,972-code gap** — do you want an allocation pass run against them (reusing the exact
   method from the session log, at ~7× the original scale), staged/batched somehow (by `count`
   frequency? by book/passage relevance to what's actively being studied?), or left alone until a
   specific need surfaces? This is the large, real remaining work — the rule you gave applies to it
   only *after* classification exists, and nothing here proposes running that classification pass
   itself yet.
5. **T3/FLAG codes specifically** — same open question carried over from the filter-re-triage
   review: does `T3` membership alone justify promotion (a `T3` code's "cluster" is explicitly *not
   tied to a specific characteristic* — is that still "carries a full meaning section," or does it
   need a verse-level pairing first to mean anything)? The rule as given treats T3 the same as any
   M-code; flagging that T3's own definition ("context may pair the operation with a specific
   cluster") makes it a slightly different kind of "allocated" than a direct M-code hit.

## 6. Proposed phasing (not started)

- **Phase A** — the 419 non-T2 `backfill`-origin codes with existing cluster data: promote per
  whichever depth (§4) you choose; flip `origin`; re-verify `strong_meaning_parsed`/`strong_related`
  coverage; confirm `verse_lexical` freshness (should already be current, since nothing about the
  underlying span/verse changes — only the `strong_verse` assertion and `origin` flag are new).
- **Phase B** — the 10,972-code allocation pass, reusing the session log's own numbered recipe
  (§4 there) at scale — a major undertaking, likely wanting its own staged plan, not a single pass.
- **Phase C** — fold this triage's completeness requirements into the rows-5–7 / `raw-complete`
  redefinition work already in flight, so both gates share one mechanism rather than diverging.

Nothing above has been built or run. Answers to §5 determine exactly what Phase A writes.
