# Escalation deep history

## #787 — New cfg_setting 'prose.extractor_version' = '1.1' - the pro…
type=config source=configmaint related_activity=configmaint.propose from_id=

**v1** (2026-08-21T17:38:14Z, ?) state=raised next_action= assigned_to=Researcher
> **short description (set this version):** New cfg_setting 'prose.extractor_version' = '1.1' - the pro…
> **context (set this version):** {"table": "cfg_setting", "op": "insert", "where": {}, "set": {"value": "\"1.1\"", "use": "prosestore.extract's JSON meta.extractor_version -- escalation #648 compliance fix, was a module-level constant in build_programme_prose_extract.py", "module": "prose"}, "full_message": "New cfg_setting 'prose.extractor_version' = '1.1' -- the prose-extract JSON meta.extractor_version, was hardcoded EXTRACTOR_VERSION in scripts/build_programme_prose_extract.py, flagged NON-COMPLIANT by escalation #648. Part of #784's incorporation of the prose store into IBA. Module='prose' chosen over cfg_prose_chapter/cfg_prose_concept (prose's dedicated tables) because this is a tooling/runtime constant, not chapter-registry data."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision (approve / reject / revise-with-comment via `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]`)
> **related activity (set this version):** configmaint.propose
