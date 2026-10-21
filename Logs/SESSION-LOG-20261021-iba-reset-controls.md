# Session log 2026-10-21: IBA app reset, the control documents and controls

Session id: `089851fd-e080-45a5-bb43-64281485997f` (Developer Mode, started 2026-10-21T03:38Z).

## 1. Scope

2026-10-21. In Developer Mode, the researcher opened #2177 to reset the IBA app as the project's
primary process controller.
- Rule 63 was amended (#2178).
- The control documents and controls were reviewed (#2179). Seven options were built and approved:
  - A: the control map (#2180)
  - D: stale controls retired (#2182)
  - C: replaced history out of the read path (#2183)
  - E: memory (#2184)
  - F: scoped rule delivery (#2185)
  - G: the SC15 close check (#2186)
- B, CLAUDE.md cut to pointers (#2181), is built and awaits approval.
- USER-GUIDE.md was rewritten (#2187).
- Follow-up items were raised (#2188–#2194).

No study work: the study is on hold.

## 2. Escalations

**Raised and completed:**

| Id | Title | Outcome |
|---|---|---|
| #2178 | Backlog check: hand-over for approval must say what | raised, completed (approved) |
| #2179 | Verify IBA control docs are structured against misreading | raised, completed (approved) |
| #2180 | Control map: one home per kind of control (A) | raised, completed (approved) |
| #2182 | Retire stale root controls (D) | raised, completed (approved) |
| #2183 | Replaced history out of the read path (C) | raised, completed (approved) |
| #2184 | Memory holds only what config cannot (E) | raised, completed (approved) |
| #2185 | Scope start print and compliance to the session (F) | raised, completed (approved) |
| #2186 | Session-close check of control files done properly (G) | raised, completed (approved) |

**Raised and still open:**

| Id | Title | Outcome |
|---|---|---|
| #2177 | Reset IBA app as the project's primary process controller | raised, updated; open as the umbrella (pick-up record in v12) |
| #2181 | Cut CLAUDE.md to a short entry file (B) | raised, updated; ready_for_approval with the researcher |
| #2187 | Rewrite the user guide | raised, updated; ready_for_approval with the researcher |
| #2188 | Move the 8 live instruction files into config | raised, updated; on-hold with Claude |
| #2189 | Permission settings: information for a decision | raised, updated; ready_for_approval with the researcher |
| #2190 | Study-side controls to settle when the study re-opens | raised; on-hold with the researcher |
| #2191 | Retirement check for the 36 old files in docs/ | raised; with Claude |
| #2192 | Replaced history in code comments and docstrings | raised; with Claude |
| #2193 | Copy tests must use the SQLite backup API | raised; with Claude |
| #2194 | CHARTER sections 2 and 3 describe a past state | raised; on-hold with the researcher |

## 3. Files

- **Config migrations** (each through `apply_logged`, run ids `DEVMODE-2178..2187-*`), all in
  `iba/app/migration/`:
  - `rule63_approval_handover_checks_v1_20261021.py`
  - `control_map_v1_20261021.py`
  - `claude_md_rules_to_config_v1_20261021.py`
  - `history_out_of_read_path_v1_20261021.py`
  - `devmode_rule_from_command_v1_20261021.py`
  - `memory_rules_to_config_v1_20261021.py`
  - `rule_delivery_scope_v1_20261021.py`
  - `control_file_check_v1_20261021.py`
  - `control_kinds_add_tool_usage_v1_20261021.py`
- **Code:**
  - `iba/app/lib/cfgquality.py`
  - `iba/app/lib/cfgreport.py`
  - `iba/app/lib/compliance.py`
  - `iba/app/handlers/compliance.py`
  - `iba/app/handlers/session_close.py`
  - `iba/app/handlers/configmaint.py`
  - `iba/app/ps/Compliance.ps1`
  - `iba/app/ps/Behaviour.ps1`
  - `iba/app/ps/Start-Iba.ps1`
  - `.claude/hooks/stop_check_escalation_backlog.py`
- **Control documents:**
  - `CLAUDE.md`
  - `iba/app/GOVERNANCE.md`
  - `iba/app/USER-GUIDE.md`
  - `iba/app/CHARTER.md` (§4 only)
  - `iba/app/BUILD.md` §354–§364
  - `.claude/commands/developer-mode.md`
  - `.claude/commands/start-project.md`
  - `.claude/commands/session-close.md`
  - the Claude memory folder (cut to 6 files; 339 archived)
  - `iba/docs/ps tools worksheet.xlsx`
- **History copies:** `archive/docs/`
  - `claude-md-history-to-20261021.md`
  - `governance-md-history-to-20261021.md`
  - `user-guide-md-history-to-20261021.md`
  - `readme-md-history-to-20261021.md`
  - `tasks-md-history-to-20261021.md`
  - `interaction-preferences-history-to-20261021.md`
  - `file-organisation-rules-history-to-20261021.md`
- **Archived (moved to `archive/` folders):**
  - 19 `Workflow/Instructions` files
  - 169 `iba/docs` files
  - the unused `iba/config` configurator design
  - 15 `iba/app/tools/temp_*` scripts
- **Deliverables** (`outputs/escalation/`):
  - `2179-control-documentation-structure-review-v2-20261021.md`
  - `2181-claude-md-content-homes-v1-20261021.md`
  - `2182-stale-root-controls-retired-v1-20261021.md`
  - `2184-memory-dispositions-v1-20261021.md`
  - `2189-permission-settings-information-v1-20261021.md`
- **Generated:**
  - `outputs/configs/CONFIG-REPORT-v598-20261021.md`
  - `research/discovery/file-manifest-v8-20261021.md`
  - `_analytics/cross-cluster-web/open-threads-register-v27-20261021.md`
- **Compliance:** `Logs/compliance/COMPLIANCE-20261021-089851fd.md`

## 4. Decisions

- Researcher: #2177 stays open until every element of the reset is done (#2177 v7).
- Researcher: hand-overs for approval state what is approved; interim approvals carry the
  follow-up flag (`cfg_behaviour_rule`, #2178 v4).
- Researcher: no rule in more than one document; replaced history is kept out of the read path
  (#2179 v5).
- Researcher: options A, C, D, E, F and G approved (#2180 v5, #2182 v5, #2183 v5, #2184 v5,
  #2185 v5, #2186 v5).
- Researcher: retire the second configurator and the one-off scripts; the 27 old tasks are
  superseded (#2182 v5, `iba/app/GOVERNANCE.md`).
- Researcher: the user guide is to be rewritten (#2187 v4).
- Claude: CLAUDE.md is pointers only, and its rules moved into config (`cfg_behaviour_rule`;
  `CLAUDE.md`); awaiting approval on #2181 v5.
- Claude: the governance-setting orphan check and the rule-delivery check were fixed at the shared
  code (`iba/app/lib/cfgquality.py`).
- Claude: the #2179 review is corrected to v2: `apply_session_patch.py` exists (#2179 v8).

## 5. Open items

- #2181: for the researcher to approve (CLAUDE.md and the 13 rules moved from it).
- #2187: for the researcher to approve (the user guide).
- #2189: for the researcher to decide (permission settings; the edits are the researcher's).
- #2190: parked for the researcher until the study re-opens.
- #2194: parked for the researcher (CHARTER §2 and §3).
- #2188: for Claude next session, in `/developer-mode` (the 8 instruction files into config).
- #2191: for Claude next session (the old `docs/` files).
- #2192: for Claude next session (history in code comments).
- #2193: for Claude next session (copy tests through the backup API).
- #2177: the umbrella; the full pick-up record is v12.

## 6. Git
- branch: main
- first commit: 435cedf6b75bb76ae5fdfbeefeef65f0a9a3182d
- push: `825e180a..435cedf6  main -> main` to github.com/lcilliers/Bible_Projects
