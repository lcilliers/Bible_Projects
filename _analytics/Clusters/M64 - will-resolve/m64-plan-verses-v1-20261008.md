# M64 "plan" set: verse pull (v1, 2026-10-08)

**Escalation:** #1986 (the will set, extended) · **Status:** data pull only, no reading

Researcher, verbatim: *"continue with 1986. add the this extract the verses around plan, planning, count and other terms directly related"*.

- **CSV:** [`m64-plan-verses-v1-20261008.csv`](m64-plan-verses-v1-20261008.csv). It has one row per verse, in canonical order, with the same columns as the will set: reference, hits, hit_words (Strong's, ESV surface, morph, position), other_m_words, narrative_n, narrative_refs, esv_text.
- **Script:** [`m64-choose-verses-pull-v3-20261008.py`](m64-choose-verses-pull-v3-20261008.py), unchanged. It was run as `H2803I H2803H H2803G H2161 H2162 H6246 H5779 H0908 H3336 G1011 G1012 G4286 G4388 G5427 --tag plan` and is read-only against iba.db.
- The will set ([`m64-will-verses-v1-20261008.md`](m64-will-verses-v1-20261008.md)) is not changed. This is a second set on the same escalation.

## 1. Which terms are in the set

The set is every live M64 `cluster_strong` row that is not already in the choose set, the will set or the dedicate words (H6942H, H5144A). Each one has a plan, devise, count, purpose or intention gloss. The surfaces below are the ESV words in `verse_lexical.surface`.

| Strong's | Gloss | Hits | Verses | ESV surface (top) |
| --- | --- | --- | --- | --- |
| H2803I | to devise: devise | 44 | 43 | devise 9, planned 3, intend 3, devised 3, plans 3, formed 3, meant 2, thought 2 |
| H2803H | to devise: count | 34 | 34 | counted 8, calculate 5, regarded 4, considered 3, accounting 2, regard 2, accounted 2, esteemed 2 |
| H2803G | to devise: design | 19 | 18 | skillfully 5, skilled 4, devise 3, devised 2, designer 1, devises 1, execute 1, skillful men 1 |
| H2161 | to plan | 13 | 13 | purposed 6, propose 1, meant 1, plot 1, plots 1, devising evil 1, considers 1, planned 1 |
| G1012 | plan | 12 | 12 | plan 4, purpose 3, counsel 2, decision 1, decided 1, purposes 1 |
| G4286 | purpose | 12 | 12 | purpose 6, Presence 4, steadfast 1, aim in life 1 |
| H3336 | intention | 9 | 9 | intention 2, inclined 1, plan 1, purposes 1, frame 1, mind 1, thing formed 1, creation 1 |
| G1011 | to plan | 9 | 7 | wanted 3, made plans 2, deliberate 1, planned 1, make 1, plans 1 |
| G5427 | purpose | 4 | 3 | mind on 2, mind 2 |
| G4388 | to plan/present | 3 | 3 | intended 1, put forward 1, set forth 1 |
| H5779 | to plan | 2 | 2 | take counsel 1, Take 1 |
| H0908 | to devise | 2 | 2 | devised 1, inventing 1 |
| H2162 | plan | 1 | 1 | evil plot 1 |
| H6246 | to plan | 1 | 1 | planned 1 |

Four things in the data to note before reading:

- **H2803 is one word with three M64 sub-entries:** devise (I), count (H) and design (G). A fourth sub-entry, **H2803J *to devise: think*** (26 hits), is tagged **M15**, not M64. It is not in this pull.
- **H2803G is mostly craft:** skillfully, skilled, designer, skillful men. 11 of its 18 verses are the tabernacle work in Exodus. The other 7 include Haman's plot (Est 8:3, 9:25) and God's devising (2Sa 14:14).
- **G4286 "Presence" (4 hits) is the bread of the Presence.** These hits are in the data but not about planning.
- **G1011 "wanted" (3 hits)** was the reason G1011 was left out of the will set. Its verses are here, with the rest of its plan words.

**G1013** *plan* (2 hits) is already in the will set, so it is not repeated here. Act 27:43 is the verse that set holds for G1013 together with G1014.

## 2. Scale

- **159 verses, 165 hits.** Five verses hold more than one hit: Gen 50:20 (2), Exo 35:35 (2), Rom 8:6 (2), 2Co 1:17 (3) and Eph 1:11 (2).
- **Overlap with the other sets:** Heb 6:17 is also in the will set and Rom 9:11 is also in the choose set. Every other verse is new to this strand.
- **10 of the 29 marked M64 × M47 verses** (`m64-m47-marked-verses-v1-20261006`) are in this set: Lev 7:18, 1Ki 12:33, Neh 6:8, Psa 17:3, Psa 35:4, Dan 6:3, Jon 1:4, Act 11:23, 1Co 4:5 and 2Co 1:17.
- **49 verses are cited somewhere in the narrative.** As with the will set, a citation shows only that the verse is quoted, not that its plan or count word has been dealt with, so none of the 49 is set aside.
- **32 verses carry no other M-code.**
- **Other M-codes in the same verses, by number of verses:** M58 31, M47 30, M06 29, M24 16, M72 15, M15 14, M65 13, M18 11, M16 10, M14 9, M25 8 and M23 8.

## 3. Related words outside M64 (not pulled)

These are the non-function words outside M64 that the ESV renders as plan, plot, devise, count, purpose or intend at least twice. They are listed so you can decide whether any belongs in this set. None is pulled.

| Strong's | Gloss | Cluster | Hits | Relevant ESV surfaces |
| --- | --- | --- | --- | --- |
| H2803J | to devise: think | M15 | 26 | count 10 (same root as H2803 G/H/I) |
| H4284 | plot | M06 | 56 | plan 14, purpose 4, devise 1 |
| H6098 | counsel | M16 | 89 | plan 10, purpose 6 |
| H3289 | to advise | M63 | 79 | plan 5, purpose 7, devise 3 |
| G3049 | to count | M26 | 39 | count 16 |
| H4209 | plot | M06 | 19 | purpose 2, intent 3 |
| H2790A | to plow/plot | M06 | 25 | devise 5, plan 1 |
| H3335I | to form: plan | T3 | 6 | plan 3, purpose 1 |

Words such as H4487 *to count*, H4557 *number* and H6485A *to reckon: list* are about numbering things, so they are not listed.

No verse has been read. Nothing here is interpreted or woven.
