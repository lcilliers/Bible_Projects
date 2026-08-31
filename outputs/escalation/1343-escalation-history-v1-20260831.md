# Escalation deep history

## #1343 — Formalize Developer Mode vs App Mode operating split
type=task source=researcher

**v1** (2026-08-31T09:51:34Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Formalize Developer Mode vs App Mode operating split
> **comment (set this version):** Development task record (per the new rule itself -- every development task gets an escalation item). Design/proposal: presented in chat, approved in chat ('approved and proceed'). Build: (1) CHARTER.md sec4 written -- the two-mode definition, scope, and process. (2) GOVERNANCE.md sec69 written -- pointer + record, same content. (3) cfg_behaviour_rule row proposed (escalation #1342, pending your approval -- config content, not app mechanism, so it stays on the configmaint.propose path per the rule's own logic). Test plan: verify CHARTER.md/GOVERNANCE.md read consistently with existing text (done, no contradiction found); verify #1342's row is live and queryable once approved; real test is the next actual code fix -- no configmaint.propose gate for a code-only change, gate stays for cfg_setting/research-parameter changes.
> **context (set this version):** CHARTER.md sec4, GOVERNANCE.md sec69, escalation #1342 (cfg_behaviour_rule row, pending approval). Memory: feedback_developer_mode_vs_app_mode_operating_model.

**v2** (2026-08-31T09:55:51Z, Researcher) state=withdraw next_action=reject assigned_to=Claude
> **comment (set this version):** not approved, to be redesigned
