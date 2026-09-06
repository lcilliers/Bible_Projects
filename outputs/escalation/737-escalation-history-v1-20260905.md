# Escalation deep history

## #737 — IBA Debate-Pipeline to research_db Migration (Gated)
type=task source=researcher

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** IBA Debate-Pipeline to research_db Migration (Gated)
> **comment (set this version):** Move the debate work currently in IBA (passage/phenomenon/operation/hib tables) to research_db -- it's part of findings (governance.scope_research_db), not process-control/base data (governance.scope_iba_db). GATED: do not start until the IBA design audit is complete.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** Carried over from escalations_old #654 -- was on-hold, hold until work on the analytic phase is restarted. Reference: Workflow/Chat_responses/Additional configs

**v2** (2026-08-21T12:26:43Z, Researcher) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** on hold until analysis phase start

**v3** (2026-08-21T12:36:06Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Re-applying after fixing #762 -- this is what the original -State on-hold call should have produced.

**v4** (2026-08-21T15:29:04Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** from_id set to -1 (checked, no discoverable spawn parent -- escalation #767 v3's full audit; sentinel decided by researcher, escalation #773 v2).

**v5** (2026-09-05T16:25:20Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  this now becomes the main focus of attention, this is window 2 previously through through, and will use the new clusters as input. Review the previous method s associated with this, align it with the window 2 thinking, and do a deep dive to cleanout and prepare old analysis findings. do not close this escalation, keep it in progress, and let us first thorough plan it. 
> **context (set this version):**   

**v6** (2026-09-05T16:34:58Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Checked: still gated (GATED: do not start until the IBA design audit is complete) and no evidence that audit has completed. Nothing actionable for me while blocked -- was incorrectly sitting as next_action=review assigned to Claude with no actual review possible. Moved to state=on-hold and reassigned to you, since deciding when the gate opens (IBA design audit complete / analysis phase restarted) is your call, not mine.

**v7** (2026-09-05T16:37:06Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Correction to my prior comment (v6): the gate's own 'IBA design audit' is NOT stalled -- it is actively underway, this session, as the Window 1 lexical/cluster work (verse-lexical CRUD redesign, #1006 cluster-subgroup review, the M01-M47 family-grouping reallocation just completed, BUILD.md #235/#236). Researcher's own framing: Window 2 (passage/phenomenon/operation/hib -- the tables this item wants moved to research_db) IS the inner-being analysis process itself, so its research_db migration is naturally gated on Window 1's own audit/rebuild landing first, which is what's in flight now. Still correctly GATED -- the migration itself has not started and nothing here changes that -- but 'no evidence the audit has completed' was wrong to imply idle; it's live, just not finished.

**v8** (2026-09-05T16:39:07Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** My mistake -- I read this item's top-level context/gate note and my own prior comments, but missed your own reopening instruction further down the comment trail (Window 2 becomes main focus, using the new M-cluster taxonomy as input; review previous Window 2 methods, align with the corrected window-2 thinking, deep-dive cleanout of old analysis findings; keep in progress, plan thoroughly first, do not close). Reassigning back to Claude, in-progress, per your own instruction -- not on-hold.
