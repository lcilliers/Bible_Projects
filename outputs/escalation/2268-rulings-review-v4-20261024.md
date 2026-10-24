# \#2268 Rulings review (v4): R1 to R12 decided, except R5 and R6 rephrased; R13 to R19 reformulated

**Date:** 2026-10-24 · **Escalation:** #2268 · **For:** the researcher's rulings on R5, R6 and R13 to R19, before the alignment design. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"you can process R4 - R12.  I have not done R13-R17.   R13 is not in keeping with I described as the gap analysis yesterday - it looks like you got confused.  Gaps are related to the missing items in the tables. R13 is not formulated around this.  R14-R17.  It looks like the ledger work you did in the last few days got lost, and got confused with the catalogue work in the past.  I am now confused about you have done in the ledger work and how does in correlate with the observations."*

**Sources.**

* **Your rulings, verbatim:** #2268 v13, v15 and v16. Your annotated files are in `outputs/escalation/archive/` (`…-v1-…-researcher-feedback.md`, `…-v3-…-researcher-rulings.md`).
* **The account of the ledger work and the catalogue work:** `outputs/escalation/2268-ledger-work-and-observations-v1-20261024.md`. Read this first: it is the footing for R14 to R19.
* **The process and its reading rules:** `outputs/escalation/2268-analytic-process-and-reading-plan-v1-20261024.md`.

## 1\. Decided

|#|Your ruling (in short; verbatim on #2268)|What follows for the design|
|-|-|-|
|R1|Rules in config: no operating rule in scripts, and no choice left to interpretation. A file is the authority only with a config pointer (the programme and IB definitions)|The guide, the checklist and the method files go into config; the hard-coded rules too (C25)|
|R2|B:84 retired and replaced by configs (`whole\_cluster\_reading\_start`); backfill becomes gathering work already done|RO3, RO8|
|R3a|B: D1 and D2 run per word and cluster on their own schedule; a reading gathers their results|0.GAP pre gathers D1 and D2 results|
|R3b|A: D3 reads the current claims on the scope||
|R3c|B: Claude reads in a session, on demand from the tables. The API read was tested and found not cost-effective|The API steps are retired, and their rules carried into config where they still hold|
|R3d|A: RO1 to RO9 adopted|They become config rows|
|R4|None of A, B, C. The narrative style is predefined in config. Every block fits the flow and context of its chapter's story, and the chapters follow a story. Turning claims into narrative, and weaving, is Claude's call, with no approval before publishing. You read the chapters in context and correct through Claude. The current B rules on this topic are retired or replaced|The style guide goes into config (R1). Each block is checked against the chapter's story and style. B:72's narrative sentence, B:85, B:86, B:87, B:88, B:90 and B:91 are reviewed for retirement or replacement in the design|
|R7|B: a reading's files go under its home cluster's folder (`\_analytics/Clusters/<home>/readings/<label>/`)|`reading.output\_dir` changes. **New point (C27):** `reading\_index.roots` indexes `\_analytics/Clusters`, so a reading's own files would be indexed as earlier file readings; the design must exclude them|
|R8|A: the passage tables stay in iba.db; research\_db stays prose-only; B:13 corrected||
|R9|C, and "Glossary must be kept up to date. Nothing in the project is inforcing it."|Controlled values in `cfg\_enum` and `cfg\_column`, each pointing to its glossary entry. **New gap P33:** nothing checks that the glossary is current|
|R10|A: worked examples live in config and are kept current with the rules. The four in the guide are from a previous era|A config table of examples, each tied to its rule; the four are restated or replaced|
|R11|B: take what is relevant from the July method file into config, then archive it. Genre is no longer written to any table, and there is no book reading||
|R12|B: a generated guide, never edited by hand. You will review it after all the rules are restated, because you are "not convinced that it is co-herent, complete and not confusing"|A review of the generated guide is a step of the design's close|

## 2\. Open: R5 and R6, rephrased

### R5 Where a verse ends up after a reading, and in what words

**In practice.** When a reading is done, every verse it read must end up somewhere you can see:

* told in a chapter;
* carried by a claim;
* held on an open item;
* assessed but not for the narrative;
* or only the setting of another verse.

Two places record this today, in two vocabularies:

* **In the reading's file** (the October way): a "Placements" table in each reading, account or ledger *file*, one row per verse, with one of the words told, claim, data, forward OT-nn.n, held #nnnn, parked, context. Session-close checks these tables (B:79), but only in `\_analytics` files.
* **In the tables** (the reading process): an observation is `resolved` (a claim carries it), `open` (held on an item), `silent` or `withdrawn`; a claim is told in a block, or held.

**For example:** a verse read in the M64 reading `m64-plan` has its observation's status and its claim's telling in the tables, and no Placements table, because `Reading.ps1` writes JSON, not a reading file. A verse read in the October anger ledger has a Placements row in the file and, since the catch-up, an observation in the tables with status `draft`.

|Option|What it means in practice|
|-|-|
|**A My understanding is that the thread / ledger method tested a new approach towards scoping the reading of the verses and that what you have placed in the ledgers for the verses will find its way to the observations and claims with entries in some of the underlying tables also. My expectation is that the thread reading (or any other scoped reading will create observation entries for reading of the verse. where the observations for the verse is already done, it will take that as input and add additional observations if needed. what need to be recorded and how is to be defined in the section about the observations**|Record it in the tables only, with one set of words: told, claim, held (on an item), data (assessed, not for the narrative), context (the setting of another verse), withdrawn. The Placements tables stay only in the October files that are still to be gathered, and retire as those files are gathered.|
|**B**|Keep the Placements table in every reading's file as the record, beside the tables.|

**Claude's view (inferential):** A. You see one answer in one place, and session-close checks the tables instead of the files.

**Decision R5:** \_\_\_A\_\_\_

### R6 B:68: what it is for, and whether to keep it

**What it is for.** B:68 was written in September for Stage 1, the API route. Its point: an observation written from an LLM answer may be corrected only by asking the LLM again for that exact occurrence, and the recording pass then replaces the row. No script may edit or derive such rows directly. The recording pass decides whether a new answer is the same, a broadening, or new, by text similarity, against the threshold `cluster.recording\_similarity\_threshold` (the "setting"). That is how 4,953 Stage 1 rows came to be withdrawn.

**Why it gets in the way.**

* With R3c, the API route is retired, so the correction B:68 requires (a fresh LLM answer) has no live path.
* The rule also stands against the reading process, which writes and disposes of observations through Claude's reading (overlay C7).

|Option|What it means|
|-|-|
|**A**|Retire B:68, and the similarity threshold with the API route. Keep its one lasting point in the observation write rules (R15): no observation is changed except by a reading, and every change is recorded with its reason.|
|**B**|Keep B:68 for the existing catalogue rows only, as they are gathered.|

**Claude's view (inferential):** A. Once the API route is retired, B adds nothing.

**Decision R6:** \_\_\_\_A\_\_

## 3\. Open: R13 to R19, reformulated

### R13 Gaps: missing items in the tables

**Your definition** (2026-10-23, #2228 v32 D.1, and #2161 v8):

* a gap is an item missing from the tables for the scope;
* the gaps are recorded in a structured JSON with a section for each gap type, so that every type is considered;
* each item is recorded by writing the missing item into its table, with the table id written back into the JSON;
* the gap types are learned as the work goes on;
* gaps are determined before the claims, and the claims are then finalised from the tables;
* the first gap found for M72 was that every verse lacked an observation.

**What is built already** follows this for five types:

* not read;
* read in files only;
* strand hit unread;
* meaning missing;
* open item;

and for two at the claims: observed with no claim, and claim not told. Each type is in `reading.gap\_types`. What is missing is the full list of the items the tables should hold.

**R13a The gap types: the items the tables should hold for a scope.** A candidate list, by phase:

|Phase|Gap type: the item missing|Recorded in|
|-|-|-|
|0.GAP pre|a base datum: span, Strong's, meaning in each of the three sources|routed to recovery: New-Word, `raw.backfill\_meaning`, the spine|
|0.GAP pre|a word occurrence with no word-level result (D1)|`ib\_observation` / `ib\_node`|
|0.GAP pre|a word with no place among its cluster's characteristics (D2)|the cluster and subgroup tables|
|0.GAP pre|an earlier reading in a file, not in the tables (`read\_in\_files\_only`)|`ib\_observation`|
|0.GAP pre|a face recorded on a strand hit, not carried into the record (R18)|per R18|
|0.GAP pre|an open item on the scope with no response|the item's response|
|D4 observe|a verse with no observation (`not\_read`)|`ib\_observation`|
|D4 observe|an M-coded word in a verse with no role|the record field (P9)|
|D4 observe|a verse with no main operation, parties, route or home|the record fields|
|D4 observe|a word occurrence with no face|the record field (R18)|
|0.GAP post|an observation carried by no claim and not disposed|the claim source or the disposition|
|0.GAP post|a claim told in no block and not held|the telling|
|0.GAP post|a claim resting on verses only, with no observation (303 current claims today)|the claim source|
|0.GAP post|a verse cited in a block with no claim and no observation behind it (B:77)|a claim or an observation|

|Option|What it means|
|-|-|
|**A** |Adopt the list as the starting template in config, with new types added as they are learned.|
|**B the list is by enlarge right, but not specific enough.  on verse read: all verse related observations (face, role, operation, parties, route, home) all expected to be in the observations for each M-code and for T-codes that turns out to be relevant.  term gaps if they are not in a cluster (term-cluster) or does not have meaning (missing meaning); It is important to note that the term reading result for the verse (e.g additional meaning information that is relevant, surface variants, related terms etc. all goes into observations) ; next is GAP post which will be checked and update against the claims.   Any unresolved GAPS and GAPS that require further work goes into open items.  GAPs are measured against the expectations. mere presence of something, but not necessarily the right thing is not a resolved gap.**|Adopt with changes: write them below.|

**R13b When an item exists but lacks what the rules require.** For example, an observation with no role for its words.

|Option|What it means|
|-|-|
|**A GAPS is about quality, and yes, if a part is missing it is a gap to  be addressed.**|Each required part is an item of its own, so a missing part is a gap of its own type (as in R13a's D4 rows).|
|**B false**|Only a whole missing row is a gap; a row short of the rules is a separate quality finding.|

**R13c Seeing the gaps across the study.**

|Option|What it means|
|-|-|
|**A The json for the scope is recording of the gaps as they are being discovered. the json must be processed into the tables as soon as the stage is completed and before the next gate is started.  GAPs are usually only processed for the scope and not across the whole study or cluster or book.** |A reading's gap JSON is the record of its gaps (D.1). A study-wide view is the same gap analysis run read-only over a wider scope (a cluster, a chapter, the whole study), as a report.|
|**B True - for all the items in the scope**|Only per reading.|

**Claude's view (inferential):** A for each. R13b A keeps your one idea: what the rules require is an item, and its absence is a gap.

**Decisions:** R13a \_\_B\_\_\_\_ R13b \_\_\_A\_\_\_ R13c \_\_\_B\_\_\_

### R14 One lifecycle for observations

**In tension (the ledger account §1, §5):**

* The catalogue rows use #1782's statuses: `draft` until looked at; `resolved` once cleared for analysis.
* The ledger rows are imported as `draft`, and a reading sets them `resolved` (carried by a claim) or `open` (held on an item).
* With the API retired, #1782's meanings have no live writer.

|Option|What it means|
|-|-|
|**A**|One lifecycle for all observations, as the reading uses it: `draft` (recorded, not yet through claims), `resolved` (carried by a claim), `open` (held on an open item), `silent` (data: assessed, not for the narrative), `withdrawn` (wrong, or replaced, with the successor named). The catalogue rows are read on this lifecycle as they are gathered. `needs-corroboration` is retired, or kept for a row 0.GAP finds below the rules. A status flow in config says who sets each value.|
|**B Verses can be included in a scope from various angles (e.g. by cluster group, open item, and each scope may add additional observations for the verse (e.g. the role that a specific M-code or T-code plays). That is the whole reason that the observations of a verse is all read into the focus when a verse are read to allow the scope objective to evaluate against what has already been read.**|Each body of work keeps its own meanings, by stage.|

**Claude's view (inferential):** A. One record should have one meaning per status.

**Decision R14:** \_\_\_\_B\_\_

### R15 Which method's rules govern an observation

**In tension.** The ledger observations were made by the October method: the strand rules and the role guide. The catalogue observations were made by the September checklist. My earlier R15 offered the checklist for every write, which mixed the two (the ledger account §5).

|Option|What it means|
|-|-|
|**A My understanding is that the ledger observations in real terms are the catalogue items without answering each catalogue question. the 700+ verses already done through the catalogue should not be put aside, but when the verse comes in focus, the observations that are missing in terms of the ledger method must be added. Any observations that is no longer supported must be soft deleted. my expectation is that the ledger method will use the catalogue as a guide for the areas of exploration.** |Every observation written from now on follows one method: the reading method (the role guide and the strand rules, restated for readings and put into config under R1). From the September checklist, only the rules that still hold carry over: verses resolved fresh at write time; flags carried, not resolved inline; can't-resolve recorded; relations only on evidence. The rest is archived.|
|**B**|Each body of work keeps its own rule set, by stage.|

**Claude's view (inferential):** A.

**Decision R15:** \_\_\_A\_\_\_

### R16 Where a reading's observation is homed

**Unchanged from v3.** Every observation a reading records takes the reading's `home\_cluster`, while the role guide says a verse's home follows its main operation. The ledger work homed its observations by the strand's cluster, so the same question applies to it.

|Option|What it means|
|-|-|
|**A**|Homed by the main operation of its verse.|
|**B each scope should have a clear objective of reading - that defines its home.  if a verse have multiple M-codes or T-Codes in focus then I expect multiple rows in the observation.  Note that the rule of no duplicate rows, applies. I expect to see a single observation to have multiple nodes to signal that the observation applies to multiple verses or terms etc.**|Homed by the reading's (or strand's) cluster, as now.|

**Claude's view (inferential):** A.

**Decision R16:** \_\_\_B\_\_\_

### R17 The question catalogue, now that the API route is retired

**In tension.** The catalogue (116 questions) was the question set of the API stages. It has 6,527 live answers (5,642 Stage 1, 885 characteristic) on 718 verses. The ledger work never used it.

|Option|What it means|
|-|-|
|**A**|Retire the catalogue as a question set. Its answers stay as work already done, gathered in 0.GAP pre as D1 and D2 results.|
|**B the questions are very relevant, but what has changed is to process of forcing answers to questions that does not apply, or manufacturing answers that is not evident from the verse. the questions are prompts or guidance.  The focus is on understanding what the verse context is in relation the IB.**|Keep it as the question set for D1 and D2, read in a session (R3c).|
|**C**|Retire it, but carry the questions that still serve the reading method into the D4 record (for example the word-level meaning questions M0.1 and M0.5 as the word's meaning in context).|

**Claude's view (inferential):** C. It keeps what was useful in the questions, and gives the record one shape.

**Decision R17:** \_\_\_B\_\_\_

### R18 The ledger faces (new)

**In tension (the ledger account §2.5).** 4,239 faces are recorded on `reading\_strand\_hit`, one per word occurrence, for four strands now superseded, and only 111 are linked to an observation. The ledgers' part A (faces by party) has no table. A reading does not show these faces to the reader.

|Option|What it means|
|-|-|
|**A If you closely look you will see the concept of a face as per the ledgers is already part of the catalogue, just using different terminology**|The faces become part of the observation record (the face of each occurrence: guide §4.7, P10). The 4,239 are gathered into it as work already done.|
|**B**|`reading\_strand\_hit` (renamed, no longer tied to strands) stays the home of faces, one per occurrence. 0.GAP pre gathers it, and the reader sees it.|
|**C**|The faces stay where they are and are not carried forward.|

**Claude's view (inferential):** B. A face is per occurrence, which is that table's grain, and its 4,239 rows need no conversion.

**Decision R18:** \_\_\_A\_\_\_

### R19 The findings of #2260 to #2267 (new)

**In tension (the ledger account §5).** #2260 judged the ledger observations against the catalogue's rules (no question code, multi-verse, no Stage 1 coverage), and #2261 to #2267 were raised on that footing. The ledger observations' own method is the strand rules and the role guide.

|Option|What it means|
|-|-|
|**A the thread analytic method is using an amalgamation of the ledger method and catalogue method to prompt the reading of the verse. the focus is on the scope and each item in the scope, but the points to be explored stay largely the same.**|Restate #2260 to #2267 against the reading method once it is in config (R15): what each ledger observation lacks by that method (role, face, parties, route, home) becomes a gap under R13. Findings that rest only on the catalogue rules are withdrawn.|
|**B**|Keep the findings as they are.|

**Claude's view (inferential):** A.

**Decision R19:** \_\_\_\_\_\_A

## 4\. After the rulings

Claude records your rulings verbatim on #2268, then writes the alignment design for your approval before any change.

