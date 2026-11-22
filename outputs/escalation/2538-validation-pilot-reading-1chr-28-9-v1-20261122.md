# Validation pilot, part 2: the reading of 1Chr.28.9

Escalation #2538, 2026-11-22. Part 1 (structure): `2538-validation-pilot-pull-thought-v1-20261122.md`. Plan: `2538-validation-step-plan-v8-20261122.md`.
Everything below was done on the **copy** of the database. The live database was not touched. The reading is mine (inferential, B:4); every quotation and every word position was checked against the base data (`verse`, `verse_lexical`).

## What was read

All 55 live observations that carry a node on 1Chr.28.9 (154 live nodes). On the copy a `nature` column was added and set on all 55, and each judgement was logged in `ib_observation_change` (column `nature`, run `PILOT-2538-1CHR-28-9`, 55 rows) with its reason.

**Base data check of the nodes.** All 154 nodes on the verse name a real `verse_lexical` row of that verse with the same surface and Strong's code (0 mismatches), and the morph code agrees where set. The nodes are founded. Gaps: role empty on 13 nodes, collection empty on 3, subgroup empty on 124 (reported, not judged).

## Result

| marker | count | where |
|---|---|---|
| evidence | 29 | layer-2 11, prior-capture 6, layer-3 4, layer-1 2, verse-reading 2, lexical, char-reading, char-answers, strand-reading 1 each |
| inner being | 20 | prior-capture 8, layer-3 5, char-answers 3, engagement 2, strand-reading 2 |
| neither (held for your ruling) | 6 | all prior-capture |

| judgement | count |
|---|---|
| keep as it stands (true, founded) | 25 |
| repair (restate, complete nodes, or add a trace) | 17 |
| split into single-meaning observations before anything else | 4 |
| consolidate with another observation | 3 |
| for the researcher's ruling (neither marker) | 6 |

The marker follows content, not stage (principle 2): prior-capture holds both kinds; four layer-3 observations are evidence by content because they report only word distances.

## Findings that a structural test could not give

1. **A statement that is untrue.** #7319 says seeking precedes finding "invariably, never the reverse". Isa.65.1 says "I was ready to be found by those who did not seek me", and #7303 quotes that verse. Repair: restate to the three verses it cites (Jer.29.13, Isa.55.6, 1Chr.28.9).
2. **Codes that are not in the verse.** #5797 names M59 for forsake (the words carry M30 only) and calls M34 "whole/forever" (whole is M12; M34 is forever).
3. **A claim not founded for this verse.** #20549 says 1Chr.28.9 has the inclination "kept forever toward you"; that is 1Chr.29.18. In 1Chr.28.9 "forever" is the casting off.
4. **A claim stronger than its verse.** #12431 says thoughts are fully open to God and Jesus; Ps.139.23 is a petition, and the subject of Heb.4.12 is the word of God. #7320 adds "covenantal", which the verse does not state. #17167 is titled "rejection and non-rejection" but quotes only the rejection.
5. **A count that does not match its own list.** #22623 says "ten" where it names nine verses with "do" (ten occurrences, Num.33.56 twice), and it drops 1Chr.28.9 "serve" though it holds the node. All other word distances in the 16 current-method observations on this verse check out against `verse_lexical.position`.
6. **Meaning duplicates inside the current method.** #22524 and #22604 (heart or mind with the thought), and #22525 and #22608 (knowing and the thought), say the same thing; the later of each pair traces the earlier. Merging is not a plain merge: the trace must be re-pointed to the earlier one's own sources (#22342, #22306 and #22346, #22306).
7. **Text with nodes missing.** #7317 cites Ps.119.10 and Isa.31.1 without nodes; #21752 names objects it holds no node for; #19613 and #20029 cite far more verses than they hold nodes for.
8. **Old-document residue.** Six prior-capture observations are table rows or outline lines of the earlier work ("Carried since #1986", "Include", "New section", "waits for the researcher"): #19613 (election statement with a pointer to "§2a"), #19915, #20029, #20345, #20414, #20427. They are neither evidence nor inner being, so they are held for the ruling. Their verse facts are all true and held elsewhere.
9. **Nodes I expected to be duplicates were not.** On #20019, node 80171 and node 66620 are two different "heart" occurrences of Gen.8.21; node 85440 is the same word as 66628 under another collection. A node per collection on the same occurrence is the design, not a duplicate.

## Consumption: what the pilot shows

**No older observation on this verse can be shown to be consumed by a current-method observation.** The current method (thought) covers the partner words and the placing of "thought" itself; the older observations carry facts about seeking, forsaking, planning, willing, serving and God knowing thoughts, which belong to collections that have not yet been through stages 1 to 4. They are not discarded and not consumed: they stay live, marked, until the owning collection's validation can show their meaning stated by a new observation.

So the rule is: a consumption is recorded (`consumed_by`) only when a live observation states every fact the old one states and the old one adds no claim the new one lacks; until then the old one stays, with its marker. The expectation that most are consumed holds collection by collection, not for one collection in isolation.

The one consumption that is real inside this verse is among the older observations themselves: the sentence "God and Jesus know thoughts" occurs in #12431, #20455 (second claim), #20489 (last section) and #20498 (first claim). Those three compound observations are split first and then that claim is consumed into #12431 once restated.

## The noise question: do created evidence observations earn their place?

Of the 20 inner-being observations, 5 trace to evidence already (the layer-3 ones) and 15 do not. A created evidence observation is not noise only when it states something about the data that the nodes and the quotation do not. Test:

- **#12431 (God and Jesus know thoughts): earns it.** The nodes list the words, not who does what to what. Draft, every quotation verified verbatim in `verse`: *In Ps.139.2 ("you discern my thoughts"), 1Chr.28.9 ("understands every plan and thought"), Isa.66.18 ("I know their works and their thoughts"), Ps.94.11 ("knows the thoughts of man") and 1Cor.3.20 ("knows the thoughts of the wise") the subject is God and the thoughts are the object of discerning, understanding or knowing; in Ps.139.23 God is asked to know the speaker's thoughts; in Luke.5.22 and Matt.9.4 the subject is Jesus; in Heb.4.12 the word of God discerns "the thoughts and intentions of the heart".* It makes the inner-being observation checkable and repairs finding 4.
- **#7319/#7320 (seeking and finding): earns it.** Draft: *In Jer.29.13 ("You will seek me and find me"), Isa.55.6 ("Seek the Lord while he may be found") and 1Chr.28.9 ("If you seek him, he will be found by you") the seeking is stated before the finding, and 1Chr.28.9 states it as a condition; Isa.65.1 states the finding as given to "those who did not seek me".* The clause type is not in any node.
- **#12413 (God knows the inclination before it acts): earns it.** Draft: *Deut.31.21 ("I know what they are inclined to do even today", "before I have brought them into the land") uses H3336, the code of "plan" in 1Chr.28.9.* The timing is not in any node.
- **#19501 (know and serve with the whole inner being): noise.** The quotation and its 11 word nodes are the whole evidence; a created observation would restate them.
- **#20019: not needed.** It can trace to #12412, which already states H3336 across Gen.6.5, Gen.8.21, 1Chr.28.9 and Ps.103.14.

So two refinements to the trace rule (IB-07): (a) a trace points first at an existing evidence observation, and an evidence observation is created only when none states the fact; (b) an inner-being observation whose entire evidence is the verse quoted in full, with a word node for every word it relies on, counts as self-evidencing and needs no created observation.

## What the pilot changes in the plan (for v9)

- The ruling state is `for_ruling`; 6 here, all old-document residue. No other case needed a ruling.
- Repair came before deletion in every case: of 55, **none** is proposed for deletion. 6 wait for your ruling; the rest are kept or repaired.
- Splitting is a separate action before consumption (4 observations).
- Consolidating an observation that another traces needs a function that re-points the trace; `merge_observation` cannot do it (same text only).
- Restating needs a function for observations of any stage; `modify_observation` exists but the 26 deleted observations and the layer-3 trace chain have no sanctioned path yet.

## Not done, and limits

- Only 1Chr.28.9 was read. #21757 has 79 nodes; the other 78 verses were not read. Hebrew sense claims (for example "base cultic-consultation sense" of H1875 in #5793) were not checked: `strong_meaning_tree` holds sense text by lemma and was not read in the pilot.
- Nothing was restated, split, consolidated or deleted. The three drafted evidence observations are text only; none was created on the copy.
- The marker `nature` exists on the copy only; `cfg_enum`, rule IB-07, the consumption function, the restate/split/consolidate functions, a PowerShell entry point, a test plan (B:46) and the USER-GUIDE entry are not built.
