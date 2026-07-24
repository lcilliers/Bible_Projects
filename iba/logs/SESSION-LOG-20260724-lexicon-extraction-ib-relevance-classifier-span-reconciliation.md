# Session log — 2026-07-24 — lexicon term extraction, IB-relevance classifier, span/term-list reconciliation (CLOSED)

**Session closed 2026-07-24 — the next session starts fresh, with no memory of this conversation.**
This log is written as a cold-start entry point: read it first, then follow its pointers.

---

## What this session did, start to finish

The session opened by running `Start-Iba.ps1` and reading the prior session's own closing log
(`SESSION-LOG-20260723-orphan-check-fix-candidate-retraction-escalation-closeout.md`), which had
just retracted the whole candidate system as "a substantial mess-up" and left the candidate/passage
redesign explicitly unstarted, deferred to "whenever the researcher defines it." This session did
**not** touch the candidate system directly. Instead, working from three existing raw lexicon
extract scripts (`build_mounce_lexicon_extract.py`, `build_lsj_sense_extract.py`,
`build_meaning_tree_extract.py` — already present but uncommitted from an earlier, unlogged session),
the researcher walked through a genuinely new, ground-up exploration: **can Inner-Being relevance be
judged from a term's own meaning, independent of any existing registry or Strong's-number lookup?**
That question, and the tooling built to test it, is the substance of this session.

### 1. Extract normalization — row_type + gloss-splitting (all three lexicon scripts)

- Added a `row_type` column to `build_lsj_sense_extract.py` and `build_meaning_tree_extract.py`,
  matching `build_mounce_lexicon_extract.py`'s existing pattern, then unified the label to
  **"lookup"** across all three (was "english gloss" for the first two — renamed once the researcher
  pointed out the inconsistency).
- All three gloss/sense columns were still bundling multiple comma/semicolon-delimited terms into
  one string; factored the bracket-aware split logic Mounce already had into a new shared module,
  **`lexicon_split_common.py`** (`split_multi_gloss`, `classify_row`, `strip_bracketed`,
  `bracket_aware_split`), and applied it to LSJ and meaning-tree too. Verified the Mounce refactor
  produced byte-identical output before/after.
- Fixed a real LSJ parsing bug found along the way: a sub-sense nested under the (usually implicit)
  first "I" carries a bare numeric label in the source HTML ("2" instead of "I.2"), unlike a
  sub-sense under a later, explicitly-tagged top level ("II.2") — composed the missing prefix from
  the nearest preceding top-level Roman numeral (3,856 of 25,775 LSJ rows / 662 strongs affected).
  This directly explained a "duplicate" the researcher spotted (G0026's sense "I" and unlabeled
  sub-sense "2" both glossing "love" — genuinely different senses, not a parsing artifact).
- Built **`build_lexicon_lookup_extract.py`**: combines the `row_type == "lookup"` rows from all
  three sources into one flat (strong, term, source) CSV, with its own further filtering (blank
  terms, stray Greek-script cross-references leaking into English glosses) and de-duplication of
  exact repeats within one source. Final: 40,039 rows.

**Artifacts**: `outputs/csv/mounce-lexicon-parsed-iba-20260723.csv`,
`lsj-sense-parsed-iba-20260723.csv`, `strong-meaning-tree-parsed-iba-20260723.csv`,
`lexicon-lookup-terms-iba-20260724.csv`.

### 2. The "sense engine" — `ib_relevance_classifier.py`

The researcher's framing, stated explicitly and worth preserving verbatim in spirit: *this is not a
lookup against the registry or Strong's number — that's fundamentally the wrong method. It is asking,
of the term's own meaning alone, whether it relates in some way to the inner being. Most cases are a
"no-brainer," and that majority should be resolved for free, without incurring API/LLM cost.*

Built as a local, wordlist-based, three-way classifier — **IB related / Not relevant / Could impact
IB** (deliberately the default/fallback bucket: a wrong confident call is worse than an honest "not
sure"). No DB lookups, no context, no verse disambiguation (explicitly deferred as "the next phase").

This went through many honest rounds of the researcher finding real gaps by inspecting actual output,
not by inspecting the code:
- First pass: 84% landed in "Could impact IB" — far short of the "80% obvious" expectation. Traced to
  the dataset's true nature: this is the *entire* Bible lexicon (~3,463 strongs), not a pre-filtered
  inner-life set, so most glosses are ordinary vocabulary a wordlist can't sort confidently. Added a
  batch of missing obvious IB words (praise, pure, true, understand, counsel, curse, British spelling
  variants) — modest gain (84% → 82.3%).
- Researcher: "you're pumping everything undecided into Could-impact, that's nonsense" → inspected the
  actual bucket contents (not assumed) and found it was mostly stopword-adjacent filler the wordlists
  never covered: light verbs (come/go/take/give), prepositions (before/among/without/against),
  quantifiers (nothing/anyone/whoever), generic nouns (man/place/time/day). Added ~150 words across
  new `GENERIC_VERB_WORDS`/`GENERIC_NOUN_WORDS`/`GENERIC_ADJECTIVE_WORDS`/`QUANTIFIER_INDEFINITE_WORDS`
  categories and expanded `STOPWORDS`.
- "H3967 numbers as IB relevant????" → confirmed numerals were landing in "Could impact IB" (not
  actually "IB related", but still nonsensical to leave undecided) — root cause: pure-digit tokens
  had no letters so weren't being filtered as junk. Added the fix plus `UNIT_OF_MEASURE_WORDS`
  (cubits, shekels, hundredfold, percentage — all still slipping through despite being number-like).
- "Large percentage of transliterations" → investigated two ways (curated known-transliteration list,
  and an empirical check against the DB's own `strong.stepTransliteration` column) — found only a
  handful of genuine hits either way, NOT a large percentage. Asked for concrete examples rather than
  keep guessing with unreliable heuristics (a suffix-pattern heuristic tried first was actively wrong,
  mostly catching ordinary English words like "destruction"/"excel").
- Researcher supplied screenshots: turned out to be **proper names** (Abaddon, Abagtha, Abdeel,
  Abel-beth-maacah, ...), not transliterations in the logos/agape sense — the Bible has thousands of
  minor genealogical/place names the original ~75-name list never covered. Fixed three ways: (a) a
  Unicode curly-apostrophe normalization bug (STEP renders possessives as "aaron’s" with U+2019,
  which several viewers mis-render as mojibake — wasn't being stripped, so possessive forms of
  covered names fell through uncertain); (b) a structural rule for compound place names (3+ hyphen
  segments, or a hyphenated term starting with a known Hebrew place-name element like "abel-"/"beth-"/
  "kiriath-"); (c) ~400 more names added to `PROPER_NAME_WORDS` from direct knowledge, not exhaustive.

Net effect on the **span-side** exception list (see §3) across the whole session: "Could impact IB"
84.0% → 57.3% before the reconciliation-level fixes in §3 took it further.

**Artifact**: `iba/app/tools/ib_relevance_classifier.py`. **Value going forward**: real, but bounded —
it is explicitly a coverage heuristic sized to clear the obvious majority for a one-time triage pass,
not a maintained linguistic model. Its wordlists are English-only and word/phrase-level; it has no
notion of a Strong's number's *dominant* meaning (see §3's `H3068G` finding) and will keep producing
occasional false positives/negatives on rare, idiomatic, or borrowed-surface-text rows. Re-running it
after any of the source lexicon extracts change is cheap (pure Python, no network); extending its
wordlists further is possible but hit diminishing returns quickly, per the researcher's own read of
where this needed to stop (see §5).

### 3. Span/term-list reconciliation — `build_span_term_reconciliation.py`

Reconciles the combined lookup-term list against `span` (every actual word occurrence in the loaded
Bible text), joined on STRONG ALONE per the researcher's explicit correction (word-level mismatches
are not gaps — a lexicon synonym never chosen by this translation, or a real rendering our lexicon
tables haven't loaded a gloss for yet, are both expected, not errors). Two directions:

- **`span-words-missing-from-term-list-iba-20260724.csv`** — Strong's numbers with real text
  occurrences but zero lexicon coverage (a possible "missing term" signal).
- **`term-list-words-missing-from-span-iba-20260724.csv`** — lexicon-covered Strong's numbers that
  never occur in the loaded text at all (a possible "missing verse" signal). Checked directly against
  STEP for all 240 such strongs (a separate one-off, `_check_missing_strongs_in_step.py`): **all 240
  (100%) have zero verses in STEP itself** — not a `span`-loading gap, STEP's own ESV_th module simply
  never tags any verse with these. Nine of the 240 had unusual 5-digit codes initially flagged as
  possibly malformed; investigated via STEP's own gloss-lookup and confirmed they're legitimate
  STEPBible Extended Strong's Numbers, not corrupted data (written up separately, see §4).

The span-side file went through a second, structural round of cleanup once the researcher spotted
`H0853` (the Hebrew direct-object marker "et") showing up attached to dozens of unrelated words
("spirit", "evil", "wisdom", ...) as if it meant something — it doesn't; a grammatical marker's
`surface` text in `span` is borrowed from whatever adjacent content word STEP's tagging attached to
that position. `is_particle` didn't catch it (that flag only covers the `H9xxx`/`G9xxx` extended-
particle range). Investigated systematically (queried `span` for the strongs with the most DISTINCT
surface words attached — a real content word has bounded synonym variety; H0853 alone had 2,111) and
built `FUNCTION_WORD_STRONGS`, a hand-verified set of ~61 Hebrew/Greek function words (direct-object
marker, copula "to be", prepositions, conjunctions, pronouns, demonstratives, interrogatives,
particles, numeral "carriers") now excluded from the whole reconciliation. A follow-up researcher
spot-check on `H4069` (maddua, "why") found more of the same pattern at smaller scale (rarer overall,
so missed by the original top-80-by-distinct-word cutoff) — added 12 more interrogative particles
after individually confirming each against `span` directly.

Even after that, the researcher found further residual noise checking STEP verse-coverage for the
"IB related" rows (see below): `H3068G` (the divine name, YHWH) tagged "IB related" from a single
stray occurrence of "peace"; `G3778` ("this") from "purpose"; `G1909` ("upon") from "believe" — the
same borrowed-surface-text artifact, just now showing up among CONTENT strongs rather than pure
function words, at the individual-word level rather than the whole-strong level. This was surfaced,
explained, and **left as a known, open limitation** rather than patched further (see §5) — the
researcher's own conclusion was that the right fix is a change in method, not another wordlist
expansion.

**Preliminary STEP assessment** (`_check_ib_related_span_step_coverage.py`, at the researcher's
request): of 235 distinct strongs behind the 281 "IB related" span rows, 174 (74%) are already fully
covered locally; the remaining 61 have a combined gap of only 460 verses against STEP's totals — a
small, scattered gap, not a large missing block. (First version of this script had a real bug —
compared STEP's per-exact-variant total against a base-form-aggregated local count, producing a
nonsensical negative total gap; fixed by matching on the exact `strong_variant` on both sides,
confirmed against `H3068` directly before trusting it.)

**Artifacts**: `build_span_term_reconciliation.py`, `_check_missing_strongs_in_step.py`,
`_check_ib_related_span_step_coverage.py`, plus their output CSVs (`span-words-missing-from-term-
list-iba-20260724.csv`, `term-list-words-missing-from-span-iba-20260724.csv`, `missing-strongs-step-
verse-check-iba-20260724.csv`, `ib-related-span-step-coverage-iba-20260724.csv`) and one ad-hoc pull
(`span-h0853-iba-20260724.csv`, all 10,184 raw span rows for H0853, requested directly).

### 4. Malformed-strong-codes investigation

Separate written finding: `iba/app/reports/malformed-strong-codes-investigation-20260724.md`. Nine
5-digit Strong's codes (`G20125`, `G21422`, etc.) initially flagged as possibly corrupted turned out
to be legitimate STEPBible Extended Strong's Numbers, confirmed via STEP's own gloss-to-code lookup
returning the exact same codes back. Flagged for later: any future "well-formed Strong's number"
validation in this project should allow the 5-digit extended form, not just the standard 4-digit one.

---

## The conclusion this session reached

The researcher's own summary, which frames what should and shouldn't continue from here: **coverage
of real inner-being content by the strongs already in the system is high** (74% of a spot-checked
235-strong sample fully covered; the term-list/span verse-gap for genuinely lexicon-covered strongs
is small and scattered, not systemic). Given that, **and** given that essentially every remaining
classification error traced back to the same root cause — a word-level classifier judging a
`(strong, word)` pair with no sense of the verse or the strong's dominant meaning around it — the
conclusion is that **pre-classifying word/span meaning as IB-relevant is the wrong level to keep
investing in**. The study is moving toward analysing **individual spans or individual characteristics
directly** — reading what a verse actually says about the inner being and letting that evidence
speak, rather than continuing to sort terms into a grid ahead of time. This mirrors the main Bible
study programme's own 2026-06-25 "Characteristics → Movements" reset (move away from pre-classifying/
naming individual characteristics, toward reading verses for what they do and letting patterns
emerge) — the same shift, one level down, for IBA's own term/span layer.

**What this means for the tooling built this session, concretely:**
- The three lexicon extract scripts + `lexicon_split_common.py` remain straightforwardly useful:
  they're a real, reusable normalization of raw lexicon HTML into clean, split, classified rows, and
  nothing about the method-pivot invalidates that layer.
- `ib_relevance_classifier.py` and `build_lexicon_lookup_extract.py`/`build_span_term_reconciliation.py`
  did their job as a **one-time triage pass** — they answered "is coverage good enough to stop
  worrying about it" (yes, ~74%+) and located the genuinely small gap worth a look. They are not
  positioned to be the ongoing method; further investment in the wordlists would keep hitting the
  same word-level ceiling regardless of size.
- `_check_missing_strongs_in_step.py` and `_check_ib_related_span_step_coverage.py` are generic,
  reusable STEP-coverage-checking patterns (govered-client usage, read-only) that could be repointed
  at a different input list if a similar question comes up later.
- The `FUNCTION_WORD_STRONGS` list inside `build_span_term_reconciliation.py` is a genuinely durable,
  hand-verified finding (Hebrew/Greek grammar doesn't change) independent of the method pivot — worth
  keeping even if the reconciliation script itself isn't run again soon.

---

## Where to start a fresh session

1. **Read this log**, then decide with the researcher what "understanding what a verse says about
   the inner being" looks like concretely for the IBA app — what gets read/recorded per span or per
   characteristic. That definition work had not started as of this log.
2. The candidate/passage system redesign (deferred at the end of the 2026-07-23 session) is **still**
   untouched and still open — this session did not revisit it, and the pivot toward span/verse-level
   analysis may now be directly relevant context for how that redesign should be shaped.
3. `git status` — this session's work (see file list in the commit that follows this log) plus
   several unrelated pre-existing untracked items from prior sessions (a session-log folder move, an
   "AI failures" research thread) that this session deliberately left untouched, not its own work to
   commit or resolve.
