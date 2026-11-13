# Re-reading the prior study documents into new observations, by collection (design v1)

Escalation #2498 (raised under the researcher's ruling of 2026-11-13 on #2484). Status: **design for your decision. Nothing has been built, no document has been read, nothing in `iba/app/db/iba.db` has been written.** Everything here comes from the tables and the code, read only. Counts marked *(inferential)* are my forecasts, not queried facts (B:4); each is replaced by a counted figure before any write.

Rules this design obeys: the node rule (behaviour rule 130, `nodes-index-the-collection-and-comply-with-the-node-rules`), the observation rule (131, `observations-are-founded-unique-and-fit-the-node-rules`), the collection rule (129), the collection-is-the-unit rule (127), and your rulings N1 to N15 and 4.1 to 4.6 in `outputs/escalation/2484-node-and-observation-rules-v2-20261113.md`. Read before writing: `iba/app/CHARTER.md`, `iba/app/GOVERNANCE.md`, `iba/app/USER-GUIDE.md` sections 7.2, 7.4 and 8.2, `iba/app/lib/priorcapture.py`, `iba/app/lib/observationrecord.py`, `iba/app/lib/nodecheck.py`, and the live `cfg_setting` and `cfg_method_rule` rows.

**Your ruling, restated so you can correct it:** (1) re-read the documents into new observations and nodes under the two rules, capturing as much of the work as possible; (2) evaluate the result against the old observations; (3) only after the evaluation, soft-delete the old observations and nodes that make no sense. Nothing old is deleted before the re-read; nothing is deleted without your approval at each stage.

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
5. A refusal if the document changed since the index (sha256) or a pack is wider than a configured size (the document is then split by section; the largest will be).

### 2.3 Fill: what the reader (Claude, in a chat session) does with a pack

For each collection in the pack, from the document's lines and the verses (read first, B:116):

- Write each **finding the document makes about a verse** as an application or analytic statement in the reader's own wording, founded in the verse, never repeating more than 7 consecutive verse words (`reading.observation_items`, `max_verse_words_copied`), tied to the verse and surface it concerns. The document's meaning and implication are kept; its table, bullet or heading framing is dropped; a quotation is shortened to what the point needs.
- Keep the document's **basis**: stated where the verse says it; read where the document reads it (grounds are then required, as the item rules already say).
- Give each finding **a node for each variant it concerns**: each verse, surface, Strong's code and collection (B:130). The reader names the **occurrence** (`verse_lexical_id`) and the **role**; the writer fills surface, Strong's code, morph code and collection from the occurrence and the surface's one collection. A word recognised with no inner-being role in that verse is `standalone`; a role is never taken from a cluster tag.
- Put entity and other words of an in-scope verse on the observation that covers them as **supportive nodes**, carrying the collection of the surface they support (your ruling 4.3).
- Never split one finding by table row or by quotation; two observations only where the document says two different things.
- Where the same meaning already stands live for the same verse and surface (this stage, another document, or an earlier-stage observation that complies), the finding names that observation as *existing* and adds nodes (B:131: one observation with a node for each variant).
- A claim that rests on other verses or on the document's own synthesis, and that the cited verse does not found, is **not an observation** (B:131). It is listed in the document's report with its line, stays in the document and goes to the claims step. It is not written with a softer label.

### 2.4 Record: what the tool does (a new Reread-Record step, through `observationrecord.write`)

Written whole or refused whole, as before. It refuses a document unless:
- every line that names a verse has an answer (section 3);
- every node's occurrence is in the node's verse, and surface, Strong's, morph and collection agree with the occurrence and the surface's one collection (the node checker's checks, run on the plan **before** writing);
- no observation repeats the verse text, and none is a second live observation with the same text (the join rule is applied, not only refused);
- every observation has at least one live node, and every node a role judged by the reader.

It writes stage **`prior-reread`** (new; `prior-capture` stays on the old rows), status `draft`, `stable_key` `<reading_file_id>:L<first line>:<collection id>`, and `revisit_note` naming the document, its lines, the collection and the run, so any observation traces to the line that gave it. Every write goes through `observationrecord` with its reason in `ib_observation_change`.

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

---

## 3. How each document line is accounted for

The old table `prior_capture_line` (19,112 rows) stays untouched, as the old answer. A new table `reread_line` (to be registered in `cfg_table` and `cfg_column`, with a write grant and a step) holds one answer **per line and collection** (a line that speaks to two collections has two rows; a line that speaks to none has one row with no collection):

| Answer | Meaning |
|---|---|
| `observed` | the observation(s) it gave (id) for that collection |
| `joined` | the same meaning is already live; the line's nodes were added to it (id) |
| `not founded in the verse` | a document claim about a verse that the verse does not found, listed in the report with the claim |
| `not an observation` | with a reason class (the old classes: heading, reference list, hit count, surface or gloss table, scope or method record, pointer with no content, weave or quote-check record, next-steps list); a heading's route is carried to the findings under it |
| `out of scope` | the line's verses hold no member surface of a live collection (B:130: not touched) |

**Every line is answered, per collection.** Reread-Record refuses the document while any line has no answer. The report for a document lists: lines by answer; old answer against new answer where they differ, with the reason; the claims listed as not founded; quotations not found in the ESV text; references that resolve to no single verse (as the old report did). Nothing is written for a node with no occurrence.

`reading_file` gains a second status for the re-read (`reread`, `reread partly`), set by Record, so the index shows where the re-read stands; the old `capture_status` is not changed.

**The 52 "nothing to capture" and the 4 "not started" documents.** The 52 are worksheets, passage lists, validation registers and data documents the old tool passed over (3,538 lines answered). I have not opened them. A worksheet may hold per-verse evaluations that are findings. See decision Q5. Of the 4 "not started", two are the 267 KB `cluster-assign` files with no verse lines, one is a 1.7 KB file with none (`m10-family-synthesis-L_defilement-20260911.md`), and one is `1682-test-m10-process-c-H_guilt-v1-20260911.md` (12 lines, 39 verses in scope).

---

## 4. How the new observations are checked

1. **Before the write** (inside Reread-Record): the checks in 2.4, as a refusal list, nothing written.
2. **After each pilot and each batch**, `pwsh iba\app\ps\Node-Check.ps1 -Step Report` (about 5 seconds, reads only). It needs a small addition: a `-Stage prior-reread` filter, so the new stage's report stands alone beside the whole-table one (a change to `iba/app/lib/nodecheck.py` and `iba/app/ps/Node-Check.ps1`, with its method rule and test, after approval). **Pass criterion for the new stage:** zero findings on every node check (no occurrence, no collection, no role, collection disagrees, duplicate, out of scope) and on every observation check (no live node, not tied, no role node, duplicate text, no collection, out of scope). The verse-copy check is a candidate list: each candidate is read by hand and either justified (a short repeat the finding needs) or restated. A finding in the new stage stops the work until fixed.
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

## 7. The evaluation against the old observations (before anything is deleted)

**What is compared.** For each old live observation of stage `prior-capture`, find its counterpart in the new stage by **the same document line, verse and occurrence** (the old `revisit_note` names document and lines; the new `stable_key` and `revisit_note` do too). The evaluation is **read-only** and produces a workbook (one row per old observation: id, document and lines, new counterpart ids or none, the checker findings, the class below, the reason) in `_analytics/reading-tools/prior-reread/`, per document and per cluster. It deletes nothing.

**Four classes of an old observation:**

| Class | Test | If you approve |
|---|---|---|
| **A. Replaced** | a new observation says the same about the same verse, occurrence and document line | the old observation and its nodes are soft-deleted, reason "replaced by observation N" |
| **B. Sensible, not replaced** | no new counterpart, it passes every observation and node check, and reads, to a reader holding only its text, its nodes and the verse, as a statement about a named word in a named verse that the verse founds | kept; a node lacking a collection, role or occurrence is completed, not deleted |
| **C. Non-sensible** | at least one of the tests below | soft-deleted, reason named |
| **D. Undecided** | I cannot tell without you | listed for you, with the evidence for that case alone (B:127) |

**What makes an old observation non-sensible** (B:131 retires only what "cannot be revived to comply"; each test is countable):
1. **Not a statement:** a table row, a citation list, a heading or a bare pointer standing as text, with nothing a reader can restate as a finding.
2. **Repeats the verse:** the verse text with a label, with no more in it than the verse says and no restatement.
3. **Not founded in the verse:** the verse does not support it (the re-read lists the same claim as "not founded in the verse").
4. **Cannot be tied** to one surface and occurrence in the cited verse (checker findings `O-not-tied`, and nodes the re-read could not place).
5. **A duplicate** of another live observation of the same meaning (checker `O-duplicate-text`, and what the re-read joined).
6. **Its source line was answered "not an observation"** in the re-read, with a reason that holds (a heading, a scope note): it is a record about the work, not a finding.

Wording that is only awkward, or a kind tag that is only coarse, is **not** a reason to delete (N13).

**Guards on any deletion.**
- Class by class, a pilot of the class first, the count predicted and checked (B:130's rule for bulk changes).
- Through `iba/app/lib/observationrecord.py` (`soft_delete_observation`, `delete_node`), the reason in `ib_observation_change`; `deleted = 1`, never a physical delete.
- **No loss of coverage.** The old observations carry most of the collection evidence today (6,139 of 6,709 have a collection node). The list of member surfaces with no live node is run before and after each class; an observation whose deletion would add a surface to that list is class D, kept until a new observation covers it.
- A named snapshot before each class, and the number of rows it will touch given to you before it is run.

---

## 8. What I will build, only after you approve (a separate Developer Mode build, tested on a copy)

1. `iba/app/lib/rereadprepare.py` (Reread-Prepare, reads only) and `iba/app/lib/rereadrecord.py` (Reread-Record) with a PowerShell front door in `iba/app/ps/`, registered in `cfg_work_package`, `cfg_step`, `cfg_utility` and `cfg_write_grant`.
2. Table `reread_line` in `cfg_table` and `cfg_column`; settings `prior_reread.output_dir`, `prior_reread.stage`, the pack size; the method rules (2.5); stage `prior-reread`; the output folder in `folder_purpose` (B:128).
3. The writer change in `observationrecord.py` (2.6), done with #2495.
4. `Node-Check.ps1 -Stage`, and the evaluation report (Reread-Evaluate, reads only).
5. USER-GUIDE section, BUILD entry, tests on a copy, the results on this item. The old tool and `prior_capture_line` stay as the record of the old method.

---

## 9. Decisions for you

| # | Question | Options | My recommendation |
|---|---|---|---|
| Q1 | **The approach** | a) re-read by collection, per document, with per-line accounting (this document); b) re-read by document, as the old tool, under the new rules (cheaper to build, brings back the focus problem); c) a fresh reading of the verses without the documents | **a** |
| Q2 | **The wording** | a) restate in the reader's words, keep the document's meaning, drop its framing, list claims the verse does not found; b) keep the document's wording where it passes the 7-word test; c) as a, but also write the not-founded claims with basis "read" | **a** (B:131: never a statement the verse does not found; c writes what the rule forbids) |
| Q3 | **Duplicates across documents** (replaces CP-04) | a) join the live observation of the same meaning, the pack showing candidates; b) keep each document's observation separate | **a** (B:131) |
| Q4 | **The pilot** | a) pilot 1, then pilot 2, then the M09 batch; b) pilot 1 only, then the batch; c) other documents you name | **a** |
| Q5 | **The 52 "nothing to capture" and 4 "not started" documents** | a) a later phase, starting with three worksheet or passage-list samples after pilot 2 to see whether they hold findings; b) leave out; c) read with the 179 | **a** (I have not opened them; the old verdict was "not an observation" line by line, so some may hold nothing) |
| Q6 | **Stage and rules** | a) new stage `prior-reread`, new method rules, the old method rules marked superseded; b) reuse stage `prior-capture` | **a** (the evaluation needs the two sets apart) |
| Q7 | **The evaluation classes and the non-sensible tests** (section 7) | a) as written; b) changes by you | **a**, with your corrections |
| Q8 | **The writer change** (a node needs no cluster named; the history column filled by the writer) | a) within #2495; b) a separate item | **a** |

---

## 10. After your decision

On your decisions Q1 to Q8: I register the method rules and settings through `configmaint.apply_logged` on a copy first, build items 1 to 5 of section 8 (Prepare first, reads only), run the dry-run Prepare for the pilot documents and bring you the counted figures to replace the forecasts, then follow the steps in section 5. Until then no document is read, no code is written and nothing is changed.

**Decision blank (you):** Q1 ___ Q2 ___ Q3 ___ Q4 ___ Q5 ___ Q6 ___ Q7 ___ Q8 ___ Corrections: ______
