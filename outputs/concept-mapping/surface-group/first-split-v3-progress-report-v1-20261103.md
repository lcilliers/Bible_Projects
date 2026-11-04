# Progress report: first split of surfaces, batch first-split-v3-20261103 (#2354)

Snapshot 2026-11-03 17:00 UTC, while the cycle is still running. Every group below is the answer of the model (qwen3:30b, prompt v3) and is inferential until the researcher confirms it. Nothing has been written to `iba.db`.

## Where the run stands

| | |
|---|---|
| Surfaces on the list (distinct live surfaces of `surface_subgroup`) | 6,069 |
| Judged | 3,367 (55.5 percent) |
| Failed (no usable answer) | 0 |
| Left | 2,702 |
| Started | 2026-11-03 06:05 UTC; 10 work periods (60 minutes work, 10 minutes rest) |
| Speed | 10.1 s per surface (mean of the last 50); 10.2 s mean over all judged, median 10.0 s |
| Server | steady temperature with the 60/10 cycle (researcher's observation); no halts, 0 periods in a row without progress |
| Estimated finish | 2026-11-04 01:44 UTC (work time left at the recent mean, plus the rests) |

## Groups so far

| Group | Surfaces | Share of judged | Rows for the word (`surface_subgroup`) |
|---|---|---|---|
| inner_being_state | 1,469 | 43.6 percent | 5,451 |
| behaviour | 805 | 23.9 percent | 2,735 |
| other | 693 | 20.6 percent | 1,493 |
| being | 400 | 11.9 percent | 1,077 |
| **Total** | **3,367** | | **10,756 of 13,458** |

`rows_for_word` counts the placements in `surface_subgroup` that carry the English word. It is not a weight of significance: it shows that a word has many Strong's terms and may work differently under each. One group per word would be written to all of its rows, so the load step has to allow for that.

## Largest words in each group (by rows for the word)

- **inner_being_state:** strong 28, right 26, desire 24, mighty 24, strength 24, fear 22, good 22, trouble 22
- **behaviour:** evil 24, wrong 21, keep 19, cry 18, praise 18, rule 18, angry 17, destroy 17
- **being:** power 23, wealth 15, body 13, gift 12, flesh 11, gifts 11, dominion 10, cover 9
- **other:** please 14, up 14, away 13, out 12, harm 11, left 11, you 10, cause 9

Examples of the reasons the model gave for `other`: "please" (not a Bible term), "up", "away", "out" (preposition, no inner being reference), "you" (pronoun).

## Researcher's positions (recorded on #2354 v35)

- The state/behaviour border is untested and settled in context and downstream; the split stays.
- `being` is hard for the model to judge; not a reason to stop or revise prompt v3; the researcher deals with it separately.
- `other` works.
- Behaviour and state are interrelated; analysed after all surfaces are grouped.

## Not done

- The remaining 2,702 surfaces (the cycle is judging them).
- Reviewing the results, and loading groups into `surface_subgroup.surface_group` (a database write; not built, needs design and approval).
- The second pass over `other`.
- Nothing is committed to git.

## How to read it live

`Surface-Judge.ps1 -Action Progress -Batch first-split-v3-20261103` for the figures; `-Action Stop` to end the cycle after the surface in hand; `-Action Cycle` to resume.
