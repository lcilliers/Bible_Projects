# \#2268 Rulings R1 to R17: review file (v3)

**Date:** 2026-10-24 · **Escalation:** #2268 · **For:** the researcher's rulings, before the alignment design is written. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"#2268: write R1 to R12 as one review file with the options and a decision blank for each."*

**What this version covers.**

* **R1 and R2 are decided**, by your feedback written into the v1 file. That feedback is recorded verbatim on #2268 v13, and your annotated copy is in `outputs/escalation/archive/2268-rulings-review-v1-20261024-researcher-feedback.md`.
* **R3 is rephrased** as R3a to R3d, on the reading definition and the phases you gave. The phases are set out in `outputs/escalation/2268-analytic-process-and-reading-plan-v1-20261024.md`.
* **R4 to R17 stand,** each with a line on how the phases change it.

**How to use this file.** Each open ruling gives:

* what is in tension;
* the options;
* Claude's view, labelled **inferential** (B:4);
* a decision blank.

The evidence is in:

* the process file (`2268-analytic-process-and-reading-plan-v1-20261024.md`);
* the inventory (`2268-analytic-process-config-inventory-v3-20261024.md`);
* the overlay (`2268-config-overlay-on-reading-process-v3-20261024.md`), with its codes C, W, P;
* the guide plotting (`2268-role-guide-v2-plotted-into-config-v3-20261024.md`).

**Order.**

* R3a to R3d first: they set the phases the others act in.
* R14 and R15 before R13.
* R17 follows R3c.
* R4, R5, R7 and R16 are independent.

\---

## R1 Where the study method lives: decided

**Your ruling (verbatim, from your comments on options A, B and C):**

* A: *"Yes. 99% of all governing rules should follow this pattern. No operating rule should be hard coded in scripts, and no choices should be left for arbitrary interpretation if they can be formulated in a rule."*
* B: *"This may apply in limited cases where it is impossible to state the rule without extended explanation. In general, if this happens, it is because the rule is not well thought through."*
* C: *"there are limited scenarios where files remain the authority.  There should always be a config that points to the file. The only scenario that I am aware of where a config points to a file is for the programme and IB definitions which are also in the programme prose."*

**What follows:**

* The role guide, the observation-rules checklist and the three method files go into config (overlay C2, P26).
* The rules hard-coded in the reading's code go into config (overlay C25).

\---

## R2 What B:84 means: decided

**Your ruling (verbatim, from your comments on options A, B and C):**

* A: *"It seems that B:84 is trying to capture a segment of the truth without proper context. It should be replaced with proper configs: whole\_cluster\_reading\_start "prepare overview of cluster to allow for segmentation, do not read all the verses in a cluster by default""*
* B: *"B:84 is not a config and must state what the underlying configs state, B:84 should not exist, or modify or overrule the configs. The concept of backfill is replaced with the concept of gathering work already done, and not re-doing work, unless there is reason to believe the previous work is incomplete or need revision."*
* C: *"No - B:84 as it stands must be modified or retired."*

**What follows:**

* B:84 is retired, and its content is replaced by configs, starting with `whole\_cluster\_reading\_start` (RO8).
* Gathering work already done replaces "backfill" (RO3).

\---

## R3 How reading takes place across the analytic process: rephrased

Your repositioning (verbatim on #2268 v13) defines **reading** as digesting the content and context of data for a scope, not only reading verse text. Each reading rule answers what is read, why, what outcome is expected, and what it relates to. It gives the phases:

* **0.B base data:** read only in 0.C and 0.GAP; missing data routed to recovery.
* **0.GAP:** read from the tables, no verse text, at quality depth, before claims and after claims; the post-claims reading is done with the claims reading.
* **D1 to D3:** table data only.
* **D4:** verses in context, from observations to narration.

The process file sets these out (§2, §3) with the reading rules RO1 to RO9 (§4). Your note that D4, D5 and OBS were misplaced is answered there: D4 runs from observations to narration, and D5 and OBS are not phases but the observation record across D1 to D4.

### R3a The order of the phases

|Option|What it means|
|-|-|
|**A**|Every phase runs per reading, in order: 0.C, then 0.GAP pre, D1, D2, D3, then D4 (observe; claims with 0.GAP post; narrate), then Publish.|
|**B**|D1 and D2 run per word and per cluster on their own schedule, not per reading, because a word's occurrences and a cluster's characteristics are read once for the whole study. A reading's 0.GAP pre gathers their results (RO3, RO5). Only D3 and D4 run per reading.|
|**C**|Another order: write it below.|

**Claude's view (inferential):** B. Under A, two readings that share words each run D1 and D2 again, which is the repeated reading you asked to remove. Under B, 0.GAP pre finds where D1 or D2 results are missing or below the rules for the scope, and that is a gap with its own work.

**Decision R3a:** \_\_\_B\_\_\_

### R3b What D3 reads

|Option|What it means|
|-|-|
|**A**|The current claims resting on the scope's verses and observations, with their sources and the characteristics they speak of, read before D4 so that D4 tests them rather than re-claims them.|
|**B**|A, plus the narrative blocks that tell those claims, so the narration the scope touches is known before D4.|

**Claude's view (inferential):** A. The blocks are read once, at D4 narrate, where they are rewritten (RO9). Reading them in D3 as well would be a second read.

**Decision R3b:** \_\_\_A\_\_\_

### R3c Who performs D1 and D2, and what happens to their existing results

**Facts:**

* The registered steps `lexical.meaning`, `lexical.relational`, `cluster.subgroup`, `cluster.reading` and `cluster.answer` call the API.
* Stage 1 has read 718 verses, in 49 of the 80 M-clusters, leaving 10,595 observations, 4,953 of them withdrawn.
* The characteristic stages left 885 observations.
* 92 of 95 clusters are at the first status.

|Option|What it means|
|-|-|
|**A**|The API steps stay the performers of D1 and D2, under their cost caps (B:7). They run where 0.GAP finds the word-level or characteristic results missing. Existing results are gathered as done (RO3) unless 0.GAP finds them below the rules.|
|**B Claude perform the reading in a session where it has maximum benefit of reading on demand from the tables, rather than loading all the input data in bulk for every reading cycle.**|Claude performs D1 and D2 in a session, from the tables. The API steps are retired, and their method rules are carried into the phases' config. Existing results are gathered as done unless below the rules.|
|**C  Note that the API read was tested (as per some of the results) but found that it is not cost effective at all. You should see session logs and cost analysis in the history for it.**|The API for D1 (one answer per occurrence, high volume), and Claude in a session for D2 (judgement over a cluster's words). Existing results are gathered as in A.|

**Claude's view (inferential):** C. D1 is one bounded answer per word occurrence across up to 24,227 verses, which suits batched calls under a cost cap. D2 is a judgement across a cluster's words, which suits a reading in a session. Your R3 note ("none of it use the API") may mean you already intend B for D2. Your ruling sets it.

**Decision R3c:** \_\_\_B\_\_\_

### R3d The reading rules RO1 to RO9

The rules are in the process file §4. In short:

* RO1: verse text read only in D4, once per verse per reading.
* RO2: every word's role and every significance recorded, so later readings read the record.
* RO3: gather, don't redo, unless a gap says so.
* RO4: base data only in 0.C and 0.GAP, with gaps routed to recovery.
* RO5: 0.GAP reads each table once, and the later phases read what it gathered.
* RO6: D1 to D3 read table data only.
* RO7: 0.GAP post is done in D4's claim step.
* RO8: no whole-cluster reading by default.
* RO9: narration reads claims and observations, not verses in context.

|Option|What it means|
|-|-|
|**A**|Adopt RO1 to RO9 as stated, as config rows in the design.|
|**B**|Adopt with changes: write which below.|

**Claude's view (inferential):** A. Today 65% of verses with M-coded words carry two or more M-clusters, so RO2 alone halves the verse readings, or better.

**Decision R3d:** \_\_A\_\_\_\_

\---

## R4 Who authorises the narrative a reading writes

**Under the phases (v3):** This is D4 narrate. It is unchanged by the phases.

**In tension (overlay C10, C11):**

* **B:85:** "Claude writes no prose (… a narrative chapter file) without a specific instruction."
* **B:72:** "Routing a strand's verses into the narrative waits for the researcher's direction."
* **Gate 2** (`Reading.ps1 -Step Apply`) tells every claim or holds it, and rewrites the narrative blocks, as routine reading work.
* **B:106:** a workflow Claude designs adds no per-item approval steps by default.

|Option|What it means|
|-|-|
|**A**|Opening a reading under an escalation is the instruction: gate 2 writes claims, tellings and blocks. You review through the published chapters (gate 3) and the reading's escalation. B:85 and B:72 are reworded to say so.|
|**B**|Gate 2 writes claims and tellings, but a block rewrite waits for your go-ahead on the reading's escalation before Apply writes it: one approval per reading, not per block.|
|**C**|B:85 as it stands: Claude drafts each rewrite, and you approve it before it is written.|

**Claude's view (inferential):** A fits B:106 and the gate design. B is the choice if you want to see narrative changes before they are written. This is your call about your own text.

**Decision R4:** \_\_none of the above.  the narrative style must be predefined and the narrative blocks must be in keeping of the style configs and the chapter narration.  that means that any individual paragraph or block must fit into the flow and context of the story of the chapter, and the chapters must follow a story.  It terms of approval, the process of turning claims into narratives, and weaving is your to call - I am unable to validate it pre-publishing.  I will read the chapters in context and make corrections through you if you got it wrong.  The current B rules around this topic must be retired/replaced because it constantly cause issues as it stands. \_\_\_\_

\---

## R5 One vocabulary for where a verse or observation goes

**Under the phases (v3):** Dispositions are recorded in D4's claim step. The placement files B:79 checks belong to the earlier way of working.

**In tension (overlay C6, W18):**

* **B:79** and `session\_close.placement\_kinds` give every verse in a reading, ledger or weave *file* one placement: told, claim, data, forward OT-nn.n, held #nnnn, parked, or context. Session-close SC5(d) checks them, in `\_analytics` files only.
* **Gate 2** records, in tables, every observation as carried by a claim or disposed (held on an item, silent, withdrawn), and every claim as told or held.
* Two vocabularies cover one job.

|Option|What it means|
|-|-|
|**A**|Gate 2's vocabulary is the one, extended by the two placements it lacks: **data** (route C: assessed, not for the narrative) and **context** (named only as another verse's setting). B:79 and SC5(d) then apply only to the `\_analytics` files still to be carried in, and retire when they are.|
|**B**|The placement kinds become the vocabulary, and gate 2's dispositions are renamed to them.|
|**C**|Both stay, with a mapping between them in config.|

**Claude's view (inferential):** A. The tables are the record now. C keeps two names for one fact.

**Decision R5:** \_\_I do not understand R5 - make it practical for me to digest it.\_\_\_\_

\---

## R6 The scope of B:68

**Under the phases (v3):** RO3 points the same way as B:68 (no re-run or re-read without a recorded gap). The question is which observations B:68 governs: D1's, or every phase's.

**In tension (overlay C7):**

* **B:68:** every correction to `ib\_observation` happens only through `record\_one\_observation` processing a fresh LLM answer.
* **The reading process** writes observations through Claude's reading (`record\_strand\_observations`, with `supersedes`), and changes their status at gate 2 (`set\_disposition`).
* B:68 was written for Stage 1 (route D1).

|Option|What it means|
|-|-|
|**A**|B:68 is limited to the observations of the API routes (D1, D2, if they stay under R3). A reading's observations are corrected only through the reading: a new observation that supersedes the old, or a disposition at gate 2, each with its reason. No standalone edit script is allowed for either.|
|**B**|B:68 applies to every observation, and the reading may not supersede or dispose. Gate 2 as designed cannot then run.|

**Claude's view (inferential):** A. Its last clause keeps B:68's real point, that no script edits observations without a reading behind it.

**Decision R6:** \_ what is the purpose of this rule and setting.  it seems to get in the way for no apparant value\_\_\_\_\_

\---

## R7 Where a reading's files are filed

**Under the phases (v3):** Unchanged.

**In tension (overlay C8):**

* `report.cluster\_folder\_naming\_convention`: "ALL output relating to a cluster (analysis, readings …) is filed in that cluster's subfolder."
* `reading.output\_dir`: every reading under `outputs/reading/<label>/` (its gap JSON, collation and synergy JSON).

|Option|What it means|
|-|-|
|**A**|`outputs/reading/<label>/`, as now. A reading is a scope, not a cluster, and may cross many. The cluster folder rule is reworded to exclude readings.|
|**B**|Under the home cluster's folder (`\_analytics/Clusters/<home>/readings/<label>/`), with `reading.output\_dir` changed.|

**Claude's view (inferential):** A. A reading's scope is not one cluster (B:84, R2).

**Decision R7:** \_\_\_B\_\_\_

\---

## R8 The passage-method tables and the research database

**Under the phases (v3):** The passage method is retired (your R3 feedback), so option C applies unless you rule otherwise: its tables stay in iba.db as sources that 0.GAP reads.

**In tension (overlay C13):**

* `governance.scope\_iba\_db`: "a few analysis tables (debate/passage control) are expected to migrate back to research\_db".
* `governance.scope\_research\_db`: research\_db is "prose-only".
* B:13 calls research\_db "prose + analytic findings" (C12, a correction either way).

|Option|What it means|
|-|-|
|**A**|They stay in iba.db. The migration sentence is removed, research\_db stays prose-only, and B:13 is corrected.|
|**B**|They move to research\_db, and research\_db's scope is widened to say so.|
|**C**|Follows R3: if route D3 is retired, its tables stay in iba.db as sources a reading collates (A).|

**Claude's view (inferential):** A, or C if R3 retires D3. Both leave research\_db prose-only, as it is today.

**Decision R8:** \_\_\_A\_

\---

## R9 Where the study's terms live

**Under the phases (v3):** Unchanged. The terms are used in D4 and in the observation record.

**In tension (guide plotting §2):** the guide's terms are used in rules but defined nowhere in config:

* role, characteristic, operation, main IB operation, qualifier;
* relational observation, pointer observation, face, route, faculty, party-kind T-codes.

Seven have glossary entries in the prose store (ids 1089, 1047, 1043, 1066, 1048, 1046, 1069), all at status `draft`. Only *inner being* has a `cfg\_prose\_concept` pointer. The prose is yours (B:85), and `governance.prose\_canonical\_authority` makes it the canonical authority on the programme's concepts.

|Option|What it means|
|-|-|
|**A**|The glossary is the definition. Each term gets a `cfg\_prose\_concept` pointer, delivered at `Reading.ps1`. The missing glossary entries (main IB operation, relational, pointer, face, route, faculty) are drafted for you to write or approve.|
|**B**|The definitions live in config: the controlled values as `cfg\_enum` (roles, routes), with their meanings in a setting (as `ib\_observation.tag\_guidance` does for tags) and in `cfg\_column` use text.|
|**C Glossary must be kept up to date. Nothing in the project is inforcing it.**|Both. The glossary stays canonical, and `cfg\_enum` and `cfg\_column` carry the controlled values, each pointing to its glossary entry. The words a record may hold are thus checked, and their meaning has one home.|

**Claude's view (inferential):** C. It is the existing pattern (`governance.prose\_canonical\_authority` with `cfg\_prose\_concept`), plus the controlled values a record needs. The glossary drafts stay yours to approve.

**Decision R9:** \_\_C\_\_\_\_

\---

## R10 Where the worked cases live

**Under the phases (v3):** Unchanged.

**In tension (guide plotting §3 §6):** the guide's four worked cases (2Pe 2:13, 2Cor 7:11, Lam 4:6, Psa 1:1 and 1:5) teach how the rules apply. No config table holds an example.

|Option|What it means|
|-|-|
|**A the four worked cases are from a previous era;  examples must be in the config and been kept up to date if changes in rules dictate it.**|A config table of worked examples: the rule or check each illustrates, the verse, what the reading found and why. Each is delivered with its rule at first use, so the example arrives where the rule does.|
|**B**|In the glossary, as your prose under the term each illustrates.|
|**C**|A teaching document that config points to, holding no rule.|

**Claude's view (inferential):** A. The Lam 4:6 case is the failure the rules guard against (reading inward, nearly closing on "not X"), and it is worth most at the point of use. C reopens the gap R1 closes.

**Decision R10:** \_\_\_\_A\_\_

\---

## R11 The July method file the guide draws on

**Under the phases (v3):** Unchanged. Under R1, a file left with live rules in it is not allowed.

**In tension (guide plotting §2):** the guide's definition of role rests on `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` §13 and §14. That file is the July "live lexical process" (genre treatment, self-learning loop, index-driven build, poetic and discourse-shaped books), much of it from earlier eras.

|Option|What it means|
|-|-|
|**A**|Carry §13 and §14 into config with the guide, and archive the file.|
|**B  Take from the file what is relevant, and place it in config, then archive the file. I know for instance that genre is no longer written to any table, and we no longer do any book reading so a lot of stuff from this document is no longer relevant**|Review the whole file: what is still live goes into config (genre treatment, poetic and discourse books may bear on reading in a passage), and the rest is archived with a note of what was carried.|
|**C**|Leave it as it is.|

**Claude's view (inferential):** B. A file left with live rules in it is the same gap as R1.

**Decision R11:** \_\_\_\_\_\_

\---

## R12 The guide itself, once its content is in config

**Under the phases (v3):** Under R1, option C (keep the guide beside the config) is no longer open.

**In tension (guide plotting §1):** once the 57 statements are in cfg rows, the guide would restate them (B:3, single authority), and B:73 still points to it.

|Option|What it means|
|-|-|
|**A**|Archive the guide (B:96), and reword B:73 to point to the cfg rows.|
|**B this "guide" should never live on its own, or have content that is not config based.  I would like to review the "guide" after all the rules have been restated and added to configs again as I am not convinced that it is co-herent, complete and not confusing.**|Replace it with a **generated** reading guide, written from the cfg rows by a tool and never edited by hand, the way the claim register is exported. You keep one readable page, and it cannot drift. The current guide is archived.|
|**C**|Keep the guide alongside the config.|

**Claude's view (inferential):** B. It keeps a readable whole, which the guide gives and scattered rows do not, without a second home. C contradicts your instruction.

**Decision R12:** \_\_\_B\_\_\_

\---

## R13 Gaps: what a gap is, where it is recorded, when it reopens, what "enough" means

**Under the phases (v3):** 0.GAP pre and 0.GAP post are where gaps are discovered and updated. R13 decides how they are kept, reopened and measured.

**In tension (overlay §2.GAP; C23, P23 to P25, P31):** gaps are found in seven places, each with its own test:

* a reading's gap JSON;
* the collation's presence test;
* `verse\_meta.status`;
* Stage 1 coverage;
* `cluster.status`;
* the file index;
* the narrative register and the thread audit.

All of them test presence. None relates to another. B:114 says "the gaps are recorded into the tables", but there is no table of gaps. A gap's state lives only in a reading's gap JSON file, or is recomputed when a measure is run. When an observation is withdrawn or found below the rules, nothing reopens its verses: 4,008 verses stay `analysed`. Nothing says when a verse, word, scope or cluster has been read enough.

|Option|What it means|
|-|-|
|**A**|**A gap register in iba.db.** One table of gaps, each with its kind (one study-wide list of gap types, extending `reading\_gap\_type` with quality gaps), what it is on (verse, word, cluster, claim, item), the measure that found it, its state (open, closed, reopened) and the reading or escalation that closed it. A discovery step runs the measures and writes the register. The gates close gaps, and a withdrawal or a rule change reopens them. A study-wide gap report is read from the register. "Enough" is defined in config as the hand-over checks passing (guide §7, R15), not presence.|
|**B**|**One study-wide gap analysis step, no register.** The measures stay computed on demand, but one step runs them all under one config definition of a gap and of "enough", and writes one report. A reading's gap JSON stays its own record, and reopening is found by rerunning the step.|
|**C**|As now: a reading's own gaps, plus the separate measures.|

**Claude's view (inferential):** A, because your words "discovery and updating of the gaps" need a gap's state to be kept, and only a register keeps it and lets a gap reopen. B is the simpler step (B:39) if a rerun report is enough for you.

**Decision R13:** \_\_\_\_\_\_

\---

## R14 What each observation status means, and who sets it

**Under the phases (v3):** Gate 2 is now D4's claim step. The quality status is what 0.GAP reads, and the disposition is what D4 claims writes.

**In tension (C18, C22, P27):**

* `cfg\_column ib\_observation.status` (#1782, your definitions of 2026-09-20):

  * `draft`: written, not yet looked at;
  * `needs-corroboration`;
  * `open`: no writer sets it, and it is kept pending your call on retiring it;
  * `silent`;
  * `withdrawn`;
  * `resolved`: cleared for inclusion in analysis.
* Gate 2 uses `resolved` for "carried by a current claim" and `open` for "held on an open item".
* The checklist wants a `superseded` status, which the enum lacks: superseding sets `withdrawn`.
* No status flow says who sets each value.

|Option|What it means|
|-|-|
|**A**|Keep #1782's meanings for `status`, as a quality lifecycle. Gate 2 records its placement elsewhere (the claim source link, and a disposition note), not in `status`.|
|**B**|Redefine `status` as the reading's lifecycle:|

* `draft`: recorded at gate 1;
* `resolved`: carried by a claim;
* `open`: held on an item;
* `silent`: assessed, not for the narrative;
* `withdrawn`: wrong, or superseded, with the successor named;
* `needs-corroboration`: below the rules, to be read again.

A `cfg\_status\_flow` for `ib\_observation` says who sets each value. |
| **C** | Two fields. `status` keeps the quality lifecycle (is the observation up to the rules?). A new disposition field holds gate 2's placement (carried, held, silent, data). Both get a status flow. |

**Claude's view (inferential):** C. Whether an observation meets the rules and where it went are separate facts. Under A or B one of them is lost, and R13 needs the first to find quality gaps.

**Decision R14:** \_\_\_\_\_\_

\---

## R15 One rule set for every observation write

**Under the phases (v3):** D1, D2 and D4 all write observations. R1 puts the checklist into config.

**In tension (C19, C7, P26, P29; W37):** `iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md` calls itself the one place for every rule on writing an observation, but it is a document, written for routes D1 and D2, and not updated since 2026-09-16. Its cross-cutting rules (§0) are:

* one writer, and the recording pass decides edit or new;
* a fixed run structure;
* verses resolved fresh;
* flags carried, not resolved inline;
* can't-resolve recorded;
* node coverage checked twice;
* relations only on evidence.

They are not in config, except in part. The reading writes observations by a path that skips the recording pass's similarity match and does no coverage check.

|Option|What it means|
|-|-|
|**A**|The checklist's rules go into config as the rules for every observation write, delivered at every tool that writes one, `Reading.ps1` included. The reading's Record goes through the same checks: verses resolved fresh (it already does), the new-or-edit decision made against the existing observations on the same verse and word, the coverage of the scope's words checked (P29), relations only on evidence. The checklist is archived (R1).|
|**B**|Two rule sets in config: the API routes keep the checklist's rules, and the reading gets its own.|
|**C**|As now.|

**Claude's view (inferential):** A. One record should have one set of rules, whoever writes it.

**Decision R15:** \_\_\_\_\_\_

\---

## R16 Where a reading's observation is homed

**Under the phases (v3):** This is D4 observe. It is unchanged by the phases.

**In tension (C24):** every observation a reading records takes the reading's `home\_cluster` as its `cluster\_code`. The role guide (§4.8) says a verse's home follows its main operation: the cluster of the word that is the characteristic in that verse, which may differ verse by verse.

|Option|What it means|
|-|-|
|**A**|Each observation is homed by the main operation of its verse, as the reading records it. The reading's `home\_cluster` names only what the reading is anchored on.|
|**B**|As now: the reading's cluster for every observation.|

**Claude's view (inferential):** A. Under B the 2Pe 2:13 case (guide §6) would be homed under M18 (pleasure), the outcome the guide was written to prevent.

**Decision R16:** \_\_\_\_\_\_

\---

## R17 Whether a reading answers the question catalogue

**Under the phases (v3):** This follows R3c: the catalogue is D1's and D2's question set.

**In tension (overlay §2.OBS):** the question catalogue (`wa\_obs\_question\_catalogue`, 116 rows in iba.db) gives routes D1 and D2 their questions. Through it they record a question code, a window and a meaning source on each observation. 10,595 Stage 1 and 748 characteristic observations carry one. A reading answers no catalogue question, and its observations have no question code, window or meaning source. The catalogue's own config text is out of date (C21).

|Option|What it means|
|-|-|
|**A**|The reading answers catalogue questions: its record carries a question code, window and meaning source, and the catalogue is the reading's question set, with the role guide's sequence set against it.|
|**B**|The catalogue stays with routes D1 and D2. The reading's record follows the role guide (R9, R16), and it reads the catalogue answers already recorded as part of what is known.|
|**C**|The catalogue is retired with the routes it serves (if R3 retires them), and its rows and answers are kept as history and as sources.|

**Claude's view (inferential):** this follows R3. If Stage 1 stays as an input (R3 A), then B. If the reading is the only route (R3 B), then A or C, and that is a method choice for you.

**Decision R17:** \_\_\_\_\_\_

\---

## After the rulings

Claude records your rulings verbatim on #2268, then writes the alignment design for your approval before any change. The design will:

* put the phases and the reading rules into config (R3a to R3d, P32);
* carry the whole guide, the observation rules and the hard-coded rules into config (R1, R9 to R12, R15, C25);
* replace B:84 (R2);
* set up gap discovery and gap analysis in 0.GAP pre and post (R13);
* align the observation record (R14, R16, R17);
* reword the era configs (W1 to W37);
* settle the conflicts (C1 to C26);
* fill the gaps (P1 to P32).

