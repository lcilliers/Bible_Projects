# Escalation deep history

## #753 — Escalation utility Refinement
type=task source=researcher related_activity= from_id=

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Escalation utility Refinement
> **comment (set this version):** the escalation utility was completely redesigned in 18-20 Aug 2026. this is first review since it has gone live. This task will serve as the entry point for all the issues and tasks that about escalation that relates to it.

This task will stay open until all the aspects covered in this note have been fully covered and signed off.


prepare an detail report of all the existing configs related to escalation utility before any changes are made

validate that all the existing configs are used, aligns with the intent, and are complete. I have already notice issues in that the new columns use does not align with the design or expectations; and are not convinced that the rules for the new functionality is actually encapsulated in the configs and comply with the governance standards.
Configs report done and filed: iba/docs/escalation-config-review-v1-20260820.md. Table/column registration and cfg_setting usage are complete and correct -- no gaps there. Four real gaps found and raised as their own item, #755 (state-machine rules not in cfg_status_flow, escalation_next_action vocabulary-merge validation gap, both reports bypass the app's reportkit/cfg_report standard entirely, one orphan write-grant) -- section 5 of the report proposes concrete fixes for your decision, nothing built yet per your "before any changes are made".

One item from your notes I can't act on without clarification: "escalation History: short-description does not comply with" cuts off mid-sentence in the notes file, no object stated -- what should it comply with?

Holding on the remaining buckets (Open-escalations report layout -- now root-caused by #755 finding 3, not a separate fix; User Guide pass) until #755's proposals are decided, so the guide describes the settled shape once, not twice.
Recording a real failure in the #755 config review, per your correction: the review checked cfg_table/cfg_column/cfg_enum/cfg_write_grant/cfg_utility/cfg_escalation/cfg_setting/cfg_report/cfg_status_flow row-by-row and reported 4 specific findings, but never asked the actual question -- is the operational rule set that governs VALIDATING and COMPLETING an escalation, and the automation that executes it, represented in config at all. It is not, almost entirely, and I did not report that.

Concretely, none of the following exist in any cfg_* table -- every one of them lives ONLY in escalation.py Python code:
- which fields are required for which action (comment required at Raise; resolution required when next_action=approved; state required as withdraw|supersede when next_action=reject; tried required when next_action_assigned_to=Claude after a failed correction) -- _check_next_action()/update()'s own inline checks
- the auto-state derivation rules AND THEIR PRIORITY ORDER (plan v3 sec3's 6-rule table, first-match-wins) -- _derive_state()
- the two-stage approval semantics (ready_for_approval -> approved -> completed) and who is allowed to set which next_action -- nowhere, just the plan doc + code
- duplicate suppression, module blocking, resolution precedence, chat routing (cfg_escalation's 7 rows DO exist for these, but per #746 they are stale and not reviewed against the redesign)

Finding 1 in #755 only flagged that cfg_status_flow (which could hold PART of this -- the status-target mapping) was empty. That is one symptom. It is not the finding that the whole validation/authorization/ordering rule engine for this module has no config representation at all -- a much larger, more fundamental gap that I should have generalised to and did not.

Governance rule violated by how I actually responded once this surfaced (checked, not guessed -- cfg_behaviour_rule id, class=development, rule_key=root-fix-not-one-off): "A defect that is an instance of a class ... is fixed at the shared mechanism so every future case is correct, not remediated case-by-case while the mechanism stays broken." The short_description migrations (round 1, round 2) and even the raise-time guardrail were exactly this -- per-item/per-symptom patches on top of a mechanism (config-driven validation) that still does not exist. The guardrail stops ONE symptom (a bad title) from recurring; it does nothing for the other undocumented, unconfigured rules above, which can drift or break silently the same way short_description did.

Next: redoing the #755 config work properly -- not table-by-table presence-checking, but an explicit inventory of every validate/complete rule this module enforces, config or code, before proposing the root-cause fix.
Config work redone properly -- full report: iba/docs/escalation-config-review-v2-20260820.md. Read every function in escalation.py line by line, catalogued every validate/complete rule against whether any cfg_* row actually drives it. Findings:

A. Field-requirement rules (comment required at Raise, resolution required at approved, state required at reject, tried required after a failed Claude correction) -- ALL hardcoded, zero config. The "tried" rule was never even implemented in code, despite being in your own v1/v2 review comments.
B. State-derivation: the TARGET VALUES are partially config-backed (cfg_status_flow, once #756 clears) but the priority-ordered branching logic itself cannot be represented in that table's schema at all (entity/status/set_by has no room for a condition or an order) -- 100% Python regardless of whether #756 is approved.
C. The two-stage approval handshake (ready_for_approval -> approved) has NO check anywhere, config or code, that the two parties are actually different people.
D. cfg_escalation's own 7 rule rows -- 2 of 7 (document_reference_grouping, half of source_classification) claim enforcement by escalation.raise_manual, a function that no longer exists anywhere in the codebase. Concrete, not just "stale" as #746 already said in general terms.
E. The root cause of the originator-misattribution bug you caught: "Researcher" as a default answered_by/originator, hardcoded in 4 separate places, zero config, zero justification -- caused >=39 misattributed rows this session including #753 v4 itself, written 2 messages before I found this.

Root-cause fix (a real config representation for these rules that code actually reads, matching how cfg_on_fail drives run.py or cfg_step drives handler resolution) is NOT built in this pass -- it needs a design, and given how this same module's last redesign went (3 review rounds before anything was built), that design should get the same treatment, not another rushed patch. Awaiting your direction before proposing one.
> **context (set this version):** Escalation functionality is supported by the following design documents 

Workflow\Chat_responses\archive\comments - escalation-system-mechanics
iba\docs\archive\escalation-redesign-plan-v1-20260818.md
iba\docs\escalation-redesign-plan-v3-20260819.md



**v2** (2026-08-21T12:54:28Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** this is the master for the escalation utility revision, this can be prepared for sign off when all the related fixes have been completed
