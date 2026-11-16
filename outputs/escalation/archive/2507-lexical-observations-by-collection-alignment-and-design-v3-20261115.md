# #2507 The lexical stage by collection: what the record defines, what exists, how the old work is amalgamated, and the control list of change (v3, 2026-11-15)

Status: read-only audit and design for the researcher's correction (B:105). Nothing is changed. v1 and v2 are archived, not approved. v2 found what to change by the names of files and configs; this version is built from the content of the record and of the tables, and says where it is inference.

**What was read for this version, in full:** the 99 active method rules of the steps `reading.*`, `collection.*`, `lexical.*`, `draft_apply.apply`, `node_check.report`, `spine.check`, `raw.verses`, `cluster.assign`; the `cfg_table` and `cfg_column` purpose text of `verse_lexical`, `ib_observation`, `ib_node`, `surface_term`, `collection`; the enums for stage, window, tag, role; #1383 (the specification and its correction banner), #1451, #1706 progressive reading; the whole history of #2463 and #2354; the catalogue rows of dimension M0; the function lists and imports of the old modules; observations and nodes counted by stage and role. **Not read in full:** the 115 active behaviour rules beyond those named, the 328 settings beyond those named, `iba/app/USER-GUIDE.md` beyond sections 6 and 7, #1706 full pipeline checklist, #1824, #1860 and the 16 `reading.narrate` rules' relevance to this stage (read: they are about the narrative, not this stage). Section 11 lists what is still to be digested and how.

## 1. What the record defines (the stage, its layers, its place)

1. **The stage exists and was defined: Window 1, "Stage 1", the lexical stage** (#1383 specification title: "Verse-lexical Window 1 (Stage 1)"; #1451; rule `lexical.readiness` 69, researcher ruling #1606 2026-09-15: "lexical readiness is a precursor for the lexical reading stage, which is a precursor for the sub group"). It sits between the base data and the inner-being analysis (Window 2). v2's D10 ("a stage of its own") was wrong: the stage is old and defined; what is missing is that the current settings and rules do not name it.
2. **Window 1 has two layers** (#1383 v23 banner; the researcher ruled that both are Window 1 whatever their method): **Layer 1** is `verse_lexical`, the structural composition of the verse, built mechanically (`lexical.build`). **Layer 2** is the lexical enrichment: the judgement-bearing findings about that structure, each a "note" with a type: idiom, pronoun_resolution, noun_relational, noun_severity, chain, connective, related_word, polarity, entity_link, inert, structural_pattern (later also recurrence_role_shift, verb_argument), and a resolution status (resolved, unresolved, checked_empty, unclassified, not_supported_this_language). Layer 2 is verse-scoped, and reads an adjacent verse only to satisfy one need, recording `unresolved` where it cannot (#1451). Window 1 "can never carry an inner-being concept" (#1383 v23).
3. **The mechanism for Layer 2 was retired and nothing replaced it.** `lexical.enrich` and the table `verse_lexical_note` (175 live notes in total: related_word 104, inert 23, connective 11, pronoun_resolution 10, entity_link 7, idiom 5, and a few others) were retired on 2026-09-16 (#1706) in favour of observations; the replacement was the verse-reading stage, which was built on clusters and mixed lexical and inner-being questions (section 3.3). So **Layer 2 of Window 1 has no process today.** The researcher's statement of 2026-11-14 is that exactly this lexical work is incomplete and that the claims layers rely on it (#2463 v18 (h), §5.5).
4. **The old pipeline had four stages that stratified the work on the words** (#1706): Stage 1 verse-reading (lexical, word level then relational), Stage 2 char-subgroup (forming groups of words), Stage 3 char-reading (reading each group), Stage 4 char-answers (the catalogue battery), and a fifth, synergy, designed but not built. The collection layers are the refinement of these: **my reading, to confirm**: Stage 1 maps to the lexical stage, Stage 2 to claim layer 1 step 1.1 (the groups), Stage 3 to 1.2 and layer 2, Stage 4 to the claim formulation, Stage 5 to what follows layer 2.
5. **The surfaces are stratified before any of this** (the surface cycle, #2361 and #2354, modules 0 to 5). `surface_term.surface_group` (module 1) holds four groups: **behaviour**, **inner_being_state** (the two that are "the study of the inner being": bases and collections are built for them, "collection a"), **entity** ("collection b") and **other** ("collection c"); b and c stay untouched until the researcher assesses them. Counts: behaviour 1,204; inner_being_state 2,180; entity 717; other 2,068; 56 not yet judged. The 169 collections hold the surfaces of a.
6. **Two uses of "layer 1" and "layer 2" collide.** Window 1 Layer 1 and Layer 2 (the lexical stage, #1383) are not the researcher's claim-reading layer 1 and layer 2 (2026-11-14: groups, Strong's enrichment, pairings). My build named its stages `layer-1` and `layer-2` and v2 called the lexical stage "layer 0". That vocabulary has to be settled (D11).

## 2. The amalgamation: what the past did, what is kept, where it goes

The researcher's concern is that the new process must be a deep amalgamation of the old. This table takes each piece of the old work that I found, says what it contributed to the study, and where it lives in the new process. "Verified" means I read the code or text; "inference" means I did not.

| Old piece | What it contributed | Where it lives in the new process |
|---|---|---|
| Stage 1 word-level battery, M0.1 and M0.5 (14 questions: name, direction or constitutional implication, grammatical form, root meaning, form, semantic range, aspect, structural-opposite term, person-type term, supplication term, Testament context, coinage, divergence nuance) | the lexical reading of every word, per occurrence, grounded in the three meaning sources (RG-08) | **lexical stage, word items** (section 3). Verified: the 14 questions are the lexical ones. |
| #1706: "the first read of a verse must answer these questions for every M-code word, not only the pass's own home word"; "no pass re-derives what an earlier pass found" | a verse is read lexically once for all its words and later readings build on it | the lexical stage reads **per verse for every member occurrence of the collection**; a later reading reads it into focus (RO2, RW-09) |
| #1706 §4.5: nothing asked for the alternative meaning (the nuance where the surface diverges from the gloss) | faces | M0.5.11 and the face observation; RG-09 already states that identifying the face is lexical work |
| #1706 §4.6: the qualifier role was lost (a "godly" before "grief") | qualifiers | the structural reading of the verse (section 3.2) names the qualifier candidate; what it gives the characteristic is claim layer 2 (RG-04) |
| Stage 1 relational half (M0.6.5, M0.6.6, D7.7.1, M0.7, M0.8.1) | the relation between the words of the verse | **split**: the structural part (how the words stand, M0.6.1, M0.6.5, M0.6.6) is the lexical stage; the part that is about the inner being (M0.7, M0.8.1, D7.7.1) is claim layer 2. Verified from the question text: M0.7.x asks "what inner-being response", "constitutional level", "movement toward God". |
| #1383 Layer 2 note types (idiom, pronoun_resolution, noun_relational, noun_severity, chain, connective, related_word, polarity, entity_link, inert, structural_pattern, recurrence_role_shift, verb_argument) | the definition of what a lexical enrichment holds | the **items of the lexical stage** (section 3.1); these were the content definition and have been lost with the retired table |
| `verse_lexical_note` (175 rows) | the only lexical enrichment ever written | adopted: each note becomes the answer to the matching item for its occurrence (inference: they are few; a count by collection is made at build) |
| 5,522 live verse-reading observations on 6,142 nodes (M-code words only, cluster keyed, no role, 4,772 with a collection) | the word-level and relational readings of the M-coded words | **adopted, not left as history** (section 9) |
| `stage1coverage.expected_nodes` (verified: the (verse, strong, question) triples Stage 1 should attempt, computed from the data without the model; validate_coverage reports missing, unexpected, over-count) | deterministic completeness | the same idea is the ledger and `LayerCheck` built under #2505; the lexical items use it. Nothing is lost by retiring the cluster version if the lexical items' expected nodes are derived the same way (a build test). |
| `recordingpass.py` (712 lines: occurrence resolution, question and tag validation, same/broaden/new dedup, keyword matching) | the recording engine of the old stages | **not part of the dead chain**: `observationrecord`, `draftapply`, `strandreading` and my `layerreading` import it (verified). It stays. Its cluster-keyed parts are #2448. |
| Stage 2 to 4 (char-subgroup, char-reading, char-answers), retired by #2299 | grouping, per-group reading, the catalogue battery | claim layer 1, layer 2 and the claim formulation; the observations they left (428 nodes char-reading, 1,405 char-answers, 18 char-subgroup) are history of retired stages and stay as gathered rows |

## 3. The lexical stage: what it represents and what it produces (replaces v2 §4 D1)

### 3.1 What it represents

For every verse in which a member surface of a collection occurs, the **lexical reading** says, about the words and about the structure of the verse, only what the text, the lexicon entries and the stored structure show, never what it does for the inner being. It is Window 1 Layer 2 (section 1.2) entered through the collection (#2507 v1). It answers, per verse and per member occurrence:

- **Word items** (the words of the collection): what the word is and how it is used here: the M0.1, M0.4 and M0.5 questions (14), the face where the sense departs from the gloss (M0.5.11), the idiom or combined span, the related word, the Testament context and coinage, each per lettered Strong's code (B:113, RG-21), not per lemma.
- **Structure items** (the verse around the words): the typed neighbours and where each stands (side, distance); pronoun resolution and entity links; negators and the words they reach (adjacency is not scope: a negator beside the member word negates the content or another verb in 4 of 7 samples, #2463 v28); connectives; chains; qualifier candidates; structural patterns; noun relations. These are the Layer 2 note types of section 1.2, now as observations.
- **What it does not state**: any role, effect or implication for the inner being, any group, any claim.

### 3.2 Gap: the prompts do not yet cover the structure items

The catalogue's scope `Word/term (lexical)` holds 26 active questions. **Only 14 are lexical in the researcher's sense** (M0.1.1 to 3, M0.4.1, M0.5.1 to 9, M0.5.11). The other 12 (D5.1.1, D5.2.1, D7.1.1 to D7.4.3a, D7.6.1, X0.4.x) ask whether the characteristic is "predicated of God" or "extended by one person toward another": they are inner-being questions that sit in the bucket because #1007 classified them by the focus of the word, and the column text says the bucket is the stage-selection bucket of the retired Stage 4. The scope is therefore **not a reliable marker of lexical work**, and v1 and v2 were wrong to rely on it. The rest of dimension M0 (the 3 verse questions M0.6.1, M0.6.5, M0.6.6 are structural; M0.7 (16) and M0.8.1 are inner-being; M0.2, M0.3 are characteristic) is also mixed, and the column text of `dimension` ("M0 = lexical evidence") is stale.

What covers what, against the items of section 3.1:

| Item | Existing prompt | Complete? |
|---|---|---|
| word name, form, root meaning, range, aspect, related terms, Testament, coinage, face | M0.1.1 to 3, M0.4.1, M0.5.1 to 9, M0.5.11 | yes for words |
| function of the word in its sentence | M0.6.1 | partly |
| relation of the member word to other words of the verse | M0.6.5, M0.6.6, written for "M-code words", a cluster concept | no: must be restated for the collection's neighbours |
| pronoun resolution, entity link, negation and its reach, connectives, chains, qualifier presence and candidate, structural pattern, idiom, noun relation, verb argument | none | **no prompt exists** |

The replacement is **a list in config of the prompts per lexical item** (`cfg_setting`, the pattern already used by `reading.observe_prompts`, so no column is added to the catalogue), the 17 questions above marked by item, and **new catalogue questions written for the structure items**, drafted from the Layer 2 note types and the researcher's own list (pairings, entities, negators, connectives, qualifiers, direction). The drafted questions come to the researcher before they are registered (B:105). The column text of `scope` and `dimension` is corrected to say what they now mean.

### 3.3 What exists, what is different

| | Exists today | The lexical stage |
|---|---|---|
| Entry | a cluster (`-ClusterCode`); M-coded words only | a collection; every member occurrence |
| Content | word-level and a relational half that mixes structure and inner being (M0.7, M0.8.1) | lexical and structural only |
| Result | 5,522 observations, old catalogue tags (`answered-no-flag`, `not-related-to-meaningful-word`), nodes without role | observations in the kinds the study now uses, nodes with occurrence, collection, role (section 4) |
| Completeness | per cluster, M-coded words | per collection: every member occurrence has its items answered or stated absent with the reason (the ledger) |
| Coverage of `thought` | 3 verse-reading observations on its 394 occurrences | all occurrences |

### 3.4 Which tables and columns hold the outcome (and the others)

`verse_lexical` is **read, never written** by this stage (it is Layer 1). The outcome is `ib_observation` and `ib_node`. Column by column, from the purpose text:

**`verse_lexical`** (what the stage reads): `id`, `span_id`, `verse_id`, `strong`, `morph_code`, `position`, `surface`, `unit_surface`, `surface_kind`, `unit_size`, `unit_role` (the multi-term unit), `testament`, `is_negator`, `narrative_morph`, `gloss_consistent_in_verse`, `party_kind`: **used**. `role` (the JSON array of every cluster code of the strong, redesigned 2026-09-16): **a cluster-era column in the structural table**; it is the "role" of section 4 (i) and the value is a cluster tag, so by the #1383 v23 definition it carries a concept in Window 1; it is not read by this stage and is flagged (D12). `status`, `created_at`, `updated_at`, `deleted`: bookkeeping.

**`ib_observation`:**

| Column | Lexical stage |
|---|---|
| `stage` | new value for the stage (D11); old values stay, never used to filter (RS-04) |
| `tag` | the kind: term, face, link (and use) already mean lexical work; mapping of the note types to kinds in 3.5 |
| `question_code` | the lexical prompt the observation answers |
| `window` | `meaning` for word items, `relational` for structure items; already filled from the catalogue |
| `strong` | the code of the word observed |
| `obs_text`, `meaning` | the finding; `meaning` states what the word means here, not what it does for the inner being |
| `basis` | stated or read |
| `parts` | the structured parts; carries the **item** (word, face, pronoun, negation, connective, chain, qualifier candidate, pattern, idiom, relation) the way `reading.observation_items` carries the claim items; no new column |
| `meaning_source`, `meaning_keywords` | the lexicon source read; keywords for matching (used by `recordingpass`) |
| `status`, `supersedes_observation_id`, `run_id`, `stable_key`, `revisit_note`, `created_at`, `updated_at`, `deleted` | lifecycle, as for every observation |
| `implication`, `route`, `chain`, `parties`, `setting` | **left empty**: inner-being statements and party routes belong to claim layers; `chain` here is the verse's own stated link between acts, a lexical item only where the text states it (to confirm) |
| `cluster_code`, `cluster_subgroup_id` | history; empty (B:130, B:131) |

**`ib_node`:** `observation_id`, `seq`, `strong`, `surface`, `morph_code`, `verse_reference`, `verse_lexical_id` (required), `collection_id` (required), `question_code`: used. `role`: section 4. `subgroup_id`: empty at this stage (the groups do not exist yet); filled when the surface is placed (LR-05). `disposition`, `disposition_note`: claim step only. `reading_id`: the reading that applied it. `source_stage`, `traced_observation_id`: as now. `cluster_code`, `cluster_subgroup_code`: history.

### 3.5 Kinds for the note types (proposal, to confirm)

term: word, related_word, idiom, noun_severity, noun_relational; face: the divergence; link: pronoun_resolution, entity_link, chain, connective, structural_pattern, verb_argument, recurrence_role_shift; qualification: polarity and qualifier candidate (the kind `qualification` exists, but its use today is for what the qualifier gives the characteristic, which is claim layer 2: so a lexical qualifier candidate is recorded inside the structure observation, as RS-05 already says, and not as a kind of its own); inert: **no observation** ("recognised, nothing to read", the same as RS-05's standalone word). The `parts.item` carries the note type, so none is lost.

## 4. Roles: which roles, and how they relate to the four groups of surfaces

Three different things are called a role:

| | Where | Meaning | Set by |
|---|---|---|---|
| (i) `verse_lexical.role` | per Strong's code | the JSON list of its cluster codes (T and M) | `lexical.build`, from `cluster_strong` |
| (ii) `ib_node.role` | per occurrence in a finding | characteristic, qualifier (relevant); object, relational_target, enactment (bears on); standalone (recognised, no inner-being role): the word's role in the finding, "from this verse and never from a cluster tag" (RG-03) | the claim reading |
| (iii) `surface_term.surface_group` | per surface text | behaviour, inner_being_state, entity, other | the surface cycle, module 1 |

(i) is a property of the code, (iii) of the word's text, (ii) of one use. **The data shows that (ii) does not follow (iii):** of the nodes that have a role, every group takes every role. For example the surfaces of the group `entity` have the role characteristic on 715 nodes and qualifier on 2,130, `behaviour` surfaces are `standalone` on 2,245, and `inner_being_state` surfaces are `qualifier` on 7,052 and `characteristic` on 4,289 (counted 2026-11-15 over live nodes joined to `surface_term` by the surface text). The group says what the word usually is; the role says what it is in this finding. So the group cannot give a role, and the role cannot give a group; both are needed, and the lexical stage uses neither as an inner-being verdict.

**What the lexical stage gives a node as role.** The inner-being roles (ii) are the claim reading's judgement, and the lexical reading is not inner-being aware, so none of them is true of a lexical node. B:130 requires a role. The choice is: (A) a value `lexical` of `observation_role`, meaning "read lexically, inner-being role not yet assessed" (distinct from `standalone`, which means assessed and none); (B) role NULL for lexical nodes with B:130 scoped to inner-being stages; (C) a structural role of its own (head, qualifier candidate, negator, connective, entity, pronoun), derivable from `verse_lexical` (`unit_role`, `is_negator`, `party_kind`). I recommend (A) for the node, with the structural function carried in the observation's `parts.item`, because it keeps one role enum and one check, and (C)'s values are the items. This also changes the gate: it must test that the lexical observations exist for each member occurrence, not that an inner-being role was given.

## 5. What is retired, what it contributed, what replaces it (replaces v2 D3 and D6)

For each: contribution to the study; whether it takes part in the base data or `verse_lexical`; what else does the same; what replaces it. "Writes" is from `cfg_write_grant`.

| Item | Contribution | Base data or `verse_lexical`? | What else does it / replacement | Disposition |
|---|---|---|---|---|
| `lexical.meaning`, `lexical.relational`; `VerseReading.ps1`, `RelationalReading.ps1`, `Run-Stage1Batch.ps1` | the old Stage 1 reading | **No.** Grants: `ib_observation`, `ib_node`, `run_batch` only; `verse_lexical` is written by `lexical.build` alone. | the lexical stage (section 3), by collection | retire, **after** the lexical stage is built and a run on `thought` has been checked; not before, so no gap in the process |
| `versereadinggenerate.py` | builds the Stage 1 prompt package: word-level and relational checklists, prior-observation context, cost estimate | no | the layer pull (`layerreading.pull`) builds the evidence; the prompts become the config list (3.2). Its `_meaning_sources` (three lexicon sources) is also imported by three retired cluster generators and is the RG-08 evidence: **its logic is moved to the lexical pull, not lost** | retire after the move |
| `stage1coverage.py` | expected-versus-actual coverage of Stage 1 | no | the ledger and `LayerCheck` (same idea, by collection) | retire after the lexical items' expected nodes are derived and tested |
| `lexicalenrichgenerate.py`, `lexical.llm_*` (9 settings), B:7 to B:9 delivered at `VerseLexical.ps1` | the Anthropic API client, the cost cap and the usage log of the old generators | no | **`lib/aiclient.py` is the current AI client** (used by `collectionask`, `surfacebase`, `surfaceresolve`, `collectionevidence`, with `ai_call` and `cfg_ai_model`). Whether it carries the cost cap and the usage log of B:7 to B:9 is **not yet checked**; if not, B:7 to B:9 are re-scoped to its callers and not dropped | retire after that check |
| `charanswergenerate`, `charreadinggenerate`, `subgroupgenerate` (utilities active; steps retired by #2299) | the retired Stage 2 to 4 generators | no | claim layers | retire together with the above (they import it) |
| `lexicalscope.py`, `clusterstatus.py`, `handlers/cluster.py` | selector to verse ids; the cluster status machine | no | collections (#2448) | **keep** until #2448 |
| `recordingpass.py` | recording engine | no | none: live code uses it | **keep** |
| `handlers/lexical.py` `meaning`, `relational` | | no | | archive the two functions; keep `build`, `readiness` |
| `report.lexical_exceptions` (4 sections: layer-1 tally, layer-2 dispositions, judgement calls, integrity) | the self-audit of a Window 1 run: complete enumeration of Layer 1, every Layer 2 disposition against it | reads `verse_lexical` and the retired `verse_lexical_note` | the self-audit was a required part of Window 1 (#1383 (g)); its content is what `LayerCheck` reports for the lexical items | **adjust, not retire**: re-found on the lexical stage's ledger, same sections |
| `report.lexical_extract` (JSON "Phase 2 input" filtered by passage, verse, surface, strong) | the downstream input of the lexical work | reads `verse_lexical` and notes | the collection evidence report is the same role by collection | **adjust**: filter by collection, add the lexical observations; or fold into the evidence report (decision) |
| `lexical.notes`, `verse_lexical_note` (12 `cfg_column` rows), `passage.genre`, `passage.lexical_complete_at` | retired Layer 2 store | table is history | observations | keep the table as history; the 175 notes adopted (section 2) |

## 6. Prompts: if they are stale, what replaces them, is it complete

Answered in 3.2: the replacement is a config list of prompts by lexical item plus new questions for the structure items. It is **not complete today**: no question exists for the structure items. The completeness test is the table in 3.2, run as a check (every lexical item has at least one prompt), and the drafted questions come to the researcher before registration. The stale texts are corrected: the catalogue column text of `scope` and `dimension`, and `reading.observe_prompts` (it hands lexical prompts, M0.1.x and M0.5.x under face and term, to the inner-being reading).

## 7. The boundary between the lexical reading and the claim reading (how it works)

The principle is the researcher's (2026-11-14): "the verse cannot be lexical analysed and determine the ib implications in the same process, it needs separate observations"; "identifying and clarifying the faces is lexical work; what the faces do for the inner being is layer 2". How it works in the machinery:

1. **Order and gate:** the lexical stage for a collection comes first; the claim layer 1 step 1.1 opens only when every member occurrence has its lexical items answered (the ledger, section 3). The gate tests the existence and validity of the lexical observations, by collection, not by stage or role.
2. **Separate observations:** the lexical stage and the claim layers each write their own observations; the claim reading reads the lexical ones into focus (RO2, RW-09) and cites them as its base. A claim observation states what the word does for the inner being; a lexical observation never does.
3. **The test for a statement:** it is inner-being if it says what a word does or is for the inner being, or whether it bears on a person's state, relation to God or others; it is lexical if it follows from the word, the lexicon or the verse's stored structure alone. Where the border blurs the researcher says it is an enrichment, not a conflict (#2463 v18 (b)); the lexical observation may note the nuance and the claim reading uses it. No existing rule states the blur allowance (checked #2463 v20): it is added to the lexical rules.
4. **Engagement and the reading prompts:** engagement (#2406) already writes face, use, qualification, statement and link observations per verse and surface, inner-being by definition (520 observations), and `reading.observe_prompts` hands lexical prompts to the inner-being reading. After the change they read the lexical observations as their base and state only what a face or a relation does for the inner being; the lexical prompts leave `reading.observe_prompts`. How an engagement observation that restates a lexical fact is treated is the amalgamation of section 9.
5. **The moves between sets:** a word wrongly in a collection is moved to entity or other, and that movement is processed or completeness tests fail (#2463 v18 (e)); the ledger already retires the aspects the data no longer demands.

## 8. Where the stage sits (replaces D10)

The stage is Window 1 / Stage 1, between the base data (spine, `verse_lexical` Layer 1) and the inner-being analysis. `governance.programme_stages` says "Base_data (STEP through lexical)", which reads as Layer 1 only; I propose rewording it to name Window 1 Layers 1 and 2, with the lexical reading as the last part of the base for the analysis, and updating `glossary.currency_check` with the term. The existing rule 69 already states the order (readiness, the lexical reading stage, then the groups).

## 9. The existing observations (replaces v2 D5): amalgamated, not left as history

Rule RS-04 already defines the process: when a verse is worked, every existing observation and node on it, of any stage, is checked by its wording and accepted, modified in place, merged, soft deleted or left, and "the stage is not an indication of the nature of an observation and is never used to filter". The lexical reading follows it: for each verse in a collection's scope the existing observations of the lexical kinds (the 5,522 verse-reading observations; the face, term and link observations of prior-capture 919, engagement 130, Analysis_phase_1 126, reading 22) are read into the ledger item they answer, adopted or corrected, and given the collection, the occurrence and the role. The ledger therefore has to be able to **adopt** an existing observation, and not only to count new ones of its own stage; my `LayerCheck` currently counts observations of the layer's stage only and must be generalised (it also filtered by stage, against RS-04).

## 10. Control list of change

Each row: what, where, action, depends on / replaced by. "after" means the order of the build. Items marked D are decisions in section 12.

**Config rows**

| # | Item | Home | Action | Depends on / replaced by |
|---|---|---|---|---|
| C1 | `ib_observation.stage` value for the lexical stage | `cfg_enum` | add (D11) | |
| C2 | `observation_role` value `lexical` | `cfg_enum`, `reading.node_roles` | add (D2) | role choice (section 4) |
| C3 | the lexical items, their prompts, kinds, `none_allowed` | `cfg_setting layer.reading` (or a sibling setting) | add | C1, 3.2 |
| C4 | the gate of step 1.1: "the lexical items of every member occurrence are closed" | `layer.reading`, rule LR-01 | change | replaces the stage-and-role gate |
| C5 | new catalogue questions for the structure items | `wa_obs_question_catalogue` | add, **after the researcher approves the drafted text** | 3.2 |
| C6 | `scope` and `dimension` column texts | `cfg_column` | reword | |
| C7 | `reading.observe_prompts` lexical prompts | `cfg_setting` | remove from the inner-being list | C3 |
| C8 | method rules LR-01 to LR-05 | `cfg_method_rule` | reword for the lexical items | |
| C9 | method rules for the lexical stage (the blur allowance, no inner-being statement, per lettered code, adjacency is not scope) | `cfg_method_rule` | add | RG-08, RG-09, RG-14, RG-16, RG-21, RG-24, RW-04, RW-05 are the lexical rules in the reading set and **move**; the inner-being rule keeps its own half |
| C10 | the mixed rules RG-03, RG-05, RG-07, RS-01, RS-03 | `cfg_method_rule` | split (the structural half to C9) | |
| C11 | B:132, B:133 (reword); B:130 (role of a lexical node); B:113 and B:121 delivered also at `Collection-Build.ps1` | `cfg_behaviour_rule`, `cfg_rule_scope` | reword, add scope rows | |
| C12 | `governance.programme_stages`, `glossary.currency_check` | `cfg_setting` | reword, add term | section 8 |
| C13 | retire `lexical.meaning`, `lexical.relational`, their 6 grants and 3 settings | `cfg_step`, `cfg_write_grant`, `cfg_setting` | retire **after** the first lexical run is checked | section 5 |
| C14 | retire the five generator utilities, `lexical.llm_*`, and re-scope B:7 to B:9 | `cfg_utility`, `cfg_setting`, `cfg_rule_scope` | after the `aiclient` check | D6 |
| C15 | `report.lexical_exceptions`, `report.lexical_extract` | `cfg_report`, `cfg_step` | adjust | section 5 |
| C16 | `lexical.readiness` text | `cfg_step` | check and reword if it names clusters | |
| C17 | `collection.layer_open` text | `cfg_step` | reword | |

**Code**

| # | Item | Action | Depends on |
|---|---|---|---|
| K1 | `lib/layerreading.py`: the gate; the items; adopt existing observations; stage-free matching | generalise | C1 to C4, section 9 |
| K2 | the lexical pull: occurrences, neighbours (`collectionevidence.build_pairs`), lexicon sources (the logic of `_meaning_sources`), the prior observations and notes for the verse | add | |
| K3 | `handlers/collectionbuild.py`, `Collection-Build.ps1` | the lexical steps open and close through the same actions | K1 |
| K4 | `handlers/lexical.py` `meaning`, `relational`; `ps/VerseReading.ps1`, `RelationalReading.ps1`, `Run-Stage1Batch.ps1`; `lib/versereadinggenerate.py`, `stage1coverage.py`, `lexicalenrichgenerate.py`, `charanswergenerate.py`, `charreadinggenerate.py`, `subgroupgenerate.py` | archive, after the import trace is re-run clean | C13, C14 |
| K5 | `ps/VerseLexical.ps1` `-Step` list | remove retired steps | K4 |
| K6 | `lib/lexicalscope.py`, `clusterstatus.py`, `recordingpass.py`, `handlers/cluster.py` | **keep** (dependencies) | |
| K7 | tests naming the old modules (`temp_2295`, `temp_2323`) | check, reword or archive | K4 |

**Documents**

| # | Item | Action |
|---|---|---|
| D1 | USER-GUIDE section 6 (book-scoped, `lexical.enrich`, `lexical.notes`) | reword to the retired state and the lexical stage |
| D2 | USER-GUIDE section 7 (`VerseReading.ps1` and the others, "Stage 1") | reword |
| D3 | USER-GUIDE layered reading paragraph | add the lexical stage |
| D4 | `iba/docs/ps tools worksheet.xlsx` | update rows (not yet opened) |
| D5 | BUILD entry; `iba/docs` engineering notes stay as history | |

**Data**

| # | Item | Action |
|---|---|---|
| X1 | the 175 `verse_lexical_note` rows | adopt into the items |
| X2 | the lexical-kind observations of the five stages | adopt by RS-04 (section 9) |
| X3 | the 6,142 nodes without role | take the role `lexical` when adopted |
| X4 | first run on `thought`: its 394 occurrences, 346 verses | after the build and tests on a copy |

**Checks (D9):** the alignment check over every control home for any active row, rule scope or guidance that names a retired lexical entry without a disposition; the import trace before any archive move; the lexical item against the prompt list (3.2); `configmaint.validate` before and after.

## 11. What is not yet digested, and how

Still to be read for the build, before the build and not after: the 115 behaviour rules (all, not only those found by name); the 328 settings; USER-GUIDE in full; #1706 full pipeline checklist, #1824, #1860; the `reading.narrate` rules only for terms that name this stage (none found); the Excel worksheets; whether `aiclient.py` carries the cost cap and usage log. The way to avoid reading "reams of half-truths" is the control list above becoming the register: each row carries its final state, so after the build the rules, settings and guides for this stage are the rows listed as kept, reworded or added, and everything else for it is inactive or archived. I propose the register as a generated report (`Config-Report` section) and not another hand-written file, so it cannot go stale.

## 12. Decisions

| # | Decision | Recommendation |
|---|---|---|
| 1 | The stage is Window 1 Layer 2 re-founded on observations, entered by collection (section 3). Is the content of 3.1 (word items and structure items from the note types) right? | yes |
| 2 | The node role (section 4): A `lexical`, B NULL, C structural role | A |
| 3 | Prompts (3.2): config list by item, plus new questions for the structure items drafted for you before registration | yes |
| 4 | The order of retirement (section 5): old steps retire only after the lexical stage has run on `thought` | yes |
| 5 | Reports (section 5): adjust `report.lexical_exceptions`, and `report.lexical_extract` either adjusted or folded into the evidence report | adjust the first; fold the second |
| 6 | The existing observations (section 9): adopted by RS-04, the ledger generalised to adopt | yes |
| 7 | Vocabulary (D11): name the stages so that Window 1 Layer 1 and 2 are not confused with claim layers 1 and 2 | stage `lexical` and claim stages `claim-layer-1`, `claim-layer-2` (rename of my two values; no data uses them yet, to be checked) |
| 8 | `verse_lexical.role` (D12): leave, or clear the cluster array from the structural table later | leave; raise separately |
| 9 | The stored alignment check and the generated register (sections 10, 11) | yes |
| 10 | My reading of the four old stages (section 1.4) | to confirm: this is the part I am least sure of |
