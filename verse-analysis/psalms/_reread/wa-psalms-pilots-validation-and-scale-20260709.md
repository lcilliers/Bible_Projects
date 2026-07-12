# Psalms re-read — pilots validation + honest scale (2026-07-09)

> Result of the three pilots (Psalm 4, 23, 78) and the true scale of completing the Psalter. Companion to the intervention plan + per-psalm reading JSONs (`_read/`) + the progress monitor.

## Pilots — method validated across the size range
| pilot | chars | result |
|---|--:|---|
| **Psalm 4** (small) | 16 | all measurable gates → pass; **iterate-to-pass** worked (G6 caught v6, closed with a verse-level discovery) |
| **Psalm 23** (medium) | 7 | all gates pass **first pass** (G10/G2/G3/G6=0, 17 span-id pairs, 0 dangling) |
| **Psalm 78** (large, 72v) | 10 of 71 | **stanza sub-unit reading validated** (prologue vv3-8); G0 satisfied by focused sections; `process_marker` now set per-verse-read (partial-chapter safe) |

**What is proven:** char-driven reading (char = lens, pairs resolved across the passage as **span-ids**), the genre-aware poetic ledger (source/effect deferred to Phase-2), explicit `none`, the discovery-lookout, the reusable apply tool (`_apply_reread_lexical_v1`), and the iterate-to-pass loop — all work end-to-end. The read also **corrects real errors** the old mechanical pass made (proximity-paired manner/coupling, nearest-proper bearers, object-vs-characteristic role questions surfaced e.g. *evil* in Ps 23, *glorious* in Ps 78).

## The honest scale (important)
- **The Psalter has 3,810 characteristics.** After the pilots: **33 done (0.9%)** — chapters 4 & 23 complete, Psalm 78 at 10/71.
- The reading is **genuine per-verse exegesis** — the char-by-char judgment is the whole point and **cannot be scripted or backgrounded** (a mechanical pass reproduces exactly the errors being fixed). So it advances **only while I'm actively working a turn**, at roughly one small-to-medium psalm (≈10–16 chars) per focused pass.
- **Therefore completing the Psalter is a sustained, multi-session effort** — on the order of ~250–350 focused passes, not a single run. Psalm 78 alone (71 chars) is ~5 passes.
- **Nothing is lost between sessions:** every section is committed to git + tagged `reread-psalms-2026` in the DB. Resume any time; the monitor (`_check_psalms_reread_progress_v1`) shows exactly where it stands and I continue from there.

## How it proceeds from here
Per the standing instruction (proceed without per-step approval): I continue **section by section / psalm by psalm**, committing and re-measuring as I go, filing reading JSONs under `_read/`. The per-psalm record is the JSON + commit + monitor (not 150 separate delta docs). At book close: the 25-unit read-back audit + full delta vs the baseline.

*Filed 2026-07-09. Pilots complete; Psalter rollout underway (Psalm 78 continuing, then onward).*
