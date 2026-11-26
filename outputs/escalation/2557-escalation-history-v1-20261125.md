# Escalation deep history

## #2557 — collection.layer_check crashed: 11
type=run_error source=collection

**v1** (2026-11-25T13:17:33Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** collection.layer_check crashed: 11
> **comment (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
> **context (set this version):** {"traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\run.py\", line 152, in run_step\n    outcome: Outcome = handler(ctx)\n                       ~~~~~~~^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\handlers\\collectionbuild.py\", line 393, in layer_check\n    rep = lr.check(conn, ctx.cfg, ctx.run_id, coll, subgroup=str(ctx.params.get(\"Subgroup\", \"\")).strip() or None)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\layerreading.py\", line 1199, in check\n    exp = expected_nodes(L, item, gid, subject)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\layerreading.py\", line 335, in expected_nodes\n    name = L[\"groups\"][gid][\"name\"]\n           ~~~~~~~~~~~^^^^^\nKeyError: 11\n"}
> **tried (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
