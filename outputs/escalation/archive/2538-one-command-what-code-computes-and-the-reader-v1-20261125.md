# #2538: one command for stages 1 to 4 — what code computes, what needs a reader, and the decision (v1, 2026-11-25)

Written by Claude, session 760131f7 (Developer Mode), as step (1) of the plan in #2538 v38. Nothing is built.
Sources: specification v5 (`outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md`), `cfg_setting layer.reading`
(the steps, items and their `asks`), `cfg_setting layer.interventions`, the live ledger `collection_layer_item` for thought (id 56),
the transcript of session 43742f37 (2026-11-25 13:46 to 13:59). Open escalations cross-checked: #2544 (working mode), #2545 (parked).

## 1. The requirement, in your words

- 2026-11-21: "the analysis process must be codified in such a way that it can run 169 times over many days and even months and every process and output will work exactly the same. it also need to provide for self learning, and evaluation, but in each case the self learning must be baked into the code and not live at all in scratch folders."
- 2026-11-25 13:53: "I am not interested in you orchestrating every run, it is not what I asked for, and it is contrary to everything built in this study."
- 2026-11-25 13:56: "wrong.  I want the stage 1 - 4 to run with a command taking input as a collection, including everything inside, with all the controls and checks that a normal method would require."

The "wrong" of 13:56 answered Claude's proposal of 13:53: a driver verb `LayerRun` whose read step calls a Claude model through the API. #2538 v38 recorded it as "not an API model as reader". That reading is **inferential**: your words reject the proposal, and do not say which part of it.

## 2. What each step needs: computed from data (C) or judged by reading (R)

"C" = a rule over stored data gives the answer, the same every run. "R" = the answer is a judgement of meaning written in words (the "Reading, how" of each step in specification v5; the `asks` of each item in layer.reading).

| Step | C: code computes from stored data (source; config) | R: needs a reader |
|---|---|---|
| A1 GroupPull | all of it: surfaces of the collection, WordNet network groups and pairs, seed groups (surface_relation, surface_network_group; surfaces.relation_scope, surfaces.relation_pair_rules) | nothing |
| A2 GroupRecord | adopting the WordNet seed groups as subgroups; a surface WordNet lacks as its own subgroup; surface_event rows | naming and defining each subgroup from its members (B:129); setting aside a surface plainly not a member in meaning |
| B1 words | the words (surface with lettered Strong's code), every occurrence, morph, verse reference, lexicon entries, function-word exclusion with negators and connectives kept, node columns, ledger rows (verse_lexical, verse, strong_meaning_tree, strong_lexicon; layer.reading word-sense); old observations in scope by node, verse, surface or code; exact-text duplicates | the sense of each occurrence in its verse; which occurrences are used the same way (one observation) and which differ or are a face; the text of each observation; each old observation's answer (accept, restate, consume, split, delete) except exact duplicates |
| B2 1.1 / 1.2 | the constraints (every B1 observation in exactly one sense), the node union, the traced nodes, the codes of each sense | the senses themselves, driven by meaning in context (your ruling 2026-11-25); the 1.2 definition from the lexicon (RW-04) |
| B3 2.1 | words standing with the subgroup in each verse, side and distance from stored positions, the partner collection, the WordNet control (both, WordNet only, verse only), the codes a surface carries across verses (double meaning), entity surfaces named in the verse | the word a negator or qualifier reaches, what a qualifier gives by the grammar, pronoun reference, direction of travel, whether verses show the same finding or a different one, the text |
| B4 sweep | which old observations are still NULL | evidence, inner being or neither, for each |
| B5 evidence validation | every structural check (marked, live node, required columns, no dead trace, exact duplicates, coverage) | truth and coherence (specification v5 L1: no code check of content exists) |
| C1 3.1 | the pull by marker, the trace structure, the gate | all of it: the elements of a behaviour from the evidence |
| C2 3.2 | the pull, the gather constraint | all of it: the behaviours of the collection |
| C3 3.3 | every unique match (observations whose nodes carry more than one collection; the combinations; the shared verses); the partner gate | whether the verses of a match show a variety of implications or a single behaviour |
| C4 inner-being validation | the structural checks (IB-07 trace, no dead evidence) | repair: finding the evidence, restating |

**Finding.** Every step that writes an observation has an R part, except A1. Every item in layer.reading is written as a question to a reader (`asks`). The code built so far holds the controls (gates, pulls, ledger, recorder checks). Nothing in it produces an answer: in every run on thought, the answers were written by a session.

## 3. Volume, measured (thought, live ledger, 2026-11-25)

S1 word-sense rows 177; old observations answered at S1 181 and at 1.1 20; 1.1 groups 10; 1.2 enrichments 8; 2.1 rows 194 (66 open); 3.1 rows 7; 3.2 rows 1; 3.3 rows 87. Total: 685 reading answers for one collection, against 169 collections. Token cost per answer is not measured.

## 4. The conflict to decide

A command that runs "everything inside" with no session must have something inside it that answers the R parts. Three standing rules bear on whatever that is:
- **B:127** (collection-taken-through-whole-path-with-researcher) excludes a model, or bulk or templated output, as the producer of the study result.
- **B:132** (collection-reading-runs-in-layers) and **B:136** (collection-validation-follows-stage-4) name Claude as the reader who decides, with you scrutinising.
- **Your 2026-11-21 words, "every process and output will work exactly the same".** A rules-only command meets them to the letter. A model reader repeats the process, inputs and checks, but not the exact wording of its answers.
- **#2544** records that you now use Claude for pointed tasks you can control and validate. Section 3's volume is far beyond what you can scrutinise answer by answer.

## 5. The options

**Option 1: rules only, no reader.** The command computes every C part and writes structural evidence observations from templates. Examples: "in Ps 94:11 thought (H4284) stands 2 words after vain (H1892), of collection vanity"; the occurrences of each word grouped by Strong's code and morph; the double-meaning lists; the 3.3 match lists.
- Output identical every run.
- No senses (B2), no inner-being content (C1, C2), no old-observation judgements. The command stops at each R gate, so it does not deliver stages 1 to 4.
- Needs B:127 amended to accept templated structural observations as evidence.

**Option 2: rules plus a reader inside the command.** Option 1's computation runs first and becomes the reader's input and its check. Inside the same run, an in-app reader answers each ledger row one at a time: a Claude model through the API, held as a service in config under B:124.
- The recorder's existing checks refuse a bad answer. The row is retried, then left open with its reason.
- The run resumes from the ledger.
- Learning lives in the database: every refusal, every correction you make, and every rule added is fed to later answers.
- Delivers stages 1 to 4 from one command.
- Not byte-identical between runs.
- Needs B:127, B:132 and B:136 amended: an item-by-item reader under the app's controls is permitted, bulk and one-shot output stay excluded, and the app's reader reads while you scrutinise.
- **This is in substance what was proposed at 13:53 and you called "wrong".**

**Option 3: the command pauses at each R part for a session to answer.** This is the orchestration you rejected at 13:53. It is listed only so the set is complete.

## 6. Recommendation

Option 2 is the only one that meets "a command taking input as a collection, including everything inside" in full. If your "wrong" rejected a model reader, then no code can deliver the R parts. The honest choice is then Option 1, with the command leaving the judgement content of stages 1 to 4 undone, and I would not present it as delivering them.

Either way, the first build step is the same and is useful under both options: the C column of section 2 as one verb, with its tests on a copy of thought. Then a pilot of the chosen option on one subgroup of a copy, with its token cost measured, before anything else.

## 7. Decision sought

1. Option 1 or Option 2 (or your correction of section 2).
2. If Option 2: confirm that B:127, B:132 and B:136 are to be amended as stated in section 5, and that the Claude API is the reader.
