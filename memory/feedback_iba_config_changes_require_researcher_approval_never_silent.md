---
name: feedback_iba_config_changes_require_researcher_approval_never_silent
description: "Any change to the IBA app's cfg_* configuration must pause for explicit researcher validation/approval before it commits — never a silent/automatic DB write, even from a \"trusted\" utility; reuse the existing escalation (pause-continue) pattern, not a direct write."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T14:02:58.391Z
---

Proposed (2026-07-21) that `configuration_maintenance`'s load step be "DB-direct, no file round-trip" —
the utility validates a proposed config change and writes it straight to `cfg_*`. Researcher's verdict:
**"it is a no-no. I want to validate and be involved in any updates to the configs. These configs is
VERY important to the app, and messing it up will seriously break everything."**

**Why:** config drives every module's behaviour (rules a/d in `iba-application-design-v2`'s governing
principles); an automatic write — even one that's schema-validated — bypasses the researcher's own
judgement on whether the *content* of the change is right, and a config mistake propagates everywhere
at once, unlike an ordinary data-row mistake.

**How to apply:** any mechanism that changes `cfg_*` content must pause for explicit researcher approval
before the write commits. Reuse the app's own proven `escalation` table + `run.state` pause/resume
pattern — the same one `handlers/registry.py`'s `create()` already uses for new-word approval — rather
than inventing a new mechanism. Shape: **propose → validate → escalate (researcher answers yes/no) →
apply only on yes.** Never design or build a path where Claude Code (or any utility) can commit a
config change without that stop. Related: [[project_iba_db_is_master_over_legacy_json_seeds]],
[[feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches]].
