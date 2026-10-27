# Analysis_phase_1: the specification, gathered from the escalations (v1, 2026-10-27)

Escalation #2318. Nothing here is new: every line is taken from what you already ruled or agreed, with its source. I read #2304 (design v3, rulings D1 to D7), #2310, #2312 (rulings D1 to D7 and the v5 instruction), #2308 (v4 rulings), the design `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`, the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md`, and the 54 active `cfg_method_rule` rows for `reading.open`, `reading.observe` and `reading.check` (RM, RO, RG, RW, RS). Where sources differ, the newest researcher ruling wins (section 5). Section 6 compares the specification with the code described in `outputs/escalation/2318-analysis-phase-1-description-v1-20261027.md`.

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

## 4. Step 3, Observe and Record: the surfaces

### 4.1 Which surfaces are in focus

"Word" always means the surface with its embedded Strong, never the word registry (#2312 D1, verbatim). Not every surface needs observations. The rules (RG-03, RG-07, RG-21 to RG-24; #2312 v2 §3):

- Every M-coded surface, and every T-coded surface found relevant. Content words are read even with no cluster tag.
- Read for what they carry: T3 operations, movement and force, negators (a refusal is an act), connectives, body parts, places, objects, nature.
- Function words (particles, prepositions, conjunctions, suffixes, pronouns) get no observation of their own, except negators and connectives.
- A T2 word is read as the qualifier of what it binds to; a tagged word working adverbially is a qualifier there.
- The words in `reading.non_characteristic_strongs` are never a verse's characteristic.
- A word is read per its lettered Strong's code (its grain), never the bare lemma (RG-21).

### 4.2 What each surface needs (RS-01, the agreed definition)

| Part | What it is | Rules |
|---|---|---|
| role | the surface's role in this verse (characteristic, qualifier, standalone); from the verse, never from the cluster tag | RG-03, D7 |
| face | how the word appears here, the circumstance, why it differs from its other occurrences, where the sense departs from the general gloss | RG-09, #2312 D7 |
| term reading result | meaning in context, surface variants, related terms; recorded as a `term` finding | RW-02, plan 2268 §3 |
| silence | a surface with no inner-being bearing gets a `silence` finding with its reason in place of face and term | RS-01, RG-10 |
| other kinds | party (with route), statement, link, use, qualification: recorded where the verse shows them, never forced | RG-06, RG-17, RW-02 |

Only what a surface is missing is added; a surface that lacks nothing is not read again (RS-01, #2312 D1: *"only missing observations for the surface must be added"*).

### 4.3 How each finding is written

- Read outward from the verse, in its passage and genre, with the speaker named; every observation already recorded for the verse is read into focus first (RG-01, RG-02, RO2, RW-09). Verse text and passage are read only here, once per verse per reading (RO1).
- **Term findings** take the root's range from all three meaning sources read together, the ESV renderings across its verses, whether the English adds or hides, the literal sense beside the rendering; where more than one reading is open, each is recorded and the choice marked "I read" (RG-08). The text is concise and tied to this verse, never a restatement of the dictionary sense; a transliteration is never given without its gloss (RW-04). Missing data is named as a gap, never filled from memory (RW-11, B:114).
- **Face findings** say what differs from the word's other occurrences (RG-09).
- **Qualifiers:** what a qualifier gives the characteristic it binds to is evaluated and recorded as a `qualification` finding, applied to the qualifier (role qualifier) and the characteristic (role characteristic). There is no fixed list of what it can give (RG-04, #2273 D9). A qualifier that gives nothing gets its node or its reason.
- **Parties and route** (A, B or C), on party and link findings (RG-06, #2273 D3).
- One observation per finding; the same description is never written twice; applied to another verse or word it gains a node (RW-03, RO11). Where the evidence points to more than one reading, each is its own observation (RW-08). A difference or specific inference is its own observation (RG-15).
- **The record:** `ib_observation` holds obs_text, meaning, implication, basis, tag (the kind), route, stage `reading`, status. `ib_node` holds verse, strong, surface, morph, `cluster_code`, **`cluster_subgroup_code` (the word's subgroup where it has one)**, `verse_lexical_id`, role, `reading_id`, and later the disposition (design 2273-2274 v6 §3; #2304 D5).
- Every change to a finding or node is kept with its reason in `ib_observation_change`; no observation is changed except by a reading; an observation no longer supported is withdrawn with its reason (RW-01). Existing nodes are not reclassified unless a re-read finds an error (#2273 D6).
- Verse references are resolved fresh at write time (RW-06). A flag is carried to an open item and not resolved inline (RW-07). After recording, every observation is read back against the verse (RG-20).

### 4.4 Aligning the existing data

- *"When the subgroup for the cluster is processed, the nodes will be created; when the verse enters the scope, the rest of the surfaces for the word will be completed and added, nodes for existing surfaces will be updated."* (#2308 v4 D1 and D2, researcher.)
- *"When a surface appears multiple times, it usually will create one node for it, but the practice of trying to read all the nodes just to check for duplicates is not advocated."* (#2308 v4 D3, researcher.)
- Data that does not apply is set aside, with its reason (#2312 v5). The 63 observations with no node are left as a stated limit (#2312 v4).

### 4.5 Open items

Every open item related to the scope is answered by the reading, never silently ignored. The response uses the register's vocabulary (`closed`, `touched` with "read in part" where the item reaches past the scope, `forward`, `withdrawn`, `superseded`) with what the reading found. A flag the reading cannot resolve becomes a new open item (#2304 v3 D4 and D5, researcher; RW-07; #2273 D8).

### 4.6 The Observe gate (Check)

Passes only when every surface in focus has role, face and term (or silence), counting earlier findings by occurrence; every open item related to the scope has its response; every finding is written; the verses are then marked analysed (RS-01, RS-02; #2304 v3 resolution; #2273 §4). Before the whole scope is read, a few verses are read and checked first (RG-19; this is how #2316 was run).

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
| k | `gate_pre` and `gate_observe` check against the definition | `gate_pre` checks that a record exists; the observe gate checks the parts of 4.2 per occurrence | G50, K03 |
| m | rows 2.1 to 2.3 written directly to the JSON | `collate` builds the whole collation for all verses in memory and writes the file afterwards | O22, O02 |
| l | rules in config (P-1, R1) | fixed in code: 10 and 15 character minimums, the bare-negation word list, the passage window of two verses, the registry of pre detectors | O02, G13, G18, B09, O12 |

## 7. What happens next

You said not to ask you to work this out again, so I am not asking. The next step is to put this into the form the build follows: for each of the three steps, the checks and writes of sections 2 to 4 as config rows and code changes, listed against rows a to l. I will test on a copy (B:97) and record the result here. I start when you approve this specification, or say what in it is wrong.
