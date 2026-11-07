# Escalation deep history

## #2363 — ib_observation note names 1 of 6 writers
type=task source=researcher

**v1** (2026-11-06T14:01:28Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **short description (set this version):** ib_observation note names 1 of 6 writers
> **comment (set this version):** Found during #2361 stage 1c, not caused by it. Running the older manifest test iba/app/tools/temp_2231_2232_test_run.py after the manifest change gives 12 of 13: case A2 fails ("#2231 iba row: grain set; the use names every live writer step"). cfg_table.use of ib_observation (database iba) names one of the six live writer steps in cfg_write_grant (reading.record), and not lexical.meaning, observation_enhancer.apply, lexical.relational, reading.apply and prior_capture.record. The test also re-runs the 23 October migration ib_observation_use_2231_v1_20261023.py, whose text was later replaced, so the test no longer reflects the table's current note. The question for later: bring the note in line with the rule that it names every live writer, or retire the stale check. Cases B1 to B5 (archive handling) and A3 pass, and the manifest change did not touch this.
> **context (set this version):** iba/app/tools/temp_2231_2232_test_run.py; parent #2361 stage 1c
