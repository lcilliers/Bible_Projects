# Re-reading the prior study documents into new observations, by collection (design v2)

Escalation #2498 (raised under the researcher's ruling of 2026-11-13 on #2484). Status: **design for your decision, revised after your reading of the two draft samples. Nothing has been built, no document has been read, nothing in `iba/app/db/iba.db` has been written.** Everything here comes from the tables and the code, read only. Counts marked *(inferential)* are my forecasts, not queried facts (B:4); each is replaced by a counted figure before any write.

Rules this design obeys: the node rule (behaviour rule 130, `nodes-index-the-collection-and-comply-with-the-node-rules`), the observation rule (131, `observations-are-founded-unique-and-fit-the-node-rules`), the collection rule (129), the collection-is-the-unit rule (127), and your rulings N1 to N15 and 4.1 to 4.6 in `outputs/escalation/2484-node-and-observation-rules-v2-20261113.md`. Read before writing: `iba/app/CHARTER.md`, `iba/app/GOVERNANCE.md`, `iba/app/USER-GUIDE.md` sections 7.2, 7.4 and 8.2, `iba/app/lib/priorcapture.py`, `iba/app/lib/observationrecord.py`, `iba/app/lib/nodecheck.py`, and the live `cfg_setting` and `cfg_method_rule` rows.

**Your ruling and your reading of the two samples, restated so you can correct it:**
1. Re-read the documents under the node and observation rules, capturing as much of the work as possible.
2. **The re-read is a value-adding operation on the observations that already exist.** It enriches and corrects them as much as it creates new ones. It does not replace them and does not set out to disprove them (your words of 2026-11-13, after the two samples).
3. It is an intelligent reading of the source documents, so that every observation that relates to a document line is improved, and added to where necessary.
4. It shows **gaps in the collections**: words a document names that no collection surface matches, where the actual surface may differ from the words the document uses.
5. An old observation is soft-deleted only if, after this, it makes no sense and cannot be revived. Nothing is deleted without your approval at each stage.

What the two samples showed (drafts in `outputs/escalation/2498-pilot-sample-m18-group-g-reading-draft-v1-20261113.json` and `outputs/escalation/2498-pilot-sample-fear-ledger-unit2-draft-v1-20261113.json`; nothing was written to the database): the ledger's findings were mostly live already, with nodes but no roles and one-line texts; the small reading's subject words are in no collection. Both are what the revised method is built around.

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

## 2. The method: a re-read by collection

### 2.1 The unit

The unit of work is **one document read for one collection** (a *pack*). Reasons: the collection is what the node carries and what the narrative follows (B:127, B:130); a verse holds many collection words (a median captured document touches 87 collections through the verses it cites, so reading "by verse" or "by document" gives the reader no focus). A document is still the unit of accounting (section 3).

### 2.2 Prepare: what the tool gives the reader (reads only, a new Reread-Prepare step)

For one document, the tool writes a JSON and a readable Markdown, arranged **by collection**. It reads the document and the tables and never judges:

1. The document's lines that name a verse (from `reading_ref`, as the old Prepare), each with its section heading and the lines around it, the verses resolved fresh.
2. For each verse, from `verse_lexical`: its occurrences of **member surfaces of the 169 live collections**, each with occurrence id, surface, Strong's code, morph code and the one collection of the surface (own row, else base: the reader the node checker uses, `collectionexport._memberships`). The occurrences whose surface or gloss the line names are marked *named*; the rest of the verse's collection words are listed, not marked, so the reader sees what else the verse holds.
3. For each collection touched by a named occurrence: its name and members, and what is already live and compliant in the re-read stage for the same verse and surface (so the reader joins rather than duplicates; B:131).
4. The **old answer** for each line (`prior_capture_line`: answer, reason class, observation ids) and the old observation text beside it: shown for reference, never copied.
5. **What is already recorded for the line (new).** For each line and collection: every live observation of any stage that has a node on a verse of the line, with its text, its nodes (occurrence, role, collection) and what each lacks (no role, no collection, no occurrence, a verse the document cites with no node). This is how the reader sees that a ledger's findings are already live (the fear ledger: 29 of 39), so the work is to improve them and not to write them again.
6. **Words the document names that no collection surface matches (new, see 2.7).**
7. A refusal if the document changed since the index (sha256) or a pack is wider than a configured size (the document is then split by section; the largest will be).

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

### 2.4 Record: what the tool does (a new Reread-Record step, through `observationrecord.write`)

Written whole or refused whole, as before. It refuses a document unless:
- every line that names a verse has an answer (section 3);
- every node's occurrence is in the node's verse, and surface, Strong's, morph and collection agree with the occurrence and the surface's one collection (the node checker's checks, run on the plan **before** writing);
- no observation repeats the verse text, and none is a second live observation with the same text (the join rule is applied, not only refused);
- every observation has at least one live node, and every node a role judged by the reader.

**New observations** are written with stage **`prior-reread`**, status `draft`, `stable_key` `<reading_file_id>:L<first line>:<collection id>` and a `revisit_note` naming the document, its lines, the collection and the run. **Existing observations that are enriched or corrected are changed in place** through `observationrecord` (their stage is kept; the `revisit_note` gains the re-read reference), with the before and after and the reason in `ib_observation_change`, so the reading's work is traceable and an enrichment can be reversed. Added nodes are written by the same call. Every write goes through `observationrecord` (RW-01).

### 2.5 The method rules (applied only on your approval, as `cfg_method_rule` rows on a new step `prior_reread.record`, through `configmaint.apply_logged`)

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

The old table `prior_capture_line` (19,112 rows) stays untouched, as the old answer. A new table `reread_line` (to be registered in `cfg_table` and `cfg_column`, with a write grant and a step) holds one answer **per line and collection** (a line that speaks to two collections has two rows; a line that speaks to none has one row with no collection):

| Answer | Meaning |
|---|---|
| `added` | a new observation (id) for that collection |
| `enriched` | an existing observation (id) was restated or given nodes, roles or collections |
| `corrected` | an existing observation or node (id) was corrected, with the reason |
| `already right` | an existing observation (id) already holds the finding and needs nothing |
| `not founded in the verse` | a document claim about a verse that the verse does not found, listed in the report with the claim |
| `not an observation` | with a reason class (the old classes: heading, reference list, hit count, surface or gloss table, scope or method record, pointer with no content, weave or quote-check record, next-steps list); a heading's route is carried to the findings under it |
| `out of scope` | the line's verses hold no member surface of a live collection (B:130: not touched) |

**Every line is answered, per collection.** Reread-Record refuses the document while any line has no answer. The report for a document lists: lines by answer; for each enriched or corrected observation the before and after; old answer against new answer where they differ, with the reason; the gap list (2.7); the claims listed as not founded; quotations not found in the ESV text; references that resolve to no single verse (as the old report did). Nothing is written for a node with no occurrence.

`reading_file` gains a second status for the re-read (`reread`, `reread partly`), set by Record, so the index shows where the re-read stands; the old `capture_status` is not changed.

**The 52 "nothing to capture" and the 4 "not started" documents.** The 52 are worksheets, passage lists, validation registers and data documents the old tool passed over (3,538 lines answered). I have not opened them. A worksheet may hold per-verse evaluations that are findings. See decision Q5. Of the 4 "not started", two are the 267 KB `cluster-assign` files with no verse lines, one is a 1.7 KB file with none (`m10-family-synthesis-L_defilement-20260911.md`), and one is `1682-test-m10-process-c-H_guilt-v1-20260911.md` (12 lines, 39 verses in scope).

---

## 4. How the new observations are checked

1. **Before the write** (inside Reread-Record): the checks in 2.4, as a refusal list, nothing written.
2. **After each pilot and each batch**, `pwsh iba\app\ps\Node-Check.ps1 -Step Report` (about 5 seconds, reads only). It needs a small addition: a `-Stage prior-reread` filter, so the new stage's report stands alone beside the whole-table one (a change to `iba/app/lib/nodecheck.py` and `iba/app/ps/Node-Check.ps1`, with its method rule and test, after approval). **Pass criterion for the new stage and for every observation the re-read enriched or corrected (listed by id in the run; the checker is run on them as well, before and after, so the improvement is counted):** zero findings on every node check (no occurrence, no collection, no role, collection disagrees, duplicate, out of scope) and on every observation check (no live node, not tied, no role node, duplicate text, no collection, out of scope). The verse-copy check is a candidate list: each candidate is read by hand and either justified (a short repeat the finding needs) or restated. A finding in the new stage stops the work until fixed.
3. **A read-back by you** of the document's new observations beside the lines that gave them: **all of them for the pilots, then a sample you name** for batches. One Markdown per document in `_analytics/reading-tools/prior-reread/`.
4. **Coverage:** the list of member surfaces with no live node (`C-surface-no-node`, 1,381 on 2026-11-13) is recorded before and after each batch, as a list under the one stated definition (B:129), never a percentage. It is expected to fall; it must never rise.

---

## 5. The pilot, with predicted counts and a snapshot before any write

Every pilot runs first on a copy, then live after a named snapshot. Commands (run only after approval):

```powershell
python -m iba.app.lib.dbsnapshot --copy-to C:\Bible_study_projects\_tmp\iba-pilot-copy.db
python -m iba.app.lib.dbsnapshot --reason "2498 prior re-read pilot" --named
```

Reference figures are queried (old live observations and nodes whose `revisit_note` names the document; lines from `prior_capture_line`; verses and occurrences from `reading_ref` and `verse_lexical`). The "expected new" columns are *(inferential)*, from the old counts, and are replaced by the dry-run Prepare count before any write.

| Pilot | Documents | Lines (old answers) | Verses in scope / member occurrences | Old live obs / nodes | Expected new obs | Expected new nodes |
|---|---|---|---|---|---|---|
| **1: two small prose readings** | `_analytics/Clusters/M18 - desire-longing/m18-group-G-reading-v1-20261009.md` (id 92); `_analytics/Clusters/M08 - pride-arrogance/ot-05-16-self-glory-reading-v1-20261019.md` (id 53) | 14 captured; 6 captured and 5 not an observation | 45 and 7 / 105 and 22 (127 in all) | 11 and 2 = 13 / 37 and 3 = 40 | 10 to 25 | 40 to 110 |
| **2: a ledger with October ids** | `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit2-v1-20261001.md` (id 8) | 185: 111 captured, 29 already recorded, 45 not an observation | 206 / 761 | 31 / 227 | 25 to 50 | 150 to 400 |
| **Batch, after both pilots are approved** | the 11 documents of cluster M09 (humility-lowliness), 168 KB | 649 | 892 / 3,540 | 269 / 1,905 | 200 to 400 | 1,300 to 2,800 |

Why these: pilot 1 is the two smallest reading documents with six or more verse lines (3.5 KB each; I have not opened them), so you can read all of their new observations in one sitting. Pilot 2 is the hard case: a ledger where 29 findings are already live in another stage, so it tests the join against existing observations. The batch is one whole cluster of moderate size, to test packs across documents and the cross-document join. Later batches follow in section 6.

**What the two draft samples already tell us (counted, nothing written).**
- *Small reading, document 92:* 14 lines; the old capture had 11 live observations and 37 nodes for it; the draft has 11 observations and 43 nodes, of which 12 supportive (the subject words are in no collection); 3 lines gave nothing recoverable (a quotation with a placement note, a pointer, a route-to-data list).
- *Fear ledger, document 8:* 39 findings; 29 already live (stage `strand-reading`) with nodes on 119 of 122 unit words but **no role on any node** and one-line texts; the 10 the old capture took have 144 nodes (113 characteristic, 31 standalone); the draft restates those 10 (116 nodes, 6 without a collection) and adds 18 face observations (109 nodes). Section C (findings about findings) is not yet drafted.
- *So the pilot's value is enrichment:* roles on existing nodes, fuller wording of thin statements, corrections, the few new findings, and the gap list. The counts to predict for each pilot are therefore: observations enriched, observations corrected, observations added, nodes added, roles set, and gaps listed, instead of observations created.

**Steps, each ending at your approval before the next:**

1. *Dry run, reads only.* Prepare for the pilot documents. I bring you the counted figures that replace the forecasts (lines, verses, member occurrences, collections touched, named occurrences) and the packs. **No write.**
2. *Rehearsal on a copy.* Fill and Record pilot 1 on the copy; Node-Check on the copy; the read-back report to you.
3. *Your decision on the rehearsal.* If approved: named snapshot, the same on the live database, Node-Check live, read-back.
4. Pilot 2, same four steps. Then the evaluation of both against the old (section 7), **before** the batch.
5. The batch (M09), per document, same steps, a report per document; the batch ends with the evaluation for that cluster.

A pilot that fails a pass criterion in section 4 is reverted by restoring the named snapshot, and the method goes back to design before it is run again (B:44).

**Cost and the cheaper path (B:20).** The captured documents are 4.1 MB, about 1 million tokens to read and two to three times that with the packs *(inferential)*, so this is many sessions, as the old capture was. Paths I considered: (a) repair the old observations by script (your ruling: not worth it; the old text itself reads badly); (b) read only the 13,376 lines the old tool answered "captured" (leaves out lines it wrongly passed over); (c) a fresh pass over the 24,847 in-scope verses without the documents (a different task: it does not capture the documents' work). I recommend the method above, with the pilot's measured tokens and time per document as the measure of pace.

---

## 6. The order after the pilots (for information; each batch needs your go)

Captured documents by cluster (queried; documents, size, old live observations / nodes): M07 3, 79 KB, 58 / 205; M53 1, 23 KB, 27 / 153; M72 6, 115 KB, 189 / 941; M20 3, 136 KB, 221 / 1,506; M08 11, 145 KB, 224 / 2,317; M09 11, 168 KB, 269 / 1,905; M01 9, 221 KB, 304 / 1,520; no cluster 21, 220 KB, 264 / 1,478; M18 28, 314 KB, 706 / 3,047; M25 17, 338 KB, 486 / 2,540; M64 27, 462 KB, 739 / 4,347; M47 24, 735 KB, 1,374 / 16,099; M02 18, 1,167 KB, 1,848 / 10,413. Proposed order: M09 (the batch), then the small clusters first (M07, M53, M72, M20, M08, M01), the documents with no cluster with the cluster they speak to, then M18, M25, M64, and last M47 and M02, the largest, split by section. The order does not change what is written.

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
- Only after the re-read of the document's cluster and the evaluation, class by class, a pilot of the class first, the count predicted and checked.
- Through `iba/app/lib/observationrecord.py` (`soft_delete_observation`, `delete_node`), the reason in `ib_observation_change`; `deleted = 1`, never a physical delete.
- No loss of coverage: the list of member surfaces with no live node is run before and after each class; an observation whose deletion would add a surface to it stays (undecided).
- A named snapshot before each class and the row count given to you first.

---

## 8. What I will build, only after you approve (a separate Developer Mode build, tested on a copy)

1. `iba/app/lib/rereadprepare.py` (Reread-Prepare, reads only) and `iba/app/lib/rereadrecord.py` (Reread-Record) with a PowerShell front door in `iba/app/ps/`, registered in `cfg_work_package`, `cfg_step`, `cfg_utility` and `cfg_write_grant`.
2. Table `reread_line` in `cfg_table` and `cfg_column` (answers per line and collection, including the existing observation each enriched or corrected); settings `prior_reread.output_dir`, `prior_reread.stage`, the pack size; the method rules (2.5); stage `prior-reread`; the output folder in `folder_purpose` (B:128).
3. The writer change in `observationrecord.py` (2.6), done with #2495.
4. `Node-Check.ps1 -Stage`, the evaluation report (Reread-Evaluate, reads only), and the gap list (2.7).
5. USER-GUIDE section, BUILD entry, tests on a copy, the results on this item. The old tool and `prior_capture_line` stay as the record of the old method.

---

## 9. Decisions for you

| # | Question | Options | My recommendation |
|---|---|---|---|
| Q1 | **The purpose and approach** | a) a value-adding re-read by collection: improve existing observations (enrich, correct), add what is missing, list collection gaps; b) a replacing re-read (new observations, old ones then deleted); c) a fresh reading of the verses without the documents | **a** (your reading of the two samples) |
| Q2 | **How an existing observation is changed** | a) in place, through `observationrecord`, before and after and the reason kept in `ib_observation_change`, stage kept; b) a new observation in stage `prior-reread` and the old one withdrawn | **a** (nothing is withdrawn by the re-read; an enrichment is reversible) |
| Q3 | **The wording** | a) restate in the reader's words, founded in the verse, keeping the document's meaning; a claim the verse does not found is listed, not written; b) keep the document's wording where it passes the 7-word test | **a** (B:131) |
| Q4 | **The pilot** | a) the two documents already sampled (92, then 8) run for real on a copy, counted as enriched, corrected, added, roles set and gaps; then the M09 batch; b) other documents you name | **a** |
| Q5 | **Gaps in the collections** (2.7) | a) the re-read lists them and changes no collection; you decide with #2463 which surfaces join which collections; b) the re-read proposes the additions itself | **a** |
| Q6 | **The 52 "nothing to capture" and 4 "not started" documents** | a) a later phase, three samples first (worksheets and passage lists may hold per-verse evaluations); b) leave out; c) with the 179 | **a** |
| Q7 | **Retirement** (section 7) | a) the five classes and six tests as written; b) changes by you | **a**, with your corrections |
| Q8 | **The writer change** (a node needs no cluster named; the history column filled by the writer) | a) within #2495; b) a separate item | **a** |
| Q9 | **Sources outside the 179 documents** that a document depends on (the ledger's face-per-hit CSV) | a) read when a line points at them and they are in the project, named in the pack; b) not read | **a** |

---

## 10. After your decision

On your decisions Q1 to Q9: I register the method rules and settings through `configmaint.apply_logged` on a copy first, build items 1 to 5 of section 8 (Prepare first, reads only), run the dry-run Prepare for the pilot documents and bring you the counted figures to replace the forecasts, then follow the steps in section 5. Until then no document is read, no code is written and nothing is changed.

**Decision blank (you):** Q1 ___ Q2 ___ Q3 ___ Q4 ___ Q5 ___ Q6 ___ Q7 ___ Q8 ___ Q9 ___ Corrections: ______
