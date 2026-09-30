# Verse-Lexical Visibility Report — 2026-09-05

> First real look at the `verse_lexical`/`verse_lexical_note` corpus (built escalation #1383,
> 2026-09-04) plus today's cluster reallocation work (T4–T9). Everything below is queried live
> against `iba.db`, not summarised from memory.

## Correction first, before anything else

Earlier in this session I reported **975,451 rows** as the live corpus size. That was wrong — I
queried `verse_lexical` without filtering `deleted=0`, so it included every superseded/re-processed
row still on file for history (the project's standard soft-delete convention — `deleted=1`, no
physical deletes). Spot-checked one such pair directly: an August 9 row and an August 12 row for
the same span, the older one correctly flagged `deleted=1`, not a duplication bug — the newer row
added the Layer-1 mechanical columns (`position`/`surface`/`language`/`testament`/
`gloss_consistent_in_verse`) the older one predates. No data-integrity problem; my count was just
wrong. Live rows (`deleted=0`) exactly equal distinct `(verse_id, span_id, code_ordinal, strong,
position)` combinations — zero duplication once filtered correctly.

## Headline numbers (live rows only)

| Metric | Value |
|---|---|
| `verse_lexical` rows, live | **544,572** (975,451 on file incl. 430,879 superseded) |
| Verses covered | 29,754 of 29,759 in the corpus (99.98%) |
| `role = content` | 363,253 |
| `role = function` | 181,319 |
| `is_negator = 1` | 8,527 |
| `party_kind = divine` | 12,789 (the only party_kind populated before today — human/angelic/adversarial were 0 until this session's cluster work, which lives in `cluster_strong`, not this column; see below) |
| `verse_lexical_note` (Layer 2 relational — chain/entity_link/connective/verb_argument/etc.) | **0 live rows** — schema built, never run against real content, only a throwaway test fixture (John 1:1–5, created and deleted, escalation #1450) |

## Two real verses, in full, so you can eyeball the actual output

**Daniel 1:8** (25 tokens, matches the verse's real word count exactly):

| strong | morph | role | surface | flag |
|---|---|---|---|---|
| H1840G | HNpm | content | Daniel | |
| H7760A | HVqw3ms | content | resolved | |
| H5921A | HR | content | resolved | |
| H3820A | HNcmsc | content | resolved | |
| H0834A | HTr | content | that | |
| H9023 | HSp3ms | function | that | |
| H3808 | HTn | content | not | **is_negator** |
| H1351 | HVti3ms | content | defile | |
| H4428G | HNcmsa | content | king's | |
| H9009 | HTd | function | king's | |
| H6598 | HNcmsc | content | food | |
| H9003 | HR | function | food | |
| H3196 | HNcmsc | content | wine | |
| H9002 | HC | function | wine | |
| H9003 | HR | function | wine | |
| H4960 | HNcmsc | content | drank | |
| H1245 | HVpw3ms | content | asked | |
| H9023 | HSp3ms | function | asked | |
| H8269 | HNcmsc | content | chief | |
| H9006 | HR | function | chief | |
| H5631 | HNcmpa | content | eunuchs | |
| H9009 | HTd | function | eunuchs | |
| H0834A | HTr | content | allow | |
| H3808 | HTn | content | not | **is_negator** |
| H1351 | HVti3ms | content | defile himself | |

Note the `content`/`function` split on Hebrew words carrying an attached prefix (e.g. `H4428G`
king's + `H9009` the-[definite article], both from one Hebrew word) — that's the design, not a
duplicate.

**John 3:16** (21 tokens):

| strong | morph | role | surface | flag |
|---|---|---|---|---|
| G1063 | CONJ | function | For | |
| G2316 | N-NSM-T | content | God | **party_kind=divine** |
| G3779 | ADV | content | so | |
| G0025 | V-AAI-3S | content | loved | |
| G2889 | N-ASM | content | world | |
| G5620 | CONJ | function | that | |
| G1325 | V-AAI-3S | content | gave | |
| G0846 | P-GSM | content | his | |
| G3439 | A-ASM | content | only | |
| G5207 | N-ASM | content | Son | |
| G2443 | CONJ | function | that | |
| G3956 | A-NSM | content | whoever | |
| G4100 | V-PAP-NSM | content | believes | |
| G1519 | PREP | function | in | |
| G0846 | P-ASM | content | him | |
| G3361 | PRT-N | function | not | **is_negator** |
| G0622 | V-2AMS-3S | content | perish | |
| G0235 | CONJ | function | but | |
| G2192 | V-PAS-3S | content | have | |
| G0166 | A-ASF | content | eternal | |
| G2222 | N-ASF | content | life | |

Both read cleanly, one row per real word, correct flags on "God" and "not" — the mechanical layer
looks sound on inspection, for whatever two verses' worth of confidence that's worth.

## Today's cluster work (T4–T9), full membership — for your review of #1499/#1500's actual output

| Cluster | Meaning | Codes |
|---|---|---|
| **T4** Adversarial | Satan/the Devil | H7854 (satan), G4567 (satanas), G1228G (diabolos) |
| **T5** Negator | negation particles | H0408, H3808, H3809, G3756, G3361, G3760, G3761 |
| **T6** Connective | clause-linking (kept as one bucket, not split by causal/coordinating/purpose) | H3588A, G1063, H9002, G2532, G1161, G2443 |
| **T7** Party-Divine | God/the LORD/Christ/Jesus | H0430G, H0410G, H0410L, H0410K, H3068G, G2316, G5547, G2424 |
| **T8** Party-Human | man/woman/mankind/human | H0120G, H0376G, H0802, H0582, G0444, G0435G, G1135, G0442 |
| **T9** Party-Angelic | messenger/angel | H4397G, H4397H, H4398, G0032G, G0032H |

## What this means for #1501 (the rewire) and your "million records" concern

You asked to see this before deciding on the backfill. Two things worth weighing, now that you can
see the real shape of the data:

1. **`is_negator`/`party_kind` are stored, backfilled columns on `verse_lexical`** — computed once
   at build time from whatever lexicon existed then. Rewiring the *source* (cfg_lexical_code_class
   → cluster_strong) without re-running the backfill means these two columns go stale relative to
   T4–T9's new content (e.g. no row will show `party_kind=human` or `party_kind=non_human` until a
   re-backfill runs, even though T7/T8/T9 now have real content).
2. Given `verse_lexical_note` — the layer that would actually need re-running most often as new
   `note_type`s/classes get added — is still at **0 rows corpus-wide**, there's a real argument for
   *not* treating "backfill the whole 544k-row column" as the default response to every future
   cluster change, exactly your instinct. A join-at-read-time against `cluster_strong` (computing
   `party_kind` live rather than storing it) would make every future T-code addition free instead
   of a corpus rewrite — a real design option worth putting on the table for #1501's actual code
   change, not decided here.

Not started: the backfill itself, per your explicit hold.
