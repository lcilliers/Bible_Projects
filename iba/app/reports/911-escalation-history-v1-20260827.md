# Escalation deep history

## #911 — Session log has no content-spec in config
type=issue source=researcher

**v1** (2026-08-27T04:38:57Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Session log has no content-spec in config
> **comment (set this version):** Researcher, verbatim: you can proceed with a session log - I notice that you check back to the previous logs instead of validating that what is in configs and governance everytime you do a session log. I guess at some point this is going to catch you out, because you are not following governance protocol. Checked live before writing anything, not assumed: cfg_setting has exactly 2 rows touching session logs -- governance.session_log_dir (Logs/) and governance.session_log_triggers_commit (the commit-and-push consequence). No cfg_step generates one, no cfg_enum/naming-pattern row constrains its filename beyond the SESSION-LOG-*.md convention named in that one setting text, and no cfg_* row or governance/CLAUDE.md prose specifies REQUIRED CONTENT at all -- confirmed by full grep of GOVERNANCE.md and CLAUDE.md, only the two settings above exist. This matches governance.past_precedent_investigation_signals_missing_config exactly: needing to check old logs for format/content is itself the signal the config is missing, not a puzzle to solve from precedent. Per that rule the instruction should stop here for the gap to be closed first -- but proceeding on direct instruction this turn, judgement-based content this one time, with this gap surfaced rather than silently repeated.
> **context (set this version):** governance.rules_must_be_config_driven also applies: any process rule (what a session log must contain) existing only as an unstated convention, backed by no cfg_* row, is itself a deviation requiring escalation -- which this is.

**v2** (2026-08-27T04:42:21Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** proceed to capture the instructions for a session log, including hithub actions into governance
