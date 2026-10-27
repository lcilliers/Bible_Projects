# Analysis_phase_1: the specification, gathered from the escalations (v2, 2026-10-27)

Escalation #2318. **v2: section 4 replaced on the researcher's rulings of 2026-10-27 (#2319); v1 is in `outputs/escalation/archive/`.** Nothing here is new: every line is taken from what you already ruled or agreed, with its source. I read #2304 (design v3, rulings D1 to D7), #2310, #2312 (rulings D1 to D7 and the v5 instruction), #2308 (v4 rulings), the design `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`, the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md`, and the 54 active `cfg_method_rule` rows for `reading.open`, `reading.observe` and `reading.check` (RM, RO, RG, RW, RS). Where sources differ, the newest researcher ruling wins (section 5). Section 6 compares the specification with the code described in `outputs/escalation/2318-analysis-phase-1-description-v1-20261027.md`.

## 1. What Analysis_phase_1 is

The governing instruction (researcher, #2312 v5, chat 2026-10-27, verbatim): *"I just want you to build step 1 -3, not try and reconcile old and new thoughts. ... step 1 - 3 should align the data, or set it aside if it is not applicable. it is so simple."*

In one sentence: **for one subgroup (or a segment of it), collect its verses; pull into the same JSON every existing observation and open item for those verses; then, for each surface in those verses that the rules say needs observations, check what is there against the agreed definition, add only what is missing, bring the existing nodes into line, or set aside what does not apply. It is not synergy, claims or the story** (#2312 v5 D4: *"observe is not about synergy/it is not about building the story, it is about understanding the surfaces of the verse"*).

## 2. Step 1, Open (0.C): the scope JSON

| # | Requirement | Source |
|---|---|---|
| 1.1 | The scope is one subgroup, or a segment of one. A segment is a subset of the subgroup, given by surfaces or by verses. | #2304 v1 instruction; D1 (v3) *"likely to be a subset of a sub group"*; design 2304 v3 §2 |
| 1.2 | The subgroup is the home. The home cluster is the subgroup's cluster, so no `-Home` is given. A qualifier group is refused. | design 2304 v3 §2; rule 120; RO10, RM-02 |
| 1.3 | A reading takes one scope with a clear objective; the objective defines the home of what is recorded. | RM-01, RM-02, RO10 |
| 1.4 | The verses are collected through `surface_subgroup`, exact to the occurrence, with current subgroup settlements applied. | #2304 v1 instruction; design 2304 v3 §2 |
| 1.5 | A cluster with unallocated or stale surface pairs is refused. | #2294 G-a; design 2304 v3 §2 |
| 1.6 | A large subgroup (over 30% of its cluster's hits) is segmented into logical units when it comes into focus; a cluster is not read whole by default. | RO13, RM-03, RO8 |
| 1.7 | The output is one JSON with all the verse references in scope; per verse, every surface occurrence with its clusters, its subgroup (through `surface_subgroup`), its occurrence id and whether it is in focus by the rules in 4.1. A verse is in the scope because a surface of the subgroup stands in it (for example Mat 7:8 is in the asking subgroup); **every surface of that verse is in scope for observations, not only the subgroup's** (ask, receive, seek, find, knock, open). | #2304 v1 instruction; #2312 v2 §2 and P1; researcher, chat 2026-10-27 (this clarification) |
| 1.8 | One JSON file per scope run, saved to the cluster (the home cluster's folder); each step adds its own section to it. | #2304 v3 D2 (researcher); design 2304 v3 §1 |
| 1.9 | **There is one version of the scope: the JSON.** The scope is not also kept in a table (`reading_verse` is dropped for these steps). The next phase reads strictly from observations for the scope; the scope is re-assembled from the JSON so that phase 2 can pull from observations. | researcher, chat 2026-10-27 (*"there should not be two versions of the same truth in the reading process. the next phase must strictly read from observations for the scope. I am aware that the scope will need to be re-assembled for phase 2 to be able to pull from observations"*) |

## 3. Step 2, 0.GAP pre: the pull

| # | Requirement | Source |
|---|---|---|
| 2.1 | Pull into the scope JSON all the existing observations for the verses of the scope, and all the open items for those verses. The criterion is the verse; the pull is not filtered by subgroup, so items across several subgroups of the verse come back. | #2312 v5 (researcher, verbatim); #2304 v1 instruction |
| 2.2 | Existing observations: every non-withdrawn observation with a node on the verse, each node placed on its surface occurrence, with its role and subgroup. | #2312 v2 §2; design 2304 v3 §3; #2276 (B4) |
| 2.3 | A node belongs to a surface by its `verse_lexical_id`, or, with none, when its verse, Strong and surface match one occurrence only. Any other node is set aside and counts for no surface. | RS-02; #2312 v4 |
| 2.4 | Open items are matched through the verse and its surfaces' Strongs and clusters (a scope item by its own verses). Each item shows the subgroups it reaches through cluster, Strong and `surface_subgroup`. | #2310 4.2 option B (approved); #2312 v2 §2 |
| 2.5 | The open items the scope run will clear are listed once: an item whose target verses lie in the scope, or reach past it (read in part), or that names the home cluster or one of its codes. | #2304 v3 D3 (researcher: *"the open items that will be cleared by the scope run"*) |
| 2.6 | The documents are not read in 0.GAP pre. The gap type `read_in_files_only` is retired; the prior work is in `ib_observation` (#2305). | #2310 4.1 (researcher: *"approve"*); #2304 v8 |
| 2.7 | The face components are gathered in this phase (the ledger faces are linked to the observation that holds them, or a face finding is written); the face story is built in the claims. `face_not_gathered` is measured per surface occurrence; `term_reading_missing` stays in 0.GAP pre. | #2312 D7 (researcher: *"correct"*); #2312 v2 §4 and P5 |
| 2.8 | Base data is read only in 0.C and 0.GAP pre. (The gap half of this rule, a missing or poor base datum routed to its recovery, **moves to step 4**: see 2.10.) | RO4, RW-11; plan 2268 §4 |
| 2.9 | Work already done is gathered, not redone. 0.GAP pre reads each table once and the later phases use what it gathered. | RM-04, RO3, RO5 |
| 2.10 | **Step 2 is about gathering the available data. Gaps come into play only when step 4 is started.** Step 2 therefore records no gaps and has no gap gate. What step 2 writes to the tables is not specified beyond this; as I read it, it writes none and gathers into the JSON only (to be confirmed). Rows 2.7 and 2.8 are read the same way. The previous wording (gaps recorded in the JSON and processed into the tables, RO12) is withdrawn from step 2. | researcher, chat 2026-10-27 (*"the design of 2.10 is not clear. the gaps only comes into play when step 4 is started. step 2 is about gathering the available data"*) |
| 2.11 | **Rows 2.1, 2.2 and 2.3 are written directly to the JSON as they are pulled, not kept separately in memory**, so that the number of observation details does not overwhelm memory. | researcher, chat 2026-10-27 |

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

### 4.1 Which surfaces are evaluated, and what is recorded

- **Every surface of the verse is evaluated.** Every live word row is enumerated, with no pre-filtering by role or gloss. The verses come in through the subgroup, but all their surfaces are evaluated (row 1.7).
- **Relevance is judged by tests, not by the gloss or the cluster tag.** In plain words: does the gloss carry inner-being vocabulary; is it part of an idiom or combined span whose surface gloss diverges; does it carry a volitional sense behind a plain action; does it name or imply another party (tested against "relates" in the five-part definition: thinks, feels, chooses, relates, orients toward meaning, others and God); is it a negation or modifier on an operation; does its morphology link it to another operation in sequence; does it contribute nothing beyond grammar. Inner-being content is often not declared but discoverable, so a surface that bears on the inner being only by what it does (the outward act, the party engaged, the refusal) is relevant through the tests.
- **A surface is relevant when it has an inner-being role: the characteristic, or a qualifier of it** (researcher: *"surface words that does not have a inner being role (either as characteristic or as qualifying it) must not be recorded in the observastions"*).
- **A relevant surface gets observations. A surface with no inner-being role is not recorded in the observations.** The evaluation of every surface, with its result and reason, is kept in the JSON so that the gate can see that every surface was evaluated. It is not written to `ib_observation` or `ib_node`.
- **A standalone word** (researcher): in most cases it has no role, and is ignored. In limited cases it could move to being a qualifier; then the standalone word is recorded **inside the observation**, for the claims process to decide. `standalone` is therefore not a node role in Analysis_phase_1.
- **The words that bear on a relevant act without being its characteristic or qualifier** (what the act is directed at, the party engaged, the outward act) are recorded as **nodes of the observation of the act**, with role values wider than characteristic and qualifier: object or content, relational target, enactment (researcher: decision D-a, option 2). They are not observations of their own.

### 4.2 What an observation of a relevant surface covers

One observation is one finding about one inner-being operation or characteristic in this verse, written once; it gains nodes when it applies to other words or verses. It covers, where the verse shows it:

1. **The surface and its meaning here:** the sense active in this verse, with the evidence for it (the idiom or combined span, the morphology, the ESV rendering, the three meaning sources read together). Never the dictionary sense restated, never from memory; missing data is named as a gap.
2. **Its role:** the characteristic, or the qualifier and what it gives the characteristic (grade, nature, impact, size, relation or other; there is no fixed list).
3. **Its polarity:** whether the act is a refusal or a pursuit. This belongs to the observation, not to the node (researcher).
4. **Its content or object:** what the act is directed at or against.
5. **Its enactment:** the outward act the inner act produces, if the verse states one.
6. **The other party and the sequence:** who else is engaged and in what order, with the route (A, B or C) on a party or link finding.
7. **How it appears here:** the circumstance in this verse.
8. **The chain and the primary operation:** the operations the verse links in sequence (the Hebrew narrative sequencing mark is one signal; the Greek version of this test is not built) and which operation has nothing upstream. There can be more than one. **The chain is recorded as a link-kind observation and the primary operation as a statement-kind observation** (researcher: decision D-b, option 1).
9. **Typed flags:** a data-quality flag (the data itself is doubtful) is kept apart from a discovery flag (a hypothesis the verse cannot settle, needing neighbouring verses). A discovery flag is carried to an open item for the claims work.

Each part is a structured field or a clearly delimited part of the observation, never an unranked sentence, and none is ranked below another. A structural fact (a relational transaction, the polarity, the sequence) is kept even when nothing in the verse explains it.

**Nodes** are the classification and relational record of the observation (researcher): for each word the observation covers, its verse, word, subgroup, occurrence, cluster and its role in the finding.

**Kinds:** the face kind records how a word appears here; qualification, party, statement, link, use and term are used as before. The silence kind records a surface with no inner-being bearing; it has no use in Analysis_phase_1.

### 4.3 What the claims work records

The characteristic-level observations (how a face differs from the word's other occurrences, how the parties interact, how the role works for the characteristic, what the neighbouring verses add) are written during the claims processing, as observations of an **existing characteristic-level stage value** of the observation table (researcher: decision D-c, option 1; *"it must be based on the context of the verse"*). Which stage value is for the claims work to settle: the table has the values characteristic synergy, characteristic reading, characteristic answers and characteristic subgroup, and none holds a live characteristic-synergy observation today. Analysis_phase_1 leaves room for it and writes none of them.

### 4.4 The Observe gate

The gate passes when:
- every surface of every scope verse has an evaluation in the JSON, with its result and reason;
- every relevant surface has observations covering the parts of 4.2 that the verse shows;
- no surface with no inner-being role has an observation;
- every discovery flag is carried to an open item, and every open item related to the scope is answered (4.5 below);
- every finding is written, and the verses are marked analysed.

The earlier test, role, face and term of every content surface or a silence finding, is replaced. Two method rules change with it: the rule that each surface needs a role, a face and a term result (and silence otherwise), and the face rule (the claims part moves out). These are config changes for the build.

### 4.5 Open items

Every open item related to the scope is answered by the reading, never silently ignored. The response uses the register's vocabulary (`closed`, `touched` with "read in part" where the item reaches past the scope, `forward`, `withdrawn`, `superseded`) with what the reading found. A flag the reading cannot resolve becomes a new open item (#2304 D4 and D5, researcher; the flag-carrying rule; #2273 D8).

### 4.6 Aligning the existing data

- *"When the subgroup for the cluster is processed, the nodes will be created; when the verse enters the scope, the rest of the surfaces for the word will be completed and added, nodes for existing surfaces will be updated."* (#2308 v4 D1 and D2, researcher.)
- *"When a surface appears multiple times, it usually will create one node for it, but the practice of trying to read all the nodes just to check for duplicates is not advocated."* (#2308 v4 D3, researcher.)
- Data that does not apply is set aside, with its reason (#2312 v5). The 63 observations with no node are left as a stated limit (#2312 v4).

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
| n | step 2 gathers the available data into the JSON; no gap work, no gap gate | `Gather` is built on the gap file: it writes a record per gap item into the tables, and `Check` at `open` runs `gate_pre` on those records | G02, G49, G50 |
| o | open items appear once, structured in the JSON | open items are put in three places: per verse in `<label>-collation.json`, as a section of `<label>-gaps.json`, and per verse in `<label>-observe.json` | O22, O02, B02 |
| e | ledger faces linked to their observation (3,068 candidates) or a face finding written | code writes what the reading supplies; it does not link by itself | O09, G02 |
| f | term findings from the three meaning sources, not memory (RG-08, RW-04, RW-11); face findings say what differs (RG-09) | form is checked; the content is not | G13 |
| g | `cluster_subgroup_code` on every node | never written | G17 |
| h | existing nodes updated when their verse enters the scope (2308 D2) | no element updates existing nodes except to withdraw them | G17, R05 |
| i | a repeated surface gets one node (2308 D3) | the gate counts each occurrence; the second occurrence of an identical surface can never get a node, so the gate cannot pass (the second "and", Mat 7:8) | G19, B04, K03 |
| j | every related open item answered or the gate refuses | the gate does not look at open items | K03 |
| k | the observe gate checks the evaluation of every surface and the parts of 4.2 for every relevant surface (4.4) | the observe gate requires role, face and term (or a silence finding) of every content surface; `gate_pre` checks only that a record exists | G50, K03, B04 |
| m | rows 2.1 to 2.3 written directly to the JSON | `collate` builds the whole collation for all verses in memory and writes the file afterwards | O22, O02 |
| p | every surface of the verse is evaluated for an inner-being role and the result kept in the JSON (4.1) | a surface is in focus unless its morph is a function word; nothing else evaluates it, and nothing is kept for a surface left out | B04 |
| q | a surface with no inner-being role is not recorded in the observations (4.1) | the silence kind exists to record exactly such a surface, and the gate accepts it | G13, B04 |
| r | node roles: characteristic, qualifier, object or content, relational target, enactment; standalone is not a role (4.1) | roles are characteristic, qualifier and standalone | G13, G17 |
| s | polarity, the chain and the primary operation in the observation (4.2) | no kind or field for polarity or the primary operation; the chain has no tested field | G13 |
| t | the face rule records how a word appears here; the cross-occurrence part is claims work (4.0) | the face rule asks for why the word differs from its other occurrences | method rules, `reading.observe` |
| l | rules in config (P-1, R1) | fixed in code: 10 and 15 character minimums, the bare-negation word list, the passage window of two verses, the registry of pre detectors | O02, G13, G18, B09, O12 |

## 7. What happens next

You said not to ask you to work this out again, so I am not asking. The next step is to put this into the form the build follows: for each of the three steps, the checks and writes of sections 2 to 4 as config rows and code changes, listed against rows a to t. I will test on a copy (B:97) and record the result here. I start when you approve this specification, or say what in it is wrong.
