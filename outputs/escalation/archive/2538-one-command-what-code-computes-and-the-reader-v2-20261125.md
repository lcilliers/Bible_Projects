# #2538: one command for stages 1 to 4 — what the base data already give, what is left to read, and who reads it (v2, 2026-11-25)

Written by Claude, session 760131f7 (Developer Mode). It replaces v1 (in `outputs/escalation/archive/`), which the researcher judged not thought through (#2538 v44, his words there). Nothing is built.

## 1. What v1 got wrong

- **It marked steps as "needs a reader" without checking what the base data hold.** The lettered Strong's codes, their sense heads, the negator flag and the party kind are stored, and v1 did not look at them.
- **It recommended the API as the reader without reading the cost record of the earlier API use.**

## 2. The cost record of the earlier API use (measured)

`outputs/cost-history/api-exports/`, all API usage by month:

| month | uncached input | cache write | cache read | output | input share |
|---|---|---|---|---|---|
| 2026-05 | 4,928,733 | 347,018 | 896,961 | 1,966,061 | 76% |
| 2026-06 | 6,247,135 | 6,232 | 17,782 | 3,518,282 | 64% |

- **Input is most of the cost, and it was almost never cached.** The exports do not separate instructions from data within the input, so your 70% cannot be confirmed exactly from them. Nothing in them contradicts it.
- **The model also skipped what prose instructions asked.** BUILD #315 records a systematic gap of this kind. Your instruction then, recorded at #1831, was that "the expected answer for each question and strong had to be pre-drafted as part of the stage 1 code", and it was never built.
- **Conclusion:** the method's long prose `asks` were not designed to pass productively through the API. Sending them through it as they stand would repeat that experience.

## 3. What the base data already give (measured on thought, collection 56)

- **Words and senses.** Thought has 177 words (a surface with its lettered Strong's code) on 33 surfaces and 110 base codes, with 361 occurrences. **Every one of the 177 has a sense head in `strong_sense`.** The lettered code is STEP's own choice of sense at each occurrence, so the sense of each occurrence is stored, not read.
- **Faces and double meanings.** 23 of the 33 surfaces carry more than one code. Each such surface is a double meaning, and an occurrence under a code other than the surface's usual one is a face. Both can be computed.
- **Stored in `verse_lexical`:** position, morph, `is_negator`, `party_kind` (a named divine, human or non-human party), `narrative_morph`, unit role. With these come the partner collection of each word in the verse, and the WordNet control from `surface_relation` and `surface_network_group`.
- **Not stored:** syntax. That means the word a negator or qualifier reaches, what a pronoun refers to, and the direction of travel by the grammar.
- **Finding raised:** the recorded description of `verse_lexical` claims a sense column it does not have (#2559).

## 4. The split again, after checking the data

| Step | Computed from stored data | Left to read |
|---|---|---|
| A | WordNet seed groups as subgroups; a surface WordNet lacks as its own | the name and one-line definition of each subgroup (10 for thought) |
| B1 | all of it: one observation for each word-sense (lettered code with its head), its occurrences as nodes; faces from the codes | nothing, if a stored fact recorded with its nodes is accepted as the observation (section 5) |
| B2 | seed senses: lettered senses with the same head, or joined by `strong_related` or WordNet, grouped; nodes and traces | confirming or splitting the seed senses by meaning in context (one judgement per subgroup) |
| B3 | partner words with side and distance; negator present; named parties; double meanings; WordNet control (both, WordNet only, verse only) | what a negator or qualifier reaches, pronouns, direction. These go away only if a syntax source is brought in as base data, which is a separate decision. |
| old observations | exact or near restatements of a computed fact are consumed; the rest is listed | each one that is left (thought: 201 in scope; how many are left after computing is not measured) |
| B4, B5, C4 checks | all structural checks | truth and coherence of what was read |
| C1, C2 | pulls, traces, gates | all of it: the inner-being content (thought: 7 subgroup rows, 1 collection row) |
| C3 | every unique match, with its verses | whether the verses show one behaviour or several (thought: 87) |

**What this changes.** Most of the evidence layer is the base data recorded with nodes. Reading is needed in a bounded set of places, most of them in stage 4. As things stand, the method has a reader write prose for each word that restates the sense head and the verse. That is the costly part, and it adds little the data do not already hold.

## 5. Two points for your ruling

**(1) Can a computed evidence observation stand?** This means a stored fact (the word, its lettered code, its sense head, its occurrences; a partner word and where it stands) recorded as an observation with its nodes and a sentence generated from the fields.
- B:127 excludes "templated observation text" as a substitute for reading.
- My reading: that ban is aimed at judgement made by template, not at recording what the base data state.
- If you rule this way, B1 and most of B3 need no reader at all, and B:127 is re-worded to say so.

**(2) Who reads what is left.**
- **(a) The command reads nothing itself.** It runs the whole collection in one go and writes one reading packet of only the residual items, each with its data pre-drafted and the expected answer shape stated. One answer file goes back through the same command, with all its checks. Whoever answers (you, or Claude as a pointed task under #2544) answers a bounded list. Nobody steers the steps.
- **(b) An API reader for the residual only, built for the API.** Compact structured input, a per-item checklist in code, instructions cached, batch calls. It still needs B:127, B:132 and B:136 amended, and a measured pilot.
- **No option removes the reading of stage 4.** The inner-being content is a judgement, and no rule over the data produces it.

## 6. Recommendation and what is sought

- **Build the computed layer first,** as one command on a copy of thought: A seed groups, B1 complete, B2 seed senses, the computed part of B3, the consumption of old observations that restate a computed fact, the checks and the ledger. It is needed under every option.
- **Measure what is left.** The command then reports the residual: how many items, of what kind, and how many old observations remain.
- **Then choose 2(a) or 2(b)** on those measured numbers, not on an estimate.

Sought now:
- your ruling on point (1);
- approval to build the computed layer on a copy of thought and report the measured residual.
