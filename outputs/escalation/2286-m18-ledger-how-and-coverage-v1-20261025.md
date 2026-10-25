# #2286 prototype step 6: how the M18 ledger reached its summary, and how complete it is

Date: 2026-10-25. Escalation #2286 v14. Read from the M18 folder
(`_analytics/Clusters/M18 - desire-longing/`), `archive/docs/claude-md-history-to-20261021.md`, and
live iba.db, read-only. The coverage script is in the session scratchpad.

## 0. The question (v14, verbatim)

> So M18 ledger did analyse this cluster without subgroups. a) how did it reach its point of summary
> of the cluster? b) does that mean M18 ledger is substantially incomplete.

## 1. a) How the ledger reached its summary

**The ledger did segment the cluster. It just didn't use the subgroup table.** The overview
(`m18-cluster-overview-v1-20261008.md`, #1993) split M18's 88 codes into seven gloss groups, A to G. It
said plainly that they were "a reading aid by gloss only. They are not a finding and not a
sub-grouping of the cluster". The groups:

| group | gloss | codes | hits |
|---|---|---|---|
| A | desire, craving, longing | 35 | 258 |
| B | delight, pleasure, pleasant, good | 19 | 640 |
| C | will, willing, acceptance | 9 | 372 |
| D | jealousy, zeal | 9 | 112 |
| E | thirst, hunger | 5 | 45 |
| F | precious, costly | 4 | 60 |
| G | gloss away from desire | 7 | 23 |

**The order of work** (`m18-strand-handoff-v9-20261012.md`, the last record):

1. **Overview:** scale (1,370 verses, 64 books), the codes by gloss, where a word's surface varies,
   and which other M clusters share verses with M18.
2. **Shared-verse read-backs first:** the verses M18 shares with M47 Inner Seat (208), M25 Life &
   Death (89) and M02 Anger & Wrath (51). Later, M72 Authority & Dominion (182).
3. **Held items** from earlier threads: jealousy OT-95, *ṭôb* (good) OT-96, heat OT-15, rousing #1942.
4. **The gloss groups, one at a time:** A, D, E, F, G, then B (split into B1 delight, B2 pleasant, and
   the rest triaged by role), then C. For each group:
   - Pull its verses.
   - Drop the verses already decided in an earlier register.
   - Decide each verse, with its reason, into a register CSV.
   - Read the verses in depth in a reading file.
   - Weave the result into the narrative.
5. **Role triage** (from 2026-10-11, cfg_behaviour_rule 73). Each verse's M18 word was given its role
   against the verse's main operation. Where the M18 word was central, the verse was read. Where it
   qualified another cluster's word, the verse was marked forward. Where it qualified an act with no
   M-code in the verse, it was "no carrier". Where it had no inner-being sense, it was data.

**There was no single summary of the cluster.** The ledger ended in the woven narrative: the M18
words were read into 10.6 and its sections ("10.6 is fine for M18", researcher, 2026-10-09). Some
were also woven into 10.1 to 10.13, Ch 2, Ch 11, Ch 12, 13.1 and Ch 14, with the claim register up
to v48. Each group was closed by its weave, and the cluster was closed when the last group was woven.

## 2. b) Is it substantially incomplete?

The answer depends on which kind of completeness is meant. They give different answers.

### 2.1 Verse decisions: 84% decided, and the rest left by a ruling

| measure | verses |
|---|---|
| M18 verses, live now (88 codes) | 1,370 (the same set as the overview) |
| with a decision in one or more of the 13 registers and triages | **1,146 (84%)** |
| with no decision anywhere | **224 (16%)** |

**Who the 224 are:** 204 are on H2896A *ṭôb* ("good, better, well"). The other 20 are on H5273A (8),
H2895 (5), G0701 (4), H2655 (4), G5369 (1) and H2656 (1). They are the qualifier hits from group B
("good" said of something else). They were left by a ruling (researcher, 2026-10-09, in
`archive/docs/claude-md-history-to-20261021.md` line 254): the qualifier hits are mostly secondary,
*"if needed it my be picked up when the primary cluster comes into focus"*.

**Whether anything will bring them back:**

| | verses |
|---|---|
| a word of another M cluster is in the verse, so that cluster's reading can reach it | 183 |
| **no other M-coded word in the verse, so no cluster reading will bring it back** | **41** (for example 1Ki 20:3, 1Sa 8:14, Deu 6:10, Deu 8:7, Exo 2:2) |
| held by an open thread item | 9 |
| cited in the narrative | 33 |

Only the 23 forward marks from item H (the M72 verses) were recorded as open items (OT-97). The
other 183 that rely on "the primary cluster" have no forward mark. They come back only if that
cluster's reading happens to pull the verse.

**On this measure the ledger is not substantially incomplete.** About a sixth of the verses were
left on purpose. The gap is that 41 have no way back and 183 depend on chance.

### 2.2 In the tables: almost nothing

The ledger's results live in CSVs, reading files and the narrative. They do not live in the
observation tables:

| table | M18 content |
|---|---|
| `ib_observation` on M18 codes | 210 rows, all stage verse-reading, none with cluster_code M18 |
| `ib_node` with cluster_code M18 | 60 nodes, 22 verses |
| `ib_node` on any M18 code | 220 nodes, 25 verses |
| `reading_strand_hit` on M18 codes | 0 |
| `narrative_citation` of M18 verses | 918 of the 1,370 verses are cited in the narrative |

So the 1,146 verse decisions, their reasons and their faces are in files, not rows. That matters
for the analytic process now: claims and narrative are worked only from the tables (B:114), and work
done earlier is gathered, not redone (RM-04). Read that way, **M18 is close to empty in the tables.**
The verses are woven into the narrative, but the findings behind the weave can't be gathered.
This is the gap that #2261 (ledger shape), #2218 (readings not yet in the tables) and #2266 (October
catch-up) are about.

### 2.3 Against the observation rules: not checked

The ledger ran before the reading-by-role rules and the observation rules RG-01 to RG-25 were set
in config. It hasn't been checked against them. That is the subject of #2260 and #2265 to #2267.

## 3. What this shows for the work unit

These are inferential: my reading of the facts above, not a ruling.

- **The ledger's gloss groups did the job a subgroup does**, cutting 1,370 verses into units that
  could be worked. They were made by hand, in one overview, by gloss. They were never written to
  `cluster_subgroup`, so nothing can query them.
- **The verse decisions were per verse, but the unit of work was the group.** The registers show the
  shape a work-unit JSON might take: each verse with its decision, reason and home.
- **The step that kept the work manageable was filtering out verses already decided** in an earlier
  register before each group. That is the "what is already known" question (O7 in the step 2
  paper), done by hand.
