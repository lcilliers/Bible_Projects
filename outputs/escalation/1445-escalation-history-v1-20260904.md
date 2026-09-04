# Escalation deep history

## #1445 — Mark wa_flag_type_question_link inactive
type=issue source=configmaint

**v1** (2026-09-04T04:41:51Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Mark wa_flag_type_question_link inactive
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_table", "op": "update", "where": {"database": "bible_research", "name": "wa_flag_type_question_link"}, "set": {"inactive": 1, "use": "Maps quality-flag types to the catalogue questions that a raised flag should prompt. REDUNDANT (2026-08-29): all 12 rows link to questions that are status=redundant_v1/deleted=1 in wa_obs_question_catalogue, and half the flag_type_id values (36, 319) are orphaned since the 2026-08-23 flag-types reset -- the surviving ids (1, 3) only resolve by id-reuse coincidence, not a real relationship. Full review: outputs/flag-type-question-catalogue-review-20260829.md. Original note: twelve rows, all written in one run on 20 April 2026, all connecting four flag types to the Q-COV coverage question family."}, "full_message": "Completing escalation #1018 (approved 2026-08-29, never actually applied -- drift found by #1444's harvest 2026-09-04): mark wa_flag_type_question_link inactive in cfg_table, all 12 linked questions are redundant_v1/deleted, half its flag_type_id values orphaned, actual-applications table (wa_data_quality_flags) empty."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-09-04T04:42:08Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Self-approved per direct researcher instruction (this chat, 2026-09-04): 'complete the update mentioned in 1018 -- this should have been done at the time and is correct to set this table to inactive.' Backlog-clearing of an already-approved-but-never-applied change, faithfully implementing the exact Where/Set #1018 v2 already specified.

**v3** (2026-09-04T04:42:35Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **resolution (set this version):** Approved -- direct researcher instruction, this chat, 2026-09-04: this should have been done at the time and is correct to set this table to inactive.

**v4** (2026-09-04T04:43:41Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Applied and verified live: cfg_table row for (bible_research, wa_flag_type_question_link) now inactive=1, use text carries the redundancy finding (12/12 rows link to redundant_v1/deleted catalogue questions, half the flag_type_id values orphaned since the 2026-08-23 reset, wa_data_quality_flags -- the actual-applications table -- empty). CONFIG-REPORT.md regenerated. This closes out #1018's original, never-applied proposal -- assigning back to you for review per your instruction.

**v5** (2026-09-04T10:50:32Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**  apply config change to wa_flag_type_link 
