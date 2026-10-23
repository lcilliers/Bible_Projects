# 2228 — Recording the gaps of a scope: decision (v1)

Escalation: #2228 v23. Status: **held for your decision; nothing is built.** It is the next step after
collating, and it decides method (rule 44), so it was not built under the permission of 2026-10-23.

**Where the tools stand now:**
- built: scope → collate what is known → the gaps (`Verse-Scope.ps1`, `Reading-Index.ps1`,
  `Verse-Collate.ps1`)
- missing: recording the gaps into the tables → finalising claims from the tables → the narrative

## 1. What recording can do today, and where it stops

Recording today is `Strand-Reading.ps1`, keyed on a **strand**: a word family with an escalation.
(Read in `iba/app/lib/strandreading.py`.)

| Step | Takes | Does it allow a subset? |
|---|---|---|
| `Record` | a JSON of observations and hits | **Yes.** It records only what the JSON names, so a subset of a strand's verses can be recorded. |
| `Map` | every narrative block related to the strand | **No.** It refuses while any related block is unmapped (178 for anger). This is the whole-strand rebuild #2228 was raised for. |
| `Derive` | dispositions for the strand's observations | It works per observation, but the close gate needs every observation of the strand disposed. |
| close gate | every hit faced or given a reason, every observation disposed, every matched item answered | Whole strand. |

So for a scope that sits inside a strand, recording already works. A scope that is not a strand (a
verse list, a chapter, a claim, a subgroup) has no place to record into. And Map, Derive and the gate
still work on the whole strand.

## 2. Options

| | Option | What it means | For | Against |
|---|---|---|---|---|
| **A** | **A reading keyed on the scope** (recommended) | A new `reading` record: the scope's request, the escalation it serves (the task or issue that anchors the reading, as you said of tasks and issues), its verses. `Record`, `Map` and `Derive` take `-Reading` as well as `-Strand`. Map covers only the blocks that cite the scope's verses or tell claims resting on them; the gate covers only the scope's verses and observations. A strand becomes one kind of reading. | One recording path for any scope. Only the scope is gated. Matches discovery v3: the strand is one kind of request, not the container. | A schema change (a reading table, readings on observations), and the strand steps reworked to take a reading. |
| B | Scope inside a strand only | Keep strands. `Map`, `Derive` and the gate take `-Scope <collation file>` and cover only its verses. | Smaller change. | A verse list, chapter or claim scope has no strand to record into, so a strand must be invented for it. |
| C | Record only, no gate | Record observations for any verse with no strand. Leave Map and Derive as they are. | Smallest change. | No account of what a reading covered. Claims and the narrative still rebuild whole strands. |

## 3. Points the decision covers

1. **A, B or C.**
2. **What a reading closes on** (A or B): every verse in the collation's `not read` gap has an
   observation or a stated reason, every observation is disposed, and every matched item answered?
3. **`analysed` on verse_meta:** with D1 (Bible_Books excluded), should a recording set `analysed`
   only through this path?
4. **The session break** you expect between the end of recording and synergising: is it marked in
   the record (a reading at state `recorded`, synergising allowed only from `recorded`)?

| | Your choice | Comment |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
