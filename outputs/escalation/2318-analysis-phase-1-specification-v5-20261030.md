# Analysis_phase_1: the specification, gathered from the escalations (v4, 2026-10-27)

Escalation #2318. **v4: a modified observation is changed in place; open items move out of Analysis_phase_1 (researcher, 2026-10-27, #2318 v13). v3: the JSON is an index and each verse is worked by a query of the database (researcher, 2026-10-27, #2318 v11); section 3 rewritten, section 4.7 added, open items provisional (4.5). v1 to v3 are in `outputs/escalation/archive/`.** Nothing here is new: every line is taken from what you already ruled or agreed, with its source. I read #2304 (design v3, rulings D1 to D7), #2310, #2312 (rulings D1 to D7 and the v5 instruction), #2308 (v4 rulings), the design `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`, the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md`, and the 54 active `cfg_method_rule` rows for `reading.open`, `reading.observe` and `reading.check` (RM, RO, RG, RW, RS). Where sources differ, the newest researcher ruling wins (section 5). Section 6 compares the specification with the code described in `outputs/escalation/2318-analysis-phase-1-description-v1-20261027.md`.

## 1. What Analysis_phase_1 is

The governing instruction (researcher, #2312 v5, chat 2026-10-27, verbatim): *"I just want you to build step 1 -3, not try and reconcile old and new thoughts. ... step 1 - 3 should align the data, or set it aside if it is not applicable. it is so simple."*

In one sentence: **for one subgroup (or a segment of it), collect its verses into a JSON that indexes them; then work each verse by querying the database for its existing observations, check each one (accept, modify or soft delete, observations and nodes), evaluate every surface of the verse for an inner-being role, and write the observations that are missing. It is not synergy, claims or the story** (#2312 v5 D4: *"observe is not about synergy/it is not about building the story, it is about understanding the surfaces of the verse"*).

## 2. Step 1, Open (0.C): the scope JSON

| # | Requirement | Source |
|---|---|---|
| 1.1 | The scope is one subgroup, or a segment of one. A segment is a subset of the subgroup, given by surfaces or by verses. | #2304 v1 instruction; D1 (v3) *"likely to be a subset of a sub group"*; design 2304 v3 §2 |
| 1.2 | The subgroup is the home. The home cluster is the subgroup's cluster, so no `-Home` is given. A qualifier group is refused. | design 2304 v3 §2; rule 120; RO10, RM-02 |
| 1.3 | A reading takes one scope with a clear objective; the objective defines the home of what is recorded. | RM-01, RM-02, RO10 |
| 1.4 | The verses are collected through `surface_subgroup`, exact to the occurrence, with current subgroup settlements applied. | #2304 v1 instruction; design 2304 v3 §2 |
| 1.5 | A cluster with unallocated or stale surface pairs is refused. | #2294 G-a; design 2304 v3 §2 |
| 1.6 | A large subgroup (over 30% of its cluster's hits) is segmented into logical units when it comes into focus; a cluster is not read whole by default. | RO13, RM-03, RO8 |
| 1.7 | The output is one JSON that **indexes** the verses in scope: per verse its reference, the route(s) that brought it in, its progress (waiting, in hand, done) and the evaluation of its surfaces (4.1). A verse is in the scope because a surface of the subgroup stands in it (for example Mat 7:8 is in the asking subgroup); **every surface of that verse is in scope for observations, not only the subgroup's** (ask, receive, seek, find, knock, open). The surfaces, observations and nodes themselves are read from the tables when the verse is worked (section 3), not copied into the JSON. | #2304 v1 instruction; researcher, chat 2026-10-27 (*"the json is simply the indexer to allow for a list of verses to work through"*) |
| 1.8 | One JSON file per scope run, saved to the cluster (the home cluster's folder); each step adds its own section to it. | #2304 v3 D2 (researcher); design 2304 v3 §1 |
| 1.9 | **There is one version of the scope: the JSON.** The scope is not also kept in a table (`reading_verse` is dropped for these steps). The next phase reads strictly from observations for the scope; the scope is re-assembled from the JSON so that phase 2 can pull from observations. | researcher, chat 2026-10-27 (*"there should not be two versions of the same truth in the reading process. the next phase must strictly read from observations for the scope. I am aware that the scope will need to be re-assembled for phase 2 to be able to pull from observations"*) |

## 3. Step 2: the pull is a query by verse, not a copy in the JSON

Researcher, chat 2026-10-27 (verbatim): *"I agree we need to make the query by verse change."* The separate step that gathered the existing observations and open items into the JSON is replaced. Its pull is the first move on each verse in step 3. A step 2 that only reports counts per verse can be kept if you want it; none is specified here.

| # | Requirement | Source |
|---|---|---|
| 2.1 | For each verse of the index, query the database for the verse's existing observations (not withdrawn), each with its nodes placed on their surface occurrences, with role and subgroup. The criterion is the verse: the query is not filtered by subgroup, so the observations of every subgroup in the verse come back. Nothing is copied into the JSON. | researcher, chat 2026-10-27; #2312 v5 |
| 2.2 | A node belongs to a surface by its `verse_lexical_id`, or, with none, when its verse, Strong and surface match one occurrence only. Any other node does not count for a surface; it is still shown to the check in 4.7, so that it can be accepted, modified or soft deleted. | existing-counts-by-occurrence rule; #2308 v4 D2 |
| 2.3 | The query is made when the verse is worked, so that the observations written for earlier verses are seen. | researcher, chat 2026-10-27 |
| 2.4 | The ledger faces recorded for the verse's surfaces (`reading_strand_hit`) are queried with the observations. Linking each hit to the observation that holds its face is part of the check in 4.7. (From #2312 D7; unchanged by this version.) | #2312 D7 |
| 2.5 | The documents are not read. The prior work is in `ib_observation`. | #2310 4.1 (approved) |
| 2.6 | Work already done is gathered, not redone. Base data is read only here (the verse's words) and in the scope. | RO3, RO4, RO5 |
| 2.7 | Only one verse is held in memory at a time, so that the number of observation details does not overwhelm memory. | researcher, chat 2026-10-27 |
| 2.8 | Gaps (a term with no cluster, no meaning, a missing base datum) are not recorded in this step. **Gaps come into play when step 4 starts.** | researcher, chat 2026-10-27 |

## 4. Step 3, Observe and Record: the verse understanding

*(Replaced in v2 on the researcher's rulings of 2026-10-27, #2319 v1 to v9. The earlier text is in the archived v1 of this file. The working draft and its decisions: `outputs/escalation/2319-section-4-draft-v1-20261027.md`; the earlier lexical work it rests on: `outputs/escalation/2319-lexical-phase-1-phase-2-prior-work-v1-20261027.md`.)*

### 4.0 The frame and the line

The frame (researcher): *"to arrive at a claim about a characteristic work in the inner being, there must be a solid understanding of the lexical meaning of the verse and the context of the surface words that mean something for the inner being. two parts formulating the claim and the verse understanding. that is all that the process is about."*

- **Analysis_phase_1 is the verse understanding.** It creates the observations: *"Everything necessary for the claims to know must be in the observations."* The earlier lexical work (the Dan 1:8 worked example and its twelve-test checklist) is the closest model.
- **The claims work formulates the claim** and uses the surrounding verses when it does (researcher: *"when the characteristic claim is formulated, the surrounding verses are often used"*).

**The line between the two parts.** An observation belongs to Analysis_phase_1 if the verse itself shows it. It belongs to the claims if it needs more than one verse or the characteristic as a whole.

| What the verse itself shows (Analysis_phase_1) | What needs more than one verse (claims) |
|---|---|
| the meaning of the surface in this verse, and the evidence for that sense | how the face differs from the word's other occurrences |
| the surface's role here: the characteristic, or a qualifier of it | how the role works for the characteristic |
| the kind of act: refusal or pursuit (polarity) | the backdrop that only the neighbouring verses give (for example the disposition behind a resolve) |
| what the act is directed at, and the outward act it leads to | the motive readings built on that structure |
| the other party the verse names, and the sequence | how the parties interact across verses |
| the chain of operations stated in the verse, and which is primary | the face story and the characteristic roll-up |

The face rule as it stood asked the verse reading for how a word differs from its other occurrences. That part is claims work. Analysis_phase_1 records how the word appears here.

**First move on every verse:** query its existing observations and nodes (section 3) and check them (4.7), then evaluate the surfaces (4.1).

### 4.1 Which surfaces are evaluated, and what is recorded

- **Every surface of the verse is evaluated.** Every live word row is enumerated, with no pre-filtering by role or gloss. The verses come in through the subgroup, but all their surfaces are evaluated (row 1.7).
- **Relevance is judged by tests, not by the gloss or the cluster tag.** In plain words: does the gloss carry inner-being vocabulary; is it part of an idiom or combined span whose surface gloss diverges; does it carry a volitional sense behind a plain action; does it name or imply another party (tested against "relates" in the five-part definition: thinks, feels, chooses, relates, orients toward meaning, others and God); is it a negation or modifier on an operation; does its morphology link it to another operation in sequence; does it contribute nothing beyond grammar. Inner-being content is often not declared but discoverable, so a surface that bears on the inner being only by what it does (the outward act, the party engaged, the refusal) is relevant through the tests.
- **A surface is relevant when it has an inner-being role: the characteristic, or a qualifier of it** (researcher: *"surface words that does not have a inner being role (either as characteristic or as qualifying it) must not be recorded in the observastions"*).
- **A relevant surface gets observations. A surface with no inner-being role is not recorded in the observations.** The evaluation of every surface, with its result and reason, is kept in the JSON so that the gate can see that every surface was evaluated. It is not written to `ib_observation` or `ib_node`.
- **A standalone word** (researcher): in most cases it has no role, and is ignored. In limited cases it could move to being a qualifier; then the standalone word is recorded **inside the observation**, for the claims process to decide. `standalone` is therefore not a node role in Analysis_phase_1.
- **The words that bear on a relevant act without being its characteristic or qualifier** (what the act is directed at, the party engaged, the outward act) are recorded as **nodes of the observation of the act**, with role values wider than characteristic and qualifier: object or content, relational target, enactment (researcher: decision D-a, option 2). They are not observations of their own.

### 4.2 What an observation of a relevant surface covers

One observation is one finding about one inner-being operation or characteristic in this verse, written once; it gains nodes when it applies to other words or verses. It covers, where the verse shows it:

1. **The surface and its meaning here:** the sense active in this verse, with the evidence for it (the idiom or combined span, the morphology, the ESV rendering, the three meaning sources read together). Never the dictionary sense restated, never from memory; missing data is named as a gap. The sheet carries the meaning data the tables hold for each surface (the meaning tree, the sense head, the STEP gloss, the related words and, for Greek, the lexicon; cfg_setting `reading.sheet_meaning`, #2329), and a data-quality flag about meaning sources is written from what it holds or lacks.
2. **Its role:** the characteristic, or the qualifier and what it gives the characteristic (grade, nature, impact, size, relation or other; there is no fixed list).
3. **Its polarity:** whether the act is a refusal or a pursuit. This belongs to the observation, not to the node (researcher).
4. **Its content or object, and what comes before:** what the act is directed at or against (part `content`); and the prompt, state or purpose the verse states before the act (part `before`; #2329).
5. **Its enactment, and what follows:** the outward act the inner act produces, if the verse states one (part `enactment`); and what follows the act, the answer, result or response (part `after`; #2329). The answer is often in the next verse: the part cites it by reference from the passage around the verse on the sheet, and no verse enters the scope for it.
6. **The other party and the sequence:** who else is engaged and in what order, with the route (A, B or C) on a party or link finding. A stated party holds the sentence and the kind of the one who acts and of the one acted on, from `party_kind` (divine, human, non_human; #2329), so who asks whom comes from a query.
7. **How it appears here:** the circumstance in this verse.
8. **The chain and the primary operation:** the operations the verse links in sequence (the Hebrew narrative sequencing mark is one signal; the Greek version of this test is not built) and which operation has nothing upstream. There can be more than one. **The chain is recorded as a link-kind observation and the primary operation as a statement-kind observation** (researcher: decision D-b, option 1).
9. **Typed flags:** a data-quality flag (the data itself is doubtful) is kept apart from a discovery flag (a hypothesis the verse cannot settle, needing neighbouring verses). A discovery flag is recorded inside the observation, typed, for the claims work (open items: 4.5).

Each part is a structured field or a clearly delimited part of the observation, never an unranked sentence, and none is ranked below another. A structural fact (a relational transaction, the polarity, the sequence) is kept even when nothing in the verse explains it.

**Nodes** are the classification and relational record of the observation (researcher): for each word the observation covers, its verse, word, subgroup, occurrence, cluster and its role in the finding.

**Kinds:** the face kind records how a word appears here; qualification, party, statement, link, use and term are used as before. The silence kind records a surface with no inner-being bearing; it has no use in Analysis_phase_1.

### 4.3 What the claims work records

The characteristic-level observations (how a face differs from the word's other occurrences, how the parties interact, how the role works for the characteristic, what the neighbouring verses add) are written during the claims processing, as observations of an **existing characteristic-level stage value** of the observation table (researcher: decision D-c, option 1; *"it must be based on the context of the verse"*). Which stage value is for the claims work to settle: the table has the values characteristic synergy, characteristic reading, characteristic answers and characteristic subgroup, and none holds a live characteristic-synergy observation today. Analysis_phase_1 leaves room for it and writes none of them.

### 4.4 The Observe gate

The Observe gate passes when:
- every verse of the index is done;
- on every verse, every existing observation and node has been accepted, modified or soft deleted, with the reason recorded where it changed (4.7);
- every surface of every verse has an evaluation in the JSON, with its result and reason;
- every relevant surface has observations covering the parts of 4.2 that the verse shows;
- no surface with no inner-being role has an observation;
- every finding is written, and the verses are marked analysed.

The earlier test, role, face and term of every content surface or a silence finding, is replaced. Two method rules change with it: the rule that each surface needs a role, a face and a term result (and silence otherwise), and the face rule (the claims part moves out). These are config changes for the build.

### 4.5 Open items move out of Analysis_phase_1

Researcher, chat 2026-10-27 (verbatim): *"open items move out of phase 1."* (Earlier the same day, as a leaning: *"I am leaning towards clearing open items after the claims have been completed, as a process of secondary validation. I am not convinced that the open items are really playing a role any longer now that we are a) covering all the surface b) work systematically by sub group."*)

Analysis_phase_1 neither pulls the open items for a verse nor answers them, and the gate does not look at them. The open items stay in the register untouched and are cleared after the claims, as a secondary validation. A flag the reading cannot settle is recorded inside the observation (4.2, part 9), not raised as an open item. The earlier rulings of 2026-10-26 that open items related to the scope are updated and never silently ignored (#2304 D3 to D5) are superseded for this process by this ruling.

### 4.6 Aligning the existing data

- *"When the subgroup for the cluster is processed, the nodes will be created; when the verse enters the scope, the rest of the surfaces for the word will be completed and added, nodes for existing surfaces will be updated."* (#2308 v4 D1 and D2, researcher.)
- *"When a surface appears multiple times, it usually will create one node for it, but the practice of trying to read all the nodes just to check for duplicates is not advocated."* (#2308 v4 D3, researcher.)
- Data that does not apply is set aside, with its reason (#2312 v5). The 63 observations with no node are left as a stated limit (#2312 v4).

### 4.7 Existing observations and nodes: accept, modify, soft delete

Researcher, chat 2026-10-27 (verbatim): *"we must not loose the objective to check the current observations and a) accept b) modify c) soft delete both observations and nodes."*

When a verse is worked, every existing observation and node on it (of any stage: prior capture, strand reading, verse reading and the others) is checked against the verse, and one of three things is done:

| Action | Observation | Node |
|---|---|---|
| accept | unchanged; it counts for the surface it names | unchanged; it counts for its occurrence |
| modify | changed; the old value, the new value and the reason are recorded in `ib_observation_change` (no observation is changed except by a reading) | completed or corrected: occurrence, subgroup, cluster, role (#2308 v4 D2: *nodes for existing surfaces will be updated*) |
| soft delete | status withdrawn, with the reason; nothing is deleted | disposition withdrawn, with the reason |

The observations with no node cannot be reached from a verse; that stays a stated limit (63 observations). Reading all the nodes only to look for duplicates is not advocated (#2308 v4 D3).

**Decision.** Researcher, chat 2026-10-27 (verbatim): *"changed in place (overwritten)"*. A modified observation is changed in place; it is not replaced by a new observation. The previous value is kept in `ib_observation_change` with its reason, which is the history home for a replaced value, so the live row holds only the current version. The check in the code that refuses a changed description on an existing observation (`observationrecord.check`) has to change for this.

## 5. Where the sources differ, and which I follow

| Point | Older | Newer (followed) |
|---|---|---|
| Documents | #2304 v4: adopt readings from the cluster documents first | #2304 v8 parked it; #2310 4.1 retired the document read; the documents are in `ib_observation` (#2305) |
| Pre-gate records | #2304 v3 D4: dropped | the design of #2304 was parked at v8; #2310 and #2312 v4 keep the gather records; I follow #2312 v4 (built and approved) |
| Existing observations | #2304 D3: shown, none counts until applied | #2312 v4 and RS-02: an existing node counts for a surface by its occurrence |
| Repeated surface in a verse | #2312 v4: one node per occurrence | #2308 v4 D3: usually one node per surface |

## 6. The specification against the code as it stands

Each row names the element in the description file.

| # | Specified | Code today | Description element |
|---|---|---|---|
| a | one subgroup or a segment of one; no `-Home` | any selectors and `-Home` are accepted; the home is the request's subgroups of the home cluster | O02, O18, O21 |
| b | one JSON in the cluster's folder | three files under `outputs/reading/<label>/` | O02 |
| c | the surface path with subgroups per surface | built (collation lists every surface occurrence with clusters and subgroups) | O22 |
| d | (moved to step 4: gap types and their checks) | no detector for three pre gap types | O12, section 9 |
| e | ledger faces linked to their observation (3,068 candidates) or a face finding written | code writes what the reading supplies; it does not link by itself | O09, G02 |
| f | term findings from the three meaning sources, not memory (RG-08, RW-04, RW-11); face findings say what differs (RG-09) | form is checked; the content is not | G13 |
| g | `cluster_subgroup_code` on every node | never written | G17 |
| h | existing nodes updated when their verse enters the scope (2308 D2) | no element updates existing nodes except to withdraw them | G17, R05 |
| i | a repeated surface gets one node (2308 D3) | the gate counts each occurrence; the second occurrence of an identical surface can never get a node, so the gate cannot pass (the second "and", Mat 7:8) | G19, B04, K03 |
| k | the observe gate checks the evaluation of every surface and the parts of 4.2 for every relevant surface (4.4) | the observe gate requires role, face and term (or a silence finding) of every content surface; `gate_pre` checks only that a record exists | G50, K03, B04 |
| p | every surface of the verse is evaluated for an inner-being role and the result kept in the JSON (4.1) | a surface is in focus unless its morph is a function word; nothing else evaluates it, and nothing is kept for a surface left out | B04 |
| q | a surface with no inner-being role is not recorded in the observations (4.1) | the silence kind exists to record exactly such a surface, and the gate accepts it | G13, B04 |
| r | node roles: characteristic, qualifier, object or content, relational target, enactment; standalone is not a role (4.1) | roles are characteristic, qualifier and standalone | G13, G17 |
| s | polarity, the chain and the primary operation in the observation (4.2) | no kind or field for polarity or the primary operation; the chain has no tested field | G13 |
| t | the face rule records how a word appears here; the cross-occurrence part is claims work (4.0) | the face rule asks for why the word differs from its other occurrences | method rules, `reading.observe` |
| u | each verse is worked by a query of the database; the JSON is an index with per-verse progress (1.7, section 3) | the collation copies the verses, words, observations and open items of the whole scope into `<label>-collation.json` and the gap file; `Observe` then queries the tables again | O22, O02, B02 |
| v | every existing observation and node is accepted, modified or soft deleted when its verse is worked (4.7) | `Record` can withdraw a node or an observation; there is no accept or modify action, no element updates an existing node, and the check refuses a changed description on an existing observation | R02, R05, R06 |
| w | open items are not pulled or answered in Analysis_phase_1 (4.5) | the pre gap and the observe file carry the open items of each verse; `Record` takes a record on an open item | O11, B02, R02 |
| l | rules in config (P-1, R1) | fixed in code: 10 and 15 character minimums, the bare-negation word list, the passage window of two verses, the registry of pre detectors | O02, G13, G18, B09, O12 |

## 7. What happens next

You said not to ask you to work this out again, so I am not asking. The next step is to put this into the form the build follows: for each of the three steps, the checks and writes of sections 2 to 4 as config rows and code changes, listed against the rows of section 6. I will test on a copy (B:97) and record the result here. I start when you approve this specification, or say what in it is wrong.
