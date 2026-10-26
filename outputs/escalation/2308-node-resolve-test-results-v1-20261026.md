# #2308 Node-Resolve: test plan and results (v1)

**Date:** 2026-10-26 · **Escalation:** #2308 · **Tool:** `iba/app/ps/Node-Resolve.ps1` (rules NR-01 to NR-06) · **Rule:** B:46, the results are shown here and cited in the escalation.

Cases run on a copy of the database as it stood before the sweep (20,800 nodes needing work), except T8, which ran on the live database and refused without writing.

| # | Case | Result |
|---|---|---|
| T1 | Plan on the before-copy | 20,572 nodes to fill: 16,295 occurrence ids and 15,529 subgroup codes; 20,800 examined; left: 3,392 no subgroup defined for the strong in the cluster, 32 occurrences disagree on the subgroup |
| T2 | Apply the whole plan | 20,572 written, 0 stale (the live run gave the same numbers) |
| T3 | A node changed between Plan and Apply | 20,571 applied, 1 skipped as stale, and the changed node kept its own value |
| T4 | Never overwrite (NR-05): every existing value, surface and cluster before against after | 0 nodes changed |
| T5 | The occurrence belongs to the node's own strong and verse | 0 nodes where it does not |
| T6 | A subgroup written equals the surface_subgroup row of its occurrence; surfaces mapped to two subgroups | 0 duplicate (cluster, strong, surface) keys in surface_subgroup. 5 of the sampled nodes differ from the table: they are older character-stage nodes (M67, G3636 "trouble", node ids 769, 771, 1044, 1067, 1116) that already carried a different subgroup, `M67_B_dereliction_of_duty` against the table's `M67_not_this_sense`; the sweep left them as they were |
| T7 | A second Plan after Apply | 0 to fill (only the deliberately stale node remained on the copy); 0 on the live database |
| T8 | Refusals, live: `-Step Apply` with no file, and with a capture JSON that is not a plan | each refused with its reason, nothing written |

**Found, for the researcher:** the 5 character-stage nodes in T6 disagree with the cluster's subgroup table; they were not
changed (NR-05) and are listed here for the cleanup decision on #2308.
