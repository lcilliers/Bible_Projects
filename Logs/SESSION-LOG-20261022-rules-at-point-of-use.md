# Session log — 2026-10-21/22 — rules at the point of use, reading waste cut, fix-not-count

Session id: `ac12e7c5-9668-4a70-ac93-a5627fd602c4` (Developer Mode). Close report:
`iba/app/reports/session-close-v153-20261022.md` (and its re-runs).

## 1. Scope

2026-10-21 to 2026-10-22, Developer Mode, for the #2177 reset of the IBA app:
- the reading waste cut (#2206);
- PS folder setting read by code (#2208);
- every rule linked to the operations it governs and shown at the point of use, with the start
  delivering only the 41 general rules (#2209);
- the Escalation Context path reader fixed (#2211);
- the fix-not-count method begun (#2207).

## 2. Escalations

- #2177 (task, reset parent): updated v20–v23, stays open (with Claude).
- #2197: withdrawn (stale validate findings; #2206 option 1).
- #2206: raised; options v1 sent back by the researcher, v2 approved; built (BUILD.md sec 372);
  approved. Open for option 2b, now folded into #2207 (with the researcher).
- #2207: raised by validate; made ready, then revised by the researcher; method approved; partly
  built (sec 377, 378). In progress, with Claude.
- #2208: raised; option (a) approved, built (sec 373), approved, completed.
- #2209: raised; parts (a) and (b) approved, built (sec 374, 375), approved, completed.
- #2210: raised by validate (missing write grant); resolved (self_correctable).
- #2211: raised; fixed (sec 376); resolved (self_correctable).
- #2212: raised at close (prose patches name a retired apply script), with the researcher.

## 3. Files

**Code:**
- `iba/app/handlers/configmaint.py`, `iba/app/lib/cfgquality.py`, `iba/app/lib/cfgreport.py`
- `iba/app/lib/escalation.py`, `iba/app/lib/compliance.py`, `iba/app/init.py`
- `iba/app/lib/escalationcontext.py`, `iba/app/handlers/reports.py`, `iba/app/ps/Escalation.ps1`
- `iba/app/lib/sessionwindow.py`, `iba/app/handlers/session_close.py`, `iba/app/lib/recordingpass.py`

**Hooks and settings:**
- `.claude/hooks/rules_at_point_of_use.py` (new), `.claude/hooks/stop_check_escalation_backlog.py`
- `.claude/settings.json`, `.gitignore`

**Commands:** `.claude/commands/start-project.md`, `.claude/commands/developer-mode.md`

**Docs:** `iba/app/BUILD.md` (sec 372–379), `iba/app/GOVERNANCE.md`, `iba/app/USER-GUIDE.md`

**Migrations**, all in `iba/app/migration/archive/`:
- `reading_waste_2206_v1_20261021.py`, `ps_dir_setting_2208_v1_20261021.py`
- `rule_scope_2209_v1_20261021.py`, `rule_scope_grant_2209_v1_20261021.py`
- `rule81_general_2209_v1_20261022.py`
- `fix_not_count_2207_v1_20261022.py`, `meaning_source_2207_v1_20261022.py`

**Tests** in `iba/app/tools/`: `temp_2206_reading_waste_test_run.py`, `temp_2208_ps_dir_test_run.py`,
`temp_2209_rule_scope_test_run.py`, `temp_2209b_layers_test_run.py`

**Deliverables** in `outputs/escalation/`:
- `2177-reading-waste-options-v2-20261021.md`
- `2206-reading-waste-test-results-v1-20261021.md`
- `2208-ps-dir-setting-test-results-v1-20261021.md`
- `2209-check-before-acting-v2-20261021.md`, `2209-rule-scope-test-results-v1-20261021.md`,
  `2209-layer-review-v1-20261021.md`, `2209-layers-test-results-v1-20261022.md`
- `2207-new-config-findings-v1-20261022.md`, `2207-fix-not-count-v1-20261022.md`

**Moved to archive:** `scripts/apply_session_patch.py` and the two untitled queries, now in
`scripts/archive/`.

**Compliance file:** `Logs/compliance/COMPLIANCE-20261021-ac12e7c5.md`

## 4. Decisions

**The researcher's decisions:**
- reading-waste options 1, 2a, 2b, 3, 4 and 5 approved: #2206 v5
- #2208 option (a): #2208 v4
- #2209 approved as realistic, across the board: #2209 v3
- #2209 part (a) and part (b) rows 1–5: #2209 v6; approved as built: #2209 v9
- the #2207 per-item decisions A–E: #2207 v4
- fix-not-count method parts 1–3: #2207 v7
- meaning_source option B: #2207 v11

**Self-correctable fixes, made and closed by Claude:**
- missing write grant for cfg_rule_scope: #2210 v2
- Context path reader: #2211 v3
- 16 method rules on retired steps deactivated: cfg_method_rule (DEVMODE-2209-RULE-SCOPE-20261021)
- rule 81 text amended to general-rule delivery: cfg_behaviour_rule (DEVMODE-2209-RULE81-GENERAL-20261022)

## 5. Open items

- **#2207, Claude:** the rest of the fix-not-count backlog, all carried by #2207:
  - scrap the batch monitoring (#2207);
  - retire lexicalenrich and lexicalscope (#2207);
  - taggingguidance definitions into config (#2207);
  - backup_db_to_nas constants into config (#2207);
  - catalogue config (#2207);
  - clusterfamilyscan literals (#2207);
  - 2 PS scripts through run.py (#2207);
  - 7 file renames (#2207);
  - the 13 rules not fully controlled (#2207);
  - then part 1, validate errors only (#2207);
  - `.claude/hooks/rules_at_point_of_use.py` still splits on a `;` inside quoted text, which gives a
    false first-use refusal (#2207).
  - SC16 counts a tool's designed exit 3 (`Session-Close.ps1` while findings are open) as a failure;
    it should leave designed report-stops out (#2207).
- **#2212, researcher:** how a prose patch is applied now that its script is retired.
- **#2205, researcher:** 6 spine gaps not verified against STEP, which is not running (SC2 carried).
- **#2177, Claude:** the reset parent stays open until every element is done.

## 6. Git
