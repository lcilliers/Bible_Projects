# Escalation deep history

## #786 — Programme Prose Chapter 4
type=task source=researcher

**v1** (2026-08-21T16:33:54Z, Researcher) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Programme Prose Chapter 4
> **comment (set this version):** This item will read the existing chapter 4 of the programme prose and compare it with the IBA and all its configurations and bring the prose chapter up to date

**v2** (2026-08-26T15:31:11Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **comment (set this version):** Before starting the chapter 4 rewrite, checked for an existing thread first (same discipline just applied to #863/#736) -- found #739 'Programme Prose Realignment (Ch. 4-6)', same scope (chapter 4, plus 5-6), already on-hold, your own words twice: 'on hold must be scheduled before analysis phase.' Not proceeding with content work until this is resolved: is #786 meant to override that hold (i.e. the analysis phase is now considered started/scheduled), or is this a duplicate that should merge into #739 the same way #863 merged into #736? Holding rather than guessing -- this is a real timing decision, not a mechanical one.

**v3** (2026-08-26T16:38:17Z, Researcher) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** reassigned for my attention

**v4** (2026-08-27T04:40:16Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** 739 and 786 can be done together

**v5** (2026-08-27T05:05:06Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Chapter 4 rewritten and applied live as part of the combined #739/#786 pass; see #739 for full detail and the pending config-approval run ids.
> **context (set this version):** Companion item: #739 (chapters 4-6 done together). Pending config approvals: RUN-20260827_060344_431-CONFIGMAINT (ch4), RUN-20260827_060402_125-CONFIGMAINT (ch5), RUN-20260827_060406_397-CONFIGMAINT (ch6) -- each pauses a cfg_prose_chapter.status update to 'reviewed'; answer via Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve|Reject|Revise|Hold|Noted, then re-run the same Config-Maintenance Propose command to commit.
> **resolution (set this version):** Chapter 4 specifically (this item's own scope): rewritten in full against live cfg_table/cfg_column facts in iba.db, not against BUILD.md/session-log precedent or the old chapter text. Full account of what changed and why is filed under escalation #739's resolution (raised together, per your instruction '739 and 786 can be done together') -- not restated here to avoid duplication/drift between the two records. Chapters 5 and 6 were also done in the same pass since #739 covers all of 4-6 and you said to do them together.

**v6** (2026-08-27T05:15:03Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** I approve that you have done something.  If the work is not correct, then I will raise another escalation
