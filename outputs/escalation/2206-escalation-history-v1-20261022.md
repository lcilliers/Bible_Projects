# Escalation deep history

## #2206 — Cut what the routines make Claude read
type=issue source=researcher

**v1** (2026-10-21T17:23:24Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Cut what the routines make Claude read
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): "my observation is that the there is a lot of inconsistencies, redundant routines, incoherent rules still in the active processes. a) configs have a long list of incoherent notifications/warning (#2197). Remember everything you read which is not necessary/just result in an error or exception/ not coherent is a waste of real money in terms of costs and tokens.  we have spent the a lot of tokens on sorting out so far - resulting in multiple corrective actions and still I see 'failed', 'configs', long lists of rules that is being read unneccessary". Element of the #2177 reset. Claude measured the waste at this session's start and wrote 5 options.
> **context (set this version):** outputs/escalation/2177-reading-waste-options-v1-20261021.md; #2177; #2197

**v2** (2026-10-21T17:23:31Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Decision sought: approve, reject or revise each of the 5 options in outputs/escalation/2177-reading-waste-options-v1-20261021.md (1 close stale #2197 and keep validate JSON out of escalations; 2 drop permanent validate advisories; 3 compliance file holds rules only, scoped by subject; 4 escalation list shows open items, latest version only; 5 stop hook skips standing parent items). Each approved option is built as its own task under #2177, tested on a copy.

**v3** (2026-10-21T17:25:44Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): "how can I approve this if you have not even investigated why the control was there in the first place and why it now suddenly become redundant?" Claude takes #2206 back: for each of the 5 controls, trace why it was introduced (escalation, BUILD.md section, cfg row) and whether that reason still holds, before any option is put for decision again.

**v4** (2026-10-21T17:27:59Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2177-reading-waste-options-v2-20261021.md; v1 archived at outputs/escalation/archive/2177-reading-waste-options-v1-20261021.md; iba/app/handlers/configmaint.py; iba/app/BUILD.md
> **resolution (set this version):** Decision sought: approve, reject or revise options 1, 2a, 2b, 3, 4 and 5 in outputs/escalation/2177-reading-waste-options-v2-20261021.md. The file gives, per control, why it was built (escalation, BUILD.md section or commit), whether that reason still holds (it does for all but the list history, which has no ruling), and what is wasteful in how it runs now. Not for decision: configmaint.validate storing full findings in escalation.context breaks the BUILD.md sec 42 standard; Claude fixes it with option 1, since both change the same code in iba/app/handlers/configmaint.py.

**v5** (2026-10-21T17:33:57Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-21 (verbatim): "Approve options 1, 2a, 2b, 3, 4 and 5 in #2206 (v2 file); build them with the sec 42 fix."

**v6** (2026-10-21T17:33:57Z, Claude) state=in-progress next_action=approved assigned_to=Claude
> **comment (set this version):** Build started: options 1, 2a, 2b, 3, 4, 5 and the sec 42 fix, tested on a copy made with iba/app/lib/dbsnapshot.copy_db.

**v7** (2026-10-21T17:52:11Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2206-reading-waste-test-results-v1-20261021.md; outputs/escalation/2206-low-config-density-utilities-v1-20261021.md; iba/app/BUILD.md; #2207; #2208
> **resolution (set this version):** Built, tested and live (commit 1267b220, BUILD.md sec 372). Approval sought for the finished build: options 1, 2a, 3, 4, 5 and the sec 42 fix. Tests 15/15 on a copy: outputs/escalation/2206-reading-waste-test-results-v1-20261021.md. Live effect: the validate escalation went from 41,180 to 2,642 characters (#2207 replaces withdrawn #2197 and asks only the 19 findings new since #2107); unenforced list 81 to 13; compliance file 52 to 45 governance rows; escalation list 22,345 to 11,651 bytes. One change from the v2 file: option 3 leaves out 7 settings, not 9; governance.scripts_ps_dir and scripts_python_dir are read by no code, so they stay delivered (#2208). Decision also sought for option 2b: fill the per-utility table and answer Question A in outputs/escalation/2206-low-config-density-utilities-v1-20261021.md (12 utilities, not 10). Claude applies the 2b decisions after approval.

**v8** (2026-10-22T03:33:06Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** noted

**v9** (2026-10-22T03:37:10Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2207-new-config-findings-v1-20261022.md
> **resolution (set this version):** Option 2b (the 12 utilities) is now table D of outputs/escalation/2207-new-config-findings-v1-20261022.md, decided together with #2207. The earlier 2b file is archived (outputs/escalation/archive/2206-low-config-density-utilities-v1-20261021.md). Decision sought: rows D and E of that file.

**v10** (2026-10-22T03:57:49Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** noted

**v11** (2026-10-22T05:03:43Z, Claude) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Option 2b progress, carried in #2207 (BUILD.md sec 383): of the 12 utilities, batchprogressreport and lexicalenrich are retired and taggingguidance reads config; validate now lists 4 with no config (was 7 live). The remaining 4 (lexicalscope, iba/app/handlers/catalogue.py, clusterfamilyscan, scripts/backup_db_to_nas.py) and batchcontrol are decisions in outputs/escalation/2207-item2-utility-decisions-v1-20261022.md, #2207 v21. #2206 closes when those are built.

**v12** (2026-10-22T05:35:53Z, Claude) state=on-hold next_action=approved assigned_to=Claude
> **comment (set this version):** Parked with #2207 (researcher, chat 2026-10-22, verbatim: "A then 1"): the rest of option 2b is the five item-2 decisions in outputs/escalation/2207-item2-utility-decisions-v1-20261022.md, parked on #2207 v23. Done of 2b: batchprogressreport and lexicalenrich retired, taggingguidance reads config (BUILD.md sec 383).
