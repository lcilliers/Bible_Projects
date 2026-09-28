# M47 (Inner Seat) — Surface-Form Listing, 2026-09-27

## Request

Run the researcher's ad-hoc query (`scripts/SQLite/IBA_DB/explore clusters-2.sqlite3-query`,
lines 27-55) listing every M47 ("Inner Seat" — heart/soul/spirit/inward-parts) Strong's code with
its actual English surface form and verse reference.

## Bug found and fixed (escalation #1879, resolved)

The query as written joined `span` to `strong` by plain equality:
`left join span on strong.strongNumber = span.strong_variant`. `span.strong_variant` holds a
space-delimited list of codes when STEP combines more than one onto a single HTML tag (e.g. a
fused preposition+noun), so the equality join only ever matched a span holding *exactly* one code
— any M47 word fused into a multi-code tag was invisible.

Measured against `verse_lexical` (the DB's own correct, pre-exploded one-row-per-code table) this
was not a fringe edge case — it was dropping roughly half the cluster's core vocabulary:

| Strong's | Gloss | Shown (buggy) | Actual (verse_lexical) | Missing |
|---|---|---|---|---|
| H3820A | heart | 326 | 594 | 45% |
| H1320 | flesh | 123 | 270 | 54% |
| H7307G | spirit | 88 | 216 | 59% |
| H5315H | soul: life | 86 | 207 | 58% |
| H3824 | heart | 132 | 252 | 48% |
| H5315G | soul | 162 | 246 | 34% |

Fixed in place: the query now joins through `verse_lexical` (`vl.strong = strong.strongNumber`,
then `span` via `vl.span_id`, `verse` via `vl.verse_id`), matching the pattern the researcher had
already applied to two other queries earlier in the same file. Total row count went from 1,992 to
the correct **3,175**. Grepped `iba/app/**/*.py` for the same equality pattern — none found, so no
production code was affected, only this scratch query.

## Full corrected result set

3,175 rows exported to
[`cluster-M47-surface-forms-20260927.csv`](cluster-M47-surface-forms-20260927.csv) (columns:
cluster_code, short_name, description, strongNumber, stepGloss, surface, reference, text).

## Per-Strong's-code summary (occurrence count + observed surface forms)

| Strong's | Occurrences | Gloss | Sample surface forms |
|---|---|---|---|
| H3820A | 594 | heart | Hearts, Laban, able, accord, attention, breast, brokenhearted, care... |
| G4151G | 374 | spirit/breath: spirit | Spirit, breath, spirit, spirits |
| H1320 | 270 | flesh | Flesh, and, blood, body, creature, flesh, lead, like those... |
| H3824 | 252 | heart | Consider, anger, breasts, brokenhearted, consider, encouragingly, fainthearted, heart... |
| H5315G | 246 | soul | distress, enraged, grieved, he, heart, heart's, heart's desire, inwardly... |
| H7307G | 216 | spirit | Spirit, living creatures, made life, mind, no, spirit, spirit in, spirits... |
| H5315H | 207 | soul: life | alive, and your, breath, deadly, delivered my life, fatally, forfeit, human beings... |
| G2588 | 156 | heart | enraged, heart, hearts, heart's, himself, minds, purpose |
| G4561 | 146 | flesh | another, anyone, bodies, bodily, body, condition, desire, earthly... |
| H7307H | 145 | spirit: breath | air, blast, breath, cool, wind, winds, windy |
| H5315I | 130 | soul: myself | I, We, Whoever, accusers, among them, and, and they, away... |
| H5315J | 96 | soul: person | (various, incl. some noisy/mis-tokenized entries — see CSV) |
| G5590G | 49 | soul | Soul, being, fainthearted, he, heart, heartily, living, me... |
| H5315L | 47 | soul: appetite | appetite, counts, crave, craved, craving, desire, desires, greed |
| G5590H | 40 | soul: life | life, lives, selves |
| G4893 | 30 | conscience | conscience, consciences, consciousness, mindful |
| G4152 | 26 | spiritual | spiritual, spiritual blessings, spiritual gifts, spiritual things, spiritual truths |
| H2436G | 20 | bosom: embrace | arms, bosom, breast, chest, embrace, embraces, heart, lap |
| H7607 | 16 | flesh | body, close, flesh, food, himself, kinsman, kinsmen, meat |
| H5315K | 13 | soul: animal | creature, creatures, living creature |
| H5315M | 13 | soul: dead | bodies, body, dead, dead body |
| H7308 | 11 | spirit | spirit, wind, winds |
| H7307J | 10 | spirit: temper | Has the, I, anger, self-control, spirit, temper |
| G5590J | 8 | soul: person | human being, person, persons, soul, souls |
| G2293 | 7 | take heart | courage, heart |
| H3825 | 7 | heart | heart, mind |
| H3826 | 7 | heart | heart, hearts |
| H7307I | 7 | spirit: side | side, sides |
| G1573 | 6 | to lose heart | grow weary, lose heart |
| G5590I | 6 | soul: myself | soul, us |
| G4151H | 5 | spirit/breath: breath | Spirit, breath, wind, winds |
| G4641 | 4 | hardness of heart | hardness, heart |
| H1321 | 3 | flesh | flesh |
| G2589 | 2 | heart-knower | heart, hearts |
| G3050 | 2 | spiritual | spiritual, spiritual worship |
| H5315N | 2 | soul: neck | neck |
| H3821 | 1 | heart | heart |
| H7907 | 1 | heart | mind |

Note: `H5315J`'s surface-form sample includes what look like OCR/parse noise ("000", "32") — not
investigated further here since it wasn't the object of this request; flagging in case it's worth
a separate look at that Strong's code's span data specifically.

## Note on scope (not fixed here)

Two earlier queries in the same file (lines 3-25 and originally a first-pass "thought verses"
query) still use the same `strongNumber = strong_variant` equality pattern in places for
gloss/cluster lookups. Not touched this pass since they weren't what was asked for — flagged for
awareness if you go back to those.
