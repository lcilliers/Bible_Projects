# #2315 Config alignment for steps 1 to 3: rows to soft delete, update and create

Researcher, chat 2026-10-27 (verbatim): "All stale configs for step 1 - 3 must now be soft deleted or update, and all missing configs for these steps must now be created." Read-only inventory of the live store and the code. Nothing is changed. Method: the rule texts, step descriptions and settings were read from `iba/app/db/iba.db`; code use was searched in `iba/app`. Where a row is a judgement, it says *(inferential)* (B:4).

Applies to steps `reading.open` (0.C), `reading.gather` (0.GAP pre), `reading.observe` and `reading.record` (0.3), the pre and observe gates of `reading.check`, and what they depend on.

## A. Soft delete

| # | Row | Why | Check before delete |
|---|---|---|---|
| A1 | method rule RM-02 `objective-defines-home` (id 128) | Same rule as RO10 (id 140), which is shorter. Keep RO10 and add RM-02's second sentence to it (U1). | RO10 is named in quality check 30; nothing else points at RM-02 *(to confirm)* |
| A2 | method rule RO8 `no-whole-cluster` (id 138) | RM-03 (id 129) states it and names `reading.whole_cluster_reading_start`. | search for "RO8" in config and code |
| A3 | method rule RM-04 `gather-not-redo` (id 130) | RO3 (id 133) states it and adds that a re-read happens only for a recorded gap. | search for "RM-04" |
| A4 | method rule RW-09 `reread-builds-on-prior` (id 170) | RO2 (id 132) states it more fully (observations already recorded read into focus). | search for "RW-09" |
| A5 | method rule RO6 `tables-only-before-d4` (id 136) | "D1 to D3 read table data only: no base data tables" uses the superseded D labels and conflicts with RO4 (base data read in 0.C and 0.GAP pre). RO1 and RO4 cover it. *(inferential)* | confirm RO4 and RO1 are enough |
| A6 | gap type `term_reading_missing` (`cfg_enum reading_gap_type`, `reading.gap_types`) | Pre-gap type with no detector in `iba/app/lib/reading.py` (`PRE` holds only `face_not_gathered`, `meaning_missing`, `open_item`). Observe now answers it per surface (RS-01, `reading.surface_requirements`). | migration 423 tests mention it only in the retired `temp_2310` test |
| A7 | steps `lexical.meaning` and `lexical.relational` (work package `verse-lexical`, still active) with settings `lexical.meaning_max_verses_per_batch` and `lexical.relational_max_verses_per_batch` | The Stage 1 API route that 0.3 observe replaces; their method rules are already inactive. **Decision needed:** #2259 asked whether the reading process takes Stage 1 as its first step; the answer is not in the record. | scripts `iba/app/ps/RelationalReading.ps1`, `Run-Stage1Batch.ps1` and `iba/app/handlers/lexical.py` use them |

**Not to delete:** `lexical.llm_*` (9 settings). `iba/app/lib/surfacemap.py`, `iba/app/handlers/surfacemap.py`, `iba/app/handlers/lexical.py` and `iba/app/handlers/cluster.py` read them; the surface-map tail pass needs them.

## B. Update

| # | Row | Change |
|---|---|---|
| U1 | RO10 `objective-is-home` | add: a verse may come into several scopes from different angles, each adding the observations its objective calls for (from RM-02) |
| U2 | RO1 `verse-text-once` | "D4 observe" becomes "0.3 observe" |
| U3 | step description `reading.observe` | "D3 and D4 input" becomes "0.3 observe input" |
| U4 | step description `reading.record` | "D4 observe written" becomes "0.3 observe written" |
| U5 | gap types `term_cluster`, `base_missing`, `observation_unsupported` | no detector exists. **Decision:** (i) keep and state "no detector yet; routed to recovery by RO4" in the guide, or (ii) build detectors (B6, #2278, on hold with the claims work). I recommend (i) *(inferential)*. |
| U6 | `reading.output_dir` and its `use` text | the researcher ruled one JSON per scope run saved to the cluster's folder (#2304 D2). Today `iba/app/lib/reading.py:98` writes `outputs/reading/<label>`. This needs a code change and the reading index's exclusion (#2279). I propose it as its own unit after the config rows. |

The D labels also appear in the step descriptions of `reading.synergy`, `reading.apply` and `reading.narrate`. Those are later steps and are not touched.

## C. Create

| # | Row | Content |
|---|---|---|
| C1 | method rule on `reading.open` | 0.C scope: a subgroup, or a subset of one by surfaces or verses; the verse references are collected through `surface_subgroup`; the output is one JSON per scope run (#2304 D1, D2) |
| C2 | method rule on `reading.observe` | nodes: created when a subgroup is processed; when a verse enters a scope, the rest of its surfaces are completed and nodes of existing surfaces updated; one node per surface, no check of all nodes for duplicates (#2308 D1 to D3) |
| C3 | method rule on `reading.observe` | nodes without an occurrence id are completed as their verses are read; nodes with no verse and observations with no node are not reached, a stated limit with no action (researcher, chat 2026-10-27) |
| C4 | method rule on `reading.record` | every open item the scope pulls is answered or given a reason in Record; none is silently ignored (#2304 D4, D5). The open-item guide says "settled at the claim step" and is not changed |

No row is created for adopting cluster documents: the documents are captured into `ib_observation` (#2305) and 0.GAP pre no longer reads them (#2310). No row is created for the role filter on the deeper reading (#2161, #2259): it follows observe, so it goes with the claims read process.

## D. Not changed, with the reason

- `reading.focus_words`, `reading.surface_requirements`, RS-01, RS-02, NR-01 to NR-06 and RG-01 to RG-25 were set or restated in #2312 and #2305 and match the design.
- The 25 quality checks on `reading.check` were not assessed one by one; those on narrating belong to later steps.

## E. Decisions needed

1. A7: retire `lexical.meaning` and `lexical.relational` and their two batch settings, or keep them until #2259's question is answered.
2. U5: keep the three pre and observe gap types without detectors (recommended), or build the detectors.
3. U6: agree to the output-folder change as a separate small build.
4. Approve A1 to A6, U1 to U4 and C1 to C4 as listed. On approval I write one migration under `iba/app/migration/`, test it on a copy, apply it live, run `Config-Maintenance.ps1 -Step Validate`, and add the BUILD.md entry.
