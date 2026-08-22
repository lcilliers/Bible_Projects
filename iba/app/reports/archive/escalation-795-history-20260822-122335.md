# Escalation deep history

## #795 — Dispatcher AnswerRun collapses approve/reject/revise
type=issue source=researcher related_activity=escalation-module-rebuild-20260820, found while answering #794 from_id=794

**v1** (2026-08-22T04:42:34Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Dispatcher AnswerRun collapses approve/reject/revise
> **comment (set this version):** Researcher's design intent (2026-08-22, verbatim): task and issue [escalation types] should not be able to use this method [AnswerRun's flat approve/reject/revise decision]. Coding error reports [type=run_error] should be handled the same as issues. NOT proposing a fix myself -- filing for the researcher's own design decision per their explicit instruction: 'I am finding you are making too many code fix compromises for you to approve it yourself.'
> **context (set this version):** cfg_escalation_transition for shape='dispatcher' has only 3 rules: decision=hold -> on-hold, decision=noted -> closed, everything else (approve/reject/revise alike) -> completed (cfg_status_flow: 'dispatcher-tied answer_for_run, decision not hold/noted'). This is keyed to the dispatcher SHAPE, not to type='config' -- confirmed it also affects type='issue': run.py's _escalation_type_for() gives type='issue' to every step ending '.validate', and iba/app/handlers/reports.py's _validation_outcome() explicitly answers those with decision=approve/reject/revise via the same AnswerRun mechanism ('researcher confirmed these findings are known/acceptable' for decision=approve). type='task' (any word-scoped step) goes through the identical pause-continue path too, so is presumed to have the same exposure, not yet directly confirmed with a live example. Separately: Update() and Correction() both explicitly refuse any dispatcher-tied item outright ('answer it via AnswerRun, not Update') -- confirmed correct, not in question here.
> **related activity (set this version):** escalation-module-rebuild-20260820, found while answering #794

**v2** (2026-08-22T04:56:26Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** the code around the types and the approval processes is not yet consistent and effective. I am in two minds around error correction. for the time being, error correction should follow the same path as issues and tasks, not configs

**downward chain (spawned from #795):** #797

## #797 — escalation CLI crashed: 'Review' is not a member of cfg_enu…
type=run_error source=iba.app.lib.escalation related_activity=escalation-cli-crash from_id=795

**v1** (2026-08-22T04:55:21Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** escalation CLI crashed: 'Review' is not a member of cfg_enu…
> **comment (set this version):** argv=['update', '795', '--originator=Researcher', '--next-action=Review', '--assigned-to=Claude', '--state=in-progress', 'the code around the types and the approval processes is not yet consistent and effective. I am in two minds around error correction. for the time being, error correction should follow the same path as issues and tasks, not configs']
Traceback (most recent call last):
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 968, in main
    return _dispatch(cfg, db, argv)
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 1034, in _dispatch
    print("  " + update(cfg, db, int(argv[1]), next_action=next_action,
                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        next_action_assigned_to=assigned_to, comment=comment, context=context,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        tried=tried, resolution=resolution, related_activity=related_activity,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        state=state, from_id=int(from_id) if from_id else None,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        originator=_require_flag(originator, "originator")))
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 574, in update
    checked_action = _check_next_action_manual(db, next_action)
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 158, in _check_next_action_manual
    raise ValueError(f"{next_action!r} is not a member of cfg_enum "
                     f"'escalation_next_action_manual' ({valid!r})")
ValueError: 'Review' is not a member of cfg_enum 'escalation_next_action_manual' (['ready_for_approval', 'approved', 'reject', 'revise', 'noted', 'review'])

> **context (set this version):** {"argv": ["update", "795", "--originator=Researcher", "--next-action=Review", "--assigned-to=Claude", "--state=in-progress", "the code around the types and the approval processes is not yet consistent and effective. I am in two minds around error correction. for the time being, error correction should follow the same path as issues and tasks, not configs"], "traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 968, in main\n    return _dispatch(cfg, db, argv)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1034, in _dispatch\n    print(\"  \" + update(cfg, db, int(argv[1]), next_action=next_action,\n                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        next_action_assigned_to=assigned_to, comment=comment, context=context,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        tried=tried, resolution=resolution, related_activity=related_activity,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        state=state, from_id=int(from_id) if from_id else None,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        originator=_require_flag(originator, \"originator\")))\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 574, in update\n    checked_action = _check_next_action_manual(db, next_action)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 158, in _check_next_action_manual\n    raise ValueError(f\"{next_action!r} is not a member of cfg_enum \"\n                     f\"'escalation_next_action_manual' ({valid!r})\")\nValueError: 'Review' is not a member of cfg_enum 'escalation_next_action_manual' (['ready_for_approval', 'approved', 'reject', 'revise', 'noted', 'review'])\n", "full_message": "escalation CLI crashed: 'Review' is not a member of cfg_enum 'escalation_next_action_manual' (['ready_for_approval', 'approved', 'reject', 'revise', 'noted', 'review'])"}
> **related activity (set this version):** escalation-cli-crash

## #794 — CORRECTION (re-raised, supersedes withdrawn #793): my own p…
type=config source=configmaint related_activity=configmaint.propose from_id=-1

**v1** (2026-08-22T04:06:07Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** CORRECTION (re-raised, supersedes withdrawn #793): my own p…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision (approve / reject / revise-with-comment via `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]`)
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"module": "prose", "value": "\"1.1\""}, "set": {"key": "prose.extractor_version"}, "full_message": "CORRECTION (re-raised, supersedes withdrawn #793): my own prior insert (run RUN-20260821_183813_600-CONFIGMAINT) dropped the 'key' field from Set, writing a cfg_setting row with key=NULL instead of key='prose.extractor_version'. This sets the missing key on that exact row, identified uniquely by value='1.1' + module='prose'. No other column changes."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision (approve / reject / revise-with-comment via `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]`)
> **related activity (set this version):** configmaint.propose

**v2** (2026-08-22T04:34:10Z, Researcher) state=completed next_action=revise assigned_to=Researcher
> **comment (set this version):** versioning is prose works differently as far as I can remember. each time a change of a section is processed, the current version is set as soft delete and the new item gets a new version number. each section runs its own versioning.  i am not sure what this version 1.1 is actually referring to

**downward chain (spawned from #794):** #795
