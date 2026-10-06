# M64 Will & Resolve: quick summary (strand start)

**Date:** 2026-10-06 · **Escalation:** #1978 · **Status:** data summary only, no reading yet

**Source:**
- the researcher's query, run unchanged and read-only against iba.db: [`m64-strand-quick-summary-query-v1-20261006.sql`](archive/m64-strand-quick-summary-query-v1-20261006.sql)
- its output: [`m64-strand-quick-summary-pull-v1-20261006.csv`](archive/m64-strand-quick-summary-pull-v1-20261006.csv) (728 rows)

## 1. Two things about the query, for your decision

1. **Deleted `cluster_strong` rows are not filtered out.** Neither CTE has `cs.deleted = 0`.
   - H0014 (*be willing*) has two M64 rows in `cluster_strong`, both from the #1880 move from M30: id 17528 (`deleted = 1`) and id 17529 (live).
   - So every H0014 row appears four times in the output: 2 on the M64 side × 2 on the other side.
   - The 728 rows hold **551 distinct rows**. The figures below are counted on distinct hits, so they are not inflated.
   - The other 27 Strong's have one row each. Of M64's 29 `cluster_strong` rows, 28 are live.
2. **The "other" side is also filtered to M64.** `other_m_hits` has `cs.cluster_code = 'M64'`.
   - So the output pairs each M64 hit with every M64 hit in the same verse, itself included (distance 0).
   - `other_cluster_code` is always M64.
   - If you meant co-occurrence with **other** clusters (the column names suggest so), the filter would be `cs.cluster_code <> 'M64'`, or a pattern on the M-codes. I have not run that variant.

## 2. Scale

| Measure | Count |
| --- | --- |
| M64 Strong's in `cluster_strong` (live) | 28 (all have hits) |
| M64 hits (`verse_lexical`, distinct verse · position · Strong's) | 493 |
| Verses | 468 |
| Books | 54 |
| Verses with more than one M64 hit | 22 |
| Within-M64 pairs in one verse (unordered, distinct positions) | 29 |

The books with the most M64 verses are:

| Book | Verses |
| --- | --- |
| Deu | 41 |
| Psa | 40 |
| Isa | 39 |
| Act | 25 |
| 2Sa | 23 |
| 1Ch | 21 |
| 2Ch | 20 |
| Lev, Jer, Pro, Exo | 18 each |
| 1Sa | 17 |

## 3. Strong's, by hits

Surface forms are the ESV words in `verse_lexical.surface`, with their counts (the top six only).

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H0977 | to choose | 171 | 163 | chosen (71), choose (49), chose (28), chooses (6), choice (4), Choose (3) |
| H0014 | be willing | 54 | 52 | would (14), willing (13), he would (8), consent (3), unwilling (3), and would (2) |
| H2803I | to devise: devise | 44 | 43 | devise (9), planned (3), devised (3), intend (3), formed (3), plans (3) |
| H2803H | to devise: count | 34 | 34 | counted (8), calculate (5), regarded (4), considered (3), accounting (2), regard (2) |
| G1014 | to plan | 34 | 34 | want (5), I would (3), wishing (3), wished (3), desire (2), wanted (2) |
| H6942H | to consecrate: dedicate | 25 | 22 | dedicated (7), dedicates (6), dedicate (5), dedicated gifts (2), set apart (2), Consecrate (1) |
| H2803G | to devise: design | 19 | 18 | skillfully (5), skilled (4), devise (3), devised (2), skillful men (1), execute (1) |
| H2161 | to plan | 13 | 13 | purposed (6), meant (1), propose (1), planned (1), devising evil (1), considers (1) |
| H0972 | chosen | 13 | 13 | chosen (8), chosen ones (3), chosen one (2) |
| G1012 | plan | 12 | 12 | plan (4), purpose (3), counsel (2), purposes (1), decided (1), decision (1) |
| G4286 | purpose | 12 | 12 | purpose (6), Presence (4), aim in life (1), steadfast (1) |
| H6634 | to will | 10 | 7 | he will (4), he would (4), to his will (1), desired to (1) |
| G1011 | to plan | 9 | 7 | wanted (3), made plans (2), make (1), plans (1), planned (1), deliberate (1) |
| H3336 | intention | 9 | 9 | intention (2), plan (1), purposes (1), inclined (1), creation (1), mind (1) |
| H5144A | to dedicate | 5 | 5 | abstain (2), separates (1), consecrated (1), keep (1) |
| H5081G | noble: willing | 5 | 5 | willing (3), willing man (1), generous (1) |
| G5427 | purpose | 4 | 3 | mind (2), mind on (2) |
| G0138 | to choose | 3 | 3 | chose (1), choosing (1), choose (1) |
| G4388 | to plan/present | 3 | 3 | set forth (1), intended (1), put forward (1) |
| H0908 | to devise | 2 | 2 | devised (1), inventing (1) |
| H5779 | to plan | 2 | 2 | Take (1), take counsel (1) |
| G1013 | plan | 2 | 2 | plan (1), will (1) |
| G0830 | self-chosen | 2 | 2 | accord (2) |
| H7148 | chosen | 2 | 2 | chosen (2) |
| H2162 | plan | 1 | 1 | evil plot (1) |
| H6246 | to plan | 1 | 1 | planned (1) |
| G0140 | to choose | 1 | 1 | chosen (1) |
| G4401 | to choose | 1 | 1 | chosen (1) |

All surface counts are taken from distinct hits. In the raw CSV, H0014's rows appear four times over (see §1.1), and the Judg 17:3 position appears four times (see §4).

The same surface word sits under several Strong's. For example:
- "chosen" is under H0977, H0972, H7148, G0140 and G4401
- "plan", "planned" and "plans" are under H2803I, H2161, H6246, G1011 and G1012
- "would" is under H0014 and H6634

Surface variety within one Strong's is wide in places: G4286 (purpose / Presence), H2803 (devise / count / design) and H3336 (intention / creation / mind). That is where the change-of-character reading (#1919) would start. **No reading has been done.**

## 4. Within-M64 pairs (verses with more than one M64 hit)

There are 29 unordered pairs, in 22 verses.

| Pair | Count | Verses |
| --- | --- | --- |
| H0977 + H0977 | 8 | 1Ch 19:10; 1Ch 28:4; 1Ki 8:16; 2Ch 13:3; 2Ch 6:5; 2Ch 6:6; 2Sa 10:9; Isa 66:4 |
| H6634 + H6634 | 6 | Dan 5:19 (four hits) |
| H6942H + H6942H | 3 | 1Ch 26:28; 2Sa 8:11; Neh 12:47 |
| G1011 + G1011 | 3 | 2Cor 1:17 (three hits) |
| H0014 + H0014 | 2 | 2Sa 14:29; Eze 3:7 |
| H2803G + H2803G | 1 | Exo 35:35 |
| H2803I + H2803I | 1 | Gen 50:20 |
| G5427 + G5427 | 1 | Rom 8:6 |
| G1014 + G1013 | 1 | Act 27:43 |
| G1014 + G1012 | 1 | Heb 6:17 |
| G4286 + G1012 | 1 | Eph 1:11 |
| H6942H + H2803H | 1 | Lev 27:18 |

**Judg 17:3** has two H6942H rows at one position ("I dedicate"; morph HVhaa + HVhp1cs, codes 0 and 2 of one span). That is one ESV word over two Hebrew forms, not a duplicate. It is a single hit in the counts above.
