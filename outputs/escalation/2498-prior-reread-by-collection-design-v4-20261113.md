# The documents' work built into the collection reading (design v4)

Escalation #2498 (raised under the researcher's ruling of 2026-11-13 on #2484). Status: **the pilot is done; the collection-reading part is carried by #2448. Revised to your decisions of 2026-11-13. Nothing has been built, no document has been read, nothing in `iba/app/db/iba.db` has been written.** Everything here comes from the tables and the code, read only. Counts marked *(inferential)* are my forecasts, not queried facts (B:4); each is replaced by a counted figure before any write.

Rules this design obeys: the node rule (behaviour rule 130, `nodes-index-the-collection-and-comply-with-the-node-rules`), the observation rule (131, `observations-are-founded-unique-and-fit-the-node-rules`), the collection rule (129), the collection-is-the-unit rule (127), and your rulings N1 to N15 and 4.1 to 4.6 in `outputs/escalation/2484-node-and-observation-rules-v2-20261113.md`. Read before writing: `iba/app/CHARTER.md`, `iba/app/GOVERNANCE.md`, `iba/app/USER-GUIDE.md` sections 7.2, 7.4 and 8.2, `iba/app/lib/priorcapture.py`, `iba/app/lib/observationrecord.py`, `iba/app/lib/nodecheck.py`, and the live `cfg_setting` and `cfg_method_rule` rows.

**Your decisions of 2026-11-13, restated so you can correct them:**
1. **The documents' work is brought into the collection reading, not run as a separate campaign.** The collection method gets access to the documents that reference the verses and surfaces in the collection's scope. The documents are read **only for those verses**, never as general documents.
2. **No bulk re-read of the other documents before the collection reading starts.** A document is read, line by line, when a collection that its lines name is taken up.
3. **The two drafts already prepared** (document 92 and the fear ledger, document 8) **are processed into the observations now**, since the work is done and valuable.
4. The reading is a **value-adding operation**: it enriches and corrects the existing observations in place, adds what is missing, and lists gaps in the collections (words a document names that match no collection surface, including where the surface differs from the document's word). It does not replace or disprove the earlier observations.
5. An old observation is soft-deleted only if, after this, it makes no sense and cannot be revived, with your approval at each stage.

The drafts are `outputs/escalation/2498-pilot-sample-m18-group-g-reading-draft-v1-20261113.json` and `outputs/escalation/2498-pilot-sample-fear-ledger-unit2-draft-v1-20261113.json`; the plan for processing them, with counts, is `outputs/escalation/2498-pilot-processing-plan-v1-20261113.json` and section 5. Nothing has been written to the database.

---

## 1. What the old capture did, and why it failed

### 1.1 What it did

The capture tool (`iba/app/lib/priorcapture.py`, run as `iba/app/ps/Prior-Capture.ps1`, designed in `outputs/escalation/2305-prior-work-capture-design-v2-20261026.md`) worked **one whole document at a time**, in a chat session, in three steps: *Prepare* (the document's lines that name a verse, with the M- and T-coded words of each verse), *Fill* (Claude wrote findings and an answer for every line), *Record* (written whole or refused whole). Its method rules, on step `prior_capture.record`:

| Method rule | What it required |
|---|---|
| every-verse-line-is-answered (CP-01) | each line naming a verse gets one answer: captured, already recorded, or not an observation |
| capture-as-written-no-reanalysis (CP-02) | record what the document says, as written; the verse is not read again; nothing added, checked, corrected or rejected |
| one-finding-many-nodes (CP-03) | one finding is one observation; verses, words, clusters, subgroups are nodes |
| no-duplicate-check-across-documents (CP-04) | no search for duplicates across documents (your 2026-10-26 ruling, to save overhead) |
| node-classification-from-the-word (CP-07) | a node takes strong, occurrence, cluster and subgroup from the tables |
| nodes-on-m-coded-words (CP-10) | a node on each M-coded word the finding's text names, with that word's own cluster |
| clusterless-documents-last (CP-09), chat-sessions-no-api (CP-08), parts-already-recorded-skipped (CP-05), unfitted-tag-for-the-rest (CP-06) | order, route, October ids, and a tag for what fits no kind |

What it produced (queried 2026-11-13): 15,574 lines answered in the 179 captured documents and 3,538 in the 52 "nothing to capture" ones (19,112 rows in `prior_capture_line`: 13,376 captured, 717 already recorded, 5,019 not an observation); 8,045 observations written, **6,709 still live**, with **46,471 live nodes** (6.9 per observation, the largest 137).

### 1.2 Why it failed (the evidence, from the node checker run over the 6,709)

| Failure | Cause in the method | Evidence |
|---|---|---|
| The text reads badly | The unit was the **document line**, and the wording was adjusted only "to fit the structure" while the document's own wording was kept. A table row, a citation list or a heading-plus-clause became an observation. | 869 observations contain a table bar `\|`; 859 start with a verse reference; 300 begin "What it leads to…" or a similar document label. Example, observation 19914: *"Deu 2:30 \| Ch 6 v10 quotes the will word … \| Carried for the will reading since #1986."* |
| It repeats the verse | Findings were built from quotations the document gave as evidence; nothing tested the text against the verse. | 3,214 of 6,709 (48%) are flagged by the checker as repeating more than 7 consecutive verse words (`O-verse-copy`, a candidate list to be read by hand, not yet a verdict). 5,089 contain a quotation. |
| Nodes mean the wrong thing | The node went on **every M-coded word the text names** (CP-10), with the role chosen as "characteristic, qualifier or standalone". Standalone was used to mean "named in the text". Under the new node rule it means "recognised, with no inner-being role". | 20,429 of 46,471 nodes (44%) are standalone; what they mean cannot be trusted either way. |
| The collection is missing | The tool ran on cluster and subgroup, which were the structure at the time. Collections did not exist. | 3,749 nodes without a collection; 570 observations none of whose nodes carries one. |
| Over-splitting and no join | No duplicate check across documents (CP-04), and one observation per table row (`m18-group-B-verb-split-v1-20261009.md` gave 76 observations of one node each). | `O-duplicate-text` found 1 (the writer refused identical text only); near-duplicates across documents were never looked for. |
| A kind that carries no information | Eight kinds were filled by one pass per line. | 5,701 of 6,709 (85%) are `statement`. |
| One pass, whole documents | A document of 217 KB and 1,101 lines (`wa-cluster-M02-unit2-phenomena-v3-20260929.md`) was filled in one run. | No step let a reader check one collection's evidence at a time. |

The main cause, in one sentence: **CP-02 made the tool a transcriber of document lines, and the unit it worked by (cluster, subgroup, line) is retired** (the node rule says clusters and subgroups play no part in nodes and observations; their retirement from the code is #2495). The result passes the structure checks poorly: 4,136 of 6,709 have at least one checker finding, 2,573 have none.

What was good and is kept: the documents' work, the line-by-line accounting (`prior_capture_line`), the writer's all-or-nothing record, the document index (`reading_file`, sha256 checked on every Prepare), and Claude reading and filling in a chat session (CP-08; B:127 forbids a bulk or model pass).

---

## 2. The method: the collection reading gets the documents' lines for its verses

### 2.1 The unit

The unit is the collection (B:127), and the work is part of the collection's own reading, in the same sitting. When a collection is taken up, its reader is given, for each verse in the collection's scope, what the documents say about that verse. A document is never read as a whole: the reader sees only the lines that name a verse of the scope, with the section heading and the neighbouring lines for context. A document line that names verses of several collections is seen once for each collection, when that collection is taken up.

### 2.2 What the reading sheet gives the reader (an addition to the existing Observe step, reads only)

The reading process already puts each verse in hand with a sheet built from the tables (`iba/app/ps/Reading.ps1 -Step Observe`, section 8.2 of `iba/app/USER-GUIDE.md`): the verse text, its surfaces, and the existing observations with their nodes, each existing observation taking an action to fill (accept, modify, merge, delete). The addition is two blocks on that sheet:

1. **The documents' lines for the verse (new).** From the reading index (`reading_ref`): every line of every indexed document that names the verse, with the document, line numbers, section heading and the neighbouring lines, and the old answer for the line (`prior_capture_line`: answer, reason class, observation ids). The old answer is shown for reference, never copied. A document changed since the index (sha256) is refused with the instruction to rebuild the index.
2. **Words the documents name that no collection surface matches (new, see 2.7).**

The sheet already shows, per verse, what is live: every observation of any stage with a node on the verse, with what each lacks (role, collection, occurrence). That is how the reader sees that a ledger's findings are already recorded and the work is to improve them.

### 2.2a What the reading does not need

No new Prepare or Record tool is needed. The existing Record already applies an action to an existing observation or node **in place** with the before, after and reason kept in `ib_observation_change` (`modify_observation`, `modify_node`, `merge_observation`, `soft_delete_observation` and `write` with `existing` in `iba/app/lib/observationrecord.py`). The build is the two sheet blocks, and a loader for the two prepared drafts (section 5).

### 2.3 Fill: what the reader (Claude, in a chat session) does with a pack

For each collection in the pack, from the document's lines and the verses (read first, B:116):

- Write each **finding the document makes about a verse** as an application or analytic statement in the reader's own wording, founded in the verse, never repeating more than 7 consecutive verse words (`reading.observation_items`, `max_verse_words_copied`), tied to the verse and surface it concerns. The document's meaning and implication are kept; its table, bullet or heading framing is dropped; a quotation is shortened to what the point needs.
- Keep the document's **basis**: stated where the verse says it; read where the document reads it (grounds are then required, as the item rules already say).
- Give each finding **a node for each variant it concerns**: each verse, surface, Strong's code and collection (B:130). The reader names the **occurrence** (`verse_lexical_id`) and the **role**; the writer fills surface, Strong's code, morph code and collection from the occurrence and the surface's one collection. A word recognised with no inner-being role in that verse is `standalone`; a role is never taken from a cluster tag.
- Put entity and other words of an in-scope verse on the observation that covers them as **supportive nodes**, carrying the collection of the surface they support (your ruling 4.3).
- Never split one finding by table row or by quotation; two observations only where the document says two different things.
- **An observation that already exists for the line (any stage) is improved, not repeated.** The reader decides, by reading the document and the verse, one of: *enrich* (the existing statement is thin, a label or a one-liner, and the document says more that the verse founds: the text, meaning and basis are restated; nodes the document's verses or words call for are added; every node gets its role and collection), *correct* (the existing statement, a role, an occurrence or a collection is wrong against the verse: it is corrected, with the reason), or *leave* (it is already right). Where the same meaning stands live under several observations, the duplicates are joined (B:131).
- **A finding the document makes that no existing observation holds is added** as a new observation, with its nodes.
- A claim that rests on other verses or on the document's own synthesis, and that the cited verse does not found, is **not an observation** (B:131). It is listed in the document's report with its line, stays in the document and goes to the claims step. It is not written with a softer label.

### 2.4 Record: what the existing Record does with the sheet (through `observationrecord`)

Written whole or refused whole, as before. It refuses a document unless:
- every line that names a verse has an answer (section 3);
- every node's occurrence is in the node's verse, and surface, Strong's, morph and collection agree with the occurrence and the surface's one collection (the node checker's checks, run on the plan **before** writing);
- no observation repeats the verse text, and none is a second live observation with the same text (the join rule is applied, not only refused);
- every observation has at least one live node, and every node a role judged by the reader.

**New observations** are written with stage **`prior-reread`**, status `draft`, `stable_key` `<reading_file_id>:L<first line>:<collection id>` and a `revisit_note` naming the document, its lines, the collection and the run. **Existing observations that are enriched or corrected are changed in place** through `observationrecord` (their stage is kept; the `revisit_note` gains the re-read reference), with the before and after and the reason in `ib_observation_change`, so the reading's work is traceable and an enrichment can be reversed. Added nodes are written by the same call. Every write goes through `observationrecord` (RW-01).

### 2.5 The method rules (applied only on your approval, as `cfg_method_rule` rows through `configmaint.apply_logged`)

| Old method rule | Fate | New rule |
|---|---|---|
| capture-as-written-no-reanalysis (CP-02) | replaced | restate in the reader's words, founded in the verse; document claims the verse does not found are listed, not written |
| no-duplicate-check-across-documents (CP-04) | replaced (your 2026-10-26 ruling was about overhead; B:131 now says one meaning is one observation, and the pack makes the join cheap) | join the live observation of the same meaning |
| node-classification-from-the-word (CP-07), nodes-on-m-coded-words (CP-10) | replaced | a node per variant, from the occurrence; collection from the surface; role judged per finding; no cluster or subgroup |
| clusterless-documents-last (CP-09) | void | clusters are retired; every document is read for its collections |
| every-verse-line-is-answered (CP-01), chat-sessions-no-api (CP-08), unfitted-tag-for-the-rest (CP-06) | kept (CP-01 extended to an answer per collection) | |

### 2.6 Dependencies on existing code

- `iba/app/lib/observationrecord.py` today **refuses a node whose Strong's code sits in several clusters unless the cluster is named** (lines 252 to 259) and writes `ib_node.cluster_code` (NOT NULL, history). A re-read by collection must not ask the reader for a cluster. That is the part of #2495 (retire cluster and subgroup from node and observation code) this build needs first: the writer fills the history column itself, without refusing. I propose to do that small part within #2495 and not widen it.
- The tag `unfitted` and the eight kinds stay (your ruling N13: no aim of consistent parts).
- No Ollama or API route (B:124 not engaged); the work is not run as one background job (B:127): each document is a chat step, and you see its report after it.

### 2.7 Gaps in the collections (new)

Your concern is words that are not found. The two samples show the ways a named word is missed, so the tool tests for each and lists the result; it never changes a collection.

For each word a document names (a quoted or italic word, a bracketed gloss, a Strong's code, a transliteration), in each verse of its line, Prepare tries, in this order: (1) the same surface in `verse_lexical`; (2) the same Strong's code where the document gives one; (3) the gloss in the STEP lexicon of an occurrence in the verse; and reports the result as one of:

| Result | What it means | Seen in the samples |
|---|---|---|
| matched, in a collection | the normal case; the node carries the surface's collection | most nodes |
| matched, surface differs from the document's word | the occurrence exists but STEP set the surface on a neighbouring English word (the ledger says so itself for Mic 7:17, Gen 27:33, Psa 14:5 and 53:5, Job 3:25) | Gen 27:33 "violently" and "said" for the trembling words |
| matched, in no collection | the occurrence is found but its surface is not a member of any collection (group other or entity) | "thrill", "shocked", "stirred up", "roused", "wrung", and the document's own subject words in the small reading: "far", "long", "gathered" |
| not matched, no such occurrence | no occurrence in `verse_lexical` carries the code or the gloss | Job 23:16, Dan 10:10, Psa 48:5, Jer 33:8, Isa 32:9 for the dread words |
| verse missing | the verse is not in the `verse` table | Mark 12:39 |

The gap list is one file per document, and one consolidated list for the collections work (#2463). A node on a "matched, in no collection" occurrence is a supportive node carrying the collection of the word it supports (B:130). Where nothing in the verse can carry a collection, the node is not written and the line is listed, so no collection is assumed. **The re-read adds no surface to a collection:** a surface that should be a member is the collections work's decision, brought to you with its evidence.

---

## 3. How each document line is accounted for

The old table `prior_capture_line` (19,112 rows) stays untouched, as the old answer. A line is answered when the collection it speaks to is read; a document is complete when every line has an answer for every collection it speaks to. A new table `reread_line` (to be registered in `cfg_table` and `cfg_column`, with a write grant and a step) holds one answer **per line and collection** (a line that speaks to two collections has two rows; a line that speaks to none has one row with no collection):

| Answer | Meaning |
|---|---|
| `added` | a new observation (id) for that collection |
| `enriched` | an existing observation (id) was restated or given nodes, roles or collections |
| `corrected` | an existing observation or node (id) was corrected, with the reason |
| `already right` | an existing observation (id) already holds the finding and needs nothing |
| `not founded in the verse` | a document claim about a verse that the verse does not found, listed in the report with the claim |
| `not an observation` | with a reason class (the old classes: heading, reference list, hit count, surface or gloss table, scope or method record, pointer with no content, weave or quote-check record, next-steps list); a heading's route is carried to the findings under it |
| `out of scope` | the line's verses hold no member surface of a live collection (B:130: not touched) |

**Every line is answered, per collection.** the reading Record refuses the document while any line has no answer. The report for a document lists: lines by answer; for each enriched or corrected observation the before and after; old answer against new answer where they differ, with the reason; the gap list (2.7); the claims listed as not founded; quotations not found in the ESV text; references that resolve to no single verse (as the old report did). Nothing is written for a node with no occurrence.

`reading_file` gains a second status for the re-read (`reread`, `reread partly`), set by Record, so the index shows where the re-read stands; the old `capture_status` is not changed.

**The 52 "nothing to capture" and the 4 "not started" documents.** The 52 are worksheets, passage lists, validation registers and data documents the old tool passed over (3,538 lines answered). I have not opened them. A worksheet may hold per-verse evaluations that are findings. See decision Q5. Of the 4 "not started", two are the 267 KB `cluster-assign` files with no verse lines, one is a 1.7 KB file with none (`m10-family-synthesis-L_defilement-20260911.md`), and one is `1682-test-m10-process-c-H_guilt-v1-20260911.md` (12 lines, 39 verses in scope).

---

## 4. How the new observations are checked

1. **Before the write** (inside the reading Record): the checks in 2.4, as a refusal list, nothing written.
2. **After each pilot and each batch**, `pwsh iba\app\ps\Node-Check.ps1 -Step Report` (about 5 seconds, reads only). It needs a small addition: a `-Stage prior-reread` filter, so the new stage's report stands alone beside the whole-table one (a change to `iba/app/lib/nodecheck.py` and `iba/app/ps/Node-Check.ps1`, with its method rule and test, after approval). **Pass criterion for the new stage and for every observation the re-read enriched or corrected (listed by id in the run; the checker is run on them as well, before and after, so the improvement is counted):** zero findings on every node check (no occurrence, no collection, no role, collection disagrees, duplicate, out of scope) and on every observation check (no live node, not tied, no role node, duplicate text, no collection, out of scope). The verse-copy check is a candidate list: each candidate is read by hand and either justified (a short repeat the finding needs) or restated. A finding in the new stage stops the work until fixed.
3. **A read-back by you** of the document's new observations beside the lines that gave them: **all of them for the pilots, then a sample you name** for batches. One Markdown per document in `_analytics/reading-tools/prior-reread/`.
4. **Coverage:** the list of member surfaces with no live node (`C-surface-no-node`, 1,381 on 2026-11-13) is recorded before and after each batch, as a list under the one stated definition (B:129), never a percentage. It is expected to fall; it must never rise.

---

## 5. Processing the two prepared drafts (the pilot)

The two drafts are the pilot: the reading is done, the counts are known from the mapping below, and only the writing is left. Nothing is written until you approve this section.

**What is processed.** Each draft observation is matched to the existing observation for the same document line (document 92, by the line in the old `revisit_note`) or the same ledger id or face (document 8, by `stable_key` `fear:FE-nn` and the face letter), and applied through the existing in-place functions. All counts below are from the mapping in `outputs/escalation/2498-pilot-processing-plan-v1-20261113.json` (queried; nothing written).

| | Document 92 (the small reading) | Document 8 (the fear ledger) |
|---|---|---|
| Existing observation **enriched in place** (text restated, nodes added, roles set or corrected) | 9 | 26 (the 10 findings the old capture took, and 16 faces) |
| **Added** as a new observation (stage `prior-reread`) | 2 (the John 21 recognition, line 19; the 1Co 7:32 care, line 41) | 2 (the faces "Making others afraid, as an act" and "Trembling called for") |
| Existing observation **left as it is** (the document gives nothing to restate) | 2 (line 21, a quotation with a placement note; line 43, a route-to-data list) | none among the 28 |
| **Nodes added** | 22 (18 on existing observations, 4 on the added ones) | 83 (71 on existing observations, 12 on the added ones) |
| **Roles changed** on existing nodes | 12 (the old tool set them all to qualifier) | 0 |
| Existing nodes in matched observations that the draft does not name, **kept as they are** | 11 | 64 |

Total: 35 observations enriched, 4 added, 105 nodes added, 12 roles changed, 75 existing nodes kept. The 29 fear findings already live (stage `strand-reading`) are **not** touched: their nodes (749, none with a role) need a role judged by hand from the verse, a separate step on a small scale that I propose after this.

**Two things you should know before you approve.**
- **Roles in document 8 are a default.** The draft puts every unit word on `characteristic`, because the ledger's subject is those words. That is mechanical, not a judgement on each occurrence. Document 92's roles were judged one by one. You see them in the draft and may correct any before the write (decision Q4).
- **The draft's nodes are the unit words only.** The 75 existing nodes the draft does not name (for example the seat "heart", or the party) stay, since nothing says they are wrong. A later reading of the collection that carries them judges them.

**Steps, each ending at your approval before the next:**
1. *Rehearsal on a copy* (`python -m iba.app.lib.dbsnapshot --copy-to C:\Bible_study_projects\_tmp\iba-pilot-copy.db`): the loader applies the plan; the node checker is run before and after on the copy; the counts above are checked against what the copy shows; a read-back of every changed observation, before and after, to you.
2. *Your decision on the rehearsal.* If you approve: a named snapshot (`python -m iba.app.lib.dbsnapshot --reason "2498 pilot drafts" --named`), the same on the live database, the node checker live, the read-back.
3. A failed check reverts to the named snapshot, and the method returns to design.

**The loader** is a small registered step (a PowerShell front door, `cfg_step`, `cfg_write_grant`), reading the draft JSON and the plan, refusing the whole file on any problem, writing through `observationrecord` with the reason "re-read of <document>, #2498" for every change. It is built only on your approval of this section, tested on a copy first.

**Cost.** The processing is small (39 observations, 105 nodes, two documents). The effort per document of the reading itself is measured by these two: I will report the time and tokens each took, as the measure for the collection reading.

---

## 6. Order

There is no bulk reading of the other documents before the collection reading starts. The documents are read for each collection when it is taken up, in the order the study takes the collections. For information, the share of the collections' scope the documents cover (queried): of 24,847 verses in scope, 9,856 are cited in the 179 captured documents (7,818 already carry a live node, 2,038 do not), and 14,991 are cited in none of them; 13,901 verses in scope have no live node at all. For the 40% the documents cover, the collection reader starts from improved observations; for the other 60% the reading is as it is now. The 52 "nothing to capture" and the 4 "not started" documents are read the same way, for any line that names a verse of a collection in hand; no separate phase.

---

## 7. The evaluation after the re-read, and what may be retired

**What it is for.** To show what the re-read did to the existing observations, and to find the few that make no sense even after it. It is read-only and produces a workbook per document and per cluster in `_analytics/reading-tools/prior-reread/`: one row per old observation of the document (id, stage, document and lines, what the re-read did to it, the checker findings before and after, the class below, the reason).

**Classes of an existing observation after the re-read:**

| Class | Test | Next step |
|---|---|---|
| **Improved** | enriched or corrected by the re-read | stays, in its improved form |
| **Right as it was** | the re-read found it already holds the finding and passes the checks | stays |
| **Not reached** | no document line speaks to it (another source, another stage) | stays; the re-read has nothing to say about it |
| **Makes no sense** | at least one test below, and the re-read could not revive it | proposed for soft delete |
| **Undecided** | I cannot tell without you | listed for you with the evidence for that case alone (B:127) |

**What makes an observation make no sense** (B:131 retires only what "cannot be revived to comply"; each test is countable):
1. **Not a statement:** a table row, a citation list, a heading or a bare pointer standing as text, with nothing a reader can restate as a finding, and the document gives nothing to restate it from.
2. **Repeats the verse** and the document gives no more than the verse says.
3. **Not founded in the verse:** the verse does not support it, and the document does not either.
4. **Cannot be tied** to one surface and occurrence in a cited verse, even after the re-read.
5. **A duplicate** of another live observation of the same meaning, after the join.
6. **Its source line is not an observation** (a heading, a scope note): a record about the work, not a finding.

Wording that is only awkward, a kind tag that is only coarse, or a missing role or collection is **not** a reason to delete: those are enriched or completed (N13).

**Guards on any deletion.**
- Only after the reading of the collection that carries the observation and the evaluation, class by class, a pilot of the class first, the count predicted and checked.
- Through `iba/app/lib/observationrecord.py` (`soft_delete_observation`, `delete_node`), the reason in `ib_observation_change`; `deleted = 1`, never a physical delete.
- No loss of coverage: the list of member surfaces with no live node is run before and after each class; an observation whose deletion would add a surface to it stays (undecided).
- A named snapshot before each class and the row count given to you first.

---

## 8. Who builds what

**Done under #2498 (live, with the pilot):** the loader that processes a prepared load file into the observation record (`iba/app/lib/draftapply.py`, `iba/app/ps/Draft-Apply.ps1`, step registration, method rules DA-01 to DA-04, USER-GUIDE 7.5, BUILD 524 and 525).

**Carried by the collection reading, escalation #2448 (reading by collections; the collection reading is run from there, not from #2498).** Its requirements, recorded on #2448:
1. The two blocks on the Observe sheet (2.2): the documents' lines for each verse in the collection's scope, and the word-match gap list (2.7).
2. The reading Record sets `collection_id` on a new node by the own-row rule (open point D5 of #2484), takes the actions accept, modify, merge, delete and leave on existing observations, and records the answer to each document line per collection (table `reread_line`, section 3).
3. The writer change so a node needs no cluster named (decision Q8, with #2495).
4. The evaluation after a collection's reading and the retirement tests (section 7).
5. The method rules (2.5), USER-GUIDE and BUILD entries, tests on a copy.

---

## 9. Decisions for you

Decided by you on 2026-11-13 and built into this design: the documents' work is folded into the collection reading and read only for the verses of the collection in hand; no bulk re-read before the collection reading; the two drafts are processed now; the reading enriches, corrects and adds.

| # | Question | Options | My recommendation |
|---|---|---|---|
| Q1 | **Process the two drafts as in section 5** (35 enriched, 4 added, 105 nodes added, 12 roles changed; copy rehearsal, then a named snapshot, then live) | a) approve; b) approve with changes by you | **a** |
| Q2 | **How an existing observation is changed** | a) in place, with the before, after and reason in `ib_observation_change`, stage kept; b) a new observation and the old one withdrawn | **a** (nothing is withdrawn; reversible) |
| Q3 | **The stage of the four added observations** | a) `prior-reread`; b) `Analysis_phase_1` | **a** (they come from documents, not from a standard reading) |
| Q4 | **Roles in document 8** | a) accept the default (characteristic for the ledger's subject words), and correct any you name in the read-back; b) I judge each occurrence first | **a** |
| Q5 | **The 29 live fear findings with no role on any node** | a) a separate small step after the pilot, roles judged by hand from the verse; b) left to the collection reading | **a** |
| Q6 | **Lines that name a word but no verse** (a term finding, a Strong's code with no verse) | a) shown on the sheet when the code or surface is in the collection's scope; b) only lines that name a verse | **a** |
| Q7 | **Retirement** (section 7) | a) the five classes and six tests as written, applied per collection after its reading; b) changes by you | **a** |
| Q8 | **The writer change** (a node needs no cluster named) | a) within #2495; b) a separate item | **a** |
| Q9 | **Sources outside the indexed documents that a line depends on** (the ledger's face-per-hit CSV) | a) shown on the sheet when a line points at them and they are in the project; b) not read | **a** |

---

## 10. After your decision

The pilot decisions Q1 to Q5 are executed. The decisions that concern the collection reading (Q6 to Q9) go with the requirements to #2448; they are answered there when that design is taken up.


**Decision blank (you):** Q1 ___ Q2 ___ Q3 ___ Q4 ___ Q5 ___ Q6 ___ Q7 ___ Q8 ___ Q9 ___ Corrections: ______
