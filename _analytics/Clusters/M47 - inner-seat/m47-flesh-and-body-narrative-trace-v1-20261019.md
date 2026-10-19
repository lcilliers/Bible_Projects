# Flesh and body: did the analysis reach the narrative? (trace, v1)

**Date:** 2026-10-19 · **Escalations:** #2162 (flesh and body), #2163 (the word complex), #2160 (threads on completed clusters)

**Question (researcher, chat 2026-10-19, verbatim):** *"yesterday we did substantial work around the flesh and body, including adding new verses for body but I only see limited edits in the narrative related to body.  I have no easy way to check if all the analysis that you showed me in the md files actually found its way into the narratives"*

## 1. Short answer

**You are right: very little of the flesh-and-body work is in the narrative, and the main reason is that the flesh-and-body reading itself was never done.** What was done on 18–19 October was preparation and data work, not reading:
- the overview, the 606-verse list, the completeness check and the batch 1 passages (pulled, **not read**)
- the word complex (#2163): 13 T-coded body and flesh codes moved into M47 in the database. This changed the tags, **not the narrative**. No verses were missing, so no new verses were added to the verse set; the body words now carry M47.
- the verse-level scope rulings for *sarkinos*, the corpse words and "downfall"

**#2162 was closed (approved) on 2026-10-18 with its work outstanding.** Its last resolution reads: *"Held on #2163 ... awaiting direction on #2163, then batch 1."* The handoff's "Next" list (batch 1 reading, batches 2–5, the cross-batch account, Ch 7 rebuilt as flesh and body) has not started. No register update names any flesh-and-body file.

**What did reach the narrative about the body** came through #2160, from other threads:
- update 155 (OT-05.26): Ch 2 *The body raised* (believed, questioned, denied; raised with Christ now; living toward it), 13.1 *Immortal*, Ch 11 *Imperishable*
- update 156 (OT-07.2): 10.12 *Fear in the body* (the hands)
- update 157 (OT-07.3): 10.13 *Anger in the body* (the teeth)
- update 160 (OT-05.16): 10.6, "their god is their belly" (Php 3:19)

## 2. The trace

A new read-only tool does what you asked for: [`reading-to-narrative-trace-v1-20261019.py`](../../cross-cluster-web/reading-to-narrative-trace-v1-20261019.py). For any reading file (`.md`) or verse list (`.csv`), it lists every verse the file names, where the current narrative tells that verse (chapter and section), whether it is a claim source, and which register updates name the file. It reads references with the register's own parser, so a verse counts as told exactly when the register counts it.

This run: [`flesh-body-trace-check-v1-20261019.md`](../../cross-cluster-web/flesh-body-trace-check-v1-20261019.md), with verse-level detail in the `.csv` beside it.

| File | What it is | Verses named | Told now | Not told | Register update |
| --- | --- | --- | --- | --- | --- |
| `m47-flesh-and-body-verses-v1-20261018.csv` | the 606-verse list | 606 | 180 | 426 | none |
| `m47-flesh-and-body-batch1-passages-v1-20261018.md` | batch 1, pulled, not read | 99 | 47 | 52 | none |
| `ot-05-11-m47-body-with-inner-being-reading-v1-20261018.md` | OT-05.11 reading (judged shallow; forwarded to #2162) | 23 | 22 | 1 | none |
| `m47-flesh-and-body-scope-rulings-v1-20261019.md` | scope rulings | 26 | 15 | 11 | none |
| `life-death-ot05-26-body-raised-r0-v1-20261019.md` | OT-05.26, woven | 117 | 91 | 26 | 155 |
| `ot-07-2-fe85-lam4-reading-v2-20261019.md` | OT-07.2, woven | 30 | 26 | 4 | 156 |
| `ot-07-3-anger-ledger-m-reading-v1-20261019.md` | OT-07.3, woven | 46 | 37 | 9 | 157 |
| `ot-98-2-data-verses-reading-v1-20261019.md` | OT-98.2, woven | 85 | 57 | 28 | 159 |

**How to read "not told".** A reading names many verses for context (a root's range, a passage's neighbours, comparison lists). An untold verse is a gap only where the reading **proposed** it for the narrative. The tool cannot tell those apart; §4 does it by hand for the woven files.

## 3. The 606 flesh and body verses now

| Kind | Told | Not told | Where the told ones are |
| --- | --- | --- | --- |
| flesh | 116 | 264 | Ch 7 56, Ch 2 29, 10.7 14, 10.6 12, 10.14 11, Ch 12 10, 10.12 9 |
| body | 53 | 92 | Ch 2 21, Ch 14 10, 10.1 9, 13.1 7, Ch 11 5, 10.7 5, 10.6 4; **Ch 7 1** |
| body + flesh | 3 | 3 | 10.14, Ch 14, Ch 2 |
| corpse | 8 | 59 | Ch 2 5 (most corpse verses are data under the 2026-10-18 ruling) |
| body + corpse, corpse + flesh | 0 | 8 | |

- **Ch 7 is unchanged since 2026-10-12** (`07-flesh-v8-20261012.md`). It is still the flesh chapter, with one body verse. The rebuild as *flesh and body* has not been done.
- The body verses that are told sit mostly in Ch 2 (death and the raised body) and Ch 14.

## 4. Proposals made in the readings, checked one by one

**OT-05.11 (the body with the inner being).** Its three proposals were **not applied**. The item was forwarded to #2162 (OT-05.58), and #2162 was closed.

| Proposal | In the narrative now? |
| --- | --- |
| Restore the body half of Heb 10:22, "and our bodies washed with pure water" (Ch 8, Ch 14) | No. The phrase is in no chapter. |
| Restore 1Co 6:19b–20, "You are not your own … So glorify God in your body" (Ch 6, Ch 14) | No. Neither phrase is in any chapter; 1Co 6:20 is cited nowhere. |
| A short account of the body beside the inner words | Not written (you judged the reading shallow; it was not to be built on). |

**OT-05.26 (woven, update 155).** Of the 26 named but untold verses:
- **Carried through a parallel or neighbour.** Mar 12:24 (Ch 2 quotes the words at Mat 22:29), Luk 7:22 (at Mat 11:3, 5), Joh 12:9 and 12:17 (at Joh 12:10–11), Rev 20:5 (at 20:6), 1Co 15:13–16 (Ch 2 quotes 15:12, 17, 19), Luk 24:46 (at 24:45), Mat 14:2 (Herod is told at Mar 6:16 and Luk 9:7).
- **Left out by decision.** Hos 6:1–2 (taken out as fitted), Gal 6:8 (to the flesh-and-body reading), 2Pe 2:12 and 2:19 (the M57 handle), Rom 9:17, Rom 1:4, Gal 1:1 (data), 1Co 15:14 (the faith handle).
- **Proposed and not woven.** Tit 2:7 (the imperishable said of the inner person, with "integrity" in teaching) and Php 3:11 ("that by any means possible I may attain the resurrection from the dead"; Php 3:10 is in Ch 14). Two small gaps.
- Rom 8:20, Luk 24:40–41 and Joh 12:3 were context only.

**OT-07.2 and OT-07.3 (woven, updates 156, 157).** The untold verses are context: examples of the root's range (1Sa 31:3, Deu 2:25, Mic 1:12, Mic 4:10) and the list of verses where a breach comes before wrath (Num 1:53; 18:5; Jos 22:20; 1Ch 27:24; 2Ch 24:18). Nothing proposed is missing.

**OT-98.2 (woven, update 159).** 28 untold of 85. Not yet checked one by one against the reading's own decisions; the tool lists them.

**The scope-ruling verses** (ruled for reading in the flesh-and-body strand): Mat 24:28, Heb 7:16 and the six "downfall" verses (Pro 29:16; Eze 26:15, 18; 27:27; 31:16; 32:10) are not yet read or told. Of the verses ruled for reading, 2Co 3:3 (*sarkinos*), Eze 31:16 and Eze 32:10 are already cited elsewhere. The others are untold because the reading has not started, which is expected.

## 5. What follows (for your direction)

1. **#2162 was closed before its reading began.** Either reopen #2162, or give the flesh-and-body reading a new escalation, so that batches 1–5, the account and the Ch 7 rebuild are tracked. Raised as #2172 for your decision.
2. **The two OT-05.11 corrections** (Heb 10:22 and 1Co 6:19b–20) are small and stand on their own. They can be applied now under rule 77, or wait for the flesh-and-body reading.
3. **The two OT-05.26 gaps** (Tit 2:7, Php 3:11) can be woven in Ch 2 now, or carried into the flesh-and-body reading.
4. **The trace tool** can be run on every reading before its weave is recorded, and the result filed with it. It turns "did it all land?" into a list you can check.
