# Escalation deep history

## #925 — the proposed change fails a coherence check — never escalat…
type=config source=configmaint

**v1** (2026-08-27T08:35:04Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** the proposed change fails a coherence check — never escalat…
> **comment (set this version):** hard error (report-stop) — recorded for visibility; answering this does not resume the run, which is already terminal
> **context (set this version):** {"full_message": "the proposed change fails a coherence check \u2014 never escalated \u2014 1 problem(s): cfg_setting.value \"A session log (Logs/SESSION-LOG-*.md) must, at minimum, carry: (1) date and a one-line scope summary of the session; (2) every escalation touched, by id, with its outcome (raised/updated/resolved/rejected) -- not narrative paraphrase, the actual ids; (3) every file or deliverable created or changed, with its path; (4) decisions made, distinguishing which were the researcher's own decision vs a self_correctable fix Claude made and closed directly; (5) open items carried into the next session -- what is left, and for whom; (6) confirmation of the git state this log's own completion triggers (governance.session_log_triggers_commit): branch, commit hash, and that the push succeeded -- not asserted, the actual git status/log output. A log missing any of these is incomplete, not merely terse.\" is not valid JSON \u2014 cfg.setting() always json.loads()s it on read; a plain string must be quoted (e.g. '\"my string\"'), matching every other cfg_setting.value"}
> **tried (set this version):** hard error (report-stop) — recorded for visibility; answering this does not resume the run, which is already terminal
