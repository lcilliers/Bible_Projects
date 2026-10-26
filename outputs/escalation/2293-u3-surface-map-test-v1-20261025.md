# #2293 test record: #2286 U3, the surface mapping steps

Date: 2026-10-25. Developer Mode session 3646374f.
- **Test script:** `iba/app/tools/temp_2293_surface_map_test_run.py`, run with `--live`.
- **Design:** `outputs/escalation/2293-surface-map-design-v1-20261025.md`, test plan in section 5.
- **Setup:** a backup-API copy of iba.db with the migration applied; the output folder and the API usage log redirected to scratch.

The groups and allocations are synthetic. They test the mechanics, not a mapping: the real mapping is the pilot, #2298.

**Result: 30 of 30 pass.** T0 is the migration; T1 to T9 are design cases 1 to 9.

| case | what | result | evidence |
|---|---|---|---|
| T0 | migration on the copy, and a second run writes nothing | PASS | ['28 write(s) applied (run DEVMODE-2293-SURFACE-MAP-STEPS-20261025, logged to cfg_change_detail)', '0 write(s) applied (run DEVMODE-2293-SURFACE-MAP-STEPS-20261025, logged to cfg_change_detail)'] |
| T1a | Pairs M18: every pair once; pairs and hits equal a direct query | PASS | ok pairs 454 vs 454, hits 1510 vs 1510 |
| T1b | Pairs M18: head is the pairs up to 80% of the hits (163 expected from the design) | PASS | head 163, cut 163 |
| T1c | Pairs M18 twice on a day: the second file is -v2, the first archived | PASS | C:\Users\lerouxc\AppData\Local\Temp\claude\C--Bible-study-projects\3646374f-685b-404e-b3c9-7ec0c57b899f\scratchpad\t2293\out\m18-pairs-20261025-v2.json |
| T2 | Pairs M67: 24 inherited pairs pre-filled with their subgroup, 20 blank | PASS | inherited 24, prefilled 24, blank 20 |
| T3a | Apply refuses a head pair with no group, nothing written | PASS | 1 problem(s), nothing written:   head pair H2896A 'good': no group |
| T3b | Apply refuses a new group with no kind, nothing written | PASS | 1 problem(s), nothing written:   group M18_t2: kind None is not one of ['group', 'not_this_sense', 'qualifier'] |
| T3c | Apply refuses a new group of kind anomaly (made only by the step), nothing written | PASS | 1 problem(s), nothing written:   group M18_t2: kind 'anomaly' is not one of ['group', 'not_this_sense', 'qualifier'] |
| T3d | Apply refuses a pair not in the cluster, nothing written | PASS | 1 problem(s), nothing written:   pair H0001 'father': not a pair of M18 |
| T3e | Apply refuses a blank reason, nothing written | PASS | 1 problem(s), nothing written:   pair H2896A 'good': no reason |
| T3f | Apply refuses a new code not <cluster>_<slug>, nothing written | PASS | 82 problem(s), nothing written:   group X_bad: a new code is <cluster>_<slug> (letters, digits, underscores)   pair H2896A 'better': group 'M18_t2' is not a group of M18   pair G2309 'want': group 'M18_t2' is not a group of M18   pair H3368 'precious': group 'M18_t2' is not a group of M18   pair H26 |
| T3g | Apply refuses a file for another cluster, nothing written | PASS | 1 problem(s), nothing written:   the file is for 'M19', not M18 |
| T3h | Apply refuses an inherited pair moved without a 'correction:' reason | PASS | 9 problem(s), nothing written:   pair G4710 'earnestness': moved from its inherited subgroup M67_C_earnest_diligence without a 'correction:' reason (#2286 B5: an inherited pair moves only where its data is in error)   head pair H5647I 'work': no group   head pair H5647I 'labor': no group   head pair |
| T3i | Apply refuses a missing -File | PASS | -File is required and must exist: '.' |
| T4a | Apply M18: 2 groups added with their kinds, 163 head pairs as session, one anomaly group | PASS | ('M18: 2 group(s) added; pairs 163 inserted, 0 updated, 0 unchanged. Next: -Step Tail (a preview), then -Step Check.', [('session', 163)], 1, {'M18_t1': 'group', 'M18_t2': 'qualifier', 'M18_anomaly': 'anomaly'}) |
| T4b | Apply the same file again: nothing changes, still one anomaly group | PASS | M18: 0 group(s) added; pairs 0 inserted, 0 updated, 163 unchanged. Next: -Step Tail (a preview), then -Step Check. |
| T4c | Apply M19: its empty-surface pair (G4100) goes to the anomaly group | PASS | ('M19: 2 group(s) added; pairs 27 inserted, 0 updated, 0 unchanged. Next: -Step Tail (a preview), then -Step Check.', [('G4100', 'anomaly', 'empty surface in verse_lexical: cleared by hand (#2286 C4)')]) |
| T5 | Apply M67: 23 inherited, the corrected pair and the missing head pairs as session; old subgroups unchanged | PASS | ('M67: 0 group(s) added; pairs 32 inserted, 0 updated, 0 unchanged. Next: -Step Tail (a preview), then -Step Check.', {'inherited': 23, 'session': 9}, 8, [('session', 'correction: test move of an inherited pair')]) |
| T6a | Tail preview M67: no call, the pairs and the cost shown, nothing written | PASS | PREVIEW M67: 12 tail pair(s), about 1675 input tokens, at most 16000 output tokens, estimated $0.2450 on claude-sonnet-5. No call made, nothing written. Re-run with -Live to allocate. |
| T6b | Tail refuses a cluster over the cost cap | PASS | M67: 12 tail pair(s), about 1675 input tokens, at most 16000 output tokens, estimated $0.2450 on claude-sonnet-5: over lexical.llm_max_cost_per_batch ($0.00) |
| T6c | Tail refuses a cluster whose head is not yet allocated in session (M83 before Apply, B1) | PASS | M83: 21 head pair(s) not yet allocated (the head is allocated in session, B1): fill them in the pairs file and run -Step Apply first |
| T6d | Tail refuses a cluster with no groups yet (M20) | PASS | M20 has no groups yet: run -Step Pairs, fill the groups and the head, then -Step Apply |
| T7a | a reply with not JSON is refused, nothing written | PASS | the reply is not JSON with an 'allocations' list: Expecting value: line 1 column 1 (char 0); first 300 chars: 'sorry' |
| T7b | a reply with a pair missing is refused, nothing written | PASS | 12 problem(s) in the reply, nothing written:   ('H5647I', 'committed'): missing   ('H5647I', 'dress'): missing   ('H5647I', 'labored'): missing   ('H5647I', 'laborer'): missing   ('H5647I', 'made'): m |
| T7c | a reply with an unknown group is refused, nothing written | PASS | 24 problem(s) in the reply, nothing written:   ('H5647I', 'committed'): group 'NOPE' unknown   ('H5647I', 'dress'): group 'NOPE' unknown   ('H5647I', 'labored'): group 'NOPE' unknown   ('H5647I', 'lab |
| T7d | Tail live M67: every tail pair placed once, as api, each with a reason; usage logged | PASS | ('M67: 12 tail pair(s) allocated by the API (0 to the anomaly group); 12 inserted, 0 updated; cost $0.0232 (2559 in, 1033 out). Next: -Step Check.', 0, (12, 0)) |
| T8a | Check M67: report written; shares add to 100% once all pairs are placed; unallocated 0 after Tail | PASS | ('-> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/3646374f-685b-404e-b3c9-7ec0c57b899f/scratchpad/t2293/out/m67-check-20261025.md\n  M67: 5 group(s); 0 pair(s) unallocated; 0 in the anomaly group; 0 two-sense; over 30%: M67_C_earnest_diligence', 1.0) |
| T8b | Check M18: a group of kind group over 30% is flagged; a qualifier group is never flagged | PASS | ([('M18_t1', 0.4596, True), ('M18_t2', 0.3411, False), ('M18_anomaly', 0.0, False)], '-> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/3646374f-685b-404e-b3c9-7ec0c57b899f/scratchpad/t2293/out/m18-check-20261025.md\n  M18: 3 group(s); 291 pair(s) unallocated; 0 in the anomaly group; 0 two-sense; over 30%: M18_t1') |
| T9a | Registry: four steps with handlers, grants for Apply and Tail, the work package's PS script | PASS | ([('cluster.surface_pairs', 'iba.app.handlers.surfacemap:pairs'), ('cluster.surface_apply', 'iba.app.handlers.surfacemap:apply'), ('cluster.surface_tail', 'iba.app.handlers.surfacemap:tail'), ('cluster.surface_check', 'iba.app.handlers.surfacemap:check')], [('cluster.surface_apply', 'cluster_subgroup'), ('cluster.surface_apply', 'surface_subgroup'), ('cluster.surface_tail', 'cluster_subgroup'), ('cluster.surface_tail', 'surface_subgroup')]) |
| T9b | Validate checks on the copy: no new finding except B:117 and B:118 now partially_enforced; no cluster.surface_map setting unread | PASS | ({'scope_gaps': [], 'unenforced': ['[study_method] #117 subgroups-are-surface-groups — partially_enforced', '[study_method] #118 surface-mapping-conditions — partially_enforced'], 'hedge': [], 'orphan': [], 'grant_writers': [], 'no_ps': [], 'bypass': [], 'unclassified': []}, ['[study_method] #117 subgroups-are-surface-groups — partially_enforced', '[study_method] #118 surface-mapping-conditions — partially_enforced'], []) |

## The live API call (T7d)

M67's tail went to the API in one call: 12 pairs on `claude-sonnet-5`, 2,559 tokens in and 1,033 out, $0.0232. The preview estimated $0.2450, because it prices the full output ceiling.

Every pair was placed once, with a reason, and none went to the anomaly group.

**Quality *(inferential)*:** M67 had only its four inherited groups (idleness, dereliction, diligence, administrative thoroughness). The API put plain labour renderings of H5647I ("dress", "plowed", "laborer", "labored", "worked", "performed") in *dispositional idleness*. Those uses read as labour, on the diligence side, or outside the cluster's sense. It did not use the anomaly group. This is recorded on #2298: in the pilot, M67 is given a `not_this_sense` group and its tail placements are judged.

## Live

- **Snapshot first:** `iba/app/db/snapshots/iba-20261025T204602Z-pre-2293-surface-map-steps.db`.
- **Applied:** 28 writes; a re-run gives 0.
- **Through `Surface-Map.ps1` on live** (read-only steps):
  - Pairs M67 wrote `outputs/surface-map/m67-pairs-20261025.json`: 44 pairs, 30 head, 14 tail, 24 inherited.
  - Check M67 wrote its report.
  - Tail M67 refused: 30 head pairs unplaced.
  - The point-of-use hook delivered B:117 and B:118 at the script's first use.
- **Worksheet:** the `Surface-Map` tab shows no drift.
- **Validate:** `Config-Maintenance.ps1 -Step Validate` (RUN-20261025_204825_291) is ok. Unread settings are down to #2268's 2. B:117 and B:118 are listed as `partially_enforced`.
