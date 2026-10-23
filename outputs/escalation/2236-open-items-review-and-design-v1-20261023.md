# 2236 — Open items: review, definition and the registering tool (v1)

Escalation: #2236 (raised from #2228). Status: (a) the review is done, read-only; (b) the design is
for your decision; (c) the tool is built only after (b) is decided (rule 105). Facts are from
`iba.db`, 2026-10-23; the per-item list is
`outputs/escalation/2236-open-items-review-v1-20261023.csv`.

Your description (verbatim on #2236), and what this design is built from:

> "open items is designed to be pointers into further work, without interupting the current flow of
> analysis. it creates a record of related analysis to do and should always be cleared at some point.
> open items must always relate to the core underlying analysis to give it context."

---

## (a) The review: 323 open items on 24 threads

| Measure | Items | Share |
|---|---|---|
| Points at **more than 100 verses** (a whole cluster or a common strong) | 185 (54 of them over 1,000) | 57% |
| Points at 11–100 verses | 26 | 8% |
| Points at 2–10 verses | 22 | 7% |
| Points at one verse | 74 | 23% |
| Names no verse (escalation, event, researcher), or does not resolve | 16 | 5% |
| **No note**, or a note under 60 characters | 141 + 80 = 221 | 68% |
| The same kind:value also open on another thread | 167 | 52% |
| Tied to the escalation that opened it (`opened_by`) | 78 | 24% |
| Already responded to, still open | 101 | 31% |

By kind: cluster 178, verse 74, strong 47, escalation 8, chapter 8, researcher 4, strand 2, event 2.
The two strand items do not resolve: their values are descriptions, not strand codes. 318 of the 323
were opened in October.

**What the numbers mean.** The wide items are wide because of how they are written, not because the
work is wide. The precise target usually exists, but sits outside the item:
- **OT-103.1, `cluster:M58`** (1,299 verses). The thread holds one item per M-code co-occurring with
  anger, and the verses meant are only the shared anger verses, listed in
  `wa-cluster-M02-mcode-face-combinations-v1-20261005.csv`.
- **OT-97.1, `cluster:M12`** (1,278 verses). The note says "7 verses"; the seven are in the M18 group B
  triage CSV.
- **OT-05.1, `strong:G4983`** (122 verses). No note at all.
- **OT-105.2, `cluster:M12`**. The note names the verses and "18 shared verses", but the item matches
  all 1,278.

So when a scope is collated, a cluster item matches every verse of the cluster: the "open item" gap on
all 22 verses of the anger-in-the-bosom scope. That is noise, not a pointer. An item rarely says which
analysis raised it or what is to be done.

---

## (b) Design: what an open item is

**Purpose.** A pointer from the analysis in hand to related work that should not interrupt it. It
records what is to be done, where, and why, and it is cleared at some point.

**Parameters.** Each one is required unless marked:

| Parameter | What it holds | Today |
|---|---|---|
| **Origin** | the analysis that raised it: the escalation (the reading's task or issue), and the anchor in that analysis (an observation, a claim, a narrative block, or a verse being read) | `opened_by` set on 24%; no anchor |
| **Target** | the exact verses the further work is about, given as a scope request (the `Verse-Scope.ps1` selectors) and stored resolved, verse by verse. Kept within a size limit (D3). | a single kind:value, often a whole cluster |
| **Home** (optional) | the cluster, strong, strand or chapter whose work should bring it back. Used to surface the item, not as its scope. | the kind:value itself |
| **Question** | what is to be done or asked, in a sentence, naming what the origin found | the note; empty on 44% |
| **Comes back when** | the trigger: a home being worked, a narrative chapter or block being worked, or a researcher event | on the thread, not on the item |
| **Clearing** | closed with the answer and the escalation that answered it; withdrawn with the reason; superseded by a named item. Never left open with no next step. | as today (rule E:18) |

**Matching** (the "open item" gap and thread checks). An item matches a scope when its **target
verses** meet the scope's verses, or when the scope's work is its **home**. It never matches on a whole
cluster's verses. This removes the sweeping matches.

**Thread.** Threads stay as they are: a thread groups items for a topic, its lifecycle is unchanged
(rule E:18), and it is shown in the register. What changes is the item. (D2 asks whether a thread
should instead be one per origin analysis.)

## (c) The tool (after the decision)

- `Open-Item.ps1 -Action Add`, through `run.py`, with these parameters:
  - **origin:** `-Origin` (escalation), `-Anchor` (`observation:12478`, `claim:C-330`, `block:"10.1 / The bosom"` or `verse:Ecc 7:9`)
  - **target:** the `Verse-Scope.ps1` selectors, or `-File`
  - **the rest:** `-Home`, `-Question`, `-ComesBackWhen`, `-Thread OT-nn`
- **What it checks:** that the target resolves within the size limit, the question is given, the origin exists, and the item is not a duplicate on the same thread. Then it records the item and its verses.
- **Reports:** `-Action List` and `-Action Show`.
- **Answering:** stays with `Escalation.ps1`.
- **Schema:** new columns on `escalation_thread_item` (origin, anchor, question, target request,
  comes back when), and a table of the item's target verses. `Escalation.ps1 Match` and
  `Verse-Collate.ps1` then match on target verses and home.
- **Recording:** strand reading and any later reading raise their items through the same code.

**Reformulating the 323 existing items** (your point a), with the tool, in three groups:
1. **Mechanical, where the target is written down:** the item's note lists the verses, or its
   thread names the file that lists them (OT-103 with the face-combination CSV, OT-97 with the triage
   CSV, OT-105 notes). The target is set from that source and the change recorded as a response.
2. **By reading the origin:** items with no note or no list (OT-05's strongs, OT-94). Claude reads
   the origin the thread names and writes the target and question; each one is recorded and listed for
   your review.
3. **Withdrawn or superseded:** duplicates of the same target and question on two threads, and items
   already answered (101 have responses). Each one is closed with the reason recorded.

## Decisions for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| D1 | The parameters above (origin and anchor, target verses, home, question, comes back when, clearing): accept, or change? | | |
| D2 | Threads: keep them as topic groups (recommended), or make one thread per origin analysis? | | |
| D3 | A size limit on an item's target: **recommended 200 verses**. A wider item must be split or reformed. | | |
| D4 | "Always cleared": list items older than a set age at session start (**recommended 60 days**), or a stronger gate (a reading cannot close while it has raised items with no target)? | | |
| D5 | Reformulate the existing items in the three groups above: mechanical first, then reading, then closing, each change recorded on its item? | | |
