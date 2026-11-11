# Escalation deep history

## #2460 — Engagement keeps no reason or test per verse
type=task source=researcher

**v1** (2026-11-10T17:51:31Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Engagement keeps no reason or test per verse
> **comment (set this version):** Found 2026-11-10 while the researcher inspected collection search (#2412), read live (ib_node, ib_observation, ib_observation_change for vl 1478344 and 1155718). Per verse the app stores one node (verse, surface, Strong code, morph, cluster, role, stage engagement) under an observation whose text is shared by all its verses; Claude reason for each verse is kept only in the assessment file (_analytics/surfaces/working_files/engagement/engagement-search-assessment-20261110.json) and in outputs/reports/engagement/engagement-search-observations-20261110.md, except confirm and reopen reasons (ib_observation_change). The test is stored once per observation (the most common one), so Rom 7:21 and Psa 17:3 (judged by inner_being_vocabulary) sit in an observation whose parts.test is idiom_or_combined_span. The observation strong is the first verse code (H4672 for a group that includes G2147). Also: the 209 confirm reasons written by the review have their first letter lowercased (ahab cannot find Elijah); history rows are append-only and untouched. Nothing is designed or built (B:105).
> **context (set this version):** outputs/reports/engagement/engagement-search-observations-20261110.md; iba/app/lib/engagement.py

**v2** (2026-11-10T17:51:35Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Decision: whether and how engagement should keep a reason and a test for each verse. A (recommended): keep each verse reason and test on its node or its change row, written by Record and Close from the assessment, with a Developer Mode build and a repair of collections already done. B: leave as is; reasons stay in the assessment files and reports. C: split observations by test so the one test is right, still no per-verse reason. Approval sought: choose A, B or C. Details: outputs/reports/engagement/engagement-search-observations-20261110.md

**v3** (2026-11-10T17:54:11Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, verbatim (2026-11-10): "the reasoning and recording of it in the md is helpful. but the recording in the observations are poor.  does this apply to the other 7 already completed also." Checked live against ib_node, ib_observation and the seven assessment files: (1) per-verse reason is stored in no observation table for any of the eight collections (5321 verse items with a live engagement node: aloud 172, call 833, deal 386, new 483, anger 713, godly 1742, choose 307, search 685, of which none keeps its reason on the node; the reasons exist only in each _analytics/surfaces/working_files/engagement assessment file, and confirm or reopen reasons in ib_observation_change). (2) The observation Strong code is the first verse code: it differs from the node code on 2797 of the 5321 nodes (aloud 133, call 382, deal 271, new 225, anger 395, godly 855, choose 165, search 371). (3) The one test per observation is wrong only in search: 52 of 685 items (the earlier seven were split by test, search was split by sense). Scope of option A therefore: all eight collections.

**v4** (2026-11-10T18:05:20Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Note (2026-11-10, after the researcher said the observations captured are far from right and the method is not settled): the storage decision A, B or C depends on what an observation must say, which is not settled (see #2412 v26). Recommend this decision waits for that.

**v5** (2026-11-11T11:12:54Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**   approved
