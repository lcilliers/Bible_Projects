# Escalation deep history

## #924 — escalation CLI crashed: an update carrying comment/context/…
type=run_error source=iba.app.lib.escalation

**v1** (2026-08-27T08:24:02Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** escalation CLI crashed: an update carrying comment/context/…
> **comment (set this version):** argv=['update', '922', '--originator=Researcher', '--next-action=review', '--assigned-to=Claude', 'Prepare an extract in a table for both research_db and IBA showing matching tables and other tables for each DB with the current active status of the cfg.table in IBA']
Traceback (most recent call last):
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 1003, in main
    return _dispatch(cfg, db, argv)
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 1086, in _dispatch
    print("  " + update(cfg, db, int(argv[1]), next_action=next_action,
                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        next_action_assigned_to=assigned_to, comment=comment, context=context,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        tried=tried, resolution=resolution,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        state=state,
                        ^^^^^^^^^^^^
                        originator=_require_flag(originator, "originator")))
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 729, in update
    _check_requirements(db, "update", originator=who, checked_action=checked_action,
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        values={"state": new_state, "comment": comment, "context": context,
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                               "tried": tried},
                               ^^^^^^^^^^^^^^^^
                        self_id=escalation_id)
                        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 336, in _check_requirements
    raise ValueError(r["message"])
ValueError: an update carrying comment/context/tried cannot leave the item at state='raised' -- move it off raised first (e.g. -State in-progress) before attaching work (D26).

> **context (set this version):** {"argv": ["update", "922", "--originator=Researcher", "--next-action=review", "--assigned-to=Claude", "Prepare an extract in a table for both research_db and IBA showing matching tables and other tables for each DB with the current active status of the cfg.table in IBA"], "traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1003, in main\n    return _dispatch(cfg, db, argv)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1086, in _dispatch\n    print(\"  \" + update(cfg, db, int(argv[1]), next_action=next_action,\n                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        next_action_assigned_to=assigned_to, comment=comment, context=context,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        tried=tried, resolution=resolution,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        state=state,\n                        ^^^^^^^^^^^^\n                        originator=_require_flag(originator, \"originator\")))\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 729, in update\n    _check_requirements(db, \"update\", originator=who, checked_action=checked_action,\n    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        values={\"state\": new_state, \"comment\": comment, \"context\": context,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                               \"tried\": tried},\n                               ^^^^^^^^^^^^^^^^\n                        self_id=escalation_id)\n                        ^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 336, in _check_requirements\n    raise ValueError(r[\"message\"])\nValueError: an update carrying comment/context/tried cannot leave the item at state='raised' -- move it off raised first (e.g. -State in-progress) before attaching work (D26).\n", "full_message": "escalation CLI crashed: an update carrying comment/context/tried cannot leave the item at state='raised' -- move it off raised first (e.g. -State in-progress) before attaching work (D26)."}
