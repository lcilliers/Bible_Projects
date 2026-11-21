# #2526 Stage 2: the grouping of the surfaces and the subgroups. A proposal, with the implications worked through (v1, 2026-11-21)

Status: a proposal for your reading and correction (B:105). Nothing is built or changed. It starts from what you defined, shows from the tables what the first attempt (#2509) actually did, says why it failed, and proposes a simpler method. Where I am inferring, it says so (B:4). The data figures were read from the live tables and from the rollback snapshot taken before the `thought` grouping was cleared, read-only.

**Terms (researcher's definition, 2026-11-21).** *Surface groups* are the four main groups into which the surfaces are sorted against the working definition of the inner being; the collections are built from two of them (behaviour and inner_being_state). A *collection* is built from like or related surfaces. A *subgroup* (surface subgroup) is the working unit of a collection: a collection consists of subgroups, and the subgroup is the unit of reading. **In this document "the grouping" and "a group" mean the subgroups of a collection, never the four surface groups.** Where an earlier line said "surface group" for the working unit, it meant the subgroup.

## 1. What you defined (the points I build on)

| No | The point | Your words, where recorded |
|---|---|---|
| 1 | **Purpose.** The subgroup makes a collection digestible and becomes the unit of reading. Each layer reads by subgroup and deposits observations for the next layer. | #2515 v20 ("the subgroups becomes the unit of reading") |
| 2 | **A subgroup is a concept inside the collection.** An observation is made once for it, and the verses of every surface travel with it through the nodes. | #2463 v18 (d): "these sub groups are concepts"; (a) "the verses travel with it in the nodes" |
| 3 | **The unit that is grouped is the surface, the word.** | #2463 v16: "looking through the 33 words I can spot specific grouping"; "each grouping becomes an observation with the surfaces as the nodes"; v18: "all the derivatives of mind that travels together: minding, in mind, to mind, minds" |
| 4 | **Your groups of `thought`:** starting (conceiving, gives thought, imagine); weighing (considered, conflicting thoughts); types of thought (imagination, meditation, minding, musing, opinion, reasoning, pondering, thinking, suggestion). "The word thought is a collective word that has lots of different nuances." | #2463 v16 |
| 5 | **The basis is the meaning of the surface words**, mostly simply judged from the dictionary and Strong's meaning, and has nothing to do with the inner being. | #2509 v3 |
| 6 | **Membership of the collection is settled.** The sorting was "roughly 90% correct, with an acceptable margin of error"; what is wrong is picked up in the deeper analysis and compensated for; a word wrongly in a collection is moved out by the change procedure and the move is processed. | #2515 v20; #2463 v18 (e) |
| 7 | **Claude decides in the majority of cases; you scrutinise.** | #2463 v18, 5.4 |
| 8 | **The grouping is tested and reformed in the later layers.** | #2463 v16 ("keep on validating the grouping, reform the groups if needed") |
| 9 | **Step 1.2: the Strong's codes are placed with the group as "the link to the usage of the grouping".** | #2463 v16 |

## 2. What the first attempt did (from the tables)

`thought` has **33 surfaces** (19 word families by base: for example imagine, imagines, imagining, imagination are one family), 394 occurrences, 351 verses.

- **The unit was changed from the surface to the surface and Strong's code.** The 33 surfaces became **197 index rows** (188 of them by code) and each row was judged on its own.
- **Each code was judged on its own lexicon meaning, which re-decided what the collection had already settled.** 81 of the 197 rows were set aside as "not the meaning this collection gathers". All 9 codes of `conceive` were set aside, although `conceive` is in your "starting" group. `reason` had 17 of 18 codes set aside.
- **Surfaces were scattered.** `thought` sat in 8 groups, `think` in 5, `regard` in 3, `considered` in 4.
- **The groups were named for what the original words mean, not for the facets of the concept.** The ten groups were thinking, considering, meditating, reasoning and disputing, a thought, planning and plotting, counting and regarding as, knowing and understanding, remembering, weighing. Only some resemble yours; none is "starting".
- **The report unit was the code row.** You could not scrutinise 197 rows of codes the way you scrutinised 33 words.

## 3. Why it failed (my reading; inferential until you confirm)

1. **Wrong unit.** You group words. I grouped the lexemes underneath them. The surface is the ESV word, and one ESV word renders many original words: across all collections 18% of surfaces carry 9 or more codes and only 35% carry exactly one. A code-level judgement therefore cuts every common English word apart.
2. **I second-guessed the membership.** The collection already says the word belongs. Re-judging each code against a lexicon "changed the meaning of the underlying words", which is your verdict, and it is accurate: `conceive` was removed from the concept it was gathered for.
3. **The facets were never the target.** Your groups are facets of the concept (a thought starts, is weighed, takes kinds). A lexicon gives lexeme senses, which are not facets.
4. **No acceptance test.** You named the groups of `thought` yourself. That is the test, and it was not applied to the result: #2509 v5 reports counts, not agreement with your groups.
5. **Over-engineering.** Split rules, uncertain flags, scrutiny reports of code rows, for a task you do by eye in minutes.

## 4. The proposal

**4.1 The unit is the surface.** A surface is placed whole in one subgroup. Its occurrences inherit the subgroup through the node (already built, `ib_node.subgroup_id`). The code split of the index is not used in stage 2.

**4.2 Word families are the default gathering.** The base is in the data (`surface_term.base_id`): `thought` has 19 families for 33 surfaces, so a judgement of 19 units gives the 33. The family is a default, not a rule: your own groups split the family imagine (imagine in "starting", imagination in "types"). A form may go to another group when its meaning differs; the reason is one line.

**4.3 Membership is taken as given.** The method judges which facet of the concept a surface expresses, not whether it belongs. A surface plainly outside the concept is moved out by the collection change procedure (B:129, B:134), not set aside in a subgroup state. I expect almost none.

**4.4 [AMENDED by 4.10: the evidence is meaning in context] The evidence per surface:** the surface and its family; its tier in the collection (core, synonym, opposite, gathered: already in `collection_link`); its occurrence count; the head sense of its commonest own codes (Strong's, as a pointer to the facet); and, where stage 1 is done, the stage 1 sense observations (what the word means in its verses). One or two verses may be read where the meaning in use is not clear. This reverses a change I made today: method rule GP-01 now says "judged without the verses", taken from the Programme book. The conceive and reason cases show that the verse sometimes decides, so GP-01 should say the dictionary is the evidence in most cases and the verses may be read where they are not clear (your "in the majority of cases"). **This also fixes the order: stage 1 first, then the grouping** (the Programme book's order), because stage 1 already records what each word means in its verses.

**4.5 The shape of the groups.** Few, each a facet, named in your terms, with a one-sentence definition (which becomes the step 1.1 observation). The default for a collection is one group; a collection is split only where its words differ in kind of meaning. There are 61 collections of 12 surfaces or fewer, and for most of them the collection is the concept. A word that names the concept itself (`thought`, `thoughts`) is the collective word; it needs a home (decision Q4).

**4.6 [SUPERSEDED by 4.10: there is no "concept" test before stage 4] Polysemy: the surface stays whole, the codes that do not carry the concept are marked.** `reason` is mostly "for this reason", `conceive` is partly pregnancy, `considered` carries noise codes such as "no" and "I" from multi-word units. The surface stays in its one group. The codes (and so the occurrences) that do not carry the concept are marked outside with a reason, at the code level, not regrouped. They remain with the surface for the verses, are not enriched at 1.2, and are read at stage 4 as standalone or outside. This reuses the existing code rows of the index with the state `outside` beside the whole placement.

**4.7 [SUPERSEDED by 4.10] Step 1.2 changes with it.** Today the rule demands a node for every Strong's code of the group, which would demand an enrichment of "no" and "I" for `considered`. Your definition (point 9) is the codes that link the group to its usage. The rule becomes: the concept-bearing codes (those not marked outside).

**4.8 The review is a short list.** For each collection: the groups, each with its definition and its surfaces (counts), and a one-line flag on any surface I am unsure of. For `thought` the acceptance test is agreement with your groups, and I show the disagreements.

**4.10 Revised after the researcher's answers to Q1 to Q6 (2026-11-21).**

Answers, in the researcher's words: Q1 agree. Q2 agree. Q3 "evidence are meaning in context. meaning is derived from the surface, recognising that a surface may have hidden meaning that is in the different strongs used for the same surface". Q4 "this is exactly what the surface subgroup are". Q5 "concepts only come into play in Stage 4 when surface subgroups forms behaviours which is synonymous to concepts". Q6 agree.

What changes:
1. **Evidence is meaning in context (Q3).** The meaning is derived from the surface, in its verses. The dictionary and Strong's is a pointer, not the basis. The different Strong's codes under one surface are read as possible hidden meanings of that surface, not as separate things to place. So 4.4 stands in its direction (verses are read; stage 1 first) but the rule that the verses are kept out (GP-01 as I amended it today) is withdrawn, not just softened: GP-01 must say meaning in context.
2. **No concept test in stages 2 and 3 (Q5).** A concept (a behaviour) exists only in stage 4, when a subgroup forms a behaviour. So the notion "a code that does not carry the concept" (4.6) and "enrich only concept-bearing codes" (4.7) are wrong and withdrawn. A subgroup before stage 4 is a lexical working unit grouped by kind of meaning. Nothing is judged "outside the concept" in stages 2 and 3, and my recommendation on Q5 was mistaken.
3. **Polysemy (replaces 4.6).** The surface is placed whole in one subgroup (Q2). Its different codes are not marked outside. They are the lexical variation that stage 1 and step 1.2 record (the double-meaning item of 2.1 already exists for this), and in stage 4 they become dimensions of the behaviour (5.1).
4. **Step 1.2 (replaces 4.7).** It stays as built: the codes of the subgroup's surfaces are enriched, because hidden meaning sits in the codes. The noise codes that arise from multi-word units ("no", "I" under `considered`) are the stage 1 alignment question (#2527 step 1), not a concept question. That is settled once there, not by dropping codes from step 1.2 on a concept ground. This makes the build smaller: **no `outside` marks at all.**
5. **Collective words (Q4).** `thought` and `thoughts` form a subgroup of their own: that is what a subgroup is, a working unit of kind of meaning. No special rule.
6. **Section 7, `thought`.** Read the unplaced words (regard, regarded, reason) as a stage 2 judgement of kind of meaning in context, and the `conceive` pregnancy occurrences as hidden meaning inside the surface, not as marks outside.
7. **Section 6, build.** Drop "outside marks" from GroupRecord and the 4.7 rule change to LR-04; the evidence of GroupPull is the surface's occurrences in context (verses), its family, tier and counts, with the stage 1 results; GP-01 reworded to meaning in context.

**4.9 Regrouping.** Allowed until stage 3 is closed; after that it goes through the same change procedure and reopens the rows (built and tested). For the pilot, stage 3 does not open until you have read the grouping (the subgroup status column exists: `indicative` until you confirm).

## 5. Implications by stage

| Stage | Effect of this grouping |
|---|---|
| 1 (words) | Unchanged: one row for each surface and lettered code. Its results become the evidence for 4.4 and 4.6, so it runs first. The question of function-word rows for multi-code units (#2527 step 1) is the same alignment noise as 4.6 and is settled once. |
| 3 (step 1.1, meaning) | One observation for each group; its nodes are all occurrences of the group's surfaces. |
| 3 (step 1.2, enrichment) | Needs the rule change of 4.7. Without it the step demands codes that are noise. |
| 3 (step 2.1, pairings) | Pairings, qualifiers, relations and double meanings are keyed to the group. More groups means more pairs of groups to test against the three-verse threshold, so keep groups few. A double meaning item already exists for a surface with two codes, which fits 4.6. |
| 4 (steps 3.1 to 3.3) | A verse-working row is a subgroup and a verse. Volume is driven by verses, not by groups: the 3,437 surfaces of the 169 collections have 70,145 occurrences in 58,450 (collection, verse) pairs, so about 58,000 verse rows and at five rows a file about 11,700 working files. For `thought`: 351 verses. A verse with words from two groups gives two rows, so splitting a collection into many groups costs rows. |
| Claims (5) | **Corrected (researcher, 2026-11-21).** Claims do not bind to groups. Stage 5 pulls the stage 4 observations together into behaviour statements, and the surface groups fall away. All the analysis of the groups and their verses is finished in stage 4 and arrives in stage 5 as observations only. See 5.1. (My first wording, "claims bind to observations of groups", kept the group alive into stage 5 and was wrong.) |
| Nodes | Unchanged. `subgroup_id` follows the surface placement; whole placement makes it simple and exact. |

### 5.1 Two modes of work on the same group, and where the group ends (researcher's clarification, 2026-11-21)

**Lexical mode (stages 1 to 3).** The group is a unit of work, but the focus is the specific surface and its meaning in context. What matters is the distinctive use of each word, the differences between words, what it means that one surface renders several Strong's codes, and the small variations between forms of a surface. The group holds these together for handling; it does not smooth them out. This is why 4.1 to 4.7 keep the surface whole, mark codes that do not carry the concept, and enrich codes one by one.

**Inner-being mode (stage 4).** The mode switches from analysis of words to interpretation of behaviour. The group is likely to morph into a single concept of behaviour, and the lexical variations (the different codes, forms and uses) turn into the dimensions of how that concept works. So the group is read here as a collection for understanding behaviour, not as a set of words to tell apart. The lexical results of stages 1 to 3 are the evidence it is read from; they are not re-done.

**What this means for the proposal:**
1. The grouping of stage 2 is a working grouping for the lexical stages. It is not the final shape of the concept. It may be reformed in stage 4 (point 8 of section 1), and in stage 4 the unit of reading may be the group as one concept rather than its facets as separate things. 4.9 therefore stands, and the pilot should expect regrouping at the start of stage 4.
2. Do not design the grouping to serve stage 4's needs (for example by making groups small to match "dimensions"). The dimensions come from the lexical variation inside a group, which stage 4 reads. Groups are made on meaning (4.4).
3. The built stage 4 (steps 3.1 to 3.3) reads by subgroup and verse. I have not checked whether it carries the lexical variation (which code, which form, which tier) into the verse-working row as dimension evidence, or whether its wording treats the group as a set of words. That check is open (see 5.2).

### 5.2 Stage 4 and stage 5 are different jobs

| | Stage 4 (inner-being analysis) | Stage 5 (claims) |
|---|---|---|
| Job | Articulate and set the observations for all the elements of the behaviour. These are the building blocks. | Pull the observations together into behaviour statements. |
| Unit | The group and its verses (rows: subgroup and verse, subgroup, interworking) | The observations only. The group has fallen away. |
| Produces | Observations | Claims (statements of behaviour) |
| Must not | Formulate a claim as an observation | Discover a new building block |

Consequences to check in what is built or written:
- Stage 4 rules IB-01 to IB-06 and the stage 4 row wording must ask for building blocks (elements, dimensions, relations of the behaviour), never a conclusion about the behaviour as a whole. Row 3.2 (per subgroup) and 3.3 (interworking) are the places where this is most at risk of becoming claim-making.
- Stage 4 must be complete in itself: everything a claim will need from the groups and verses has to be an observation by the end of stage 4, because stage 5 will not go back to the groups.
- If stage 5 finds a missing building block, the way back is a stage 4 reopening, not a new observation made in stage 5.
- The Programme prose wording on stages 4 and 5 (written today) should be read against this table.

### 5.3 Stage 4 discovers behaviours from the observations (researcher's answer to Q7, 2026-11-21)

In the researcher's words: "the subgroups and observations of a collection will be the input for stage 4. in most cases the subgroup is likely to form into a concept/behaviour but that is not a given. the behaviours will be discovered from analysing the Stage 3 observations, with the occasional reading back into the base data."

This corrects 5.1 (where I said the group morphs into the concept) and is the main thing to carry into stage 4:
1. **Input of stage 4:** the collection's subgroups and the stage 3 observations on them. The verses are the base data, read back into only occasionally.
2. **A behaviour is discovered, not given.** A subgroup often forms one behaviour, but it may form none, several, or join with another subgroup's observations. So a behaviour is not keyed to a subgroup, and the subgroup is not the unit that a stage 4 row has to be.
3. **Stage 4 is analysis of observations,** with a return to the verses when an observation needs it. It is not a fresh reading of every verse of every subgroup.

**Consequence I must state plainly: this does not match what I built.** My stage 4 (steps 3.1 to 3.3, built and applied today, 44 of 44 tests passing on a copy) is a verse-first design: step 3.1 is one row for each subgroup and verse (about 58,000 rows across the 169 collections), with the observations on the verse as an add-on, and 3.2 and 3.3 are rows keyed to the subgroup and to pairs. Passing its own tests does not make it the design you describe. It was built on the brief's reading, which I did not test against your description. What is likely wrong:
- the verse as the main unit of work (you describe observations as the main input, the verse as occasional back-reading);
- the subgroup as the key of every row (a behaviour need not equal a subgroup);
- the volume that follows (58,000 verse rows) when the real work is analysis of a much smaller set of observations.

Nothing needs to be undone now: no stage 4 row has been written on live data and the stage cannot open before stages 1 to 3 close. But #2528 should not be approved as it stands. A stage 4 design built on 5.3 would need your direction on what its unit of work is (for example, a row for each cluster of related observations of a collection, or a row for each candidate behaviour), and what "occasional reading back" requires on the record (which verse, why). I have not designed that; it is the next proposal after stage 2, or before it if you prefer.

So the grouping decision is cheap in effort (3,437 surfaces, a short pass for most collections, 61 of them with 12 surfaces or fewer) and large in consequence (everything after is keyed to it), which is the reason to get the unit right first.

## 6. What changes in the build (small)

- `GroupPull`: one row for each surface (not each code), with the evidence of 4.4; the family shown with it.
- `GroupRecord`: one placement for each surface; a group name and definition; `outside` marks at code level with a reason; no code split of the whole placement.
- The `IndexCheck` report and the scrutiny report: a list of surfaces by group (the form of your own reading).
- Method rules GP-01 to GP-04 and the step 1.2 rule (LR-04) reworded; the guide; the test `temp_2509_grouping_test_run.py`, with the acceptance test on `thought` against your groups.
- Not changed: the tables, the node rule, the ledger, the gates.

## 7. Worked example: `thought`, my reading of your groups (for your correction)

| Facet (your word) | Surfaces | My confidence and the question |
|---|---|---|
| Starting | conceive; gives thought; imagine, imagines, imagining | You put "imagination" in the types, so the family imagine splits. `conceive`: its pregnancy occurrences (H2029) are marked outside (4.6). |
| Weighing | considered; conflicting thoughts; weigh, weighing | You named the first two; weigh and weighing are my addition. |
| Kinds of thought | imagination; meditate, meditates, meditation; mind on, minds on, setting your mind; musing; opinion; pondering, ponders; reasoned, reasoning; think, thinks, thinking; suppose, supposing | Your list, with the derivatives gathered. |
| The collective word | thought, thoughts | Q4: its own group, or with the kinds? `thought` has 28 codes (the verb past tense, mainly "said in his heart", and the noun thoughts, H4284). |
| Unplaced, a question for you | regard, regarded, once regarded; reason (the noun) | You did not name them. `regard` has 27 codes and mostly means "with regard to" or "regard as". Likely "weighing" or outside. |

## 8. Decisions for you

**Status 2026-11-21: Q1, Q2, Q6 agreed; Q3 answered (meaning in context); Q4 answered (its own subgroup); Q5 answered differently from my recommendation, so the recommendation below is withdrawn. See 4.10. Q7 open.**

| No | Question | My recommendation |
|---|---|---|
| Q1 | Is the unit the surface, with the family as the default gathering? | Yes. |
| Q2 | A surface in more than one group? | No: one group; the codes that do not carry the concept are marked outside (4.6). A second group only by your ruling, as B:129 already says for collections. |
| Q3 | Evidence: dictionary and Strong's, plus stage 1 results, with verses where unclear? | Yes, and stage 1 first. |
| Q4 | Where do the collective words (`thought`, `thoughts`) go? | In their own group (the concept in general), unless you want them with the kinds. |
| Q5 | Step 1.2 enriches the concept-bearing codes only? | Yes. |
| Q6 | A small collection is one group by default? | Yes, a split needs a stated difference in kind. |

| Q7 | **[ANSWERED 2026-11-21, see 5.3: the subgroups and observations are the input to stage 4; behaviours are discovered from analysing the stage 3 observations; the subgroup often, not always, forms a behaviour.]** **Answered in part (researcher, 2026-11-21):** surface groups are the four main groups; subgroups are the working unit; a collection consists of subgroups. Still to confirm: in stage 4, what morphs into "a single concept of behaviour" and is read as a collection for understanding behaviour: the subgroup (its surfaces and codes becoming dimensions), or the whole collection (subgroups becoming dimensions)? | I read it as the subgroup, because the subgroup is the unit of reading and a collection is already a set of like or related behaviours. 5.1 and 5.2 are written that way. If you mean the collection, the stage 4 unit of reading changes and I will say how before building. |

## 9. Corrections to what I said earlier

- (2026-11-21, later) §5 did not state the switch from lexical to inner-being mode, and its "claims" row was wrong. Both corrected in 5.1 and 5.2.

- The readiness audit (F12) said `thought` is the largest collection, with 197 surfaces. That was wrong: 197 was the number of index rows after the code split. `thought` has 33 surfaces and the median collection has 15; the largest, `desire`, has 63. Corrected in the audit.
- Method rule GP-01 was amended today to say the grouping is judged without the verses. See 4.4: I suggest it be amended again.
