# G2128 — on-demand verse restatement, by single Strong's reference (sample)

> Redesign of the report from the whole-registry-word scope down to **one Strong's reference per
> run** — the smallest unit that still keeps volume manageable (§ `verse-lexical-by-registry-
> 20260810.md` showed even the median registry word carries 565 verses; a single Strong's code is
> orders of magnitude smaller). "Verse restatement" = the verse text unchanged, with only the span
> carrying **this exact code** annotated inline with its `strong_meaning_parsed` senses (the
> parse-meaning level), same inline style agreed for the registry-word version. Test case: **G2128**.

## First finding: the expected count (52) does not hold — real answer is 8, checked twice

You expected 52 verses, reading `strong.count` from `blessing-strong-span-v1-20260809.md`
("STEP total count: 52"). That field is **not** a verse-occurrence count. Checked two independent
ways, both agreeing exactly:

1. **Local DB** — `span` (and `verse_lexical`) each carry exactly **8** rows for
   `strong_variant='G2128'` (Mar 14:61, Luk 1:68, Rom 1:25, 2Cor 1:3, Eph 1:3, 1Pe 1:3, Rom 9:5,
   2Cor 11:31).
2. **Live STEP, this session** — `call3_strong("G2128")` (the actual verse-search call) returned
   `total: 8`, the same 8 references, fetched fresh — not a stale/incomplete local-onboarding
   artefact (the coverage caveat this app normally has to worry about, per
   `build_verse_span_meaning_extract.py`'s own note that `span`/`verse_lexical` are only as
   complete as what's been onboarded).

The 52 comes from a *different* STEP field — `call2_getInfo("G2128")` returns
`"count": 52, "freqList": "8;8;8;8;8;;8;8;8;8;8;8;2;8;;;;;8;8;8;8;8;8;8;11@8;45;40;8;41@40;8"` — a
STEP-internal aggregate that does not decode to 8 or to any obvious per-book verse tally I could
reconstruct in this session; it is **not** "how many verses this exact code occurs in." The
`-strong-span-` report's "STEP total count" label inherits this same field for every Strong's row
it shows — worth you knowing that label doesn't mean verse-occurrences anywhere in that report,
not just here. Not fixed in this session (out of scope for a report preview); flagging it as a
real labeling defect in the existing report, not just this one's expectation.

Proceeding on the real, twice-confirmed number: **8 verses**.

## Exact-variant senses for G2128 (all `strong_meaning_parsed` rows, this code only — no sibling/base collapse, since Q3 asked for span-specific senses, not the general variant set)

G2128 has no sibling sub-letter codes sharing its base, so every row below is unambiguously this
code's own:

- worthy of being praised, blessed, or commendedpraiseworthy *(general, `sort=0`)*
- worthy of praise *(`sort=1`)*
- blessing, blessed *(`sort=1`)*

## The 8 verses, restated — only the G2128 span annotated, rest of the verse untouched

### Mar 14:61

> But he remained silent and made no answer. Again the high priest asked him, "Are you the
> Christ, the Son of the **Blessed** [G2128, A-GSM: worthy of being praised, blessed, or
> commendedpraiseworthy; worthy of praise; blessing, blessed]?"

### Luk 1:68

> " **Blessed** [G2128, A-NSM: worthy of being praised, blessed, or commendedpraiseworthy; worthy
> of praise; blessing, blessed] be the Lord God of Israel, for he has visited and redeemed his
> people

### Rom 1:25

> because they exchanged the truth about God for a lie and worshiped and served the creature
> rather than the Creator, who is **blessed** [G2128, A-NSM: worthy of being praised, blessed, or
> commendedpraiseworthy; worthy of praise; blessing, blessed] forever! Amen.

### Rom 9:5

> To them belong the patriarchs, and from their race, according to the flesh, is the Christ, who
> is God over all, **blessed** [G2128, A-NSM: worthy of being praised, blessed, or
> commendedpraiseworthy; worthy of praise; blessing, blessed] forever. Amen.

### 2Cor 1:3

> **Blessed** [G2128, A-NSM: worthy of being praised, blessed, or commendedpraiseworthy; worthy of
> praise; blessing, blessed] be the God and Father of our Lord Jesus Christ, the Father of
> mercies and God of all comfort,

### 2Cor 11:31

> The God and Father of the Lord Jesus, he who is **blessed** [G2128, A-NSM: worthy of being
> praised, blessed, or commendedpraiseworthy; worthy of praise; blessing, blessed] forever, knows
> that I am not lying.

### Eph 1:3

> **Blessed** [G2128, A-NSM: worthy of being praised, blessed, or commendedpraiseworthy; worthy of
> praise; blessing, blessed] be the God and Father of our Lord Jesus Christ, who has blessed us in
> Christ with every spiritual blessing in the heavenly places,

### 1Pe 1:3

> **Blessed** [G2128, A-NSM: worthy of being praised, blessed, or commendedpraiseworthy; worthy of
> praise; blessing, blessed] be the God and Father of our Lord Jesus Christ! According to his
> great mercy, he has caused us to be born again to a living hope through the resurrection of
> Jesus Christ from the dead,

## How collision-safety (Q4) was actually handled here, and where it's still not solved generally

Checked for every one of the 8 verses: the matched surface string (`"Blessed"`/`"blessed"`,
exact case) occurs **exactly once** in that verse's text — confirmed by count, not assumed. So a
plain case-sensitive text search was safe here and nothing was silently dropped or misattributed.
That check is verse-specific luck, not a structural guarantee — e.g. Eph 1:3 itself contains
"Blessed" (this G2128 match), "blessed" (a *different* code, G2127), and "blessing" (G2129,
different word again); case-sensitivity happened to disambiguate all three here, but a Strong's
code whose surface form repeats verbatim (same case) elsewhere in the same verse — including a
*different* code that happens to render the same English word — would break plain text search.
**Not yet built**: position-exact substitution using `span.position` (or, doing this fully live,
STEP's own tagged HTML order from `parse_spans()`) instead of string search, which is what closes
this properly. Every verse in this 8-verse sample happens not to need it; the real report should
not depend on that being generally true.

## Addendum — where "STEP total count: 52" actually comes from (traced live)

Tested directly: called `call2_getInfo` for G2127 with the `{version}` parameter swapped across
nine values — `ESV_th` (our real configured module), `LXX`, `LXX_th`, `TAGNT`, `SBLGNT`, `NA28`,
`byz`, and even two **Hebrew-only** modules (`OSMHB`, `OHB`) that have no business returning
anything for a Greek code at all:

| version passed | count returned | gloss returned |
| --- | --- | --- |
| ESV_th | 334 | to praise/bless |
| LXX | 334 | to praise/bless |
| LXX_th | 334 | to praise/bless |
| TAGNT | 334 | to praise/bless |
| SBLGNT | 334 | to praise/bless |
| NA28 | 334 | to praise/bless |
| byz | 334 | to praise/bless |
| OSMHB | 334 | to praise/bless |
| OHB | 334 | to praise/bless |

Identical every time, including under Hebrew-only modules. That rules out "count is scoped to
whichever Bible module/version you pass" outright — the `{version}` slot in
`getInfo/{version}//{strong}//` is not actually consulted for this field. `count` (and the whole
`vocabInfos` entry — gloss, definitions, `relatedNos`) is a **fixed Strong's-dictionary reference
number**, read straight out of STEP's bundled lexicon data, entirely independent of any specific
Bible text or translation module. It is not computed by scanning a corpus at request time at all.

That also explains the earlier LXX/Philo citations noticed in G2128's `lsjDefs`
("LXX.Gen.9.26, +others, 1st c.AD: Philo Judaeus 1.453, NT.Luke.1.68, NT.Rom.1.25, etc.") — the
underlying lexicon entry these numbers are drawn from documents this word's use across Greek
literature broadly (LXX, Philo, NT), which is consistent with the dictionary-level count being
much larger than an NT-only tally: 42 is the standard NT occurrence count for G2127 (matches the
9 "Unique spans" rows in `blessing-strong-span-v1-20260809.md` summing to 42, and closely matches
live `call3_strong`'s 40), while 334 sits at roughly 8x that — plausible for "this lemma across
LXX + NT + other cited Greek literature" but **not confirmed exactly** — no LXX-specific module
was reachable locally to verify the arithmetic directly (the version-swap test above shows the
figure doesn't come from *any* queryable module in this STEP instance; it's baked into the
lexicon data itself, not derivable by querying a different corpus through this API).

**Conclusion for the report label:** "STEP total count" in `-strong-span-` reports is dictionary
metadata (a global, corpus-independent fact about the Strong's number), not a count of verses in
this app's Bible text. The right field for "how many verses does this exact code occur in, in our
data" is `call3_strong`'s `total` (or the local `span`/`verse_lexical` row count, which the live
check above confirmed agree) — a real, per-run defect in every `-strong-span-` report's labeling,
not just a one-off puzzle for G2128.

## Open items carried forward

1. **Report scope confirmed**: one Strong's reference per run, all its verses (whole Bible, not
   NT-only) — matches what you asked for here.
2. **Live STEP vs local DB**: this sample used local DB (`span`/`verse.text`) since it happened to
   fully agree with a live STEP recheck (8=8). A code with incomplete local onboarding would need
   the live STEP path (`call3_strong` + `parse_spans`) to actually reach every verse, not just the
   locally-onboarded subset — not yet decided which is the report's primary path vs. a
   cross-check.
3. **The mislabeled "STEP total count" field** in `blessing-strong-span-v1-20260809.md` (and every
   other `-strong-span-` report) — flagged, not fixed. Real per-code verse-occurrence counts
   need `call3_strong`'s `total`, not `strong.count`.
4. Position-exact substitution (previous paragraph) still needs building before this is safe on an
   arbitrary Strong's code, not just this collision-free 8-verse sample.

No code changes made yet — data preview only, built directly against `span`/`strong_meaning_
parsed` (local) and `call3_strong`/`call2_getInfo` (live STEP) for G2128.
