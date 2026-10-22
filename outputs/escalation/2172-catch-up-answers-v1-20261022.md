# 2172 — Catch-up decisions: your answers and what was done

Escalation: #2172 (v26). Answers to section 3 of `outputs/escalation/2172-catch-up-plan-v1-20261022.md`.
Everything below was checked read-only on 2026-10-22. Nothing was imported or built.

Researcher, chat 2026-10-22 (verbatim): "Q1 M63 is likely to closest. Did you check the location of
associated strongs?  Q2 - this should not happen. report it to investigate.  Use open items to raise
it. Q3 - raise an escalation  and add a open item Q4 provide further information on these
dispositions, where do they fit in.  Q5 register all these open readings as open items"

## Q1. Origin of thought: where its Strong's numbers are assigned

No, I had not checked before. I have now. The strand's words are the 19 thought words (23 variant
codes) of the v2 ledger's change-of-character pull,
`_analytics/cross-cluster-web/origin-of-thought/change-of-character-thought-words-pull-v1-20261001.csv`
(369 verse rows). Their live assignment in `iba.db` `cluster_strong` (deleted rows excluded):

| Cluster | Words (variant codes) | Pull rows |
|---|---|---|
| M64 Will & Resolve | H2803I, H2803H, H2803G *chashab* (to devise, plan); H3336 *yetser* (frame, purpose) | 106 |
| M06 Malice & Enmity | H4284 *machashabah* (thought, plan); H4209 *mezimmah* (purpose, scheme) | 75 |
| M15 Knowing & Understanding | H2803J *chashab* (to regard, consider); G1271 *dianoia* (mind); G3540 *noema* (thought); H7476 *rayon* (thought, Aramaic); G1761 *enthumesis* (reflection); G3053 *logismos* (reasoning); H7454 *rea* (thought); G1270 *dianoema* (thought); H6248 *ashtuth* (thought) | 60 |
| M26 Judgment & Condemnation | G3049 *logizomai* (to reckon, consider) | 39 |
| T3 Operations | H1819 *damah* (to be like, liken, ponder) | 30 |
| M84 Outcry & Shouting | H1897 *hagah* (to meditate, mutter) | 25 |
| M63 Reasoning & Interpretation | G1260 *dialogizomai* (to reason, discuss); G1261 *dialogismos* (reasoning) | 29 |
| M20 Doubt & Discouragement | H8312 *sarappim* (disquieting thoughts) | 2 |
| T2 Supplementary / FLAG | H5587A, H5587B *seippim* (divided thoughts) | 3 |

What this shows:
- M63 holds 2 of the 23 codes (29 of 369 rows). By words, M15 holds the most (9 codes); by rows,
  M64 holds the most (106).
- The heart word H3824 *lebab*, which the ledger cites for "say in the heart", is in M47 Inner Seat.
  H3820 *leb* has no live cluster row.
- Several assignments look like they don't fit the thought sense. This is my reading, not
  confirmed: H1897 *hagah* is in M84 Outcry & Shouting, G3049 *logizomai* is in M26 Judgment &
  Condemnation, and H4284 and H4209 are in M06 Malice & Enmity. Most of these rows came from
  `heuristic-family-grouping-v1-20260905` or `old-system-migration`.

The strand's home is still your choice. You said M63 is "likely to closest", but the data does not
point to M63. M15 Knowing & Understanding holds the most thought words, and M64 Will & Resolve the
most verse rows. Your call: M63 as you said, M15, or M64.

## Q2. A ledger verse with no strand word: raised to investigate

- Raised as #2216 ("Ledger verses cited with no strand word in them"), assigned to Claude.
- Added as open item OT-108.1 on the new thread OT-108 (#2218).
- How many there are is not yet known; none has been listed. Finding them is the first step of #2216.
- Catch-up B grounds no such verse until this is settled.

## Q3. Hits with no per-hit face: escalation and open item

- Raised as #2217 ("Strand hits with no per-hit face recorded"), assigned to Claude.
- Added as open item OT-108.2.
- Affected (checked against the CSVs): life-death Q4 and origin of thought, whose pulls have no face
  column, and the two ledgers with no pull of their own, the anger strand ledger (AN) and anger at
  the inner seat (MS). Every unit of fear, anger units 1 to 5, life-death units 1 to 4 (with their
  supplements) and Q2 and Q3 have a face for every hit in their pull or faces CSVs. The hit counts
  per strand are part of #2217.

## Q4. The October dispositions: what they are and where they fit

**What they meant in October.** Each row ledger ends each observation with a disposition, which was
a proposal for the narrative, not a record of what was done. Life-death unit 1 heads the column
"Disposition (proposed)". The legends:
- `_analytics/Clusters/M02 - anger-wrath/anger-strand-observation-ledger-v1-20261001.md` line 28
- `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit1-v1-20261002.md` line 29
- the origin of thought ledger, Columns

| Code | October meaning | Count* |
|---|---|---|
| W | woven: weave it where it touches existing text | 506 |
| RS | reshapes existing text | 45 |
| NS | new structure needed (a new section or part) | 35 |
| H | held (not used yet; parked) | 11 |
| D | stays in data (true, but not for the narrative) | 147 |

\*Counted by a simple table parse over the 19 ledger files. The total is 744 of about 950 rows, so
the parse misses some rows: none of the 31 MS rows, and 53 of origin of thought's 109. Treat the
counts as a lower bound. By ledger, D is mostly the anger units 1 to 5 (128 of the 147).

**Where they fit in the new process.** The new process has no disposition column. A disposition is
the observation's `ib_observation.status`, set at step 6 Derive (`iba/app/lib/strandreading.py`,
`status_of`). There are four outcomes, and the strand close gate refuses any observation still at
`draft`:

| Derive outcome | `ib_observation.status` | What it records |
|---|---|---|
| claim | `resolved` | carried by a named claim in the narrative |
| held | `open` | held as a thread item |
| silent | `silent` | not used, with why |
| withdrawn | `withdrawn` | dropped, with why |

How the October codes line up with these. This is my reading, not a decision:

| October | Likely outcome at step C | Why it can't simply be copied over |
|---|---|---|
| W | claim, if a current claim on the same verses means the same thing | W said "weave", not "woven". All 19 ledgers match a woven/where search (by text match; not checked row by row), so step C can start from those records, but it still has to find the claim. |
| RS | claim, where the reshaped text holds a claim that carries it; otherwise held | whether the reshaping was ever done is recorded per ledger, not per row |
| NS | held, unless the structure was built (e.g. NS-1, 10.4 Speaking, approved in the origin of thought ledger) | it proposed structure, not content |
| H | held (a thread item; OT-07 "Held items in the earlier ledgers" already carries some) | closest match |
| D | silent, with "stays in data" as the why | closest match |

This is why the plan's option A keeps the October code as a note (`revisit_note`) and sets the
status only at step C. Option B (map the code to a status now) would mark W rows as `resolved`
before any claim is shown to carry them. Decision 4 is still open: A or B.

## Q5. The prose readings of 6 to 19 October: registered as open items

All of them are on thread OT-108 (#2218), one item per cluster. Each item's note names every file
by full path, so `Escalation.ps1 -Action Match -Cluster <code>` finds them when a strand of that
cluster is pulled.

| Item | Cluster | Reading files |
|---|---|---|
| OT-108.3 | M64 Will & Resolve | 13 |
| OT-108.4 | M72 Authority & Dominion | 3 |
| OT-108.5 | M08 Pride & Arrogance | 6 |
| OT-108.6 | M09 Humility & Lowliness | 7 |
| OT-108.7 | M07 Shame & Confusion | 2 |
| OT-108.8 | M18 Desire & Longing | 20 |
| OT-108.9 | M53 Dishonor & Disgrace (the same 2 files as M07) | 2 |

Limits:
- I listed only `.md` reading files dated 6 to 19 October in each cluster's own folder. Register
  CSVs, pulls and summaries are not counted as readings.
- The plan said "about 25 files" for M64; this listing found 13 reading files. The difference is
  the CSVs, pulls and summaries in that folder.
- A reading kept in another folder would not be in this list.

## Still open

- #2172: decision 1, the home cluster for origin of thought (M63, M15 or M64), given the Q1 table.
- #2172: decision 4, option A (keep the code as a note) or B (map it now).
- #2216 and #2217: decisions 2 and 3 wait on these. Decision 5 is settled: the readings are open
  items on OT-108 and wait for the study to re-open.
- #2172: catch-up B can run once decisions 1 and 4 are settled. Verses and hits from #2216 and
  #2217 are left out until those are investigated.
