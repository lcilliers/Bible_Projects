# Escalation deep history

## #736 — Main-Project / IBA Filing Consolidation
type=task source=researcher

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Main-Project / IBA Filing Consolidation
> **comment (set this version):** Think through filing between main project and IBA -- phase-related work filed together, not split across branches; topic reports must not dump into the general one-off folder. Also resolves the deferred governance.oneoff_report_dir CSV row.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** Carried over from escalations_old #650 at the 2026-08-19 redesign cutover -- was on-hold, dependent on a deeper review of the statement of affairs. Reference: outputs/markdown/iba-table-review-response-v1-20260816.md

**v2** (2026-08-21T12:25:33Z, Researcher) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** on hold until escalation usage has stabilised

**v3** (2026-08-21T15:29:04Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** from_id set to -1 (checked, no discoverable spawn parent -- escalation #767 v3's full audit; sentinel decided by researcher, escalation #773 v2).

**v4** (2026-08-26T15:17:11Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Findings from #863 (raised this session, now closed as supersede into this item) added for when this comes off hold. #863's own trace: iba/app/reports/file-versioning-config-trace-20260826.md -- two narrow config mechanisms exist (report.version_on_regenerate, governance.oneoff_*), neither general-purpose, project-wide file naming/versioning/archiving has ZERO cfg_* representation. #863's scope plan: iba/docs/file-naming-and-location-governance-plan-v1-20260826.md -- splits docs/file-organisation-rules.md into (a) general timeless naming/versioning/archiving principles (proposed for adoption: new filing cfg_behaviour_class, real cfg_behaviour_rule rows, a shared utility generalising oneoff_path() project-wide, a configmaint.validate check for hand-imitated naming) vs (b) artefact-specific patterns tied to a superseded methodology (NOT proposed for adoption as live rules -- encoding dead patterns as governance). Researcher's own framing this round, verbatim: 'filing is in a real mess... all I want is that it is properly done and I can find things when I look for it' -- also flagged: a bulk historical-mess cleanup is a separate, later item from getting the RULE itself config-driven going forward. When this item comes off hold, both the plan's (a) adoption AND the explicitly-deferred (b)/location-table/cleanup items are the outstanding work, not just (a).

**v5** (2026-08-27T14:56:25Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Proceed, this item relates to 929 and the current session  -Context 
