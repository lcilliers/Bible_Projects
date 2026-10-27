# #2314 The three steps (0.C scope, 0.GAP pre, 0.3 observe): design and build status

One home for the three steps, as of 2026-10-27. It points to the sources and states the status; it does not restate them (B:3). Where this file and a source disagree, the source wins.

## What the three steps are

The researcher's cycle on one JSON (#2304 design, section 1): 0.C builds the scope JSON of verse references from a subgroup or a segment of one; 0.GAP pre pulls into it every existing observation and every open item for those verses; 0.3 observe finds the missing observations on the surfaces and writes them into the tables. Not synergy, claims or narrative.

## Design

| Part | Source |
|---|---|
| The cycle, 0.C, 0.GAP pre, observe, and the researcher's answers | `outputs/escalation/2304-reading-cycle-one-json-design-v3-20261026.md` |
| The surface model: a word is the surface with its embedded Strong; what Observe requires per surface; the decisions taken | `outputs/escalation/2312-scope-pull-observe-gap-analysis-v2-20261027.md` |
| 0.GAP pre without the document read; open items carry subgroups | `outputs/escalation/2310-gap-pre-open-item-hooks-v1-20261026.md` |
| Prior analysis in documents captured into `ib_observation` | `iba/app/BUILD.md` sections 420 and 421 |

## Build status

| Step | Built | Where it is recorded | Status |
|---|---|---|---|
| 0.C scope JSON | yes | BUILD.md 423 (`iba/app/lib/versecollate.py`) | applied live |
| 0.GAP pre pull | yes | BUILD.md 422 and 423 | applied live |
| 0.3 observe | yes | BUILD.md 423 (`iba/app/lib/reading.py` `surfaces_state`, `gate_observe`; `recordingpass.py`, `observationrecord.py`) | applied live |

Tested on a copy: `iba/app/tools/temp_2312_surface_observe_test_run.py`, 22 of 22 cases pass.

## Not done

- Observe has not been run on a real full scope. Next: run the three steps on new and existing subgroups (researcher, chat 2026-10-27).
- The older tests `temp_2273_reading_phases_test_run.py`, `temp_2304_reading_cycle_prototype.py` and `temp_2310_gap_pre_test_run.py` were experimental and are not to be systemised (researcher, chat 2026-10-27).
- 14,730 nodes carry no occurrence id (10,179 name a verse and no word); 63 observations have no node (BUILD.md 423). The nodes are completed as their verses are read; nodes with no verse and observations with no node are never reached, a noted limit with no action (researcher, chat 2026-10-27).
- The build of the three steps is approved (#2312, #2310, #2308, #2304).

## Where the leftovers went

- The verse-level read test (`iba/app/lib/versecollate.py:199`): the claims read process, by the researcher's ruling (chat 2026-10-27: "verse level read in context, and the associated observations, belongs in the claims read process"). Items #2262, #2276, #2278 and #2280 are on hold for it.
- Stale configs and the retired method: #2315 (carries the retire half of #2275 and #2277, #2279, #2281 to #2285).
- New features outside the three steps: #2235 (key words of a scope, reverse lookup) and #2303 (T-a tool).
- Config alignment for the three steps (stale rows soft deleted or updated, missing rows created): #2315, table in `outputs/escalation/2315-config-alignment-steps-1-3-table-v1-20261027.md`.
- Not ready for approval: #2305.
