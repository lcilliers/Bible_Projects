# Escalation deep history

## #1010 — escalation CLI crashed: next_action='ready_for_approval' re…
type=run_error source=iba.app.lib.escalation

**v1** (2026-08-29T04:03:27Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** escalation CLI crashed: next_action='ready_for_approval' re…
> **comment (set this version):** argv=['update', '1009', '--originator=Claude', '--next-action=ready_for_approval', 'Ready for your decision -- Approve / Not-approve / Resubmit.']
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
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 706, in update
    _check_requirements(db, "ready_for_approval", originator=who, checked_action=checked_action,
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        values={"resolution": new_resolution})
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 333, in _check_requirements
    raise ValueError(r["message"])
ValueError: next_action='ready_for_approval' requires resolution to be filled in -- the readiness check, re-confirmed at 'approved' (D25).

> **context (set this version):** {"argv": ["update", "1009", "--originator=Claude", "--next-action=ready_for_approval", "Ready for your decision -- Approve / Not-approve / Resubmit."], "traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1003, in main\n    return _dispatch(cfg, db, argv)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1086, in _dispatch\n    print(\"  \" + update(cfg, db, int(argv[1]), next_action=next_action,\n                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        next_action_assigned_to=assigned_to, comment=comment, context=context,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        tried=tried, resolution=resolution,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        state=state,\n                        ^^^^^^^^^^^^\n                        originator=_require_flag(originator, \"originator\")))\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 706, in update\n    _check_requirements(db, \"ready_for_approval\", originator=who, checked_action=checked_action,\n    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        values={\"resolution\": new_resolution})\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 333, in _check_requirements\n    raise ValueError(r[\"message\"])\nValueError: next_action='ready_for_approval' requires resolution to be filled in -- the readiness check, re-confirmed at 'approved' (D25).\n", "full_message": "escalation CLI crashed: next_action='ready_for_approval' requires resolution to be filled in -- the readiness check, re-confirmed at 'approved' (D25)."}
