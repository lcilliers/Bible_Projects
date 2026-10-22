# 2209 — Test results: part (b), rows 1 to 5

Escalation #2209 part (b). Test plan: `iba/app/tools/temp_2209b_layers_test_run.py`, run 2026-10-22 on a copy of iba.db made with `lib/dbsnapshot.copy_db`; compliance files written to scratch. Synthetic cases: T3, T5, T6, T12.

12/12 pass. Rule 81's text amendment was checked on a copy before the live run (DEVMODE-2209-RULE81-GENERAL-20261022; find_rule_scope_gaps 0).

| case | what | result | evidence |
|---|---|---|---|
| T1 | rows 1-2: only general rules are delivered (developer 41, standard 40) | PASS | developer 41, standard 40 |
| T2 | the start print says how many rules come at their point of use | PASS |   -- 122 more rules reach you at their point of use: the first use of an operation in a session is refused once with its rules (cfg_rule_scope, #2209) -- |
| T3 | synthetic: with no cfg_rule_scope every rule is delivered (fails open to reading) | PASS | 137 delivered |
| T4 | row 2: a compliance file with the 41 general rows passes the start check | PASS | [] |
| T5 | synthetic: a row for an operation rule is a finding (not delivered at start) | PASS | [{'key': 'B:63', 'reason': "row for a rule that is not delivered at start in this session's mode (delivered at its point of use, retired, unknown, or its condition does not hold)"}] |
| T6 | synthetic: a missing general row is a finding | PASS | [{'key': 'G:governance.escalation.scope', 'reason': 'no row for this active rule'}] |
| T7 | row 3: the close check (SC6) reads the file's rows only, so it covers the general rules | PASS | [] |
| T8 | row 4: the undelivered-conversational-rules check is gone from cfgquality, validate and the report | PASS | absent |
| T9 | row 5: Context -Id reads one escalation's files | PASS | 1 item, 7 files |
| T10 | row 5: -Id works for a parked item too (read when taken up) | PASS | #1891 |
| T11 | without -Id it still covers every open escalation | PASS | 11 of 11 |
| T12 | synthetic: an unknown id gives no item, not an error | PASS | [] |
