# Session log 2026-11-21: role (config, glossary, programme prose), the project-map check

Session id: 7063fa17-e22e-4eee-831c-b96c5e1ae45e (Developer Mode)

## 1. Scope

2026-11-21. Developer Mode session. Applied the three approved config proposals (#2519, #2521, #2522); finished #2506 (glossary entries subgroup and collection approved); built and tested the session-close check that keeps the project map current (#2516, SC17); investigated the definition and application of role and aligned it (#2524): programme prose, glossary, behaviour rule 73 and the configs; changed the engagement step so a no-bearing surface is written with the role standalone and migrated the existing nodes (#2525).

## 2. Escalations

- #2519, #2521, #2522: applied through Config-Maintenance.ps1 with their run ids, completed.
- #2506: completed (glossary entries subgroup and collection approved; role left to the researcher at that point).
- #2516: built (SC17), handed over ready_for_approval, approved by the researcher, completed.
- #2523: raised by configmaint.validate (a one-run migration left in the live folder), resolved self-correctable.
- #2524: raised; findings handed over; prose, glossary and config aligned; completed by the researcher; the researcher's messages recorded by a correction (v5).
- #2525: raised (silence nodes carried no role), the researcher ruled, built and completed.
- #2448, #2463: untouched, multi-session collection-reading work, assigned to Claude.

## 3. Files

- Code: iba/app/handlers/session_close.py (SC17), iba/app/lib/engagement.py (no-bearing role), iba/app/tools/temp_2406_engagement_test_run.py (role assertions edited, not run), iba/app/tools/temp_2525_standalone_test_run.py (new).
- Migrations (archive): iba/app/migration/archive/project_map_check_2516_v1_20261121.py, iba/app/migration/archive/role_alignment_2524_v1_20261121.py, iba/app/migration/archive/silence_nodes_standalone_2525_v1_20261121.py.
- Documents: iba/app/BUILD.md (entries 541 to 543), iba/app/USER-GUIDE.md, iba/app/GOVERNANCE.md, CLAUDE.md, iba/docs/project-map.md (moved from outputs/escalation/2510-project-map-v3-20261120.md).
- Deliverables: outputs/escalation/2524-role-record-vs-programme-prose-v1-20261121.md, outputs/escalation/2524-role-in-the-escalation-record-v1-20261121.md, outputs/escalation/2524-role-in-the-programme-prose-v1-20261121.md.
- Prose and glossary patches (archive/patches/): wa-prose-set-status-20261121T041316Z.json, wa-prose-chapter-supersede-20261121T044233Z.json, 044234Z, 044356Z, 045837Z, 054648Z, 054649Z, 054650Z, glossary-role-20261121T050000Z.json; edit files under Workflow/Programme/prose-edits/.
- Reports: Logs/compliance/COMPLIANCE-20261121-7063fa17.md, _analytics/reading-tools/node-check/node-check-20261121-v1-20261121.md.

## 4. Decisions

- Researcher: apply #2519, #2521, #2522 ("Approve all three"); recorded on #2519 v3, #2521 v3, #2522 v3 and in iba/app/BUILD.md (entry 541 onward).
- Researcher: role is updated in the programme prose and the glossary in all its nuances; rule 73 reactivated; standalone is a role and the configs that say otherwise are fixed; the glossary is Claude's to align. Recorded in cfg_behaviour_rule (rule 73 text and active), cfg_setting reading.node_roles, cfg_method_rule, cfg_column, and iba/app/migration/archive/role_alignment_2524_v1_20261121.py.
- Researcher: a surface judged standalone in a verse is written to the observation and reconsidered when the verse is re-evaluated; recorded on #2525 v2 and in iba/app/migration/archive/silence_nodes_standalone_2525_v1_20261121.py.
- Claude (self-correctable, closed): the one-run migration left in the live folder was archived; recorded on #2523 v2 and in iba/app/BUILD.md (entry 541).
- Claude: SC17 uses the disposition `no change needed: <reason>` and blocks the commit like the other checks (the design the researcher approved on #2516 v3); recorded in iba/app/BUILD.md.

## 5. Open items

- #2448: Claude, multi-session collection-reading work (design in outputs/escalation/2448-reading-by-collections-design-v2-20261110.md).
- #2463: Claude, collection analysis; also carries the older engagement test iba/app/tools/temp_2406_engagement_test_run.py, written for the merged collection aloud and unable to run, its role assertions edited and not run.
- #2486: the researcher, cross-link every claim to its collection.

## 6. Git

Branch: main. Commit 071f7cf2 (session 20261121: role defined across config, glossary and programme prose ... #2506 closed).
Push: `To https://github.com/lcilliers/Bible_Projects.git   5a04e370..071f7cf2  main -> main`.
