# Escalation deep history

## #790 — raise_() skips cfg_escalation_requirement entirely
type=issue source=researcher related_activity=escalation-module-rebuild-20260820, found investigating #784/#787 from_id=

**v1** (2026-08-22T03:27:03Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** raise_() skips cfg_escalation_requirement entirely
> **comment (set this version):** Root-caused, not yet fixed -- needs a scope decision: (a) raise_() should call _check_requirements() and set from_id=-1 like raise_new() does, or (b) the dispatcher-tied shape is deliberately exempt from cfg_escalation_requirement, in which case that exemption needs its own recorded rule (a condition_key scoping the comment-required rule to manual raises only) rather than being an unrecorded code gap. Not fixed inline per feedback_iba_exploratory_use_logs_escalations_not_inline_fixes -- logged for triage.
> **context (set this version):** Every dispatcher-tied escalation (any pause-continue/report-stop outcome, including every configmaint.propose proposal) is created via lib/escalation.py raise_() (line 429), which never calls _check_requirements(). Only the MANUAL shape (raise_new(), line 505) calls it. Live proof: cfg_escalation_requirement has action=raise field=comment condition_key=always active=1 ('comment is required at Raise'), yet #787 (a configmaint.propose escalation) was created with comment=NULL, next_action=NULL, originator=NULL, and from_id=NULL (not the -1 no-parent sentinel escalation #773 established). raise_()'s own field dict (line 434-442) has no comment parameter at all and never sets from_id. Found investigating escalation #784 (researcher, 2026-08-22: '#787 has no comment, no next-action, and no related_activity. This is a serious deviation from escalation config rules.'). Scope: affects every dispatcher-raised escalation project-wide, not just #787.
> **related activity (set this version):** escalation-module-rebuild-20260820, found investigating #784/#787

**v2** (2026-08-22T03:40:49Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **context (set this version):** Proceed to fix this bug

**downward chain (spawned from #790):** #791

## #791 — escalation CLI crashed: next_action='approved' requires res…
type=run_error source=iba.app.lib.escalation related_activity=escalation-cli-crash from_id=790

**v1** (2026-08-22T03:39:29Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** escalation CLI crashed: next_action='approved' requires res…
> **comment (set this version):** argv=['update', '790', '--originator=Researcher', '--next-action=approved', '--assigned-to=Researcher']
Traceback (most recent call last):
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 943, in main
    return _dispatch(cfg, db, argv)
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 1009, in _dispatch
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
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 568, in update
    _check_requirements(db, "approved", originator=who, checked_action=checked_action,
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        values={"resolution": new_resolution})
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Bible_study_projects\iba\app\lib\escalation.py", line 313, in _check_requirements
    raise ValueError(r["message"])
ValueError: next_action='approved' requires resolution to be filled in (plan v3 sec3)

> **context (set this version):** {"argv": ["update", "790", "--originator=Researcher", "--next-action=approved", "--assigned-to=Researcher"], "traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 943, in main\n    return _dispatch(cfg, db, argv)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1009, in _dispatch\n    print(\"  \" + update(cfg, db, int(argv[1]), next_action=next_action,\n                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        next_action_assigned_to=assigned_to, comment=comment, context=context,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        tried=tried, resolution=resolution, related_activity=related_activity,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        state=state, from_id=int(from_id) if from_id else None,\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        originator=_require_flag(originator, \"originator\")))\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 568, in update\n    _check_requirements(db, \"approved\", originator=who, checked_action=checked_action,\n    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        values={\"resolution\": new_resolution})\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 313, in _check_requirements\n    raise ValueError(r[\"message\"])\nValueError: next_action='approved' requires resolution to be filled in (plan v3 sec3)\n", "full_message": "escalation CLI crashed: next_action='approved' requires resolution to be filled in (plan v3 sec3)"}
> **related activity (set this version):** escalation-cli-crash

## #784 — Prose Management
type=task source=researcher related_activity=Prose management root from_id=-1

**v1** (2026-08-21T16:20:44Z, Researcher) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Prose Management
> **comment (set this version):** This item describe the design and build of Prose in the project and build the management of prose into the IBA App
> **related activity (set this version):** Prose management root

**v2** (2026-08-21T16:45:13Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Extract all the files in the project that have prose in its title and save the output as a md in \research\discovery
> **context (set this version):** Prose is part of bible_research_db. This context will contain a listing of the key references about prose

**v3** (2026-08-21T16:55:42Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Extracted all files with 'prose' in the filename, project-wide (excluding .git): 269 files across 11 top-level directories, grouped by top-level dir with modified date + size. Also noted 6 directories that carry 'prose' in their own name (their contents included regardless of individual filename).
> **resolution (set this version):** iba/app/reports/... n/a -- deliverable is research/discovery/prose-files-inventory-20260821.md

**v4** (2026-08-21T17:02:31Z, Researcher) state=re-assigned next_action=review assigned_to=Researcher
> **context (set this version):** The main architecture: docs/prose-store-architecture.md

**v5** (2026-08-21T17:09:13Z, Researcher) state=re-assigned next_action=review assigned_to=Researcher
> **context (set this version):** building the programme extract: scripts/build_programme_prose_extract.py; exporting chapter for edit: scripts/export_prose_chapter_edit.py; importing a chapter into prose: scripts/import_prose_chapter_edit.py; seraching:  scripts/search_prose.py

**v6** (2026-08-21T17:16:03Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** Chapters 1 - 3 has already been rewritten for to alignthe project description with the latest methodologies and management processes. next task is to extract from IBA all configs that is related to prose. file the extract in the research\discover folder.

**v7** (2026-08-21T17:21:22Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Familiarised with docs/prose-store-architecture.md + the 4 named scripts. Extracted every cfg_* row in iba.db mentioning 'prose', split into core (prose store config: cfg_prose_chapter 7 rows, cfg_prose_concept 2 rows, cfg_utility 15 scripts, cfg_setting/cfg_behaviour_rule/cfg_content_index_exclude/cfg_write_grant/cfg_enum, plus the full prose_section-family cfg_table+cfg_column+cfg_unique catalogue) vs incidental (generic use of the word). Headline finding: ALL 15 prose-related cfg_utility scripts -- including the 4 you named -- are inactive=1 (mostly escalation #729 dormant-not-exempt, 4 also open NON-COMPLIANT under #648). Filed research/discovery (no research/discover folder exists; matches v2's own path).
> **resolution (set this version):** research/discovery/prose-config-extract-20260821.md

**v8** (2026-08-21T17:27:34Z, Claude) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** RESEARCHER INSTRUCTION (verbatim, this chat turn): 'staying in #784 you have rightly identified that the tables, columns and scripts are not incorporated in IBA. activate the 4 scripts, make them compliant, activate the tables and columns, and align it with the architecture. add this chat content to comment as the instruction.' Scope: the 4 named scripts (build_programme_prose_extract.py, export_prose_chapter_edit.py, import_prose_chapter_edit.py, search_prose.py) -> reactivate + fix cfg_setting-driven non-compliance (escalation #648); the prose_section table family (currently declared in cfg_table/cfg_column but not incorporated into IBA's operating config -- e.g. no cfg_write_grant beyond cfg_prose_chapter/cfg_prose_concept) -> incorporate; and align the whole with docs/prose-store-architecture.md. Investigating live code+config now before making changes.

**v9** (2026-08-22T02:58:30Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Full build plan filed for review before applying anything further: iba/docs/prose-store-iba-incorporation-plan-v1-20260822.md. Code (lib/prosestore.py, handlers/prose.py, ps/Prose.ps1, 4 rewritten scripts/*.py) is written and tested live (read-only verified, DB mtime unchanged) -- detailed in the plan Sec2. Config NOT yet applied: 13 approval-gated configmaint.propose changes needed (1 already raised as #787 pending, 12 not yet submitted), full literal Table/Op/Where/Set payload for every one is in the plan Sec3, so review can happen once over the whole batch rather than blind per-proposal. Note: instruction said 'use 874 to record and reference' -- read as a typo for #784 (this escalation); no #874 exists (max id 787). Awaiting: (1) confirm the 874/784 reading, (2) review Sec3 payloads, (3) decide whether I self-answer the 13 AnswerRuns or you do.
> **resolution (set this version):** iba/docs/prose-store-iba-incorporation-plan-v1-20260822.md

**v10** (2026-08-22T03:25:12Z, Claude) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** RESEARCHER INSTRUCTION (verbatim, this chat turn): '#787 has no comment, no next-action, and no related_activity. This is a serious deviation from escalation config rules. the plan should include the actual wording of the configs you will be adding, and a clear indication of the clode [code] changes to make to respond to it. your plan language and use of words and description is not easy to read, has a lot of things I need to read 5 times before I really understand. do not reference something and force me to go and look it up to investigate it. Note that prose management is not a utility, it is a full scale module of the project. You need to cross read the architecture to ensure that all the rules of the architecture is built into the configs. this is a governance rule by itself. every time you suggest to not do something, or decide to do it, quote the governance rule you are complying or the missing governance rule. Add this instruction in 784'. Actions required: (1) investigate #787's missing comment/next_action/related_activity as a possible escalation-module deviation, (2) rewrite the plan doc self-contained/plain-language with full literal config wording + matching code diffs inline, (3) re-treat 'prose' as a full module not a utility per governance.module.config, (4) audit docs/prose-store-architecture.md's rules against cfg_* coverage (governance.rules_must_be_config_driven) and report gaps, (5) cite the specific governance rule for every do/don't decision going forward.

**v11** (2026-08-22T03:30:09Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Plan rewritten as v2 (iba/docs/prose-store-iba-incorporation-plan-v2-20260822.md), v1 superseded not deleted. Fixes applied per your feedback: (1) #787's missing comment/next_action/related_activity root-caused as a real code bug in lib/escalation.py raise_() -- never calls _check_requirements(), affects every dispatcher-raised escalation project-wide -- raised properly as escalation #790 (quoted in full inline in the plan, not just referenced). (2) Every config item now shows literal wording + plain-English meaning + the exact code line reading it + the governance rule it satisfies, together, not spread across sections. (3) Language simplified throughout -- short sentences, no forced cross-referencing. (4) Corrected: prose is a module not a utility -- Part B compares prose against real modules (candidate/cluster/lexicon/passage: kind=operations, write grants, status flow) and shows what I built is only the read-side reporting layer; the actual prose_section WRITE path (apply_session_patch.py) has zero IBA registration at all. (5) Architecture cross-read done -- 5 explicit rules from docs/prose-store-architecture.md (status CHECK values, author CHECK values, session_a_replace exception, two-patch pattern, supersede-only discipline) checked one by one against cfg_status_flow/cfg_enum/cfg_method_rule -- none found in config, all flagged as governance.rules_must_be_config_driven deviations. Held back proposing cfg_work_package/cfg_step (items 9-13) pending your direction on B3/B4's scope, rather than locking in a shape that might be wrong.
> **resolution (set this version):** iba/docs/prose-store-iba-incorporation-plan-v2-20260822.md

**v12** (2026-08-22T03:39:02Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Fixed per your instruction: (a) memory updated -- feedback_escalation_links_go_in_context_not_resolution.md, cfg_column's own definition of context ('plus links to external documents', cumulative) vs resolution ('what was actually done', required at approved) quoted verbatim so this doesn't drift again. (b) the 4 links that were sitting only in resolution across v3/v7/v9/v11 are now in this update's context, cumulative so nothing already there is lost.
> **context (set this version):** Deliverable links, surfaced here per researcher correction (2026-08-22: links belong in context, not resolution -- previously only in resolution on v3/v7/v9/v11): v3 -> research/discovery/prose-files-inventory-20260821.md (prose-named files list). v7 -> research/discovery/prose-config-extract-20260821.md (IBA config extract). v9 -> iba/docs/prose-store-iba-incorporation-plan-v1-20260822.md (build plan, superseded by v2). v11 (current) -> iba/docs/prose-store-iba-incorporation-plan-v2-20260822.md (build plan, current).

**downward chain (spawned from #784):** #785, #786

## #787 — New cfg_setting 'prose.extractor_version' = '1.1' - the pro…
type=config source=configmaint related_activity=configmaint.propose from_id=

**v1** (2026-08-21T17:38:14Z, ?) state=raised next_action= assigned_to=Researcher
> **short description (set this version):** New cfg_setting 'prose.extractor_version' = '1.1' - the pro…
> **context (set this version):** {"table": "cfg_setting", "op": "insert", "where": {}, "set": {"value": "\"1.1\"", "use": "prosestore.extract's JSON meta.extractor_version -- escalation #648 compliance fix, was a module-level constant in build_programme_prose_extract.py", "module": "prose"}, "full_message": "New cfg_setting 'prose.extractor_version' = '1.1' -- the prose-extract JSON meta.extractor_version, was hardcoded EXTRACTOR_VERSION in scripts/build_programme_prose_extract.py, flagged NON-COMPLIANT by escalation #648. Part of #784's incorporation of the prose store into IBA. Module='prose' chosen over cfg_prose_chapter/cfg_prose_concept (prose's dedicated tables) because this is a tooling/runtime constant, not chapter-registry data."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision (approve / reject / revise-with-comment via `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]`)
> **related activity (set this version):** configmaint.propose

## #785 — Prose Management
type=task source=researcher related_activity=Prose management root from_id=784

**v1** (2026-08-21T16:21:18Z, Researcher) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Prose Management
> **comment (set this version):** This item describe the design and build of Prose in the project and build the management of prose into the IBA App
> **related activity (set this version):** Prose management root

**v2** (2026-08-21T16:36:48Z, Researcher) state=withdraw next_action=reject assigned_to=Researcher
> **comment (set this version):** Duplicate of 784

## #786 — Programme Prose Chapter 4
type=task source=researcher related_activity=Prose management from_id=784

**v1** (2026-08-21T16:33:54Z, Researcher) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Programme Prose Chapter 4
> **comment (set this version):** This item will read the existing chapter 4 of the programme prose and compare it with the IBA and all its configurations and bring the prose chapter up to date
> **related activity (set this version):** Prose management
