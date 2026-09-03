# Escalation #1388 batch — behaviour-rule delivery verification fix, pending approvals

33 individual `configmaint.propose` escalations (#1389–#1421), each `decision_required`, 
`state=raised`, `next_action=review`, assigned to Researcher. Each proposal's full 
representative description (specific to that one change) is in its own `escalation.context.full_message`.

## Approval mechanics (per escalation)

```
iba/app/ps/Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval -AnsweredBy Researcher -Resolution "..."
iba/app/ps/Escalation.ps1 -Action Update -Id <id> -NextAction approved -AnsweredBy Researcher -Resolution "..."
```

Then Claude re-runs the SAME `Config-Maintenance.ps1 -Step Propose` call with `-RunId` from the 
table below (same Table/Op/Where/Set) to actually apply the write.

## The 33 changes

| Escalation | run_id | Change |
|---|---|---|
| #1389 | `RUN-20260903_074844_493-CONFIGMAINT` | `cfg_enum` insert `{}` -> `{"name": "behaviour_rule_enforcement_status", "value": "context_delivered", "ordinal": 6, "inactive": 0}` |
| #1390 | `RUN-20260903_074846_118-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 1}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_verify_db_state_before_acting"}` |
| #1391 | `RUN-20260903_074847_240-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 2}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_confirm_output_exists_before_reporting_done"}` |
| #1392 | `RUN-20260903_074848_355-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 4}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_label_inferential_output_not_confirmed"}` |
| #1393 | `RUN-20260903_074849_579-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 11}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_default_readonly_db_connections"}` |
| #1394 | `RUN-20260903_074857_338-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 13}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_dont_assume_which_database"}` |
| #1395 | `RUN-20260903_074901_451-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 17}` -> `{"enforcement_status": "context_delivered"}` |
| #1396 | `RUN-20260903_074902_557-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 18}` -> `{"enforcement_status": "context_delivered"}` |
| #1397 | `RUN-20260903_074904_504-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 19}` -> `{"enforcement_status": "context_delivered"}` |
| #1398 | `RUN-20260903_074906_328-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 20}` -> `{"enforcement_status": "context_delivered"}` |
| #1399 | `RUN-20260903_074907_429-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 21}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_chat_items_become_escalations_same_turn; cfg_escalation.chat_routing (fuller detail, id=5, cross-referenced not duplicated)"}` |
| #1400 | `RUN-20260903_074910_919-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 22}` -> `{"enforcement_status": "context_delivered"}` |
| #1401 | `RUN-20260903_074912_220-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 23}` -> `{"enforcement_status": "context_delivered"}` |
| #1402 | `RUN-20260903_074915_303-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 24}` -> `{"enforcement_status": "context_delivered"}` |
| #1403 | `RUN-20260903_074923_102-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 25}` -> `{"enforcement_status": "context_delivered"}` |
| #1404 | `RUN-20260903_074924_359-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 27}` -> `{"enforcement_status": "context_delivered"}` |
| #1405 | `RUN-20260903_074925_532-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 28}` -> `{"enforcement_status": "context_delivered"}` |
| #1406 | `RUN-20260903_074928_998-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 29}` -> `{"enforcement_status": "context_delivered"}` |
| #1407 | `RUN-20260903_074930_066-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 31}` -> `{"enforcement_status": "context_delivered"}` |
| #1408 | `RUN-20260903_074933_394-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 33}` -> `{"enforcement_status": "context_delivered"}` |
| #1409 | `RUN-20260903_074934_473-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 34}` -> `{"enforcement_status": "context_delivered"}` |
| #1410 | `RUN-20260903_074937_714-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 36}` -> `{"enforcement_status": "context_delivered"}` |
| #1411 | `RUN-20260903_074938_770-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 37}` -> `{"enforcement_status": "context_delivered"}` |
| #1412 | `RUN-20260903_074942_158-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 38}` -> `{"enforcement_status": "context_delivered"}` |
| #1413 | `RUN-20260903_074943_882-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 39}` -> `{"enforcement_status": "context_delivered"}` |
| #1414 | `RUN-20260903_074946_403-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 40}` -> `{"enforcement_status": "context_delivered"}` |
| #1415 | `RUN-20260903_074954_413-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 42}` -> `{"enforcement_status": "context_delivered"}` |
| #1416 | `RUN-20260903_074955_428-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 47}` -> `{"enforcement_status": "context_delivered"}` |
| #1417 | `RUN-20260903_074956_586-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 54}` -> `{"enforcement_status": "context_delivered", "source": "iba/docs/flag-management-proposal-v1-20260823.md section 3b (PROSE_QUALITY flag group)"}` |
| #1418 | `RUN-20260903_074959_626-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 55}` -> `{"enforcement_status": "context_delivered", "source": "iba/app/GOVERNANCE.md D2: 'may only be inserted on explicit researcher instruction'"}` |
| #1419 | `RUN-20260903_075000_642-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 57}` -> `{"enforcement_status": "context_delivered"}` |
| #1420 | `RUN-20260903_075004_129-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 59}` -> `{"enforcement_status": "context_delivered"}` |
| #1421 | `RUN-20260903_075005_217-CONFIGMAINT` | `cfg_behaviour_rule` update `{"id": 61}` -> `{"enforcement_status": "context_delivered", "source": "memory feedback_inactive_tables_never_active_inputs"}` |

## Re-run command per row (after approval)

```powershell
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074844_493-CONFIGMAINT -Table cfg_enum -Op insert -Set '{"name": "behaviour_rule_enforcement_status", "value": "context_delivered", "ordinal": 6, "inactive": 0}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074846_118-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 1}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_verify_db_state_before_acting"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074847_240-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 2}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_confirm_output_exists_before_reporting_done"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074848_355-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 4}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_label_inferential_output_not_confirmed"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074849_579-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 11}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_default_readonly_db_connections"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074857_338-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 13}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_dont_assume_which_database"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074901_451-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 17}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074902_557-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 18}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074904_504-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 19}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074906_328-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 20}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074907_429-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 21}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_chat_items_become_escalations_same_turn; cfg_escalation.chat_routing (fuller detail, id=5, cross-referenced not duplicated)"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074910_919-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 22}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074912_220-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 23}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074915_303-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 24}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074923_102-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 25}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074924_359-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 27}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074925_532-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 28}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074928_998-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 29}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074930_066-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 31}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074933_394-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 33}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074934_473-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 34}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074937_714-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 36}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074938_770-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 37}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074942_158-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 38}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074943_882-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 39}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074946_403-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 40}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074954_413-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 42}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074955_428-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 47}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074956_586-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 54}' -Set '{"enforcement_status": "context_delivered", "source": "iba/docs/flag-management-proposal-v1-20260823.md section 3b (PROSE_QUALITY flag group)"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_074959_626-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 55}' -Set '{"enforcement_status": "context_delivered", "source": "iba/app/GOVERNANCE.md D2: 'may only be inserted on explicit researcher instruction'"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_075000_642-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 57}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_075004_129-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 59}' -Set '{"enforcement_status": "context_delivered"}'
iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId RUN-20260903_075005_217-CONFIGMAINT -Table cfg_behaviour_rule -Op update -Where '{"id": 61}' -Set '{"enforcement_status": "context_delivered", "source": "memory feedback_inactive_tables_never_active_inputs"}'
```

Full per-row rationale (why each is either a straight status flip or a status+source fix) is in 
escalation #1388's own comment history, and in each individual escalation's `context.full_message`.