# Escalation deep history

## #2188 — Move the 8 live instruction files into config
type=task source=researcher

**v1** (2026-10-21T05:35:14Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Move the 8 live instruction files into config
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): '2182:  §2 8 files kept - create escalation to transfer these instructions into the configs and rules and consolidate it, especially the narrative rules.  §4 all 27 tasks are superceded or retired. task list is now fully controlled by escalations. close and archive the tasks.  §5 permissions:  create escalation to resolve these - I need more information before decision.  §6 retire and archive all these items.   2182 then approved.     2183: approved , 2184 approved, 2185  approved, 2186 approved, proceed with 2187' -- item §2. The 8 Workflow/Instructions files kept by #2182 (style guide v2, verse-reading-by-role guide v2, verse-analysis method v1, operational governance v1_0, WA passage-read guidance v1.5, WA interpretation questions v1.4, WA inner-being narrative guidance v1, WA narrative hard constraints v1): their instructions transferred into cfg rules and consolidated, especially the narrative rules. Element of #2177.
> **context (set this version):** #2177; #2182; outputs/escalation/2182-stale-root-controls-retired-v1-20261021.md

**v2** (2026-10-21T05:48:25Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **comment (set this version):** Queued, not started (2026-10-21; researcher asked for a session-close first). Also in scope, found during #2182 sec 6: iba/config/DBSchema/ and iba/config/utility/DBSchema_maintenance.json + step.json are live config held outside cfg_* (read by iba/scripts/build_dbschema.py and iba/scripts/probe_step_api.py) -- the same 'instructions into config' question as the 8 files. Files kept: Workflow/Instructions/{wa-inner-being-narrative-style-guide-v2-20261001, wa-verse-reading-by-role-guide-v2-20261019, wa-verse-analysis-method-v1-20260702, wa-operational-governance-v1_0-20260614, WA-passage-read-guidance-v1.5-2026-08-02, WA-interpretation-questions-v1.4-2026-08-02, WA-inner-being-narrative-guidance-v1-2026-07-28, WA-inner-being-narrative-hard-constraints-v1-2026-07-30}.md; the four WA-* are read by narrative/passage-debate code through method.* settings.

**v3** (2026-10-21T09:09:50Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): 'proceed with developer-mode.  the base escalation is 2177. start with 2195, then 2188,2191,2192, and 2193.' Scope measured read-only and the approach proposed, with decisions, in outputs/escalation/2177-reset-backlog-plan-v1-20261021.md; no build until the researcher approves the approach (rule 105).
> **context (set this version):** outputs/escalation/2177-reset-backlog-plan-v1-20261021.md; #2177

**v4** (2026-10-21T09:11:20Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Approval sought for the approach in outputs/escalation/2177-reset-backlog-plan-v1-20261021.md sec 1: step 1 is a mapping only (each instruction in the 8 files and the iba/config JSON -> existing cfg row / new rule / history / #2190), narrative files first, no cfg write until the mapping is approved. Decisions: 1A the four files code reads stay as files with only their conduct rules moved to cfg (recommended) or become cfg rows read by code; 1B go ahead while the study is on hold, study content untouched (recommended) or park with the study. Interim approval: Claude then builds the mapping.

**v5** (2026-10-21T09:43:32Z, Researcher) state=on-hold next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): '2188 - pause this work until the study is restarted and the narration can be aligned between the rules.' Parked with the study (governance.study_status); nothing built.

**v6** (2026-10-21T14:06:34Z, Claude) state=on-hold next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** For the restart: under #2201 item 5 the book-narrative stage was retired, with its 10 narrative/method settings (method.inner_being_narrative_guidance_path and method.narrative_hard_constraints_path among them) and the narrative_required_channel enum now inactive. Code: iba/app/lib/archive/narrativegenerate.py, iba/app/handlers/archive/narrative.py. When the study restarts, the narrative alignment starts from those archived rows and files (BUILD.md sec 370).

**v7** (2026-10-24T03:19:28Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** proceed with mapping
