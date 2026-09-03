# Lexical inner-being reading checklist — v1

> Escalation #1378/#1379. Extracted from the Dan 1:8 worked example
> ([`1379-lexical-to-finding-worked-example-v1-20260901.md`](1379-lexical-to-finding-worked-example-v1-20260901.md)) —
> every item below corresponds to a real miss-and-correction in that session, not an invented step.
> This is a checklist candidate, not yet adopted as a governed procedure.

## The checklist

| # | Test | What it catches | First evidenced by |
|---|---|---|---|
| 1 | **Enumerate every live row** — no pre-filtering by role or gloss before the tests below run | Prevents cherry-picking the terms that already look IB-shaped | The `H1245`/"asked" and `king`/`chief`/`eunuchs` misses — both skipped because the pass wasn't exhaustive |
| 2 | **Genre/mode, recorded explicitly per verse** (prose / narrative / poetic / declarative / other) | Determines which of tests 4–9 even apply, and how | `bible_research.db`'s `verse.genre` — real prior art, not ported to `iba.db`, and found too coarse (book-level) on Dan 1:8's own tag |
| 3 | **Language/testament, recorded explicitly per row** (not inferred from the H/G prefix) | Determines which implementation of test 9 applies | `strong.language` exists but only at term level, not on `verse_lexical`/`span` |
| 4 | **Declared-vocabulary test** — does the row's own gloss carry inner-being vocabulary directly? | The baseline test — catches the obvious cases | `H3820A` (heart) |
| 5 | **Idiom/combined-span test** — is this row part of a multi-code span whose surface gloss diverges from a literal per-code reading? | Catches inner-being content with no surface English word at all | "resolved" hiding `H3820A` inside a 3-code combined span |
| 6 | **Outward-enactment test** — does the row's gloss carry a volitional/appetitive sense even where its contextual sense looks like plain action? | Catches IB content expressed through a *second* verb, not just the first | `H1245` "asked" (gloss includes "desire, demand") — missed on the first pass |
| 7 | **Relational test** — does the row name or imply another party, tested against the programme's own "relates" dimension, not against vocabulary? | Catches IB content carried by *what relation a term establishes*, never by vocabulary | `king`/`chief`/`eunuchs` — dismissed as "context" until tested against the five-part definition directly |
| 8 | **Polarity test** — is the row a negation/modifier attached to a declared or structural operation? | Catches type-determining modifiers with no gloss of their own to screen on | `H3808` "not" — invisible to every vocabulary-based test by construction |
| 9 | **Sequencing/chain test** (testament-branching) — does the row's morphology carry a narrative-sequencing marker linking it to another operation? | Surfaces the primary-operation/chain structure and the verse's entry point | Hebrew: waw-consecutive (`HVqw3ms`/`HVpw3ms`) linking resolve→ask. Greek needs its own version — not yet built |
| 10 | **Related-term/lemma test** — for declared-vocabulary rows, pull `strong_related`, then sort each entry by checking `strong_meaning_tree.lemma_key` | Distinguishes real semantic relatives from coincidental root-sharing | Heart↔"encourage"↔"bake" (real, shared lemma) vs. the `lemma_key` test's own control-case failure (defile/defilement have *different* lemma_keys despite being the same root) — **this test's own reliability is still open, not settled** |
| 11 | **Primary-operation/theme test** — of all chain-linked operations, which has nothing upstream of it? | Answers the entry-point problem: which term should a corpus process record as the verse's theme | `resolve`, not `ask` or `defile`, in Dan 1:8 — evidenced by test 9's sequencing data |
| 12 | **Inert check** — confirm explicitly that a row contributes nothing beyond grammar | Keeps the process from manufacturing content out of function words | Articles, conjunctions, bare prepositions in Dan 1:8 |

**Two governing rules, not per-row tests:**
- Every row's result is recorded as a **structured field**, never prose-only and never ranked by
  assumed importance — declared vs. structural is a difference in what Phase 1 can assert, not in
  what matters.
- **Two distinct flag types**, kept separately labelled from the point they're raised: a
  **data-quality flag** (e.g. the same Strong's+morph pair glossed two different ways in one verse)
  and a **discovery flag** (a backdrop/disposition hypothesis the verse's own data can't settle,
  awaiting cross-verse evidence). Conflating them risks routing both to the same downstream process
  when they need different ones.

## Catalogue questions each test touches

Cross-checked against the 16-question **Word/term (lexical)** Scope-focus bucket
([`1007-tier-catalogue-scope-focus-v3-20260831.md`](1007-tier-catalogue-scope-focus-v3-20260831.md)), full
text, obs_id from [`1007-word-term-lexical-source-v1-20260831.md`](1007-word-term-lexical-source-v1-20260831.md).
Other buckets (Characteristic behaviour/relational, Verse-context) are plausibly touched by tests
7, 9 and 11 as well — noted below, not cross-checked question-by-question in this pass.

| Test | Catalogue question(s) touched | obs_id |
|---|---|---|
| 4 (declared-vocab) | T1.1.2 "What do the primary Hebrew and Greek terms show at the definitional level?"; T7.1.1 "What are the primary terms...and what do their root meanings show?" | 237, 393 |
| 5 (idiom/combined-span) | T7.1.2 "What is the grammatical range of the primary term...and what does that range show about how the characteristic operates?" | 394 |
| 6 (outward-enactment) | T7.1.7 "Does the vocabulary include a supplication or seeking term...?" — directly, `H1245`'s own sense is exactly this pattern | 399 |
| 7 (relational) | T1.1.3 "What directional, relational, or constitutional implication does the name carry?" (flagged in this session for possible re-bucketing to a new "Characteristic — what it is") | 238 |
| 8 (polarity) | No direct match in the 16 — none of the lexical-bucket questions ask about negation/modification. Worth naming as a gap in the catalogue itself, not just an oversight in this mapping. | — |
| 9 (sequencing/chain) | T7.1.2 (grammatical range → operation) again; also plausibly Verse-context bucket questions (single-verse empirical readings) — not cross-checked here | 394 |
| 10 (related-term/lemma) | T6.4.1 "Which vocabulary terms does this characteristic share with other characteristics?"; T6.4.2 "Does the sharing extend to root-level architecture?"; T6.4.3 "What does the vocabulary sharing show about the conceptual relationship?"; T7.1.3 "semantic range"; T7.1.4 "distinguishing distinct aspects"; T7.1.5 "structural opposite or absence" (directly — redeem/defile is exactly this); T7.1.10 "full vocabulary arc" | 379, 380, 381, 395, 396, 397, 402 |
| 11 (primary-operation/theme) | No question in the 16-item lexical bucket asks this directly — it's a corpus-navigation/indexing concern, closer to how a term-driven process should *use* the catalogue than a question the catalogue itself poses. Worth naming as a second catalogue gap. | — |
| 3 (language/testament) | T7.1.8 "What does the relationship between OT Hebrew and NT Greek vocabulary show about continuity or development across the Testaments?" | 400 |
| — (not touched today) | T7.1.6 "person-type term"; T7.1.9 "newly coined NT term" — no Greek example run this session | 398, 401 |

**Two gaps the mapping itself surfaces:** polarity (test 8) and the primary-operation/theme
question (test 11) have no home in the current 16-question lexical bucket at all — not because
they're unimportant (both did real work in the worked example), but because the catalogue's
questions were never framed to ask for them. Worth carrying into whatever comes out of #1007's
closing conclusion (structural catalogue deficiency), not treated as this checklist's own oversight.
