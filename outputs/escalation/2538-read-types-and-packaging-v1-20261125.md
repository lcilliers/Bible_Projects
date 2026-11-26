# #2538: the reads of stages 1 to 4 — each type, its input, its result, and how it is packaged (v1, 2026-11-25)

Written by Claude, session 760131f7, on the researcher's instruction recorded in #2538 v51. Analysis only: nothing is built, and no model has been called.

- **The steps:** specification v5 (`outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md`). This file adds the reads, not the steps.
- **The measurements:** live iba.db, collection thought (id 56), by a read-only script. Every lookup was indexed (SEARCH on `idx_verse_lexical_strong` and `idx_verse_lexical_verse_id`), and the whole run took 1.1 seconds.
- **Characters to tokens:** tokens are estimated at characters ÷ 4. That ratio is an assumption, not a measurement.

## 1. Thought, measured, by subgroup

| subgroup | words | occurrences | verses | verse text | verse structure | lexicon (LSJ+Mounce) | meaning tree | old obs | B1 output |
|---|---|---|---|---|---|---|---|---|---|
| thinking and thought | 79 | 206 | 193 | 26,915 | 102,531 | 435,094 | 42,316 | 122 | 15,986 |
| weighing and taking account of | 49 | 74 | 65 | 8,981 | 33,883 | 152,415 | 50,062 | 19 | 9,046 |
| reasoning | 15 | 27 | 27 | 3,867 | 14,336 | 102,556 | 10,925 | 17 | 3,764 |
| supposing and imagining | 15 | 20 | 19 | 2,596 | 9,050 | 117,184 | 4,789 | 10 | 3,058 |
| meditating and pondering | 13 | 27 | 27 | 2,674 | 9,685 | 25,754 | 1,854 | 19 | 2,761 |
| the mind on | 2 | 3 | 2 | 268 | 601 | 22,333 | 1,107 | 7 | 565 |
| conflicting thoughts | 1 | 1 | 1 | 163 | 515 | 2,895 | 203 | 7 | 254 |
| giving thought | 1 | 1 | 1 | 95 | 290 | 0 | 994 | 0 | 244 |
| once regarded | 1 | 1 | 1 | 154 | 461 | 11,509 | 1,353 | 0 | 284 |
| setting your mind | 1 | 1 | 1 | 171 | 540 | 18,317 | 1,010 | 0 | 275 |
| **total** | **177** | **361** | **337** | **45,884** | **171,892** | **888,057** | **114,613** | **201** | **36,237** |

All text sizes are in characters. "Verse structure" is the verse_lexical rows of those verses. The old observations in scope hold 92,924 characters (the longest is 2,556). There are 87 matches at 3.3. Thought's 2.1 rows (194 in all) are opened only for reasoning: 60 pairings, 3 double meanings, and one each of qualifier, entity and direction.

**What the numbers say:**
- **The lexicon is the volume.** It is 888,057 characters against 45,884 of verse text. One code, G3056 (logos), holds 72,237 characters, and the 115 codes hold 514,830 between them. A package that carries the lexicon whole is mostly lexicon.
- **The output is small.** All of B1 for thought is 36,237 characters.
- **The units are small and uneven.** Most words stand in one or two verses. Four subgroups have one word each, while one subgroup has 79 words and 193 verses.
- **The instructions per item are short** (135 to 1,029 characters). The weight is in the rules the reading must keep, specification v5 sections 2, 2A and 3. Those are 37,441 characters if sent whole, and that is what made the earlier API use costly.

## 2. The read types

Each type is a different read: a different unit, different input, a different result, and a different place it is written. "Calls" is the number of reads for thought, where it is known.

| # | step | read | unit | input (what, thought's size) | result expected | written by |
|---|---|---|---|---|---|---|
| R1 | A step 2 | name and define each subgroup; set aside a surface not a member | collection (10 subgroups, 33 surfaces) | the surfaces of each seed group with their WordNet relations and sense heads; small | per subgroup: name and one sentence; per surface: placed or set aside with reason | GroupRecord → collection_subgroup, collection_subgroup_surface, surface_event |
| R2 | B1 | read a word in each of its verses | word (177) | for each occurrence: the verse text, the verse's structure lines, the sense head; the meaning tree once; lexicon only as needed (section 3) | one observation for each distinct use, with the occurrences it holds; a face where the use departs | LayerRecord S1 → ib_observation, ib_node, ledger |
| R3 | B1 | answer an old observation | old observation (201; 92,924 chars) | its text and nodes, the verse it names, the new B1 observations of its words | re-apply, restate, consume, split, carry forward or delete, with the reason | LayerRecord S1 (old-observation rows) |
| R4 | B2 1.1 | gather the word readings into senses | subgroup (10) | the subgroup's B1 observations (largest 79, 15,986 chars) with codes and sense heads | senses, each a name, a text and the list of B1 observations it carries (each exactly once) | LayerRecord 1.1 |
| R5 | B2 1.2 | what the codes of a sense say | sense | the sense, and the lexicon entries of its codes (here the lexicon is the point) | one enrichment text per sense | LayerRecord 1.2 |
| R6 | B3 2.1 | what stands with the subgroup in each verse: pairing (per partner collection), qualifier, entity, direction, double meaning | ledger row (reasoning: 66) | the shared verses' structure lines with positions and the partner's collection, the WordNet control, the B2 senses | findings, each with the verses it holds in | LayerRecord 2.1 |
| R7 | B4 | judge what is still unmarked | old observation left after R3 and R6 (count known only after them) | its text and nodes | evidence, inner being, or neither (delete) | LayerRecord 2.1 (sweep) |
| R8 | B5 | check truth and coherence of the evidence | subgroup | all its evidence observations with their verses | a list of what is untrue or contradictory, for repair | repair through LayerRecord; check by LayerCheck |
| R9 | C1 3.1 | the elements of a behaviour | subgroup (10) | the evidence by marker (B2 first, then B3, B1) and the verse text (largest: 26,915 chars) | findings on the nine items, each with traces and a role per occurrence | LayerRecord 3.1 |
| R10 | C1 | answer an old inner-being observation | old observation | its text, nodes and the evidence it could rest on | accept with trace, restate, consume, merge, split, delete | LayerRecord 3.1 |
| R11 | C2 3.2 | the behaviours of the collection | collection (1) | all C1 observations | behaviours gathering their elements; every C1 observation gathered or declared not | LayerRecord 3.2 |
| R12 | C3 3.3 | what a match across collections shows | match (87) | the observations the match comes from and the shared verses | one observation per match: one behaviour or a variety, or none with reason | LayerRecord 3.3 |
| R13 | C4 | repair an inner-being observation that fails the trace | failing observation | the observation and the evidence of its subgroup | trace found, restated, or deleted with reason | validation actions |

## 3. How each read is packaged

The same principles apply to every type. They are what make a model call productive, whatever the server.

1. **One fixed instruction block per read type, never the whole specification.**
   - It holds only that type's ask, the rules that type must keep (named per type from specification v5 sections 2, 2A, 3), and the exact output shape as a schema.
   - It is the same for every call of the type and is cached: API prompt caching charges about 10% for a cached read. Ollama holds the model loaded (`ollama.keep_alive`). Whether Ollama reuses a repeated prefix in this setup is not verified.
2. **The data as compact fields, not prose, and only what the type uses.**
   - R2 needs the verse text, the occurrence's structure line, the sense head and the meaning-tree lines.
   - It does not need the full LSJ and Mounce entry. In the raw tables that is 73% of the volume (888,057 of the 1,220,446 characters across verse text, structure, lexicon and meaning tree).
   - The present pull (`_lexicon` in `iba/app/lib/layerreading.py`) already cuts the meaning range, LSJ and Mounce to 700 characters each. What the present pull lacks is a package per read: one step's pull mixes several reads, puts every verse of the subgroup in the header, and carries each row's ask but not the rules the read must keep.
   - R5 is the read that carries the lexicon, once per sense.
3. **Small units batched, large units split.**
   - The one-verse words (most of thought) go several to a call under one instruction block.
   - A word or subgroup above a size limit is split, for example R9 for "thinking and thought" by sense.
   - The limits are settings in config, set from the pilot, not guessed.
4. **The output is the recorder's file.**
   - The answer is the same JSON that LayerRecord already takes, so the existing checks refuse a bad one.
   - A refused answer is retried once with the refusal message, then left open on the ledger with its reason.
5. **Each read is timed and sized, with limits in config.**
   - Every call logs its input size, output size and seconds in `ai_call`.
   - A call over its time limit, or a run of failures, stops the run with the read named (B:124).
   - A long run is started outside the session with a progress log (B:125).
6. **The order follows the specification.** R2 to R10 per subgroup, then R11, then R12 and R13. Each read pulls only its own unit's data, with indexed lookups. Nothing is loaded whole and scanned.

## 4. What is not known until it is tried

- Whether a model on the Ollama server (`qwen3:30b`, `ollama.num_ctx` 4096) can do each type well. R2 with batching and an R2 package that fits 4096 tokens both have to be shown.
- Tokens per call for each type. The figures above are characters.
- How many old observations are still left at R7.

A meaningful test covers each read type, not one word. The pilot should be one subgroup taken through R2 to R9 on a copy: "meditating and pondering" (13 words, 27 verses, 19 old observations) is small and complete. Its output should go side by side with what is recorded for it, with the size and seconds of every call.
