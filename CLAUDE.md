# CLAUDE.md — entry

This file holds pointers only. It holds no rules, no state and no history: each of those has one
home, named in the control map (`cfg_control_home` in `iba/app/db/iba.db`; config report section
15 at `cfg_setting configmaint.report_path`). If something here and a home disagree, the home wins.

**The project.** A sole-researcher Bible study, by le Roux Cilliers, of how Scripture describes
the workings of the human inner being. The IBA app (`iba/app/`, database `iba/app/db/iba.db`) is
the process controller for the whole project: its rules, settings and procedures are `cfg_*` rows.
What the app is for: [`iba/app/CHARTER.md`](iba/app/CHARTER.md).

**Starting a session.**
- Standard session: run `/start-project`. It prints every active rule and setting from config,
  and the session restates them in the compliance file.
- Building or fixing the app: `/developer-mode`, as the first thing typed in a fresh session.

**Before any study work,** read `cfg_setting governance.study_status`.

**Where to look:**
- Rules: `cfg_behaviour_rule`, `cfg_escalation`, `cfg_setting` (module `governance`).
- Open items and study state: the `escalation` table (`iba\app\ps\Escalation.ps1`).
- How to run a tool: [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md).
- How config governs the code: [`iba/app/GOVERNANCE.md`](iba/app/GOVERNANCE.md).
- What changed and why, read only to assess a past state: [`iba/app/BUILD.md`](iba/app/BUILD.md).
  This file's own earlier content is at `archive/docs/claude-md-history-to-20261021.md`.
