# Session log -- 2026-11-26 -- #2637: refusal keys, CheckAnswer, readable view, judgement-only form

Session id: 44fa45e5-b886-40b6-9928-2c435d1a9f56 (Developer Mode)

## 1. Scope

2026-11-26. Developer Mode session on #2637 (the analytic reading package pre-coded from grouping to 3.2): X4 (every refusal keyed to a configured rule and printed in the packet), X3 (CheckAnswer), X1 (readable view), X2 (judgement-only form), the fixes of #2628 and #2621, B:20 restated as the default cheaper route; after the first close, on the researcher's approval, X6 and X7 (the Cycle command and B:138 audit), B:138 amended, and from X9 the classes G3, C4 and C1.

## 2. Escalations

- #2637: updated v12 (X4 live), v13 (X3 live), v14 (X1, X2, #2628, #2621, B:20), v15 (the researcher's messages verbatim; the B:138 run question), v16 (approval; Cycle, B:138, G3, C4, C1). Stays in-progress with Claude.
- #2628: fixed; approved by the Researcher, completed.
- #2621: fixed; approved by the Researcher, completed.

## 3. Files

- iba/app/lib/refusalrules.py (new), iba/app/lib/cycleview.py (new)
- iba/app/lib/readcommands.py, iba/app/lib/layerreading.py, iba/app/lib/layerinner.py, iba/app/lib/collectionvalidate.py, iba/app/lib/buildvalidate.py, iba/app/lib/layerloop.py
- iba/app/handlers/collectionbuild.py, iba/app/ps/Collection-Build.ps1
- iba/app/migration/archive/encode_2637_refusal_keys_v1_20261126.py, iba/app/migration/archive/encode_2637_check_answer_v1_20261126.py, iba/app/migration/archive/encode_2637_cheaper_route_v1_20261126.py, iba/app/migration/archive/encode_2637_view_and_form_v1_20261126.py, iba/app/migration/archive/encode_2637_cycle_v1_20261126.py, iba/app/migration/archive/encode_2637_g3_c4_v1_20261126.py
- iba/app/tools/temp_2637_refusal_keys_test_run.py, iba/app/tools/temp_2637_check_answer_test_run.py, iba/app/tools/temp_2637_view_form_test_run.py, iba/app/tools/temp_2637_cycle_test_run.py
- iba/app/BUILD.md (600, 601, 602, 603), iba/app/USER-GUIDE.md (8.20), iba/app/GOVERNANCE.md (section 2)
- Logs/compliance/COMPLIANCE-20261126-44fa45e5.md

## 4. Decisions

- Researcher: proceed with #2637, then X3, then complete the work under the cheaper route (#2637 v15).
- Researcher: the cheaper route is always the default: cfg_behaviour_rule 20 restated (iba/app/migration/archive/encode_2637_cheaper_route_v1_20261126.py).
- Claude, within the approved plan: X4 as the config registry of design #2637 v10 (cfg_setting layer.refusals, iba/app/lib/refusalrules.py); the read contract rules PC-01..PC-07 in cfg_method_rule (prefix RC held by inactive cluster rules) (#2637 v12).
- Claude, self-correctable: the archived X4 migration writes the registry only where it is absent, after a re-run on a copy undid the X3 registry (iba/app/migration/archive/encode_2637_refusal_keys_v1_20261126.py, #2637 v13).
- Researcher: "All approved, proceed with 2637": #2628 and #2621 approved; the B:138 run may be the live reading of the unit (cfg_behaviour_rule 138, #2637 v16).
- Claude, within the approved plan: G3 as decided (#2637 v7) and C4 conformed (cfg_method_rule IB-02; cfg_setting reading.observation_rules; #2637 v16).
- Claude: #2628 fixed at the shared function (iba/app/lib/buildvalidate.py); #2621 fixed in iba/app/lib/layerloop.py.

## 5. Open items

- #2637 (Claude): the B:138 run, the live standard-session reading of boast / boastful audited by Cycle; not built: C6, C7, C8, E1, E4, F2, F3, the K10 retry (#2637 v16); the 3.1/3.2 limit of CheckAnswer (#2637 v13).
- #2620 (Claude): waits for #2637. #2619 (Claude): on hold behind its gate.

## 6. Git

