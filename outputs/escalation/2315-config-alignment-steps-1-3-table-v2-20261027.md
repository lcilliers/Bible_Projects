# #2315 Steps 1 to 3: what is stale, what is missing, what is not built (v2)

Replaces v1. The researcher's rulings, chat 2026-10-27 (verbatim): "E1 - retire if these routines are not used elsewhere, especially in the claims cycle which is still not designed. 2. I am expecting that you have built all the code components for step 1 -3 if that is not the case then do it. do not leave any cleanup for later. U6 this is not in keeping with the instructions which says all analytic outputs are files by cluster. E4 - I am highly suspicious that you have the realignment of configs under control. I suspect there are numerous rules and other items previously identified that is silently ignored."

v1 was wrong in one respect: it treated #2277, #2279 and #2281 to #2285 as stale-config clean-up. They are builds from the #2268 change set (`outputs/escalation/2268-config-alignment-change-set-v1-20261024.md`, section 9, B1 to B12), several of them inside steps 1 to 3. This file checks the whole change set against the live store and code. Nothing is changed yet.

## 1. How this was checked

- All 61 method-rule keys named in change set section 5, all 23 settings named in section 3, the enums of section 4 and the control-map rows of section 7 were compared with the live `cfg_*` tables.
- Each build of section 9 was compared with `iba/app/lib/reading.py`, `versecollate.py` and the settings.
- Not checked: the 57 behaviour and escalation rule rows of section 2 one by one (only B:68 to B:73, B:84 to B:95 and B:109 to B:112 were read), and the 12 new quality checks of section 6 against their text.

## 2. Present as planned

All 61 method rules of section 5 exist (RC-01 to RC-07 are inactive because the word.read and cluster.read route was dropped when #2304 replaced #2275's design). The enums `observation_role`, `observation_route`, `observation_disposition`, the `ib_observation.reading` status flow and the `study_method` control-map row are in place.

## 3. Not as planned (the evidence for E4)

| # | Finding | Evidence |
|---|---|---|
| F1 | B:70, B:71, B:72 still carry the old era in `enforced_by`: "applied when writing strand ledgers", memory file names (memory was retired, #2184), "Not mechanically enforced" | `cfg_behaviour_rule` ids 70 to 72 |
| F2 | Setting `reading_index.exclude` named in the change set (B7) does not exist | `cfg_setting` |
| F3 | Table `cfg_method_example` (R10, B10) does not exist | `sqlite_master` |
| F4 | Reading rules still hard-coded (R1, B5): state lists and constants in `iba/app/lib/reading.py` (`STATES`, `NOT_SCOPE`, `SETTLE`, `PART_MARK`, `DISPOSE`) and `GAPS` in `iba/app/lib/versecollate.py` | code read |
| F5 | Gap types with no detector: `term_cluster`, `base_missing`, `observation_unsupported` (and `term_reading_missing`, superseded by Observe's surface check) | `reading.py` `PRE` holds three detectors |
| F6 | Reading output still goes to `outputs/reading/<label>` (`reading.py:98`); R7 says readings sit in the cluster's folder | code and setting |
| F7 | Duplicate method rules: RM-02 and RO10, RM-03 and RO8, RM-04 and RO3, RO2 and RW-09; RO6 uses the old D labels and conflicts with RO4 | rule texts compared |
| F8 | D labels remain in the step descriptions of `reading.observe` and `reading.record`, and in RO1 | step and rule texts |
| F9 | Ledger faces (4,239 on `reading_strand_hit`) are not written as findings (B8, W-3) | #2314 table; `face_not_gathered` open |
| F10 | `cluster.status` still advances on the retired Stage 1 coverage (B9) | change set section 4 |
| F11 | Collation does not give passage, T-codes, meaning text or renderings (B4 second half) | not found in `versecollate.py` |
| F12 | Quality checks have no delivery at the gates (B11); passage-method retirement deferred (B12, the first attempt failed on 9 coherence errors) | #2268 comment; BUILD.md 406 |
| F13 | Generated role guide (W-4) not built; `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` still exists | #2285 |

## 4. Proposed work, in this order (each its own test on a copy and BUILD.md entry)

Config and code together, so nothing is left for later.

| Unit | Content | Findings |
|---|---|---|
| 1 | Config clean-up: soft delete RM-02, RO8, RM-04, RW-09, RO6 (keeping RO10 with RM-02's sentence, RM-03, RO3, RO2); D labels to 0.C, 0.GAP pre, 0.3; B:70 to B:72 `enforced_by` reworded; create the missing method rules (scope definition, node creation and completion, open items answered in Record) | F1, F7, F8 and the C rows of v1 |
| 2 | Hard-coded rules into config, read by the code | F4 |
| 3 | Gap detectors for every gap type of the three steps, or the type retired where Observe makes it redundant; tests | F5 |
| 4 | Readings written to the cluster's folder; reading index excludes them (`reading_index.exclude`); USER-GUIDE and worksheet | F2, F6 |
| 5 | Collation gives passage, T-codes, meaning text, renderings to Observe | F11 |
| 6 | Faces on `reading_strand_hit` written as face findings; strand enums retired | F9 |
| 7 | `cluster.status` redesigned or retired | F10 |
| 8 | `cfg_method_example` and the glossary currency check | F3 |
| 9 | Quality checks delivered and checked at the pre and observe gates | F12 |
| 10 | Retire the Stage 1 route (E1): steps `lexical.meaning` and `lexical.relational`, `iba/app/handlers/lexical.py` functions for them, `iba/app/lib/versereadinggenerate.py`, `iba/app/lib/stage1coverage.py`, `iba/app/ps/RelationalReading.ps1`, `Run-Stage1Batch.ps1`, `VerseReading.ps1`, their two batch settings, and the passage method (B12). Kept: `lexical.llm_*`, read by the surface-map code. | F12, E1 |
| 11 | Generated role guide, and the Workflow file archived | F13 |

Use check for unit 10 (E1): `reading.py` and `versecollate.py` do not import the Stage 1 code; its only other importers are `charreadinggenerate.py`, `charanswergenerate.py` and `subgroupgenerate.py`, whose steps are already inactive. The claims cycle is not designed, so the Stage 1 code would be retired with it and can be rebuilt from git if the claims design needs it. This is a judgement for you to confirm.

## 5. Decisions needed

1. Unit 10: retire the Stage 1 route and the passage method as above.
2. Whether verse text, passage, T-codes and renderings reach Observe (unit 5, B4) or only the claims read, given your ruling that the verse-level read in context belongs in the claims read process.
3. Go-ahead to run the units in the order above.
