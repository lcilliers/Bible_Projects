# Escalation deep history

## #2516 — Session-close check that keeps the project map current
type=task source=researcher

**v1** (2026-11-20T14:19:53Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Session-close check that keeps the project map current
> **comment (set this version):** Researcher, 2026-11-20, verbatim: '2515 Q26.  This seems like a outstanding task for you. complete this task and close Q26'. Question 26 of #2515: the session-close check that keeps the project map current (the researcher's decision D3 on #2510, 2026-11-19: 'yes, the map is your guide, and keeping the map up to date is part of session close') is not built. Checked first (B:123, B:1): cfg_control_home has no row for the project map, so the map has no recorded home; the map exists only as outputs/escalation/2510-project-map-v2-20261119.md, a deliverable of #2510 (now completed); no code or setting under iba/app names it. Building it changes config and code (a new control-home row, session_close.* settings, a detection in the session-close check, USER-GUIDE, GOVERNANCE, BUILD), which is app development: B:105 requires the design to be approved first, and the build runs in developer mode (configmaint.propose gate).
> **context (set this version):** outputs/escalation/2510-project-map-v2-20261119.md, outputs/escalation/2510-open-questions-v1-20261120.md

**v2** (2026-11-20T14:20:16Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Approval sought: the design below, so that the check can be built in developer mode (a separate session, started with /developer-mode). Nothing is built or changed yet. Decision D3 (keep the map current as part of session close) is already the researcher's; what is put for approval is the HOW, in three parts.

1. Home of the map. Today none is recorded and the map sits in an escalation deliverable folder, tied to #2510's prefix. Option A (recommended): move it to iba/docs/project-map.md (the engineering-note folder, rule 60) and add a cfg_control_home row, kind project_map, read_when session_start, history_home git history of that file. Option B: leave it at outputs/escalation/2510-project-map-v2-20261119.md and record that path as the home (risk: the file is archived with the escalation's deliverables). Option C: hold the map in bible_research.db prose; it covers the app as well as the programme, so it does not fit the prose book. The researcher's rule that only database results are the project result stands: the map is a working guide, not a result.

2. What the check does. A new session-close detection (next free SC number) reads the map file's header line 'Current as of: <date> <commit>' and, for the session's git window, looks for change signals in what the map describes: a row added, changed or retired in cfg_control_home; a governance.* setting changed (programme stages, study status, narrative home); a table added to cfg_table; the stages or layers settings changed (cfg_setting layer.reading); an escalation of type task completed that BUILD.md names as a new mechanism. If any signal fired and the map file did not change in the window, the check reports a finding per signal, and each needs a disposition in the session's compliance file under the existing close-disposition lines: 'map updated' (and the header moved), or 'no change needed: <reason>'. The signal list is a cfg_setting (session_close.map_signals), not code. Limit stated: the check detects that something the map describes changed and was not reflected; it cannot judge that the map's text is right. That stays Claude's disposition reason and the researcher's spot-check.

3. Where it is built. Code: the session-close detection module beside the other SC checks; config: session_close.map_home, session_close.map_signals, the control-home row, the finding's wording; docs: the SC table in iba/app/USER-GUIDE.md, iba/app/GOVERNANCE.md (the mechanism), iba/app/BUILD.md. Tested on a copy first, with a session that changes a signal and one that does not.

Not decided here and left to the researcher: whether session-close should also refuse to commit on this finding (as it does for the other detections) or only report it. Recommendation: block, like the others, since D3 makes upkeep part of close.

**v3** (2026-11-20T18:38:52Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**   approved
