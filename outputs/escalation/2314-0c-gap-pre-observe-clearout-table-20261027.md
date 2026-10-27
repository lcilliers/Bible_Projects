# #2314 Clear-out of open items for 0.C, 0.GAP pre and 0.3 observe: what the #2312 build covers

Developer Mode session 2026-10-27. Researcher's aim (chat): clear the old, superseded points for the three steps, leave the design document and build status, then clear the stale configs.

Sources read: the latest comment and resolution of each item; `iba/app/BUILD.md` sections 421 to 423; `iba/app/lib/versecollate.py` and `iba/app/lib/reading.py` as they stand; `cfg_setting reading.gap_types`. This table changes nothing.

## Finding that changes the plan

Fewer items are fully covered than their titles suggest. Observe (step 3) now works per surface (`iba/app/lib/reading.py` `surfaces_state`), but the verse-level collation keeps the old test: `iba/app/lib/versecollate.py:199` marks a verse `read` when it has any non-withdrawn observation or any ledger face. That is the #2262 defect. It sits in the collation and the claims-side gap types (`not read`, `observed, no claim`), which belong to the later steps, not to the three steps.

## Table

Covered means the #2312 build (BUILD.md 423) or the earlier steps (421, 422) does the whole job the item names.

| Item | What it asked | Done by | Left over | Proposed |
|---|---|---|---|---|
| #2262 gap analysis counts any observation as read | quality test for "read" | Observe checks role, face and term per surface (423) | verse-level `read` test at `versecollate.py:199`, used by the claims-side gaps | keep, narrowed to the verse-level test |
| #2275 B3 D1 and D2 in a session; API steps retired | word and cluster read in a session; retire the API work packages | design replaced by #2304 and #2312 (scope JSON, Observe) | retiring `lexical.meaning`, `lexical.relational`, `cluster-reading` and their `lexical.llm_*` settings | close the design half; the retire half goes to stale configs |
| #2276 B4 collation reads every observation | all non-withdrawn observations; passage, T-codes, meaning text, renderings | 423 does the observation half | passage, T-codes, meaning text and renderings: unresolved, not found in `versecollate.py` | keep until that half is decided |
| #2278 B6 gap types and their checks | 14 gap types found and checked | 422 retires `read_in_files_only`; pre detectors exist for 3 types | `term_cluster`, `base_missing`, `term_reading_missing` and the post types have no detector | keep |
| #2280 B8 ledger faces gathered | 4,239 ledger faces gathered into the observation record; strand enums retired | 421 captured the ledger documents; 423 counts a ledger hit as gathered when a face finding holds it | faces on `reading_strand_hit` are not written as findings; `face_not_gathered` is open | keep |
| #2296 U6 reading recorded per occurrence | occurrence id on nodes, backfill, per-occurrence gap analysis | 421 sweep, 423 (occurrence id on nodes) | 14,730 nodes still lack an occurrence id | keep; researcher: actioned when a reading reaches its clusters |
| #2235 key words of a scope, reverse surface lookup | new design | none | all of it | keep; a new feature |
| #2303 T-a addition has no tool | tool to write `cluster_strong` | none | all of it | keep; returns at the first T-a addition |
| #2277 B5 hard-coded reading rules into config | rules out of `versecollate.py`, `reading.py`, `recordingpass.py` | not assessed | not assessed | stale configs unit |
| #2279 B7 output folder, index exclusion | file location rules | none | all of it | stale configs unit |
| #2281 B9 `cluster.status` lifecycle | redesign or retire | none | all of it | stale configs unit |
| #2282 B10 glossary check, worked examples | glossary currency check | none | all of it | stale configs unit |
| #2283 B11 quality checks at the gates | 21 checks on `reading.check` | not assessed | not assessed | stale configs unit |
| #2284 B12 passage method retired | retire work packages, steps, scripts | none | all of it | stale configs unit |
| #2285 last live Workflow instruction files | assess four files | none | all of it | stale configs unit |
| #2268 reading process not built on the study's expectations | root of B1 to B12 | the three steps (423) | B3 to B12 above | open until its children settle |

## Waiting on the researcher, not mine to close

#2161, #2259, #2270, #2304, #2305, #2308, #2310, #2312. The build of the three steps is #2312.

## Result for the clear-out

- One item is plainly closable: the design half of #2275.
- #2277, #2279, #2281 to #2285 concern the stale configs and the retired method, not the three steps. They suit the next unit.
- The pieces of the design and build status exist: #2304 design v3, #2312 gap analysis v2, BUILD.md 421 to 423, the USER-GUIDE entry. Step 3 of the plan joins them in one file.

## Decisions for the researcher

1. Approve closing the design half of #2275 and moving its retire half with #2277, #2279, #2281 to #2285 into one stale-configs item, so the list for the three steps holds only items with a real leftover. Or name the items you want closed regardless.
2. Say whether the verse-level `read` test (#2262, #2276, #2278, #2280) belongs to the three steps or to the later claims and narrative steps.
