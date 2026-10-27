# Escalation deep history

## #2310 — 0.GAP pre: drop document reading, subgroup hook
type=task source=researcher

**v1** (2026-10-26T18:18:30Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **short description (set this version):** 0.GAP pre: drop document reading, subgroup hook
> **comment (set this version):** Researcher, chat 2026-10-26: 0.GAP pre no longer needs to read documents; what remains is the pull of the observations and the open items; check whether the open items have logical hooks into the verses and subgroups. Findings and decision in the file named in the context.
> **context (set this version):** iba/app/lib/reading.py; iba/app/lib/escalation.py; cfg_setting reading.gap_types

**v2** (2026-10-26T18:18:43Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Decision sought on outputs/escalation/2310-gap-pre-open-item-hooks-v1-20261026.md section 4: (1) retire the document read from 0.GAP pre (gap type read_in_files_only inactive, RO4 reworded); (2) open items and subgroups: A leave the pull as it is, B (recommended) show on each gathered open item the subgroup it reaches via cluster, Strong's and surface_subgroup, C add a subgroup field to items; (3) the 9 open items without verses: leave or give verse scopes. Finding: all 296 scope items hook to verses (3,594 links), 202 of 204 worded items reach a subgroup by join, none names one. Nothing built.

**v3** (2026-10-26T18:27:12Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2310-gap-pre-open-item-hooks-v1-20261026.md; outputs/escalation/2310-nine-open-items-without-verses-v1-20261026.md; iba/app/lib/reading.py; iba/app/migration/gap_pre_2310_v1_20261026.py; iba/app/tools/temp_2310_gap_pre_test_run.py; iba/app/BUILD.md section 422; iba/app/USER-GUIDE.md
> **resolution (set this version):** Approval sought for the finished build (4.1 and 4.2 as you decided): gap type read_in_files_only retired (cfg_enum inactive, out of reading.gap_types, detector removed from iba/app/lib/reading.py); each open_item in the pre-gap JSON now carries its subgroups through surface_subgroup; which items are pulled is unchanged. Tested on a copy, 11 of 11 cases pass (dry run, apply, second run refused, config agreement, 204 real items of which 202 reach a subgroup and the other two are on T clusters, synthetic no-term and unknown-strong cases give none); applied live (run DEVMODE-2310-GAP-PRE-20261026, 3 cfg writes in cfg_change_detail). Not run: Reading.ps1 -Action Open end to end on the new code. 4.3: the 9 items are listed in outputs/escalation/2310-nine-open-items-without-verses-v1-20261026.md; all files the six cluster items name are captured; nothing settled. Approve to close #2310, or name what to change.

**v4** (2026-10-27T05:10:47Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-10-26 (verbatim): "we can update 0.GAP pre as it no longer required to read documents in the gap work. what is remaining is the pull of the observations and the open items.  What you can do is to see if the open items have logical hooks into the verses and sub clusters to allow them to be pulled into the gap work."
Researcher, chat 2026-10-26 (verbatim): "4.3: surface the 9 open items for cluster work so I can inspect them.  4.1 approve; 4.2 option B"
Researcher, chat 2026-10-26 (verbatim): "it looks like 6 of the 9 items can be closed as the observations have been captured and the other 3 is moot as it is not open items.  It seems that you create an open item for a issue and task cluster, which serves no purpose."
Claude: the six were closed and the three withdrawn on the thread items; the cause of the third point is on #2311.

**v5** (2026-10-27T08:55:57Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted
