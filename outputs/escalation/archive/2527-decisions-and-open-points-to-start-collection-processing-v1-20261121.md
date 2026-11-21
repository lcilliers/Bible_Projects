# #2527 Decisions that start collection processing, with the open points that bear on them (v1, 2026-11-21)

For the researcher's review. Three decisions (D1 to D3) and the open points carried from #2463, #2448 and the Programme book's "what is not yet defined", set against each other because each decision settles or changes some of the points. Measured against the approved Programme book (Workflow/Programme/programme_prose/wa-programme-prose-extract-20261120.md, section Programme flow). The work these decisions start is #2526; the claims are #2528; the narrative is #2529. The disposition of every part of the five old items is in outputs/escalation/2463-open-items-aligned-to-the-programme-v1-20261121.md.

## 1. Where collection processing stands (checked facts)

- 169 collections are live. Only thought has been opened in the layered reading. Its stage 1 (the lexical analysis of the words) was run and closed: 394 aspects validated, 281 observations, 518 nodes on all 394 member occurrences (#2463 v38). Those results were made before the method was corrected and are to be revisited when collection processing starts properly (researcher, #2515 Q2).
- No subgroup stands for any collection. The grouping built under #2509 was run on thought and you declared the run a failure; nothing previously done stands and the subgroup methods are rerun (researcher, #2515 Q3). The 33 surfaces of thought are unplaced.
- No stage 2 or stage 3 result exists for any collection.
- The configuration sets no order for the collections, no number of rows for a sitting and no rule for resuming other than the open state of the ledger (Programme flow, Volume).

## 2. The decisions

### D1 Where collection processing starts, and in what order

| Option | What it means | Basis |
|---|---|---|
| A (recommended) | Thought is the pilot. It is taken through stages 1 to 3 first (stage 1 revisited, stage 2 grouping, stage 3 steps 1.1, 1.2, 2.1, each gate passed). The order of the other collections is decided after the pilot, from what it showed. | The Programme book says the layered design has not been run through a stage on any collection, so it has not met the test where an earlier technique failed, consistency at scale. Thought is the only collection with stage 1 done and the only one whose evidence report exists. A full order set now would be set before that test. |
| B | Set the full order now, by alphabetical order, smallest evidence first, or by surface group. | Gives a plan for all 169 at once, but the sitting size (D2) and the grouping method (D3) are not proven, so the order could not be tested against them. |

### D2 The size of one sitting, and how work resumes

| Option | What it means | Basis |
|---|---|---|
| A (recommended) | The collection is the unit of a sitting. Every step is opened, pulled, recorded and checked for one named collection; a collection may be left partly answered and the next pull returns what is left; a job longer than a few minutes runs outside the session with a log. No cap on rows. | This is what is built and configured today (Programme flow, Volume: the pull writes every open row and caps only the evidence shown per row; the file is checked whole and written in one transaction). |
| B | Cap the number of rows in one sitting, set in configuration. | Protects a session from a large collection, but changes built behaviour and needs a configuration row, a rule and a resume rule. |

### D3 How the subgroup method is re-set

| Option | What it means | Basis |
|---|---|---|
| A (recommended) | I design the grouping method from the stated purpose of the subgroup in the programme prose and bring the design to you. It is tested on thought only, shown to you, and nothing is run on another collection until you have read thought's grouping. | The grouping is judged by Claude from the evidence and scrutinised by the researcher (your definition at #2463 v16, behaviour rule 132). The earlier build left the grouping to the researcher's instruction and had no method for it (#2463 v39). The Programme book gives the purpose but not the method. |
| B | You state the method and I build to it. | Settles it faster but puts the design on you, which you have said is the work you expect of Claude. |

Approval means: D1, D2 and D3 as chosen (recommended A, A, A). On approval, #2526 starts with those choices.

## 3. The open points, and which decision each bears on

### 3.1 Settled or changed by D1 to D3

| Open point | Source | Bears on | Effect |
|---|---|---|---|
| Revisit the thought stage 1 results; adjust or delete any observation found wrong | #2463 v40 (1), #2515 Q2 | D1 | Under D1 A this is the first step of the pilot, before the grouping. Under B it waits for thought's place in the order. |
| Check the anomalies from the first stage 1 run against the span and STEP: H1961 in Eze 19:10 (surface reason, from the phrase by reason of, which belongs to the preposition); G1161 in Rom 2:3 (suppose on a particle); H0413 in Jer 40:4 (think on a preposition); H6424 in Pro 5:21 (stored to envy against the lexicon range to weigh, make level); G6063 and G1097 in 2Cor 5:16 (regard, once regarded) | #2463 v40 (1) | D1 | Same step as the line above. |
| Whether a word row for every code of a multi-code unit makes function words rows | #2463 v40 (1) | D1, D3 | Decided on thought during the revisit, because the answer changes the number of rows and the grouping input. |
| The subgroup methods are rerun; no subgroup stands | #2463 v40 (2), #2515 Q3 | D3 | The method is the content of D3. |
| What a subgroup is for, stated separately for its two uses (the verse-lexical observations of stage 3, and the inner-being observations of stage 4) | Programme flow, what is not yet defined | D3 | D3 A settles the stage 3 use on thought. The stage 4 use waits for #2528. |
| The order of the collections | Programme flow, what is not yet defined | D1 | The content of D1. |
| The size of a sitting and the rule for resuming | Programme flow, what is not yet defined | D2 | The content of D2. |
| The node and observation classes the checker still lists (nodes with no role, observations with no relevant-role node, no collection, same text, no live node, nodes with no surface or occurrence, member surfaces with no live node) and the validation flag of ruling N14, not built | #2448 v12 | D2 | Worked as each collection is read, with iba/app/ps/Node-Check.ps1 before and after. They enlarge one collection's sitting, which is why D2 has to be settled first. |
| The earlier observations and the documents that name a verse of the collection: read for those verses only, improved or retired with a reason | #2448 v11, Programme flow | D2 | The method is not yet built for the layered reading. It is part of a collection's sitting and adds to its size. |

### 3.2 Not settled by D1 to D3, and where each is carried

| Open point | Source | Decided by | Carried in |
|---|---|---|---|
| The alignment of the configuration's stage numbering with the order of the layers | Programme flow, what is not yet defined | Claude proposes the change; you approve it | #2526 step 4 |
| The old reading machinery: Reading.ps1 Open on a subgroup, reading.home_cluster, rules 119 and 120, RO13, RM-03, RO8, the USER-GUIDE line that waits for #2448; the breach at #2448 v16 | #2448 v13, v16, v17 | Design to you first, built in developer mode | #2526 step 4 |
| The inner-being layer: what it reads, how it is done, what it leaves; the grain of a working across several nodes; the unit of a batch; the nuances of a working across verses; consistency from one read to the next | Programme flow | You, from what stage 3 shows | #2528 |
| The formulation of claims; the 294 verse-only claims to be re-evaluated against their observations; the stance of a link; binding values | Programme flow, #2486 | You, after stage 3 | #2528 |
| How the chapters of the narrative follow the collections beyond the chapter on the inner being at work | Programme flow, #2376 | You, after the claims | #2529 |
| How the per-cluster science reviews are used in the claims reading | Programme flow | You, at the claims reading | #2528 |
| The step that records surfaces sorted wrongly into the four groups, unjudged or set aside; whether a surface set aside is read afterwards; whether a pairing of fewer than three shared verses is left unread; whether surfaces with no group set are in the collections | Programme flow | You | Not yet carried by an item; raise when the first collection reaches the step. |
| Whether the study boundary of the Strong's codes (the codes the cluster method allocated) stays or widens | Programme flow, what stands unsolved | You | Not carried; it does not block the pilot. |
| No check of content before a stage closes; no independent control of completeness; the layered design not yet run through a stage; the recorders audited after the first run failed, not before | Programme flow, what stands unsolved | The pilot is the test of the third; the others need a design from Claude | #2526 step 1 reports on them after the pilot. |

## 4. What happens after approval

1. D1 to D3 are recorded on #2527 with your words and #2527 is completed.
2. #2526 step 1 begins: the stage 1 revisit and anomaly check on thought, then the grouping method design (D3 A) to you.
3. Nothing is run on a collection other than thought before you have read thought's grouping.
