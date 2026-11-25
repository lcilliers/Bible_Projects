# Session close (#1875, rebuilt #2173)

> Generated 2026-11-25T16:14:37Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `43742f37-102e-4251-b1fc-180884e2c5ca` (CLAUDE_CODE_SESSION_ID); started 2026-11-24T08:54:17Z; window base commit `0130fb3a0ec60fe509f2a9829092b9d61bbe6a21`
- compliance file: `Logs/compliance/COMPLIANCE-20261124-43742f37.md`; session log: `--`
- **open findings: 151**; cleared by disposition: 0


## Contents

- [Summary](#summary)
- [SC1](#sc1-session-and-window)
- [SC2](#sc2-spine-fatal)
- [SC3](#sc3-researchers-words-recorded)
- [SC4](#sc4-open-items-in-the-register)
- [SC5](#sc5-analysis-integrity)
- [SC6](#sc6-rule-compliance)
- [SC8](#sc8-session-log)
- [SC9](#sc9-decisions-reached-their-targets)
- [SC10](#sc10-buildmd-coverage)
- [SC12](#sc12-publish)
- sc15
- sc16
- sc17

<a id="summary"></a>
## Summary

151 open finding(s); SC3 38, SC4 13, SC6 37, SC8 1, SC10 46, SC16 12, SC17 4

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:8d5c9eec`: researcher message 2026-11-24T08:54 is too short to be matched; name where it is recorded: "developoer-mode"
- **OPEN** `SC3:a85ee533`: researcher message 2026-11-24T09:30 is too short to be matched; name where it is recorded: "Marker at creation"
- **OPEN** `SC3:0f1aa8f8`: researcher message 2026-11-24T09:31 is too short to be matched; name where it is recorded: "Approve as proposed"
- **OPEN** `SC3:60238499`: researcher message 2026-11-24T09:52 is too short to be matched; name where it is recorded: "Yes, apply it"
- **OPEN** `SC3:0ea4e302`: researcher message 2026-11-24T12:40 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:32632787`: researcher message 2026-11-24T13:38 is too short to be matched; name where it is recorded: "Yes, build it"
- **OPEN** `SC3:27984de7`: researcher message 2026-11-24T14:50 is too short to be matched; name where it is recorded: "Yes, build it"
- **OPEN** `SC3:3068f153`: researcher message 2026-11-24T14:35 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:f11e5796`: researcher message 2026-11-24T14:53 is too short to be matched; name where it is recorded: "Review diff first"
- **OPEN** `SC3:fccbfd09`: researcher message 2026-11-24T15:09 is in no escalation comment written this session: "<task-notification>
<task-id>by3k7qmm9</task-id>
<tool-use-id>toolu_01DLp8VF7zgdVqwHFDwn2tvW</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:4ca6dc7f`: researcher message 2026-11-24T15:18 is too short to be matched; name where it is recorded: "Allow, apply"
- **OPEN** `SC3:aaecfd42`: researcher message 2026-11-24T15:28 is too short to be matched; name where it is recorded: "Yes, run it"
- **OPEN** `SC3:121e07a1`: researcher message 2026-11-24T16:35 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:31abf471`: researcher message 2026-11-24T16:27 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:b838c7d8`: researcher message 2026-11-24T19:58 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:1ca479a4`: researcher message 2026-11-25T05:32 is in no escalation comment written this session: "<task-notification>
<task-id>batzvwk59</task-id>
<tool-use-id>toolu_018u6dZedoA3c3ek4mSbzGhP</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:d46a4767`: researcher message 2026-11-25T05:32 is in no escalation comment written this session: "<task-notification>
<task-id>ba0k91zcb</task-id>
<tool-use-id>toolu_013Tq9EokTFUSgoNqScVhAEk</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:40dc02c3`: researcher message 2026-11-25T05:32 is in no escalation comment written this session: "<task-notification>
<task-id>beqlgjdcv</task-id>
<tool-use-id>toolu_014W343QxPau6niSKe7PHgvh</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:de5af57d`: researcher message 2026-11-25T05:49 is too short to be matched; name where it is recorded: "Start audit"
- **OPEN** `SC3:0a23402f`: researcher message 2026-11-25T06:19 is in no escalation comment written this session: "<task-notification>
<task-id>b459dgy81</task-id>
<tool-use-id>toolu_01JfSoYWEWyrWbSKBHPdshBS</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:046d877f`: researcher message 2026-11-25T06:38 is in no escalation comment written this session: "<task-notification>
<task-id>bv2p94cg4</task-id>
<summary>Monitor event: "Wait for the loop phase table to appear"</summary>
<event>[Monitor expired after 25m w"
- **OPEN** `SC3:14df8728`: researcher message 2026-11-25T06:48 is in no escalation comment written this session: "<task-notification>
<task-id>bj39jt3g5</task-id>
<summary>Monitor event: "Wait for the second loop audit to finish"</summary>
<event>[Monitor expired after 25m "
- **OPEN** `SC3:2ab72adb`: researcher message 2026-11-25T06:53 is in no escalation comment written this session: "<task-notification>
<task-id>b7dsk2vfi</task-id>
<summary>Monitor event: "Wait for the loop audit with P8 to finish"</summary>
<event>[Monitor expired after 28m"
- **OPEN** `SC3:96db3651`: researcher message 2026-11-25T07:04 is in no escalation comment written this session: "<task-notification>
<task-id>bll091pi1</task-id>
<tool-use-id>toolu_01UpTuwvLbgwDKsAimUHfHD9</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:cbbb6df8`: researcher message 2026-11-25T07:26 is in no escalation comment written this session: "<task-notification>
<task-id>b80o82b9i</task-id>
<tool-use-id>toolu_01RFttaqzcNBwbfp1WQQxVgU</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:64ddcdf6`: researcher message 2026-11-25T07:45 is in no escalation comment written this session: "<task-notification>
<task-id>b3o681hot</task-id>
<tool-use-id>toolu_01Qna3mRPQQgviKfP4oJDwYY</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:84edef17`: researcher message 2026-11-25T07:48 is in no escalation comment written this session: "<task-notification>
<task-id>bzhkczo3n</task-id>
<tool-use-id>toolu_01J9Q1FGTGZU5dEeS9e9XkWd</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:40985016`: researcher message 2026-11-25T10:56 is in no escalation comment written this session: "<task-notification>
<task-id>bnz82m14i</task-id>
<tool-use-id>toolu_01BxsRAsA8t5u1UxfrtkMcE5</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:206df1dc`: researcher message 2026-11-25T11:09 is in no escalation comment written this session: "<task-notification>
<task-id>bouyd5sof</task-id>
<tool-use-id>toolu_01WgNZYX16buFzwVeNfBsBof</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:57ed1a5d`: researcher message 2026-11-25T11:11 is in no escalation comment written this session: "<task-notification>
<task-id>b8pv8952f</task-id>
<tool-use-id>toolu_01Y9ixDnDKd49JALxbM2pTFR</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:86bbf0d8`: researcher message 2026-11-25T11:18 is in no escalation comment written this session: "<task-notification>
<task-id>bzqsnqixw</task-id>
<tool-use-id>toolu_017kUioPTNYdCKk4LSLhW5bN</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:ef29ec78`: researcher message 2026-11-25T11:20 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:dbcce91b`: researcher message 2026-11-25T12:29 is too short to be matched; name where it is recorded: "Start the loop"
- **OPEN** `SC3:db4f045d`: researcher message 2026-11-25T12:33 is in no escalation comment written this session: "S C:\Bible_study_projects> .\iba\app\ps\Escalation.ps1 -Action Update -Id 2556 -AnsweredBy Researcher -NextAction approved -Comment "Approved." -Resolution "App"
- **OPEN** `SC3:209e9756`: researcher message 2026-11-25T13:04 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:229d467e`: researcher message 2026-11-25T13:12 is too short to be matched; name where it is recorded: "Yes, read it"
- **OPEN** `SC3:7661b9d8`: researcher message 2026-11-25T13:23 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:15aaddfb`: researcher message 2026-11-25T13:42 is too short to be matched; name where it is recorded: "Yes, apply it"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:b993eeef`: researcher message 2026-11-24T10:35 holds, defers or asks to check something; name its register item: "the main focus now must be on completing the codifying, not fixing the data. my understanding is that you are currently working on have repeatable processes tha"
- **OPEN** `SC4b:6540b787`: researcher message 2026-11-24T12:54 holds, defers or asks to check something; name its register item: "the S1 data pull: the objective is to pull data about surfaces of the collection to create the grouping. It is not necessary to pull the entire verse-lexical at"
- **OPEN** `SC4b:0ea4e302`: researcher message 2026-11-24T12:40 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:2b4f9c0e`: researcher message 2026-11-24T13:24 holds, defers or asks to check something; name its register item: "step 2. correction. the output is updating the sub group table. no json required. missing wordnet item - treat them as a subgroup on their own - still require g"
- **OPEN** `SC4b:3068f153`: researcher message 2026-11-24T14:35 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:31abf471`: researcher message 2026-11-24T16:27 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:b838c7d8`: researcher message 2026-11-24T19:58 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:0d74a86f`: researcher message 2026-11-25T05:20 holds, defers or asks to check something; name its register item: "read my instruction again.  Did I mention you should check a few items. if you roll back before you made detail notes of all the transgressions then you will no"
- **OPEN** `SC4b:618a12f6`: researcher message 2026-11-25T05:43 holds, defers or asks to check something; name its register item: "you cannot build a system from a single sentence. you will have to collate my guidance accross multiple escalations, check it against you multiple attempts to d"
- **OPEN** `SC4b:5d4349ad`: researcher message 2026-11-25T05:55 holds, defers or asks to check something; name its register item: "redo the entire audit. in each step of the code look at the expectations set by me, and look at the actual results of the method, and check that the code worked"
- **OPEN** `SC4b:7bb30170`: researcher message 2026-11-25T09:55 holds, defers or asks to check something; name its register item: "before starting coding - did you ensure that the specification is up to date with all the detail.  did you check that the prose programme correlates with the sp"
- **OPEN** `SC4b:ef29ec78`: researcher message 2026-11-25T11:20 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:03958a3c`: researcher message 2026-11-25T11:43 holds, defers or asks to check something; name its register item: "3.3 will read all the observations where multiple collections are referenced. (it is critically important that the nodes of each of the underlying observations "

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:B:1`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:4`: engaged, with no evidence
- **OPEN** `SC6:B:10`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:17`: engaged, with no evidence
- **OPEN** `SC6:B:18`: engaged, with no evidence
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:21`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: engaged, with no evidence
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:34`: engaged, with no evidence
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:40`: engaged, with no evidence
- **OPEN** `SC6:B:44`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:97`: engaged, with no evidence
- **OPEN** `SC6:B:98`: engaged, with no evidence
- **OPEN** `SC6:B:99`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:B:105`: engaged, with no evidence
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (43742f37-102e-4251-b1fc-180884e2c5ca); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/handlers/collectionbuild.py`: `iba/app/handlers/collectionbuild.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexical.py`: `iba/app/lib/lexical.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/data_corrections_2541_2542_v1_20261124.py`: `iba/app/migration/archive/data_corrections_2541_2542_v1_20261124.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/grouping_first_2538_v1_20261124.py`: `iba/app/migration/archive/grouping_first_2538_v1_20261124.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/layernext_verb_2538_v1_20261125.py`: `iba/app/migration/archive/layernext_verb_2538_v1_20261125.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/marker_at_creation_2538_v1_20261124.py`: `iba/app/migration/archive/marker_at_creation_2538_v1_20261124.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/span_correction_2551_v1_20261124.py`: `iba/app/migration/archive/span_correction_2551_v1_20261124.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/validation_in_build_2538_v1_20261124.py`: `iba/app/migration/archive/validation_in_build_2538_v1_20261124.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/Collection-Build.ps1`: `iba/app/ps/Collection-Build.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_map_handler_test_run.py`: `iba/app/tools/temp_2172_map_handler_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_register_test_run.py`: `iba/app/tools/temp_2172_register_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_rewrite_test_run.py`: `iba/app/tools/temp_2172_rewrite_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_strand_test_run.py`: `iba/app/tools/temp_2172_strand_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2206_reading_waste_test_run.py`: `iba/app/tools/temp_2206_reading_waste_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2209_rule_scope_test_run.py`: `iba/app/tools/temp_2209_rule_scope_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2273_reading_phases_test_run.py`: `iba/app/tools/temp_2273_reading_phases_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2295_scope_resolver_test_run.py`: `iba/app/tools/temp_2295_scope_resolver_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2297_2299_config_test_run.py`: `iba/app/tools/temp_2297_2299_config_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2301_rollback_method_test_run.py`: `iba/app/tools/temp_2301_rollback_method_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2305_prior_capture_test_run.py`: `iba/app/tools/temp_2305_prior_capture_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2320_analysis_phase_1_test_run.py`: `iba/app/tools/temp_2320_analysis_phase_1_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2320_rules_in_config_test_run.py`: `iba/app/tools/temp_2320_rules_in_config_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2323_deleted_and_fixes_test_run.py`: `iba/app/tools/temp_2323_deleted_and_fixes_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2326_surface_migration_test_run.py`: `iba/app/tools/temp_2326_surface_migration_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2328_reading_folder_test_run.py`: `iba/app/tools/temp_2328_reading_folder_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2329_observation_items_test_run.py`: `iba/app/tools/temp_2329_observation_items_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2361_ai_test_run.py`: `iba/app/tools/temp_2361_ai_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2361_collection_ask_test_run.py`: `iba/app/tools/temp_2361_collection_ask_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2361_group_test_run.py`: `iba/app/tools/temp_2361_group_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2361_independence_test_run.py`: `iba/app/tools/temp_2361_independence_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2388_set_group_test_run.py`: `iba/app/tools/temp_2388_set_group_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2393_export_test_run.py`: `iba/app/tools/temp_2393_export_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2406_engagement_test_run.py`: `iba/app/tools/temp_2406_engagement_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2479_phrase_members_test_run.py`: `iba/app/tools/temp_2479_phrase_members_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2503_collection_index_test_run.py`: `iba/app/tools/temp_2503_collection_index_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2507_alignment_test_run.py`: `iba/app/tools/temp_2507_alignment_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2509_grouping_test_run.py`: `iba/app/tools/temp_2509_grouping_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2525_standalone_test_run.py`: `iba/app/tools/temp_2525_standalone_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_dataset_test_run.py`: `iba/app/tools/temp_2538_dataset_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_loop_order_test_run.py`: `iba/app/tools/temp_2538_loop_order_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_old_observations_test_run.py`: `iba/app/tools/temp_2538_old_observations_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_pull_test_run.py`: `iba/app/tools/temp_2538_pull_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_scope_test_run.py`: `iba/app/tools/temp_2538_scope_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_spec_audit_run.py`: `iba/app/tools/temp_2538_spec_audit_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_stage4_input_test_run.py`: `iba/app/tools/temp_2538_stage4_input_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_subgroup_loop_test_run.py`: `iba/app/tools/temp_2538_subgroup_loop_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- **OPEN** `SC16:PowerShell:_$d="$env:TEMP\t2538";:17ac67cc`: PowerShell: $d="$env:TEMP\t2538"; failed 2 times this session: [PASS] C1: {'max_vm_ops': 1000000, 'progress_step': 1000, 'chunk': 400, 'scan_ok': ['_vpairs'], 'large_tables': ['ib_nod
- **OPEN** `SC16:Bash:_python:e29939cc`: Bash: python failed 5 times this session: /usr/bin/bash: -c: line 100: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 106: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 15: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 30: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 81: unexpected EOF while looking for matching `''
- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 3 times this session: [31;1mEscalation.ps1: [31;1mCannot validate argument on parameter 'State'. The argument "resolved" does not belong to ; Update refused, 1 problem(s):; error: next_action='ready_for_approval' requires resolution to be filled in -- the readiness check, re-confirmed at 'app
- **OPEN** `SC16:Bash:_cat:e29939cc`: Bash: cat failed 3 times this session: /usr/bin/bash: -c: line 104: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 24: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 61: unexpected EOF while looking for matching `''
- **OPEN** `SC16:Bash:_sleep:90afd348`: Bash: sleep failed 2 times this session: Blocked: sleep 100 followed by: cat "C:/Users/lerouxc/AppData/Local/Temp/claude/83b0e86d1e0e650a/43742f37-102e-4251-b1fc
- **OPEN** `SC16:Bash:_python:61e040fa`: Bash: python failed 2 times this session: Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Destructive or Unwanted Actions]
- **OPEN** `SC16:Config-Maintenance.ps1_-Step_Validate`: Config-Maintenance.ps1 -Step Validate failed 2 times this session: work package : configuration-maintenance
- **OPEN** `SC16:Collection-Build.ps1_-Action_LayerRecord`: Collection-Build.ps1 -Action LayerRecord failed 5 times this session: [31;1mInvoke-Expression: [31;1mUnexpected token 'where' in expression or statement.[0m; filled 3 of 3 rows; unfilled: []; work package : collection-build
- **OPEN** `SC16:Bash:_python:eb90f5a4`: Bash: python failed 2 times this session: KeyError: 'occurrence'
- **OPEN** `SC16:next.ps1`: next.ps1 failed 2 times this session: [31;1mInvoke-Expression: [31;1mMissing file specification after redirection operator.[0m; work package : collection-build
- **OPEN** `SC16:Escalation.ps1_-Action_Raise`: Escalation.ps1 -Action Raise failed 2 times this session: Raise refused, 2 problem(s):; Raise refused, 3 problem(s):
- **OPEN** `SC16:Collection-Build.ps1_-Action_LayerNext`: Collection-Build.ps1 -Action LayerNext failed 2 times this session: work package : collection-build

- **OPEN** `SC17:layer_reading_setting`: the stages or layers of the collection reading changed, and `iba/docs/project-map.md` did not change: cfg_setting update layer.reading; cfg_setting update layer.reading; cfg_setting update layer.reading (+1 more)
- **OPEN** `SC17:table_added`: a table added to cfg_table, and `iba/docs/project-map.md` did not change: cfg_table insert {"database": "iba", "name": "span_correction", "grain": "one row per corrected f
- **OPEN** `SC17:mechanism_task_completed`: a task completed that BUILD.md names as built this session, and `iba/docs/project-map.md` did not change: #2541 Propose the four stored-data corrections of #2533; #2556 Approve migration findings_2538 on the live db
- **OPEN** `SC17:programme_book_section`: a Programme book section the map rests on was changed, and `iba/docs/project-map.md` did not change: Programme book section 'Programme flow'; Programme book section 'The analytical grouping: collections and subgroups'; Programme book section 'The collection reading'
