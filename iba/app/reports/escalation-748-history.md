# Escalation deep history

## #748 — Escalation #735 Orphan-Config Follow-Up
type=task source=claude related_activity=escalation-redesign-followups-20260820 from_id=

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Escalation #735 Orphan-Config Follow-Up
> **comment (set this version):** The 2 orphan-config findings from escalation #735 (raised during live verification of the redesign, 2026-08-20) were never resolved. Re-run configmaint.validate under the live new system to raise a fresh, properly-tracked replacement.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** #735 is now frozen, unanswered, in escalations_old -- the v2 cutover only carried over the 4 items named explicitly (#650/#654/#668/#725), not #735.
> **related activity (set this version):** escalation-redesign-followups-20260820

**v2** (2026-08-21T12:44:26Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** proceed to check if this is still relevant, if so then fix.  also, if there is a another escalation it refers to, then complete the related columns

**v3** (2026-08-21T13:20:51Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Checked (per your instruction): still relevant -- the 2 orphan-config findings are confirmed live today (direct query, not the dispatcher). Re-running configmaint.validate as instructed is currently BLOCKED by module_blocking on TWO open items sharing source='configmaint': #756 and #760 (both pushed to ready_for_approval/you, with ordering notes on each -- #756 first, #760 second). Once both clear, re-running validate either finds 0 orphans (if the 2 remaining ones get fixed as part of #760's resolution) or raises a fresh escalation for the same 2 -- will complete this item for real once unblocked, not before.
