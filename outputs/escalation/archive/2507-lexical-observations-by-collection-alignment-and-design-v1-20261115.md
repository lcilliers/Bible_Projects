# #2507 The lexical observations by collection: what is in place, what is not aligned, and the design (v1, 2026-11-15)

Status: read-only audit and a design for the researcher's correction (B:105). Nothing is changed. Sources are named per statement. "Lexical observation" is used in the researcher's sense (#2507 v1, verbatim): an observation about the structural composition of the verse, explicitly not inner-being aware.

## 1. What the record says the lexical observations are

- `verse_lexical` is the structural composition of the verse and "can never carry an inner-being concept" (researcher ruling, #1383 v23, `iba/docs/1383-verse-lexical-window1-full-build-specification-v1-20260904.md`). The next step is the observations about that structure, entered now through the collections (#2507 v1).
- The first mechanism, `lexical.enrich` (`verse_lexical_note`), was retired on 2026-09-16 (#1706 Phase B) because the `ib_observation` architecture superseded it, and `lexical.run` on 2026-09-07 because it was built on books and passages (#1549). The replacement was the verse-reading stage: `lexical.meaning` (word level) and `lexical.relational` (relations), split on the researcher's word of 2026-09-23 (#1860): "the relational process depends on the word work, and doing it in the same session can only result in errors."
- The question catalogue marks the lexical evidence itself: dimension M0 is "lexical/textual evidence, feeds the 12 but is not itself one" (`cfg_column wa_obs_question_catalogue.dimension`). Its scope `Word/term (lexical)` holds 26 active questions: M0.1 name and naming, M0.2 kind, M0.3 boundary, M0.4 grammatical form, M0.5 lexical and semantic analysis (root meaning, grammatical form, semantic range, aspect, structural opposite, Testament context, coinage, divergence nuance).
- The researcher's layer 2 has two sets (#2507 v1): the lexical-structural set (part of the lexical enrichment) and the inner-being observations about it (the claims process). Faces are identified and clarified in the lexical work; what they do for the inner being is layer 2 (#2463 v22).

## 2. What is in place

| Item | State | Evidence |
|---|---|---|
| The structure itself | Sound: 544,667 live rows, every verse and span covered, no unknown code, no duplicate position | `verse_lexical` checks of 2026-11-15 (#2507 v3) |
| The member occurrences of a collection, and the typed neighbours in each verse (member, entity, negator, other collection, qualifier candidate, connective) | Built | `lib/collectionevidence.py` `build_pairs` (#2502) |
| The kinds that already mean lexical work | Exist | `ib_observation.tag` term ("the term's meaning in context against its lexicon entries, its surface variants and related words"), face, link, use (`cfg_enum` tag guidance); they are the kinds `reading.observation_parts` already allows |
| The ledger, whole-file recorder, nodes built from the data, and the check that validates them | Built (#2505) | `lib/layerreading.py` |
| The questions that guide the text | Exist: 26 lexical-scope prompts | `wa_obs_question_catalogue` scope `Word/term (lexical)` |
| The word-level and relational generators | Exist, cluster based | `lib/versereadinggenerate.py`, steps `lexical.meaning`, `lexical.relational` |

## 3. What is not aligned

1. **Entry.** `lexical.meaning` and `lexical.relational` are scoped by cluster (`VerseReading.ps1 -ClusterCode`, `RelationalReading.ps1 -ClusterCode`, `Run-Stage1Batch.ps1 -ClusterCodes`); none takes a collection. Their text says "per-cluster, pre-subgroup Layer 2" and "cluster-agnostic (every M-code word in the verse)".
2. **Gates.** The relational step refuses a verse unless every M-code word has a committed word-level observation, and `lexical.relational` carries the cluster status transition (`t_cluster_assignment_completed` to `ready_for_subgroup_allocation`). Both are cluster concepts that no longer start anything.
3. **Rules.** Both steps are active and all their method rules are inactive (`lexical.meaning` 10, `lexical.relational` 13, `lexical.enrich` 15): active steps governed by no rule. The 98 method rules deactivated on 2026-10-24 (`DEVMODE-2268-CONFIG-ALIGNMENT`) and the 16 on 2026-11-13 (`DEVMODE-2495-RETIRE-CLUSTER-SUBGROUP`) were the cluster-era guidance; nothing replaced it for the lexical observations.
4. **Coverage.** The verse-reading stage holds 1,229 occurrences of 544,667 (the M-coded words only), none after 2026-09-23. Of the 394 member occurrences of `thought`, 282 have no lexical node with a role and 3 verse-reading observations touch it.
5. **Nodes without a role.** All 6,142 nodes of the verse-reading stage have `role` NULL, while B:130 requires a role and the node roles (`reading.node_roles`: characteristic, qualifier, object, relational_target, enactment, standalone) are all inner-being roles. No role exists for a node of a lexical observation.
6. **My lexical gate is wrong.** `lib/layerreading.py` `lexical_gate` counts a node with a role from `reading.node_roles` on a stage that is not a layer. That test is the inner-being test: it ignores every verse-reading observation (no role) and would accept an engagement observation (inner-being) as lexical. The gate must test that the lexical observations exist, not that an inner-being role was given.
7. **Layer 2 as I built it mixes the two sets.** The aspects pairing, qualifier, entity, direction, group-relation and double-meaning are all treated as inner-being observations on top of one gate. Their structural part (which words stand with the group in the verse, connectives, negation and its reach, entity and pronoun references, qualifier presence, the divergent face of a word) is lexical work and has no process of its own; only the question of what these do for the inner being is layer 2.
8. **Guidance still saying the old thing.** The catalogue column text for `scope` says the lexical scope is "NOT selected by any live stage's query" (checked 2026-09-21, before #1860); the 77 reading method rules RG-01 to RG-25 and RS-01 to RS-10 describe one pass that does both kinds of observation (#2507 v2 and the scan `outputs/escalation/2507-legacy-scan-v1-20261115.md`).

## 4. The design

**D1. The lexical observations are made by the machinery just built, as a layer before layer 1.** `cfg_setting layer.reading` gains a layer 0 with two steps and the stage `lexical` (a new `ib_observation.stage` value); the ledger, the working file, the recorder, the check and the group on the node are used as they are, generalised for the new items. The gate of step 1.1 then becomes "step 0.2 is closed", replacing `lexical_gate`. The cluster-based generators are not reused.

| Step | Item | Kind (existing) | Subject and grain | Nodes |
|---|---|---|---|---|
| 0.1 words | word-lexical | term | each member surface and Strong's code of the collection (a lettered code, never the bare lemma, B:113 and RG-21): what the word is by the lexical prompts (name, kind, boundary, grammatical forms, root and semantic range, aspect, structural opposite, Testament context, coinage) | every occurrence of that surface and code |
| 0.1 words | word-face | face | each occurrence whose meaning diverges from the usual sense of the word (M0.5.11, `surface-gloss-divergence`); none allowed with a reason | that occurrence |
| 0.2 structure | verse-structure | link | each verse that holds a member occurrence: how the member words stand in the verse by the stored data (the typed neighbours with side and distance, connectives, negators and the words they reach, entity and pronoun references, qualifier presence); no inner-being statement | the member occurrences and the neighbours the observation names |

The inner-being set stays as built (layer 1 and 2 steps 1.1, 1.2, 2.1); step 2.1's observations cite the lexical ones as their base.

**D2. A role for a lexical node.** Add one group to `reading.node_roles`, `lexical` with the value `lexical`: the word is read lexically and carries no inner-being role. B:130's requirement of a role holds, the node checker passes, and the gate can test for it. The existing verse-reading nodes keep NULL until the collection that carries them is read.

**D3. The cluster-based lexical steps.** `lexical.meaning`, `lexical.relational`, `VerseReading.ps1`, `RelationalReading.ps1` and `Run-Stage1Batch.ps1` are retired (inactive, scripts archived), as their method rules already are; `lexical.build` and `lexical.readiness` stay, as the base data.

**D4. Guidance.** The 26 lexical-scope prompts are the prompts of step 0.1 (read into the working file, never answered by force, RG-17); the stale catalogue column text is corrected; the method rules LR-01 to LR-05 gain the lexical items; the behaviour rule on lexical and claims readings (`lexical-and-claims-readings-are-separate`) names step 0.2 as its gate.

**D5. What is not decided here.** Whether the 6,142 existing nodes of the verse-reading stage are re-read into the lexical stage by the collection that carries them (as the prior documents are, #2498) or left as history; which of the catalogue's other 'Verse' and relational questions the verse-structure observation draws on.

## 5. Decisions for the researcher

| # | Decision | Recommendation |
|---|---|---|
| 1 | D1: layer 0 through the new machinery (A), or adapt the cluster-based `lexical.meaning` and `lexical.relational` to take a collection (B) | A: B keeps the cluster gates and a second recorder, and the researcher's split of word and relational work is kept by the two steps 0.1 and 0.2 |
| 2 | D2: the role `lexical` | Yes |
| 3 | D3: retire the cluster-based lexical steps and scripts | Yes, with the same archive route as the Concept-Edit tool |
| 4 | The grain of 0.1: one observation per surface and lettered code (A), or per surface only (B) | A, by B:113 and RG-21 |

## 6. If approved, the build

Config: `layer.reading` layer 0, the stage, the role group, the items, the gate; the method rules; the retirement of the cluster-based steps. Code: `layerreading.py` generalised (derive and expected nodes for the three items; the gate replaced), the pull evidence for 0.1 and 0.2 from `build_pairs` and the lexicon tables, the checker. Tests on a copy as in #2505, the USER-GUIDE and BUILD entries, then the first run on `thought` by the ledger: the 282 uncovered occurrences become the ledger rows of step 0.1.
