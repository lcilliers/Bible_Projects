# #2376 -- Chapter 10 reorganised around the collections: outline v2 (2026-11-08)

Replaces v1 (archived). Nothing in the narrative register has been changed.

## Researcher's corrections to v1 (verbatim record on #2376 v4), as applied here

- a) Collection creation is in progress; more collections will be added (for example humility). The list is therefore open, not fixed at 58.
- b) Old material is placed by its verses and associated claims, not by name matching. The collections CSV is the framework that decides the member verses of each sub-chapter. Chapter 10.0 is reserved for an overview of all sub-chapters. Collections such as `saying` will go through a pre-analysis filter (say or said is not exclusively an inner-being phenomenon).
- c) Sub-chapter headings are, for now, the collection label (which may cover several base words).
- d) The analysis in 10.1-10.15 is the starting point; nothing is thrown away; every statement finds a home.
- e) The narration is continuously updated.

## Structure

- `10` part heading stays. `10.0` becomes the overview of chapter 10 and its organisation.
- One sub-chapter per collection, alphabetical by collection label, numbered from 10.1. A new collection takes its alphabetical place and later numbers move (the register keeps history against the chapter, not the number). The table of 58 collections is in v1's list; it is not repeated here because the list is not final.
- No families.

## What I read (live database, read-only)

`narrative_section` (current blocks: `last_version` NULL), `narrative_claim_telling` (status current), `narrative_claim_source` and `narrative_citation` (verse rows), `verse` (osisId), and the collections CSV (osisId per collection). Column meanings were read from `cfg_table` and `cfg_column` first. Script: `C:\Users\lerouxc\AppData\Local\Temp\claude\cd505264a45b298d\3e786860-fe9c-4009-a10b-28b1c03f3294\scratchpad\ch10_homes.py` (scratch, not kept in the project).

A block is the unit (a heading and its text). A block's verses are the verses its told claims rest on plus the verses it cites.

## What the tables show (all 244 current blocks of 10.0-10.15)

| Current chapter | Blocks | Blocks with no told claim | Blocks with no verse | Distinct verses | Of those, not in any collection | Collection with most of its verses |
|---|---|---|---|---|---|---|
| 10.0 The inner being at work | 6 | 3 | 1 | 72 | 14 | saying (22) |
| 10.1 Feeling | 25 | 23 | 1 | 312 | 58 | saying (63), fear (62), delight (53) |
| 10.2 Knowing and hearing | 6 | 2 | 0 | 159 | 38 | saying (27), wise (19), know (18) |
| 10.3 Remembering and forgetting | 8 | 6 | 0 | 75 | 14 | forget (35) |
| 10.4 Thinking | 13 | 5 | 1 | 194 | 57 | saying (39), thought (37) |
| 10.5 Speaking | 13 | 10 | 1 | 130 | 32 | saying (35), fear (16) |
| 10.6 Wanting | 21 | 15 | 1 | 547 | 135 | desire (109), saying (91) |
| 10.7 Choosing and setting direction | 24 | 6 | 0 | 792 | 207 | saying (185), choose (86) |
| 10.8 Right and wrong | 1 | 0 | 0 | 35 | 6 | fear (13), saying (6) |
| 10.9 Relating to God | 16 | 9 | 1 | 318 | 83 | saying (54), fear (47), anger (32) |
| 10.10 Relating to others | 18 | 8 | 1 | 449 | 124 | saying (105), fear (35), love (32) |
| 10.11 Hiding and disclosing | 9 | 8 | 0 | 106 | 42 | saying (23), fear (10), know (10) |
| 10.12 Fear | 14 | 9 | 0 | 283 | 32 | fear (169), saying (67) |
| 10.13 Anger | 37 | 28 | 2 | 442 | 59 | anger (212), saying (96) |
| 10.14 Humility | 22 | 3 | 2 | 296 | 73 | pride (71), saying (33) |
| 10.15 Pride | 11 | 1 | 0 | 227 | 47 | pride (41), saying (41), boast (35) |

Verses recur across chapters, so the columns do not add up to a project total.

What this means:

1. **Verse overlap is real but wide.** Fear, anger, desire, forget and pride show a clear main collection in their old chapters. The others (feeling, relating to God, relating to others, choosing) spread their verses over many collections, so a chapter does not move as one piece. Placement has to be per block, or per statement.
2. **`saying` is in the top three of almost every chapter.** Until its pre-analysis filter exists, a statement cannot be placed in `saying` on verse overlap alone.
3. **Between 6 and 207 verses per old chapter are in no collection yet.** The blocks resting on them cannot be placed by verses until the collections that hold those verses exist (humility, and any others the collection work adds).
4. **Most blocks have no told claim.** 136 of the 244 blocks tell no claim in the register; their only verses are citations. Under the register rule (B:77) a statement that goes beyond its verses needs a claim with verse sources. That is the present state of the narrative, not something this move creates, but it means placement of those blocks rests on citations, not on claims.
5. **11 blocks have no verse at all** (block counts in the table). I have not read them; they may be headings or openings. They need a home by their text.

## Decisions needed

1. **A statement whose verses fall in several collections.** Options: (a) one main home, the collection holding most of its verses, with a pointer from the others (the register already has a telling kind `pointer`); (b) the statement is told in full in each collection it touches; (c) you choose the home statement by statement. I would take (a): it keeps one telling per statement and nothing is lost.
2. **A statement whose verses are in no collection yet.** Options: (a) a holding sub-chapter at the end of chapter 10, for example "Held for collections", from which statements move as collections are built; (b) the old sub-chapter stays in place unchanged until every one of its statements is placed. I would take (a): the numbering stays clean and 10.1-10.15 can go at once.
3. **`saying` and similar.** Statements resting mainly on `saying` verses are held (in the holding sub-chapter) until the pre-analysis filter says which saying verses are inner-being. Confirm.
4. **Order of work.** The move is a build of its own. Proposed order: design the placement rule (1-3), then a read-only placement report for every block (block, its verses, main collection, pointers, held), reviewed by you, then the register changes through `Narrative-Register.ps1`.

## What approval means

Approval of decisions 1-4 sets the rule and the order. It changes nothing in the register or in any chapter text; the placement report would be my next step and comes back to you before anything is moved.
