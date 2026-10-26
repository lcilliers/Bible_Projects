# #2294 test record: #2286 U4, stale and unallocated pairs and the reading gate

Date: 2026-10-25. Developer Mode session 3646374f.
- **Decision:** G-a (#2294 v4): the gate applies as worded.
- **Test script:** `iba/app/tools/temp_2294_reading_gate_test_run.py`.
- **Setup:** a backup-API copy with the migration applied, all outputs redirected to scratch, no API call.

The mappings are synthetic: they test the gate, not a mapping.

**Result: 12 of 12 pass.**

| case | what | result | evidence |
|---|---|---|---|
| G1 | migration on the copy, and a second run writes nothing | PASS | ['4 write(s) applied (run DEVMODE-2294-READING-GATE-20261025, logged to cfg_change_detail)', '0 write(s) applied (run DEVMODE-2294-READING-GATE-20261025, logged to cfg_change_detail)'] |
| G2 | overview: 80 M clusters, none allocated, none stale, in seconds (B:71) | PASS | 80 clusters, 0.44 s |
| G3 | reading.open refuses an unmapped M home cluster (M18), naming the counts and the next step | PASS | -Home M18: 454 unallocated and 0 stale (code, surface) pair(s). A cluster with unallocated or stale pairs is not read until they are (behaviour rule surface-mapping-conditions). Map it first: iba\app\ps\Surface-Map.ps1 -Step Pairs -Cluster M18, then Apply, Tail and Check. |
| G4 | the gate passes a T home cluster (rule is for M clusters) | PASS |  |
| G5 | M18 with only its head allocated: still refused (tail unallocated); overview shows it partly mapped | PASS | ('M18: 0 stale pair(s) retired; 1 group(s) added; pairs 163 inserted, 0 updated, 0 unchanged. Next: -Step Tail (a preview), then -Step Check.', '-Home M18: 291 unallocated and 0 stale (code, surface) pair(s). A cluster with unallocated or stale pairs is not read until they are (behaviour rule surface-mapping-conditions). Map it first: iba\\app\\', {'cluster': 'M18', 'pairs': 454, 'allocated': 163, 'unallocated': 291, 'stale': 0}) |
| G6 | M67 fully allocated: the gate passes and the reading opens | PASS | ('M67: 0 stale pair(s) retired; 0 group(s) added; pairs 44 inserted, 0 updated, 0 unchanged. Next: -Step Tail (a preview), then -Step Check.', 'ok', 'reading t-gate-m67 opened (#2294, home M67): 1 verse(s); pre-gaps term_cluster 0, meaning_missing 0, base_missing 0, term_reading_missing 0, read_in_files_only 0, face_not_gathered 0, open_item 0\n  -> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/3646374f-685b-404e-b3c9-7ec0c57b') |
| G7 | cluster.validate: M18 partly mapped is a finding (escalates), with the mapping in its report | PASS | Cluster-assignment findings: 0 `strong` row(s) have NO cluster assignment at all; 4455 strong(s) carry a non-T2 cluster with no word_registry link at all; 2786 `backfill` strong(s) have an already-active or already-clustered sibling; 0 surface pair(s) are stale and 1 M cluster(s) are partly mapped ( |
| G8 | a code leaving M67 (G0691) makes its 1 pair(s) stale and the gate refuses | PASS | (1, '-Home M67: 0 unallocated and 1 stale (code, surface) pair(s). A cluster with unallocated or stale pairs is not read until they are (behaviour rule surface-mapping-conditions). Map it first: iba\\app\\ps') |
| G9 | Check lists the stale pairs | PASS | -> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/3646374f-685b-404e-b3c9-7ec0c57b899f/scratchpad/t2294/out/m67-check-20261025.md   M67: 5 group(s); 0 pair(s) unallocated; 1 stale; |
| G10 | Apply retires the stale pairs (soft delete, reason kept), and the gate passes again | PASS | ('M67: 1 stale pair(s) retired; 0 group(s) added; pairs 0 inserted, 0 updated, 43 unchanged. Next: -Step Tail (a preview), then -Step Check.', (1, 1)) |
| G11 | a surface that no longer occurs is stale too, with its reason | PASS | [{'id': 164, 'cluster_code': 'M67', 'strong': 'H5647I', 'surface': 'zzz-no-such-surface', 'reason': 'test allocation', 'why': 'the surface no longer occurs for the code'}] |
| G12 | registry: the report section exists; validate checks on the copy show no new finding | PASS | ('## Surface mapping (#2294)', {'scope_gaps': [], 'hedge': [], 'orphan': [], 'grant_writers': [], 'no_ps': [], 'report_rows': []}) |

**Regression:** the U3 suite (`iba/app/tools/temp_2293_surface_map_test_run.py`) re-run after this change passes every mechanics case. Two cases are not failures of the change:
- T7d is the live API call, not repeated.
- T9b compares the copy against live, which now already holds U3's config, so it finds nothing new by design.

## Live

- **Snapshot first:** `iba/app/db/snapshots/iba-20261025T210410Z-pre-2294-reading-gate.db`.
- **Applied:** 4 writes; a re-run gives 0; the script is archived.
- **`Cluster-Assign.ps1 -Step Validate`** (RUN-20261025_210437_762) is ok:
  - 15,455 strongs checked;
  - the existing findings are within the baseline approved on #1707, so nothing was re-raised;
  - the report has the Surface mapping section.
- **`Reading.ps1 -Step Open -Home M64`** (RUN-20261025_210812_473) was refused: "165 unallocated and 0 stale (code, surface) pair(s)". No reading row was written.
- **`Config-Maintenance.ps1 -Step Validate`** (RUN-20261025_210834_947) is ok, with findings identical to #2270.
