# #2268 The analytic process and what is read when, with rulings R1 to R19 (v2)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** the plan the config is to be aligned to. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"rulings-review-v4 is answered and can now be incorporated in the planning. next is to assess and adjust all the configs and rules to align with it."*

All the rulings are verbatim on #2268 (v13, v15, v16, v18), and the researcher's annotated rulings files are in `outputs/escalation/archive/`. This plan states what the rulings make the process. The changes to config that follow are in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md`.

## 1. The governing principles (from the rulings)

| # | Principle | Ruling |
|---|---|---|
| P-1 | Rules live in config: no operating rule in scripts, and no choice left to interpretation that can be stated as a rule. A file is the authority only with a config pointer, and the only such case is the programme and inner-being definitions in the programme prose. | R1 |
| P-2 | **Reading** is digesting the content and context of data for a scope, not only verse text. Every reading rule states what is read, why, the expected outcome, and what it relates to. | R3 |
| P-3 | Work already done is **gathered, not redone**, unless there is reason to believe it is incomplete or needs revision. | R2 |
| P-4 | Claude reads in a session, on demand from the tables. The API generator steps are retired (tested, not cost-effective). | R3c |
| P-5 | The narrative style is predefined in config. Each block fits the flow and context of its chapter's story, and the chapters follow a story. Turning claims into narrative, and weaving, is Claude's call. The researcher reads the chapters in context and corrects through Claude. | R4 |

## 2. The phases

| Phase | What it is | Reads | Writes |
|---|---|---|---|
| **0.C Scope** | a collection of verses with **a clear objective**, which defines the home of what is recorded (R16). A cluster is not read whole by default: an overview segments it (R2, `whole_cluster_reading_start`). A verse may come into scopes from several angles (a cluster group, an open item), each with its own objective (R14). | base data, to assess the scope | the reading and its scope |
| **0.GAP pre** | the gaps of the scope, measured against what is expected (§4), recorded in the scope's gap JSON as they are found | every table for the scope at quality depth, without verse text; **all observations already recorded for each verse** (R14) | the gap JSON. It is processed into the tables as soon as the phase is complete and before the next gate (R13c) |
| **D1 Word level** | per word, on its own schedule, not per reading (R3a); Claude in a session (R3c) | `verse_lexical`, the word's meaning in three sources, earlier word-level observations | term observations: meaning in context, surface variants, related terms (R13a) |
| **D2 Characteristics** | per cluster, on its own schedule (R3a); Claude in a session (R3c) | D1 results, the cluster and subgroup tables, open items | characteristic observations; open items |
| **D3 Claims** | per reading (R3a): the current claims resting on the scope (R3b) | claims, their sources, their observations | – |
| **D4 Observe** | each verse in its passage, the only reading of verse text (RO1), with all of the verse's observations read into focus (R14) | verse text and passage, the gathered set | the observations the scope's objective calls for (§3) |
| **D4 Claims with 0.GAP post** | observations carried by claims or disposed; the post-claims gaps checked against the claims in the same read (RO7) | the scope's observations and claims | claims, dispositions; post-claims gaps recorded, then processed into the tables before the next gate |
| **D4 Narrate** | the blocks rewritten to the predefined style, fitting the chapter's story (R4) | claims and blocks | blocks |
| **Publish** | the touched chapters published | – | the published files |

Across all phases: open items, which hold unresolved gaps and gaps that need further work (R13a); and the observation record (§3). Reading files are filed under the home cluster's folder (R7).

## 3. The observation record

**What a reading of a verse records** (R13a, R15, R16, R17, R18):
- **Per M-code in focus, and per T-code that turns out to be relevant,** the verse's observations hold:
  - the **face** (R18: the ledger face and the catalogue's term for the same thing are one concept);
  - the **role**;
  - the **operation**;
  - the **parties**;
  - the **route**;
  - the **home**.
- **The term reading results** for the verse also go into observations: additional meaning that is relevant, surface variants, related terms.
- **Several M-codes or T-codes in focus give several observation rows.** There are **no duplicate rows**. A single observation may carry **several nodes**, when it applies to several verses or terms.
- **One method** governs every observation written (R15). It is the reading method: the role guide and the strand rules, restated in config. From the September checklist, these carry over: verses resolved fresh; flags carried, not resolved inline; can't-resolve recorded; relations only on evidence.
- **The question catalogue is kept as prompts and guidance for the areas to explore** (R15, R17). No answer is forced to a question that does not apply, and none is manufactured beyond what the verse shows.
- **The catalogue work already done (718 verses) is not put aside** (R15). When such a verse comes into focus, the observations the reading method expects and that are missing are added. Any observation no longer supported is soft-deleted.
- **The ledger work** (key statements, faces) is work already done, gathered the same way (R5, R18, R19).
- **Status meanings stay by stage** (R14), each set down in config with who sets it.
- **Corrections** (R6): B:68 is retired, with the API route and its similarity threshold. No observation is changed except by a reading, and every change is recorded with its reason.
- **Where a verse ends up** is recorded in the tables only (R5): told, claim, held (on an item), data, context, withdrawn. The October Placements tables retire as their files are gathered.

## 4. Gaps

- **A gap** is an expected item that is missing, or present but not what is expected. Mere presence of something that is not the right thing is not a resolved gap. A required part that is missing is a gap of its own (R13b).
- **Gaps are processed for the scope only** (R13c). The scope's gap JSON records them as they are discovered, and is processed into the tables when its phase completes, before the next gate.
- **The gap types** (R13a, specified):

| Phase | Gap type: the expected item missing or not as expected | Resolved by |
|---|---|---|
| 0.GAP pre | a term not in a cluster (term-cluster) | the cluster assignment's recovery (0.B) |
| 0.GAP pre | a term with no meaning (missing meaning) | the meaning's recovery (0.B) |
| 0.GAP pre | a missing base datum: span, Strong's | the base data recovery (0.B) |
| 0.GAP pre | a term with no term reading result for the verse (meaning in context, surface variants, related terms) | D1 observations |
| 0.GAP pre | an earlier reading in a file not in the tables | gathered into observations |
| 0.GAP pre | a ledger face not in the observation record | gathered (R18) |
| 0.GAP pre | an open item on the scope with no response | the item |
| D4 observe | a verse with no observation for an M-code in focus, or for a T-code found relevant | observations |
| D4 observe | an observation missing its face, role, operation, parties, route or home | the observation's parts |
| D4 observe | an observation no longer supported by the verse | soft-deleted, with the reason |
| 0.GAP post | an observation carried by no claim and not disposed | a claim, or a disposition |
| 0.GAP post | a claim told in no block and not held | a telling, or a hold |
| 0.GAP post | a claim resting on verses only, with no observation | a claim source to an observation |
| 0.GAP post | a verse cited in a block with nothing recorded behind it | an observation and a claim |
| any | a gap unresolved, or needing further work | an open item (R13a) |

## 5. Reading rules (RO1 to RO12)

RO1 to RO9 as adopted (R3d), with RO10 to RO12 added from R13 to R16.

| # | Rule |
|---|---|
| RO1 | Verse text and passage are read only in D4, once per verse per reading. |
| RO2 | When a verse is read in D4, all of its observations already recorded are read into focus, and the scope's objective is evaluated against them (R14). The observations the objective calls for, and that are missing, are added. |
| RO3 | Work already done is gathered, not redone, unless it is incomplete or needs revision (P-3). |
| RO4 | Base data is read only in 0.C and 0.GAP pre. A missing or poor base datum is a gap routed to its recovery, never worked round. |
| RO5 | 0.GAP pre reads each table once for the scope. The later phases read what it gathered. |
| RO6 | D1 to D3 read table data only. |
| RO7 | 0.GAP post is done inside D4's claim step, from the same read. |
| RO8 | A cluster is not read whole by default. An overview segments it (`whole_cluster_reading_start`). |
| RO9 | Narration reads claims and observations. It quotes verse text from the `verse` table and does not re-read the verse in context. |
| RO10 | A scope's objective defines the home of the observations it records (R16). |
| RO11 | One observation row per M-code or relevant T-code in focus, with no duplicate rows. An observation applying to several verses or terms carries several nodes (R16). |
| RO12 | A scope's gap JSON is processed into the tables as soon as its phase completes, before the next gate (R13c). |

## 6. Terms, examples, files

- **Terms (R9):**
  - the glossary is canonical, and controlled values (role, route, face, gap types) are `cfg_enum` rows pointing to their glossary entries;
  - a check that the glossary is current is needed (P33).
- **Worked examples (R10):** examples live in a config table, each tied to its rule and kept current when the rule changes. The guide's four cases are from a previous era and are restated or replaced.
- **The July method file (R11):** the relevant parts go to config, and the file is archived. Genre is no longer written to any table, and there is no book reading.
- **The role guide (R12):** it is replaced by a generated guide. The researcher reviews it after all the rules are restated.
- **#2260 to #2267 (R19):** these are restated against the reading method once it is in config. Findings that rest only on the catalogue rules are withdrawn.
