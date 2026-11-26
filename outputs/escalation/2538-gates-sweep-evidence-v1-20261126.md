# #2538: the sweep (B4) and the evidence validation (B5) — the gates of step 2.1, with real packages (v1, 2026-11-26)

Written by Claude, session 760131f7, for the researcher's review before they are applied live. Made on a copy of live with `gates_2538_v1_20261126.py` applied. Nothing was written to the live database.

## 1. Where they sit in the loop

- Step 2.1 gains two ledger-only items, `sweep` and `evidence-validation`: one row each for every subgroup.
- Step 2.1 closes for a subgroup only when both are answered and validated, so 3.1 (which needs 2.1 closed) waits for them.
- LayerNext now names the read command of the next open item from config (`layer.read_types`: each read's `command` and `items`): ReadStructure while 2.1 rows are open, then ReadSweep, then ReadEvidence, then step 3.1.
- A subgroup already past 2.1 without the gate rows ("reasoning" on live) counts as 2.1 open, so LayerNext names ReadSweep for it.
- The gate rows are refused in a LayerRecord working file and left out of LayerPull.
- **ReadSweep** is refused while a 2.1 row of the subgroup is open. It packages every unmarked observation of the subgroup's scope.
- **RecordSweep** takes keep (with its marker), merge, consume (verified, VA-03), delete_neither or defer, each with its reason, and refuses an answer that leaves any unmarked observation unanswered. With nothing left to sweep, ReadSweep answers the row itself.
- **ReadEvidence** is refused before the sweep. It shows the eight code checks and packages the evidence observations not yet read (at most 40, in step order, with their verses once).
- **RecordEvidence** takes, for each observation, true (with why) or repair (with why and the validation's own actions, written through `collectionvalidate.record`). It logs each one read (`evidence_read`); the gate validates when every evidence observation is read and the checks pass.
- **The eight code checks:** every observation marked; none without a node; no word node missing a column without its reason; no trace to a deleted observation; no two of one text; every B1 observation traced by a sense; every sense traced by the 2.1 findings on its occurrences; no older observation left open. The trace and duplicate checks cover evidence and unmarked observations; an inner-being observation's traces are the inner-being layer's (VA-06).

## 2. What the sweep found in "reasoning" on live

The sweep package holds **29 unmarked observations** (26,091 characters, 0.11 s): [`2538-readsweep-sample-package-v1-20261126.json`](2538-readsweep-sample-package-v1-20261126.json).

All 29 are the earlier layered reading of the group "reasoning and giving grounds" (group 13), which the regrouping of 25 November deleted: its 1.2 enrichment, 2.1 pairings, double meanings, qualifier, entity and direction, and its 3.1 and 3.3 findings. Their ledger rows were never retired, so their observations stayed live and unmarked on this subgroup's occurrences. The first sweep design took only older observations of other stages and missed them. The evidence checks found them (29 unmarked, 8 of them tracing deleted observations), so the sweep now takes every unmarked observation of the scope the evidence checks read.

**My reading of the 29 (the answer recorded on the copy):**

- **consume (13):**
  - 22315: the enrichment of the deleted group 'reasoning and giving grounds' names the codes of reasoning (G1256, G1261, G3049, H3198) and of the ground (G0156, G1352, G1223, G5484, G5124, H6440I, H1697M, H3651C, H2600) and the small words in the units; the seven enrichments of the subgroup's senses state the codes of each sense Carriers [22913, 22914, 22915, 22916, 22917, 22918, 22919].
  - 22382: belief beside the reasoning in Act 19:9 (unbelief before it) and after 'for this reason' in 1Th 3:5, 1Th 3:7 and 1Ti 1:16: the two findings of the believe pairing state the same verses and positions Carriers [22947, 22948].
  - 22383: words of duration in Dan 4:34, 1Ti 1:16 and 1Pe 3:15 in other clauses: the continual pairing states always qualifying the readiness in 1Pe 3:15 and the lasting words qualifying other nouns in Dan 4:34 and 1Ti 1:16 Carriers [22961, 22962].
  - 22384: bearing in Num 18:32, 1Th 3:5 (same clause as the reason) and patience in 1Ti 1:16: the three findings of the endure pairing state each verse Carriers [22973, 22974, 22975].
  - 22385: knowing in Mar 12:24 (the not knowing as the cause of the error), Luk 9:47 (Jesus knowing the reasoning) and 1Th 3:5 (learn): the three findings of the know pairing state each verse Carriers [22997, 22998, 22999].
  - 22386: sin near the reason in Num 18:32, Isa 1:18 and 1Jo 3:8: the three findings of the sin pairing state each verse Carriers [23020, 23021, 23022].
  - 22421: the surface reason carrying eighteen codes, the ground or cause codes, H3198, G2138, H4486, G3056, and the small words G2596, G0302 and H1961: the double-meaning finding of reason states the codes and their uses Carriers [22920].
  - 22422: reasoned as G1256 in five verses and G3049 in 1Cor 13:11: the double-meaning finding of reasoned states the same Carriers [22921].
  - 22423: reasoning as G1261 in Luk 9:47 and G1256 in Act 19:8 and 19:9: the double-meaning finding of reasoning states the same Carriers [22922].
  - 22433: the qualifiers of the group: the negator reaching the reason in Pro 3:30 and Act 28:18, the negators of Num 18:32, 1Sa 20:29 and Gen 41:31, three in Act 17:2, like a child in 1Cor 13:11, often in Rom 15:22: the eight qualifier findings state each; its reading that the not of Mar 12:24 reaches the reason is not kept, the finding on Mar 12:24 reads it as framing the question Carriers [22923, 22924, 22925, 22926, 22927, 22928, 22929, 22930].
  - 22440: the entities named in the verses, divine and human, and Paul referred to but not stored: the six entity findings state who is named in each verse Carriers [22931, 22932, 22933, 22934, 22935, 22936].
  - 22447: the direction of the reasoning across the verses (from Paul to hearers, Jesus to those he answers, the Lord to the people, the ground in 1Ti 1:16 and 1Jo 3:8, Jesus knowing in Luk 9:47): the seven direction findings state each Carriers [22937, 22938, 22939, 22940, 22941, 22942, 22943].
  - 22484: the small words in the units of reason (H1961 in Eze 19:10, G2596 and G0302 in Act 18:14) and G2138 in Jam 3:17: the double-meaning finding of reason names each code and its use Carriers [22920].
- **keep as inner_being (16):**
  - 22473: an element of the reasoning from the replaced group's 3.1 (the act and its mode: spoken reasoning in the Acts verses); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22474: an element from the replaced group's 3.1 (inward reasoning in Luk 9:47, known by Jesus); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22475: an element from the replaced group's 3.1 (the reckoning of a child in 1Cor 13:11, given up in adulthood); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22476: an element from the replaced group's 3.1 (what the reasoning is on: the Scriptures, righteousness, the kingdom of God); a stage 4 building block, considered first at 3.1
  - 22477: an element from the replaced group's 3.1 (what the ground phrases name the ground of); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22478: an element from the replaced group's 3.1 (the ground beside bearing and sin); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22479: an element from the replaced group's 3.1 (knowing as the ground of error); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22480: an element from the replaced group's 3.1 (the ground denied); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22481: an element from the replaced group's 3.1 (the refusal of a ground); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22482: an element from the replaced group's 3.1 (the manner and length the qualifiers give); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22483: an element from the replaced group's 3.1 (the directions of reasoning and ground); a stage 4 building block, considered first at 3.1 for this subgroup
  - 22644: an interworking finding from the replaced group's 3.3 (believing and the reasoning); considered at 3.3 when the collection reaches it
  - 22645: an interworking finding from the replaced group's 3.3 (duration beside the ground, no tie of grammar); considered at 3.3 when the collection reaches it
  - 22646: an interworking finding from the replaced group's 3.3 (bearing and the ground); considered at 3.3 when the collection reaches it
  - 22647: an interworking finding from the replaced group's 3.3 (knowing and the reasoning); considered at 3.3 when the collection reaches it
  - 22648: an interworking finding from the replaced group's 3.3 (sin and the ground); considered at 3.3 when the collection reaches it

Recorded on the copy: every consumption verified by the recorder (each word occurrence of the old observation on a live node of a carrier), the sweep row validated, and after it all eight evidence code checks pass. Result: {'answered': 29, 'validated': True, 'reason': 'swept: 29 older observation(s) answered by content', 'next': ".\\iba\\app\\ps\\Collection-Build.ps1 -Collection thought -Subgroup 'reasoning' -Action ReadEvidence"}.

## 3. The evidence validation of "reasoning"

After the sweep, **139 evidence observations** are to be read, in 4 packages of up to 40. The first: [`2538-readevidence-sample-package-v1-20261126.json`](2538-readevidence-sample-package-v1-20261126.json) (37,612 characters, 0.02 s; the 15 B1 observations, 7 senses, 7 enrichments and the first 2.1 findings, with their 36 verses).

**One observation, as the package carries it:**

```json
{
 "observation": 22673,
 "step": "S1",
 "item": "word-sense",
 "kind": "term",
 "text": "In Act 17:2, 17:17, 18:4, 18:19 and 24:25 'reasoned' is Paul's spoken discourse with listeners: in the synagogue and market he argues from the Scriptures and persuades. In Act 24:25 the same word takes topics (righteousness, self-control, judgment) as what he argues about. The sense is speaking to others to convince, not private thinking; the verse names the audience and the place each time.",
 "basis": "read",
 "grounds": "reasoned with them from the Scriptures",
 "traces": [],
 "verses": [
  "Act 17:17",
  "Act 17:2",
  "Act 18:19",
  "Act 18:4",
  "Act 24:25"
 ]
}
```

The reading of these 139 is the live run, after your review; it is not a test.

## 4. The ReadSweep instruction block

**What this read is.** The sweep (B4) of one subgroup, after its 2.1 rows: every observation of the subgroup's scope still unmarked after B1 to B3 -- older observations on its occurrences that B1 carried forward and B2 and B3 did not take up, any carried to the sweep, and any other unmarked observation of the scope (for example the reading of an earlier grouping). Each is judged by its content. End state: none of the subgroup's observations is unmarked, except one deferred to a named collection.

**How to read.**
1. Take one older observation at a time (`older`): its text, its stage and kind, its verses, how many of its nodes are on this subgroup's occurrences and how many elsewhere, and the collections its nodes belong to.
2. Judge it by what it states, not by its stage or kind: does it state what the data are or show, tied to a verse (evidence)? how something works in the inner being, based on evidence (inner being)? or neither?

**What to write.**
1. Fill `answer.older`, one entry for each observation, each answered once, with `reason`: what it states and why it is so judged.
2. merge, with `into`: a live observation of the subgroup says the same in the same words. consume, with `carriers` (observation ids) and `mapping`: live observations already state what it says; every word occurrence of it must be on a live node of a carrier (VA-03), then it is deleted. keep, with `nature` evidence or inner_being: it stands as it is (an inner-being one waits for 3.1). delete_neither: it is neither evidence nor inner being; it is commented, then deleted with its nodes here (one held by other subgroups or collections loses only the nodes here). defer, with `collection`, `nature` and `finding`: another collection owns it; it is marked now and the finding is left to that collection.
3. Then: Collection-Build.ps1 -Action RecordSweep -File <the answer file> (-Check to preview). The record refuses the whole file on any fault; every unmarked observation must be answered.

**Rules kept:** VA-04 neither-evidence-nor-inner-being-is-deleted, VA-05 the-marker-follows-content-not-stage, RW-01 changed-only-by-reading, RS-04 existing-checked-accept-modify-delete (text read live from `cfg_method_rule`).

## 5. The ReadEvidence instruction block

**What this read is.** The evidence validation (B5) of one subgroup, after its sweep, the gate before 3.1: the code checks of its observations (shown in `code_checks`), and the reading of every evidence observation of the subgroup (its own of S1 to 2.1, and the older ones on its occurrences kept as evidence) for whether it is true, founded and coherent with the others. Inner being is not judged here; the two validations are never run together.

**How to read.**
1. Read the code checks first: a failing check names observations to repair (unmarked, no node, a word node missing a column without its reason, a trace to a deleted observation, two of one text, a B1 observation no sense traces, a sense the 2.1 observations on its occurrences do not trace, an older observation left open).
2. Take one observation at a time (`observations`, in the order of the steps): its text, basis and grounds against its verses (`verses`) and the observations it traces. Is it true of those verses? Does it say more than they show? Does it contradict another observation of the subgroup?

**What to write.**
1. Fill `answer.observations`, one entry for each observation of the package: verdict true, with `why` (what in the verses and the data bears it out); or verdict repair, with `why` (what is wrong) and `actions`: the actions of the validation that repair it (cfg_setting validate.reading actions, each with its parameters, for example {"action": "restate", "oid": id, "new_text": ..., "checked": ..., "reason": ...}, or delete_neither, complete_node, add_trace).
2. A repair is checked as it is written; an observation that cannot be made true is deleted with its reason.
3. Then: Collection-Build.ps1 -Action RecordEvidence -File <the answer file> (-Check to preview), and ReadEvidence again until every evidence observation is read; the gate passes when all are read and the code checks pass.

**Rules kept:** VA-01 a-sheet-is-one-checked-transaction, VA-02 repair-first-and-every-finding-acted-on, VA-03 consumption-is-verified-before-deletion, VA-04 neither-evidence-nor-inner-being-is-deleted, VA-05 the-marker-follows-content-not-stage, VA-06 evidence-validation-gates-inner-being-validation, RW-01 changed-only-by-reading, RW-03 no-duplicates-multi-node, RW-04 concise-verse-specific, RW-06 resolved-fresh-on-evidence, RW-11 missing-is-named (text read live from `cfg_method_rule`).

## 6. Tested

- **`iba/app/tools/temp_2538_gates_test_run.py`:** 35 of 35 pass. It covers:
  - the order of the gates, on a subgroup at 2.1;
  - the real sweep of the live copy;
  - every refusal: a missing answer, a wrong action, a short reason, an observation not a candidate, a consumption whose carriers do not hold its occurrences;
  - the evidence package and record and their refusals, and a repair previewed through the validation actions;
  - and, as marked scaffolding (reads logged directly on the copy), the gate closing end to end: 2.1 closes and LayerNext moves to 3.1.
- **The earlier suites, rerun on copies carrying the gates:** words, senses, enrichment and structure (26, 26, 24 of 25, 27). The loop-order test, whose L1 and L3 now allow for the gates and the read commands, passes 8 of 8 on copies of live with and without the gates.
