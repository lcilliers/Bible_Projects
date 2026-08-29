# Escalation deep history

## #1018 — Mark wa_flag_type_question_link inactive in cfg_table - tod…
type=issue source=configmaint

**v1** (2026-08-29T04:32:28Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Mark wa_flag_type_question_link inactive in cfg_table - tod…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_table", "op": "update", "where": {"database": "bible_research", "name": "wa_flag_type_question_link"}, "set": {"inactive": 1, "use": "Maps quality-flag types to the catalogue questions that a raised flag should prompt. REDUNDANT (2026-08-29): all 12 rows link to questions that are status=redundant_v1/deleted=1 in wa_obs_question_catalogue, and half the flag_type_id values (36, 319) are orphaned since the 2026-08-23 flag-types reset -- the surviving ids (1, 3) only resolve by id-reuse coincidence, not a real relationship. Full review: outputs/flag-type-question-catalogue-review-20260829.md. Original note: twelve rows, all written in one run on 20 April 2026, all connecting four flag types to the Q-COV coverage question family."}, "full_message": "Mark wa_flag_type_question_link inactive in cfg_table -- todays extract-and-join review (outputs/flag-type-question-catalogue-review-20260829.md) found it structurally dead: all 12 linked questions are redundant_v1/deleted, half its flag_type_id values are orphaned, and the actual-applications table (wa_data_quality_flags) is empty. governance.tables requires tables no longer in use to be set inactive."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T04:33:03Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision -- Approve / Not-approve / Resubmit.
> **resolution (set this version):** Proposed: cfg_table.inactive=1 for wa_flag_type_question_link (bible_research), use text updated with the redundancy finding + report link. Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_053227_151-CONFIGMAINT to apply once approved. CSV already archived: Workflow/schema/bible_research/archive/wa_flag_type_question_link-20260829-053242.csv (reportkit.archive_before_write, the standard convention).

**v3** (2026-08-29T04:34:20Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted 
